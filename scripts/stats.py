#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Recalcula as estatísticas do estudo e grava JSON pronto para a API/widget.
Sem dependências externas (qui-quadrado e p-valor implementados aqui).

Uso:
    python scripts/stats.py --in data/loteria-federal.csv --out docs/api/
"""
import argparse
import csv
import json
import math
import os
from collections import Counter, defaultdict

BICHOS = [
    "Avestruz", "Águia", "Burro", "Borboleta", "Cachorro", "Cabra", "Carneiro",
    "Camelo", "Cobra", "Coelho", "Cavalo", "Elefante", "Galo", "Gato", "Jacaré",
    "Leão", "Macaco", "Porco", "Pavão", "Peru", "Touro", "Tigre", "Urso",
    "Veado", "Vaca",
]
# Grupo oficial do bicho: (primeira dezena .. quarta dezena). Grupo 25 = 97-00.
DEZENAS = {g: [f"{(g - 1) * 4 + 1 + i:02d}" for i in range(4)] for g in range(1, 25)}
DEZENAS[25] = ["97", "98", "99", "00"]


def _gser(a, x):
    ap, s, d = a, 1.0 / a, 1.0 / a
    for _ in range(2000):
        ap += 1.0
        d *= x / ap
        s += d
        if abs(d) < abs(s) * 1e-15:
            break
    return s * math.exp(-x + a * math.log(x) - math.lgamma(a))


def _gcf(a, x):
    tiny = 1e-300
    b, c, d, h = x + 1.0 - a, 1.0 / tiny, 1.0 / (x + 1.0 - a), 1.0 / (x + 1.0 - a)
    for i in range(1, 2000):
        an = -i * (i - a)
        b += 2.0
        d = an * d + b
        if abs(d) < tiny:
            d = tiny
        c = b + an / c
        if abs(c) < tiny:
            c = tiny
        d = 1.0 / d
        delta = d * c
        h *= delta
        if abs(delta - 1.0) < 1e-15:
            break
    return math.exp(-x + a * math.log(x) - math.lgamma(a)) * h


def chi2_sf(stat, df):
    """P(X >= stat) para uma qui-quadrado com df graus de liberdade."""
    if stat <= 0:
        return 1.0
    a, x = df / 2.0, stat / 2.0
    return 1.0 - _gser(a, x) if x < a + 1.0 else _gcf(a, x)


def chi2_critical(df, alpha=0.05):
    """Valor crítico por bisseção (sem tabela hardcoded)."""
    lo, hi = 0.0, 200.0
    for _ in range(200):
        mid = (lo + hi) / 2.0
        if chi2_sf(mid, df) > alpha:
            lo = mid
        else:
            hi = mid
    return round((lo + hi) / 2.0, 2)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="src", default="data/loteria-federal.csv")
    ap.add_argument("--out", dest="dst", default="docs/api/")
    args = ap.parse_args()

    counts, por_decada, milhares = Counter(), defaultdict(Counter), Counter()
    ultimo, total_bruto = {}, 0
    concursos = set()
    with open(args.src, newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            total_bruto += 1
            bruto = (row.get("milhar") or "").strip()
            # Só descarta registro ausente: campo vazio ou zero-padding com mais de
            # 4 dígitos (formato antigo). "0000" é número válido — sai no sorteio
            # com a mesma chance de qualquer outro e NÃO pode ser removido.
            if bruto == "" or (len(bruto) > 4 and set(bruto) == {"0"}):
                continue
            milhar = int(bruto)
            grupo = int(row["grupo"])
            concursos.add(int(row["concurso"]))
            counts[grupo] += 1
            milhares[milhar] += 1
            por_decada[row["data"][:3] + "0"][grupo] += 1
            chave = (row["data"], int(row["concurso"]))
            if chave >= (ultimo.get("data", ""), ultimo.get("concurso", 0)):
                ultimo = {"data": row["data"], "concurso": int(row["concurso"]),
                          "milhar": milhar, "grupo": grupo}

    total = sum(counts.values())
    df = len(counts) - 1
    esperado = total / 25.0
    chi2 = sum((counts[g] - esperado) ** 2 / esperado for g in range(1, 26))
    p = chi2_sf(chi2, df)

    grupos = []
    for g in range(1, 26):
        obs = counts[g]
        grupos.append({
            "grupo": g,
            "bicho": BICHOS[g - 1],
            "dezenas": DEZENAS[g],
            "vezes": obs,
            "percentual": round(obs * 100.0 / total, 2),
            "desvio_pct": round((obs - esperado) * 100.0 / esperado, 2),
        })
    grupos.sort(key=lambda item: item["vezes"], reverse=True)
    for pos, item in enumerate(grupos, 1):
        item["ranking"] = pos

    est = {
        "gerado_em": __import__("datetime").datetime.now(
            __import__("datetime").timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "fonte": "https://bicho-hoje.com/blog/federal-nenhum-grupo-quente",
        "dataset": "https://huggingface.co/datasets/dada1991/loteria-federal-grupos-jogo-do-bicho",
        "licenca": "CC BY 4.0",
        "periodo": "1962-09-15 a 2026-11-11",
        "concursos": ultimo.get("concurso"),
        "concursos_com_dados": len(concursos),
        "premios": total,
        "premios_brutos": total_bruto,
        "premios_descartados": total_bruto - total,
        "esperado_por_grupo": round(esperado, 1),
        "teste": {
            "nome": "qui-quadrado de aderência",
            "estatistica": round(chi2, 2),
            "graus_de_liberdade": df,
            "valor_critico_5pct": chi2_critical(df),
            "p_valor": round(p, 4),
            "conclusao": ("compatível com distribuição uniforme"
                          if chi2 < chi2_critical(df)
                          else "afasta-se da distribuição uniforme"),
        },
        "grupos": grupos,
        "milhar_mais_sorteado": {
            "milhar": milhares.most_common(1)[0][0],
            "vezes": milhares.most_common(1)[0][1],
            "milhares_distintos": len(milhares),
        },
    }

    os.makedirs(args.dst, exist_ok=True)
    with open(os.path.join(args.dst, "estatisticas.json"), "w", encoding="utf-8") as fh:
        json.dump(est, fh, ensure_ascii=False, indent=1)
    print(f"OK: chi2={est['teste']['estatistica']} p={est['teste']['p_valor']} "
          f"n={total} -> {args.dst}estatisticas.json")


if __name__ == "__main__":
    main()
