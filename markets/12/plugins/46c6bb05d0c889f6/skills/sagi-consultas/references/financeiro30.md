# Financeiro 3.0

> Versão 0.4.0: os exemplos podem ser adaptados e executados com SQL livre de leitura. Todas as filiais da empresa do login estão autorizadas; TODAS tem esse escopo. O catálogo não exige cadastro de cada SQL. Confirme o esquema real e os critérios do relatório.

## Mapa de dados

| Tabela | Papel / relacionamento |
|---|---|
| `fin_cab_pagrec` | Título: `cab_pagrec_id`, `cab_pagrec_pr`, `cab_pagrec_data`, `cab_pagrec_filial`, `moe_codigo`, `orides_codigo` |
| `fin_ite_pagrec` | Parcela: `ite_pagrec_id`; `cab_pagrec_id` liga ao título; valores, vencimento e pagamento |
| `fin_origemdestino` | Cadastro financeiro por `orides_codigo`; `orides_nome` usado no portal |
| `fin_estorno` | Relação com parcela por `estorno_ite_pagrec_id`; não somar via JOIN que duplica parcelas |
| `fin_docto` | Tipo de documento por `docto_id`; `docto_desc` |
| `sagi_nome_filial` | `id_nome_filial` relaciona com `cab_pagrec_filial`; descrição `filial` |
| `sagi_moedas` | `moe_codigo`; nome `moe_nome_moeda` |
| `fin_rel_pagrec_mod` | Vínculos documentais; confirmar cardinalidade antes de JOIN |
| `fin_iterea` | Realizações de parcelas; uma parcela pode ter várias realizações |
| `fin_bcocxa`, `view_extrato_bco` | Bancos/caixas e extrato: usar somente definição conferida e autorizada |
| `view_favorecidos` | Dados de favorecidos; não retornar dados bancários/PIX sem necessidade e autorização |

No dicionário, cabeçalho financeiro está na página impressa 226. O esquema MCP precisa confirmar as colunas do cliente. `orides_codigo` não equivale automaticamente a `codcli`/`codfor`; não unir por códigos apenas aparentemente iguais.

## Critérios distintos, sem substituição automática

**Listagem do exemplo fornecido:** saldo = valor da parcela + juros - descontos - valor pago. O exemplo filtra `cab_pagrec_data >= 2025-01-01`, isto é, lançamento, não vencimento. Não acrescenta variação cambial nem exclui estorno/adiantamento nesse recorte. Sua situação temporal usa vencimento em relação à data atual, mesmo para títulos pagos. Sua situação de pagamento usa a comparação exata dos valores, sem tolerância criada pelo assistente.

**Dashboard do portal:** `src/rotas/finan30.ts` acrescenta `ite_var_cambial` ao saldo, usa período de vencimento, exclui estornos, títulos `ASADT%` e saldo zero. Esse é um recorte diferente. Não aplicar seus filtros ao exemplo original nem apresentar ambos como se fossem o mesmo total. Se o perfil não estiver informado pelo MCP, esclarecer qual relatório o usuário quer reproduzir.

Saldo bancário depende de saldo inicial, compensação, conta, moeda e exclusões específicas. Não obter saldo bancário somando títulos. Não calcular saldo histórico em uma data passada com campos atuais de valor pago; exige reconstrução das realizações e estornos segundo regra validada pelo Time BDI.

## Exemplo reduzido de listagem

Projeção reduzida do exemplo enviado, com a mesma fórmula e corte de lançamento, sem seus JOINs de detalhamento. Omitir os detalhes é intencional: este exemplo não reproduz toda a tela, todas as notas ou favorecidos. Confirmar esquema e autorizações antes de executar. Não adiciona exclusões de dashboard.

```sql
SELECT a.ite_pagrec_id AS parcela_id,
   b.cab_pagrec_id AS titulo_id,
   b.cab_pagrec_pr AS tipo,
   b.cab_pagrec_numtit AS titulo,
   a.ite_pagrec_parcela AS parcela,
   b.cab_pagrec_data AS lancamento,
   a.ite_pagrec_vencimento AS vencimento,
   a.ite_pagrec_pagamento AS pagamento,
   b.cab_pagrec_filial AS filial_id,
   b.moe_codigo AS moeda_codigo,
   COALESCE(a.ite_pagrec_valparcela, 0) AS valor_parcela,
   COALESCE(a.ite_pagrec_valjuros, 0) AS juros,
   COALESCE(a.ite_pagrec_valdesc, 0) AS descontos,
   COALESCE(a.ite_pagrec_valpago, 0) AS valor_pago,
   (COALESCE(a.ite_pagrec_valparcela, 0)
      + COALESCE(a.ite_pagrec_valjuros, 0)
      - COALESCE(a.ite_pagrec_valdesc, 0))
      - COALESCE(a.ite_pagrec_valpago, 0) AS saldo_listagem
FROM fin_ite_pagrec a
INNER JOIN fin_cab_pagrec b ON b.cab_pagrec_id = a.cab_pagrec_id
WHERE b.cab_pagrec_data >= DATE '2025-01-01'
ORDER BY a.ite_pagrec_vencimento, a.ite_pagrec_id
LIMIT 100
```

