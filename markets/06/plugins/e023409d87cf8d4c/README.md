# HA Interaction Audit

A reusable expert workflow for investigating Home Assistant dashboard behavior and building safe interaction simulations. It generalizes the irrigation and Recipe Vault audits into a target-specific testing system.

## Use it

Ask: **“Use HA Interaction Audit to thoroughly test my [dashboard].”**

Other examples:

- “Audit my irrigation editor, including typing, selections, scroll and rapid navigation. Do not change anything live.”
- “Reproduce the timer problem in this dashboard, fix it, and rerun the applicable regressions.”
- “Build an isolated interaction suite for my media dashboard and include failed requests and reconnects.”
- “Resume the previous audit from its checkpoint and tell me what remains untested.”

The audit adapts to available Home Assistant access and permitted browser tools. It does not install an HA add-on or create a new connection to your home. Existing Home Assistant access is needed for live source inspection. Browserless or another permitted browser execution surface is needed to execute interactive tests. Without it, the workflow can still produce source findings and a test plan, clearly marked as unexecuted.

## Included

- Active dashboard/resource discovery and version verification.
- Explicit in-memory service, WebSocket and API contracts.
- Default-deny HTTP resource handling and native transport guards.
- Browser-driven input helpers, shadow-root targeting and stable hit testing.
- A catalog of 106 scenario families covering form state, navigation, touch, timers, HA state, errors, data workflows, usability, recovery and performance. Families are planning categories, not preexecuted tests.
- Rigorous coverage planning with explicit applicability, independent expected outcomes, evidence, profiles, dependencies and gaps.
- Controlled delayed/reversed responses, failures before execution and lost acknowledgments after a simulated commit.
- Seeded legal action sequences, independent per-action model checks and bounded reproduction reduction.
- Temporal checks that catch disappearing controls and distinguish continuous-use requirements from eventual results.
- Fixture-only deliberate defects to challenge whether important assertions can actually detect a failure.
- Fast regressions, independent deep passes and resumable checkpoints.
- Evidence records that distinguish failed, blocked, inconclusive and unexecuted checks.
- A scoped repair workflow with verified recovery and separate live verification.

Broad audit requests use rigorous depth by default, with bounded passes and explicit gaps. The harness is a starter toolkit. Each dashboard needs an adapter, copied current resources, explicit mock data/contracts, and its own assertions. It intentionally refuses to build an unconfigured adapter. Fake-clock, multi-tab and native-device coverage require their stated capabilities and explicit extensions; they are not automatically supplied by the single-page Browserless starter. The historical 139-test Recipe Vault result is not a guarantee or an automatically applicable test count.

## Validation scope

Core transport, mock state, result accounting, workspace generation, coverage validation, payload compilation, fault scheduling, model checks, failure reduction and temporal oracles are covered by included offline checks. Deliberate synthetic defects check that the relevant oracles fail. Browser geometry helper checks use a synthetic DOM and do not establish browser-engine behavior. A separate workflow exercise checks interpretation of raw audit evidence. These checks do not constitute a new live HA audit, a complete Browserless run, or native iPhone testing.

Official implementation references are in the skill's `references/sources.md`. Instructions honor the current environment's permissions and browser-control rules.


## Support

If this plugin is useful, you can optionally support it via the tip jar: https://ko-fi.com/quietengine
