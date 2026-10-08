# Validate the tests as well as the application

## Challenge the oracle

An assertion is useful only if it can distinguish an acceptable outcome from the relevant defect. For new high-consequence oracles, run a clean contained reference and a deliberately defective fixture variant. Use a copied resource or explicit fixture switch, never production source. Label the variant and hash it independently. Do not merge mutant results into the live-candidate pass total.

| Deliberate fixture defect | Expected detecting observation |
| --- | --- |
| Attach a second nested-button handler | Transition count and intended write count exceed the contract |
| Hide a running timer after initial display | Temporal visibility fails while timer model still counts down |
| Put an overlay above Stop | Hit test/actionability or browser activation fails with overlay evidence |
| Restore stale route after a new navigation | Latest-intent route invariant fails after the late callback |
| Drop a caret restore | Deep active input and selection invariant fails after redraw |
| Resolve old search last | Result IDs/query no longer match latest user query |
| Swallow save error and display success | UI success contradicts independent store and rejected intent |
| Reject response after a successful mock commit | Ambiguous outcome recovery catches duplicate blind retry |

A “killed” mutant requires the relevant action to execute, valid prerequisites, and the intended measured oracle to fail. A syntax error, source-parity failure, missing selector, fixture timeout or unrelated runtime error does not count. If the clean control fails too, investigate the harness or invalid expectation. If a mutant survives, identify a missing observation, an invalid mutation, or an equivalent behavior before trusting the oracle. Include at least one negative control for an irrelevant change, such as reordering unrelated records; it should not fail a stable-ID assertion.

## Metamorphic and invariant checks

Use relationships with independent meaning when an exact expected screen is unwieldy: select then deselect returns to the original set; edit then Cancel leaves the mock store unchanged; entering the same filter through touch or keyboard yields the same result IDs; adding unrelated entities cannot change a draft; Save then reload reconstructs the committed values; reordering records preserves IDs and per-record data. Do not assume toggle is idempotent or that retries are safe. Define each relationship for the real feature contract.

Compare user-visible state with a separate model, mock store and complete intent ledger. Do not satisfy both expected and actual from the same property or helper return. Verify exact entity/record IDs, units, payload fields, order, cardinality, and acknowledgment versus later state. For irreversible or physical effects, this is a simulation contract, not evidence a real device acted.

## Defend evidence integrity

Record prerequisites at the moment of action: actual scroll range, enabled target, populated alternatives, unique selector, geometry, active layer, completed render where expected, and loaded source hash. Diagnose fixture setup separately. A selector from an old bundle must not be patched with a generic text match that can hit a different action.

Failing a dependency blocks downstream checks whose preconditions no longer hold. Do not continue and report a cascade as independent app bugs. Conversely, do not silently skip difficult branches and retain the original all-green denominator. A runner crash, absent page, no assertions, stale sources, short temporal window or contradictory evidence prevents a passing audit claim.

Preserve every first-run failure and repeat attempt. Use repeats to answer a defined question: independent reproduction, consistency across profiles, or whether a fix removed the same signature. Do not retry until green. Report cases, executions, failure signatures, unique defects and repetitions separately. A source, suite, fixture, contract or timing change starts a new compatible evidence set; retain earlier evidence without merging it into the current score.

Failure proportion is an observed sample rate, not overall system reliability. “0 failures in 20 runs” does not prove 99% reliability, especially for correlated deterministic runs. Avoid unexplained confidence percentages. Scope confidence to reproduced behaviors and state what would change it. Do not claim browser parity from matching viewport dimensions or fixture realism from intercepted writes alone.

## Completion and retained evidence

Before “complete,” reconcile the campaign mapping with all expected-plan files and result ledgers. Required cases must have measured outcomes; isolation, active-source identity and cleanup must be valid; remaining failures need classifications; screenshots/trace interpretations must agree with structured observations. If only runnable scope is complete, say so and list the blocked coverage. A plan validation result never substitutes for execution.

Keep a concise defect record with reproduction, expected/actual, action input mode, minimal sequence, source/fixture/suite hashes, profile, timing/fault schedule, independent evidence, severity rationale and impacted contract. For repairs, first reproduce on the unpatched active code, then run the same oracle on the candidate and relevant neighboring workflows. Recheck fresh live identity and read-only appearance separately when deployment is authorized. Do not let a successful screenshot override failed interaction evidence.

Retain private artifact paths in checkpoints. Redact secrets at capture, not only in the final answer. Trace files and screenshots can contain personal data; prefer synthetic fixtures. During this plugin's own development, offline synthetic helper tests establish helper behavior only. They are not new dashboard assertions or a Browserless session.
