# Scenario design and optimization

Start with `inspect_plan_payload`, `validate_plan_payload`, and a deterministic
`calculate_plan_payload` baseline. Clarify the user's objective, hard limits,
and which areas may change. Test a few material levers separately before
combining them, so the cause of an improvement stays clear. Keep spending,
estate scope, investment risk, housing, work, and other excluded areas fixed.

For up to eight independent variations, use `compare_plan_payloads` with a
label and merge patch for each. Merge patches replace arrays; a change to a
scheduled withdrawal range or additional portfolio must include the complete
intended array. `edit_plan_payload` can instead apply item operations by stable
ID. Inspect and preserve enabled withdrawal overrides unless changes are
authorized. Validate the modified plan and report the material diff.

For broad `start_exploration_job` or `start_optimization_job` jobs, use a
bounded search request with either explicit variables or named scenarios. Describe the actual
candidate set and objective. Screen deterministic candidates before expensive
simulation unless success-rate optimization is specifically requested. Check
the returned `searchScope`, evaluation count, stop reason, and whether the
search was exhaustive within its supplied space. A best candidate is best
only among evaluated candidates, not a global optimum.

When the user requests an annual income range, normally model flexible
spending with the upper desired amount and lower minimum, then vary only the
permitted strategy levers. Do not turn the range into a grid of constant
spending targets unless the user asks for the highest sustainable fixed
amount. For a success-rate threshold, retain its exact success criteria.
For a stress percentage, distinguish the average spending-funded fraction
from the strict count of fully funded scenarios. Present both successful and
failed alternatives and only material tradeoffs. Use selected candidate plans
to produce a complete JSON plan when the user wants to retain a scenario.
