---
name: diagnosticar-vendas-e-mix
description: Investigue vendas, diferenças entre lojas, ticket, produtos e combinações de compra com dados da Sellbie. Use para explicar desempenho comercial e encontrar aprofundamentos úteis sobre o negócio.
---

# Diagnosticar vendas e mix

Responda à pergunta de negócio e investigue o que explica o resultado. Use somente ferramentas disponíveis na conexão Sellbie; siga seus schemas e metadados atuais.

## Consultar

- Resolva a empresa com `listar_empresas_disponiveis` e nomes de lojas com `filtros_valores_categoricos`. Reutilize o contexto definido; esclareça apenas ambiguidades que mudem a análise.
- Para indicadores da plataforma, use `shortcutSalesAnalysis`, `shortcutSalesRanking` e `shortcutRankingProducts`. Para evolução visual, use `visualizar_vendas`; para evolução diária entre períodos, `comparar_periodos_vendas`.
- Quando o recorte exigir SQL, consulte primeiro `explorar_dados_empresa` e as definições pertinentes em `consultar_definicoes_metricas`. Execute pelas ferramentas de consulta personalizada. Identifique o resultado como análise personalizada; não prometa equivalência com a tela.

## Interpretar

- Compare períodos com duração, dias da semana e maturação compatíveis. Mês parcial não equivale a mês completo. Horário da consulta não comprova atualização dos dados.
- O resumo padrão de vendas exclui lojas marcadas como fechadas; não transfira essa regra automaticamente para produtos ou SQL. Preserve o recorte da fonte e declare seu efeito histórico. Em análise personalizada, não exclua lojas do histórico apenas pelo estado atual. A comparação pública não garante mesmas lojas: confirme a população antes de usar esse termo.
- Separe lojas sem movimento de lojas com desempenho baixo. Investigue mudança de composição da rede antes de atribuir a variação à operação.
- Decomponha receita em atendimentos e ticket; depois, quando os universos permitirem, em peças por atendimento e valor por peça. Calcule razões pelos totais compatíveis, nunca pela média simples dos tickets. Compradores distintos não são atendimentos e não se somam entre lojas ou períodos.
- Priorize contribuição absoluta e participação, além da variação percentual. Informe bases pequenas; com base zero, mostre a mudança absoluta sem inventar crescimento percentual.
- Diferencie receita, peças e frequência nas compras. Preserve a granularidade de produto ou variante; não interprete receita como margem, vendas como demanda total ou ausência de venda como falta de estoque.
- Nome vazio, genérico ou conflitante é sinal para investigar cadastro. Meça o impacto no universo consultado. Não exclua itens pelo nome ou pela ausência de foto; frete, embalagem e serviços podem ser registros legítimos. Toda classificação ou exclusão adicional deve ter critério explícito, preservando o total original.
- Preserve as regras da métrica para devoluções, preços e cancelamentos. Não remova quantidades negativas como limpeza padrão. Evite multiplicar valores ao juntar itens, compras, cadastros e imagens.
- Em cestas, conte compras distintas com os produtos, deduplicando compra e produto antes dos cruzamentos. Mesmo cliente não significa mesma compra. Participação, confiança ou lift exigem denominadores do mesmo universo; coocorrência não prova efeito de uma oferta.
- Não transforme ausências em zero nem um top N em total da rede. Preserve produtos sem foto e explicite resultados parciais.

## Responder e aprofundar

Apresente o achado principal, empresa, período, recorte e fonte clicável retornada pelo MCP. Separe evidência de hipótese. Use o visual suportado quando ajudar e complemente com interpretação, sem repetir todo o ranking.

Faça a decomposição necessária para responder. Quando houver um sinal útil, sugira um próximo recorte e diga o que ele ajudará a decidir. Por exemplo: ticket menor → peças por atendimento e valor por peça; queda concentrada → mix das lojas afetadas; combinação frequente → distribuição entre lojas. Não transforme uma pergunta simples em uma investigação extensa.

Contexto externo pode ser pesquisado pelas ferramentas do próprio ChatGPT, quando pertinente; não o apresente como causa comprovada pelos dados da Sellbie.
