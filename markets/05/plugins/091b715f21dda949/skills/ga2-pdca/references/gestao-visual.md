# Me Mostra — Gestão Visual GA 2.0

## Finalidade

Transformar uma situação de gestão no menor visual que permita entender o caso e decidir sem
perguntar de novo. Esta referência cuida da leitura visual. O arquivo do artefato GA 2.0 cuida
dos campos, critérios e regras do conteúdo.

Quando ambos se aplicarem, construa primeiro o artefato e depois apresente o mesmo conteúdo em
HTML. Não crie um segundo artefato paralelo. Use para processo, estado, mudança, problema,
prioridade, responsabilidade, dependência, cadência ou gate. Não use para ilustração artística,
peça de marketing ou mockup de interface.

## Sequência

1. Escreva a pergunta que o visual responde em uma frase.
2. Escolha a pergunta que libera a próxima decisão e declare o recorte.
3. Classifique a intenção: estado atual, mudança, diagnóstico ou decisão.
4. Marque cada fato ou número como medido, estimado ou em aberto. Registre fonte e data.
5. Aplique o artefato GA 2.0 dono do conteúdo.
6. Escolha uma primitiva visual principal.
7. Preserve origem, destino e ponto de decisão; corte os ramos que não mudam a leitura.
8. Gere um HTML com pergunta, leitura, visual, prova e consequência.
9. Feche com o que o visual prova, o que segue em aberto e a próxima ação ou decisão.

## Roteamento para os artefatos

| Sinal no pedido | Artefato dono | Visual indicado |
|---|---|---|
| norte, futuro, contexto estratégico | Canvas de Visão | passado → hoje → tendência → visão |
| atual, desejado, meta, gap | Diagnóstico | atual × desejado e régua do gap |
| problema, causa e plano | Relatório A3 | lado esquerdo → lado direito |
| causa raiz | 5 Porquês ou Ishikawa | cadeia dominante ou causas paralelas |
| ação, dono e prazo | 5W2H | plano por linha ou linha do tempo |
| projeto, produto ou processo | Briefing | mapa dos 3 Ps e fronteiras |
| projeto ou fluxo contínuo | Decisão Projeto ou Fluxo | árvore de decisão |
| objetivo, KR e iniciativa | OKR Canvas | objetivo → resultado-chave → iniciativa |
| prioridade | Matriz Impacto × Esforço | matriz 2 × 2 e fila resultante |
| jornada, entregas e fatia fina | Backlog 2D | mapa 2D e corte do primeiro ciclo |
| colunas, WIP e bloqueio | Kanban Canvas | quadro com limite e idade |
| limite, urgência ou congestionamento | Políticas de WIP | fluxo com limite e classe crítica |
| passo recorrente | POP | gatilho → passos → exceção → saída |
| papéis e responsabilidade | Quem Faz o Quê | raias ou matriz curta |
| autonomia de decisão | Delegação | assuntos × níveis de delegação |
| meta e capacidade do ciclo | Plano do Ciclo | linha do ciclo e carga a 70% |
| andamento diário | Gestão Diária | fotografia do quadro e bloqueios |
| prometido contra entregue | Review | antes/depois com prova |
| manter, melhorar e parar | Retrospectiva | três colunas e uma ação escolhida |
| melhoria em ciclos | PDCA | Plan → Do → Check → Act |
| melhoria pequena | Quadro Kaizen | sinal → aposta → aprendizado → decisão |
| hipótese e teste | Folha de Experimento | hipótese → protótipo → teste → critério |
| números para decidir | Painel do Gestor | três a cinco números-âncora |
| conversa difícil | Canvas CNV | fato → sentimento → necessidade → pedido; sem HTML |

Se o pedido nomeia o artefato, use esse artefato. Se nomeia uma decisão, use o artefato que
possui a decisão. Se só pede entendimento, use a fonte do estado. Sem artefato aplicável,
produza somente a leitura visual; não invente um componente do método.

## Primitivas visuais

