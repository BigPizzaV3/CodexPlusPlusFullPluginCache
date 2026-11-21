---
name: pesquisar-jurisprudencia-pt
description: "Pesquisa jurisprudência portuguesa com pesquisar_decisoes e pesquisar_precedentes, escolhendo a modalidade e os filtros que cada uma aceita e preservando a proveniência."
allowed-tools: mcp__iajus-pt__pesquisar_decisoes, mcp__plugin_iajus-pt_iajus-pt__pesquisar_decisoes, mcp__iajus-pt__pesquisar_precedentes, mcp__plugin_iajus-pt_iajus-pt__pesquisar_precedentes, mcp__iajus-pt__consultar_acervo, mcp__plugin_iajus-pt_iajus-pt__consultar_acervo
---

# Pesquisar jurisprudência portuguesa (IAJUS)

Se a ligação devolver 401 ou pedir autenticação, oriente o restabelecimento da ligação na aplicação: no ChatGPT, volte a ligar o IAJUS PT através das definições da ligação; no Codex, execute `codex mcp login iajus-pt` e reinicie a sessão. Não peça códigos de acesso nem palavras-passe na conversa. Uma recusa de permissão ou de plano não se resolve repetindo a autenticação: informe o limite devolvido. Se uma ferramenta não estiver listada após a autenticação, informe que está indisponível nesta ligação; não invente nomes nem responda quanto ao mérito jurídico de memória.

Veja primeiro as ferramentas expostas nesta ligação e use apenas as que aparecem, segundo o respetivo esquema. Para conhecer o recorte antes de pesquisar por tribunal ou de concluir que não há resultados, consulte consultar_acervo, se estiver disponível, e indique o estado e o as_of da secção relevante. Se a medição estiver indisponível ou for parcial, diga-o e prossiga com a pesquisa possível, sem alegar cobertura completa. Pesquise decisões com pesquisar_decisoes e precedentes qualificados com pesquisar_precedentes; confira depois cada citação como indicado em verificar-citacoes-pt.

## Escolher a modalidade

| Intenção | busca.modo |
|---|---|
| Questão por significado e termos complementares | hibrida |
| Tema ou conceito, sem exigir correspondência literal | semantica |
| Termos presentes no texto, frase exata ou tentativa por número de processo | textual |
| Padrão literal ou forma de citação (por exemplo um ECLI) | expressao |

A entrada é fechada e varia por modo; consulta é obrigatória em hibrida, semantica e textual, e expressao é obrigatória em expressao. Use apenas filtros que o modo aceita:

- hibrida: tribunal, classe, tipo_recurso e os campos comuns;
- semantica: tribunal, um único ano e kind;
- textual: tribunal, classe_sigla, frase_exata e os campos comuns;
- expressao: tribunal, classe_sigla, ignorar_maiusculas, allow_unindexed_scan e os campos comuns.

Os campos comuns são ano_min, ano_max, data_julgamento_min e data_julgamento_max (AAAA-MM-DD), relator, orgao_julgador, tipo e tipo_unidade. limite vai de 1 a 100 e, por defeito, é 20; ajuste à quantidade pedida. Em textual e expressao há também ordenar_por (textual: relevancia, ano ou tamanho; expressao: ano ou tamanho), direcao_ordenacao (asc ou desc) e tamanho_pagina. Os códigos de tribunal aceites vêm do acervo: consulte a secção orgaos de consultar_acervo em vez de os adivinhar.

Exemplos (os argumentos completos de cada chamada):

```json
{"busca": {"modo": "hibrida", "consulta": "responsabilidade civil do médico por falta de consentimento informado", "filtros": {"ano_min": 2015}, "limite": 10}}
```

```json
{"busca": {"modo": "textual", "consulta": "abuso de direito", "filtros": {"frase_exata": true}}}
```

Para obter mais resultados, repita consulta, filtros e limite com page_info.next_cursor em busca.cursor. Pare na quantidade pedida ou quando não houver continuação; não percorra todas as páginas sem necessidade. Híbrida, semântica e textual percorrem uma janela de até três páginas, limitada a 100 resultados; expressão usa a paginação do executor e pode não ter cursor na pesquisa sem índice. Fim da janela ou truncated não prova fim do acervo: refine o recorte. Cursor expirado, inválido ou ranking alterado exige reiniciar, sem contar a primeira página repetida como novos resultados.

Em expressao, use uma expressão regular POSIX com âncora literal e escape os caracteres especiais dos identificadores. Só permita allow_unindexed_scan quando o pedido justificar uma pesquisa sem essa âncora. ignorar_maiusculas não elimina diferenças de acentuação.

## Pesquisa por número de processo

Esta ligação não tem modo dedicado de pesquisa por número de processo. Pode tentar o número em textual, que procura no texto indexado, ou usar expressao para um padrão literal; nenhuma modalidade garante localizar a decisão pelo identificador:

```json
{"busca": {"modo": "textual", "consulta": "1234/19.4T8LSB"}}
```

