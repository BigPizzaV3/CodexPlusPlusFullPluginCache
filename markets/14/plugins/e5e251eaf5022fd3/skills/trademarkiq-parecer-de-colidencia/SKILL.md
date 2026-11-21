---
name: trademarkiq-parecer-de-colidencia
description: Monta a análise comparativa entre duas marcas (ou entre um nome novo e uma anterioridade) com os dados do conector TrademarkIQ, fundamentada no Manual de Marcas do INPI, na Lei 9.279/1996 e em decisões dos tribunais: semelhança dos sinais, afinidade dos produtos e serviços, risco de confusão e teses possíveis. Use quando pedirem análise de colidência, comparação entre marcas, subsídios para oposição, manifestação, recurso ou nulidade, ou chance de convivência.
---

# TrademarkIQ: análise de colidência entre duas marcas

Material de trabalho para quem vai redigir uma oposição, uma manifestação, um recurso ou uma nulidade, ou decidir se vale tentar a convivência. Organiza os fatos e os fundamentos; a peça e a estratégia são do profissional. Escreva no idioma do usuário.

## 1. O que perguntar antes (só o que faltar)

As duas marcas (número do processo de cada uma, ou o nome novo e as classes); de que lado o usuário está; a medida em vista (oposição, manifestação à oposição, recurso, nulidade, acordo de convivência) e a data da publicação que abriu o prazo, se houver.

## 2. Dados: sempre pelas ferramentas do TrademarkIQ

1. `trademark_details` nas duas: apresentação (nominativa, mista, figurativa), classe, especificação completa, datas de depósito e de concessão, situação, titular e despachos. `get_trademark_logo` quando houver elemento figurativo.
2. `analyze_collision` com o nome e as classes: o grau de semelhança e o risco que a ferramenta devolve.
3. `search_trademarks` com o elemento comum, na classe e nas afins: quantas marcas de titulares diferentes convivem com esse termo. É o dado que sustenta ou derruba a tese de termo diluído.
4. `manual_and_law`: os critérios do exame ("análise do requisito de disponibilidade", "colidência entre sinais", "afinidade mercadológica", "convivência entre marcas", "sinal descritivo de uso comum", "marca de alto renome") e os artigos (124, 129 e os da medida em vista).
5. `ip_case_law` com os termos da tese (por exemplo "termo evocativo", "trade dress", "convivência", "marca fraca"): 2 a 4 decisões, citadas por tribunal, classe, número, relator e data.
6. `search_ip_cases` com as partes: se já há litígio entre elas.

Fundamento: antes de explicar um procedimento, um prazo, um motivo de recusa ou de recomendar uma medida (oposição, manifestação, recurso, nulidade administrativa, caducidade, prorrogação, cessão), chame `manual_and_law` com palavras-chave curtas ("oposição prazo", "recurso indeferimento", "caducidade", "prorrogação") ou com o número do artigo. Escreva o prazo e a regra como vêm no trecho devolvido e cite o item do Manual de Marcas e o artigo da Lei 9.279/1996. Não afirme prazo, valor, requisito ou número de artigo de memória. Se a ferramenta não trouxer o ponto, diga que ele deve ser conferido no Manual de Marcas do INPI.

## 3. Formato (PDF, 3 páginas, ou texto)

Página 1, conclusão: abertura com o título como conclusão ("<A> e <B>: semelhança alta nos sinais, afinidade parcial nos serviços."); quadro lado a lado das duas marcas (sinal, apresentação, classe, especificação resumida, depósito, concessão, situação, titular); escala de risco com a posição marcada; cartão "Prazo e medida" com a data-limite e a conta.

Página 2, a análise, em quatro blocos, cada um com o critério do manual citado: (1) os sinais: fonética, grafia, significado e conjunto; (2) os produtos e serviços: o que coincide, o que é afim e o que é distinto, com as palavras das especificações; (3) o mercado: quantas marcas convivem com o elemento comum e de quantos titulares; (4) as datas: quem depositou primeiro e o que isso muda.

Página 3, teses e fundamentos: tabela com duas colunas, "A favor de <lado do usuário>" e "Contra", cada linha com o fundamento (item do manual, artigo, decisão). Depois, caminhos possíveis, numerados, com prazo e base.

Visual: páginas de 828 x 1170 px; fundo #f4f5f8; cartões brancos com borda #e1e5ee e cantos de 12 px; navy #1b3a6b; dourado #c28a2d (linha de destaque #e6b85c sobre navy); azul #2f5faa; cinza-azulado #b9c2d6; texto #1d2433 e secundário #5d667a. Fontes: Inter no texto, DejaVu Serif em títulos e números. Cabeçalho com o logotipo do TrademarkIQ à esquerda e, à direita, "Em parceria com <escritório>" quando houver. Abertura em bloco navy: linha pequena em caixa alta e dourada, título em serifa escrito como conclusão, e uma linha com o escopo e a data.

## 4. Regras

1. Logotipo: use sempre o logotipo oficial, nunca um desenho próprio nem o nome em texto. Com esta skill instalada, os arquivos estão em `assets/` (`trademarkiq-logo-fundo-claro.png` para fundo branco ou claro, `trademarkiq-logo-fundo-escuro.png` para fundo navy ou escuro, `trademarkiq-icone.png`); copie-os para o diretório de trabalho, porque o ambiente de código não tem rede. Sem a skill, chame `trademarkiq_logo`. Mantenha a proporção, não recolora e não peça o logotipo ao usuário.
2. Endereço: o site é sempre `https://trademarkiq.com.br`. Use só os links que as ferramentas devolvem e cite o número de cada processo.
3. Só entra no relatório o que veio de uma ferramenta. Se um dado não veio, escreva que não está disponível; não estime nem complete de memória.
4. Contagens: todo número de destaque tem de bater com as linhas das tabelas. Se a ferramenta devolveu uma página de um total maior, diga quantos itens existem e quantos estão listados.
5. Uma ferramenta que responde que a área não se aplica à conta, que o plano não a inclui ou que a cota do dia acabou não é falta de dados: omita a seção e diga ao usuário, fora do relatório, o que ficou de fora e por quê.
6. Não explique como as análises são calculadas nem cite fontes internas.
7. Rodapé em todas as páginas: "Fonte: TrademarkIQ (trademarkiq.com.br). Consulta em <data>.", o aviso de que o material usa dados públicos e não é parecer jurídico nem garantia de resultado, e o número da página.
8. Apresente os argumentos dos dois lados. Uma análise que só lista o que favorece o usuário não serve para decidir.
9. Decisão judicial só entra se veio de `ip_case_law` ou `ip_case`, citada com os dados devolvidos. Não cite precedente de memória e não resuma além do que a ementa diz.
10. O grau de risco é o que a ferramenta devolve; a leitura das teses é qualitativa e o material diz isso. Não prometa resultado.

## 5. Construção

HTML com SVG embutido, convertido em PDF por um navegador sem interface, com `@page` em 828 x 1170 px. Antes de entregar, abra as páginas renderizadas e confira: número de páginas, nada cortado pelo rodapé, tabelas sem texto sobreposto, logotipo nítido. Se o usuário pedir só a análise, entregue o mesmo conteúdo em texto, na mesma ordem.
