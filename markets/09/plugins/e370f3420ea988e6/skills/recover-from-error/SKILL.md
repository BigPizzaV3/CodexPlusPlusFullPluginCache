---
name: recover-from-error
description: |
  Triage repeated keel_* tool failures: capture the errors, read keel_account_status and keel_connection_check, classify by the error's code (auth, scope, quota, sync, validation rule, handoff), and propose one specific next step. Use when the user says "this keeps failing", "what's wrong", "debug this", or pastes an error. Not for a single failure — the originating tool's error already says what to do.
references:
  - step: 4
    topic: "rule:<CODE>"
    why: "the lesson behind a validation issue code"
  - step: 4
    topic: "mistakes"
    why: "structural mistakes that validate but do not work (zero trades, wrong polarity)"
  - step: 4
    topic: "universe_selection"
    why: "Universe selectors and resolved semantics behind EMPTY_UNIVERSE / unknown-symbol errors"
tools:
  - keel_account_status
  - keel_connection_check
  - keel_help
  - keel_feedback
---

# References

Reference topics this workflow cites (keel_help topics):

- Step 4 — `rule:<CODE>` — the lesson behind a validation issue code
- Step 4 — `mistakes` — structural mistakes that validate but do not work (zero trades, wrong polarity)
- Step 4 — `universe_selection` — Universe selectors and resolved semantics behind EMPTY_UNIVERSE / unknown-symbol errors

# Method

## Step 1 — Capture the last three errors

From the tool history: tool names, the `code` (envelope code or validation
issue code), the `message`, and the arguments. Fresh session and nothing
visible → ask the user to paste the most recent error verbatim.

## Step 2 — `keel_account_status`

Auth state and identity, API URL, the toolsets and tools visible right now,
remaining plan quota, cross-surface hints. Most "keeps failing" sessions are
one of: not authenticated, a tool outside the active toolsets, the wrong
account context, or an exhausted quota — all visible here.

## Step 3 — `keel_connection_check` when status looks clean

One read-only pass over auth, API reachability, and the active tool surface;
it exits non-zero on any failed check. Quote what it names in prose, not raw
JSON.

## Step 4 — Classify by code and apply the documented fix

- **Validation issue code** (`TYPE_MISMATCH`, `UNKNOWN_COMPONENT`,
  `SLOT_REF_NOT_FOUND`, `LOADER_TIMEFRAME_UNBOUND`, …) →
  `keel_help(topic="rule:<CODE>")` for the lesson; the issue's `suggestion`
  and `location` say what and where. `UNKNOWN_COMPONENT` is a search-then-edit,
  never a delete.
- **A strategy that validates but trades zero / the wrong way** → the
  `mistakes` reference (binary signals re-normalized, polarity, sizer before
  PSM).
- **401 / 403, `authenticated: false`** → sign in again through whatever
  connected you: on the hosted endpoint, the client's own connect / reconnect.
- **A plan-limit refusal** (`quota_exhausted`, `quota_cap_reached`,
  `plan_feature_unavailable`) → the refusal carries `limit_details` (the unit,
  and for a quota the used, limit and reset numbers) and `resume.verify_call`
  (the exact blocked call, every argument kept). Report the limit and the reset
  in words; a plan-limit refusal is not retried; it lifts at the reset.
- **`handoff_required`** is not an error: it names a step the user completes
  in the Keel web app.
- **`not_found` on a help topic / skill** → the error lists the closest names.

## Step 5 — One specific next step

Not a list of things to try. "The error points at <X>. Try <one call>. If it
still fails, paste the new error." The same call with the same arguments is
not a next step; if the previous call failed with those, they are the problem.

## Step 6 — Do not loop

If the same failure survives a second pass through this workflow in one
session, the loop is not converging: say so and stop retrying. When the user
wants it reported, `keel_feedback` files the report from inside the session —
show them what it will carry first (the exact prompt or command, the error
verbatim, and `keel_connection_check`'s output) and send it once they agree.
Credential or private-account matters go to `https://usekeel.io/contact`, not
into a report.

# Decision points

- Quote the original error verbatim so the user knows you read it; the
  diagnosis names the field or output that led to it.
- A tool you are unsure exists is tried, not declared missing.

# Output shape

1. One-sentence diagnosis ("Your session is not authenticated — sign in
   again").
2. The evidence (which call's output, which field).
3. The single recommended next call or action.
4. Optional: the `rule:<CODE>` or mistake reference.

# When NOT to use

- A first failure with the user not yet stuck → the originating tool's error
  says what to do.
- A "how do I" question → the relevant skill.
- A strategy-logic problem (validates, runs, loses) → `backtest-and-analyze`
  or `overfit-check`; this skill diagnoses tool friction, not edges.

# Test prompts

1. "This keeps failing — same error every time."
2. "I can't get past this 422 on strategy compose, here's the trace ..."
3. "Why does every backtest call return 401?"
