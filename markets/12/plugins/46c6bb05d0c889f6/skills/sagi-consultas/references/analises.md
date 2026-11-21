# Análises livres e descoberta de outros módulos

Os exemplos são adaptáveis e não representam dados de cliente. Confirme o esquema real com sagi_esquema. Os totais financeiros abaixo usam explicitamente saldo de listagem, sem critérios de dashboard. Todos os períodos, filiais, códigos e demais filtros podem ser alterados. Datas finais com `< dia seguinte` também funcionam para timestamp.

## G01 — Clientes por UF e status

Pergunta: “Quantos clientes temos por estado e situação cadastral?” Status bruto, sem supor ATIVO.

```sql
SELECT c.uf, c.status, COUNT(*) AS cadastros
FROM cag_cli c
GROUP BY c.uf, c.status
ORDER BY c.uf, c.status
```

## G02 — Fornecedores por cidade/UF

```sql
SELECT f.uf, f.cidade, COUNT(*) AS fornecedores
FROM cag_for f
WHERE f.fornecedor ILIKE '%RECICLAGEM%'
GROUP BY f.uf, f.cidade
ORDER BY fornecedores DESC, f.uf, f.cidade
```

## G03 — Produtos por unidade e status

Contagem cadastral; não equivale a quantidade física em estoque.

```sql
SELECT p.un AS unidade, p.status, COUNT(*) AS produtos
FROM cag_pro p
GROUP BY p.un, p.status
ORDER BY p.un, p.status
```

## G04 — Códigos/subcódigos repetidos no cadastro

Diagnóstico de registros, sem excluir nem corrigir automaticamente.

```sql
SELECT p.codpro, p.subcod, COUNT(*) AS registros
FROM cag_pro p
GROUP BY p.codpro, p.subcod
HAVING COUNT(*) > 1
ORDER BY registros DESC, p.codpro, p.subcod
```

## G05 — Saldo de listagem por mês de vencimento, filial e moeda

Pergunta: “Quanto temos a pagar e receber por mês de vencimento em 2026?” É saldo atual das parcelas do período, não saldo histórico no fechamento de cada mês. Não exclui estornos/adiantamentos ou inclui variação cambial.

```sql
SELECT DATE_TRUNC('month', a.ite_pagrec_vencimento)::date AS mes,
   b.cab_pagrec_filial AS filial_id, b.cab_pagrec_pr AS tipo,
   b.moe_codigo AS moeda_codigo, COUNT(*) AS parcelas,
   SUM(COALESCE(a.ite_pagrec_valparcela, 0)
      + COALESCE(a.ite_pagrec_valjuros, 0)
      - COALESCE(a.ite_pagrec_valdesc, 0)
      - COALESCE(a.ite_pagrec_valpago, 0)) AS saldo_listagem
FROM fin_ite_pagrec a
JOIN fin_cab_pagrec b ON b.cab_pagrec_id = a.cab_pagrec_id
WHERE a.ite_pagrec_vencimento >= DATE '2026-01-01'
   AND a.ite_pagrec_vencimento < DATE '2027-01-01'
GROUP BY DATE_TRUNC('month', a.ite_pagrec_vencimento)::date,
   b.cab_pagrec_filial, b.cab_pagrec_pr, b.moe_codigo
ORDER BY mes, filial_id, tipo, moeda_codigo
```

## G06 — Parcelas por pessoa, sem JOIN que multiplique valores

`orides_codigo` é identidade financeira; confirmar tipo de origem do favorecido no cabeçalho antes de traduzir o nome. Não converter para codcli/codfor por igualdade presumida.

