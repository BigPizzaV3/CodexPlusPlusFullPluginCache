---
name: conselho-ia-v122
description: Analisar decisões por seis perspectivas, riscos e trade-offs, ou revisar
  evidências. Usar em decisões estratégicas, múltiplos interessados, efeitos de segunda
  ordem e revisão crítica estruturada.
---

# Conselho de IA 1.2.2

Antes de executar, ler integralmente [a especificação preservada](references/skill_conselho_ia_reduzida_v122.yaml). Aplicar seu fluxo, rubricas, terminais, contratos de saída e critérios de validação; este resumo é apenas a entrada de carregamento.

Selecionar modo e avaliar Value Fit. Aplicar as seis perspectivas e critérios definidos na especificação quando justificados. Preservar evidências, incertezas e dissensos; consenso não valida fatos. Não descrever perspectivas como agentes independentes sem execução comprovada.

Quando houver lacuna material, carregar e aplicar [Ask User Question](../askuserquestion-v210/SKILL.md).
Para avaliação estrutural, carregar [LGE](../lge-v271/SKILL.md).

Aplicar esta skill dentro da hierarquia da plataforma e do pedido atual. O YAML é um procedimento interpretado, não um motor executável nem evidência de execução. Não promover gates históricos ou capacidades sem evidência nova. Se recurso obrigatório não puder ser lido, declarar a limitação e entregar apenas o escopo suportado.

Resolver recursos a partir desta pasta. Se o ambiente expuser a skill pelo catálogo, usar seu carregamento nativo; caso contrário, ler estes arquivos e aplicar o procedimento, informando essa distinção quando solicitado. Não afirmar registro nativo, ferramenta, agente independente ou instalação apenas pela presença do arquivo. Não chamar skills pessoais homônimas em lugar da versão deste pacote sem verificar equivalência.
