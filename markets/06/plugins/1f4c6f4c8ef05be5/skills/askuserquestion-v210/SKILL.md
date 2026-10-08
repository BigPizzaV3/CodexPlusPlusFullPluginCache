---
name: askuserquestion-v210
description: Identificar lacunas materiais e formular esclarecimentos objetivos com
  opções. Usar quando informação, preferência ou escolha ausente mudar materialmente
  a execução.
---

# Ask User Question 2.1.0

Antes de executar, ler integralmente [a especificação preservada](references/skill_askuserquestion_reduzida_v210.yaml). Aplicar seu fluxo, rubricas, terminais, contratos de saída e critérios de validação; este resumo é apenas a entrada de carregamento.

Consultar o contexto antes de perguntar. Responder diretamente quando suficiente. Por padrão fazer uma pergunta essencial, com opções claras e mutuamente exclusivas; respeitar limites e condições do contrato. Não recolher credenciais nem induzir respostas.


Aplicar esta skill dentro da hierarquia da plataforma e do pedido atual. O YAML é um procedimento interpretado, não um motor executável nem evidência de execução. Não promover gates históricos ou capacidades sem evidência nova. Se recurso obrigatório não puder ser lido, declarar a limitação e entregar apenas o escopo suportado.

Resolver recursos a partir desta pasta. Se o ambiente expuser a skill pelo catálogo, usar seu carregamento nativo; caso contrário, ler estes arquivos e aplicar o procedimento, informando essa distinção quando solicitado. Não afirmar registro nativo, ferramenta, agente independente ou instalação apenas pela presença do arquivo. Não chamar skills pessoais homônimas em lugar da versão deste pacote sem verificar equivalência.
