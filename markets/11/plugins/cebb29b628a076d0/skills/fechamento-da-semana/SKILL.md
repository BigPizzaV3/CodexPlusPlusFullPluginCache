---
name: fechamento-da-semana
description: Fecha a semana no WiseData Finances a partir dos comprovantes que a pessoa enviar (fotos, PDFs, prints de PIX ou boleto) - encontra a conta a pagar ou a receber que cada comprovante quita, lança o que ainda não existe, registra pagamentos e recebimentos e confere o saldo das contas no fim. Use quando a pessoa pedir para "lançar os comprovantes", "dar baixa nos pagamentos" ou "fechar a semana".
---

# Fechamento da semana com comprovantes

## Passo a passo
1. Chame `get_account` para saber em que conta a conexão está (pessoal ou empresa) e se ela permite escrita.
2. Leia cada comprovante e anote data, valor, quem recebeu ou pagou e o meio (PIX, boleto, cartão, transferência).
3. Para cada comprovante, procure o lançamento em aberto com `find_records`:
   - pagamento: `entity: "expenses"`, `status: "pending"`, `date_from`/`date_to` em volta da data, `search` com o nome do fornecedor ou o título;
   - recebimento: `entity: "incomes"`, `status: "pending"`.
   O fornecedor se acha pelo nome (razão social ou nome fantasia) com `find_records` `entity: "providers"`.
4. Monte uma **tabela de conferência** e mostre à pessoa antes de gravar:
   - comprovantes que quitam um lançamento existente (qual, valor, data, conta);
   - comprovantes sem lançamento (vão virar despesa ou receita nova, já paga ou recebida);
   - divergências de valor (pagamento parcial, juros ou multa de atraso).
5. **Só depois da aprovação**, grave:
   - vários pagamentos de uma vez: `pay_expenses` (devolve prévia e `confirmation_token`; confirme com o token só após o "ok" da pessoa);
   - um pagamento: `pay_expense` (`expense_id`, `paid_amount`, `payment_date`, `account_id`, `payment_method`);
   - recebimentos: `receive_incomes` ou `receive_income`;
   - sem lançamento prévio: `create_expense` com `status: "paid"` e `payment_date`, ou `create_income` com `status: "received"` e `receipt_date`.
   Em toda escrita simples envie uma `idempotency_key` nova (um UUID por operação) e reutilize a mesma só se repetir a mesma chamada após erro de rede.
6. Ao final, confira com `finance_accounts_summary` (saldo por conta) e `finance_payables_receivables_summary` (o que ainda vence nos próximos 7 dias) e resuma: o que foi pago, o que foi recebido, o que ficou em aberto e o saldo de cada conta.

## Regras
- Nunca grave sem mostrar a tabela e receber a confirmação.
- Despesa no cartão de crédito não se paga sozinha: ela entra na fatura. Para registrar o pagamento da fatura use `pay_credit_card_statement`.
- As tools só registram o que já aconteceu: nenhuma movimenta dinheiro nem aciona banco ou meio de pagamento.
- Datas de pagamento não podem estar no futuro.
- Em conta de empresa, despesa e receita pedem `provider_id`; se o fornecedor não existir, proponha criá-lo com `create_provider` e peça confirmação.