Restrinja ao tribunal com filtros.tribunal quando o utilizador o indicar. Use o número fornecido, sem o converter nem completar de memória. Para um ECLI, experimente expressao com âncora literal; também pesquisa texto indexado. Compare processo, tribunal, data e identificadores com os metadados devolvidos: uma decisão que apenas cita o número não é necessariamente a pedida. Não há consulta direta por entity_id ou URL nesta ligação. Zero resultados não prova que o processo não exista.

## Precedentes

pesquisar_precedentes exige busca.filtros.tipo. Para um acórdão uniformizador, use tipo auj e, quando conhecido, o número oficial em busca.numero, no formato n/AAAA ou n.º n/AAAA. Este número é diferente do número do processo. tribunal é opcional (por exemplo pt_stj) e incluir_canceladas é verdadeiro por defeito:

```json
{"busca": {"numero": "1/2024", "filtros": {"tipo": "auj", "tribunal": "pt_stj"}, "limite": 5}}
```

O número deste exemplo foi publicado no Diário da República em 2 de fevereiro de 2024. A presença do acórdão no IAJUS depende do acervo consultado. [Publicação oficial](https://diariodarepublica.pt/dr/detalhe/acordao-supremo-tribunal-justica/1-2024-840060199)

O campo `limite` aceita até 10 resultados. Esta pesquisa não tem cursor, ordenação configurável ou filtro por matéria. Para explorar um tema, pesquise também decisões. Preserve os estados e avisos devolvidos. Um resultado curto ou vazio descreve apenas a consulta efetuada.

Leia `uniformizador_valido` em cada resultado quando existir: se for falso, não apresente o acórdão como uniformizador, mesmo que o tipo devolvido seja `auj`. Preserve a indicação de classificação inconsistente; um acórdão de Relação que cita um AUJ não é por isso o ato uniformizador. Distingua a identidade do precedente, o que o sumário sustenta e a sua eventual autoridade ou aplicação ao caso: não presuma força vinculativa, vigência ou aplicabilidade a partir da classificação. Não há histórico de redações dos precedentes nesta ligação.

## Resultado e citação

Cite apenas elementos devolvidos: tribunal, número do processo ou do AUJ, data, excerto e ligação de origem quando presentes. Diga se dispõe apenas de metadados ou de um excerto; uma ligação não prova que a íntegra tenha sido lida nem concede direitos sobre o texto. Preserve a proveniência e eventuais limites de direitos, sem rotular uma ligação como oficial apenas pelo domínio. Se a ligação ou a íntegra não estiver disponível, diga-o. Um excerto não sustenta afirmações que não contém.

A data do julgamento situa o acórdão; não prova a redação nem a vigência de uma norma nessa data ou hoje. Se a pergunta depender do direito aplicável num dado momento, consulte a fonte normativa oficial adequada e indique que a pesquisa jurisprudencial, por si, não verifica a vigência.

Uma pesquisa concluída sem resultados é zero para esse pedido e recorte. Erro, tempo de espera excedido, interrupção, resposta parcial ou medida indisponível não são ausência. Não trate o limite de resultados como censo nem afirme completude.

## Recusas e selos da pesquisa

Leia error_code, busca_status (completa, parcial ou incompleta), busca_motivos, aviso_busca e filtros_ignorados antes de responder:

- input_contract_refused: a entrada não foi lida (expressão regular malformada, tipo inexistente). Reformule como a mensagem indicar e repita; não é falha do acervo.
- filtro_nao_suportado, ou filtros_ignorados não vazio: o filtro nomeado não foi aplicado. Preserve a restrição do utilizador e informe essa limitação; não apresente resultados como se o recorte tivesse sido aplicado. Só repita através de outra modalidade ou fonte suportada se mantiver o mesmo filtro e um recorte equivalente. Se isso exigir remover ou enfraquecer a restrição, pare e pergunte ao utilizador se pretende uma pesquisa mais ampla.
- parcial com janela_limitada: viu-se apenas uma janela. Continue com page_info.next_cursor ou refine o recorte; a lista não é o conjunto.
- incompleta, com falha_busca ou timeout: a pesquisa não terminou. Se repetir com um recorte mais estreito, identifique-o; o resultado não completa o pedido original. Indique a falha da pesquisa original, nunca «não encontrado».
- completa com zero resultados: zero medido neste recorte; diga que não consta do acervo para este pedido e, se vier link_pesquisa_geral, ofereça-o como pesquisa pública do tribunal.

## Fundamentação

Identifique tribunal, processo, data e relator pelos metadados ou excertos devolvidos. Votos, resultado, fundamentação e tese exigem um excerto que os sustente; sem ele, diga que não localizou esse dado, sem completar de memória. Se o utilizador contestar, repita a pesquisa com os identificadores disponíveis e indique o que o resultado efetivamente confirma.

## O que esta ligação não faz

Não há ferramenta registada para ler a íntegra de uma decisão, obter relações entre decisões ou histórico de redações de um precedente; também não há legislação nem doutrina. Remeta para a ligação de origem devolvida, quando existir, ou peça ao utilizador a decisão. Não substitua a ligação portuguesa pela brasileira.
