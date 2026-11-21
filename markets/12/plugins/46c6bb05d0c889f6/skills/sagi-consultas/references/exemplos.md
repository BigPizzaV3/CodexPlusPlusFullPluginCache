# Exemplos de perguntas para usar no ChatGPT ou no Claude

> Versão 0.4.0: os exemplos podem ser adaptados e executados com SQL livre de leitura. Todas as filiais da empresa do login estão autorizadas; TODAS tem esse escopo. O catálogo não exige cadastro de cada SQL. Confirme o esquema real e os critérios do relatório.

O cliente pode escrever as perguntas abaixo em linguagem natural, sem conhecer SQL. O assistente deve consultar o contexto/esquema autorizado, adaptar datas/códigos e usar a consulta vinculada. As datas, palavras e números são exemplos; não são dados de um cliente.

São **39 exemplos SQL**: os 25 anteriores (incluindo a referência BDI FILIAL2/2026) e 14 análises livres adicionais. Os SQLs podem ser adaptados sem cadastro prévio. Confirme campos e critérios na base do cliente; o relatório de referência foi homologado pelo BDI, e os demais exemplos não substituem validação de valores.

| ID | O cliente pode perguntar | SQL / critérios |
|---|---|---|
| P01 | “Mostre as pesagens de compra desde 01/06/2026 até hoje.” | [Entradas](pesagens.md#p01--listar-entradas-desde-1º-de-junho-de-2026) |
| P02 | “Mostre as pesagens de venda desde 01/06/2026 até hoje.” | [Saídas](pesagens.md#p02--listar-saídas-desde-1º-de-junho-de-2026) |
| P03 | “Qual o peso comprado por filial e unidade desde junho?” | [Totais](pesagens.md#p03--total-de-entradas-por-filial-e-unidade-de-medida) |
| P04 | “Mostre a evolução diária do peso vendido desde junho.” | [Por dia](pesagens.md#p04--evolução-diária-de-saídas) |
| P05 | “Quais produtos mais recebemos desde junho?” | [Por produto/subproduto](pesagens.md#p05--entradas-por-produto-e-subproduto) |
| P06 | “Quais os dez fornecedores com maior peso comprado em KG?” | [Ranking](pesagens.md#p06--fornecedores-com-maior-volume-em-uma-unidade) |
| P07 | “Mostre as entradas do fornecedor 123 desde junho.” | [Por fornecedor](pesagens.md#p07--pesagens-de-um-fornecedor) |
| P08 | “Mostre os itens do boleto de venda 456 desde junho.” | [Por boleto](pesagens.md#p08--detalhar-um-boleto-de-venda) |
| N01 | “Liste as notas fiscais emitidas desde janeiro de 2026.” | [Por emissão](fiscal.md#n01--notas-emitidas-desde-janeiro-de-2026) |
| N02 | “Liste as notas de entrada movimentadas desde janeiro.” | [Por entrada/saída](fiscal.md#n02--notas-de-entrada-pela-data-de-entradasaída) |
| N03 | “Mostre as notas de saída por mês e situação.” | [Por mês/status](fiscal.md#n03--notas-de-saída-por-mês-de-emissão-e-status) |
| N04 | “Quantas notas existem em cada operação e status?” | [Por operação/status](fiscal.md#n04--quantidade-e-valor-por-operação-e-status) |
| N05 | “Mostre os tributos destacados por CFOP e situação.” | [Tributos da NF](fiscal.md#n05--valores-de-tributos-destacados-por-cfop-e-status) |
| N06 | “Encontre a nota 12345, série 1, modelo 55, de 2026.” | [Localizar nota](fiscal.md#n06--localizar-uma-nota-por-número-série-e-modelo) |
| C01 | “Localize fornecedores com RECICLAGEM no nome.” | [Fornecedores](cadastros.md#c01--encontrar-fornecedor-por-parte-do-nome) |
| C02 | “Localize clientes com RECICLAGEM no nome.” | [Clientes](cadastros.md#c02--encontrar-cliente-por-parte-do-nome) |
| C03 | “Quais produtos de compra têm SUCATA na descrição?” | [Produtos](cadastros.md#c03--localizar-código-e-subcódigo-de-produto) |
| F01 | “Liste os títulos lançados desde 01/01/2025.” | [Listagem original reduzida](financeiro30.md#exemplo-reduzido-de-listagem) |
| F02 | “Some o saldo dessa listagem por pagar/receber e moeda.” | [Total da listagem](financeiro30.md#totais-do-mesmo-recorte-do-exemplo) |
| F03 | “Liste os títulos que vencem de hoje até daqui a 30 dias.” | [Vencimentos](financeiro30.md#f03--títulos-com-vencimento-de-hoje-até-daqui-a-30-dias) |
| F04 | “No critério do dashboard, quanto está em aberto desde junho?” | [Dashboard do portal](financeiro30.md#f04--saldo-em-aberto-no-critério-do-dashboard-do-portal) |
| S01 | “Liste as medições emitidas em janeiro de 2025.” | [Medições Serviço 3.0](servico30.md#exemplo-medições-emitidas-em-um-período) |
| S02 | “Quantas medições foram emitidas desde junho por filial/status?” | [Contagem por status](servico30.md#s02--medições-por-filial-e-status) |
| S03 | “Mostre os contratos e prestações dos itens da medição 123.” | [Itens de medição](servico30.md#s03--itens-e-contrato-de-uma-medição) |

## Como adaptar uma pergunta

O usuário pode acrescentar período, filial, código/nome, unidade, quantidade de linhas e formato de apresentação. Por exemplo: “Mostre os dez produtos mais recebidos em KG na filial autorizada que eu selecionar, em junho de 2026.” O assistente deve esclarecer a filial/unidade se houver ambiguidade, aplicar o período completo e declarar o corte do ranking.

Para a rota generic, a ponte envia cada consulta como `{"sql":"SELECT ..."}`. Não enviar o nome desta referência, a pergunta em linguagem natural ou fragmentos de SQL não validados no campo `sql`.

Regras que afetam a resposta: manter sinais de devolução e regras da função de pesagens; separar unidades e moedas; distinguir emissão/vencimento/pagamento; declarar inclusão de canceladas; separar itens de boletos e medição de recebimento. Uma lista de cem linhas não é o conjunto completo nem substitui os SQL de agregação.

## Mais 14 análises livres

Leia [analises.md](analises.md) para cadastros por UF/status, diagnósticos de códigos, financeiro mensal, pessoas e EXISTS, CTE/ranking, medições mensais e aprovação, cabeçalho fiscal, vendas de várias filiais, devoluções e comparação mensal com LAG. O documento também orienta descobrir qualquer outro módulo instalado.
