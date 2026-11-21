---
name: stress-test
description: Stress test the user's crypto holdings against recorded crises and explain the downside in dollars. Works from a list of holdings or a public wallet address. Use when the user asks how bad a crash could get for their portfolio, what their worst case is, or whether they are too concentrated.
---

# Stress test a portfolio

## 1. Get the holdings

- If the user gave a public EVM or Solana address, call `review_wallet` with it. It returns holdings, concentration, approvals, token safety and a stress result in one call. Skip step 2 unless the user also wants a specific crisis.
- Otherwise ask for each holding as a ticker and its current USD value, such as BTC $5,000. If the user only knows amounts, ask them to convert at today's price. Never ask for seed phrases, private keys or exchange logins.

## 2. Replay the crises

Call `stress_test_portfolio` with the holdings and `includeRisk: true`. Report for each crisis the drawdown in percent and dollars, then the three biggest losers. Report VaR and CVaR in one plain sentence, for example: "On a bad day like the worst 5% in the sample, expect to lose about $X; on the worst days, about $Y."

## 3. Concentration

If one holding is more than half the portfolio, or the top three are more than 80%, say so and show how much of the crisis loss comes from them.

## 4. Summary

Close with two or three sentences: the worst recorded crisis outcome, the main driver, and what the user would need to change to reduce it. Do not tell the user what to buy or sell.

End with: "These are analysis tools, not financial advice."
