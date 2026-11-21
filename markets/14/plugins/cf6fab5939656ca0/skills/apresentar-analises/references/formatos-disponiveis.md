# Formatos disponíveis

Use esta referência para escolher a apresentação. O schema e os metadados da ferramenta na sessão prevalecem se o componente evoluir.

| Pedido | Ferramenta e comportamento atual |
|---|---|
| Resumo de vendas | `visualizar_vendas`, `resumo`: indicadores selecionados. Para um número só, use o atalho de dados e responda em texto. |
| Resumo e evolução | `visualizar_vendas`, `resumo_e_evolucao`: ambos no mesmo componente e na mesma chamada. |
| Evolução de um período | `visualizar_vendas`, `evolucao`: até quatro métricas; cada métrica gera um gráfico separado. |
| Ranking visual de lojas | `visualizar_vendas`, `ranking`: dez lojas selecionadas por receita. Para menor ticket ou outra ordenação, use `shortcutSalesRanking` e preserve o critério solicitado. |
| Evolução diária comparada | `comparar_periodos_vendas`: dois a quatro períodos de até 31 dias, uma a três métricas. Vários períodos no mesmo gráfico; um gráfico por métrica. Alinhamento por dia da semana exige mesma duração e mesmo dia inicial da semana. |
| SQL visual | `consultar_dados_personalizados`: linhas, barras, cards, produtos ou cestas. Linhas e barras mostram uma métrica principal. Cards exigem uma linha numérica; atualmente exibem até quatro medidas. |
| SQL tabular | `consultar_tabela_personalizada`: tabela no chat. Limite de até 200 linhas; preserve o aviso de truncamento. |
| Produtos e cestas | Cards; grade em tela ampla e carrossel em tela estreita. Cestas comportam duas a seis mercadorias por combinação e até dez combinações. Percentual exige total de compras do mesmo universo. |
| CRM e campanhas da plataforma | Os atalhos públicos retornam dados para o chat. Não presumir widget dedicado ou usar uma ferramenta interna não exposta. |

## Limites de composição

- `LineChart` aceita várias séries, usadas hoje para períodos da mesma métrica. Isso não significa suporte público a métricas diferentes no mesmo eixo.
- Não há seleção de indicadores dentro dos gráficos, carrossel de gráficos, índice base 100 ou dois eixos no contrato atual. O carrossel de produtos/cestas não se aplica automaticamente a gráficos.
- Restrinja a visualização aos indicadores necessários. Se o pedido exigir múltiplas evoluções, mantenha-as no componente atual; não ofereça controles inexistentes nem faça consultas duplicadas.
- A apresentação automática pode escolher uma única métrica. Confira quais colunas serão exibidas e apresente no chat as demais informações necessárias à pergunta.
- A existência de um componente no código não garante que alguma ferramenta pública o entregue. Use apenas as ferramentas disponíveis e respeite sua orientação de apresentação.
