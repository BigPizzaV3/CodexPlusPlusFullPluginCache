---
name: desenvolver-clientes-e-campanhas
description: Analise a base de clientes, recorrência, retenção, reativação e campanhas com dados da Sellbie. Use para interpretar resultados de relacionamento e propor próximos aprofundamentos ou hipóteses de ação.
---

# Desenvolver clientes e campanhas

Conecte os indicadores à decisão de relacionamento do usuário. Use as ferramentas disponíveis na conexão Sellbie e as definições da própria plataforma.

## Consultar

- Resolva a empresa com `listar_empresas_disponiveis`. Use `filtros_valores_categoricos` para nomes de lojas e campanhas; campanhas exigem período. Reutilize o contexto já definido.
- Use `shortcutCRMAnalysis` para o resumo da base e `shortcutCRMTimeline` para sua evolução. Para campanhas, use `shortcutCampaignReport`, `shortcutCampaignRanking` e `shortcutCampaignMetrics`, conforme resumo, ranking ou detalhe.
- Consulte `consultar_definicoes_metricas` quando o significado ou denominador do indicador for necessário à conclusão. Para aprofundamentos personalizados permitidos, confira o catálogo com `explorar_dados_empresa`; não reconstrua por SQL um valor de campanha como se fosse o da tela.

## Interpretar

- Preserve período, filtros e população de cada fonte. Os relatórios públicos atuais de campanhas representam a marca, sem recorte garantido por loja. Não use esses totais como resultado de uma loja nem os divida por vendas de uma loja.
- Diferencie receita atribuída de receita incremental. Crescimento, atribuição e taxas de conversão não demonstram causalidade. ROI, ROAS e margem exigem custos e bases compatíveis disponíveis.
- Diferencie conversão em compras de conversão em compradores. Confira denominador e escala retornada; não multiplique novamente uma taxa já expressa em percentual. Diferencie variação percentual de pontos percentuais.
- Não some compradores distintos ou receitas sobrepostas entre campanhas e envios. Prefira o consolidado da fonte; um ranking não representa necessariamente todo o resultado. Se resumo e detalhe divergirem, preserve e identifique ambos, sem inventar a explicação.
- Compare volume e eficiência com o tamanho da base, objetivo, canal e tempo de observação disponíveis. Taxa alta sobre poucos impactados exige contexto; não invente um limiar universal de relevância.
- Valide recência, base ativa, churn e LTV pelas definições Sellbie. Recência pode representar intervalo entre compras; a janela de atividade depende da empresa; LTV não deve ser apresentado automaticamente como previsão de lucro futuro.
- Relacione o desempenho a novos, retidos, resgatados e não identificados quando os dados permitirem. Cobertura de identificação limita conclusões sobre clientes; não generalize a parte identificada para toda a base.
- Em coortes de recompra, use a mesma janela de acompanhamento. Clientes recentes sem tempo para recomprar não são perda comprovada. Não infira histórico de aberturas de e-mail a partir da data da última abertura.
- Preserve ausências e resultados parciais. Confira semanas e meses incompletos; horário da consulta não é atualização da fonte. O dashboard mensal aceita mês completo ou mês atual até ontem: explicite o período retornado.

## Responder e aprofundar

Explique o principal resultado, seu recorte e a fonte clicável retornada pelo MCP. Se o link não aplicar o período, indique o ajuste necessário na tela. Use linguagem de negócio, sem expor SQL, IDs ou nomes internos de relatórios.

Sugira um aprofundamento ligado ao achado: queda de base → novas entradas e retenção; muita receita e baixa conversão → alcance e perfil do público; maior frequência de contato → resposta e recorrência. Diga qual decisão essa investigação ajuda a tomar.

Ao propor uma ação, identifique a hipótese e o indicador de acompanhamento, sem prometer ganho. O catálogo atual não oferece disparos, uploads ou exportação de clientes. Pesquisa externa pode usar ferramentas do próprio ChatGPT; diferencie esse contexto da evidência interna.
