---
name: loop-graph-engineering
description: "Aplique a LGE 2.10.2 quando a gestão de rotinas exigir projetar ou auditar fluxos com dependências, estado, validação, loops, coordenação ou decisões humanas. Não acione para consultas simples."
---

# Loop and Graph Engineering — LGE 2.10.2

## Fonte integral

Leia integralmente [a especificação LGE 2.10.2](references/skill_LGE_v2_10_2.yaml) **quando a skill for acionada**. O arquivo é o YAML original fornecido e constitui a fonte principal de regras, gatilhos, limites, rubricas, saídas, verificações e casos. Este documento é um ponto de entrada, não uma substituição da especificação.

## Critérios de acionamento

Use esta skill para projetar ou auditar fluxos com dependências materiais, estados, pontos de decisão, responsáveis, validações, loops limitados, coordenação, recuperação ou gates humanos. Avalie antes a adequação ao pedido e selecione a **menor arquitetura suficiente**, na ordem direct_solution, structured_prompt, bounded_loop, graph e graph_with_human_gates. Avaliação de aplicabilidade não implica geração de grafo.

**Não acionar** apenas para resposta factual, revisão textual sem desenho operacional ou explicação conceitual. Se a rotina for simples e o método existente atender, use o fluxo direto de mapeamento do plugin.

## Integração com o Assistente de gestão de rotinas

- A skill principal [instructions](../instructions/SKILL.md) mantém a responsabilidade pelo contexto do MPGO, descrição dos processos, documentos em nove blocos, Mermaid e melhoria contínua; LGE auxilia apenas a estruturação, verificação e governança dos fluxos quando material.
- Preserve evidências, referências, incertezas e competências institucionais. Não trate referências históricas como normas vigentes sem confirmação.
- Distinga arquitetura de execução: Mermaid ou Graph IR é proposta de design, não prova de validação ou execução de processo, ferramenta, agente ou integração.
- Retries, loops, consultas e reparos devem ser limitados e sujeitos a evidência. Ações externas com impacto material exigem autoridade e controle humano apropriados.

## Estado de validação

A origem registra `metadata.status: implementation_candidate` e `production_readiness: blocked_until_behavioral_runtime_human_and_comparative_validation`. A incorporação em ZIP não altera essa condição. Não alegue homologação ou testes comportamentais não realizados.

## Dependências e limites

A LGE pode referir-se a Ask User Question e outros artefatos externos, mas o ZIP não garante sua presença, implantação ou integração. Quando faltar capacidade material, declarar a pendência e não inventar ferramentas, executores, permissões, evidências ou aprovações. Consulte a especificação preservada para fluxos, gates e exceções.
