---
name: fechamento-do-mes-empresa
description: Fecha o mês de uma empresa no WiseData Finances - confere impostos e folha do mês, registra o CMV e a depreciação que o app não calcula sozinho e apresenta o DRE, as margens e o caixa do mês. Use quando a pessoa pedir para "fechar o mês", "fechar o DRE", "ver o resultado do mês da empresa" ou "lançar o CMV".
---

# Fechamento do mês da empresa

Só vale em conta de **empresa**. O DRE, as margens e o CMV dependem do recurso de DRE do plano; o caixa e os comparativos, dos relatórios avançados. Se uma tool responder que o recurso não está no plano, siga com as outras e diga só que aquela parte não está disponível na conta.

## Passo a passo
1. Chame `get_account`: confirme que a conexão está numa empresa e se tem permissão de escrita. Na conta pessoal, explique que o fechamento é da empresa e pare.
2. Combine com a pessoa o **mês e o ano** do fechamento (normalmente o mês anterior).
3. **Impostos do mês**: `business_taxes_summary` (`month`, `year`) e `business_taxes_overdue`.
   - Imposto da competência que ainda não está cadastrado: confirme valor, vencimento e tipo com a pessoa e cadastre com `create_tax` (`tax_type_id` de `find_records` `entity: "tax_types"`, `amount`, `due_date`, `period` no formato YYYY-MM).
   - Imposto já pago e ainda pendente no app: `pay_tax` (`tax_id` de `find_records` `entity: "taxes"`, `payment_date`, `payment_method`, `account_id`).
4. **Folha do mês**: `business_payroll_summary` (`month`, `year`).
   - Sem folha gerada e com funcionários ativos: proponha `process_payroll` (`reference_month` YYYY-MM). Ela não marca nada como pago.
   - Linha já paga e ainda pendente: `pay_payroll_item` (`item_id` e `payroll_id` de `find_records` `entity: "payroll_items"` com `parent_id` da folha).
5. **CMV e depreciação**: o app não deriva esses dois valores dos lançamentos. Pergunte à pessoa o custo das mercadorias ou serviços vendidos (`cmv`) e a depreciação do mês. **Nunca estime nem calcule por conta própria.** Grave com `save_dre_entries` (`year`, `month`, `cmv`, `depreciation`):
   - a primeira chamada devolve a prévia com o valor salvo hoje e o novo, e um `confirmation_token`; nada foi gravado;
   - mostre a prévia; o valor enviado **substitui** o do mês;
   - só depois do "sim", chame de novo com os mesmos argumentos e o token.
6. **Resultado**: `business_dre_summary` (`month`, `year`) e, para detalhar, `business_dre_by_account_group`. Indicadores: `business_kpis_dashboard`. Caixa do mês: `business_cash_flow_summary`.
7. Feche com um resumo curto:
   - receita líquida, lucro bruto, resultado operacional e resultado líquido do mês;
   - margem bruta e líquida;
   - impostos pagos e pendentes, folha paga e pendente;
   - entrada e saída de caixa;
   - o que ficou pendente para a pessoa resolver.

## Regras
- Nenhuma gravação sem mostrar o que vai ser feito e receber a confirmação.
- Em toda escrita simples, envie uma `idempotency_key` nova (um UUID por operação) e reutilize a mesma só para repetir a mesma chamada após erro de rede.
- DRE é regime de competência e caixa é regime de caixa: se os números divergirem, explique a diferença em vez de "corrigir" um pelo outro.
- As tools só registram o que já aconteceu: nada movimenta dinheiro nem aciona banco ou meio de pagamento.
