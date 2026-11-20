# Como publicar a página /dados

Tudo aqui já está pronto e testado. Falta só colocar nos lugares certos e trocar dois valores.

## Passo 1 — Publicar a página

1. Copie `dados.html` para o seu site, como `https://bicho-hoje.com/dados`.
   - Se o seu servidor serve arquivos por nome, basta salvar como `dados.html` na raiz e apontar a URL `/dados` para ele (ou salvar em `dados/index.html`).
2. Copie `llms.txt` para a raiz do site: `https://bicho-hoje.com/llms.txt`.
3. A página aponta para dois arquivos que precisam existir:
   - `/dados/loteria-federal-grupos.csv` — o CSV completo (uma linha por prêmio)
   - `/dados/api/estatisticas.json` — já está pronto em `docs/api/estatisticas.json`
   - `/dados/api/ultimo.json` — já está pronto também

## Passo 2 — Publicar o dataset no Zenodo e pegar o DOI

1. Entre em https://zenodo.org e faça login com GitHub (é o caminho mais rápido).
2. `New upload` → envie o zip do dataset (o CSV + o `README.md` + `LICENSE-DATA.md`).
3. No formulário:
   - **Upload type**: Dataset
   - **Title**: `Loteria Federal — Grupos do Jogo do Bicho (1962–2026)`
   - **Creators**: Bicho Hoje (organização)
   - **License**: Creative Commons Attribution 4.0
   - **Keywords**: loteria federal, jogo do bicho, estatística, qui-quadrado, dados abertos
   - **Related identifiers**: `is supplemented by` → a URL do repositório no GitHub
4. Publique. O DOI aparece na hora, no formato `10.5281/zenodo.XXXXXXX`.

## Passo 3 — Trocar o DOI (é o único número que falta)

No `dados.html`, procure `XXXXXXX` e troque pelo número real. Aparece em 3 lugares:

- `"identifier": "https://doi.org/10.5281/zenodo.XXXXXXX"` (JSON-LD)
- o botão `DOI (Zenodo)` na seção de download
- o bloco de BibTeX

Depois faça o mesmo no `CITATION.cff`, no `.zenodo.json` e no `llms.txt`.

Uma linha para conferir que não sobrou nenhum:

```bash
grep -rn "XXXXXXX" .
```

## Passo 4 — Avisar o Google

1. **Google Search Console** → `Inspeção de URL` → cole `https://bicho-hoje.com/dados` → `Solicitar indexação`.
2. **Rich Results Test** (https://search.google.com/test/rich-results) → cole a URL → confirme que
   o tipo `Dataset` foi reconhecido sem erros. Se der erro em `distribution`, é porque o CSV ainda
   não está no ar — publique o CSV primeiro.
3. **Google Dataset Search** (https://datasetsearch.research.google.com) — não tem cadastro: ele
   acha sozinho depois da indexação. Costuma levar de 3 dias a 3 semanas.
4. Adicione o link `Ver dados abertos →` na home e nos artigos que usam a base. Página órfã não
   é rastreada direito.

## Passo 5 — Verificar que está tudo certo

```bash
# a página responde
curl -sI https://bicho-hoje.com/dados | head -1

# o JSON-LD está válido
curl -s https://bicho-hoje.com/dados | grep -o 'application/ld+json'

# o CSV existe e tem o cabeçalho certo
curl -s https://bicho-hoje.com/dados/loteria-federal-grupos.csv | head -1
```

O CSV precisa ter exatamente este cabeçalho:

```
concurso,data,premio,milhar,grupo,bicho
```

## Detalhes que costumam dar errado

- **`/dados` e `/dados/` são URLs diferentes.** O `url` no JSON-LD e o `canonical` têm que bater
  exatamente com a URL final, incluindo ou não a barra. Escolha uma e use sempre ela.
- **A marcação não pode ficar na home.** O Google Dataset Search exige que o `Dataset` esteja na
  página que é a landing page do próprio dataset. Na home, ele ignora.
- **Não coloque o JSON-LD num arquivo `.json` solto** e referencie por link: tem que estar no HTML,
  dentro do `<head>`.
- **Se você usa PocketBase** para servir os estáticos (como no seu caso), lembre que ele não lê
  `_headers`; para o HTML não faz diferença, mas se o CSV precisar de `Content-Type: text/csv`,
  quem define é o PocketBase. Teste com `curl -sI` e veja o `content-type` retornado.
