---
name: trace-code-history
description: Reconstruct why code exists by tracing public GitHub file history, commits, pull requests, referenced issues, patches, and tests. Use when a user asks why a file or code region was introduced, whether historical evidence supports removing it, what change motivated it, or which repository artifacts document the decision.
---

# Trace Code History

Produce an evidence-backed explanation of code provenance. Treat repository records as facts and inferred developer intent as inference.

## Workflow

1. Identify the GitHub repository and repository-relative file path. Ask only for missing information that cannot be inferred from a supplied GitHub URL.
2. Call `trace_code_history` first. Include the narrowest useful line range when the user points to specific code.
3. Review the returned candidates, confidence levels, exact patch matches, associated pull requests, referenced issues, and test files.
4. Use `get_file_content`, `get_file_commit_history`, `get_commit_context`, or `get_issue_or_pull_request` only when the aggregate trace needs a closer look.
5. Use `search_repository_history` when filenames changed or the direct history does not expose the motivating discussion.
6. Stop when the evidence explains the change or when the available public history is exhausted. Do not invent missing issue or PR context.

## Evidence Rules

- Cite absolute GitHub URLs returned by the tools next to the claims they support.
- Label a statement as **Confirmed** only when a commit, pull request, patch, test, or release record directly supports it.
- Label a statement as **Likely** when multiple records support the interpretation but intent is not stated explicitly.
- Label a statement as **Unknown** when the available history does not establish the answer.
- Do not treat a commit message alone as proof of runtime behavior; corroborate it with changed files or tests when possible.
- Do not claim that code is safe to remove. Describe evidence, likely dependencies, missing tests, and a validation plan.
- State that line attribution is an evidence-based approximation when GitHub's available APIs do not provide a true blame result.

## Response Shape

Return these sections:

1. **Short answer** — one or two sentences.
2. **Decision timeline** — dated commits and associated PRs in chronological order.
3. **Why the code exists** — confirmed facts followed by clearly marked inference.
4. **Tests and affected areas** — relevant changed files and regression coverage.
5. **Removal or rewrite risk** — evidence-based risks and checks to run.
6. **Evidence gaps** — missing or inaccessible context.

Keep raw patches brief. Prefer links and explain only the lines relevant to the user’s question.
