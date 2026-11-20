# Marcação schema.org/Dataset — colar na página `/dados`

O Google Dataset Search **só indexa** uma página que (a) tenha marcação `Dataset` válida e (b) seja rastreável. A marcação precisa ficar na página que **é** a landing page do dataset — não na home, não no artigo do blog, não num JSON solto.

## Passo 1 — criar a página

Crie `https://bicho-hoje.com/dados` (pode ser `/pt/dados`, tanto faz). Conteúdo mínimo: o que é a base, período, método, licença, botão de download do CSV, link do Zenodo, link do Hugging Face, bloco "como citar".

Essa página vira o alvo de todo o resto. Sem ela, não existe dataset para o Google.

## Passo 2 — colar isto no `<head>`

Troque `XXXXXXX` pelo número real do DOI depois de publicar no Zenodo.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Dataset",
  "name": "Loteria Federal — Grupos do Jogo do Bicho (1962–2026)",
  "description": "30.390 prêmios válidos da Loteria Federal (concursos 1 a 6.117, 1962–2026) convertidos nos 25 grupos do jogo do bicho. Teste de aderência do qui-quadrado: χ² = 20,14, 24 graus de liberdade, p = 0,69 — distribuição compatível com uniformidade; nenhum grupo é 'quente'.",
  "url": "https://bicho-hoje.com/dados",
  "identifier": "https://doi.org/10.5281/zenodo.24403509",
  "license": "https://creativecommons.org/licenses/by/4.0/",
  "isAccessibleForFree": true,
  "datePublished": "2026-11-21",
  "dateModified": "2026-11-21",
  "version": "1.0.0",
  "inLanguage": "pt-BR",
  "keywords": ["loteria federal", "jogo do bicho", "estatística", "qui-quadrado", "dados abertos"],
  "creator": {
    "@type": "Organization",
    "name": "Bicho Hoje",
    "url": "https://bicho-hoje.com"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Bicho Hoje",
    "url": "https://bicho-hoje.com"
  },
  "temporalCoverage": "1962-09-15/2026-11-11",
  "spatialCoverage": {
    "@type": "Place",
    "name": "Brasil"
  },
  "measurementTechnique": "Teste de aderência do qui-quadrado (χ²=20,14; gl=24; α=0,05)",
  "variableMeasured": [
    { "@type": "PropertyValue", "name": "concurso", "description": "Número do concurso da Loteria Federal" },
    { "@type": "PropertyValue", "name": "data", "description": "Data do sorteio (AAAA-MM-DD)" },
    { "@type": "PropertyValue", "name": "premio", "description": "Posição do prêmio no concurso (1 a 5)" },
    { "@type": "PropertyValue", "name": "milhar", "description": "Quatro últimas casas do número sorteado" },
    { "@type": "PropertyValue", "name": "grupo", "description": "Grupo do jogo do bicho (1 a 25)" }
  ],
  "distribution": [
    {
      "@type": "DataDownload",
      "name": "CSV completo",
      "encodingFormat": "text/csv",
      "contentUrl": "https://raw.githubusercontent.com/babadada18790-ops/loteria-federal/main/data/loteria-federal.csv"
    },
    {
      "@type": "DataDownload",
      "name": "API JSON — frequência dos 25 grupos",
      "encodingFormat": "application/json",
      "contentUrl": "https://babadada18790-ops.github.io/loteria-federal/api/estatisticas.json"
    }
  ],
  "citation": "Bicho Hoje (2026). Loteria Federal — Grupos do Jogo do Bicho (1962–2026). Zenodo. https://doi.org/10.5281/zenodo.24403509",
  "sameAs": [
    "https://doi.org/10.5281/zenodo.24403509",
    "https://huggingface.co/datasets/dada1991/loteria-federal-grupos-jogo-do-bicho",
    "https://github.com/babadada18790-ops/loteria-federal"
  ]
}
</script>
```

## Passo 3 — verificar

1. https://search.google.com/test/rich-results — cole a URL de `/dados`, confirme que detecta `Dataset` sem erro.
2. https://validator.schema.org — confirme que não há propriedade inválida.
3. Google Search Console → Sitemaps: a `/dados` precisa estar no sitemap. Peça indexação em Inspeção de URL → Solicitar indexação.
4. Dataset Search leva de dias a semanas para refletir. Não fique reenviando.

## Erros que anulam a marcação

- `distribution` apontando para uma página HTML que não baixa arquivo.
- `license` ausente ou apontando para a home.
- Marcação em página `noindex`.
- JSON-LD duplicado na mesma página (dois blocos `Dataset` com `name` diferente).
- `contentUrl` que retorna 403/404 quando o crawler acessa (teste em aba anônima, sem login).

## Detalhe que quase todo mundo erra

`identifier` **não** é o DOI em texto puro: use a URL `https://doi.org/...`. E `sameAs` deve repetir a mesma URL canônica. Se o DOI e o `sameAs` divergirem, o Dataset Search trata como dois registros.
