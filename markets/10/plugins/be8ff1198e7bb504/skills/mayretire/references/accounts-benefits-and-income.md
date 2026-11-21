# Accounts, benefits, and income

Inspect active owners, accounts, benefit starts, income items, and spending
schedules before editing them. Use `describe` for unfamiliar fields or
collections; defaults and templates are examples, not recommendations.

## CPP, OAS, pensions, and work

For each person, distinguish the CPP/QPP amount at its estimate age from the
chosen start age or an amount already being received. Check OAS start and
amount, current receipt state, ownership, and DB pension indexing. When testing
CPP timing, verify any modeled entitlement adjustment in the returned changes.
Compare near-term portfolio draws with later indexed benefits, after-tax income,
tax, OAS clawback, and estate. Confirm survivor assumptions when material.

For ongoing work, confirm employment versus self-employment, gross amount,
owner, start/end, indexing, and expected changes. Do not treat gross income as
net. For employment, ask whether CPP/QPP contributions and EI apply and whether
there is a group RRSP, DCPP, DPSP, or DB arrangement. For self-employment,
clarify any EI special-benefits election. If CPP is being received while work
continues after 65, confirm the relevant contribution election. Encode only
features supported by `describe` and preserve the user's stated gross amount.

## Registered, corporate, and phased cash flow

Distinguish RRSP, RRIF, LIRA, and LIF balances and withdrawals. A registered
withdrawal may reflect statutory limits, strategy settings, or an override;
do not call every registered amount an RRSP withdrawal. Use bounded income,
withdrawal, and balance views to trace transitions.

Corporate analysis applies only when corporate assets are enabled. Inspect
owner, balance, dividends, and other income. For a distribution schedule or
depletion-by-age question, compare after-tax household income, taxes, corporate
and personal balances, OAS clawback, and estate. Do not infer a salary/dividend
election that is absent from the plan.

For retirement phases, model a start, duration or recurrence, amount, owner,
and indexing behavior as explicit income or spending items. Clarify whether an
amount supplements or replaces base spending and what happens in survivor
years. Compare baseline and each phase separately, then review bounded annual
views across the transition. With flexible spending, show low-spending years:
a higher success rate may result from cuts toward the floor.
