# Dicionário de dados — `loteria-federal.csv`

Uma linha por prêmio sorteado. 30.390 linhas válidas.

| Coluna | Tipo | Descrição |
|---|---|---|
| `concurso` | inteiro | Número do concurso da Loteria Federal (1 a 6.117). |
| `data` | texto `AAAA-MM-DD` | Data do sorteio. Vai de `1962-09-15` a `2026-11-11`. |
| `premio` | inteiro | Posição do prêmio no concurso (1 a 5). |
| `milhar` | inteiro | As quatro últimas casas do número sorteado (0 a 9999). |
| `grupo` | inteiro | Grupo do jogo do bicho (1 a 25), derivado das duas últimas casas do milhar. |

## Regra de conversão

O grupo sai das **duas últimas casas** do milhar:

| Dezena final | Grupo | Bicho |
|---|---|---|
| 01–04 | 01 | Avestruz |
| 05–08 | 02 | Águia |
| 09–12 | 03 | Burro |
| … | … | … |
| 93–96 | 24 | Veado |
| 97–00 | 25 | Vaca |

Grupo `g` cobre as dezenas `(g-1)*4+1` até `(g-1)*4+4`, com o grupo 25 fechando em `97, 98, 99, 00`.

## Registros descartados

`milhar = 0000` aparece 4 vezes. **São resultados reais** e permanecem na base: a chance de sair 0000 é a mesma de qualquer outro milhar (1 em 10.000), e 4 ocorrências em 30.390 prêmios está dentro do esperado (3,04 por azar).

Versões anteriores desta base traziam 105 registros com `000000` (seis dígitos, formato antigo de campo vazio) em concursos de digitalização ruim. Esses sim eram marcadores de dado ausente. Hoje a base publicada não os contém mais — todos os 30.390 registros têm milhar de 4 dígitos.

**Nenhuma linha é descartada no cálculo.** `scripts/stats.py` só ignora campo vazio ou zero-padding com mais de 4 dígitos, o que hoje resulta em 0 exclusões: 30.390 linhas → 30.390 prêmios.

## Lacunas da fonte

A numeração de concurso vai de 1 a 6.117, mas **6.091 concursos têm registro**:

- 26 números de concurso não aparecem na fonte digitalizada;
- 16 concursos antigos (em torno de 2.871–2.900) trazem 1 prêmio em vez de 5;
- o concurso 377 traz 4 prêmios.

Como cada prêmio é um sorteio independente de 4 dígitos, a lacuna reduz o tamanho da amostra mas não enviesa a distribuição dos 25 grupos.

## Reprodutibilidade

```bash
python3 scripts/fetch_dataset.py --out data/loteria-federal.csv
python3 scripts/stats.py --in data/loteria-federal.csv --out docs/api/
```

O segundo comando deve imprimir `chi2=20.14 p=0.6886 n=30390`. Se imprimir outro número, a base mudou — verifique antes de publicar qualquer conclusão.
