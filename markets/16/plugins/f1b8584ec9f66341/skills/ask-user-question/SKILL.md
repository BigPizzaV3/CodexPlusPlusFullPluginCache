---
name: ask-user-question
description: Use para decidir se é indispensável pedir esclarecimento, restrição, escolha ou autorização material em projetos e, quando necessário, formular pergunta neutra, objetiva e de baixa fricção.
---

# Ask User Question 2.1.2

Fonte canônica: `references/source.yaml`, especialmente `activation`, `decision_rubrics`, `execution_flow`, `outputs`, `security_and_operation`. É um contrato de comportamento textual; não fornece automaticamente ferramenta interativa de coleta.

## Regra de acionamento
Faça triagem de segurança antes da elicitação. Pergunte apenas quando escolhas ou dados **materiais** ausentes modificarem escopo, governança, risco, validação, custo, autoridade ou resultado; ou quando o usuário pedir perguntas. Antes de perguntar, examine o que já consta na conversa e documentos. Não pergunte dados já fornecidos. Em pedidos objetivos ou detalhados sem lacunas críticas, responda com premissas explicitamente reversíveis.

## Pergunta mínima
Use **uma pergunta** por padrão, máximo de três quando estritamente necessário. Cada pergunta terá de duas a quatro opções equilibradas; rótulos curtos (até cinco palavras), opções sem indução e opção neutra quando apropriada. Apresente uma frase contextual antes da pergunta. Em ausência de UI nativa, renderize texto simples; nunca alegue botões reais ou confirmação inexistente. Encerre a solicitação de escolha e não finja ter recebido a resposta.

## Limites e compatibilidade
Não coletar credenciais, dados sensíveis irrelevantes, usar opções manipuladoras ou contornar recusas. Escalona à `goal-finish-line` para mudanças de objetivo e à `loop-graph-engineering` para bloqueios de arquitetura; `zero-to-goal` espera o dado material em vez de forjar baseline, prazos e aprovações. Esta fonte é `implementation_candidate` e a UI real depende da plataforma. Nenhum mecanismo de interação é garantido pela simples presença do YAML.
