---
name: estado-corpus-pt
description: "Consulta a cobertura do acervo português da IAJUS com consultar_acervo e distingue zero medido de secção não medida ou falha."
allowed-tools: mcp__iajus-pt__consultar_acervo, mcp__plugin_iajus-pt_iajus-pt__consultar_acervo
---

# Estado do acervo português (IAJUS)

Se a ligação devolver 401 ou pedir autenticação, oriente o restabelecimento da ligação na aplicação: no ChatGPT, volte a ligar o IAJUS PT através das definições da ligação; no Codex, execute `codex mcp login iajus-pt` e reinicie a sessão. Não peça códigos de acesso nem palavras-passe na conversa. Uma recusa de permissão ou de plano não se resolve repetindo a autenticação: informe o limite devolvido. Se uma ferramenta não estiver listada após a autenticação, informe que está indisponível nesta ligação; não invente nomes nem responda quanto ao mérito jurídico de memória.

Antes de consultar, veja se consultar_acervo está exposta nesta ligação e siga o respetivo esquema. Não suponha que uma ferramenta ausente está disponível.

Use esta consulta para interpretar o recorte de uma pesquisa por tribunal ou precedentes, a atualidade ou uma pesquisa sem resultados. Para a pesquisa e a confirmação de citações, prossiga com pesquisar-jurisprudencia-pt, usando apenas as ferramentas disponíveis; não transforme um resultado vazio de pesquisa num retrato do acervo.

## Consultar

Em consultar_acervo, use consulta.filtros.secao para escolher uma secção: tudo, familias, contadores, orgaos (tribunais) ou qualificadas (precedentes). limite aceita 1 a 500 e, por defeito, é 60; indique-o apenas em tudo ou orgaos, pois as outras secções não aceitam esse parâmetro. Limita a lista ordenada, nunca os totais.

```json
{"consulta": {"filtros": {"secao": "orgaos"}, "limite": 20}}
```

A ferramenta cobre decisões e precedentes portugueses. Não anuncia legislação, tribunais brasileiros nem coleções novas que não tenham sido medidas.

Leia o estado e as_of de cada secção separadamente. Informe quais secções foram medidas e o respetivo instante indicado: uma data anterior é o retrato desse instante e `live` indica medição na própria chamada. Uma secção ausente não foi medida nesta chamada.

## Interpretação

- Só reporte zero medido quando a secção respondeu com medição concluída e total igual a zero.
- Um indicador nao_medido ou NOT_MEASURED, uma secção ausente, um erro ou um tempo de espera excedido não significam zero.
- Se a resposta for parcial, identifique as secções ou partes que ficaram por medir. Uma secção bem-sucedida não valida as restantes.
- Trate as_of como o instante daquela medição. Não afirme atualidade, total final ou completude que a resposta não confirma.

Reporte os valores e a proveniência como foram devolvidos. as_of refere-se à medição do acervo, não à vigência de uma norma nem à data de um julgamento. A cobertura não prova acesso à íntegra de cada documento, direitos de redistribuição, estatísticas privadas ou cobertura de fontes que não aparecem na resposta.
