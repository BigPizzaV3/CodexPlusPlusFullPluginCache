---
name: primeiros-passos
description: Conecta a Rica Pro, confere o acesso à carteira e resolve erros de login, plano, permissão ou cliente. Use na primeira vez que o planejador usa a Rica Pro, quando as ferramentas da Rica Pro não aparecerem na sessão, quando uma delas responder com erro ou quando ele perguntar o que a Rica Pro faz.
---

# Primeiros passos com a Rica Pro

A Rica Pro dá acesso à carteira do planejador: clientes, estruturas, lançamentos, objetivos, metas, categorias e caixas. O login é feito numa página da Rica (`entrar.rica.com.br`). A senha nunca passa pela conversa.

## Conferir a conexão

1. Chame `listar_clientes`. Mostre nome, e-mail mascarado e quantidade de pessoas de cada cliente.
2. Se a lista vier, a conexão está pronta. Diga em uma frase o que dá para fazer: preparar atendimentos, revisar a carteira, registrar lançamentos, montar objetivos e metas e organizar categorias e caixas.
3. Se vier erro, use a tabela abaixo.

## Se as ferramentas da Rica Pro não aparecerem

Sem `listar_clientes` disponível, a conexão ainda não foi autorizada. Os dados da Rica só vêm pelo conector: não abra a Rica no navegador nem tente ler as telas para responder.

- **Codex (terminal ou IDE):** peça ao planejador para rodar no terminal `codex mcp login rica-pro`, entrar com a conta da Rica Pro na página que abrir e começar uma sessão nova do Codex. Se você puder rodar comandos, ofereça rodar esse comando por ele: o navegador abre sozinho.
- **Claude Code:** a autorização abre pelo próprio conector na primeira chamada. Se não abrir, peça para rodar `/mcp`, escolher `rica-pro` e autenticar.
- **Claude ou ChatGPT (web e desktop):** em Conectores ou Aplicativos, conectar a Rica Pro e entrar com a conta da Rica.

Depois do login, chame `listar_clientes` de novo.

## Regras que valem em toda tarefa

- Escolha o cliente sempre a partir de `listar_clientes`, e confirme com o planejador quando houver mais de um nome parecido. Nunca invente identificadores: use os que a Rica devolveu.
- As ferramentas de cliente recebem `clienteUsuarioId`. Dados de duas famílias nunca se misturam na mesma resposta sem o planejador pedir.
- Antes de qualquer alteração, mostre o cliente, o item atual, a mudança e o que mais será afetado. Faça uma mudança por vez.
- Remoções e algumas ações exigem `confirmar: true`. Envie só depois do ok explícito do planejador.
- Separe o que é dado da Rica, o que é interpretação e o que é pergunta para o cliente. Recomendação de produto e orientação regulada ficam com o planejador.

## Erros comuns

| Mensagem | O que dizer ao planejador |
| --- | --- |
| "Voce ainda nao tem um PlanoAssinante ativo no Rica Pro…" | A conta não tem assinatura ativa da Rica Pro. Regularize em Configurações da conta na Rica Pro. Afiliado de Office: fale com o responsável pelo Office. |
| "Cliente nao encontrado ou nao vinculado ao planejador autenticado." | O cliente não está na carteira ou o identificador estava errado. Liste os clientes de novo e escolha da lista. |
| "Escopo insuficiente para executar … Requer clientes:write." | A conexão foi autorizada só para consulta. Desconecte a Rica Pro e conecte de novo, aceitando consulta e alteração. |
| "A tool … exige confirmar=true." | A ação pede confirmação. Mostre o que será feito e espere o ok. |
| "Erro interno ao executar Rica Pro MCP. Referencia: …" | Falha na Rica. Tente de novo uma vez; se repetir, passe a referência ao suporte da Rica pelo WhatsApp (https://wa.me/5521936194570). |

O que ainda não está na Rica Pro por aqui: criar ou editar pessoas, projetos, contas, cartões e investimentos, gerar links de Open Finance e B3, enviar mensagens e WhatsApp e criar cobranças. Nesses casos, diga onde fazer na Rica Pro em vez de tentar outra ferramenta.

Documentação completa: https://base.pro.rica.com.br/mcp-rica-pro