O servidor deve aplicar a filial autorizada. Sem essa garantia, o exemplo não deve ser executado. A listagem limitada não é um total financeiro. Para perguntas em aberto/vencido, usar o saldo e os filtros do perfil confirmado, além da data, sem alterar o status financeiro por inferência.

## Totais do mesmo recorte do exemplo

Agrupa pagar/receber e moeda, sem somar moedas distintas. Não limita as parcelas antes de agregar. Inclui estornos/adiantamentos da base como o recorte do exemplo; não rotular como dashboard ou saldo histórico.

```sql
SELECT b.cab_pagrec_pr AS tipo,
   b.moe_codigo AS moeda_codigo,
   COUNT(*) AS quantidade_parcelas,
   SUM((COALESCE(a.ite_pagrec_valparcela, 0)
      + COALESCE(a.ite_pagrec_valjuros, 0)
      - COALESCE(a.ite_pagrec_valdesc, 0))
      - COALESCE(a.ite_pagrec_valpago, 0)) AS saldo_listagem
FROM fin_ite_pagrec a
INNER JOIN fin_cab_pagrec b ON b.cab_pagrec_id = a.cab_pagrec_id
WHERE b.cab_pagrec_data >= DATE '2025-01-01'
GROUP BY b.cab_pagrec_pr, b.moe_codigo
ORDER BY b.cab_pagrec_pr, b.moe_codigo
```

Fontes: SQL fornecido pelo solicitante; portal `src/rotas/finan30.ts`; API v2 `src/modules/sagi/financeiro3/sql/financeiro3.ts`; [dicionário oficial](https://sagierp.com.br/devel/uteis/sagi_dicionario_dados.pdf). Os caminhos são referências para manutenção pela Sygecom, não dependências de acesso do cliente.

## F03 — Títulos com vencimento de hoje até daqui a 30 dias

Pergunta: “Liste os títulos que vencem de hoje até daqui a 30 dias, com valores registrados.” Consulta de vencimentos, incluindo títulos já pagos e estornados da base; não rotular automaticamente como contas ainda em aberto. O período é inclusivo nos dois extremos.

```sql
SELECT a.ite_pagrec_id AS parcela_id,
   b.cab_pagrec_id AS titulo_id,
   b.cab_pagrec_pr AS tipo, b.cab_pagrec_numtit AS titulo,
   a.ite_pagrec_parcela AS parcela,
   a.ite_pagrec_vencimento AS vencimento,
   b.cab_pagrec_filial AS filial_id,
   b.moe_codigo AS moeda_codigo,
   a.ite_pagrec_valparcela AS valor_parcela,
   a.ite_pagrec_valjuros AS juros,
   a.ite_pagrec_valdesc AS descontos,
   a.ite_pagrec_valpago AS valor_pago
FROM fin_ite_pagrec a
INNER JOIN fin_cab_pagrec b ON b.cab_pagrec_id = a.cab_pagrec_id
WHERE a.ite_pagrec_vencimento >= CURRENT_DATE
   AND a.ite_pagrec_vencimento <= CURRENT_DATE + 30
ORDER BY a.ite_pagrec_vencimento, a.ite_pagrec_id
LIMIT 100
```

## F04 — Saldo em aberto no critério do dashboard do portal

Pergunta: “No critério do dashboard, quanto há em aberto, a pagar e a receber, com vencimento desde junho?” Aplicar somente com perfil `dashboard_portal` confirmado. Reproduz fórmula e filtros do portal `src/rotas/finan30.ts:45` e `:75`, agrupando ainda por moeda para evitar consolidação de moedas distintas.

O saldo inclui variação cambial, exclui estornos, `ASADT%` e saldo zero. O período é de **vencimento**, não lançamento. Não equivale ao F01/F02 nem a saldo histórico. `NOT EXISTS` verifica estorno sem multiplicar parcelas; não adiciona outro critério de estorno.

```sql
SELECT t.tipo, t.moeda_codigo,
   COUNT(*) AS parcelas_em_aberto,
   SUM(t.saldo) AS saldo_dashboard
FROM (
   SELECT a.ite_pagrec_id, b.cab_pagrec_pr AS tipo,
      b.moe_codigo AS moeda_codigo,
      (COALESCE(a.ite_pagrec_valparcela, 0)
         + COALESCE(a.ite_pagrec_valjuros, 0)
         - COALESCE(a.ite_pagrec_valdesc, 0))
         - COALESCE(a.ite_pagrec_valpago, 0)
         + COALESCE(a.ite_var_cambial, 0) AS saldo
   FROM fin_ite_pagrec a
   INNER JOIN fin_cab_pagrec b ON b.cab_pagrec_id = a.cab_pagrec_id
   WHERE a.ite_pagrec_vencimento BETWEEN DATE '2026-06-01'
      AND CURRENT_DATE
      AND b.cab_pagrec_numtit NOT LIKE 'ASADT%'
      AND NOT EXISTS (
         SELECT 1 FROM fin_estorno e
         WHERE e.estorno_ite_pagrec_id = a.ite_pagrec_id
      )
) t
WHERE t.saldo <> 0
GROUP BY t.tipo, t.moeda_codigo
ORDER BY t.tipo, t.moeda_codigo
```

Aplicar as filiais autorizadas antes da agregação. Valores negativos não devem ser eliminados ou convertidos para positivos por decisão do assistente; preservam o critério da fonte.
