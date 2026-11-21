---
name: interpretar-mapa-astral
description: Calcular e interpretar o mapa astral (mapa natal) de alguém nascido em qualquer cidade do mundo, em português, com a ferramenta calcular_mapa_astral — Big Three, planetas nas casas e aspectos — com tom acolhedor e sem previsões deterministas.
---

# Interpretar mapa astral (Lunarea)

## Entrada
- Data de nascimento e cidade de nascimento, em qualquer país. A hora é necessária para Ascendente,
  Meio do Céu e casas.
- Se faltar data ou cidade, peça tudo de uma vez. Se pedir por formulário, use estes quatro campos de
  texto, nesta ordem e nada mais: Data de nascimento (DD/MM/AAAA, digitada, sem calendário), Horário de
  nascimento (HH:MM, se souber), Cidade onde nasceu e Estado ou país. Nunca invente a hora: se a pessoa não souber, calcule sem hora e
  diga o que fica de fora.
- Envie `estado` e `pais` quando a pessoa disser (ex.: "Toledo, PR", "Paris, França", "Springfield,
  Illinois"). Cidades do Brasil não precisam de país.
- Converta datas como "12/03/1990" para `1990-03-12` e horas como "2 e meia da tarde" para `14:30`.

## Passos
1. Chame `calcular_mapa_astral`. Se a resposta disser que há mais de um lugar com aquele nome, pergunte
   à pessoa qual é (o cartão mostra as opções) em vez de escolher por ela — a não ser que a conversa já
   deixe claro. Se a cidade não for encontrada, peça a grafia certa ou a cidade maior mais próxima.
2. O cartão já mostra a mandala e as posições: não repita a tabela inteira.
3. Interprete nesta ordem, em português do Brasil, com parágrafos curtos:
   - Big Three: Sol (essência), Lua (emoções) e Ascendente (jeito de se apresentar), considerando as casas.
   - Equilíbrio de elementos e modalidades, só se houver algo marcante (ex.: nenhum planeta em Fogo).
   - Três a cinco aspectos mais exatos (menor orbe), explicando o que cada um sugere.
   - Planetas em casas ou temas específicos só se a pessoa pedir.
4. Repasse os avisos da ferramenta (cidade escolhida entre homônimas, hora desconhecida, horário de
   verão, Lua mudando de signo no dia).
5. Ofereça aprofundar um tema (amor, trabalho, um planeta específico).

## Cuidados
- Astrologia como linguagem simbólica de autoconhecimento: use "sugere", "pode indicar", nunca
  "vai acontecer".
- Não preveja morte, doença, acidentes, gravidez, traição ou resultados financeiros, e não recomende
  decisões de saúde, dinheiro ou direito com base no mapa.
- Não invente posições: use só os dados devolvidos pela ferramenta.
- Não ofereça planos, assinaturas ou produtos.
