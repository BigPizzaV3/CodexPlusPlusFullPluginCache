# Serviço 3.0

> Versão 0.4.0: os exemplos podem ser adaptados e executados com SQL livre de leitura. Todas as filiais da empresa do login estão autorizadas; TODAS tem esse escopo. O catálogo não exige cadastro de cada SQL. Confirme o esquema real e os critérios do relatório.

| Tabela | Papel / relacionamento documentado |
|---|---|
| `sagi_contrato_serv3` | Contrato por `contrato_id` |
| `sagi_item_contrato_serv3` | Item por `item_id`, relacionado a `contrato_id` |
| `sagi_prestacao_serv3` | Prestação por `prestacao_id` |
| `sagi_item_prestacao_serv3` | Itens da prestação; confirmar chaves no esquema |
| `sagi_medicao_serv3` | Cabeçalho da medição por `medicao_id` |
| `sagi_medicao_item_serv3` | Itens por `medicao_item_id`, relacionados a `medicao_id`; referências a prestação/contrato |
| `sagi_sla_serv3` | SLA por contrato; confirmar uso no contexto do cliente |

Não deduzir tabela de ordens como `sagi_ordem_serv3`: esse nome não foi confirmado nas fontes consultadas. Não recorrer às tabelas legadas para contornar ausência do Serviço 3.0.

Em medições, `medicao_codcli` é o cadastro comercial envolvido no documento, não a empresa identificada pelo token SAGI. Não usar `idempresa` como se fosse `codcli`. O código deve vir do pedido ou de uma consulta autorizada de cadastro. Acesso a todos os clientes comerciais da empresa depende da permissão do usuário.

Distinguir emissão da medição (`medicao_data`) do período das prestações e da data de faturamento. Uma medição faturada não implica título recebido. Uma prestação pode aparecer em relações de detalhe; não somar cabeçalho repetido por JOIN.

## Exemplo: medições emitidas em um período

Exemplo de cabeçalho sem fórmula monetária. Substitua o intervalo pelo solicitado após validar datas e confirmar a filial autorizada no MCP. Campos conferidos na consulta Serv3 da API v2 e no dicionário; confirmar existência na base atual.

```sql
SELECT sms.medicao_id AS numero,
   sms.medicao_data AS data_emissao,
   sms.medicao_codcli AS cliente_codigo,
   sms.medicao_status AS status,
   sms.medicao_filial AS filial,
   sms.medicao_aprovada AS aprovada
FROM sagi_medicao_serv3 sms
WHERE sms.medicao_data >= DATE '2025-01-01'
   AND sms.medicao_data < DATE '2025-02-01'
ORDER BY sms.medicao_data DESC, sms.medicao_id DESC
LIMIT 100
```

Para cliente comercial específico, acrescentar `AND sms.medicao_codcli = <codigo_numerico_validado>`. Não enviar o marcador literal. Não permitir que esse filtro substitua as permissões de filial do servidor.

A consulta Serv3 da API v2 utiliza `medicao_qtd_cobrada * medicao_valor_unit - medicao_desconto + medicao_acrescimo + medicao_col_vlr_exc - medicao_abate_bolc` para total da medição. Essa fórmula pertence àquele relatório e deve preservar seu tratamento de NULL e seus filtros. Não tratá-la como receita recebida, valor líquido fiscal ou saldo financeiro. Totais novos ou regra não documentada exigem esclarecimento do Time BDI.

Fontes para manutenção: API v2 `src/modules/log-verde/medicoes-servico/sql/medicoes-servico.sql.ts` (apenas função Serv3); `src/modules/log-verde/ordens/ordem-serv3/sql/auxiliar-ordem-serv3.sql.ts`; [dicionário oficial](https://sagierp.com.br/devel/uteis/sagi_dicionario_dados.pdf), páginas impressas 644–647 para itens/cabeçalhos de medição.

## S02 — Medições por filial e status

Pergunta: “Quantas medições do Serviço 3.0 foram emitidas desde junho, por filial e situação?” Conta cabeçalhos, sem JOIN de itens e sem inferir faturamento/recebimento por contagem. Manter status bruto; o esquema da base deve confirmar o domínio.

```sql
SELECT sms.medicao_filial AS filial,
   sms.medicao_status AS status,
   COUNT(*) AS quantidade_medicoes
FROM sagi_medicao_serv3 sms
WHERE sms.medicao_data >= DATE '2026-06-01'
   AND sms.medicao_data <= CURRENT_DATE
GROUP BY sms.medicao_filial, sms.medicao_status
ORDER BY sms.medicao_filial, sms.medicao_status
```

## S03 — Itens e contrato de uma medição

Pergunta: “Mostre o contrato, a prestação e as quantidades dos itens da medição 123.” Número ilustrativo, a substituir pelo informado. A permissão deve ser conferida também no cabeçalho; consultar um ID não concede acesso à medição.

Projeção dos campos da função `medicoesServicoDetalheServ3Sql` da API v2, em `src/modules/log-verde/medicoes-servico/sql/medicoes-servico.sql.ts:80`. Sem fórmula nova de total e sem fallback legado. Itens que não têm prestação mantêm seus campos nulos; uma cobrança sem prestação não deve ser descartada por INNER JOIN na prestação.

```sql
SELECT smis.medicao_item_id AS item_id,
   smis.medicao_id AS medicao_id,
   sms.medicao_filial AS filial,
   smis.medicao_contrato_id AS contrato_id,
   scs.contrato_descricao,
   smis.medicao_prestacao_id AS prestacao_id,
   sps.prestacao_data AS data_prestacao,
   sps.prestacao_ordem AS coleta,
   smis.medicao_tipo_servico AS tipo_servico,
   smis.medicao_qtd_prestada AS quantidade_prestada,
   smis.medicao_qtd_cobrada AS quantidade_cobrada,
   smis.medicao_valor_unit AS valor_unitario
FROM sagi_medicao_item_serv3 smis
INNER JOIN sagi_medicao_serv3 sms ON sms.medicao_id = smis.medicao_id
INNER JOIN sagi_contrato_serv3 scs ON scs.contrato_id = smis.medicao_contrato_id
LEFT JOIN sagi_prestacao_serv3 sps ON sps.prestacao_id = smis.medicao_prestacao_id
WHERE smis.medicao_id = 123
ORDER BY smis.medicao_contrato_id, sps.prestacao_data,
   smis.medicao_item_id
LIMIT 100
```

Não usar `syg_movimento_pesos('SERVICO', ...)` para substituir estes exemplos: o ramo de serviço no fonte consultado usa o módulo legado, enquanto esta skill exige Serviço 3.0.
