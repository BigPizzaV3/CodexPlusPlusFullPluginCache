# Cash and runway definitions

Use a user-provided governed definition when available. State how it differs from these defaults.

## Liquidity

`available deposit balance` is the sum of available balances for active deposit accounts in one explicit currency.

`available Treasury balance` is a separately verified and redeemable Treasury balance that is not included in deposit balances.

`total available liquidity = available deposit balance + available Treasury balance`

Exclude credit limits, accounts receivable, future financing, forecast revenue, and cash identified as restricted or unavailable.

If the MCP does not return an account currency code, keep the values separate from any amount with an explicit different currency. Use the shared currency label.

## External cash flow

`external inflow` is a positive settled transaction with a party outside the organization.

`external outflow` is the absolute value of a negative settled transaction with a party outside the organization.

`net cash flow = external inflow - external outflow`

Exclude confirmed internal transfers, reversals, failed transactions, cancelled transactions, and blocked transactions.

## Operating burn

`unadjusted burn = max(external outflow - external inflow, 0)`

Adjusted operating burn starts with external cash flow. Remove financing, owner contributions, investment activity, and one-time non-operating flows only when transaction evidence or a user-provided classification supports the change.

If you calculate adjusted operating burn, also show unadjusted burn. Reconcile every adjustment by source ID and amount.

## Runway

`runway months = total available liquidity / average monthly operating burn`

Use complete calendar months. State the burn definition, period, account scope, and currency label.

If average burn is zero, report `cash-flow positive in the selected period`. If average burn is negative because inflow exceeds outflow, also report cash-flow positive. Do not report infinite runway.

## Concentration

`inflow concentration = counterparty inflow / total external inflow`

`outflow concentration = counterparty outflow / total external outflow`

Keep inflow and outflow concentration separate. State each denominator.

## Confidence

Label runway low confidence when any of these conditions is true:

- fewer than three complete months are available;
- transaction retrieval is incomplete;
- material possible internal transfers remain unresolved;
- available Treasury or restricted-cash status is unclear;
- the currency code needed to combine balances is not available.
