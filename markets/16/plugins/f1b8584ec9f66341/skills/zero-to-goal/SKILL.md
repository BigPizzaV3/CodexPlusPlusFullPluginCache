---
name: zero-to-goal
description: Use para criar ou atualizar um plano progressivo do Marco 0 ao Goal, com marcos, atividades, dependências, responsáveis, evidências de aceite, riscos e acompanhamento de desvios.
---

# 0TG — 0 to Goal 0.1.1

Fonte canônica integral: `references/source.yaml`; consultar `ativacao`, `requisitos_formais`, `entradas`, `saidas`, `fluxo_execucao`, `dependencias_e_integracoes` conforme necessário. Esta skill planeja a progressão, não define metas, não executa ações por si e não atesta conclusão final.

## Entrada e responsabilidades
1. Receba `gfl_contract` com `contract_id`, `version`, `goal`, `finish_line`, critérios referenciados, exclusões e Stop Rule. Se houver pedido de novo projeto sem contrato formal, solicite à `goal-finish-line` contrato mínimo conforme complexidade; não imponha formalismo excessivo a demandas simples.
2. Registre **Marco 0** com estado observado, fonte e data de corte, recursos, restrições, lacunas e premissas. Na ausência de dados decisivos, acione `ask-user-question`. Não invente percentuais ou cronogramas.
3. Planeje entregáveis e marcos alinhados aos `criterion_refs` da GFL; decomponha atividades, responsáveis, evidências de aceitação e riscos. Use lista ordenada em casos simples e DAG operacional só quando as dependências justificarem.
4. Precedências obrigatórias não podem formar ciclos. CPM só pode ser calculado com durações comparáveis e precedências suficientes; senão apresente apenas dependências condicionantes. Paralelização exige independência e ausência de conflito de recursos/escrita.
5. Cada marco marcado `ACCEPTED` deve ter evidência resolvível e validação aplicável. Replanejamento registra versão, motivo, impacto nos descendentes e reconciliação; não modifica GFL Lock. Evite repetição não delimitada.
6. Prepare `PREPARE_FINISH` reconciliando todos os compromissos obrigatórios materiais (concluído, substituído autorizado, dispensado autorizado, aberto ou bloqueado); encaminhe evidências e versão à GFL. Somente GFL pode produzir `FINISH_VERIFIED` e decisão `FINISH`.

## Entrega
Plano com baseline, marcos, responsáveis, dependências, critérios de aceite, evidências e estado; resumo de riscos, decisões e ações pendentes. Percentual só com denominador e regra definidos previamente; caso contrário reporte qualitativamente. O `loop-graph-engineering` governa arquitetura técnica apenas quando necessário; `gestao-projetos` complementa EAP, governança, cronograma e comunicação.

## Estado e limites
Fonte original `pilot_observation`; revisões comportamentais, execução e validação humana não realizadas como parte desta incorporação. Dependências LGE 2.10.0/AUQ 2.1.0 citadas no YAML são históricas; o pacote contém LGE 2.10.2/AUQ 2.1.2, integradas por interface, sem alegar equivalência empiricamente provada. Sem persistência autorizada, estado é apenas conversacional ou exportável em manifesto, sem escrita silenciosa externa.
