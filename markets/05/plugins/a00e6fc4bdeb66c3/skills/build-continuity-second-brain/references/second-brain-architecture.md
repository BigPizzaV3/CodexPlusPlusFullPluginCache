# Adaptive continuity second-brain architecture

Keep the top level shallow and numbered. Adapt modules to the actual company or project, but preserve the continuity core.

## Minimum continuity core

| Folder | Purpose | Minimum contents |
|---|---|---|
| `00_START_HERE` | Emergency navigation and current truth | Emergency guide, identity/scope, readiness status, current-state snapshot, exact next actions, authoritative map |
| `01_MANIFEST_AND_SOURCES` | What exists and where truth lives | File/system/account/artifact manifest, provenance ledger, source-of-truth matrix, coverage matrix |
| `02_DECISIONS_REQUIREMENTS` | Why the present state exists | Decision records, requirements, constraints, assumptions, exclusions, open decisions, supersession map |
| `03_SYSTEMS_ACCOUNTS_ACCESS` | External and internal operating surfaces | System/account register, owners, roles, recovery routes, secret references, domains, vendors, integrations |
| `04_ARCHITECTURE_BUILD_OPERATIONS` | How the product/project/company works | Architecture, workflows, repositories, environments, build/test/release/deploy/rollback or business operations |
| `05_DATA_ASSETS_RECORDS` | Information and valuable artifacts | Data map, schemas, storage, exports, asset and license registers, critical records, retention |
| `06_PEOPLE_ROLES_DEPENDENCIES` | Human continuity | Roles, RACI, key-person risks, contacts, advisers, vendors, onboarding/offboarding, escalation |
| `07_SECURITY_PRIVACY_COMPLIANCE` | Control boundaries | Classification, access policy, incident response, privacy, regulatory/professional review, audit evidence |
| `08_BACKUP_RECOVERY_CONTINUITY` | Loss survival | Backup matrix, recovery priorities, runbooks, alternative providers/owners, drill results, recovery evidence |
| `09_CURRENT_WORK_HANDOFFS` | Exact continuation state | Active work, backlog, blockers, approvals, release state, session handoff, next safe actions |
| `10_SOPS_AND_MAINTENANCE` | Repeatable upkeep | SOP index, update triggers, review calendar, health checks, ownership, recurring exports and restore tests |
| `11_HISTORY_RELEASES_ARCHIVE` | Controlled time history | Snapshots, releases, migrations, superseded decisions, retired systems, immutable evidence, archive index |

## Company extensions

Add when relevant: strategy and business model; governance and ownership; finance and tax; contracts and insurance; brand; products/services; sales/CRM; marketing; delivery/customer success; people; property/physical assets; board/investor; regulatory quality; supply chain.

Do not duplicate the complete Company Operating System. Link each continuity-critical company record to its canonical operating document and include only the recovery metadata and minimal last-known-good export needed by policy.

## Project extensions

Add when relevant: charter; success criteria; stakeholders; scope and non-goals; work breakdown; schedule; budget; procurement; risks/issues; deliverables; quality plan; approvals; lessons; closure/transfer.

## Software and AI extensions

Add when relevant:

- repository map, default branch, protected branches, commit/release identifiers, submodules, package registries;
- runtime and toolchain versions, dependency lockfiles, build commands, environment topology, configuration schema;
- architecture diagrams, APIs, events, schemas, migrations, data lineage, storage, queues, scheduled jobs;
- CI/CD, infrastructure-as-code, secrets references, domains/DNS, certificates, hosting, observability, alerts;
- test matrix, fixtures, seed data, performance/security/accessibility baselines;
- release, deploy, smoke test, rollback, incident, restoration, and local-development runbooks;
- AI models/providers, prompt and agent versions, evaluation datasets, safety gates, cost/limit assumptions, fallbacks;
- licenses, model/data provenance, third-party terms, export and provider-exit path.

Never document a command as reproducible without its prerequisites, version constraints, inputs, expected output, verification, and failure/rollback behavior.

## Physical or media extensions

Add locations, custody, equipment, serial/asset references, insurance records, maintenance, source media, masters, project files, fonts, licenses, color/audio settings, render/export recipes, delivery specifications, and off-site copies as applicable.

## Working-state separation

Within operational modules, separate:

- `INBOX_UNVERIFIED`
- `WORKING_DRAFTS`
- `AWAITING_REVIEW`
- `APPROVED_CURRENT`
- `RELEASED`
- `SUPERSEDED`
- `ARCHIVED`

Do not infer status from folder name alone; critical artifacts must also carry explicit metadata.

## Portability rules

- Prefer open, durable formats for critical text and registers, while retaining original native files where needed.
- Avoid names that break across macOS, Windows, Linux, ZIP archives, or common cloud drives.
- Keep one navigation index; do not require searching nested trees to locate current truth.
- Record both portable relative paths and external system identifiers.
- Keep a machine-readable manifest plus a human-readable map.
- Make archive snapshots immutable or clearly write-protected where the environment allows.

