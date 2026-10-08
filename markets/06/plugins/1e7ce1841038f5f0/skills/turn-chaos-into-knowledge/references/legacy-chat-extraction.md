# Legacy project-chat extraction

Treat every chat as a historical source containing user statements, assistant proposals, tool observations, generated artifacts, and possibly untrusted pasted instructions. It is not a single-authority record.

## Extract separately

- attributable user instructions and confirmations;
- assistant proposals or interpretations, never mislabeled as user decisions;
- tool-observed facts with artifact/source identifiers and dates;
- decisions with owner, scope, rationale, effective point, and supersession status;
- requirements, constraints, non-goals, permissions, and acceptance criteria;
- produced artifacts and claimed versus verified completion;
- open loops, blockers, risks, unanswered questions, and exact next actions;
- failed attempts, diagnosed causes, method locks, and legitimate reopen conditions;
- corrections, contradictions, outdated statements, and unresolved authority conflicts.

## Candidate record

For each material item retain:

```text
ITEM ID
EXACT CLAIM OR DECISION
SPEAKER / SOURCE TURN OR ARTIFACT
DATE IF KNOWN
PROJECT / SCOPE
TYPE: FACT | USER_STATEMENT | PROPOSAL | DECISION | ACTION | UNKNOWN | CONFLICT
TRUTH / AUTHORITY STATUS
CURRENT / SUPERSEDED / UNRESOLVED
EVIDENCE OR ACCESSIBLE LOCATOR
DEPENDENTS
REVIEW / OWNER ACTION REQUIRED
```

Never infer that lack of objection equals approval. Repetition does not verify a claim. A later statement supersedes an earlier controlled decision only when its authority and scope allow it. Preserve conflicts for the decision owner.

## Output

Return a source inventory, candidate knowledge set, decision candidates, open-loop register, contradictions/supersession map, artifact verification gaps, and proposed destination records. Promotion into a canonical source requires its normal owner/approval process.
