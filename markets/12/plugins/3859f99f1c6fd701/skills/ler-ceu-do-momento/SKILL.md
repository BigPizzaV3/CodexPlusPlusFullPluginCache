---
name: ler-ceu-do-momento
description: Responder perguntas sobre o céu de agora ou de uma data — fase da Lua, Lua fora de curso, signo da Lua, Mercúrio e outros planetas retrógrados — com a ferramenta ver_ceu_do_momento, com datas e horas exatas no fuso da pessoa.
---

# Ler o céu do momento (Lunarea)

## Passos
1. Chame `ver_ceu_do_momento`. Sem data, use o momento atual; para "amanhã", "sexta" ou uma data
   específica, envie `data` (AAAA-MM-DD) e, se fizer sentido, `hora`.
2. Os horários saem no fuso da pessoa quando o ChatGPT o informa; senão, no horário de Brasília. Se a
   pessoa pedir os horários de outro lugar, envie `fuso_horario` no formato IANA (ex.: `Europe/Lisbon`,
   `America/New_York`).
3. Responda primeiro o que foi perguntado (ex.: "Sim, Mercúrio está retrógrado até 13/11"), depois
   complemente com uma ou duas informações úteis do painel. O cartão já mostra o restante.

## Termos
- Fases: a ferramenta usa as oito fases, com os mesmos nomes do app da Lunarea (Lua Nova, Lua
  Crescente, Quarto Crescente, Lua Gibosa Crescente, Lua Cheia, Lua Gibosa Minguante, Quarto
  Minguante, Lua Minguante), cada uma uma faixa de 45° de distância entre a Lua e o Sol. Informa
  também a % iluminada e se a Lua está crescendo ou minguando. Nas próximas fases aparecem os
  instantes exatos: Lua Nova, Quarto Crescente, Lua Cheia e Quarto Minguante.
- Lua fora de curso: do último aspecto exato da Lua com um planeta (Sol a Plutão) até ela entrar no
  próximo signo.

## Cuidados
- Não transforme o céu do momento em previsão garantida; fale em tendências e simbolismo.
- Não invente datas: use só as devolvidas pela ferramenta.
