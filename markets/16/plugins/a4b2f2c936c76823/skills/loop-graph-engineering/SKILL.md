---
name: loop-graph-engineering
description: Use para estruturar ou auditar workflows jurídico-administrativos com dependências, loops, estado, validação, recuperação ou gates humanos quando houver ganho material. Não acione para consulta jurídica isolada, explicação simples ou revisão textual sem desenho operacional.
---

# Loop and Graph Engineering — LGE 2.10.2

Esta é uma skill complementar ao **DIGG.IA: Assistente jurídico-administrativo TCU**. Sua fonte normativa interna é a especificação preservada, sem reduções ou reformulações, em [`references/skill_LGE_v2_10_2.yaml`](references/skill_LGE_v2_10_2.yaml). Leia o YAML integral quando esta skill for necessária e aplique seus mecanismos, critérios de ativação, fluxos, segurança e limites.

## Quando acionar

- Projetar ou auditar fluxo de instrução processual, fiscalização, análise de risco, pareceres sequenciados, validação de etapas ou coordenação de equipes, desde que dependências/estado/gates justifiquem a arquitetura.
- Descrever decisões condicionais, controles de aprovação humana, responsabilidades, critérios de aceite, recuperação bounded e rastreabilidade de evidências em um procedimento.
- Avaliar se uma solução direta, instrução estruturada, loop limitado ou grafo é o **primeiro nível suficiente**; não pressupor que grafo ou multiagente são superiores.

## Quando NÃO acionar

- Pergunta jurídica factual simples, explicação normativa ou análise isolada de acórdão.
- Elaboração ou revisão de parecer/despacho sem demanda por desenho operacional.
- Pedido cuja solução simples já atende requisitos, sem ganho material verificável com a LGE.

## Fronteiras de responsabilidade

1. A skill `instructions` continua sendo a fonte do **método jurídico** do plugin: verificação de jurisprudência e legislação, diferenciação entre fatos e inferências, ressalvas institucionais e formato documental proporcional. A LGE **não** cria teses jurídicas, autentica acórdãos ou comprova vigência normativa.
2. A LGE cuida apenas do **projeto de workflows** e de sua validação proporcional. A interpretação do YAML é instrução para o modelo, não a implantação de um motor externo, multiagente real ou API.
3. Aplicar triagem de segurança, **Value Add**, materialidade e limite de iterações. Manter fontes, estado e evidências rastreáveis. Efeitos de alto impacto exigem gate humano pré-ação. Nenhuma execução externa decorre apenas do desenho do grafo.
4. Evitar falsa independência de validação, acesso à API do TCU não configurado, afirmações de execução sem evidência e autopromoção de status de produção.
5. Quando houver escolha material do usuário que impeça a decisão, formular o esclarecimento mínimo. A dependência `skill_askuserquestion_v210.yaml` declarada no YAML **não está embutida neste pacote**; seguir o fallback explícito de perguntar diretamente quando disponível e permitido, sem alegar que outra skill foi carregada.
6. O YAML identifica a LGE 2.10.2 como `implementation_candidate`: a presença no pacote não constitui teste comportamental, integração runtime, autorização de ações ou homologação de produção.

## Entrega

Para tarefas de workflow, entregar o artefato mínimo suficiente, critérios verificáveis e pendências de execução/validação. Se houver análise jurídica, preservar os fundamentos, ressalvas e limites da skill principal. Não obrigar Graph IR ou relatório extenso para trabalho simples.
