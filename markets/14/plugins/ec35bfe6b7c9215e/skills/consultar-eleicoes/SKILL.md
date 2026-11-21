---
name: consultar-eleicoes
description: Consulte o acervo eleitoral Arvor de 2022 e 2026, nos dois turnos, por meio do MCP. Use para resultados presidenciais por território ou seção e diagnósticos de logs, encerramentos e recebimento do segundo turno de 2026.
---

# Consultar eleições

Use as ferramentas do MCP Arvor Eleições conectado no aplicativo. O endpoint é
`https://arvor.co/api/eleicoes/mcp`, público e somente de leitura. A skill não
contém o dataset nem configura a conexão automaticamente quando instalada sozinha.
Se as ferramentas não estiverem disponíveis, explique a dependência e indique
a conexão pelo aplicativo; não invente resultados ou simule uma consulta.

Consulte `arvor_eleicoes_cobertura` para identificar o snapshot, fontes, universos
e limitações. Não apresente o acervo congelado como apuração em tempo real.
Use o esquema de ferramentas que o servidor disponibilizar na sessão.

- Para votos, comparecimento, municípios, zonas e seções, leia
  [resultados](references/resultados.md).
- Para horários, logs, relógios e recebimento, leia
  [tempos](references/tempos.md). Esses diagnósticos cobrem apenas 2026/2.

Apresente o recorte, ano, turno, denominador e inclusão/exclusão do exterior.
Cite a fonte e a data do snapshot devolvidas pelo servidor; inclua o SHA quando
o usuário precisar reproduzir ou auditar a conta. Use os links retornados;
o produto é https://arvor.co/eleicoes e o acervo https://brasil.arvor.co/.
Não transforme ausência de campo em zero nem extrapole uma amostra paginada.
Resolva o nome do candidato no próprio ano/turno: números não identificam a
mesma pessoa em eleições diferentes.

Os logs não identificam o candidato escolhido nem o voto de uma pessoa.
Atrasos e sinais de relógio são diagnósticos, não demonstração de fraude ou
alteração de votos. O servidor não altera resultados nem prevê eleições futuras.

Em erro de argumento, corrija o filtro com base no esquema e na mensagem.
Em resposta grande, reduza `limite`. Em 429, respeite Retry-After quando houver
e faça no máximo uma nova tentativa; evite rajadas ou buscas paralelas massivas.
Em indisponibilidade, informe que a consulta não foi concluída e preserve o que
foi confirmado. Não substitua dados ausentes por lembranças do modelo.
