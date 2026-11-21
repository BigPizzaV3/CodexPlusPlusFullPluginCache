# Repayment comparisons

Read when the user wants a deeper cost or paydown comparison. Build from the user's stated balances, terms, and payment budget. Ask for missing inputs progressively; do not turn discovery into a full debt inventory before the user wants to calculate.

## Establish the comparison

- For existing debts, collect each balance, interest rate, and required payment or minimum-payment rule. For avalanche versus snowball, use the same total monthly payment budget for both.
- For a consolidation offer, collect the interest rate, APR, term, payment, and fees as needed. Distinguish financed fees, upfront fees, and fees withheld from proceeds; confirm the net proceeds actually cover the debt being moved.
- APR can include fees and may differ from the contract interest rate. Use the contract rate for amortization and include fees separately. If only APR is known, label an APR-based calculation as a simplified estimate rather than an exact lender schedule; do not add fees twice.
- Compare future cost from today. Include residual debt and its payments if a new product does not cover all existing balances. A longer term can lower payments while increasing total cost.
- If essential terms are unknown, give a qualitative comparison or a visibly hypothetical scenario the user requests. Do not claim savings or assume an offer will be available.

### When the payment budget or minimums are unknown

A user who is unsure what to pay and asks for consistency or a reasonable payoff period is asking for help exploring scenarios. Show two or three illustrative examples with their payment, payoff time, and remaining cost, then ask which could fit after essentials. These examples discover preferences; they do not establish affordability. Do not respond only with a list of dollar amounts to choose from.

Missing card minimums prevent a precise existing-debt plan, but do not block a supported consolidation rate call or all illustrative calculations. Prefer examples whose inputs are known. If illustrating existing-debt repayment with unknown minimums, state any assumed payment allocations prominently, explain that they may not meet actual required minimums, and request the missing minimums before presenting the result as a usable plan. Do not silently treat a past payment as a current minimum, especially after a promotion ends. Do not claim savings against an unmodeled or noncomparable baseline.

If the user says required payments are already unaffordable, return to payment-support planning instead of using hypothetical spare money. Actual terms and a user-confirmed manageable budget replace illustrative assumptions when available.

## Calculation basis

Use deterministic computation in a supported execution environment or renderer, not mental arithmetic for a repayment schedule. Expose the calculation basis alongside results: fixed rates, monthly interest approximation, payment timing, fees, and no new charges. Real revolving-account interest, minimums, and payment allocation can differ. User-supplied contract terms take precedence over illustrative defaults.

For a simple fixed-rate installment loan, monthly rate r is the annual interest rate divided by 12. For principal P and n monthly payments, payment is P*r/(1-(1+r)^(-n)); at zero interest use P/n. For each period, compute interest on the opening balance, then apply the payment. Cap the final payment at the amount owed. Maintain precision internally and round only displayed currency. Derive every local payment, interest total, payoff date, table, and chart for a scenario from the same computed schedule. Total interest is the sum of the computed interest charges; total payments are the sum of the computed payments, including the capped final payment. Do not multiply a rounded displayed payment by the term to derive totals. Reconcile principal repaid to the starting principal and total payments to principal plus interest; include fees consistently and separately. Reuse this basis across follow-up turns and recalculate every affected output when an input changes.

For multiple debts, apply the stated interest and minimum-payment rules, then allocate the remainder of the same total budget to the target debt. Avalanche targets the highest rate; snowball targets the smallest balance. State the tie rule, roll freed payments into the next debt, and carry any unused allocation forward to another debt within the same payment period. Account for changing minimums when their rules are supplied; explicitly label constant-minimum approximations otherwise.

If the budget cannot meet required payments, or a debt grows because payments do not cover interest, flag that result rather than displaying a misleading payoff date. Cap simulation length and report “not paid off within the modeled period” when appropriate. Verify zero-interest handling, final-payment caps, balance reconciliation, and that every scenario uses its stated budget before displaying results.

