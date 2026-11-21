---
name: trademarkiq-painel-do-escritorio
description: Monta o painel de gestão de um escritório de propriedade intelectual com os dados do conector TrademarkIQ: negócio no CRM (receita, funil, serviços, equipe, metas) cruzado com a carteira no INPI (clientes, vigências, clientes que passaram a depositar por outro representante). Use quando pedirem o panorama do escritório, a reunião de sócios, indicadores do mês, desempenho comercial ou onde está o risco e a oportunidade na base de clientes.
---

# TrademarkIQ: painel do escritório

Uma leitura do negócio para a reunião de sócios: o que entrou, o que está em negociação, onde a base de clientes está crescendo e onde está saindo. Só funciona para contas de escritório; a parte comercial exige o CRM ligado à conta. Escreva no idioma do usuário.

## 1. O que perguntar antes (só o que faltar)

O período (padrão: últimos 90 dias); se o painel é para os sócios (tudo) ou para a equipe (sem valores por pessoa).

## 2. Dados: sempre pelas ferramentas do TrademarkIQ

Comece por `my_account`: ela diz se as ferramentas de CRM estão disponíveis para a conta.

Negócio (CRM):
1. `crm_summary`: indicadores do período, comparação com o período anterior, receita por mês e por frente, origem do trabalho, metas.
2. `crm_funnel`: etapas, velocidade por etapa e motivos de perda.
3. `crm_services`: desempenho por tipo de serviço (em negociação, ganhos, conversão, receita, ticket, ciclo, recorrente).
4. `crm_team`: desempenho por pessoa, ranking do mês e metas.
5. `crm_opportunities`: clientes da carteira no INPI sem contato recente, renovações em 12 meses sem negócio aberto e clientes cujos depósitos novos saem por outro representante.

Carteira (INPI): `account_clients` (quem sustenta a carteira e como cada relação se move), `account_financials`, `account_history`, `account_representatives` e `portfolio_deadlines`.

Se o CRM não estiver ligado, monte o painel só com a carteira e diga, fora do relatório, que a parte comercial depende da ligação do CRM à conta.

## 3. Formato (PDF, 3 páginas)

Página 1, o negócio: abertura com o título como conclusão ("Receita de <período> em R$ X, com Y em negociação; conversão em <tendência>."); quatro números (receita fechada, valor em negociação, conversão, ticket médio); gráfico de receita por mês; cartão "O que mudou" com a comparação com o período anterior.

Página 2, onde está o resultado: tabela por serviço (em negociação, ganhos, conversão, receita, ciclo) com a linha de maior receita em destaque; funil por etapa com a etapa mais lenta marcada; motivos de perda.

Página 3, a base de clientes: três listas curtas, cada uma com o cliente, o sinal e a ação: (1) renovações nos próximos 12 meses sem negócio aberto; (2) clientes ativos sem contato há muito tempo; (3) clientes cujos depósitos novos saem por outro representante. Feche com "Três decisões para a reunião".

A página de equipe só entra se o usuário pedir, e é sempre uma página separada.

Visual: páginas de 828 x 1170 px; fundo #f4f5f8; cartões brancos com borda #e1e5ee e cantos de 12 px; navy #1b3a6b; dourado #c28a2d (linha de destaque #e6b85c sobre navy); azul #2f5faa; cinza-azulado #b9c2d6; texto #1d2433 e secundário #5d667a. Fontes: Inter no texto, DejaVu Serif em títulos e números. Cabeçalho com o logotipo do TrademarkIQ à esquerda e, à direita, "Em parceria com <escritório>" quando houver. Abertura em bloco navy: linha pequena em caixa alta e dourada, título em serifa escrito como conclusão, e uma linha com o escopo e a data.

## 4. Regras

1. Logotipo: use sempre o logotipo oficial, nunca um desenho próprio nem o nome em texto. Com esta skill instalada, os arquivos estão em `assets/` (`trademarkiq-logo-fundo-claro.png` para fundo branco ou claro, `trademarkiq-logo-fundo-escuro.png` para fundo navy ou escuro, `trademarkiq-icone.png`); copie-os para o diretório de trabalho, porque o ambiente de código não tem rede. Sem a skill, chame `trademarkiq_logo`. Mantenha a proporção, não recolora e não peça o logotipo ao usuário.
2. Endereço: o site é sempre `https://trademarkiq.com.br`. Use só os links que as ferramentas devolvem e cite o número de cada processo.
3. Só entra no relatório o que veio de uma ferramenta. Se um dado não veio, escreva que não está disponível; não estime nem complete de memória.
4. Contagens: todo número de destaque tem de bater com as linhas das tabelas. Se a ferramenta devolveu uma página de um total maior, diga quantos itens existem e quantos estão listados.
5. Uma ferramenta que responde que a área não se aplica à conta, que o plano não a inclui ou que a cota do dia acabou não é falta de dados: omita a seção e diga ao usuário, fora do relatório, o que ficou de fora e por quê.
6. Não explique como as análises são calculadas nem cite fontes internas.
7. Rodapé em todas as páginas: "Fonte: TrademarkIQ (trademarkiq.com.br). Consulta em <data>.", o aviso de que o material usa dados públicos e não é parecer jurídico nem garantia de resultado, e o número da página.
8. Os números do CRM são do escritório e confidenciais: não os compare com os de outros escritórios nem os reutilize em outro material.
9. Com poucos negócios fechados no período, diga quantos são e não tire tendência de percentuais sobre bases pequenas.
10. "Depósitos por outro representante" é o que consta no INPI; não afirme que o cliente rompeu o contrato nem o motivo.
11. Valores sempre com a moeda e o período; receita fechada e valor em negociação nunca somados.

## 5. Construção

HTML com SVG embutido, convertido em PDF por um navegador sem interface, com `@page` em 828 x 1170 px. Antes de entregar, abra as páginas renderizadas e confira: número de páginas, nada cortado pelo rodapé, tabelas sem texto sobreposto, logotipo nítido. Se o usuário pedir só a análise, entregue o mesmo conteúdo em texto, na mesma ordem.
