# Pesagens de compra/entrada e venda/saída

> Versão 0.4.0: os exemplos podem ser adaptados e executados com SQL livre de leitura. Todas as filiais da empresa do login estão autorizadas; TODAS tem esse escopo. O catálogo não exige cadastro de cada SQL. Confirme o esquema real e os critérios do relatório.

Fonte primária: `source/sagi_plsql.prg:7331`, `PLSQL_SYG_MOVIMENTO_PESOS`; assinatura SQL em `:7436`, tipo de retorno em `:7371`. Exemplos de uso: API `server/api/controllers/movimentos.controller.js:73`; portal `src/rotas/financeiro.ts:45` e `src/rotas/operacional.ts:218`. Caminhos são evidências para manutenção pela Sygecom; o cliente não precisa acessar esses projetos.

## Parâmetros de `syg_movimento_pesos`

| Posição | Nome / tipo | Uso confirmado no corpo da função |
|---|---|---|
| 1 | `cMov text` | `ENTRADA` = compra; `SAIDA` = venda. Estes exemplos não usam `TODAS` nem `SERVICO` como movimento |
| 2 | `dIni date` | Data inicial inclusiva; enviar uma data explícita |
| 3 | `dFim date` | Data final inclusiva; `CURRENT_DATE` usa o dia do banco |
| 4 | `cFil text` | Nome da filial, `TODAS` ou lista interna documentada; deve ser controlado pela autorização |
| 5 | `nFor integer` | Na entrada é `codfor`; na saída é `codcli`. `NULL` vira zero, sem filtro |
| 6 | `cCodPro text` | Código do produto; `NULL` vira vazio, sem filtro |
| 7 | `cSubPro text` | Subcódigo do produto; `NULL` vira vazio, sem filtro |
| 8 | `lDiv boolean` | `NULL` vira `FALSE`; nos ramos de boleto exclui `numbol <= 0`. Não significa excluir todos os outros tipos de origem |
| 9 | `lCompCad boolean` | `TRUE` usa comprador/vendedor do cadastro; `FALSE`/`NULL` usa o do movimento. O comentário inicial antigo descreve o inverso; prevalece o corpo lido |
| 10 | `nBol numeric` | Número do boleto; `NULL` vira zero, sem filtro |
| 11 | `cUnidade text` | Unidade da filial, não unidade de medida do produto; `NULL` vira `'0'`, sem filtro |
| 12 | `lpesotudo boolean` | `NULL` vira `FALSE`; `TRUE` inclui peso de boleto e classificação juntos e pode duplicar os valores de um total |

Retorno usado nos exemplos: `data`, `boleto`, `codigo`, `nome`, `placa`, `codpro`, `subcod`, `produto`, `unidade`, `peso_bruto`, `peso_tara`, `peso_liquido`, `desconto`, `preco`, `valor_total`, `filial`, `movimento`, `origem`, `id_recnobol`, `cod_com_ven`, `comp_vend`, `num_coleta`, `estado`. Validar as colunas na versão instalada antes de executar.

## Critérios comuns

Os exemplos preservam os oito `NULL` finais enviados pelo solicitante quando não há filtro específico. A função já aplica regras de pesos/classificação e exclusões do ERP. Não recalcular peso líquido como bruto menos tara, não ativar `lpesotudo` e não adicionar `ABS` às devoluções. Há ramos de devolução com valores negativos; são mantidos nas somas e podem estar fora do período do boleto original.

Uma linha representa item/origem, não necessariamente uma pesagem única. `COUNT(*)` mede linhas do relatório. Quando apropriado, contar boletos por `(filial, movimento, boleto)` e verificar `boleto > 0`, sem somar os valores de cabeçalho repetidos. Não usar `id_recnobol` sozinho como ID global entre origens.

Não somar unidades incompatíveis nem rotular toda quantidade como kg: agrupar pela coluna `unidade`. A função não retorna uma coluna de moeda; totais de `valor_total` dependem da convenção monetária confirmada do relatório/base, sem conversão inventada. Esses valores são de movimentos de compra/venda, não saldos do Financeiro 3.0, valores pagos/recebidos ou lucro.

`TODAS` só pode ser executado quando a ponte garante o conjunto autorizado. Para uma filial, o servidor substitui pelo nome liberado. Para múltiplas filiais, construir apenas a lista a partir do contexto autorizado; nunca aceitar fragmento `IN(...)` digitado pelo usuário como SQL. Totais devem aplicar esse recorte dentro da função.

