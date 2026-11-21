# Dashboards para decisões do dia a dia

Na primeira interação, após identificar a empresa, apresente as oito áreas e sugira começar por uma. Respeite pedidos diretos sem obrigar o usuário a montar um dashboard. Se pedir todas, organize uma visão executiva com oito seções e detalhe progressivamente. Use a data do contexto, nunca um ano/filial fixo. Para fluxos, proponha mês atual até hoje e comparação com o mesmo intervalo do mês anterior; para posições, use posição atual. Declare esses critérios e permita trocar todos os filtros.

| Área | Cards propostos, sujeitos às fontes e regras instaladas | Decisão apoiada |
|---|---|---|
| Estoque | Saldo atual por produto/unidade/filial; itens abaixo de mínimo cadastrado; itens sem movimento; evolução de entradas e saídas | Repor, transferir ou investigar materiais parados |
| Compra | Volume e valor de compras; evolução por produto; concentração por fornecedor; devoluções; preço médio ponderado apenas com bases comparáveis | Negociar preços e diversificar fornecedores |
| Venda | Volume e valor de vendas; evolução por produto; concentração por cliente; devoluções; pedidos pendentes se houver fonte validada | Priorizar clientes e revisar o mix de venda |
| Fiscal | Documentos por situação; cancelamentos/rejeições; concentração por CFOP; divergências documentadas | Corrigir pendências antes do fechamento |
| Financeiro 3.0 | A pagar/a receber abertos; vencidos com saldo; próximos vencimentos; concentração por pessoa/moeda | Priorizar cobranças e planejar pagamentos |
| Serviço 3.0 | Ordens e medições por status confirmado; prazos vencidos; valores medidos e faturados separados; concentração por cliente | Priorizar execução e identificar pendências de faturamento |
| Transporte | Viagens por situação; entregas pendentes/atrasadas; volume por rota; despesas registradas quando vinculadas e documentadas | Reorganizar rotas e acompanhar entregas |
| Almoxarifado | Posição de materiais; consumo por centro/setor; requisições pendentes; mínimos cadastrados | Planejar reposições e investigar consumo |

## Contrato de cada card

Cada card deve ter: nome e pergunta de negócio; valor real com unidade/moeda; período ou data da posição; filiais/filtros; fonte e critério de cálculo; comparação equivalente quando disponível; sinal de atenção fundamentado e ação sugerida. Inclua acesso ao detalhamento por nova consulta. Use 3 a 5 cards prioritários por área, gráfico de tendência/composição e lista de pendências quando as fontes permitirem.

Não invente metas, mínimos, status, prazos, saldos históricos, margem, custo, apuração de impostos ou regras de liquidação. Metas e semáforos exigem parâmetro cadastrado ou critério aceito pelo usuário. Sem base de comparação, indique indisponível; com denominador zero, não calcule variação percentual. Compare moedas/unidades iguais. Valores de NF não são imposto devido nem caixa recebido.

Financeiro 3.0 usa fin_cab_pagrec/fin_ite_pagrec. Os exemplos de saldo de listagem não comprovam o saldo do dashboard oficial: informe o critério real e não prometa equivalência sem validação. Serviço usa apenas fontes _serv3. Estoque, transporte e almoxarifado exigem descoberta de tabelas, chaves e regras reais; existência de tabela não comprova módulo licenciado. Card sem fonte/regra disponível deve dizer "não disponível", com a informação que falta, nunca zero.

Consulte via MCP somente leitura e agregue o conjunto filtrado antes de paginar. Consultas de áreas distintas não representam um snapshot transacional único; informe horário e período de coleta. Sugestões não executam compras, pagamentos, faturamento ou ajustes.

## Apresentação

Monte cards e gráficos na conversa quando a interface permitir; como alternativa, entregue tabela executiva com os mesmos campos. Se solicitado um artefato HTML, use os dados já autorizados, indique data da extração e mantenha todos os tokens e credenciais fora do arquivo. O artefato é uma fotografia dos dados: não alegue atualização automática, persistência ou componente embutido oficial sem implementação e teste. Atualizar exige novas consultas autenticadas.

Pedido inicial sugerido: "Crie meu dashboard de negócio para as oito áreas disponíveis. Comece identificando minha empresa e filiais, proponha o período e mostre os indicadores que ajudam a decidir o que fazer hoje."
