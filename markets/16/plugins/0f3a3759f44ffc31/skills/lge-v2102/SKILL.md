---
name: lge-v2102
description: Use para projetar, avaliar ou auditar workflows de contratações públicas com dependências, estado, validação, loops ou coordenação; não usar em redação simples sem arquitetura.
---

# Loop and Graph Engineering (LGE) 2.10.2

Esta é uma skill complementar do **DIGG.IA: Assistente de Contratações Públicas**. A especificação canônica fornecida pelo usuário encontra-se em [references/skill_LGE_v2_10_2.yaml](references/skill_LGE_v2_10_2.yaml), preservada integralmente. **Ler e aplicar a especificação quando esta skill for acionada**; este arquivo não substitui suas rubricas, triggers, non-triggers, critérios e limites.

## Acionamento proporcional

- Primeiro verificar segurança, objetivo e contexto; selecionar a menor arquitetura suficiente, sem impor grafo, múltiplos agentes ou loops para tarefas simples.
- Acionar ao desenhar ou auditar fluxos de DOD, ETP e TR que exijam dependências, revisão iterativa, passagem de responsabilidade, estados, validação ou gates humanos. A simples elaboração e revisão de um documento usa as skills específicas de contratações, não esta skill.
- Respeitar em especial `ativacao.triggers`, `ativacao.non_triggers`, `value_add_policy`, `materiality_policy`, `fluxo_execucao`, `validacao_e_auditoria` e `criterios_de_aceite` do YAML.
- Preservar a hierarquia normativa e as regras documentais da skill `../contratacoes-publicas/SKILL.md`. Fluxos concebidos não substituem verificação vigente da Lei nº 14.133/2021, normas do MPGO, modelos originais e decisão administrativa humana.
- Não tratar papéis lógicos como subagentes independentes, nem afirmar capacidade de ferramentas, integração, registro ou teste de execução não verificados. Loops/retries devem possuir limite e condição de parada.
- Quando depender de esclarecimento material, perguntar apenas o dado bloqueante; quando não houver dependência externa ou validador, limitar explicitamente o alcance da entrega.

## Estado e dependências

A LGE 2.10.2 está classificada no YAML como `implementation_candidate`, não como release com comprovação comportamental. Dependências externas citadas pela especificação, inclusive a skill Ask User Question e motores de execução, **não são instaladas nem disponibilizadas automaticamente por este pacote**. Empregar os recursos disponíveis de forma transparente, sem inventar equivalência ou integração.
