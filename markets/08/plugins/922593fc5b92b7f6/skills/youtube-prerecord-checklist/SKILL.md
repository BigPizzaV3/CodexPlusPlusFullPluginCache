---
name: youtube-prerecord-checklist
description: 'Run a complete "ready to record?" check on a YouTube script with Prepublish in one pass: spoken runtime against the target length, the opening hook, the full script audit with rewrites, the policy pre-flight and the reused-content check, then give a clear go or fix-first verdict with a short checklist. Use when the user says "is my script ready to record", "final check before filming", "pre-publish checklist", "pre-production review", "check everything before I shoot", "QA my script", or wants one consolidated review instead of separate checks. Do not use for a single narrow question (use the specific skill) or for published videos.'
---

# Ready-to-record check

One consolidated pass over a finished draft, in the order that avoids wasted work: length first (a script that is twice too long changes everything), then the full audit, then the opening, then the risk checks.

Read `references/tools.md`, `references/report-fields.md` and `references/claims-and-limits.md`. Use `assets/prerecord-checklist.md` for the final output.

## Inputs

- The full script, verbatim, and the planned title (both required).
- The target runtime, if the user has one. Ask once; if they have none, skip the length comparison.
- Email for the free audit if the user has no Prepublish account (explain its use first, never invent one).
- Whether the topic is sensitive or the channel reuses a format (faceless, compilation, AI-assisted narration). If unknown, run both risk checks.

## Order of checks

1. **Length**: `script_runtime` with `script_text`. Compare to the target. If the draft is more than 25 percent over or under the target, tell the user now and ask whether to continue or adjust first.
2. **Full audit**: `audit_script` with title, script and target runtime in seconds if given. Handle `running` with `get_audit`.
3. **Opening**: the audit already scores the hook. Call `audit_hook` on the opening only if the audit's hook score is under 50 or the top flagged passage is in the opening, so the user gets hook rewrites.
4. **Policy**: `policy_preflight` with script and title.
5. **Reused content**: `check_authenticity`, when the channel is faceless, AI-assisted, a compilation or list format, or the user asked. Otherwise skip and say so.

Stop early and report if a tool reports an allowance limit. Do not repeat checks already done in this conversation for the same draft; reuse their results.

## Verdict

- **Ready to record**: `ready_to_record` is true or no CRITICAL items remain, no Community Guidelines policy matches, reused-content risk is low or not checked, length within 25 percent of target.
- **Fix first**: anything else. List the fixes in priority order: CRITICAL audit items, Community Guidelines matches, HIGH audit items, high reused-content risk, advertiser-friendly matches the user cares about, length.

The verdict describes the script text only. Say that recording, editing, thumbnail and title packaging are outside the check.

## Output

Fill `assets/prerecord-checklist.md`. Keep it to one screen. Offer to start the `youtube-script-revision-loop` on the fix list.
