---
name: trademarkiq-boletim-da-rpi
description: Monta o boletim de uma edição da Revista da Propriedade Industrial (RPI) com os dados do conector TrademarkIQ: o que a edição trouxe, o que tocou na carteira do usuário, os prazos que começaram a correr e o que fazer em cada despacho. Use quando pedirem o resumo da RPI, o boletim da semana, o que saiu na revista ou os prazos abertos pela última edição.
---

# TrademarkIQ: boletim da RPI

A RPI sai às terças-feiras e é a partir dela que os prazos contam. O boletim tem duas partes: a edição no mercado e a edição na carteira do usuário. Escreva no idioma do usuário.

## 1. O que perguntar antes (só o que faltar)

Qual edição (padrão: a mais recente); se o boletim é só da carteira do usuário, só do mercado ou dos dois; classes ou titulares de interesse, se houver.

## 2. Dados: sempre pelas ferramentas do TrademarkIQ

1. `rpi_issues`: número e data da edição. Nunca presuma a data.
2. `rpi_summary`: volumes da edição por tipo de despacho e os procuradores com mais publicações.
3. `rpi_dispatches`: os despachos da edição, filtrados por tipo, classe ou titular.
4. Carteira do usuário: `portfolio_events` (o que foi publicado para as marcas dele), `latest_rpi_collisions` (pedidos de terceiros que colidem) e `portfolio_critical` (prazos que a edição abriu). Para um processo específico, `trademark_details`.
5. Conta de escritório ou de empresa: `account_conflicts` e `account_threats`.

Para cada tipo de despacho que aparecer no boletim, chame `manual_and_law` (por exemplo "despachos aplicáveis indeferimento", "exigência prazo", "publicação para oposição", "sobrestamento") e descreva o que o despacho significa e o que cabe fazer com as palavras do manual.

Fundamento: antes de explicar um procedimento, um prazo, um motivo de recusa ou de recomendar uma medida (oposição, manifestação, recurso, nulidade administrativa, caducidade, prorrogação, cessão), chame `manual_and_law` com palavras-chave curtas ("oposição prazo", "recurso indeferimento", "caducidade", "prorrogação") ou com o número do artigo. Escreva o prazo e a regra como vêm no trecho devolvido e cite o item do Manual de Marcas e o artigo da Lei 9.279/1996. Não afirme prazo, valor, requisito ou número de artigo de memória. Se a ferramenta não trouxer o ponto, diga que ele deve ser conferido no Manual de Marcas do INPI.

## 3. Formato (PDF, 2 páginas, ou texto para e-mail)

Página 1, a edição: abertura com "RPI <número>, de <data>" e o título como conclusão; quatro números (publicações de marcas, deferimentos, indeferimentos, pedidos publicados para oposição, ou os que a ferramenta trouxer); gráfico de barras por tipo de despacho; cartão "O que chama atenção" com 3 fatos.

Página 2, a carteira: tabela "Suas marcas nesta edição" (marca, processo, despacho, o que significa, prazo e data-limite, medida) e tabela "Pedidos de terceiros a acompanhar" (marca, titular, classe, por que colide, data-limite para oposição). Feche com a lista numerada "Prazos que começaram a correr", em ordem de data.

Se o usuário pedir texto para e-mail, use a mesma ordem, sem gráfico, com as tabelas em lista.

Visual: páginas de 828 x 1170 px; fundo #f4f5f8; cartões brancos com borda #e1e5ee e cantos de 12 px; navy #1b3a6b; dourado #c28a2d (linha de destaque #e6b85c sobre navy); azul #2f5faa; cinza-azulado #b9c2d6; texto #1d2433 e secundário #5d667a. Fontes: Inter no texto, DejaVu Serif em títulos e números. Cabeçalho com o logotipo do TrademarkIQ à esquerda e, à direita, "Em parceria com <escritório>" quando houver. Abertura em bloco navy: linha pequena em caixa alta e dourada, título em serifa escrito como conclusão, e uma linha com o escopo e a data.

## 4. Regras

1. Logotipo: use sempre o logotipo oficial, nunca um desenho próprio nem o nome em texto. Com esta skill instalada, os arquivos estão em `assets/` (`trademarkiq-logo-fundo-claro.png` para fundo branco ou claro, `trademarkiq-logo-fundo-escuro.png` para fundo navy ou escuro, `trademarkiq-icone.png`); copie-os para o diretório de trabalho, porque o ambiente de código não tem rede. Sem a skill, chame `trademarkiq_logo`. Mantenha a proporção, não recolora e não peça o logotipo ao usuário.
2. Endereço: o site é sempre `https://trademarkiq.com.br`. Use só os links que as ferramentas devolvem e cite o número de cada processo.
3. Só entra no relatório o que veio de uma ferramenta. Se um dado não veio, escreva que não está disponível; não estime nem complete de memória.
4. Contagens: todo número de destaque tem de bater com as linhas das tabelas. Se a ferramenta devolveu uma página de um total maior, diga quantos itens existem e quantos estão listados.
5. Uma ferramenta que responde que a área não se aplica à conta, que o plano não a inclui ou que a cota do dia acabou não é falta de dados: omita a seção e diga ao usuário, fora do relatório, o que ficou de fora e por quê.
6. Não explique como as análises são calculadas nem cite fontes internas.
7. Rodapé em todas as páginas: "Fonte: TrademarkIQ (trademarkiq.com.br). Consulta em <data>.", o aviso de que o material usa dados públicos e não é parecer jurídico nem garantia de resultado, e o número da página.
8. Toda data-limite é calculada a partir da data da edição devolvida por `rpi_issues` e do prazo que o trecho do manual ou da lei trouxer; mostre a conta ("60 dias a partir de dd/mm/aaaa"). Não some prazos de memória.
9. Se a carteira do usuário não teve publicações na edição, diga isso em uma linha; não preencha a página com marcas de terceiros.

## 5. Construção

HTML com SVG embutido, convertido em PDF por um navegador sem interface, com `@page` em 828 x 1170 px. Antes de entregar, abra as páginas renderizadas e confira: número de páginas, nada cortado pelo rodapé, tabelas sem texto sobreposto, logotipo nítido. Se o usuário pedir só a análise, entregue o mesmo conteúdo em texto, na mesma ordem.
