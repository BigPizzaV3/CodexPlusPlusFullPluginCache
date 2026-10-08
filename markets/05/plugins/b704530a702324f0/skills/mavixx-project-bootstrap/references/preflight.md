# Preflight workflow

## New mode

Establish product purpose, users, primary outcome, scope, critical journeys, platform, data, authentication, payments, integrations, content, brand, non-functional constraints, environments, hosting, and definition of done. Infer ordinary implementation details when reversible. Ask about decisions with business or architectural impact. When the user asked for a build, move from this preflight into implementation rather than returning the requirements as the final product.

## Existing mode

Inspect before questioning. Reuse decisions already encoded in the repository. Record working commands, dirty files, current architecture, critical journeys, existing brand, data stores, integrations, deployment, and known failures. Do not overwrite existing project instructions or generate a parallel starter. Route implementation to `$mavixx-project-upgrade`.

## Requirement output

Use four buckets:

- Confirmed
- Proposed default
- Needed before implementation
- Can be supplied later

For each needed external item—brand guide, reference screenshot, copy, API credentials, licensed asset, domain, analytics identifier—explain why it is needed and whether Codex can create a provisional version.

## Project files

- `PROJECT_BRIEF.md`: source of truth for outcomes, users, scope, journeys, constraints, decisions, and acceptance criteria.
- `AGENTS.md`: concise operational guidance: commands, repository map, conventions, verification, preservation rules, and links to deeper project docs.
- `DESIGN.md`: only for user-facing products; created through `$mavixx-design-system`.
- Plan: phases, dependencies, verification, and rollback-sensitive work.

Do not duplicate large specifications in `AGENTS.md`; link to the source of truth.