Balance-transfer comparisons require the promotional duration, transfer fee, post-promotion rate, and payment assumptions. Do not extend a promotional rate past its stated period. HELOC and cash-out scenarios need their actual variable-rate, draw/repayment, or whole-mortgage terms; do not substitute a fixed-loan model without explicitly defining a limited hypothetical scenario.

## Purchase financing with card rewards

Compare a card and a personal loan for the same all-in purchase amount and the user's payoff goal. Use supplied offer terms; a required current personal-loan rate request still uses the rate tool within its coverage. The personal-loan conversation covers $1,000–$50,000, while its current-rate tool covers $5,000–$50,000. For $1,000–$4,999, keep the loan comparison and approved handoff available without that tool. Credit-card analysis has no dollar-range gate. Never change the borrowing amount or payoff goal merely to fit a rate tool; use supplied terms or explicitly hypothetical assumptions for calculations outside its coverage. Without comparable terms, show conditional examples rather than claiming savings.

For the card, establish purchase APR, promotional duration and start date, fees, and the number of payments available before expiration. Do not assume the user has the full advertised period after making a purchase. At 0%, divide the full purchase balance plus financed fees by the available payments. Apply the supplied ongoing purchase rate to any balance remaining after a true introductory promotion; distinguish deferred-interest terms, which may charge interest back to the purchase date. Do not apply balance-transfer fees or transfer-only promotions to direct purchases.

Show interest and fees before rewards, then net cost after qualifying cash rewards. Keep the purchase principal separate from financing cost. Include annual fees and any card surcharge. Before counting a bonus, establish qualifying spend, deadline, purchase and bonus eligibility, and payout timing. Do not encourage extra spending to earn it. Value points or benefits only using a stated redemption value or spending the user would otherwise make; otherwise describe them qualitatively. A conditional bonus is a separate scenario, not guaranteed savings; ordinary cash back requires an applicable supplied rate, and points or benefits need a supported value. Do not double-count rewards. If reward timing or redemption is uncertain, keep the scheduled payments based on the full balance and show the reward as a later benefit. Do not assume a statement credit satisfies the required monthly payment.

For example, with a hypothetical $3,000 purchase, six available monthly payments at 0%, no fees, and a qualifying $250 bonus paid later, the payment remains $500 per month. Interest and fees are $0; conditional net outlay after the bonus is $2,750. Do not calculate the required payment as $2,750 divided by six. Compare that net outlay against the loan's purchase principal, interest, and fees over the same payoff horizon, including any early-payoff terms supplied by the user.

## Present and adjust

Show a small comparison of monthly budget/payment, estimated payoff time, remaining interest and fees, and total remaining outlay. Make the principal/cost distinction clear. Surface the deciding tradeoff in one sentence without declaring a winner or giving advice.

Use a compact chat table for the first straightforward payment-versus-payoff comparison, including illustrative examples used to discover a budget. For multiple-debt repayment or promotional-rate changes where an interactive control would clarify the comparison, and for repeated payment adjustments, use an available in-chat visualization capability. Also use it when requested. Load that capability's instructions only then. A simple initial comparison does not require an interactive graphic. This skill requires no CSS, branded cards, UI templates, or companion skill; follow the visualization capability's own presentation guidance. If unavailable, continue with a table and adjustments in chat without delaying the answer.

A balance-over-time chart can reveal differences in payoff paths. If supported, offer one meaningful control such as extra monthly payment. Use a user-stated manageable range when known; otherwise label the control as hypothetical exploration and ask about affordability before turning its selection into a plan. Changing it must update all affected totals, dates, and chart data. Keep assumptions and the starting scenario visible or easily restorable. If interactive controls are unavailable, ask for one adjustment in chat and recalculate. Do not build a custom interface for a simple comparison.

Use supplied or computed values only. Label hypothetical calculations separately from current rate-tool estimates and lender offers. Preserve native rate UI; this comparison is a separate repayment exploration. Never imply that a dial changes an available lender offer or confirms eligibility.
