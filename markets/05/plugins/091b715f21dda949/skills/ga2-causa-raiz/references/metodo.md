# Causa raiz — 5 Porquês, Ishikawa e Pareto

## Objetivo

Causa raiz é o que origina o problema. Sintoma é o que aparece primeiro.

A saída deve ser uma causa de processo, rotina, regra ou sistema, sustentada por evidência. Uma
pessoa nunca é a causa raiz.

Comece somente depois de fechar o diagnóstico e o gap.

## Escolha da ferramenta

| Situação | Ferramenta |
|---|---|
| Uma cadeia provável | 5 Porquês |
| Várias causas simultâneas | Ishikawa, depois 5 Porquês por ramo relevante |
| Causas com contagem de ocorrências | Pareto para ordenar |

## Problema observado

Escreva uma frase com número, unidade, período e fonte.

Ruim: “a fila está grande”.

Bom: “existem 120 chamados abertos e a resposta média foi 72 horas em julho, segundo o painel
de suporte”.

## Os cinco níveis

| Nível | Tipo de resposta |
|---|---|
| Sintoma | o efeito que grita |
| 1 | causa imediata |
| 2 | causa do processo |
| 3 | causa da rotina |
| 4 | causa da regra |
| 5 | causa do sistema |

O número cinco orienta a profundidade. Não force exatamente cinco se a causa de sistema surgir
antes com evidência ou exigir mais um nível. O erro é parar no sintoma.

## Como conduzir os 5 Porquês

Para cada nível:

1. Pergunte por que a resposta anterior acontece.
2. Pergunte como sabemos que isso é verdade.
3. Registre a evidência.
4. Se não houver evidência, marque `hipótese`.
5. Proponha um teste para confirmar ou enfraquecer a hipótese.

| Nível | Pergunta | Resposta | Evidência | Estado | Teste pendente |
|---|---|---|---|---|---|
| Sintoma | O que acontece? | | | medido | — |
| 1 | Por que o sintoma acontece? | | | | |
| 2 | Por que a resposta 1 acontece? | | | | |
| 3 | Por que a resposta 2 acontece? | | | | |
| 4 | Por que a resposta 3 acontece? | | | | |
| 5 | Por que a resposta 4 acontece? | | | | |

## Três testes de fechamento

### Teste de pessoa

Pergunte: a causa é processo ou regra, ou é o nome de alguém?

Reescreva “a analista esqueceu de conferir” como “o processo não exige conferência antes do
envio”.

### Teste de retorno

Pergunte: se corrigirmos somente esta causa, o problema volta?

Se voltar, a resposta ainda é sintoma ou causa parcial.

### Teste de controle

Pergunte: o dono controla esta causa?

Ataque o nível mais profundo que o dono controla. Registre o nível acima como dependência,
gate ou decisão externa.

## Ishikawa — espinha de peixe

Use quando várias causas podem agir ao mesmo tempo.

| Categoria 6M | O que investigar |
|---|---|
| Método | processo, regra, padrão, sequência |
| Mão de obra | capacidade, carga, treinamento, clareza de papel |
| Máquina | sistema, ferramenta, equipamento, automação |
| Material | dados, arquivos, insumos, entradas |
| Medição | indicador, fonte, frequência, visibilidade |
| Meio ambiente | prazo, local, mercado, dependência externa, restrição |

Uma categoria pode ficar vazia. Não invente causa para preencher o desenho.

Depois do levantamento:

1. elimine causas sem relação plausível;
2. marque evidências e hipóteses;
3. escolha os ramos por impacto, frequência e controle;
4. rode 5 Porquês nos ramos escolhidos.

Ishikawa sem ramo escolhido é decoração.

## Pareto

Use apenas quando houver contagem consistente.

| Causa | Ocorrências | Percentual | Acumulado |
|---|---:|---:|---:|
| | | | |

Ordene do maior para o menor. As primeiras causas orientam a prioridade. Não force a regra
80/20 quando os dados não mostrarem essa concentração.

## Causa prioritária

Pode haver várias causas reais. Escolha uma prioritária por:

- maior frequência;
- maior impacto;
- maior capacidade de agir agora.

Explique o critério. Registre causas profundas fora do controle como dependências.

## Formato para o A3

Escreva a conclusão em até duas frases:

> A causa raiz é [processo ou regra], sustentada por [evidência]. A causa acionável neste ciclo
> é [causa], porque [critério de prioridade].

Anexe a cadeia completa e o Ishikawa quando o caso for robusto.

## Armadilhas

- parar no segundo porquê;
- pular do sintoma para “falta de cultura”;
- culpar pessoa;
- responder sem evidência;
- assumir causa única;
- preencher Ishikawa sem escolher ramo;
- escolher uma causa tão profunda que ninguém controla;
- confundir uma solução desejada com causa.
