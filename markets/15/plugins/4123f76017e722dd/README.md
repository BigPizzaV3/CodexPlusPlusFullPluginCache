# Rica Pro

Plugin oficial da [Rica Pro](https://rica.com.br) para planejadores financeiros. Com ele, o Claude, o Claude Code, o ChatGPT e o Codex consultam e atualizam a carteira do planejador na Rica: clientes, estruturas, fluxo de caixa, categorias, patrimônio, objetivos, metas, lançamentos e o catálogo da consultoria.

É preciso ter uma assinatura ativa da Rica Pro. Cada planejador entra com a própria conta e vê só os clientes da sua carteira.

## O que vem no plugin

- **Conector Rica Pro**: servidor MCP remoto em `https://pro.mcp.rica.com.br/mcp`, com 83 ferramentas (50 de consulta e 33 de alteração).
- **Skills** com os roteiros do planejador:
  - `primeiros-passos`: conectar, conferir o acesso e resolver erros;
  - `preparar-atendimento`: pauta, consultas durante a reunião e resumo depois;
  - `revisar-carteira`: prioridades da semana, pipeline, atendimentos e Office;
  - `diagnostico-financeiro`: estrutura, gastos, patrimônio e previdência cadastrada;
  - `registrar-lancamentos`: criar, corrigir e remover lançamentos, parcelados e recorrentes;
  - `objetivos-e-metas`: objetivos, realizações e metas, financeiros ou de hábito;
  - `organizar-taxonomia`: categorias, conceitos, caixas e templates.

## Como o acesso funciona

Na primeira chamada, o aplicativo abre o login da Rica em `entrar.rica.com.br` (OAuth 2.0 com PKCE). A senha não passa pelo Claude nem pelo ChatGPT. São pedidas duas permissões: `clientes:read`, para consultas, e `clientes:write`, para alterações. Remoções exigem `confirmar: true`, e as skills mostram os dados antes de qualquer gravação.

Para cortar o acesso, remova ou desconecte a Rica Pro no aplicativo.

## O que o plugin envia e recebe

O plugin não roda código na sua máquina. Ele só declara o conector remoto da Rica e as skills (arquivos de texto). Os pedidos vão do aplicativo de IA para `pro.mcp.rica.com.br`, operado pela Social Rica Ltda. As respostas chegam com e-mails mascarados e sem tokens de Open Finance, documentos completos ou dados de pagamento. Tudo o que o conector devolve fica na conversa e segue as regras do aplicativo de IA que você usa.

## Instalar

No Claude Code:

```text
/plugin marketplace add https://github.com/felipebzreis/rica-pro-plugin.git
```

Depois, num segundo comando:

```text
/plugin install rica-pro@rica
```

No Codex:

```bash
codex plugin marketplace add https://github.com/felipebzreis/rica-pro-plugin.git
```

Depois, instale o plugin e entre com a conta da Rica Pro:

```bash
codex plugin add rica-pro@rica
```

```bash
codex mcp login rica-pro
```

O segundo comando abre o login da Rica no navegador. Feito o login, abra uma sessão nova do Codex. O Codex de terminal ainda não abre esse login sozinho na conversa.

No Claude (web e desktop) e no ChatGPT, procure **Rica Pro** no diretório de conectores e plugins ou adicione o conector personalizado `https://pro.mcp.rica.com.br/mcp`.

## Links

- Documentação: https://base.pro.rica.com.br/mcp-rica-pro
- Suporte: https://base.pro.rica.com.br/ajuda
- Privacidade: https://socialrica.com.br/politicadeprivacidade
- Termos de uso: https://socialrica.com.br/termosdeuso

## Licença

Os arquivos deste plugin são distribuídos sob a licença MIT. O serviço Rica Pro e a marca Rica não estão cobertos por ela.
