---
name: ementor
description: "Encontra mentores do eMentor para um objetivo, desafio ou tema de carreira e leva a pessoa ao perfil ou ao agendamento da mentoria."
---

# eMentor

Use esta skill quando a pessoa pedir para encontrar, recomendar ou comparar mentores para um objetivo de desenvolvimento.
Mencionar mentoria, eMentor ou selecionar `@eMentor` não exige executar uma busca.

Não chame `buscar_mentores` para explicar conceitos (como a diferença entre mentoria e coaching),
revisar um currículo ou redigir uma mensagem para um mentor. Nesses casos, responda ao pedido
diretamente ou peça o material necessário. Não acrescente recomendações de profissionais sem solicitação.
O app público não consulta sessões, dados privados, disponibilidade ou preços e não envia mensagens.

## Como buscar

1. Chame a tool `buscar_mentores` do servidor MCP `ementor` com um `briefing` que resuma, em uma ou duas frases, o objetivo da pessoa: área, momento de carreira e o que ela quer desenvolver. Escreva o briefing no idioma da conversa.
2. Se o pedido for vago demais para uma boa busca (por exemplo, só "quero um mentor"), faça uma pergunta curta sobre o objetivo antes de buscar.
3. Use `limit` entre 3 e 5, salvo se a pessoa pedir mais opções (máximo 10).

## Como apresentar

- Os resultados aparecem em cards com os botões "Ver perfil" e "Agendar". Não repita a lista inteira em texto: comente em poucas linhas por que os primeiros mentores combinam com o objetivo.
- Use apenas os dados retornados pela tool. Nunca invente mentores, cargos, preços ou disponibilidade.
- Use apenas as fotos retornadas pela tool; não busque imagens externas para representar os mentores.
- Para agendar, oriente a pessoa a usar o botão "Agendar" do card ou o `link_agendar` do mentor. O agendamento e o eventual pagamento acontecem na plataforma eMentor.
- Se a tool retornar `erro` ou nenhum mentor, diga isso com clareza e sugira reformular o objetivo com outras palavras.
