---
name: ha-interaction-audit
description: Rigorously audit and simulate Home Assistant dashboard interactions with active-source fixtures, independent behavioral models, temporal usability checks, controlled request faults, reproducible race sequences, and verified regressions. Optional tip jar: https://ko-fi.com/quietengine
---

# Home Assistant Interaction Audit
> If this plugin saves you time, you can optionally support it via the tip jar: https://ko-fi.com/quietengine


Turn an HA interface into reproducible user journeys, explicit behavioral contracts, and evidence-backed findings. Use the actual active frontend resources in an isolated fixture. Test visible behavior, application state, and intended backend requests together. A screenshot, source review, or passing mock suite establishes only its own evidence layer.

## Scope and decisions

- Default an audit request to investigation and isolated tests. Implement fixes when requested or existing conversation authorization covers them. Preserve restrictions such as “only these items,” “test only,” or “only Browserless.” Do not repeatedly ask for authorization already given.
- Treat “very thorough” as coverage of consequential states, transitions, and failure paths, not an arbitrary test count or thinking delay. The historic Recipe Vault 139 assertions are a reference suite, not a universal target or a current result.
- Build fixtures and supporting files autonomously. A live device action, data mutation, notification, restart, or resource deployment must be within actual task authorization. A UI audit alone does not authorize watering, opening a garage, changing a thermostat, deleting records, or restarting a shared browser add-on.
- Generalize to core Lovelace cards, custom elements, panel dashboards, and add-on/ingress apps. Do not force a custom-card fixture onto code requiring HA's full frontend runtime. Inspect capabilities and state what remains blocked.
- Use available HA access and the environment's permitted browser surface. Discover tools rather than inventing names, endpoints, installed versions, or credentials. If a browser skill constrains the control surface, follow it. The bundled Browserless runner is an artifact, not permission to bypass those constraints.
- Never promise real iPhone validation from a Chromium viewport. Do not add live device instrumentation unless requested.

## Workflow

1. **Establish scope and capabilities.** Read supplied context and existing audit artifacts. Identify dashboard/routes, device, permissions, source access, browser capabilities, and saved regressions. Read [discovery.md](references/discovery.md). If tools are missing, finish source review and the runnable test plan, then name the narrow access needed for execution.
2. **Map the active implementation.** Record configuration, mounted component chain, resource order, inline code, content hashes, dependencies, APIs, entities, and state ownership. Confirm the final override layer is active. Save a source manifest. Never silently test a retired component or cached bundle.
3. **Create a safe fixture.** Read [isolation-and-adapters.md](references/isolation-and-adapters.md). Prefer a fresh unauthenticated context and copied resources at a dedicated virtual origin. All backend operations are explicit mocks. Deny unmatched traffic and unsupported transports. Run containment probes before interactions. A mocked `callService` alone is insufficient isolation.
4. **Define coverage and expectations.** Read [coverage-catalog.md](references/coverage-catalog.md). Each assertion needs an ID, profile, precondition, action, expected observable outcome, dependency, and evidence. Record exclusions. Keep a quick critical-path suite and independent deeper passes. Use a normal-paced baseline, paced updates, then deliberate race tests.
   For broad/deep audit requests, use the rigorous campaign in [rigorous-campaigns.md](references/rigorous-campaigns.md) by default. Map every catalog family to concrete cases, a reasoned exclusion, or a coverage gap. Run `scripts/validate_campaign.py` on the resulting `campaign.json`. Planning readiness is separate from execution success. A requested narrow regression can remain narrow; state that scope explicitly.
5. **Execute real interactions.** Read [interaction-engineering.md](references/interaction-engineering.md). Use browser-driven taps/clicks/typing for actions; use app internals only for documented setup, observation, or labeled fault injection. Verify focus, selection, routes, DOM state, geometry, and exact mock requests. Do not report programmatic `.click()` or value assignment as touch/typing tests.
6. **Triage every failure.** Reduce failures to fresh minimal reproductions. Check fixture contracts, selectors, hit targets, settling, and dependencies before blaming the app. Preserve legitimate rapid-action races instead of hiding them behind sleeps. Read [evidence-and-reporting.md](references/evidence-and-reporting.md). Separate confirmed defect, harness defect, environment failure, expected behavior, and inconclusive evidence.
7. **Fix and verify when authorized.** Read [repair-and-regression.md](references/repair-and-regression.md). Verify recovery files; reproduce the defect before patching; fix the authoritative source with the narrowest durable change; run targeted and impacted regressions in isolation; deploy within scope; verify fresh live resource identity and read-only rendering. Keep simulation and live evidence separate.
8. **Checkpoint and finish.** Save results after each bounded pass: source fingerprint, fixture version, suite hash, profile, seed, completed IDs, findings, last safe state, and next command. Resume from evidence after a cutoff, comparing current sources first. Do not redo compatible passes or imply a background job exists. Finish with counts, findings, evidence, changes, limitations, and a calibrated confidence estimate.

