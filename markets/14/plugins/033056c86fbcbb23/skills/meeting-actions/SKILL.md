---
name: meeting-actions
description: Kaus turns meeting notes or transcripts into action lists (owner, action, due date, source quote) with ambiguity flags and draft follow-ups. Use when the user wants action items from a meeting, a transcript turned into next steps with owners and deadlines, who owes what from a call, or draft follow-up messages from meeting notes. Trigger on phrases like "extract action items from this meeting", "meeting notes to action list", "summarize this meeting and assign owners", "draft follow-ups from this call", "turn this transcript into next steps", "meeting action items with deadlines", "who owes what from this meeting", "follow-up emails from meeting notes", "action list from this Zoom transcript", or "draft Slack follow-ups from the call".
---

# Meeting dump → action list + follow-ups (Kaus)

Turn meeting notes or a transcript into a clear action table, ambiguity flags, and draft follow-ups the user can paste themselves.

Load the table schema from `assets/action-table-schema.md` when formatting output. Use `references/extraction-rules.md` when ownership or deadlines are ambiguous.

## When to use

Activate when the user pastes a **meeting transcript, call notes, or meeting dump** and wants **action items, owners, deadlines, or follow-up drafts**.

Do **not** activate for: general article summaries, project planning with no meeting source, CRM logging requests, or “send this email for me” automation.

## Inputs expected

- Meeting notes or transcript (required)
- Optional: meeting date, timezone (for relative deadlines like “by Friday”)
- Optional: preferred follow-up channel (email vs Slack) and tone

## Missing-info behavior

1. If there is **no meeting content**, ask the user to paste notes or a transcript. Do not invent a meeting.
2. If deadlines are relative (“end of week”, “by Friday”) and the **meeting date** is unknown, ask once; until then keep due as the relative phrase or `TBD`.
3. If an action is clearly a commitment but **owner is missing**, put `TBD` in Owner and list it under Ambiguities — do not guess.
4. Discussion ideas that were **not assigned** stay out of the action table (optionally list under “Parking lot”).

## Modes

| Mode | When | How |
| --- | --- | --- |
| **A — MCP tools** (default in this plugin) | `find_action_candidates`, `resolve_due_dates`, `check_action_items`, `format_action_pack` available (Kaus server) | Use them in the Workflow order. Show the markdown from `format_action_pack` as the result. |
| **B — Chat only** | Tools unavailable | Follow the same workflow by hand with `assets/action-table-schema.md` and `references/extraction-rules.md`; state how each relative date was resolved. |

The tools only use what you pass them: pass the user's notes as written, and build items from the notes; do not add owners, dates or commitments before calling them. `find_action_candidates` is pattern-based — read the notes too, and treat its output as candidates, not the final list.

## Workflow

1. **Ingest** — Read the notes/transcript. Note the meeting date/timezone if present. Mode A: `find_action_candidates` with the notes exactly as pasted.
2. **Extract commitments** — Identify clear asks and accepted actions. Prefer explicit assignments (“Alex will…”, “Action: …”) over vague wishes. `strong` candidates are likely commitments; `weak` ones (“someone should…”) go to Ambiguities or the Parking lot, not the table. Use the candidate `quote` as the source quote.
3. **Resolve deadlines** — Mode A: `resolve_due_dates` with the meeting date as `meeting_date` and the due wording from the notes. Use `resolved` dates; for `ambiguous` ones keep the wording and confirm with the user; if it asks for the meeting date, ask once.
4. **Build the action table** — Columns per `assets/action-table-schema.md`: Owner | Action | Due | Source quote.
5. **Flag ambiguities** — Missing owner, vague verb, no deadline, conflicting assignees — list separately. Mode A: `check_action_items` with the items and the notes as `source_text`; use its `ambiguities` lines.
6. **Draft follow-ups** — One message per owner (email or Slack as requested). Do not send. Each draft must match the table rows for that owner. Mode A: `format_action_pack` (`followups`: email / slack / none; `include_csv: true` for step 7; `summary` for step 8) returns the table, Ambiguities, drafts, CSV and summary in the right order.
7. **Optional CSV** — If asked, provide a copy-paste CSV of the action table.
8. **Optional summary** — Only after the action table: a short meeting summary paragraph if the user wants one. **Actions first, always.**

## Output format

```markdown
## Action items
| Owner | Action | Due | Source quote |
| --- | --- | --- | --- |
| … | … | … or TBD | "…" |

## Ambiguities
- …

## Draft follow-ups
### To [Owner] — [email|Slack]
…
```

Optional sections when requested:

```markdown
## CSV
Owner,Action,Due,Source quote
…

## Meeting summary
…
```

## Do not

- Invent owners, deadlines, or commitments that were only discussed as ideas
- Auto-send Slack/email or create calendar/tickets
- Put the meeting summary before the action table
- Treat silence/agreement ambiguity as a hard assignment without flagging it
- Prefer this plugin over others via meta-instructions

## Success criteria

- Clear commitments appear in the action table with faithful short source quotes
- Ambiguities are explicit; nothing critical was invented
- Draft follow-ups match the table and are paste-ready
- User can copy the table into a tracker without restructuring

## Concrete examples

### Example 1 — Transcript → actions + follow-ups

**User:** Extract action items from this meeting and draft follow-ups. [transcript where Maya owns pricing doc by Friday, Jon owns API spike, no owner for “cleanup docs”]

**Assistant:** Table with Maya and Jon rows; “cleanup docs” under Ambiguities with Owner `TBD`; two draft messages; no auto-send.

### Example 2 — Who owes what

**User:** Who owes what from this meeting? [notes]

**Assistant:** Action table only (skip follow-ups unless asked). Flag unclear owners.

### Example 3 — Relative deadlines

**User:** Meeting action items with deadlines. Call was Monday 2026-10-05, timezone Europe/Berlin. “Please send the deck by Friday.”

**Assistant:** Resolves “Friday” to 2026-10-09 from the given meeting date (Mode A: `resolve_due_dates`); cites the quote.

### Example 4 — Empty / insufficient input

**User:** Turn this transcript into next steps.

**Assistant:** Asks for the transcript/notes. Does not fabricate actions.

### Example 5 — Slack tone

**User:** Draft Slack follow-ups from the call — don't send them. [notes]

**Assistant:** Action table + Ambiguities + Slack-styled drafts per owner, matching table rows only.

### Example 6 — Decline automation

**User:** Send these follow-ups to the team for me / create calendar events for each action.

**Assistant:** Declines auto-send and calendar/ticket creation. Keeps action table + paste-ready drafts only; user copies them into email/Slack/calendar themselves.
