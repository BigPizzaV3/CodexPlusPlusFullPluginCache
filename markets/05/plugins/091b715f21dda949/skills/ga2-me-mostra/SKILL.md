---
name: ga2-me-mostra
description: "Use quando o usuário pedir para ver, desenhar ou explicar visualmente um caso, fluxo, problema, mudança ou decisão de gestão descrito no pedido ou na conversa atual; não use para assuntos sem um caso de gestão."
---

# Me Mostra — Gestão Visual GA 2.0

## Regra principal

Quando houver um caso de gestão identificável, sempre termine com um artefato HTML. Leia
`references/metodo.md` por inteiro antes de criar o visual. Mostre o menor visual que permita
entender o caso e decidir.

## Objeto do visual

Determine o objeto antes de escolher o formato:

1. Se o pedido atual nomeia um caso, processo, artefato ou decisão, esse é o objeto.
2. Se usa “isso”, “aqui”, “o que falamos”, “este caso” ou apenas “me mostra”, use o caso ou
   artefato de gestão mais recente da conversa atual.
3. O nome do plug-in ou da habilidade serve apenas para invocá-la. Nunca o use como objeto por
   padrão. Mostre o método Gestão Ágil 2.0 somente quando o usuário pedir isso explicitamente.

Prenda a resposta aos elementos concretos disponíveis no caso, como números, etapas, pessoas,
bloqueios ou decisões. Quando a conversa contiver dois ou mais desses elementos, use pelo menos
dois deles no título, na leitura ou na prova.

Se não houver um caso de gestão identificável, não gere HTML nem substitua o assunto pelo método.
Faça somente uma pergunta curta para o usuário indicar qual situação de gestão deseja visualizar.

## Linguagem obrigatória

- Escreva em português simples e direto.
- Use a palavra comum antes do termo técnico.
- Explique toda sigla na primeira aparição, na mesma linha.
- Evite inglês quando houver uma palavra comum em português.
- Aplique a regra no título, rótulos, legendas, dicas, texto alternativo e resposta final.
- Releia apenas o texto visível antes de entregar. Jargão solto reabre o trabalho.

## Como conduzir

1. Confirme o objeto usando o pedido atual e o histórico da conversa.
2. Escreva a pergunta que o visual responde.
3. Escolha a pergunta que libera a próxima decisão.
4. Separe o que é medido, estimado e ainda está em aberto.
5. Escolha um visual principal: fluxo, quadro, antes e depois, causa, matriz ou linha do tempo.
6. Gere o HTML com pergunta, leitura direta, visual, prova e consequência.
7. Feche com o que ficou claro, o que segue em aberto e o próximo passo.

Use `assets/template-artefato.html` como ponto de partida. O HTML deve funcionar sem rede,
biblioteca externa ou imagem remota.

## Entrega por ambiente

- No Claude, use Artifact quando esse recurso estiver disponível.
- No Codex ou GPT, use o artefato ou a visualização exposta na sessão.
- No Cursor, use sua prévia ou visualização disponível.
- Em outro ambiente, use o recurso equivalente.
- Não escolha pela marca do modelo. Verifique o que o ambiente oferece.
- Sem recurso nativo, salve `.md` e `.html`, mostre um resumo visual no terminal ou no chat e
  informe o caminho do HTML.

Nunca entregue apenas Markdown, Mermaid, imagem ou diagrama de terminal. O HTML é obrigatório.

## Critério de pronto

- O visual principal responde à pergunta em até 90 segundos.
- O significado continua claro sem cor.
- Fato, estimativa e ponto em aberto não se misturam.
- Título e rótulos não contêm sigla ou jargão sem explicação.
- O objeto é o caso de gestão ativo, nunca o nome do plug-in por padrão.
- A entrega gerou HTML e usou a melhor forma disponível no ambiente.
