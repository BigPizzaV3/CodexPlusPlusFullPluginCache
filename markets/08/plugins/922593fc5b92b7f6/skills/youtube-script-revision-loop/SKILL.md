---
name: youtube-script-revision-loop
description: 'Revise a YouTube script with the user, then re-check it with Prepublish so each round fixes the highest-priority flagged passages first. Use when the user says "fix my script", "improve this draft", "apply the suggestions", "rewrite the weak parts", "make it more engaging", "tighten the pacing", "help me revise before I record", or wants to compare draft one and draft two of the same video. Works from an existing Prepublish audit in the conversation or starts one. Do not use to generate a script from nothing or to rewrite someone else''s script without the user''s request.'
---

# Revise and re-check a YouTube script

A good revision round changes a few high-priority passages, keeps the creator's voice, and checks that the fixes landed. This skill runs that loop with `audit_script`, `get_audit` and, for openings, `audit_hook`.

Read `references/tools.md`, `references/report-fields.md` and `references/claims-and-limits.md`. Use `assets/revision-plan-template.md` for the plan you show the user.

## Before the first round

- Make sure there is an audit of the current draft. If the conversation already has one (an `analysis_id` or a report), reuse it with `get_audit` instead of paying for a new audit. If not, run the `youtube-script-audit` workflow first.
- Ask one question if it matters and is unknown: "Should I keep your wording where possible, or rewrite freely?" Default to keeping the creator's voice.

## Each round

1. **Plan.** Take the CRITICAL and HIGH items, at most three per round. For each: location, the user's line, the problem in one sentence, and the fix. Use Prepublish's rewrite where it was included. Where the rewrite is locked or missing, write your own fix and label it "My suggestion".
2. **Confirm.** Show the plan using the template. Let the user accept, change or skip items.
3. **Apply.** Produce the revised script with only the agreed changes. Mark changes so the user can see them (for example a short list of "changed lines" after the script). Never silently change facts, names, numbers or claims in the script.
4. **Re-check.** Ask before spending another audit: "Re-audit the revised draft?" If yes, call `audit_script` with the full revised script and the same title. If only the opening changed, `audit_hook` on the new opening is a cheaper check.
5. **Compare.** Show before and after for the overall and three sub-scores, and whether the fixed passages are still flagged. Say what improved and what is still open. Present score changes as a better read of the text, never as a predicted change in views or retention.
6. **Stop** when there are no CRITICAL or HIGH items left, when `ready_to_record` is true, when the user is satisfied, or after three rounds. Do not chase small score changes; MEDIUM and LOW items are optional polish.

## Voice and fidelity rules

- Keep the creator's phrasing, jokes, catchphrases and point of view unless a flagged passage requires a change.
- Do not add facts, statistics, quotes or claims that were not in the script. If a fix needs a fact ("add a specific number"), ask the user for it or leave a clearly marked placeholder like `[your number]`.
- Keep the title's promise intact, or flag the mismatch if the script cannot deliver it.
- If the user's instruction conflicts with a Prepublish suggestion, follow the user and note the trade-off once.

## Limits

Anonymous users get 3 free full audits a day. A full loop can use two or three. Tell the user when a re-check would use their last free audit of the day, and prefer `get_audit` and `audit_hook` where they are enough.
