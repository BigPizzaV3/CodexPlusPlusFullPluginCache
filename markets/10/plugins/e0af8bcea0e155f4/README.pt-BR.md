# Asking MCP

[English](./README.md) | **Português (BR)**
[![smithery badge](https://smithery.ai/badge/askinghq/asking-mcp)](https://smithery.ai/servers/askinghq/asking-mcp)

Plugin que conecta assistentes de IA (Claude, ChatGPT, Cursor, VS Code e outros
clientes compatíveis com MCP) ao seu atendimento no
[Asking](https://asking.com.br) via MCP.

Com a sua permissão, o assistente lê conversas, mensagens, contatos e os
relatórios do seu papel, cria notas internas e rascunhos de resposta e atualiza
status, prioridade, etiquetas e responsável. Quando a conexão inclui o escopo de
envio, ele também responde e inicia conversas em seu nome — sempre com
consentimento por escopo, registro na auditoria e revogação imediata.

## Servidor

- URL (Streamable HTTP): `https://app.asking.com.br/mcp`
- Autenticação: OAuth com os escopos `mcp:read`, `mcp:write` e `mcp:send`

## Como conectar

1. No seu cliente, adicione um servidor MCP remoto com a URL acima.
2. O navegador abre a página de consentimento do Asking — entre com sua conta de
   sempre (e-mail ou Google).
3. Se você participa de mais de uma conta, selecione a conta que quer conectar.
4. Revise os escopos e aprove. Dependendo do cliente, a primeira chamada de
   ferramenta é o que abre o consentimento no navegador.

Menus e nomes variam entre clientes e versões; procure a opção de adicionar um
servidor MCP remoto ou um conector personalizado.

### Claude

Abra **Configurações > Conectores**, adicione um conector personalizado e cole
`https://app.asking.com.br/mcp`. Conclua o consentimento no navegador.

### ChatGPT

Abra **Configurações > Conectores** e crie um conector personalizado com a URL.
Conectores personalizados dependem do plano e da liberação gradual; se a opção
não aparecer na sua conta, ainda não é possível conectar.

### Cursor

Abra **Configurações > MCP**, adicione um novo servidor MCP, escolha a opção
HTTP e cole a URL. Você também pode adicioná-lo em `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "asking": {
      "url": "https://app.asking.com.br/mcp"
    }
  }
}
```

### VS Code

Abra a Paleta de Comandos e execute **MCP: Add Server**, escolha **HTTP** e
cole a URL. Você também pode adicioná-lo em `.vscode/mcp.json`:

```json
{
  "servers": {
    "asking": {
      "type": "http",
      "url": "https://app.asking.com.br/mcp"
    }
  }
}
```

### Claude Code

Adicione o servidor pelo terminal:

```bash
claude mcp add asking --transport http https://app.asking.com.br/mcp
```

### Codex

Adicione o servidor pelo terminal:

```bash
codex mcp add asking --url https://app.asking.com.br/mcp
```

### Outros clientes

Qualquer cliente MCP com suporte ao transporte Streamable HTTP pode se conectar
à URL acima; os nomes exatos dos menus variam por cliente.

## Documentação

Passo a passo completo e limites por plano:
<https://docs.asking.com.br/hc/asking-documentation/articles/asking-conectar-assistentes-de-ia-via-mcp>

## Licença

MIT — veja [LICENSE](./LICENSE).
