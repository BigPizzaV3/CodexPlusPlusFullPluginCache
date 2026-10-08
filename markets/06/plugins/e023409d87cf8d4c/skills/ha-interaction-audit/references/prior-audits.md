# Historical templates

Provenance: user-supplied September 9, 2026 conversation and read-only inspection of the named saved runners during plugin creation. Results below are historical reports, not rerun or re-certified by this plugin. Active files and versions can change; rediscover them each time.

## Irrigation

The original isolated editor fixture loaded active inline core/editor code and the then-final V10 layer. It mocked HA calls and ran a 390x844 touch profile. The reported initial suite had 13 assertions, repeatedly passing: typing through updates; focus/caret; three expanded sections; profile selection; Manage Zones; editor scroll; nav geometry; and nav touch swipe behavior.

Reported defects motivating this suite: full DOM replacement on unrelated HA updates; accidental drag; lost expanded sections; and nav movement. Useful generalizations are independent state ownership, in-place updates, focused scroll/caret evidence, and explicit gesture contracts. Neither 390x844 nor blocking all nav swipes is mandatory for other dashboards.

Historic discovery hints: `www/irrigation-app/tests/editor-e2e.html`, `www/irrigation-app/tests/browserless-editor-e2e.js`, and a named `irrigation_browserless_e2e` command. Inspect before reuse.

## Recipe Vault

The reported sequence expanded from 28 assertions to a fast 32-assertion suite and three deeper passes of 50, 40 and 17 assertions. The final supplied V31 report stated 139/139 after registration, with 630 simulated HA updates and 43 preserving redraws. Those numbers must not become new-run results by assumption.

| Reported finding | Transferable test |
| --- | --- |
| Nested Cook step button toggled twice | Count event transitions and requests for one action |
| Expanded ingredients collapsed on redraw | Check details state through HA updates and internal redraw separately |
| Editor/search lost focus/caret | Check value, draft, deepest focus and selection together |
| Timer required a second prompt | Verify actual action contract, visible time change and persistence separately |
| Library Back returned to 0 instead of saved 550 px | Check prompt and settled restoration plus scrollability |
| New recipe tap lost to stale restore/search work | Deliberately act during pending restoration and debounce |
| Taps measured before reflow hit stale coordinates | Re-resolve/hit-test before actual browser action |
| DOMRect serialized incorrectly | Extract numeric geometry fields explicitly |
| Planner had no remaining alternative | Seed sufficient alternatives and test expected exhaustion separately |
| Obsolete tag selectors stayed in bundle | Inspect actual rendered controls |

Historic discovery hints: `www/recipe-vault-tests/v8-e2e.html`, `v8-deep-e2e.html`, `browserless-v8-e2e.js`, and `browserless-v8-deep-pass1.js` through `pass3.js`. The monolithic deep runner may lag the normalized split passes. Prefer inspecting the command target and split runners over assuming the largest file is canonical.

The original guard approach trapped important HA/API surfaces. The generalized harness additionally defaults to copied resources, no authenticated origin, unmatched-request denial and unsupported-transport blocking. Do not retroactively claim those stronger guarantees were tested in the historical suites.
