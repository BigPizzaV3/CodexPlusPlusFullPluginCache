---
name: graymatter-context
description: Find stored GrayMatter procedures and reusable methods, compile bounded task context, and inspect retrieval receipts. Use for procedure or runbook lookup, task-specific grounding, and explanations of why memory was selected.
---

# GrayMatter Context

Compile the smallest useful authorized context for the current task instead of loading broad memory exhaust.

## Procedure lookup

For a question about an existing procedure, runbook, or repeatable method, including a follow-up after retrieving memory, call `procedure_search` before answering whether one was found. Memory decisions or previous summaries are not a search of the Procedure collection.

Use the requested subject words as `query`, preserving explicit qualifiers, not the whole conversational question. For example, “Is there an existing procedure for production release review?” has the subject “production release review.” Search is case-insensitive phrase matching, not question answering. Do not add an unrequested domain. An empty bounded search proves only that the current search found no match, not that no procedure exists. Report returned enablement, confidence, evidence and binding fields as provided; discovery is not approval or proof of execution.

## Compilation effects and host confirmation

`context_compile` is a write operation: it creates a task-scoped ContextPage and retrieval receipt from authorized sources. A request to compile context does not authorize saving, changing, or forgetting durable memories, changing account scope, or approving a release.

If the host presents a confirmation, use that existing prompt without asking for a separate GrayMatter approval. A verified security or authorization denial stops that operation; do not evade it by rewriting the request, stripping invocation syntax, changing tools or accounts, widening permissions, or substituting searches.

A missing tool, transient connection/server error, or model statement that a call was "blocked" is not by itself a verified security denial or a permanent ban on testing. Inspect the actual tool outcome and authorized receipts, distinguish reported prose from surfaced errors, and repair the implicated layer. Normal same-account OAuth refresh, metadata refresh, or an in-scope bug fix may be followed by at most two controlled validation attempts per recovery episode, using the same native client, account, scopes, and original task. A user-authorized diagnostic may also test an unverified failure through that unchanged path. Record every attempt; stop on a surfaced security/authorization denial or if recovery still fails.

Compilation is not idempotent. For a timeout or uncertain write outcome, inspect existing authorized receipts/effects before another attempt and disclose uncertainty rather than claiming no execution or replaying blindly. Respect a completed tool result whose retrieval policy requires clarification, repair, retry, or denial. A manual search summary is not compiled context and has no compilation receipt; never count it as a compiler pass. Historical failures remain failures; a later successful retest needs its own useful nonempty ContextPage and new authorized receipt.

## Workflow

1. For an authorized context request, call `context_compile` with the original user task text unchanged as `task`, preserving all explicit constraints. Do not expand, paraphrase, or add invented evidence checklists, conditions, or exclusions. Set the token budget and procedure/rating controls separately. Scope and secret restrictions still take precedence.
2. Prefer the compiled ContextPage summary, selected items, hydration pointers, policy result, and receipt reference over raw memory dumps.
3. Respect retrieval policy. If the compiled result indicates low confidence, stale context, partial coverage, conflict, retry, clarification, or denial, follow that action before answering confidently.
4. For procedure discovery, follow Procedure lookup above. Use an authorized high-confidence procedure when it fits the task; do not invent tenant filters.
5. Call `retrieval_receipt_get` when the user asks why context was selected, which sources contributed, or how confidence, freshness, coverage, and policy were evaluated.
6. In that same answer, summarize the selected sources and selection reasons, coverage gaps, source dates/freshness, and answer policy. Disclose disabled or missing evaluator confidence as unavailable, never zero; retrieval, quality, and similarity scores are not evaluator confidence. If a field is missing, say it is unavailable instead of recompiling or inventing it.
7. Cite the receipt ID in the response when provenance or selection rationale materially matters.

## Context discipline

- Keep temporary conversational context in the conversation. Save only durable information through the GrayMatter memory skill.
- Do not request or pass tenant, organization, owner, user, role, permission, or ACL identifiers.
- Do not hydrate every pointer by default. Retrieve more detail only when the current task requires it.
- Treat authorization failures as final for that identifier and do not probe for cross-tenant alternatives.
