# Plugin Creator Prompt — Platform Engineering Copilot

Create/validate a **skills-only plugin** from the attached archive.

## Identity
- Package: `cloud-platform-engineering-copilot`
- Skill: `platform-engineering`
- Display name: `Platform Engineering Copilot`
- Version: `0.1.0`
- Category: `Developer Tools`

## Architecture

Keep v0.1 **skills-only**.

Do **not** add:
- MCP;
- cloud-account authentication;
- kubeconfig access;
- Terraform execution;
- deployment actions;
- live production changes;
- custom UI.

The skill may design/review infrastructure and give commands/configuration, but must never claim those commands were run unless actual tool evidence exists.

## Required behavior

Preserve:
- simplest viable platform architecture;
- evidence-first incident debugging;
- Kubernetes first-failing-boundary diagnosis;
- correct startup/readiness/liveness distinctions;
- measured requests/limits/capacity advice;
- PDB nuance;
- Terraform plan/review/apply safety;
- state-locking and state-sensitivity rules;
- GitOps desired-state/reconciliation thinking;
- immutable artifact and safe rollout patterns;
- least privilege and workload identity;
- SLO/error-budget reliability thinking;
- OpenTelemetry-oriented observability;
- platform-as-product, golden paths, and self-service;
- explicit multi-cloud complexity trade-offs;
- production blast-radius/rollback/validation controls.

Never:
- default to Kubernetes or multi-cloud;
- recommend `terraform -lock=false` casually;
- suggest force-unlock without stale-lock evidence;
- claim live cloud/cluster/state inspection without access;
- recommend cluster-wide restarts as root-cause fixes without evidence;
- invent resource IDs, accounts, regions, provider behavior, or test results.

## Preserve
- `SKILL.md`
- all reference files
- `agents/openai.yaml`
- branding
- listing material
- research notes
- five positive and three negative tests

## Validate
1. ZIP root and `plugin.json`.
2. `skills: "./skills/"`.
3. Skill frontmatter.
4. Combined plugin/skill identity <= 64 characters.
5. `agents/openai.yaml`.
6. Asset paths remain inside the package.
7. Public listing field limits.
8. Starter prompts.
9. Five positive and three negative submission tests.
10. No MCP/live infrastructure execution dependency.

Do not create, install, or submit the plugin unless the user explicitly asks for that action.
