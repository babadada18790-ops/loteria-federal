#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Baixa o dataset público (Hugging Face) e grava um CSV reproduzível.
Sem dependências externas: usa só a biblioteca padrão.

Uso:
    python scripts/fetch_dataset.py --out data/loteria-federal.csv
    python scripts/fetch_dataset.py --from-csv meu-arquivo.csv
"""
import argparse
import csv
import json
import sys
import time
import urllib.parse
import urllib.request

DATASET = "dada1991/loteria-federal-grupos-jogo-do-bicho"
ENDPOINT = "https://datasets-server.huggingface.co/rows"
PAGE = 100
FIELDS = ["concurso", "data", "premio", "milhar", "grupo"]


def fetch_all(dataset=DATASET, config="default", split="train"):
    offset, total, rows = 0, None, []
    while total is None or offset < total:
        query = urllib.parse.urlencode(
            {"dataset": dataset, "config": config, "split": split,
             "offset": offset, "length": PAGE}
        )
        req = urllib.request.Request(
            ENDPOINT + "?" + query,
            headers={"User-Agent": "bicho-hoje-dataset/1.0"},
        )
        with urllib.request.urlopen(req, timeout=90) as resp:
            payload = json.load(resp)
        total = int(payload.get("num_rows_total") or 0)
        batch = payload.get("rows") or []
        if not batch:
            break
        rows.extend(item["row"] for item in batch)
        offset += len(batch)
        print(f"  {offset}/{total}", file=sys.stderr)
        time.sleep(0.15)
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="data/loteria-federal.csv")
    ap.add_argument("--from-csv", help="já tenho o CSV, só normalizar")
    args = ap.parse_args()

    if args.from_csv:
        with open(args.from_csv, newline="", encoding="utf-8") as fh:
            rows = list(csv.DictReader(fh))
    else:
        print(f"Baixando {DATASET} ...", file=sys.stderr)
        rows = fetch_all()

    with open(args.out, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=FIELDS)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row[k] for k in FIELDS})

    print(f"OK: {len(rows)} linhas -> {args.out}", file=sys.stderr)


if __name__ == "__main__":
    main()
