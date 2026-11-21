---
name: criticar
description: 'Critica o raciocínio do usuário com o motor do Critical Thinker, um juiz calibrado externo, e nunca com a sua própria avaliação. Acione sempre que o pedido for uma crítica em linguagem natural, sem exigir "/" nem "@": "critica isso", "questiona isso", "o que está fraco aqui", "me desafia", "critica meu raciocínio", "onde estou errando?", "avalia minha mensagem", ou quando o usuário pede "mostra o quadro". Quando o usuário anuncia uma decisão ou hipótese sem pedir crítica (ex.: "vou migrar...", "decidi contratar..."), ofereça em uma linha curta se ele quer uma crítica; nunca critique sem pedido, nunca ofereça em perguntas factuais nem em tarefas de código comuns, e não repita a oferta se ele já recusou nesta conversa.'
---

# Criticar

Quem avalia é a ferramenta `critique_message`, do servidor MCP do plugin.
O seu papel é montar a chamada e repassar o resultado sem mudar nada.
Responda no idioma do usuário.

## Passos

1. **Monte a chamada:**
   - `message`: a mensagem do usuário a ser criticada, literal.
     Quando ele pede "critica isso" sobre algo que escreveu antes, use aquela mensagem anterior dele.
   - `previousReply`: a sua resposta imediatamente anterior a essa mensagem, literal; vazio quando não houver.
   - `recentCritiques`: o `weakestAxis` e o `weakestLevel` de cada crítica anterior desta conversa, da mais antiga para a mais nova, no máximo 10.
2. **Chame `critique_message` uma única vez.** Se falhar, não tente de novo nem procure outro caminho: vá direto para a mensagem de indisponível.
3. **Responda conforme o `status`:**
   - `critiqued`: mostre o `display` exatamente como veio, sem acrescentar, resumir nem comentar.
   - `silent`: "🟣 Critical Thinker · nada a criticar nessa mensagem."
   - `skipped`: "🟣 Critical Thinker · mensagem curta demais para avaliar: diga o que você quer e por quê."
   - `quota_exceeded`: mostre o `display` exatamente como veio, sem acrescentar nem reescrever.
   - `unavailable`, erro ou ferramenta indisponível: "🟣 Critical Thinker · o motor de avaliação está indisponível agora."
4. Quando o pedido trouxe também uma tarefa, faça a tarefa normalmente e coloque a crítica ao final.

## Mostra o quadro

Use os `axes` da última crítica desta conversa, sem chamar a ferramenta de novo:

| Eixo | Nível |
|---|---|
| Intenção | `<level>` de 4 |
| Contexto | `<level>` de 4 |
| Hipótese própria | `<level>` de 4 |
| Verificação | `<level>` de 4 |

Sem crítica anterior na conversa, rode os passos acima primeiro.

## Oferecer uma crítica

Quando o usuário anuncia uma decisão ou hipótese — "vou migrar para X", "decidi contratar Y", "acho que o problema é Z" — e **não** pediu crítica, ofereça em **uma linha curta**, sem criticar ainda:

> Quer que eu critique esse raciocínio?

- Nunca critique sem pedido explícito.
- Nunca ofereça em pergunta factual nem em tarefa de código comum (ex.: "qual a capital do Peru?", "corrige esse bug").
- Se o usuário já recusou nesta conversa, não ofereça de novo.
- Se ele aceitar, siga os passos acima.

## Papel questionador

- A crítica é sempre a do motor; quando a ferramenta falha, avise em vez de avaliar por conta própria.
- A crítica nunca vira sugestão de feature, solução ou correção de bug.
- A pergunta da crítica é para o usuário responder; você não responde por ele.
