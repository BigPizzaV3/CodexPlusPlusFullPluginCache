---
name: goal-finish-line
description: Use para definir, preservar, auditar ou concluir objetivos de projetos com Goal Lock, Finish Line, controle de mudanças, detecção de deriva e evidências de aceite.
---

# GFL — Goal & Finish Line Engineering 0.1.1

**Responsabilidade exclusiva:** governar a definição do destino e os critérios verificáveis de conclusão do projeto. Consulte `references/source.yaml` para o contrato canônico, estados, rubricas, gates e exceções. O arquivo é uma especificação declarativa, não um executor e não comprova runtime.

## Ativação proporcional
- Use quando a iniciativa exigir contrato de objetivo/aceite, acompanhamento iterativo, prevenção de deriva, alteração material de escopo ou decisão terminal. Para uma dúvida simples não crie contrato desnecessário.
- Quando não existir contrato, defina `contract_id`, `version`, objetivo, condições obrigatórias da Finish Line, invariantes, exclusões, Stop Rule, Reopen Rule e responsáveis *quando conhecidos*. Distinga campos pendentes; não invente aprovação humana.
- Se já existir GFL Lock, preserve contrato e versão. Mudança material solicita change record autorizado; não use última mensagem como autorização implícita.
- Aplique `goal-finish-line` **antes** de iniciar planejamento 0TG que exija um contrato bloqueado. Entregue a 0TG as referências do contrato e critérios, sem transferir controle sobre Goal/Finish Line.

## Decisão de conclusão
Para cada critério obrigatório, identifique `criterion_ref`, artefato/versão, método, escopo, responsável/validador requerido, evidência resolvível e contradições. Só emita `FINISH_VERIFIED` e a decisão `FINISH` quando todas as condições obrigatórias aplicáveis estiverem comprovadas; caso contrário indique `CONTINUE`, `REALIGN` ou `BLOCK`. Não crie verificações extras após o lock como forma de alterar o aceite. Após conclusão, desenvolvimento material requer `REOPEN` ou `NEXT_GOAL`.

## Contratos com outras skills
- `zero-to-goal`: é responsável pelo plano de marcos e encaminha evidências; não declara conclusão terminal.
- `loop-graph-engineering`: somente se houver desenho de workflow, interdependências/execução controlada que agreguem valor.
- `ask-user-question`: quando faltar escolha ou autorização material que impeça um contrato responsável.
- `gestao-projetos`: recebe resultados e traduz em instrumentos gerenciais, sem alterar a autoridade GFL.

## Integridade
A versão de origem declara `pilot_observation`, não pronta para produção sem validação comportamental, runtime e humana. Preserve esse status; não confunda condição de sucesso planejada com resultado observado nem alegue persistência fora da sessão sem ferramenta e permissão verificadas. Para trabalho longo, devolva um manifesto versionado compacto ao usuário, sem fingir memória permanente.
