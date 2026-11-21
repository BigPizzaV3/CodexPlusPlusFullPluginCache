# AtivoPlay AI 1.0.1 — pacote público

Este diretório contém o manifesto portátil e a configuração do servidor MCP de produção. Nenhuma senha, chave, token ou segredo OAuth faz parte do pacote.

## Arquivos para upload

- `plugin.json`: identidade, apresentação, casos de revisão e notas da versão.
- `mcp.json`: conexão Streamable HTTP com `https://mcp-prod.ativoplay.com.br/mcp`.

## Itens preenchidos no Portal de Desenvolvedores

1. Cadastrar uma conta de testes dedicada somente nos campos seguros do portal; nunca neste pacote.
2. Confirmar no portal que o plugin não realiza pagamentos ou compras, embora a plataforma AtivoPlay tenha planos pagos fora do plugin.

A categoria foi definida como `Productivity`; caso o Portal de Desenvolvedores não ofereça esse título, altere para `Business` antes do upload. `countries: []` foi definido intencionalmente para não restringir a distribuição por país.

O suporte público usa `https://www.ativoplay.com.br/#contactModal`, validado em navegador com abertura direta do formulário de contato.

O `mcp.json` declara o cliente OAuth público predefinido, seus endpoints, resource e escopos. O cliente não usa segredo (`tokenEndpointAuthMethod: none`). O pacote não contém `client_secret`, token da API, chave de assinatura, segredo de introspecção nem arquivos `.env`.

Esta versão usa a chave lógica `ativoplay-prod` para que o Portal de Desenvolvedores crie uma nova conexão MCP, sem reutilizar o registro OAuth incompleto salvo antes da inclusão do `clientId`.
