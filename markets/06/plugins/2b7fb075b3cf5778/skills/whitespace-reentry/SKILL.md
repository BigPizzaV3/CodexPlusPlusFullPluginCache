---
name: whitespace-reentry
description: Recover a paused project or decision from evidence and identify the next actionable step.
---

# Whitespace Reentry

Restore the thread of the work, not a dump of everything available. Context is a view for the current person or agent, question, and moment.

## Choose the outcome

Infer the mode from the request:

- **Resume** — recover intent, stopping point, current state, and one next move.
- **Decision trace** — reconstruct a decision, its evidence and alternatives, and whether it still holds.
- **Handoff** — prepare another person or agent to continue without rereading everything.
- **Drift check** — compare a plan, status note, or prior claim with current evidence.
- **Possibility compression** — turn many open loops into at most three explainable, reversible paths.

Read [references/modes.md](references/modes.md) only when a mode needs its detailed evidence and output fields. If multiple modes apply, combine them without repeating facts.

## Find the working truth

- Identify the target and the relevant time horizon. Ask at most one focused question when either cannot be inferred safely; otherwise proceed with a clearly labelled partial view.
- Start with bounded evidence: user-provided material, workspace instructions, current status, recent changes, and artifacts likely to preserve intent.
- Use this evidence order when sources conflict:
  1. current observable state, such as tests, runtime behavior, or authoritative records;
  2. current source and configuration;
  3. recent change history and decisions;
  4. plans, handoffs, tickets, and messages;
  5. prior summaries, used only for orientation until corroborated.
- Put an absolute date or timestamp beside volatile claims when available.
- Respect the user's scope. Do not widen a focused request into a broad scan of unrelated files, accounts, or history.
- Keep private inputs within their authorized environment. Do not expose secrets, credentials, personal records, or raw internal data in the brief.

## Separate knowledge states

Use plain labels when the distinction matters:

- **Observed** — directly checked in the current run.
- **Reported** — stated by a source but not independently confirmed.
- **Inferred** — a conclusion drawn from evidence.
- **Recommended** — a proposed path, not a fact.

Expose conflicts instead of averaging them into a fluent story. Prefer `confirmed`, `likely`, `stale`, or `unknown` over invented numeric confidence.

## Return a useful view

Default to a brief that fits on one screen:

1. **The thread** — what the user was trying to accomplish and why.
2. **State now** — what is currently true and what changed.
3. **Open loops** — only the unresolved items that affect continuation.
4. **Next move** — one concrete, reversible action, including its expected evidence of completion.
5. **Confidence** — what was directly verified and what remains reported, inferred, stale, or unknown.

Link concrete files, records, commits, tests, or URLs when available. Add an evidence table only when three or more claims need comparison; use `Claim | State | Evidence | Freshness`.

If the user asks to save, share, or hand off the result, create a portable **Reentry Capsule** using the template in [references/modes.md](references/modes.md). Do not create a file unless requested.

## Continue only with authority

Reentry is read-oriented by default. If the user also asks to continue, follow the permissions and operating agreements for that task. Orientation does not authorize edits or external effects. Do not publish, send, deploy, purchase, delete, or accept a proposal merely to make the context feel complete.

Treat these as separate states when relevant: source changed, tests passed, artifact built, service reachable, newest version visible, external submission accepted, and runtime behavior verified.

## Be honest about gaps

- Label stale, partial, conflicting, and unknown state plainly.
- Never turn configured, compiled, queued, uploaded, or reachable evidence into a stronger success claim.
- If available evidence cannot recover the user's intent, say what is missing and offer the least burdensome way to supply it.

## Product boundary

This is a skills-only workflow. It does not connect to Whitespace Live, a Context Graph, an account, or external connectors, and it must not imply that it does. A future authenticated service may add bounded live context reads, but live data access and write authority remain separate capabilities.
