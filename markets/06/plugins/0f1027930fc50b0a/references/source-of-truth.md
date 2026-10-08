---
type: system
status: active
version: 2.0
last_updated: 2026-09-03
scope: reusable reference; receiving-project policy takes precedence
---

# Source of Truth

Apply the [receiving-project contract](project-context.md). Paths and product names
in this reference describe a possible KB layout and source routing; resolve their
actual equivalents from the receiving project rather than requiring those tools
or creating those directories automatically.

## Purpose
Define project-wide authority and conflict rules without requiring agents to load a cross-domain ownership monolith. Detailed domain routing lives in the receiving project's domain index.

## Default startup
Do not read the full Domain Index at cold start. Follow `AGENTS.md` → `PROJECT_STATE.md` → relevant `_Context.md` → triggered skill → smallest canonical document set. Use the receiving project's domain index only when ownership is not already clear.

## Authority classes
| Knowledge type | Canonical owner |
|---|---|
| Agent operating rules | `AGENTS.md` |
| Current project-wide state | `PROJECT_STATE.md` |
| Durable design intent, gameplay rules, rationale | Canonical KB GDD/system note for the domain |
| Detailed ownership lookup | the receiving project's domain index |
| Active durable decisions | `00_System/Decisions/Active.md` |
| Decision history/rationale | `00_System/Decisions/Index.md` and `00_System/Decisions/Records/` |
| Structured configuration / live numeric balance data | Designated live configuration, Sheets, or CSV |
| Implemented behavior and schemas | Designated repository/runtime evidence |
| Final UI/UX layout and prototypes | Designated visual-design source |
| Raw analytics and production outcome data | Designated analytics source |
| Supporting non-canonical material | `90_References/` |
| Retired/historical knowledge | `99_Archive/`, superseded decision records, archived Work |

## Structured-config authority
- Resolve the primary live structured-config source from the receiving project. `BlueprintData` is a source-project example, not a required name.
- A configured value proves current configured behavior, not that design or balance validation is complete.
- Synced repository CSV files are release-build artifacts expected to follow an approved Sheet snapshot; they are not independent design validation.
- Sheet/CSV mismatch is a release-sync observation unless another canonical owner establishes a different defect.
- Balance promotion must validate/retune the designated live values first, then synchronize the approved snapshot for release.

## Design versus runtime
- The KB owns accepted intended behavior; code/runtime owns implemented behavior.
- Runtime evidence must not be silently promoted into design intent.
- Design intent must not be presented as implemented behavior without evidence.
- Use the [Runtime Audit skill](../skills/runtime-audit/SKILL.md) when reconciling these layers.

## Conflict rule
1. Identify the knowledge type and relevant domain.
2. Locate the canonical owner via the active context or the receiving project's domain index.
3. Prefer the designated canonical owner for that knowledge type.
4. If intent/ownership remains ambiguous, surface the conflict and resolve it before writing a new canonical fact.
5. Preserve material runtime/config drift explicitly; do not merge incompatible claims into confident prose.

## History rule
Chat history and assistant memory are working convenience, never project Source of Truth. Superseded decisions, legacy GDD, completed work, historical audits, and archive are Cold knowledge and must not enter default active context unless history, migration, validation, or conflict investigation requires them.
