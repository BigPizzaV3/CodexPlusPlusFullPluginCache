---
name: kb-maintenance
description: Use for the receiving project's KB linting, stale-content review, context refresh, lifecycle hygiene, contradiction/duplication audits, archival, and safe cleanup.
---

# KB Maintenance Skill

Apply the [receiving-project contract](../../references/project-context.md) for project paths, authority, companion skills, and the lint script's supported layout.

## Goal
Keep the active knowledge surface small, current, coherent, and cheap for agents to load while preserving historical rationale outside the default retrieval path.

## Trigger
Use for periodic maintenance, milestone-exit hygiene, stale-context review, archive/supersede work, decision cleanup, or KB quality audits. Also run after major migrations, balance phase exits, architecture changes, large decision growth, or long multi-session work series.

## Maintenance modes
### Light hygiene
Run frequently or at major task boundaries:
- broken links
- missing/invalid metadata
- duplicate IDs
- stale active Work state
- expired `review_after`
- active indexes pointing to superseded/archived owners
- missing replacement links
- obvious orphan context/index files

### Deep hygiene
Run at milestones or periodically:
- semantic contradictions
- duplicated canonical concepts
- long-lived temporary decisions
- stale `_Context.md` versus canonical docs
- completed work still in active paths
- obsolete migration/audit artifacts
- Source-of-Truth ownership drift
- oversized operational monoliths that should be indexed/split

## Hot/Warm/Cold policy
Maintenance protects progressive disclosure:
- Hot = root agent guide, project state, relevant domain context.
- Warm = triggered skills, active canonical docs, active decisions/work.
- Cold = legacy/superseded/history/research/archive.

Superseded or archived material must not leak into Hot/active indexes unless explicitly referenced for history.

## Action policy
- **Retain:** historically valuable decisions, major audits, final validations.
- **Archive:** completed trackers, stale working-state snapshots, superseded methodologies, historical snapshots.
- **Delete:** only clear duplicates, empty/stub notes, accidental copies, or disposable intermediates whose unique content is already compiled elsewhere.

Ambiguous destructive deletion requires owner approval.

## Deterministic-first rule
Mechanical checks should be implemented in scripts when possible, e.g. `kb_lint.py`, rather than repeatedly asking an LLM to reason about them. LLM reasoning is reserved for semantic contradiction, duplicate meaning, staleness, merge/split decisions, and lifecycle judgment.

### Current lint script
Read [runtime and project profiles](references/linting.md) before the first run. Resolve this installed skill's [lint script](scripts/kb_lint.py), use Python 3.9+ with its [runtime dependencies](requirements.txt), and pass the receiving vault root explicitly. The following paths are placeholders to replace with those resolved locations:

```bash
python3 "/absolute/path/to/installed/kb-maintenance/scripts/kb_lint.py" "/absolute/path/to/target-vault"
```

Use `--json` for machine-readable output and `--stale-work-days N` to change the default 30-day Work staleness threshold. Select the project's `.kb-lint.json` or pass `--config` with an explicit profile. For audit-only tasks, use an existing profile or a temporary one rather than writing new project configuration. Inspect reported settings, matched files and skipped checks before claiming coverage; zero matching files or exit code 0 alone is not a clean audit.

The script checks YAML metadata/lifecycle, local Markdown links and wikilinks, duplicate decision definitions, current canonical ownership, expired review dates, stale active Work, archive links, replacement metadata and context orphans under the selected conventions. A clean mechanical lint does not replace semantic review. If Python/dependencies are unavailable, state the limitation and continue only the checks the host can actually perform.

## Maintenance output
Produce a compact report grouped by: automatic-safe fixes, archive/supersede candidates, semantic-review candidates, destructive-delete candidates requiring approval, context/index refreshes, and unresolved ownership conflicts.

After accepted maintenance, rebuild affected indexes/context, read back changed artifacts, and ensure `PROJECT_STATE.md` remains compact rather than becoming a maintenance log.