## Quality rules

- Identify actual causes before recommending a CSS patch, forced redraw, blanket timeout increase, disabled gesture, or global event interception.
- Distinguish ordinary HA updates from internal app redraws; exercise both. Preserve state by stable identity, not array index alone.
- Count one nested-button action once; verify UI state and request count to expose bubbling and duplicate listeners.
- For Back restoration, test prompt and settled positions and a new action during restoration. New intent must win over stale callbacks.
- For timers, distinguish local display, persistence, background behavior, and an HA timer/service. Prove each claimed capability separately. Read [temporal-usability.md](references/temporal-usability.md): starting a timer is insufficient if it later disappears, cannot be found, or cannot be stopped. Measure sustained visibility and control reachability during real journeys, plus actual expiry and cancellation paths.
- For overlapping operations, model the expected state independently, control request delivery order, and check invariants after each action. Read [rigorous-campaigns.md](references/rigorous-campaigns.md). Preserve the seed, concrete action trace and fault release schedule. A seed alone does not reproduce browser scheduling.
- Validate high-consequence oracles with deliberate fixture-only defects and a clean control. Read [oracle-validation.md](references/oracle-validation.md). A timing failure, blocked route, or missing prerequisite does not prove the intended assertion can detect the defect.
- Separate transient violations, eventual outcomes and durability. A polling assertion that eventually passes cannot erase lost focus, a double submission, or a disappeared control earlier in the trace.
- A blocked network request means an attempted escape was prevented. It does not mean no attempt occurred. A mocked write does not exercise the real backend.
- Never mark an absent control or skipped branch passed. Report planned, passed, failed, blocked, inconclusive, skipped, and not-run counts. Keep unique assertions separate from executions and defect counts. Do not merge different versions into a misleading total.
- No “all clean” result if required assertions are unexecuted, isolation failed, parity is unknown, or unexplained relevant runtime errors remain.
- Do not equate pass ratio with system reliability. State confidence about specific checked behavior and name untested device/backend conditions.

## Reusable resources

- `scripts/new_audit.py`: create a named audit workspace with templates and harness files; refuse to overwrite an existing workspace.
- `assets/harness/`: transport policy, mock HA context, browser helpers, result ledger, starter fixture, and runner. Includes controlled response faults, seeded model sequences, bounded failure reduction, and sampled temporal oracles. The starter is deliberately not a completed dashboard test.
- `scripts/validate_campaign.py`: reject orphaned/duplicate cases and cyclic prerequisites; expose unassessed, blocked and uncovered scenario families.
- `scripts/build_payload.py`: build a self-contained Browserless function and static payload. No token or live endpoint is included.
- `scripts/summarize_runs.py`: combine compatible pass results without hiding unexecuted checks or double-counting IDs.
- `scripts/selftest.mjs`: check core harness behavior without connecting to HA.
- `scripts/test_tools.py`: validate workspace generation, payload compilation, accounting, and interrupted-run cleanup without a live browser.
- `scripts/advanced-selftest.mjs`: verify response ordering, independent oracles, failure reduction and temporal evidence using offline synthetic cases.
- `scripts/build_plugin.py`: materialize the plugin from this canonical skill and its saved metadata.
- [prior-audits.md](references/prior-audits.md): historical irrigation/Recipe Vault regressions and their limits.
- [sources.md](references/sources.md): official references to recheck against installed versions.

Example requests: “Deep-audit my irrigation dashboard without changing live data”; “Reproduce the editor focus glitch and fix it”; “Rerun the saved Recipe Vault suite”; “Build this interaction simulation for my media dashboard.”