# Loteria Federal — Grupos do Jogo do Bicho (1962–2026)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24403509.svg)](https://doi.org/10.5281/zenodo.24403509)
[![Licença: CC BY 4.0](https://img.shields.io/badge/dados-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Site](https://img.shields.io/badge/site-bicho--hoje.com-2f6f4f.svg)](https://bicho-hoje.com/blog/federal-nenhum-grupo-quente)

Base aberta e reproduzível dos **30.390 prêmios da Loteria Federal** (numeração de concurso 1 a 6.117, de 15/09/1962 a 11/11/2026; 6.091 concursos têm registro), cada um convertido em um dos **25 grupos do jogo do bicho**.

O estudo que acompanha a base aplica um **teste de aderência do qui-quadrado** e conclui que a distribuição dos 25 grupos é compatível com um sorteio uniforme:

| Item | Valor |
|---|---|
| Prêmios | 30.390 |
| Esperado por grupo | 1.215,6 |
| χ² (24 graus de liberdade) | **20,14** |
| Valor crítico a 5% | 36,42 |
| p-valor | **0,69** |

**Conclusão:** não há grupo "quente". A diferença entre o mais sorteado (Elefante, 1.277) e o menos sorteado (Cabra, 1.165) é do tamanho que o acaso produz sozinho em 30 mil sorteios.

## Conteúdo do repositório

```
data/loteria-federal.csv          base como publicada (concurso, data, premio, milhar, grupo)
data/loteria-federal-grupos.csv   a mesma base + coluna `bicho` (nome do grupo) — é o arquivo para download
data/DICIONARIO.md                dicionário de dados
scripts/fetch_dataset.py   baixa a base do Hugging Face (só biblioteca padrão)
scripts/stats.py           recalcula χ², p-valor e frequências → docs/api/
docs/api/                  JSON público, servido pelo GitHub Pages (CORS aberto)
docs/widget/               widget embutível em 1 linha
site/dados.html            página /dados pronta (JSON-LD embutido, gráfico, tabela, BibTeX)
site/dataset-jsonld.md     só a marcação schema.org/Dataset, se preferir colar em outra página
site/llms.txt              resumo para crawlers de IA (GEO)
site/COMO-PUBLICAR.md      passo a passo de publicação + Zenodo + Search Console
wikidata/NOTAS.md          rascunho de item Wikidata + quando (não) criar
```

## Reproduzir

```bash
python3 scripts/fetch_dataset.py --out data/loteria-federal.csv
python3 scripts/stats.py --in data/loteria-federal.csv --out docs/api/
```

Saída esperada: `chi2=20.14 p=0.6886 n=30390`.

## API pública (JSON, somente leitura, CORS `*`)

| Endpoint | O que devolve |
|---|---|
| `https://babadada18790-ops.github.io/loteria-federal/api/estatisticas.json` | frequência dos 25 grupos + teste |
| `https://babadada18790-ops.github.io/loteria-federal/api/ultimo.json` | último resultado publicado |

Sem chave, sem cadastro, sem limite conhecido. Se for usar em produção, prefira guardar em cache de 5 minutos.

## Widget (1 linha, sem dependências)

```html
<script src="https://cdn.jsdelivr.net/gh/babadada18790-ops/loteria-federal@main/docs/widget/bicho-widget.js"
        data-bicho-hoje defer></script>
```

Renderiza o último resultado com o crédito "Fonte: Bicho Hoje". Não exige link de volta seguido — **nofollow é bem-vindo**, o objetivo é que o dado circule com a fonte correta.

## Como citar

```bibtex
@dataset{bichohoje_federal_2026,
  title     = {Loteria Federal --- Grupos do Jogo do Bicho (1962--2026)},
  author    = {{Bicho Hoje}},
  year      = {2026},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.24403509},
  url       = {https://bicho-hoje.com/blog/federal-nenhum-grupo-quente}
}
```

## Notas de método

- O milhar são as quatro últimas casas do prêmio; o grupo vem das duas últimas (00 → grupo 25).
- **Nenhum prêmio foi descartado.** Números terminados em `0000` são resultados reais e continuam na base: aparecem 4 vezes, contra 3,04 esperadas por azar — dentro do normal. Versões anteriores desta base tratavam `0000` como dado ausente; isso estava errado e inflava artificialmente o grupo 25.
- **Lacunas da fonte:** a numeração vai de 1 a 6.117, mas 6.091 concursos têm registro. Faltam 26 números e 16 concursos antigos (≈2.871–2.900) trazem 1 prêmio em vez de 5. São falhas de digitalização, não resultados suprimidos; como cada prêmio é um sorteio independente de 4 dígitos, a lacuna reduz a amostra mas não enviesa a distribuição.
- Nenhum ajuste, filtro ou seleção de período foi aplicado depois — o resultado é o que a base dá.

## Licença

- **Dados:** CC BY 4.0 — use, redistribua e adapte, inclusive comercialmente, com crédito a Bicho Hoje e link para a fonte.
- **Código deste repositório:** MIT.

Fonte primária dos sorteios: resultados oficiais da Caixa Econômica Federal (Loteria Federal).
