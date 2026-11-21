---
name: contratos-em-andamento
description: Cadastra no WiseData Finances um financiamento, empréstimo, consórcio ou parcelamento que já está em andamento, começando da próxima parcela a pagar e mantendo a numeração do contrato (por exemplo 11/24). Use quando a pessoa disser que tem um financiamento, carnê ou empréstimo do qual já pagou algumas parcelas.
---

# Contratos em andamento (parcela inicial)

## O que perguntar antes
- Valor de cada parcela (ou o total que ainda falta) e se as parcelas têm valores diferentes.
- Total de parcelas do contrato e qual é a **próxima** a vencer (ex.: a 11ª de 24).
- Data de vencimento da próxima parcela.
- Conta que paga, categoria e, em conta de empresa, o credor (fornecedor).

## Conta pessoal ou despesa parcelada
1. Chame `get_account` para confirmar a conta e a permissão de escrita.
2. Ache os ids com `find_records`: `accounts`, `categories` (tipo `expense`) e, se for empresa, `providers`.
3. Monte `create_expense` com:
   - `occurrence: "installments"`;
   - `installments` = parcelas que **faltam** (no exemplo, 24 − 10 = 14);
   - `starting_installment` = número da próxima parcela no contrato (no exemplo, 11), para o app mostrar 11/24 … 24/24;
   - `amount` = soma das parcelas que faltam (14 × valor da parcela); com valores diferentes use `custom_installments`;
   - `due_date` = vencimento da próxima parcela, `issue_date` = hoje ou a data do contrato (não pode ser futura), `status: "pending"`;
   - `idempotency_key` nova.
4. Mostre à pessoa o resumo (quantas parcelas, numeração, valor, primeira e última data) e **só grave depois da confirmação**.
5. Confira com `find_records` (`entity: "expenses"`, `search` pelo título) que as parcelas foram criadas.

## Empréstimo ou financiamento da empresa
Em conta de empresa prefira `create_loan`, que separa juros de amortização: informe `total_amount`, `installments_total`, `interest_rate` e `interest_type`, `start_date` e `payment_frequency`. Parcelas já pagas antes do cadastro podem ser registradas com `register_loan_payment` (uma por parcela, com a data real). Confirme o plano com a pessoa antes de cada gravação.

## Regras
- Nunca invente valores: pergunte o que faltar.
- Não lance as parcelas já pagas como despesas novas, a não ser que a pessoa peça; elas já saíram do saldo no passado.
- `starting_installment` só vale com `installments` ou com recorrência que tenha data final.
