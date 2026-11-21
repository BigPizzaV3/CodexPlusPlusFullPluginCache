# Nexoza para ChatGPT

Pacote portátil Agent Plugins para conectar o ChatGPT ao MCP público da Nexoza.

## Conteúdo

- `plugin.json`: identidade portátil e metadados de publicação.
- `mcp.json`: conexão remota, sem credenciais, com `https://nexoza.com.br/mcp`.
- `assets/icon.png` e `assets/logo.png`: identidade visual oficial da Nexoza.

Documentação pública do MCP: https://nexoza.com.br/docs/mcp

O pacote não contém tokens, senhas, chaves ou dados de clientes. O servidor é público para descoberta e contato, limitado pelas regras do próprio MCP. Os dados de contato são enviados somente quando o cliente confirma explicitamente o envio.

## Como testar

1. Compacte o conteúdo desta pasta mantendo `plugin.json` e `mcp.json` na raiz do ZIP.
2. No painel de Plugins da OpenAI, escolha o upload de um novo plugin.
3. Revise o servidor MCP descoberto e conclua a verificação do domínio.
4. Rode os casos positivos e negativos descritos em `plugin.json`.

Alterações nas ferramentas hospedadas são feitas no MCP e precisam de novo scan no painel. Alterações de metadados ou assets exigem novo ZIP.

## Ponto de revisão de elegibilidade

A Nexoza não cobra, vende serviço digital ou processa pagamento no MCP. Ela pesquisa profissionais publicados, apresenta informação pública e encaminha uma solicitação de contato para negociação direta. Ainda assim, como a experiência conecta clientes a prestadores de serviços digitais, a elegibilidade final deve ser confirmada no fluxo de revisão da OpenAI. O pacote declara esse comportamento de forma explícita e não tenta ocultar sua finalidade.

## Pendências antes da publicação

- Verificar a identidade empresarial no painel da OpenAI.
- Fazer o upload do ZIP e concluir a verificação de domínio.
- Fornecer ao painel um vídeo de demonstração acessível ao revisor, se solicitado.
- Reexecutar o scan do MCP após qualquer mudança nas ferramentas.
