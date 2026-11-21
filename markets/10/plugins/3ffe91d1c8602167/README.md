# Humanizar Texto BR — plugin 0.1.4

Pacote portable para Codex e ChatGPT com um servidor MCP remoto e uma skill de uso. O servidor é implementado separadamente na aplicação Next.js deste repositório. O ZIP não hospeda nem ativa esse servidor.

A integração atende contas gratuitas e assinantes existentes, usando a mesma franquia, reserva atômica, histórico e recuperação do site. Não oferece compra, checkout ou promoção de assinaturas pelo plugin. A presença no diretório depende de aprovação e publicação; não garante recomendações, instalações ou clientes pagantes.

A versão 0.1.4 esclarece na listagem os casos de produtividade de escrita (e-mails, relatórios e rascunhos), após o scan do portal não confirmar a categoria Productivity. A skill é idêntica à 0.1.3.

## Arquivos

- `plugin.json`: identidade, listagem e cinco casos positivos/três negativos para revisão.
- `mcp.json`: endpoint autenticado de produção, `https://www.humanizartexto.com.br/mcp`.
- `skills/humanizar-texto/SKILL.md`: operação e recuperação segura.
- `assets/logo.png`: ícone existente da aplicação, copiado sem alteração.

O nome legal do desenvolvedor vem de `src/config/legal.ts`. A identidade empresarial foi aprovada no portal em 07/10/2026. Os cinco casos positivos e três negativos foram executados no cliente em 08/10/2026, com instalação privada separada e conta dedicada. O manifesto inclui a URL do walkthrough com capturas reais; não inclui credenciais nem resultados de scans do portal. A versão 0.1.3 acrescenta um limite explícito para pedidos de imagens após a observação no caso N2 da 0.1.2. O reteste explicou que o plugin só reescreve textos e recusou a garantia sobre detectores; ainda ofereceu uma ferramenta externa de imagens, sem executá-la. Essa ressalva permanece registrada. Os demais resultados pertencem à versão 0.1.2.

## Estado e teste no cliente

A implementação fica desligada por padrão (`MCP_ENABLED=false`). Em produção, foi ativada em 01/10/2026 após migrações, publicação Git e verificação HTTPS/OAuth. O pacote completo foi validado em conversas novas do Codex e ChatGPT contra banco isolado; os resultados e limites dessa evidência estão em `../../docs/mcp-plugin.md`.

O ChatGPT web aceita este ZIP com MCP direto, mas atualmente apresenta essa configuração como disponível apenas no aplicativo desktop. Para uso privado na web, registre o endpoint como aplicativo MCP OAuth e importe uma cópia da skill com `.app.json` referenciando o ID real dessa conexão; essa cópia não é o pacote de distribuição pública. Não inclua credenciais no ZIP.

Após autorização e validação do ambiente, instale pelo fluxo de plugins documentado do cliente, conecte a conta por OAuth com login por Google ou código de e-mail e teste em uma conversa nova:

> Consulte meu saldo e humanize no estilo Formal: Venho por meio deste solicitar o relatório até amanhã.

Verifique as três ferramentas, a identidade da conta, o histórico e o consumo. Teste também a recuperação com a mesma chave, saldo insuficiente, acesso de outra conta, expiração e revogação. A aceitação de JSON/ZIP ou um build não prova funcionamento no cliente.

## Distribuição pública

1. Concluir os testes de banco e OAuth/UI em ambiente isolado (ver `../../docs/mcp-plugin.md`).
2. Publicar o servidor HTTPS estável e os avisos de privacidade e suporte, após autorização.
3. No portal, selecionar organização/projeto e identidade verificada; verificar domínio e scans.
4. Executar os cinco casos positivos e três negativos em contas de teste com orçamento autorizado; gravar um walkthrough acessível. Fornecer acesso de revisão somente no formulário seguro do portal.
5. Submeter o ZIP à revisão e publicar somente com autorização e aprovação.

O ZIP inclui o MCP desde a primeira versão, como exige a rota atual para futura integração pública. Instalação e testes privados não equivalem a submissão, aprovação ou publicação no diretório. A preparação local foi concluída em 08/10/2026: acesso de revisão independente, testes reais, histórico sem duplicação e vídeo acessível sem login. A validação no ChatGPT móvel ainda não foi realizada. Upload do draft, verificação do domínio e scans foram autorizados em 08/10/2026 e estão em preparação. Submissão para revisão e publicação permanecem fora do escopo autorizado. O roteiro e a evidência ficam em `../../docs/plugin-submission.md`.

Walkthrough: [testes reais da conta de revisão](https://drive.google.com/file/d/1y3QtpFwgbpHNk_B98PG1Pcbpngdj9xxg/view?usp=drivesdk). O vídeo é uma montagem declarada de capturas do cliente, sem simulação nem credenciais.

Fontes consultadas em 30/09/2026: [pacotes](https://developers.openai.com/plugins/build/plugins), [autenticação](https://developers.openai.com/plugins/build/auth), [submissão](https://developers.openai.com/plugins/deploy/submission) e [regras comerciais](https://developers.openai.com/plugins/plugin-guidelines).
