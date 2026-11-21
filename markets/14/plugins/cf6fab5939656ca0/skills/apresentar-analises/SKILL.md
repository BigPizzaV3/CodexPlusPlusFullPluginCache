---
name: apresentar-analises
description: Escolha como apresentar resultados da Sellbie em texto, tabela, gráficos ou cards. Use em análises com comparações, vários indicadores, séries, rankings, produtos ou cestas, respeitando os componentes disponíveis e a preferência do usuário.
---

# Apresentar análises

Escolha o formato pela pergunta e preserve todos os indicadores solicitados. Use os contratos das ferramentas disponíveis; antes de escolher um componente, confira [formatos e limites](references/formatos-disponiveis.md).

## Escolher a apresentação

- Número pontual ou definição: texto breve. Valores exatos, muitas dimensões ou pedido de tabela: tabela no chat.
- Evolução: linhas; ranking: barras; reconhecimento de produtos e combinações: cards com nomes, medida relevante e fotos disponíveis. Não espere um pedido explícito de gráfico quando ele facilitar a leitura.
- Prefira uma chamada visual que cubra a pergunta. Resumo e evolução de vendas no mesmo período usam `visualizar_vendas` com `resumo_e_evolucao`. Envie somente as métricas necessárias; não acrescente gráficos acessórios.
- Compare períodos de uma mesma métrica no mesmo gráfico com `comparar_periodos_vendas`. Preserve datas, duração e convenção de alinhamento. Não calcule ticket do período pela média dos dias.
- Métricas distintas só devem compartilhar eixo com unidades, granularidade e escalas compatíveis. Receita e ticket podem ter escalas incompatíveis mesmo em reais. Não prometa seleção de indicadores, carrossel de gráficos ou normalização que o componente não oferece.
- Para pedido amplo sem métricas definidas, escolha um visual principal e os números complementares relevantes. Se o usuário pedir várias evoluções explicitamente, preserve-as em uma chamada compatível; o componente atual cria um gráfico por métrica. Não omita métricas para encurtar a resposta.
- Para SQL visual, selecione `dimensao` e `metrica` explicitamente quando houver ambiguidade. Não use o primeiro campo numérico por acaso nem altere a fonte oficial apenas para obter um gráfico.

## Acompanhar com texto

Explique o principal achado e sua implicação sustentada, com empresa, período, recorte e fonte clicável retornada pelo MCP. Inclua limitações que mudem a interpretação; detalhes técnicos somente se necessários. Análise personalizada deve ser identificada, sem inventar link para uma tela equivalente.

O texto complementa o visual: não repita todos os pontos, cards ou linhas. Quando útil, sugira um próximo aprofundamento concreto ligado ao resultado. Respeite pedidos explícitos por tabelas e informações completas.

## Preservar o resultado

- Uma chamada visual bem-sucedida já entrega o componente. Não repita a consulta nem produza outro gráfico para renderizar os mesmos dados.
- Se `auto` retornar tabela, use as linhas recebidas no chat, sem nova consulta. As tabelas não ficam dentro do widget.
- Distinga zero, ausência, falha e resultado parcial. Informe truncamento; top N não é total. Não complete lacunas temporais com zero nem gere percentuais sem denominador compatível.
- Use nomes legíveis, unidades e períodos claros. Preserve produtos sem foto; uma imagem pode representar outra variante.
- Se a ferramenta retornar dados sem componente, responda no chat. Se o visual falhar, aproveite os dados já recebidos e explique a limitação, sem alegar que ele foi exibido.
