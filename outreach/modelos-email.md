# Modelos de contato — a virada de método

## Por que as 30 primeiras tentativas deram 1 resposta e 0 links

As mensagens pediam uma coisa cara: *"publique meu texto"*. Isso transfere trabalho e risco editorial para quem recebe. A resposta natural é não responder.

O contrário funciona: **você entrega a peça pronta, com a fonte creditada, e não pede nada além de usar.** Custo para o destinatário: zero. Custo para você: um gráfico já feito.

Regra de ouro dos três modelos abaixo: **nenhum pede link.** Todos entregam algo que o destinatário pode publicar hoje sem pedir permissão a ninguém.

---

## Antes de enviar: o pacote de figuras

Prepare uma pasta pública com 5 PNGs em 1600px, fundo branco, rótulos em português, licença CC BY 4.0 declarada no rodapé de cada imagem:

1. `fig1-frequencia-25-grupos.png` — barras horizontais, 25 grupos ordenados, linha tracejada na média 1.215,6.
2. `fig2-desvio-por-grupo.png` — % de desvio em relação à média, eixo de −6% a +6%.
3. `fig3-qui-quadrado.png` — curva χ² com 24 gl, área à direita de 20,14 destacada, linha em 36,42.
4. `fig4-ultima-decada.png` — 2016–2026 isolado, mostrando o líder mudando (Águia/Urso/Burro) — prova de que "quente" não se repete.
5. `fig5-milhares.png` — distribuição dos 9.499 milhares distintos, o 9932 aparecendo 11 vezes contra média 3.

Cada imagem: rodapé `Fonte: Bicho Hoje · bicho-hoje.com · CC BY 4.0`.

Link único da pasta no corpo do e-mail. Sem anexo (anexo cai em spam).

---

## Modelo A — página de "links úteis" universitária

Alvo: `ime.ufg.br/n/2490-links-uteis`, `ime.unicamp.br/~laurarifo/linksUpa.htm`, `arquimedes.nce.ufrj.br/dm/atuaria/links-uteis/`, `obecon.ufms.br/links-uteis/`, `ence.ibge.gov.br` (biblioteca).

Assunto: `Sugestão de recurso para a página de links úteis: base aberta para ensino de qui-quadrado`

> Prezados,
>
> Mantenho uma base aberta com os 30.390 prêmios da Loteria Federal (1962–2026) convertidos em grupos do jogo do bicho, com o teste de aderência do qui-quadrado aplicado: χ² = 20,14, 24 gl, p = 0,69.
>
> Uso que pode interessar a vocês: é um caso real, brasileiro e verificável para ensinar teste de aderência em disciplina de estatística básica — dados completos, teste reproduzível em duas linhas de Python, e resultado "não significativo", que é justamente o caso que os exemplos de livro nunca mostram.
>
> Base: https://bicho-hoje.com/dados
> DOI: https://doi.org/10.5281/zenodo.24403509
>
> Se fizer sentido incluir na página de links úteis, ótimo. Se preferir usar apenas como exemplo em sala, também serve — os dados são CC BY 4.0, sem restrição de uso.
>
> [nome], Bicho Hoje

Por que funciona: oferece um **caso didático**, não um pedido de divulgação. Departamento de estatística raramente tem exemplo brasileiro de χ² com n = 30 mil.

---

## Modelo B — jornalista de dados

Alvo: Núcleo Jornalismo, Agência Pública, Aos Fatos, piauí, Folha/Metrópole em editoria de dados, Brazil Journal.

Assunto: `Pauta de dados: 64 anos de Loteria Federal provam que não existe grupo "quente"`

> Olá, [nome],
>
> Um número que pode render pauta: testei os 6.117 concursos da Loteria Federal (1962–2026, 30.390 prêmios) para ver se algum dos 25 grupos do bicho realmente sai mais. Não sai. χ² = 20,14 com 24 graus de liberdade, p = 0,69 — a variação inteira cabe no acaso.
>
> O ângulo que talvez interesse: o grupo mais sorteado (Elefante) está 5,1% acima da média e o menos sorteado (Cabra) 4,2% abaixo. São 112 prêmios de diferença em 64 anos — menos de dois por ano. É o tipo de número que desmonta, com dado, o mercado de "palpite de grupo quente".
>
> Tenho 5 gráficos prontos em alta resolução, com fonte creditada e licença aberta, caso queiram publicar direto: [link da pasta]
>
> Dados e método: https://bicho-hoje.com/dados — pode reproduzir ou pedir qualquer recorte (por década, por estado, por dia da semana) que eu preparo.
>
> [nome]

Regras: **sem pedir link**, **sem anexo**, **nunca** citar que é site de resultados nos primeiros dois parágrafos. O assunto é estatística, não aposta.

---

## Modelo C — professor / material de curso

Alvo: docentes de estatística (UFG, Unicamp, UFRJ, UFMS), coordenadores de curso, autores de material didático aberto.

Assunto: `Caso real brasileiro para ensinar teste de aderência (dados abertos, reproduzível)`

> Professor(a) [nome],
>
> Se estiver montando material de teste de aderência do qui-quadrado, deixo uma sugestão de caso real:
>
> 30.390 prêmios da Loteria Federal entre 1962 e 2026, classificados em 25 categorias. Esperado 1.215,6 por categoria. Resultado: χ² = 20,14 (24 gl), p = 0,69 — não se rejeita a uniformidade. O interesse pedagógico está no "não rejeita": mostra que ausência de significância também é resultado, e que 5% de diferença aparente em 30 mil observações é ruído.
>
> Dados em CSV, dicionário de variáveis e o script do teste (Python, só biblioteca padrão, sem instalar nada): https://bicho-hoje.com/dados
>
> Licença CC BY 4.0. Se quiser adaptar para slides ou lista de exercícios, à vontade — não precisa creditar além do rodapé.
>
> [nome]

---

## Regras de envio (valem para os três)

- **Um e-mail por destinatário.** Nada de cópia oculta para 30 endereços.
- **Follow-up único, 7 dias depois**, com duas linhas: "Conseguiu ver? Se preferir outro recorte dos dados, me diga qual." Nunca um terceiro.
- **Não mande para `contato@` de site de resultado** (resultadojogomilhar, portalcanaa, lotomania). Eles não publicam conteúdo de terceiro — é a razão do 1/30.
- **Prioridade de alvo**: 5 páginas `.edu.br` (Modelo A) → 6 jornalistas de dados (Modelo B) → 4 docentes (Modelo C). 15 e-mails segmentados valem mais que os 30 da rodada anterior.
- **Meça**: planilha com `alvo | tipo | data envio | follow-up | resposta | link obtido | rel`. Sem isso você repete a rodada anterior sem saber o que falhou.

## O que não fazer (queima reputação de domínio)

- Comentário em blog com link: o Blogger e o WordPress marcam `nofollow` e o moderador apaga. Zero link, 100% de risco.
- "Troca de links" com qualquer site: padrão clássico de esquema de links, penalizável.
- Enviar o mesmo texto trocando só o nome do destinatário: quem recebe dois iguais percebe.
