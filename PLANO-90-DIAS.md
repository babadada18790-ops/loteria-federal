# Plano de 90 dias — ordem importa mais que volume

## A regra que organiza tudo

Existem dois tipos de link:

- **Link que você cria** (perfil, diretório, espelho de dataset, pacote): custo baixo, valor baixo, escala alta. Serve para *existir* e ser encontrado, não para ganhar autoridade.
- **Link que alguém dá a você** (universidade, jornalista, professor): custo alto, valor alto, escala baixíssima. É o único que muda posição no Google.

Um site com 0 links não sobe porque apareceu no Zenodo. Sobe quando um `.edu.br` ou um veículo cita. Por isso: **as 4 primeiras semanas constroem o que se pode citar; as seguintes vão atrás de quem cita.**

Meta realista em 90 dias: **3 a 6 links editoriais reais** + 15 a 25 menções próprias (DOIS, espelhos, pacotes). Quem promete 200 links em 90 dias entrega lixo ou penalização.

---

## Fase 1 — Semanas 1–2: o que se pode citar

Sem isso, nenhum contato funciona: você não tem DOI, não tem página de dataset, não tem endereço estável para apontar.

| # | Tarefa | Tempo | Saída |
|---|---|---|---|
| 1 | Criar repo `loteria-federal` no GitHub, subir este kit, ativar Pages em `/docs` | 1h | URL pública do repo + API |
| 2 | Preencher `babadada18790-ops` nos arquivos, testar `fetch_dataset.py` + `stats.py` | 1h | `chi2=20.14 p=0.6886 n=30390` |
| 3 | Publicar release v1.0.0 no GitHub, conectar ao Zenodo, gerar DOI | 1h | DOI real |
| 4 | Trocar `XXXXXXX` pelo DOI em todos os arquivos, republicar | 30min | consistência |
| 5 | Criar `/dados` no site com a marcação `Dataset` | 2h | página indexável |
| 6 | Google Search Console: solicitar indexação de `/dados` | 10min | — |
| 7 | Atualizar o card do Hugging Face: link do DOI + link do repo + citação | 20min | cross-link |
| 8 | Instalar o widget numa página de teste e conferir | 30min | widget funcionando |

**Critério de saída da fase:** `/dados` responde 200, marcação passa no Rich Results Test sem erro, DOI resolve, e os três endereços (site, Zenodo, GitHub, HF) se apontam mutuamente.

---

## Fase 2 — Semanas 3–4: espelhos de baixo custo

Objetivo: o dado existir em mais de um lugar sob o seu nome, todos apontando para `/dados`.

| # | Tarefa | Valor | Observação |
|---|---|---|---|
| 9 | Kaggle dataset (descrição + link do DOI) | médio | público de ciência de dados, algum tráfego |
| 10 | Figshare (DOI próprio, `related` ao Zenodo) | baixo | mais um DOI citável |
| 11 | Mendeley Data | baixo | indexado no Discovery |
| 12 | PyPI: `pip install bicho-hoje` (cliente da API) | baixo | página de pacote com homepage |
| 13 | npm: publicar o widget | baixo | distribuição via CDN, não link |
| 14 | PR em `awesome-brazil-data` e similares | médio | exige que o repo tenha README decente — tem |
| 15 | Software Heritage: arquivar o repo | baixo | persistência, não link |

**Não faça nesta fase:** Wikidata (ver `wikidata/NOTAS.md`), Wikipédia, diretórios pagos, "50 sites para cadastrar seu link".

---

## Fase 3 — Semanas 5–8: pré-print e o pacote de figuras

| # | Tarefa | Saída |
|---|---|---|
| 16 | Escrever o estudo como paper de 8–12 páginas (Introdução, Dados, Método, Resultados, Discussão, Referências) | PDF |
| 17 | Publicar no SocArXiv (OSF Preprints) — grátis, DOI imediato, colhido pelo BASE/CORE | DOI de pre-print |
| 18 | Produzir as 5 figuras do pacote (`outreach/modelos-email.md`) | pasta pública |
| 19 | Enviar Modelo A para as 5 páginas `.edu.br` | 5 e-mails |
| 20 | Enviar Modelo C para 4 docentes de estatística | 4 e-mails |
| 21 | Follow-up único em todos, 7 dias depois | — |

**Sobre arXiv:** a categoria mais próxima seria `stat.AP` ou `stat.OT`, mas exige endosso de alguém já publicado. Sem endosso, **SocArXiv é o caminho** — mesmo DOI, sem barreira, e é colhido pelos mesmos agregadores. Não perca semana tentando endosso.

---

## Fase 4 — Semanas 9–12: imprensa e comunidade

| # | Tarefa | Observação |
|---|---|---|
| 22 | Enviar Modelo B para 6 jornalistas de dados | não mandar para editoria de loteria |
| 23 | Post no R-bloggers (se fizer a versão em R do teste) | agregador com link real, público estatístico |
| 24 | Notebook Colab + Observable com o teste reproduzível | superfície de descoberta, bom para docentes |
| 25 | 2 respostas úteis em Cross Validated / Stack (sem link no primeiro post) | tráfego, não link |
| 26 | 1 post em comunidade brasileira de dados (r/datasciencebr, Telegram de dados abertos) | divulgação do DOI |
| 27 | Publicar 1 página de conteúdo respondendo "qual grupo do bicho mais sai" com o estudo | vira o alvo natural de citação |

**Sobre release em PRLog/OpenPR/IssueWire:** publique no máximo **um**, só no dia do DOI. Esses sites são vizinhos de link farm, quase não são lidos e vários são `nofollow`. Não é caminho de crescimento, é registro.

---

## O que fazer todo dia (15 min)

1. `site:bicho-hoje.com` no Google — conferir indexação das páginas novas.
2. Search Console — erros de rastreamento, consultas novas com impressão.
3. Responder qualquer resposta de e-mail **no mesmo dia**. Taxa de conversão cai pela metade a cada dia de atraso.

## O que medir toda semana (planilha)

| Métrica | Onde | Meta 90 dias |
|---|---|---|
| Domínios de referência | Search Console → Links | 6 a 10 |
| Links editoriais (`.edu.br` / imprensa) | manual | 3 a 6 |
| Páginas indexadas | Search Console | +40% |
| Cliques orgânicos/semana | Search Console | base + 50% |
| Citações do DOI | Google Scholar / OpenAlex | ≥ 1 |
| Downloads do dataset | HF + Zenodo | 100+ |

## Os três erros que vão custar os 90 dias

1. **Trocar ordem.** Sair mandando e-mail antes de ter DOI e `/dados` — o destinatário clica, não acha nada citável, não responde. Foi o que aconteceu na rodada anterior.
2. **Pedir link.** Todo modelo aqui entrega algo; nenhum pede. No minuto em que o texto vira "poderia me dar um link", a taxa de resposta volta a 1/30.
3. **Contar espelhos como vitória.** Postar em 12 plataformas dá sensação de progresso e não move uma posição. Se a semana 10 chegar sem nenhum `.edu.br` ou jornalista, o problema não é volume de espelho — é o texto do e-mail.
