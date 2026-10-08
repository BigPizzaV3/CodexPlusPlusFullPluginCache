# Resultado dos testes de execução — Gestão Ágil 2.0

Data: 03/09/2026
Versão do plug-in: 0.2.1
Ambiente de regressão: Codex CLI, execução isolada e somente leitura
Modelo: GPT-5.5
Resultado estrutural: **10/10 casos válidos**
Resultado da regressão afetada: **3/3 aprovados**

| Caso reexecutado | Resultado | Evidência principal |
|---|---|---|
| positive-05-visual | Aprovado | Usou Aprovação como objeto, preservou 8 de 12 dias e seis de 14 itens bloqueados, gerou HTML e destacou a decisão. |
| positive-06-visual-contexto-ativo | Aprovado | Recuperou da conversa os 12 dias atuais, os sete dias de espera pela diretoria e a meta de cinco dias; não explicou o método. |
| negative-04-visual-fora-do-escopo | Aprovado | Respondeu somente “Qual situação de gestão você quer visualizar?”, sem HTML e sem usar o método como assunto. |

Os outros sete casos continuam com as habilidades responsáveis inalteradas e mantêm o resultado
8/8 registrado na versão 0.2.0. A validação estrutural confirmou seis casos positivos, quatro
negativos, 30 habilidades e seis trilhas.

## Alterações de instrução

- O objeto do visual agora é resolvido primeiro pelo pedido atual e depois pelo caso de gestão mais recente da conversa.
- O nome do plug-in ou da habilidade é tratado somente como invocação, não como assunto padrão.
- Sem caso de gestão identificável, a habilidade faz uma pergunta curta e não gera HTML.
- O visual do próprio método só é permitido quando o usuário o pede explicitamente.

## Limitações do ambiente de teste

- A falha original ocorreu no ChatGPT Go e foi confirmada pela captura da conversa.
- A regressão foi executada localmente no Codex; o teste final no ChatGPT Go depende da versão 0.2.1 estar disponível no diretório público.
- Avisos de outras habilidades instaladas e conexões externas sem autenticação não pertencem a este plug-in e não alteraram os resultados acima.
