---
name: coderabbit-learnings-curator
description: Curate CodeRabbit learnings CSV exports. Use when Codex needs to review, merge, globalize, de-duplicate, scope, remove one-off rules, document superseded or contradictory rules, create a git-tracked cleanup draft, or generate review reports for CodeRabbit learnings databases such as learnings.csv.
---

# CodeRabbit Learnings Curator

## Goal

Turn a raw CodeRabbit learnings export into an auditable first draft that a reviewer can inspect, correct, and import back into CodeRabbit.

## Required Outputs

Create these files in a local git repo:

- `learnings.csv`: curated draft using the original CSV schema.
- `review-index.md`: numbered raw export, one original rule per section.
- `merged-rules.md`: for each merged rule, list original rules first and the resulting merged rule after.
- `cleanup-notes.md`: summarize merge decisions, removals, scope changes, contradictions, and questions.

Commit the untouched raw export before editing. Keep curated changes uncommitted unless the user asks for a commit.

## Workflow

1. Copy or move the raw `learnings.csv` into a temporary local git repo.
2. Commit the raw CSV as the baseline.
3. Run `scripts/build_review_index.py` to create `review-index.md`.
4. Inspect rules by repository, file pattern, usage count, and repeated wording.
5. Draft curated rows with deliberate scope:
   - `GLOBAL`: use only for rules that are truly independent of company/repo context.
   - `GINA Solution`: use for cross-repo company rules.
   - Repository name: use for local implementation facts or conventions.
6. Merge only when the resulting rule is clearer and still technically true.
7. Remove one-off rules unless they document security, external contracts, explicit team policy, contradictions, or recurring false positives.
8. Never silently delete contradictory rules. Keep the current rule, remove or supersede the older rule, and document the decision in `cleanup-notes.md`.
9. Prefer preserving author intent over enforcing a global style. For example, say to keep explicit-property or positional-only record style as the author intended instead of converting everything to one style.
10. Run `scripts/generate_merged_rules_report.py` after updating `learnings.csv`.
11. Run `scripts/validate_learnings_csv.py` before reporting status.

## Curation Heuristics

Treat a rule as a good global or company-scope candidate when it appears in multiple repositories, names a shared library, describes shared CI/build behavior, or captures a company-wide review preference.

Keep a rule repository-scoped when it depends on a specific module, route, framework version, data contract, UI behavior, or known future task in that repo.

Remove or deprioritize rules with low usage when they describe a single PR, one exact file, or temporary implementation detail. Keep low-usage rules when they prevent security regressions or explain external behavior the reviewer cannot infer from code.

For test conventions, split mixed rules into narrow rules. Avoid combining framework/tooling choices, `sut` naming, `[Fact(DisplayName=...)]`, and fixture-field placement unless the same scope really owns all of them.

For review reports, show originals before merged output so the human reviewer can judge whether the merge preserved meaning.

## Scripts

Use these scripts from the skill folder:

```bash
python scripts/build_review_index.py learnings.csv review-index.md
python scripts/generate_merged_rules_report.py learnings.csv review-index.md merged-rules.md
python scripts/validate_learnings_csv.py learnings.csv --removed-sources 104,151,152,169 --removed-sources 121,140,145,148,149
```

`--removed-sources` is optional and can be repeated for source-id groups that the reviewer asked to remove.
