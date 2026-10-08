# Handoff schema

Use the shared [Context Package](../../../shared/expert-system/context-package.md) as the context field source; aliases in this schema carry the same meaning. Minimum handoff: objective, current verified state and accessible evidence/source, permission boundary, remaining work, next action and acceptance. For material work add title/date, sender/recipient, relevant decisions, unknowns, exclusions, changed artifacts, tests, dependencies, risks and freshness warning. Omit irrelevant headings, never critical unknowns. The handoff is a derived snapshot, not a new source of product authority.

For controlled implementation also require: current phase and gate, active skill, lead/support/review roles, current task execution contract, requirement and decision classes, logged Class-2 decisions, last approved visual checkpoint, current perceptual status, unresolved authority decisions, stop rules, and rollback.

For a logical chat/session rollover also require: observed rollover reason, `CONTINUE_CURRENT_SESSION` or `START_FRESH_SESSION`, read-first canonical sources in order, active focus, material delta since the prior checkpoint, open loops, applicable method locks/do-not-reopen conditions, exact next action, acceptance, and recipient-access gaps. A rollover package links evidence; it does not copy the full conversation.

Preserve applicable `METHOD_LOCK` views through the Context Package, including scope and record/source version. The receiver resolves and acknowledges the lock before execution; inaccessible records require the compact canonical view or a dependent-work blocker. Do not reopen a method because its original research chat is absent.

Never include passwords, tokens, full secrets, unnecessary personal data, or invented status.

## Coding-agent state block

Required where relevant for ongoing agent execution; otherwise omit the block:

CODING_AGENT; PROVIDER; MODEL / MODE if relevant; SESSION_STATE; SESSION_IDENTIFIER if safe and available; CONTEXT_HEALTH with evidence; CLAUDE_MD_VERSION (or other provider instruction manifest); PROJECT_HARNESS_VERSION; ACTIVE_LOCAL_SKILLS; ACTIVE_SUBAGENTS; CURRENT_BRANCH; CURRENT_REVISION; WORKING_TREE with ownership; LAST_AGENT_TASK with attempt; LAST_AGENT_REPORT; LAST_VERIFIED_EVIDENCE with tested revision; OPEN_AGENT_BLOCKERS; CONTINUE_CURRENT_SESSION or START_FRESH_SESSION with rationale; NEXT_TASK_CONTRACT with accessible versioned sources.

Unknown state is explicitly unknown, not inferred from a report. Hash/version applicable instructions and source manifests; verify recipient access. A fresh session may reload persistent context; do not promise memory deletion. No session credentials or tokens.
