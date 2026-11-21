---
name: verificar-citacoes-pt
description: "Confere citações de jurisprudência portuguesa uma a uma contra os registos e fontes devolvidos por pesquisar_decisoes e pesquisar_precedentes."
allowed-tools: mcp__iajus-pt__pesquisar_decisoes, mcp__plugin_iajus-pt_iajus-pt__pesquisar_decisoes, mcp__iajus-pt__pesquisar_precedentes, mcp__plugin_iajus-pt_iajus-pt__pesquisar_precedentes
---

# Verificar citações de jurisprudência portuguesa (IAJUS)

Se a ligação devolver 401 ou pedir autenticação, oriente o restabelecimento da ligação na aplicação: no ChatGPT, volte a ligar o IAJUS PT através das definições da ligação; no Codex, execute `codex mcp login iajus-pt` e reinicie a sessão. Não peça códigos de acesso nem palavras-passe na conversa. Uma recusa de permissão ou de plano não se resolve repetindo a autenticação: informe o limite devolvido. Se uma ferramenta não estiver listada após a autenticação, informe que está indisponível nesta ligação; não invente nomes nem responda quanto ao mérito jurídico de memória.

Extraia cada citação e a afirmação que o texto lhe atribui. Consulte a lista de ferramentas desta ligação e use apenas as presentes, com o respetivo esquema. Para pesquisa de raiz, use a skill pesquisar-jurisprudencia-pt.

## Pesquisar cada citação

| Referência | Pesquisa adequada (pesquisar_decisoes, salvo indicação) |
|---|---|
| Número de processo | Tente busca.modo textual ou expressao no texto indexado; compare o número e o tribunal nos metadados devolvidos |
| ECLI ou outro identificador literal | Tente busca.modo expressao, com âncora literal e caracteres especiais escapados |
| Excerto citado entre aspas | busca.modo textual com filtros.frase_exata verdadeiro |
| Tese sem número | busca.modo semantica e depois hibrida |
| Número oficial de AUJ | pesquisar_precedentes com busca.numero em n/AAAA e busca.filtros.tipo auj; distinga-o do número de processo |
| URL ou entity_id | Compare com os dados devolvidos; não há pesquisa direta por estes campos nesta ligação |

Exemplo para um excerto entre aspas:

```json
{"busca": {"modo": "textual", "consulta": "abuso de direito na modalidade de venire contra factum proprium", "filtros": {"frase_exata": true}}}
```

Construa busca segundo o modo e os filtros portugueses que esse modo aceita (ver pesquisar-jurisprudencia-pt). Para o número oficial de AUJ, por exemplo, use `{"busca": {"numero": "1/2024", "filtros": {"tipo": "auj", "tribunal": "pt_stj"}}}`. O número foi publicado no [Diário da República em 02/02/2024](https://diariodarepublica.pt/dr/detalhe/acordao-supremo-tribunal-justica/1-2024-840060199); isso não garante a sua presença no acervo IAJUS. Uma pesquisa de texto pode encontrar uma decisão que menciona o identificador, sem ser a decisão pedida.

## Veredictos

- CONFIRMADA: encontrou o registo e os campos ou excertos devolvidos sustentam a parte específica verificada. Se só confirmam a identidade, não apresente a tese como confirmada.
- DIVERGENTE: identificou o registo e um dado devolvido contradiz a afirmação; indique precisamente a diferença. Um campo ausente não é divergência.
- NÃO LOCALIZADA: uma pesquisa concluída não encontrou a referência. Significa apenas que não foi localizada neste pedido e recorte, não que a citação seja necessariamente fabricada.
- NÃO VERIFICÁVEL: erro, tempo de espera excedido, resposta parcial, medida indisponível ou excerto insuficiente para comparar a afirmação.
- FORA DE ÂMBITO: legislação, doutrina ou jurisprudência de outro ordenamento.

Reaja aos sinais da pesquisa como em pesquisar-jurisprudencia-pt: input_contract_refused, corrija a entrada; filtro_nao_suportado ou filtros_ignorados, preserve a restrição e informe que ela não foi aplicada. Só repita por modalidade ou fonte suportada com recorte equivalente; remover ou enfraquecer a restrição exige a escolha do utilizador; parcial com janela_limitada, continue pelo cursor. Em pesquisa incompleta com falha_busca ou timeout, declare o pedido original NÃO VERIFICÁVEL; uma tentativa mais estreita não completa o recorte original. Confirme a identidade pelos campos disponíveis: um acórdão que apenas cita o número não é o processo citado.

Separe a confirmação de identidade pelos metadados da confirmação de uma afirmação pelo excerto. Votos, resultado, fundamentação ou tese exigem texto que os sustente; sem ele, declare a afirmação NÃO VERIFICÁVEL. Se o utilizador contestar o veredicto, volte a consultar com os identificadores disponíveis e indique o que conseguiu confirmar.

Nunca confirme de memória. Respeite `uniformizador_valido` e os avisos, quando devolvidos: um acórdão que cita um AUJ não é necessariamente o ato uniformizador. Não infira força vinculativa, aplicação ao caso ou vigência pela classificação. A data do julgamento não prova a redação nem a vigência de uma norma nessa data: para isso, remeta para a fonte normativa oficial adequada.

Esta ligação não tem ferramenta para ler a íntegra da decisão, consultar relações entre acórdãos ou o histórico de redações de um precedente. Se a afirmação depender do que não foi devolvido, declare-a NÃO VERIFICÁVEL. Preserve a ligação de origem e a proveniência indicadas, sem presumir oficialidade pelo domínio; uma ligação não prova que a íntegra foi lida nem concede direitos sobre o texto. Se não houver ligação utilizável, diga-o ou peça a decisão ao utilizador.

No final, conte cada veredicto separadamente e destaque as citações não localizadas ou não verificáveis.