## P01 — Listar entradas desde 1º de junho de 2026

Pergunta: “Mostre as pesagens de compra desde 01/06/2026 até hoje, com fornecedor, produto e peso líquido.” Projeção da chamada enviada pelo solicitante, em ISO e com limite de listagem.

```sql
SELECT a.data, a.boleto, a.codigo AS fornecedor_codigo,
   a.nome AS fornecedor, a.placa, a.codpro, a.subcod,
   a.produto, a.unidade, a.peso_bruto, a.peso_tara,
   a.peso_liquido, a.valor_total, a.filial, a.origem,
   a.id_recnobol
FROM syg_movimento_pesos('ENTRADA', DATE '2026-06-01',
   CURRENT_DATE, 'TODAS', NULL, NULL, NULL, NULL,
   NULL, NULL, NULL, NULL) a
ORDER BY a.data DESC, a.filial, a.boleto DESC,
   a.origem, a.id_recnobol
LIMIT 100
```

## P02 — Listar saídas desde 1º de junho de 2026

Pergunta: “Mostre as pesagens de venda desde 01/06/2026 até hoje.” A contraparte de saída é cliente, não fornecedor.

```sql
SELECT a.data, a.boleto, a.codigo AS cliente_codigo,
   a.nome AS cliente, a.placa, a.codpro, a.subcod,
   a.produto, a.unidade, a.peso_liquido, a.valor_total,
   a.filial, a.origem, a.id_recnobol
FROM syg_movimento_pesos('SAIDA', DATE '2026-06-01',
   CURRENT_DATE, 'TODAS', NULL, NULL, NULL, NULL,
   NULL, NULL, NULL, NULL) a
ORDER BY a.data DESC, a.filial, a.boleto DESC,
   a.origem, a.id_recnobol
LIMIT 100
```

## P03 — Total de entradas por filial e unidade de medida

Pergunta: “Qual o peso líquido total comprado desde junho, separado por filial e unidade?” Agregar no banco sobre o período completo. `itens_relatorio` é contagem de linhas.

```sql
SELECT a.filial, a.unidade,
   COUNT(*) AS itens_relatorio,
   SUM(a.peso_liquido) AS peso_liquido,
   SUM(a.valor_total) AS valor_movimentos
FROM syg_movimento_pesos('ENTRADA', DATE '2026-06-01',
   CURRENT_DATE, 'TODAS', NULL, NULL, NULL, NULL,
   NULL, NULL, NULL, NULL) a
GROUP BY a.filial, a.unidade
ORDER BY a.filial, a.unidade
```

## P04 — Evolução diária de saídas

Pergunta: “Quanto vendemos em peso por dia desde junho?” Dias sem linhas não aparecem; não confundir ausência de registro com falha da API.

```sql
SELECT a.data, a.unidade,
   SUM(a.peso_liquido) AS peso_liquido,
   SUM(a.valor_total) AS valor_movimentos,
   COUNT(*) AS itens_relatorio
FROM syg_movimento_pesos('SAIDA', DATE '2026-06-01',
   CURRENT_DATE, 'TODAS', NULL, NULL, NULL, NULL,
   NULL, NULL, NULL, NULL) a
GROUP BY a.data, a.unidade
ORDER BY a.data, a.unidade
```

## P05 — Entradas por produto e subproduto

Pergunta: “Quais produtos mais recebemos desde junho?” Ranking por unidade; comparar kg com unidades de contagem não produz um ranking único válido. Sem corte de top N neste SQL.

```sql
SELECT a.codpro, a.subcod, a.produto, a.unidade,
   SUM(a.peso_liquido) AS peso_liquido,
   SUM(a.valor_total) AS valor_movimentos,
   COUNT(*) AS itens_relatorio
FROM syg_movimento_pesos('ENTRADA', DATE '2026-06-01',
   CURRENT_DATE, 'TODAS', NULL, NULL, NULL, NULL,
   NULL, NULL, NULL, NULL) a
GROUP BY a.codpro, a.subcod, a.produto, a.unidade
ORDER BY a.unidade, peso_liquido DESC, a.codpro, a.subcod,
   a.produto
```

## P06 — Fornecedores com maior volume em uma unidade

Pergunta: “Quais os dez fornecedores com maior peso comprado em KG desde junho?” `KG` é ilustrativo: consultar/confirmar a unidade exata retornada, sem conversão. Preservar sinais e regras da função.

