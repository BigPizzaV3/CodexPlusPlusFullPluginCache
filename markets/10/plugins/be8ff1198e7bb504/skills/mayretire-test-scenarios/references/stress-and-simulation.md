# Stress, Monte Carlo, and backtesting

Use `start_stress_test_job`, `start_monte_carlo_job`, or
`start_backtest_job` with a complete `basePlan`. Poll `status_plan_job` while queued or running and get
the compact result through `result_plan_job`. Do not call a queued job a
server failure. Report partial work and stop reason if a limit or cancellation
ends a job early. Use a bounded result view rather than dumping full annual
data.

**Stress:** MayRetire's built-in suite has six named deterministic adverse
return sequences. Use returned scenario names and results. Report
`scenariosPassed`/`scenariosTotal` separately from
`averageSpendingFundedFraction` (the average portion of the spending horizon
funded). Neither is a probability of future success. For a failed scenario,
report its spending-funded fraction and age reached. If an active estate goal
is the binding criterion and `averageEstateFundedFraction` is returned,
present that estate measure separately. Do not invent custom shocks when the
user asks for the built-in stress test.

**Monte Carlo:** MayRetire commonly uses 500 trials. Compare plans with the
same seed, completed trial count, engine build, and success criteria. State
that success is an estimate with sampling error; approximate standard error
for fraction `p` from `n` independent trials is `sqrt(p(1-p)/n)`. Near a
target threshold, test an independent seed when supported rather than treating
one lucky sample as exact. Do not infer income percentiles the response does
not provide or derive an exact estate-threshold probability from p10/p50/p90.

**Backtest:** Historical starting-year rotations are not independent Monte
Carlo probabilities. Preserve the plan's return method. A manual-return
account uses historical variation around its configured return, scaled by
`marketSensitivity`; it does not replace that return with raw historical
returns. Report the tested years and the relevant simulation protocol.

Screen broad ideas deterministically when the user has not requested a
probability. A simulation-backed search can multiply trials by candidate
count, so keep it bounded and use shortlisted plans when possible. If the
user explicitly asks for a probability threshold, run a probability-based
test rather than substituting deterministic feasibility.
