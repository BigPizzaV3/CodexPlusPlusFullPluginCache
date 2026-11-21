# Governance and decisions

## Exact preview flow

Use `preview_change` for confirmed Frame, finalized output, commercial decision, Review and close, reopen, context decision or sanitized outcome contribution.

The preview is read-only. Present:

- exact content and decision type;
- current basis versions;
- warnings and lifecycle effects;
- caller authority and `canCommit`; and
- expiry.

When `canCommit` is false, explain the missing authority or readiness and stop. When it is true, ask whether the user confirms this exact preview. `decide_change` receives the same unexpired fingerprint only after an explicit yes. A changed basis, different caller or expired preview requires a new preview.

## Context

`get_workspace_context` returns active reviewed workspace guidance. Proposals are not approved context. `propose_context_change` saves a bounded candidate; an owner or admin then uses the exact context-decision preview. Disputed, stale, retired or unreleased context is not silently applied.

## Attention

Profile attention is bounded and prioritized. Explain at most the returned items and act on the one most relevant to the current task. Review requests, decision requests, expiring access, stale outcomes and overdue decisions remain distinct. Attention does not transfer decision rights.

## Outputs and commercial decisions

Prepared outputs cite current evidence and basis versions. Finalization is distinct from file creation. A commercial decision records the authorized position; it does not contact a counterparty, accept an offer, publish a proposal or transfer funds.

## Review, lessons and contribution

Terminal Review records the actual commercial outcome and supports approved lesson candidates. A lesson becomes reusable workspace context only after its own governed context decision.

Sanitized outcome contribution is optional and requires an owner or admin's exact preview and consent. It carries the allowlisted outcome only. Withdrawal changes contribution availability without rewriting the workspace's historical Review record.

## Failure and retry

The server rechecks identity, membership, authority, fingerprint and basis versions. A mismatch commits nothing. Reload authoritative state, explain the changed basis and request a new preview when the user still wants the change. Idempotent retry is for the same confirmed request, not a way to bypass a failed check.
