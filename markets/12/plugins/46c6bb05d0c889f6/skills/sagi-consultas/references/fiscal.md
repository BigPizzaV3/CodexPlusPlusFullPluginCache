# Fiscal: consulta de notas fiscais

> Versão 0.4.0: os exemplos podem ser adaptados e executados com SQL livre de leitura. Todas as filiais da empresa do login estão autorizadas; TODAS tem esse escopo. O catálogo não exige cadastro de cada SQL. Confirme o esquema real e os critérios do relatório.

Fonte primária: `source/syg_plsql/syg_lista_nf.prg:37`, função SQL `syg_lista_nf`; retorno a partir de `:56`, defaults em `:92`, filtros em `:220`. Fonte de exemplos agregados: portal `src/rotas/fiscal.ts:32`. A função atual é de cabeçalho de NF, não item de produto e não CT-e.

## Os 18 parâmetros

| Posição | Nome / tipo | Significado / efeito de NULL |
|---|---|---|
| 1 | `cFil varchar` | Nome de uma filial ou `TODAS`; não recebe lista `IN(...)` |
| 2 | `nTipDat numeric` | 1 emissão, 2 entrada/saída, 3 digitação; NULL = 1 |
| 3–4 | `dIni`, `dFim date` | Período inclusivo; ambos obrigatórios |
| 5 | `cOperacao varchar` | `TODAS`, `ENTRADA`, `SAIDA` |
| 6 | `cOrigem varchar` | `TODAS`, `PROPRIA`, `TERCEIRO` |
| 7–8 | `cSerie`, `cModelo varchar` | NULL = sem filtro; modelo é texto, como `'55'` |
| 9 | `nCfop numeric` | CFOP do cabeçalho; NULL/zero = sem filtro |
| 10 | `nNumeroNf numeric` | Número da nota; NULL/zero = sem filtro |
| 11 | `lMostraDocs boolean` | NULL = TRUE; inclui detalhamento documental; FALSE omite esse texto |
| 12–14 | `lCli`, `lFor`, `lCre boolean` | NULL = TRUE, inclui clientes, fornecedores e credores; não filtra um código específico |
| 15 | `lCan boolean` | NULL = TRUE, mantém canceladas; FALSE aplica filtro por protocolo de cancelamento |
| 16 | `nFinalidade numeric` | NULL/zero = sem filtro; valores usam a finalidade oficial da NF |
| 17 | `cFiltra text` | Filtros internos documentados; NULL = vazio. Não recebe expressão WHERE livre |
| 18 | `cChaveNf varchar` | Chave da NF; NULL/vazio = sem filtro |

Para tipo 2, o fonte usa entrada/saída com fallback para emissão; para tipo 3 usa digitação com fallback para entrada/saída e emissão. A coluna `emissao` retornada continua sendo emissão mesmo quando o filtro é tipo 2 ou 3. `entsai` é retornada, mas a função não retorna coluna de digitação.

Colunas confirmadas: `nf_id`, `emissao`, `entsai`, `status`, `operacao`, `origem`, `numero`, `serie`, `modelo`, `tipo_destina`, `cod_destina`, `nome_destina`, `cnp_destina`, `documentos`, `cfop`, `valornf`, `vlr_icms`, `vlr_ipi`, `vlr_pis`, `vlr_cofins`, `finalidade`, `total_prod_vprod`. `prod_ncm` e `filial` não constam no retorno desta versão; não copiar esses campos de relatórios antigos/de itens.

## Escopo e interpretação

Todos os exemplos começam com o recorte do usuário: desde `2026-01-01` até `CURRENT_DATE`, mantendo os doze NULL finais. Isso **inclui canceladas**. Totais/contagens por status explicitam essa inclusão. Não rotular somas de todas as situações como faturamento válido, receita ou imposto devido. Para excluir canceladas, obter o critério pedido e indicar se foi usado parâmetro 15 = FALSE ou filtro de status; eles não são tratados como equivalentes para todos os status possíveis.

`TODAS` só pode ser usado com recorte de autorização garantido dentro da execução. A função não retorna filial; não tentar aplicar `WHERE n.filial ...`. Para conjunto parcial de filiais, a ponte chama a função por filial autorizada, acrescenta uma coluna literal identificando a filial e reúne as projeções explícitas com `UNION ALL`. Não adicionar novamente uma chamada `TODAS` ao mesmo total.

Confirmar que a versão implantada retorna uma linha por `nf_id` antes de somar cabeçalhos; o fonte atual agrega detalhes em LATERAL. `COUNT(DISTINCT nf_id)` não corrige sozinho uma soma duplicada. Não acrescentar JOIN de itens à base de totais de nota.

## N01 — Notas emitidas desde janeiro de 2026

Pergunta: “Liste as notas fiscais emitidas desde 01/01/2026, com status e destinatário.” Mantém operação/origem `TODAS` e os NULL do exemplo original.

