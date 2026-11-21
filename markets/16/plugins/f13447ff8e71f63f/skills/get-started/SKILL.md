---
name: get-started
description: Use Pa-ga-me to split group expenses - create a group, add expenses (also from a receipt photo), see balances and record repayments.
---

# Pa-ga-me: split group expenses

Pa-ga-me groups need no account. Each group is identified by its link (`https://pa-ga.me/g/<uuid>`): whoever has it can see and change the group, so never share it with third parties or reveal it to people other than the user.

Reply in the user's language. Tool error messages are in Spanish and explain the cause: fix the input and retry, and explain the problem to the user in their language.

## Workflow

1. **Get the group.** Ask the user for their group link, or create a new group with `crear_grupo` and give them the link so they can share it with the others.
2. **Read it first.** Call `ver_grupo` before adding anything: it returns the participants, currency, expenses, balances (positive = is owed money) and the pending payments to settle up.
3. **Add expenses** with `anadir_gasto`. Amounts are in units (12.5 = 12.50), people by name. If you don't know who paid, ask: never assume. By default the expense is split equally among everyone; use `split_among`, `split_amounts` or `split_parts` for other splits, `currency` for foreign currency and `repeat_frequency` + `repeat_until` for recurring expenses.
4. **From a receipt photo**: read the items and total, propose the expenses (description, amount, who paid, split) and add them only after the user confirms.
5. **Settle up**: use the pending payments from `ver_grupo` and record each repayment with `registrar_pago` once the user says it has been paid.

## Changes

- `editar_gasto` changes only the fields given; if only the amount changes, the split keeps its proportions.
- `borrar_gasto` cannot be undone: confirm with the user first.
- `anadir_participantes`, `renombrar_participante` and `editar_grupo` manage people, the group name and its currency (changing the currency does not convert existing amounts).
