---
name: onboarding
description: 'Mostra o valor do Critical Thinker. Use quando o usuário pergunta como funciona, o que ele faz, ou pede uma demonstração ("como funciona?", "me mostra com um teste", "o que você faz?"). No Codex o hook já entrega este bloco; aqui é o fallback, sobretudo para o ChatGPT.'
---

# Onboarding do Critical Thinker

Responda no idioma do usuário.

O contraste vem do **motor**, nunca de você: chame a ferramenta **`onboarding`** do plugin e exiba o campo **`display`** exatamente como veio. Não reescreva, não resuma e não invente eixos ou níveis.

No **Codex**, o hook já injeta esse mesmo `display` no seu contexto a cada mensagem: se ele já estiver lá, apenas exiba-o e **não** chame a ferramenta de novo.

O próprio `display` já termina com a frase **Quando quiser que eu questione seu raciocínio, diga "critica isso".** Repasse o `display` como veio, exatamente como ele terminou, sem repetir essa frase depois nem listar comandos ou atalhos.

Se o motor estiver indisponível, diga que o plugin não conseguiu falar com a API agora e encerre, sem inventar notas.