| Relação que precisa aparecer | Primitiva | Regra principal |
|---|---|---|
| ordem, handoff ou espera | fluxo | rotule a condição apenas quando ela muda o caminho |
| distribuição, limite, idade e bloqueio | fotografia Kanban | mostre limite na coluna e bloqueio no cartão |
| papéis e esperas | raias | pessoa e executor ficam em linhas distintas |
| meta e gap | atual × desejado | compare a mesma medida, unidade, escopo e período |
| regra ou processo alterado | antes × depois | destaque só o ponto que mudou |
| falha | esperado × observado | destaque a primeira divergência |
| cadeia dominante de causa | 5 Porquês | cada elo pede evidência |
| causas paralelas | Ishikawa | cada ramo traz evidência e fonte |
| origem e destino de um item | dependência ou linhagem | foco destacado, contexto comprimido |
| escolha por duas dimensões | matriz | posição sem critério medido fica estimada |
| respostas que mudam o caminho | árvore | cada folha termina em decisão ou aberto |
| cadência ou marcos | linha do tempo | compromissos usam datas exatas |
| três a cinco números | painel | número sem fonte não vira gráfico |
| muitos atributos exatos | tabela | priorize leitura precisa, não decoração |

Use um visual principal por pergunta. Acrescente uma tabela curta apenas como legenda ou prova.
Remova um nó: se a decisão não mudar, mantenha o nó removido. Tire as cores: o significado deve
continuar legível. Leia apenas título, foco e fechamento: a resposta deve continuar clara.

## Semântica fixa

- Base: contexto necessário, sem destaque.
- Foco: elemento que responde à pergunta.
- Exceção: risco, bloqueio ou divergência.
- Prova: fonte, data e procedência perto do dado.
- Teal: marca, medido e ok.
- Laranja: risco e estimativa.
- Cinza: em aberto.

Não dependa só da cor. Use rótulo, texto, borda, ícone textual ou forma para repetir o sentido.

## Molde da fonte Markdown

```markdown
# <pergunta que o visual responde>

## Leitura
<resposta direta em uma frase>

## Visual
Intenção: <estado atual | mudança | diagnóstico | decisão>
Primitiva: <tipo escolhido>
<visual principal>

## Prova
| Afirmação | Selo | Fonte e data |
|---|---|---|
| | medido / estimado / em aberto | |

## Decisão ou próximo passo
- O que acontece agora:
- Dono: <nome ou não definido>
- Data: <data ou não definida>
- Gate: <decisor ou nenhum>
```

## Contrato do HTML

Toda execução visual gera HTML. Use a melhor superfície realmente disponível:

1. preview HTML interativo exposto pela sessão;
2. Canvas ou visualização equivalente que aceite a fonte HTML;
3. arquivo `.html` autocontido e fonte `.md` equivalente.

Não presuma capacidade por plano, marca ou modelo. Não invente tag, tool call, link ou preview.
Se o recurso nativo falhar sem correção objetiva, use o arquivo autocontido.

O HTML precisa:

- usar a pergunta como título;
- responder em uma frase na abertura;
- conter um único visual principal;
- pôr fonte, data e selo perto de cada número;
- encerrar com consequência, pontos em aberto e próxima decisão;
- funcionar sem rede, CDN, biblioteca, fonte ou imagem externa;
- usar SVG inline apenas quando ele revelar uma relação melhor que uma tabela;
- adaptar-se a celular e aos temas claro e escuro;
- preservar leitura sem cor.

Estrutura mínima:

```html
<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Pergunta do visual</title>
  <style>/* estilos internos, responsivos e sem dependência externa */</style>
</head>
<body>
  <main>
    <header><h1>Pergunta</h1><p>Leitura direta.</p></header>
    <section aria-label="Visual principal"><!-- fluxo, matriz, cartões, SVG ou tabela --></section>
    <section><h2>Prova</h2><!-- fontes, datas e selos --></section>
    <section><h2>Decisão ou próximo passo</h2><!-- consequência e abertos --></section>
  </main>
</body>
</html>
```

## Exemplo didático

Pergunta: Onde o fluxo esperado divergiu do observado?

```text
ESPERADO   gatilho → executar → produzir entregas → leitura → decisão
                       │
OBSERVADO  gatilho → ERRO ───────────────→ nenhuma entrega
                       ^ primeira divergência medida
```

A prova deve registrar a fonte do erro e a contagem observada. O efeito esperado da correção
continua em aberto até uma execução real. Nomes, datas e valores do exemplo nunca viram dados do
caso do usuário.

## Guardrails e pronto

- Não invente dado, causa, dono, prazo, gate ou vínculo.
- Não use fluxograma para esconder incerteza; mostre o aberto.
- Não misture atual e desejado sem rótulo.
- Não destaque tudo.
- A conversa CNV mantém sua exceção de privacidade e não gera HTML.
- O visual deve ser entendível em até 90 segundos.
- Fato, estimativa e aberto permanecem distintos.
- O fechamento nomeia consequência, decisão ou próximo passo.
- O fallback entrega HTML, Markdown equivalente e resumo curto no chat.
