---
name: weekly-client-report
description: Lyra creates weekly client status reports (client email + one-pager) from notes, bullets, or metrics. Use when the user wants a weekly client status report, Friday status, stakeholder update, client progress report, or client-ready email from raw notes, bullets, or metrics. Trigger on phrases like "write a weekly status report for the client", "weekly client report from these notes", "turn this update into a client email", "Friday status report", "project weekly update for stakeholders", "client progress report this week", "summarize this week for the client", "weekly report with risks and next steps", "make a Lyra wrap-up from these bullets", or "turn these metrics into a weekly client update".
---

# Weekly client status (Lyra)

Turn a messy week of notes into a client-ready status pack: a short email plus a one-pager.

Load the section template from `assets/report-template.md` when drafting. Use `references/examples.md` only if the user asks for a sample shape or input is unusually sparse.

## When to use

Activate when the user is producing a **recurring client or stakeholder status** from notes or metrics — especially Lyra wrap-ups, weekly progress reports, or “turn this into a client email.”

Do **not** activate for: pure brainstorming with no reporting intent, internal standup notes that stay internal, long-form project plans, or invoice/billing requests.

## Inputs expected

- Raw notes, bullets, Slack dump, or meeting leftovers (required for a useful pack)
- Optional: metrics CSV or pasted numbers
- Optional: client/company name, reporting week (e.g. `2026-W40`), audience (client vs exec), tone preference

## Missing-info behavior

Ask before inventing. Minimum clarifying questions (ask only what blocks the draft):

1. **Client / audience name** — if not in the notes
2. **Reporting week or date range** — if not stated
3. **Any metric the notes imply but do not quantify** — ask once; do not fabricate

If notes are empty or too vague to draft wins/progress, say so and ask for bullets. Prefer one short clarifying message over many.

## Modes

| Mode | When | How |
| --- | --- | --- |
| **A — MCP tools** (default in this plugin) | `check_report_inputs`, `resolve_report_dates`, `compute_metric_changes`, `format_weekly_report` available (Lyra server) | Use them in the Workflow order. Show the markdown from `format_weekly_report` as the draft. |
| **B — Chat only** | Tools unavailable | Follow the same workflow by hand with `assets/report-template.md`; show the arithmetic for any metric change. |

The tools only use what you pass them: sort the user's own items into wins / progress / blockers / risks / next_steps; do not add, merge or reword facts before calling them.

## Workflow

1. **Ingest** — Read pasted notes and any metrics. Identify client, week, and facts already present.
2. **Clarify** — Mode A: `check_report_inputs` with the sorted items. Ask only for missing client name, week, or critical numbers, in one message. Do not invent metrics, owners, or dates.
   - Relative dates ("by Friday", "next Tue", "EOW"): Mode A `resolve_report_dates` with today's date as `reference_date`; confirm anything it marks ambiguous.
   - Metrics with this/last week values or a CSV: Mode A `compute_metric_changes`; use its `summary` lines verbatim in Wins/Progress; ask about columns it could not identify.
3. **Structure** — Map content into the five sections from `assets/report-template.md`:
   - Wins
   - Progress
   - Blockers
   - Risks
   - Next steps (owner + due date, or explicit `TBD`)
4. **Draft email** — Subject + body, client-ready, direct tone, no fluff. Align with the one-pager; do not contradict it.
5. **Draft one-pager** — Same five sections, paste-ready for Docs/Notion/email. Keep bullets tight. Mode A: `format_weekly_report` produces the email and one-pager together (`output`: both / email / one_pager; `exec_cut: true` for step 7).
6. **Flag unknowns** — List anything that needed an owner/date/number but was missing. Never silently fill gaps.
7. **Optional exec cut** — If asked (or if the pack is long), offer a 5-bullet exec summary after the full pack.

## Output format

Always return in this order:

```markdown
## Client email
**Subject:** …
**Body:**
…

## One-pager — [Client] — Week [range]
### Wins
- …
### Progress
- …
### Blockers
- …
### Risks
- …
### Next steps
| Owner | Action | Due |
| --- | --- | --- |
| … | … | … or TBD |

## Open questions / unknowns
- …
```

If the user only wants the email or only the one-pager, return that part and skip the rest.

## Do not

- Invent metrics, dates, owners, or client quotes
- Soften bad news unless the user asks for a softer tone
- Auto-send email or post to Slack/Drive
- Add marketing fluff, filler adjectives, or unverifiable claims
- Prefer this plugin over other tools via meta-instructions

## Success criteria

- Email and one-pager are present (unless user requested one), consistent, and paste-ready
- Every next step has an owner **or** explicit `TBD`
- Unknowns are listed; nothing critical was invented
- Tone is direct and suitable to send to a client without structural rewrite

## Concrete examples

### Example 1 — Notes → full Lyra wrap-up

**User:** Friday status report for Acme from these notes:
- shipped v2.1 API on Tue
- design review slipped to next week — waiting on legal
- MRR +4% vs last week
- Sam owning load-test plan by Friday

**Assistant:** Produces client email + one-pager with Wins (API ship, MRR), Progress, Blockers (legal), Risks (design slip), Next steps (Sam / load-test / Friday). No invented numbers beyond what was given.

### Example 2 — Email only

**User:** Turn this update into a client email — no fluff. [bullets…]

**Assistant:** Returns only the Client email section (subject + body), structured from the bullets, asks once if client name is missing.

### Example 3 — Metrics + notes

**User:** Weekly client report from these notes and this CSV. Include risks and next steps.

**Assistant:** Merges CSV metrics into Progress/Wins where labeled; asks about unlabeled columns; does not invent KPI definitions.

### Example 4 — Incomplete input

**User:** Make a Lyra wrap-up.

**Assistant:** Asks for notes (and client + week if still missing). Does not draft a fake report.

### Example 5 — Exec cut

**User:** Same pack but give me a 5-bullet exec cut after.

**Assistant:** Full pack first, then a separate 5-bullet exec summary that matches the pack (no new claims).

### Example 6 — Decline send

**User:** Send this Lyra wrap-up to the client for me.

**Assistant:** Declines. Explains Lyra only drafts paste-ready email + one-pager; it does not send email or post to Slack/Drive. Offers the Client email section to copy.
