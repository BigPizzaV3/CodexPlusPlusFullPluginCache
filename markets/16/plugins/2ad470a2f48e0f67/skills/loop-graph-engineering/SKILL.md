---
name: loop-graph-engineering
description: "Use ao projetar ou auditar workflows de contratos com dependências, ciclos, estado, validação, gates ou orquestração; escolha sempre a menor arquitetura suficiente. Não acione para simples análise jurídica isolada."
---

# Loop and Graph Engineering (LGE) 2.10.2

Esta é uma **skill complementar** ao `instructions` do plugin **DIGG.IA: Assistente de Contratos Públicos**. A habilidade é acionada condicionalmente para projetar ou auditar fluxos operacionais de gestão/fiscalização contratual que realmente exijam decomposição, loops, dependências, controle de estado ou gates. **O método MAE continua obrigatório para análise do mérito jurídico-contratual.**

Antes de aplicar LGE, ler a [especificação YAML completa](references/skill_LGE_v2_10_2.yaml) e observar os campos `ativacao`, `value_add_policy`, `materiality_policy`, `requisitos_formais`, `fluxo_execucao`, `seguranca_e_operacao`, `validacao_e_auditoria` e `criterios_de_aceite`. O YAML é fonte de instrução estruturada: sua presença não significa que validators, adapters, agentes ou runtimes descritos estejam instalados ou tenham sido executados.

## Ativação e roteamento

1. Aplicar safety e avaliar triggers/non-triggers da especificação. Para dúvida contratual isolada, redação de cláusula e análise MAE sem desenho de processo, **não** ativar arquitetura LGE; continuar pelo `../instructions/SKILL.md`.
2. Quando o desenho operacional for necessário, selecionar o **primeiro nível suficiente** entre `direct_solution`, `structured_prompt`, `bounded_loop`, `graph` e `graph_with_human_gates`. Não inventar capabilities nem agentes autônomos.
3. Só adicionar Graph IR, delegação, retrieval, memória, loop de revisão, reexecução, orquestração ou persistência quando houver Value Add material testável; aplicar budgets finitos, contratos de estado, evidências e gates relevantes.
4. Para atos com efeito externo ou administrativo relevante, distinguir recomendação, proposta e ação. Nenhuma aprovação ou execução material é presumida. Preservar competência humana e fontes normativas.
5. Em sínteses, não considerar consenso de perspectivas do mesmo modelo como validação independente. Caso haja dependência de Ask User Question não disponibilizada no pacote/runtime, perguntar diretamente apenas a lacuna humana material e bloqueante, sem alegar uso da ferramenta ausente.

## Evidência e estado

Preservar proveniência, controle de versões, suficiência de documentos, pendências, critérios congelados e vereditos ligados ao artefato efetivamente verificado. Não alegar que checks ou testes da própria especificação foram executados apenas porque a skill está empacotada. Os documentos jurídicos, o motor Python e o HTML do MAE permanecem como artefatos independentes desta habilidade.

**Estado da especificação LGE:** `implementation_candidate`. A aptidão comportamental e de runtime depende de validação posterior.
