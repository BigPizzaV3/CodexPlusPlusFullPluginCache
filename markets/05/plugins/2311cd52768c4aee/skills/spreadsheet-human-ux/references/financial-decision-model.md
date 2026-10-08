# Financial & Decision Model UX Profile

Use this optional profile for investment, budgeting, fiscal, financing, business-case, property, or other decision-facing financial workbooks.

It is a UX profile, not a financial, legal, accounting, tax, or investment methodology.

## Separate layers

Make the reading path distinguish:

**INPUTS → CALCULATIONS → DECISION OUTPUTS → EVIDENCE**

The user-facing layer should not require navigating the formula chain for ordinary decisions, but material logic must remain inspectable.

## Make uncertainty visible

Use ranges, scenarios, sensitivities, or breakevens for estimates that can change the recommendation. Avoid false precision.

Distinguish sourced/known values from assumptions, inferred values, and unresolved inputs.

## Expose decision-changing variables

Prioritize variables that can reverse the decision rather than displaying every available metric. Useful examples include acquisition price, demand/occupancy, sale price, financing cost, tax treatment, operating cost, delay, contingency, or capital requirement depending on the model.

## Preserve liquidity and downside visibility

A nominally profitable case should not appear unconditionally positive if it exhausts contingency, liquidity, borrowing capacity, or another critical buffer.

Show downside and liquidity constraints near the decision, not only in technical detail.

## Keep strategy-specific capital distinct

Where alternatives require different capital profiles, show those separately instead of hiding them inside a generic total. Examples can include fit-out/equipment, replacement reserves, refurbishment, staging, transaction costs, working capital, or contingency.

## Treat legal/tax/organizational regime as an explicit scenario when material

If different lawful structures or regimes materially change cash flows, costs, tax, obligations, or risk, model them as visible scenario dimensions rather than burying the chosen regime in formulas.

Do not imply that the UX skill determines which regime is legally or financially correct. Route that decision to the appropriate domain methodology/evidence.

## Decision surface

Depending on the model, a start/decision view may highlight:

- active/recommended scenario when analytically justified;
- total capital required;
- expected cash flow/return;
- breakeven threshold;
- downside result;
- liquidity/contingency remaining;
- largest unresolved input;
- explicit decision status such as VIABLE / REVIEW / NO-DEAL only when the underlying analysis supports that classification.

Use concise interpretation alongside key values so the user does not infer meaning from unlabeled numbers.
