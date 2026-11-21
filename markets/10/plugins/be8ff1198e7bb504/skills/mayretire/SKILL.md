---
name: mayretire
description: Review and explain a supplied Canadian retirement plan through MayRetire's remote MCP service; use the focused creation or scenario-testing skill for those requests.
---

# MayRetire planning

Use the MayRetire MCP tools for calculations. Before asking for a plan, explain
that using remote tools sends its financial details to MayRetire's server for
processing. Do not ask for payment-card details, health information, government
identifiers, or credentials. The remote service does not have
access to the user's browser storage, MayRetire account, or local files. Ask the
user to attach a saved/exported MayRetire JSON plan, or interview them to create
one with `create_plan_payload`. Never claim to have retrieved a plan automatically.
The complete plan is supplied in `basePlan` on each plan-related call.

## Start with the goal and scope

For a supplied plan, call `inspect_plan_payload` and `validate_plan_payload`
before relying on its calculations. For plan creation, ask for household status,
ages, province, work and pension income, CPP/OAS estimates, account balances,
debts, housing, baseline after-tax spending, and any estate goal. Ask for missing
material facts; label illustrative defaults. For investment mix, offer simple
Equity, Growth, Balanced, and Conservative presets and confirm the user's choice.

Clarify whether spending should be fixed, flexible with a stated minimum, or
selected to pursue an after-tax estate target with a minimum acceptable spending
level. Ask which areas may change before optimization: spending, benefit timing,
withdrawal strategies and schedule, investments, housing, corporate or rental
assets, debt, and one-time purchases. Limit comparisons to the areas relevant to
the user's question. Preserve any existing withdrawal overrides unless the user
agrees to change them; prefer strategy settings before adding new overrides.

## Interpret the active configuration

Use `inspect_plan_payload` and the returned assumptions to identify which
settings drive the current calculation before discussing stored plan values.
Do not flag an inactive value merely because it appears in the JSON. Mention it
when the user asks about changing modes, when it conflicts with a stated goal,
or when it materially affects the requested analysis.

Consult the bundled
[MayRetire tutorial](../mayretire-app-assistant/references/MayRetire_Tutorial.md)
when a feature's purpose, screen location, or interaction with other settings
needs explanation. For a particular JSON plan, `inspect_plan_payload`
establishes which settings are active, `describe` defines unfamiliar fields,
and calculations establish actual outcomes. Do not infer that a stored field
applies solely because the tutorial describes it, or override tool evidence
with a general tutorial example. Link the public tutorial for interface help.

With constant-dollar spending, report the fixed after-tax spending target; a
stored minimum is not an active floor. Discuss a possible floor only when
considering flexible or estate-target spending, and confirm the amount with the
user. For the main accounts, `returnMethod = 1` uses asset allocations: stored
manual or legacy real-return values do not drive their current projections.
The legacy real-return field is recognized as a fallback when a manual-return
plan lacks a nominal-return value, not evidence that the user intended to use
that rate. Additional portfolios have independent return modes. Do not claim a
projection is too optimistic solely because of a dormant return value; confirm
the intended return method and compare modeled alternatives first.

## Use the least costly evidence that answers the question

- Call `calculate_plan_payload` for a deterministic baseline and
  `compare_plan_payloads` to screen up to eight independent variations.
- Call `explain_plan_payload` for a specific age, year, or account question.
- Use `describe` to learn an unfamiliar field before editing. Apply a patch or
  item operations with `edit_plan_payload`; show material changes and return the
  resulting plan JSON to the user when they want to keep the scenario.
- Call `start_stress_test_job`, `start_monte_carlo_job`, or
  `start_backtest_job` for the corresponding risk test. Call
  `start_exploration_job` or `start_optimization_job` for a bounded set of
  scenarios when requested. The server may queue
  a job and report its position; poll `status_plan_job` until it runs and
  finishes, then call `result_plan_job`. Retrieve only selected candidate plans using
  `get_candidate_plan`. Use `cancel_plan_job` if the user redirects the search.
  Screen broad ideas deterministically before costly simulations. MayRetire's
  usual Monte Carlo count is 500 trials; keep trial count, seed, engine build,
  and success criteria aligned when comparing scenarios.

## Explain what the numbers mean

Show a small table with only metrics relevant to the user's question. State
whether spending and any active after-tax estate goal were met. A stored estate
amount can be inactive under another spending strategy. Do not compare success
rates for different goals as though they measure the same requirement. Stress
scenario pass count and average spending funded are different metrics; neither
is a probability of success. Monte Carlo success is a model estimate, not a
guarantee. Describe amounts as Canadian dollars in plan-start purchasing power
when the returned result uses that basis. Speak in user-friendly planning terms
rather than JSON field names unless the user asks for implementation details.
For a couple's survivor years, compare annual income to that year's returned
`minTargetIncomeAmount` and `targetIncomeAmount`, not the original two-person
household amounts. See the planning-goals reference for the scaling rule.

The remote pilot processes supplied plans on MayRetire's server and temporarily
holds planning jobs in memory. It does not save plans to a MayRetire account.
`plan_handoff_url` creates a browser link only when the user wants to review a
plan in MayRetire; it does not open a browser or store the plan. Do not present
modeled outcomes as personalized financial, tax, or legal advice.

## Read focused guidance when relevant

- [Planning goals and success](references/planning-goals-and-success.md):
  spending modes, active estate criteria, scope, and interpretation.
- [Accounts, benefits, and income](references/accounts-benefits-and-income.md):
  CPP/OAS, work, registered accounts, corporate assets, and spending phases.
- [Investments, housing, and tax](references/investments-housing-and-tax.md):
  return methods, additional portfolios, dormant housing, debt, and tax evidence.
- [Withdrawals and explanations](references/withdrawals-and-explanations.md):
  strategy schedules, overrides, and decision traces.
- [Opening in MayRetire](references/opening-in-ui.md): use only when the user
  asks to view the plan in the browser.

For a guided plan interview, use the `mayretire-create-plan` skill. For a
what-if search, stress test, Monte Carlo run, or backtest, use the
`mayretire-test-scenarios` skill. Both use the same remote MCP service.