```sql
SELECT n.nf_id, n.emissao, n.entsai, n.numero,
   n.serie, n.modelo, n.operacao, n.origem,
   n.status, n.tipo_destina, n.cod_destina,
   n.nome_destina, n.cfop, n.valornf, n.finalidade
FROM syg_lista_nf('TODAS', 1, DATE '2026-01-01',
   CURRENT_DATE, 'TODAS', 'TODAS',
   NULL, NULL, NULL, NULL, NULL, NULL,
   NULL, NULL, NULL, NULL, NULL, NULL) n
ORDER BY n.emissao DESC, n.nf_id DESC
LIMIT 100
```

## N02 — Notas de entrada pela data de entrada/saída

Pergunta: “Liste as notas de entrada movimentadas desde janeiro.” O período usa parâmetro 2 = 2, não emissão. Exibe ambas as datas para conferência.

```sql
SELECT n.nf_id, n.emissao, n.entsai, n.numero,
   n.serie, n.modelo, n.origem, n.status,
   n.nome_destina, n.cfop, n.valornf
FROM syg_lista_nf('TODAS', 2, DATE '2026-01-01',
   CURRENT_DATE, 'ENTRADA', 'TODAS',
   NULL, NULL, NULL, NULL, NULL, NULL,
   NULL, NULL, NULL, NULL, NULL, NULL) n
ORDER BY n.entsai DESC, n.nf_id DESC
LIMIT 100
```

## N03 — Notas de saída por mês de emissão e status

Pergunta: “Mostre o valor das notas de saída por mês e situação.” Não desconta/exclui canceladas; ficam separadas por status. Valores de NF não comprovam recebimento financeiro.

```sql
SELECT TO_CHAR(n.emissao, 'YYYY-MM') AS mes,
   n.status, COUNT(DISTINCT n.nf_id) AS notas,
   SUM(n.valornf) AS valor_notas
FROM syg_lista_nf('TODAS', 1, DATE '2026-01-01',
   CURRENT_DATE, 'SAIDA', 'TODAS',
   NULL, NULL, NULL, NULL, NULL, NULL,
   NULL, NULL, NULL, NULL, NULL, NULL) n
GROUP BY TO_CHAR(n.emissao, 'YYYY-MM'), n.status
ORDER BY mes, n.status
```

## N04 — Quantidade e valor por operação e status

Pergunta: “Quantas notas autorizadas, canceladas e de outras situações temos desde janeiro?” A resposta mantém os status oficiais, sem agrupar toda situação diferente de autorizada como erro.

```sql
SELECT n.operacao, n.status,
   COUNT(DISTINCT n.nf_id) AS notas,
   SUM(n.valornf) AS valor_notas
FROM syg_lista_nf('TODAS', 1, DATE '2026-01-01',
   CURRENT_DATE, 'TODAS', 'TODAS',
   NULL, NULL, NULL, NULL, NULL, NULL,
   NULL, NULL, NULL, NULL, NULL, NULL) n
GROUP BY n.operacao, n.status
ORDER BY n.operacao, n.status
```

## N05 — Valores de tributos destacados por CFOP e status

Pergunta: “Mostre os valores destacados de ICMS, IPI, PIS e COFINS por CFOP e status.” Consulta de campos da NF; não é apuração tributária, crédito fiscal ou orientação fiscal. CFOP é do cabeçalho, não classificação de cada item.

```sql
SELECT n.operacao, n.cfop, n.status,
   COUNT(DISTINCT n.nf_id) AS notas,
   SUM(n.valornf) AS valor_notas,
   SUM(n.vlr_icms) AS icms_destacado,
   SUM(n.vlr_ipi) AS ipi_destacado,
   SUM(n.vlr_pis) AS pis_destacado,
   SUM(n.vlr_cofins) AS cofins_destacado
FROM syg_lista_nf('TODAS', 1, DATE '2026-01-01',
   CURRENT_DATE, 'TODAS', 'TODAS',
   NULL, NULL, NULL, NULL, NULL, NULL,
   NULL, NULL, NULL, NULL, NULL, NULL) n
GROUP BY n.operacao, n.cfop, n.status
ORDER BY n.operacao, n.cfop, n.status
```

## N06 — Localizar uma nota por número, série e modelo

Pergunta: “Encontre a nota 12345, série 1, modelo 55, emitida em 2026.” Valores ilustrativos. Número isolado não identifica uma nota entre emissores/filiais/modelos; preservar `nf_id` e refinar destinatário/origem/filial quando necessário.

```sql
SELECT n.nf_id, n.emissao, n.numero, n.serie,
   n.modelo, n.operacao, n.origem, n.status,
   n.tipo_destina, n.cod_destina, n.nome_destina,
   n.valornf, n.documentos
FROM syg_lista_nf('TODAS', 1, DATE '2026-01-01',
   CURRENT_DATE, 'TODAS', 'TODAS',
   '1', '55', NULL, 12345, NULL, NULL,
   NULL, NULL, NULL, NULL, NULL, NULL) n
ORDER BY n.emissao DESC, n.nf_id DESC
LIMIT 100
```

Variações documentadas: chave de acesso na posição 18 (validar 44 dígitos para NF-e); CFOP na posição 9; origem `PROPRIA`/`TERCEIRO` na posição 6; filial individual na posição 1. Um período sem resultado não prova inexistência da nota em toda a base. Não buscar documentos confidenciais além do pedido/autorização.
