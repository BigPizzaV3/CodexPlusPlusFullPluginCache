---
name: loop-graph-engineering
description: >-
  Aplicar a Loop and Graph Engineering (LGE) 2.10.2 para escolher a menor
  arquitetura suficiente, organizar fluxos de auditoria documental com estado,
  dependências e validações, controlar evidências, recuperações e gates humanos.
  Usar nas demandas de Verifica VRA como habilidade auxiliar, sem substituir o
  contrato normativo de auditoria nem exigir grafo quando um fluxo simples basta.
---

# Loop and Graph Engineering — LGE 2.10.2

Antes de aplicar, **ler integralmente** `references/skill_LGE_v2_10_2.yaml` deste diretório. Esta é a especificação original enviada pelo responsável, preservada byte a byte.

## Papel e roteamento

- Nas solicitações executadas pela skill `verifica-vra`, aplicar a triagem LGE de segurança, contexto, admissibilidade, efeitos e Value Fit, conforme a referência principal. Selecionar o primeiro nível suficiente: solução direta, prompt estruturado, loop finito, grafo ou grafo com gates humanos. Não introduzir grafo, multiagente ou persistência de forma ornamental.
- O **Verifica VRA** continua responsável pelas regras de auditoria documental, incluindo o objeto VRA já preenchida, limites P0/P1, marco histórico, leitura integral, fundamentação por item e entrega. A LGE governa apenas a organização da execução e da evidência; não relaxa qualquer bloqueio da skill principal.
- Precedência operacional: requisitos de segurança e políticas aplicáveis > objetivo e limites do usuário > contratos de auditoria Verifica VRA > controles auxiliares LGE, quando compatíveis. Caso haja incompatibilidade material, não disfarçar o conflito e não declarar conclusão sem os requisitos de aceite da auditoria.
- Exigir limites finitos em loops/retries e recuperação segura quando necessária. Definir critérios de aceite antes de atribuir resultado; preservar evidência, identificador/versão do artefato, incerteza e decisões humanas. Não equiparar revisão pelo próprio modelo a validação independente.
- Não presumir recursos runtime, agentes, conectores ou Google Docs. Nenhuma ação externa ou gravação é autorizada apenas por esta especificação; encaminhar ações de alto impacto ao gate humano requerido.

## Situações sem complexidade adicional

Pergunta factual simples, revisão textual sem desenho operacional e explicação conceitual não exigem grafo ou múltiplos agentes. A avaliação inicial da proporcionalidade não obriga a emissão de Graph IR nem de relatório LGE separado.

## Estado de validação

A especificação embarcada declara `implementation_candidate`. O carregamento e a validação estática do YAML não demonstram comportamento validado, execução independente, melhoria empírica ou homologação institucional.