```sql
SELECT b.cab_pagrec_tabori AS tabela_pessoa,
   b.orides_codigo, b.cab_pagrec_pr AS tipo,
   b.moe_codigo AS moeda_codigo, COUNT(*) AS parcelas
FROM fin_cab_pagrec b
JOIN fin_ite_pagrec a ON a.cab_pagrec_id = b.cab_pagrec_id
WHERE a.ite_pagrec_vencimento >= DATE '2026-01-01'
   AND a.ite_pagrec_vencimento < DATE '2027-01-01'
GROUP BY b.cab_pagrec_tabori, b.orides_codigo,
   b.cab_pagrec_pr, b.moe_codigo
ORDER BY parcelas DESC, tabela_pessoa, b.orides_codigo, tipo, moeda_codigo
```

## G07 — Títulos com parcelas no período usando EXISTS

Conta cabeçalhos uma única vez, sem agrupar linhas de parcela como títulos.

```sql
SELECT b.cab_pagrec_id AS titulo_id, b.cab_pagrec_numtit AS titulo,
   b.cab_pagrec_pr AS tipo, b.cab_pagrec_filial AS filial_id
FROM fin_cab_pagrec b
WHERE EXISTS (SELECT 1 FROM fin_ite_pagrec a
   WHERE a.cab_pagrec_id = b.cab_pagrec_id
      AND a.ite_pagrec_vencimento >= DATE '2026-01-01'
      AND a.ite_pagrec_vencimento < DATE '2027-01-01')
ORDER BY b.cab_pagrec_id
```

## G08 — CTE e ranking de cadastros por UF

```sql
WITH totais AS (
   SELECT c.uf, COUNT(*) AS clientes
   FROM cag_cli c
   GROUP BY c.uf
)
SELECT t.uf, t.clientes,
   DENSE_RANK() OVER (ORDER BY t.clientes DESC) AS posicao
FROM totais t
ORDER BY t.clientes DESC, t.uf
```

## G09 — Serviço 3.0 por mês de emissão e cliente

Contagem de medições, sem inferir execução ou recebimento por status.

```sql
SELECT DATE_TRUNC('month', m.medicao_data)::date AS mes,
   m.medicao_codcli AS cliente_codigo, m.medicao_status AS status,
   COUNT(*) AS medicoes
FROM sagi_medicao_serv3 m
WHERE m.medicao_data >= DATE '2026-01-01'
   AND m.medicao_data < DATE '2027-01-01'
GROUP BY DATE_TRUNC('month', m.medicao_data)::date,
   m.medicao_codcli, m.medicao_status
ORDER BY mes, cliente_codigo, status
```

## G10 — Medições por aprovação e filial

```sql
SELECT m.medicao_filial AS filial, m.medicao_aprovada AS aprovada,
   COUNT(*) AS medicoes
FROM sagi_medicao_serv3 m
WHERE m.medicao_data >= DATE '2026-01-01'
   AND m.medicao_data < DATE '2027-01-01'
GROUP BY m.medicao_filial, m.medicao_aprovada
ORDER BY filial, aprovada
```

## G11 — Nota fiscal diretamente pelo cabeçalho

Na base conferida, nf_filial armazena o nome textual da filial (varchar), enquanto o Financeiro 3.0 usa ID. Não relacionar nf_filial ao ID numérico. Este exemplo não traduz o status nem reproduz todos os filtros da função fiscal.

```sql
SELECT n.nf_id, n.nf_numero, n.nf_serie, n.nf_modelo,
   n.nf_data_emi AS emissao, n.nf_filial AS filial, n.nf_nome_dest,
   n.nf_vnf AS valor_nota
FROM sagi_nf n
WHERE n.nf_data_emi >= DATE '2026-01-01'
   AND n.nf_data_emi < DATE '2027-01-01'
   AND TRIM(n.nf_filial) = 'FILIAL2'
ORDER BY n.nf_data_emi, n.nf_id
```

## G12 — Vendas de várias filiais por produto/unidade

Preserva devoluções, nomes e unidades; não soma KG com UN ou outras unidades.

