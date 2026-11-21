---
name: loop-graph-engineering
description: Use quando for necessário projetar ou auditar workflows, loops, agentes, grafos, dependências, ferramentas, recuperação, validação ou side effects; aplica LGE 2.10.2 com menor arquitetura suficiente.
---

# LGE — Loop and Graph Engineering 2.10.2

Fonte técnica canônica: `references/source.yaml` (completa, versão 2.10.2). Ler os blocos pertinentes à demanda: `ativacao`, `requisitos_formais`, `fluxo_execucao`, `saidas`, `criterios_de_aceite`, `seguranca_e_operacao`, `dependencias_e_integracoes`. A referência completa é material especificativo, não implementação executável.

## Decisão arquitetural
1. Avalie risco, objetivo, necessidade de coordenação, artefatos, estado, side effects e capabilities realmente disponíveis; não converter ausência de descrição de efeitos em ausência de efeitos.
2. Escolha o **primeiro nível suficiente** em: `direct_solution` → `structured_prompt` → `bounded_loop` → `graph` → `graph_with_human_gates`. Nem todo projeto precisa de grafo, multiagente ou laço.
3. Use Graph IR tipado somente se dependências, branches, concorrência ou controles não puderem ser representados suficientemente por plano simples. Se gerar IR, valide identificadores, arestas, terminais atingíveis, contratos I/O, condições, finitude de loops, limites e gates.
4. Concurrency exige independência real, permissão e consistência de escrita; número de agentes não prova diversidade epistêmica. Validators requerem evidência independente na extensão do contrato. Falha de validator bloqueante deve produzir resultado de falha, não aprovação silenciosa.
5. Side effects de alto impacto exigem gate humano pré-ação e capacidades verificadas; não construir adaptador de runtime como verificado sem evidência de versão/capabilities; não prometer paralelização ou execução automática pela mera inclusão da skill.
6. Fixe critérios de aceite antes da execução; registre falhas observadas para regressão, evite loops de reparo sem limites, e distinga progresso observado de avaliação autoreferente.

## Articulação com as demais skills
- `goal-finish-line` fornece Goal/Finish Line e autoridade sobre conclusão; LGE não redefine contrato.
- `zero-to-goal` fornece o plano e as precedências de negócio; Graph IR, quando cabível, descreve *controle técnico de execução*, sem se tornar outra fonte de verdade para marcos.
- `ask-user-question` é acionada para escolhas materiais faltantes; não roteie pergunta meramente decorativa.
- `gestao-projetos` mantém o vínculo com governança, EAP, riscos, recursos e decisões reais.

## Proveniência e estado
Metadados originais: `implementation_candidate`; gates comportamentais, execução e revisão humana ainda devem ser validados. Dependências citadas na origem (como CEE/GE ou AskUser v2.1.0) são referências históricas, não prova de instalação. Nesta distribuição, a skill de esclarecimento disponível é a v2.1.2, com contrato de integração em `../../gestao-projetos/references/orquestracao-competencias.md`. Ausência de runtime externo exige saída conceitual, contrato e limites, nunca declaração falsa de execução.
