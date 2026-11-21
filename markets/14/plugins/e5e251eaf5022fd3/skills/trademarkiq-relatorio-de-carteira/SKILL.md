---
name: trademarkiq-relatorio-de-carteira
description: Monta o relatório periódico de uma carteira de marcas (de uma empresa ou do cliente de um escritório) com os dados do conector TrademarkIQ: situação, prazos e vigências, despachos recentes, conflitos e ameaças, contencioso e presença no exterior, com o que fazer em cada ponto. Use quando pedirem relatório de carteira, de portfólio, status das marcas, prestação de contas ao cliente ou revisão mensal ou trimestral.
---

# TrademarkIQ: relatório de carteira

Relatório que um escritório entrega ao cliente, ou que o jurídico de uma empresa leva à diretoria. Responde a quatro perguntas: o que temos, o que vence, o que aconteceu desde o último relatório e o que exige decisão. Escreva no idioma do usuário.

## 1. O que perguntar antes (só o que faltar)

De quem é a carteira (a conta inteira, um titular ou um cliente do escritório); o período coberto (padrão: últimos 90 dias e próximos 12 meses); para quem é o relatório; nome do escritório que assina, se houver.

## 2. Dados: sempre pelas ferramentas do TrademarkIQ

1. `portfolio_summary`: totais, situação e vencimentos próximos. Dá os números de abertura.
2. `my_portfolio`: a lista das marcas (filtre por titular ou situação; pagine até cobrir o recorte ou diga quantas ficaram de fora).
3. `portfolio_deadlines` e `portfolio_critical`: vigências, prazo ordinário e suplementar de prorrogação, oposições a apresentar e prazos de contencioso na janela.
4. `portfolio_events`: despachos e mudanças do período. Para o detalhe de um processo, `trademark_details`.
5. `latest_rpi_collisions`: marcas de terceiros publicadas que colidem com a carteira.
6. Conta de empresa ou de escritório: `account_conflicts`, `account_threats`, `account_litigation`, `account_international`, `account_history` e, para o escritório, `account_clients` e `account_representatives`. Quando houver patentes, desenhos, contratos ou software na conta: `company_patents`, `account_designs`, `account_contracts`, `account_software`.
7. `portfolio_disputes` quando a conta tiver o dossiê de contencioso.

Fundamento: antes de explicar um procedimento, um prazo, um motivo de recusa ou de recomendar uma medida (oposição, manifestação, recurso, nulidade administrativa, caducidade, prorrogação, cessão), chame `manual_and_law` com palavras-chave curtas ("oposição prazo", "recurso indeferimento", "caducidade", "prorrogação") ou com o número do artigo. Escreva o prazo e a regra como vêm no trecho devolvido e cite o item do Manual de Marcas e o artigo da Lei 9.279/1996. Não afirme prazo, valor, requisito ou número de artigo de memória. Se a ferramenta não trouxer o ponto, diga que ele deve ser conferido no Manual de Marcas do INPI.

## 3. Formato (PDF, 3 a 5 páginas)

Página 1, resumo: abertura com o título como conclusão ("<Cliente> tem N marcas em vigor; M exigem decisão até <mês>."); quatro números (marcas em vigor, pedidos em andamento, vencimentos em 12 meses, pontos que exigem decisão); cartão "O que mudou no período" com 3 a 5 fatos; cartão "Decisões pedidas ao cliente", numeradas, cada uma com prazo.

Página 2, prazos: tabela ordenada por data com marca, processo, classe, o que vence, data-limite e medida. Separe o que vence no prazo ordinário do que já está no prazo suplementar.

Página 3, movimentação e riscos: tabela dos despachos do período (data da RPI, marca, despacho, o que significa, próxima etapa) e tabela de conflitos e ameaças (marca de terceiro, titular, classe, por que colide, medida possível e até quando).

Páginas seguintes, quando houver dados: contencioso (processo, tribunal, partes, fase), presença no exterior (país, registro, situação) e inventário completo em anexo.

Visual: páginas de 828 x 1170 px; fundo #f4f5f8; cartões brancos com borda #e1e5ee e cantos de 12 px; navy #1b3a6b; dourado #c28a2d (linha de destaque #e6b85c sobre navy); azul #2f5faa; cinza-azulado #b9c2d6; texto #1d2433 e secundário #5d667a. Fontes: Inter no texto, DejaVu Serif em títulos e números. Cabeçalho com o logotipo do TrademarkIQ à esquerda e, à direita, "Em parceria com <escritório>" quando houver. Abertura em bloco navy: linha pequena em caixa alta e dourada, título em serifa escrito como conclusão, e uma linha com o escopo e a data.

## 4. Regras

1. Logotipo: use sempre o logotipo oficial, nunca um desenho próprio nem o nome em texto. Com esta skill instalada, os arquivos estão em `assets/` (`trademarkiq-logo-fundo-claro.png` para fundo branco ou claro, `trademarkiq-logo-fundo-escuro.png` para fundo navy ou escuro, `trademarkiq-icone.png`); copie-os para o diretório de trabalho, porque o ambiente de código não tem rede. Sem a skill, chame `trademarkiq_logo`. Mantenha a proporção, não recolora e não peça o logotipo ao usuário.
2. Endereço: o site é sempre `https://trademarkiq.com.br`. Use só os links que as ferramentas devolvem e cite o número de cada processo.
3. Só entra no relatório o que veio de uma ferramenta. Se um dado não veio, escreva que não está disponível; não estime nem complete de memória.
4. Contagens: todo número de destaque tem de bater com as linhas das tabelas. Se a ferramenta devolveu uma página de um total maior, diga quantos itens existem e quantos estão listados.
5. Uma ferramenta que responde que a área não se aplica à conta, que o plano não a inclui ou que a cota do dia acabou não é falta de dados: omita a seção e diga ao usuário, fora do relatório, o que ficou de fora e por quê.
6. Não explique como as análises são calculadas nem cite fontes internas.
7. Rodapé em todas as páginas: "Fonte: TrademarkIQ (trademarkiq.com.br). Consulta em <data>.", o aviso de que o material usa dados públicos e não é parecer jurídico nem garantia de resultado, e o número da página.
8. Cada linha de prazo ou de medida leva a data-limite e a base (item do manual ou artigo). Sem a base, não recomende a medida: registre o ponto como "a avaliar".
9. Nunca diga que falta pagar taxa de concessão: descreva só as retribuições que o trecho do manual trouxer.
10. Dados de um cliente não entram no relatório de outro.

## 5. Construção

HTML com SVG embutido, convertido em PDF por um navegador sem interface, com `@page` em 828 x 1170 px. Antes de entregar, abra as páginas renderizadas e confira: número de páginas, nada cortado pelo rodapé, tabelas sem texto sobreposto, logotipo nítido. Se o usuário pedir só a análise, entregue o mesmo conteúdo em texto, na mesma ordem.