```sql
SELECT a.filial, a.codpro, a.subcod, a.produto, a.unidade,
   SUM(a.peso_liquido) AS peso_liquido,
   SUM(a.valor_total) AS valor_movimentos
FROM syg_movimento_pesos('SAIDA', DATE '2026-01-01',
   CURRENT_DATE, 'IN(''MATRIZ'',''FILIAL2'')',
   NULL, NULL, NULL, FALSE, FALSE, NULL, NULL, FALSE) a
GROUP BY a.filial, a.codpro, a.subcod, a.produto, a.unidade
ORDER BY a.filial, a.codpro, a.subcod, a.produto, a.unidade
```

## G13 — Devoluções de entrada por mês/produto

```sql
SELECT DATE_TRUNC('month', a.data)::date AS mes,
   a.codpro, a.subcod, a.produto, a.unidade,
   COUNT(*) AS itens_devolucao, SUM(a.peso_liquido) AS peso_devolucao
FROM syg_movimento_pesos('ENTRADA', DATE '2026-01-01',
   CURRENT_DATE, 'TODAS', NULL, NULL, NULL,
   FALSE, FALSE, NULL, NULL, FALSE) a
WHERE a.origem = 'DEV-ENTRADA'
GROUP BY DATE_TRUNC('month', a.data)::date,
   a.codpro, a.subcod, a.produto, a.unidade
ORDER BY mes, a.codpro, a.subcod, a.produto, a.unidade
```

## G14 — Peso mensal e diferença em relação ao mês anterior com dados

LAG compara o grupo anterior existente; meses sem movimento não são criados como zero. Não misturar unidades ou produtos.

```sql
WITH mensal AS (
   SELECT DATE_TRUNC('month', a.data)::date AS mes,
      a.codpro, a.subcod, a.unidade, SUM(a.peso_liquido) AS peso
   FROM syg_movimento_pesos('ENTRADA', DATE '2026-01-01',
      CURRENT_DATE, 'FILIAL2', NULL, NULL, NULL,
      FALSE, FALSE, NULL, NULL, FALSE) a
   GROUP BY DATE_TRUNC('month', a.data)::date,
      a.codpro, a.subcod, a.unidade
)
SELECT m.mes, m.codpro, m.subcod, m.unidade, m.peso,
   LAG(m.peso) OVER (PARTITION BY m.codpro, m.subcod, m.unidade ORDER BY m.mes) AS peso_grupo_anterior
FROM mensal m
ORDER BY m.codpro, m.subcod, m.unidade, m.mes
```

## Consultar qualquer outro módulo

Não há lista de módulos permitidos que restrinja dados de negócio. Use esta sequência para estoque, beneficiamento, rastreio, logística, contratos, ordens, comissões, custos, documentos e outros módulos instalados:

1. sagi_tabelas com um trecho de nome. Exemplo: busca "esto", "ord", "contrato", "ben" ou "rastre". Busca é literal, não fragmento SQL. Percorra páginas.
2. sagi_esquema com os nomes descobertos, até 20 por chamada. Examine descrições, tipos, PK/FK e cardinalidade confirmada. Ausência de FK declarada não prova relação por igualdade de nomes.
3. Consulte o dicionário oficial e as regras do relatório. Para estoque/custo/rastreio, uma coluna cadastral isolada não comprova saldo nem movimentação.
4. Monte SELECT explícito com filtros reais, ORDER BY e paginação. Função customizada não verificada pode ser substituída pela fonte tabular de leitura, preservando a regra documentada.
5. Se o pedido exigir cálculo desconhecido, esclareça o critério necessário; não peça cadastro/liberação do SQL e não invente fórmula.

[API Explorer](https://api.sagierp.com.br/api-explorer/) e [dicionário oficial](https://sagierp.com.br/devel/uteis/sagi_dicionario_dados.pdf) são referências auxiliares. As ferramentas MCP confirmam a versão efetivamente instalada. Registros reais e credenciais nunca devem ser adicionados aos exemplos.
