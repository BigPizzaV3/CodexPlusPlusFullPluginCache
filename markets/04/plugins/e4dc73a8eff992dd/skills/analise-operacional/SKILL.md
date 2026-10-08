---
name: analise-operacional
description: Analise a operação de uma unidade usando as tools MCP do Menu Integrado para pedidos, vendas, canais, iFood, repasses e documentos fiscais. Use quando o usuário pedir métricas, comparações ou investigação operacional de uma ou mais unidades.
---

# Análise operacional

Use as tools MCP para consultar dados reais e combine os resultados apenas quando isso ajudar a responder à pergunta.

## Escopo da unidade

1. Identifique exatamente uma unidade antes de consultar qualquer métrica.
2. Se o usuário não informar a unidade, chame `list_restaurants` e pare para pedir que ele escolha.
3. Se o nome corresponder a mais de uma unidade, mostre as opções e peça confirmação. Não escolha por semelhança.
4. Nunca chame uma tool analítica sem o `restaurant_slug` da unidade escolhida.
5. Cada chamada analítica deve consultar uma única unidade. Para comparar unidades, repita a mesma tool com um slug por vez.
6. Consulte todas as unidades somente quando o usuário pedir isso explicitamente, fazendo chamadas separadas.

Não descubra a unidade chamando métricas em todas as unidades. Não trate a primeira unidade retornada como escolha do usuário.

## Escolha das tools

- Use `get_order_metrics` para um resumo do período sem agrupamento.
- Use `get_order_metrics_grouped` para evolução por dia, semana, mês, trimestre ou ano, podendo também agrupar por dimensões disponíveis.
- Use `sales_by_channel` para comparar canais de venda.
- Use `order_status_summary` para o resumo atual dos pedidos por status.
- Use `get_ifood_metrics` para movimentações financeiras conciliadas e pagamentos do iFood. Para pedidos e descontos do iFood, use também `get_order_metrics`.
- Use `get_repass_metrics` para eventos que impactam o repasse do iFood.
- Use `get_fiscal_metrics` para documentos fiscais e sua relação com pedidos.
- Use `get_products_metrics` quando a pergunta envolver o desempenho agregado dos produtos.

Consulte somente as tools necessárias. Para investigar uma queda, comece pela métrica geral e aprofunde em canais, produtos, cancelamentos, iFood, repasses ou fiscal conforme a evidência disponível. Não chame todas as tools por padrão.

## Períodos e resposta

- Use `from` e `to` no formato `YYYY-MM-DD`.
- Para comparar períodos, repita a mesma tool para cada período.
- Informe sempre a unidade e o período consultados.
- Preserve os valores retornados pelo servidor; não estime dados ausentes.
- Diferencie faturamento, quantidade de pedidos, quantidade de itens, cancelamentos, taxas e repasses.
- Apresente primeiro um resumo curto e depois os detalhes relevantes das tools utilizadas.
