---
name: orcamento-do-mes
description: Planeja o orçamento do mês no WiseData Finances - olha quanto foi gasto por categoria nos meses anteriores, propõe um limite por categoria, cadastra os orçamentos aprovados e acompanha quanto já foi consumido. Use quando a pessoa pedir para "montar o orçamento", "definir limites de gasto", "planejar o mês" ou perguntar se "ainda pode gastar" numa categoria.
---

# Planejar o orçamento do mês

## Passo a passo
1. Chame `get_account` para saber a conta conectada e se a permissão permite escrita.
2. Combine o **mês e o ano** do orçamento (normalmente o mês que vai começar ou o atual).
3. **Histórico de gastos**:
   - `finance_monthly_comparison`: entradas, saídas e saldo dos últimos 6 meses;
   - `finance_budget_analysis`: o planejado contra o realizado por categoria e a tendência de 6 meses, quando já existem orçamentos;
   - por categoria: `finance_category_drill_down` (`category_query` com o nome, `type: "expense"`, `period_preset: "previous_month"` ou `"last_90_days"`); para o mês corrente, `finance_categories_breakdown`.
   Relatórios avançados dependem do plano; sem eles, use `finance_category_drill_down` e `finance_expense_details` (`period_preset`, `category_query`).
4. **Orçamentos que já existem**: `find_records` `entity: "budgets"` (cada um com `category_id`, `month`, `year`, `amount` e `spent_amount`). Um orçamento por categoria e mês.
5. **Proposta**: monte uma tabela com cada categoria de despesa, a média gasta, o limite sugerido e o motivo (média dos últimos meses, gasto atípico a desconsiderar, meta da pessoa). Pergunte o que ela quer ajustar; o limite é decisão dela.
6. **Gravar só depois da aprovação**:
   - categoria sem orçamento no mês: `create_budget` (`category_id` de `find_records` `entity: "categories"` com `type: "expense"`, `amount`, `month`, `year`);
   - orçamento que já existe: `update_budget` (`budget_id`, só os campos que mudam; `is_active: false` pausa).
7. **Acompanhamento**: `finance_budget_status` mostra limite, gasto, saldo e status (`ok`, `warning`, `exceeded`) de cada orçamento do mês. Para "posso gastar X?", passe `simulated_purchase` com o valor e explique o impacto antes da compra.

## Regras
- Orçamento é limite de **despesa** por categoria: categoria de receita não entra.
- O que já foi gasto no mês é contado pelos lançamentos; não lance despesa para "ajustar" o orçamento.
- Em toda escrita, envie uma `idempotency_key` nova e reutilize a mesma só para repetir a mesma chamada após erro de rede.
- Nenhuma gravação sem a tabela aprovada pela pessoa.