```sql
SELECT a.codigo AS fornecedor_codigo, a.nome AS fornecedor,
   a.unidade, SUM(a.peso_liquido) AS peso_liquido,
   SUM(a.valor_total) AS valor_movimentos
FROM syg_movimento_pesos('ENTRADA', DATE '2026-06-01',
   CURRENT_DATE, 'TODAS', NULL, NULL, NULL, NULL,
   NULL, NULL, NULL, NULL) a
WHERE TRIM(a.unidade) = 'KG'
GROUP BY a.codigo, a.nome, a.unidade
ORDER BY peso_liquido DESC, a.codigo, a.nome, a.unidade
LIMIT 10
```

## P07 — Pesagens de um fornecedor

Pergunta: “Mostre as entradas do fornecedor 123 desde junho.” `123` é dado fictício; localizar o cadastro correto antes de montar a chamada. Para cliente, usar `SAIDA` e o código do cliente na mesma posição 5.

```sql
SELECT a.data, a.boleto, a.codigo, a.nome,
   a.codpro, a.subcod, a.produto, a.unidade,
   a.peso_liquido, a.valor_total, a.filial, a.origem,
   a.id_recnobol
FROM syg_movimento_pesos('ENTRADA', DATE '2026-06-01',
   CURRENT_DATE, 'TODAS', 123, NULL, NULL, NULL,
   NULL, NULL, NULL, NULL) a
ORDER BY a.data DESC, a.filial, a.boleto DESC,
   a.origem, a.id_recnobol
LIMIT 100
```

## P08 — Detalhar um boleto de venda

Pergunta: “Mostre os itens do boleto de venda 456 no período desde junho.” `456` é ilustrativo; posição 10 filtra boleto. O período continua aplicado, inclusive a devoluções. Não somar peso do boleto e classificação com `lpesotudo = TRUE`.

```sql
SELECT a.data, a.boleto, a.codigo, a.nome,
   a.codpro, a.subcod, a.produto, a.unidade,
   a.peso_liquido, a.preco, a.valor_total,
   a.filial, a.origem, a.id_recnobol
FROM syg_movimento_pesos('SAIDA', DATE '2026-06-01',
   CURRENT_DATE, 'TODAS', NULL, NULL, NULL, NULL,
   NULL, 456, NULL, NULL) a
ORDER BY a.data, a.filial, a.origem, a.id_recnobol
LIMIT 100
```

Variações sem novas fórmulas: código/subcódigo de produto nas posições 6/7; placa em `WHERE TRIM(a.placa) = '<placa_validada>'`; comprador/vendedor agrupado por `cod_com_ven` e `comp_vend`, preservando o parâmetro 9. Alterar apenas os filtros pedidos. `SERVICO` no corpo desta função inclui tabelas de serviço legado; para Serviço 3.0 usar a referência [servico30.md](servico30.md).

## P09 — Compras de 2026 por mês e produto em FILIAL2

Use a ferramenta específica `sagi_pesagens_compra_mensal` quando liberada. Os filtros são fixos neste piloto. Percorra todas as páginas; meses sem movimento não aparecem. Agrupe por código/subcódigo, descrição e unidade para preservar o detalhamento. Peso líquido inclui devoluções negativas conforme a função. Contagens de itens e boletos não representam pesagens únicas anuais e boletos se repetem entre grupos de produtos. Não rotule o valor dos movimentos como financeiro pago nem presuma moeda.

```sql
SELECT DATE_TRUNC('month', a.data)::date AS mes,
   a.filial, a.codpro, a.subcod, a.produto, a.unidade,
   COUNT(*) AS itens_relatorio,
   COUNT(DISTINCT a.boleto) FILTER (WHERE a.boleto > 0) AS boletos_com_movimento,
   COUNT(*) FILTER (WHERE a.origem = 'DEV-ENTRADA') AS itens_devolucao,
   SUM(a.peso_liquido) AS peso_liquido,
   SUM(a.valor_total) AS valor_movimentos
FROM syg_movimento_pesos('ENTRADA', DATE '2026-01-01',
   DATE '2026-12-31', 'FILIAL2', NULL, NULL, NULL, NULL,
   NULL, NULL, NULL, NULL) a
WHERE TRIM(a.filial) = 'FILIAL2'
   AND a.data >= DATE '2026-01-01' AND a.data < DATE '2027-01-01'
GROUP BY DATE_TRUNC('month', a.data)::date,
   a.filial, a.codpro, a.subcod, a.produto, a.unidade
ORDER BY mes, a.codpro, a.subcod, a.produto, a.unidade
```
