# Freeman-based Negotiation Adviser

A stateful negotiation-adviser design based primarily on Seth Freeman's researched negotiation methods, with explicit separation between Freeman material, external evidence, synthesis and AI design decisions.

## Canonical order

1. `00_FREEMAN_RESEARCH_BASE.md` — research authority.
2. `01_NEGOTIATION_AGENT_ARCHITECTURE.md` — approved architecture.
3. `02_NEGOTIATION_BEHAVIOUR_CONTRACT.md` — approved user-facing behaviour.
4. `03_DECISION_LOG.md` — architecture/interface decisions.
5. `schemas/` — canonical state and specialist interfaces.
6. `agent/` — orchestrator, routing, state updates and system prompt.
7. `skills/` — eight bounded specialist skills.
8. `tests/` — acceptance scenarios and local structural verifiers.

## Specialist set

| ID | Skill | Purpose |
|---|---|---|
| F01 | `freeman-preparation` | Focused/full I FORESAW IT preparation |
| F02 | `ttt-offer-design` | Topics, Targets, Trade-offs and offer packages |
| F03 | `batna-leverage` | Bilateral BATNA/WATNA and leverage |
| F04 | `stakeholder-process` | Authority, influence, escalation and process |
| F05 | `difficult-conversation` | Tense/defensive interaction and de-escalation |
| F06 | `roleplay-redteam` | Isolated rehearsal and strategy stress-test |
| F07 | `communication-drafting` | Strategy-faithful final wording |
| F08 | `deal-review` | Independent acceptance gate |

## Deploying in a ChatGPT/agent workspace

Use `agent/AGENT_SYSTEM_PROMPT.md` as the primary agent instruction. Make the canonical research, architecture, behaviour, schemas and skill files available to the agent as project/workspace resources.

Where the runtime supports discoverable `SKILL.md` modules, register the eight skill directories directly. Where it does not, keep the skill files as project resources and require the orchestrator to load only the relevant one for the current decision.

For material STANDARD/FULL negotiations, provide a persistent state mechanism implementing `schemas/NEGOTIATION_STATE.md`. If the platform cannot persist a state artefact, retain a concise canonical state snapshot and disclose the continuity limitation when it matters.

## Verification status

Local structural/contract verifiers cover:
- F01;
- F02;
- F03;
- F04–F08;
- orchestrator/routing/state files.

The acceptance scenarios were written before their corresponding skill/orchestrator artefacts. This runtime does not expose an isolated model/subagent test harness, so behavioural RED/GREEN execution remains a deployment gate. Run every acceptance suite against:

1. a baseline model without the skill/control file;
2. the same model with the skill/control file;
3. adversarial variants of any observed failure/rationalisation.

Do not call the system deployment-ready solely because the structural verifiers pass.

## Independent behavioural validation

The remaining release gate is packaged for an isolated Codex/agent runtime:

- `CODEX_BEHAVIOURAL_VALIDATION_PROMPT.md` — exact independent validation instruction;
- `tests/BEHAVIOURAL_TEST_HARNESS.md` — RED/GREEN method and scoring;
- `tests/ADVERSARIAL_CROSS_SKILL_ACCEPTANCE.md` — orchestrator conflict/pressure cases;
- `tests/BEHAVIOURAL_RESULTS_TEMPLATE.md` — required evidence record.

Do not mark the adviser deployment-ready until this behavioural gate passes.

## ChatGPT/Codex plugin

This repository is the source package for the skills-only `negotiation-adviser` plugin published by Maciej Rojewski. The package preserves the eight specialist skills and adds a thin `negotiation-adviser` entry skill for end-to-end routing.

Validate the package with:

```powershell
python 'C:\Users\Leon\.codex\skills\.system\plugin-creator\scripts\validate_plugin.py' .
python tests/verify_all.py
```

The plugin does not operate an external server or persist negotiation state between separate conversations. See [`PRIVACY.md`](PRIVACY.md), [`TERMS.md`](TERMS.md), and [`docs/plugin/PUBLIC_SUBMISSION.md`](docs/plugin/PUBLIC_SUBMISSION.md) before public submission.
