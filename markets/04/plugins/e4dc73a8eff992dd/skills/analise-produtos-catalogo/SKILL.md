---
name: analise-produtos-catalogo
description: Analise produtos e catálogo de uma unidade usando as tools MCP do Menu Integrado para detalhes, variações, fichas técnicas, métricas e histórico de vendas. Use quando o usuário pedir informações, desempenho ou análise de um produto ou do catálogo.
---

# Análise de produtos e catálogo

Use as tools MCP para consultar o catálogo e o desempenho dos produtos da unidade escolhida. Separe informações cadastrais, ficha técnica e histórico de vendas.

## Escopo e identificação

1. Identifique a unidade antes de consultar o catálogo.
2. Se a unidade não estiver clara, siga a skill `analise-operacional`: use `list_restaurants` e peça a escolha.
3. Use `list_menu_products` uma vez para localizar produtos e filtre o resultado em memória.
4. Se houver mais de um produto compatível, peça confirmação. Não escolha pelo primeiro resultado.
5. Depois de identificar o produto, use o `product_slug` retornado pelo catálogo.

## Escolha das tools

- Use `list_menu_products` para listar ou pesquisar produtos do catálogo.
- Use `get_product_details` para informações cadastrais do produto.
- Use `get_product_variations` quando o usuário perguntar por variações e seus itens.
- Use `get_product_recipe` quando o usuário pedir a ficha técnica, insumos ou composição.
- Use `get_products_metrics` para desempenho agregado de vários produtos em um período.
- Use `get_product_sales_history` para o histórico de um produto específico, agrupado por dia, semana, mês, trimestre ou ano.

Não chame detalhes, variações ou ficha técnica para todos os produtos quando o usuário pediu apenas uma listagem ou uma busca. Não faça uma chamada de histórico para cada produto quando uma métrica agregada resolver a pergunta.

## Análise e limites

- Para saber quanto um produto vendeu, quando vendeu ou como evoluiu, use `get_product_sales_history` com uma unidade, um produto e um período.
- Para comparar produtos, use `get_products_metrics` uma vez e compare os resultados retornados.
- Para comparar períodos de um produto, repita `get_product_sales_history` para cada período quando necessário.
- Combine detalhes, variações e ficha técnica somente quando a pergunta exigir uma análise do cadastro.
- Não afirme que códigos fiscais, descrições, macros ou custos estão corretos sem dados suficientes.
- Não invente ingredientes, valores nutricionais, margens ou informações que não estejam no retorno das tools.
- Diferencie quantidade de itens vendidos, quantidade de pedidos e faturamento.
- Informe a unidade, o produto e o período usados na resposta.
