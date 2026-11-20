# Wikidata — leia antes de criar

## Conclusão primeiro

**Não crie o item agora.** Espere ter uma citação independente (uma matéria, um trabalho acadêmico, uma página de universidade). Motivos:

1. **Critério de notoriedade (WD:N).** Um item precisa ser descrito por uma fonte séria e publicamente disponível que seja independente do sujeito. Um DOI no Zenodo publicado por você mesmo é fonte primária, não independente. Item criado hoje tende a ser proposto para eliminação em dias — e isso deixa um rastro público negativo bem no seu nome.
2. **Link do Wikidata é `nofollow`.** Zero valor de SEO. O ganho é só de entidade/descoberta.
3. Custo de esperar: nenhum. O item pode ser criado em qualquer momento, em 5 minutos.

## Quando criar

Quando existir **pelo menos uma** destas:

- uma matéria de veículo com redação própria citando o estudo;
- uma página de universidade (`.edu.br`) listando a base em "links úteis" ou material de curso;
- um artigo acadêmico ou pré-print de terceiro citando o DOI.

Aí a fonte independente existe, e o item se sustenta.

## Rascunho pronto (para o dia em que for criar)

Propriedades mínimas para um item de dataset:

| Propriedade | Valor |
|---|---|
| Label (pt) | Base de grupos do jogo do bicho da Loteria Federal (1962–2026) |
| Description (pt) | conjunto de dados estatístico sobre a Loteria Federal brasileira |
| P31 (instance of) | Q1172284 (conjunto de dados) |
| P1476 (title) | Loteria Federal — Grupos do Jogo do Bicho (1962–2026) |
| P356 (DOI) | 10.5281/zenodo.24403509 |
| P953 (full work URL) | https://bicho-hoje.com/dados |
| P123 (publisher) | Bicho Hoje *(crie o item da organização antes, se não existir)* |
| P577 (publication date) | 21 novembro 2026 |
| P275 (copyright license) | Q30942864 (CC BY 4.0) |
| P407 (language of work) | Q9309 (português brasileiro) |
| P921 (main subject) | Q185154 (jogo do bicho), Q1142263 (Loteria Federal) |
| P2699 (URL) | https://bicho-hoje.com/dados |
| P1343 (described by source) | *a fonte independente — obrigatório* |

`P1343` sem uma fonte independente real é o que faz o item cair. Preencha por último, com a matéria que existir de fato.

## Alternativa que funciona hoje, sem risco

Se o objetivo é aparecer em bases de dados acadêmicas, o caminho é o **DataCite** (o Zenodo já deposita lá automaticamente) e o **OpenAIRE/BASE/CORE**, que colhem metadados de repositórios sozinhos. Não precisa de Wikidata para isso: publique no Zenodo com metadados completos e esses agregadores pegam em 2 a 6 semanas, sem você fazer nada.

## O que não fazer

- Não crie item para o **site** (bicho-hoje.com) — sites de conteúdo raramente passam no critério, e a tentativa fica registrada.
- Não adicione link do site nas referências de "Jogo do Bicho" (Q185154). Vai ser revertido, e a política de links externos da Wikipédia trata isso como spam.
- Não crie item duplicado se já existir um item de "Loteria Federal": a base entra como `P1343`/`P973` nele, não como item novo.
