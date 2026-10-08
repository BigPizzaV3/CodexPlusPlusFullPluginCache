---
name: wistia-registration-updates
description: Track registration pacing for a Wistia webinar against its goal and deliver scheduled updates (weekly, ramping to daily the week of the event, no weekends). This is STEP 2 of a three-skill webinar workflow (create → registration updates → post-event recap). Use when setting up or running pre-event registration reporting, checking how signups are pacing vs goal, flagging low registration or hot leads, or when handed off from webinar-event-creation. When the event ends it hands off to the post-event recap skill.
---

# Webinar Registration Updates (Step 2 of 3)

Answer the recurring promo-phase question: **are we going to hit our registration goal, and if not, how far off are we?** Pulls live registration data, compares to the goal, and delivers a short, scannable update — as a **scheduled task in Claude** that ramps in frequency as the event nears.

Middle of three sequential skills: `webinar-event-creation` → **this** → `wistia-webinar-recap`. Coordinates via **`webinar-state.json`** in the working folder.

## Identify the webinar

Read `webinar-state.json` for the active webinar (`webinar_hashed_id`, `goal`, `scheduled_for_utc`, `time_zone`). If there's no state file (Sam started here), auto-detect the soonest **upcoming published** webinar via `get-webinars` (`registration_status == published`, `scheduled_for` in the future, not `ended`, excluding test titles), confirm with Sam, and write `webinar-state.json`. Set `stage: "promoting"`, `reporting_scheduled: true` once the schedule is set.

Remember the timezone quirk: `scheduled_for` clock time is local to `time_zone`, not UTC.

## Pull the numbers (Wistia MCP)

- `show-webinar-analytics` → current total `registrations`, `impressions`.
- `show-webinar-registration-timeseries` (`granularity: daily`) → daily series for run-rate, trend, and spikes. Average the last ~7 non-empty days; registration is spiky, so don't trust a single day.
- `show-webinar-audience` (recent registrants, ~1 page) → for the Notes: tally `referrer_domain`/`utm_source` (new sources), scan `company`/email domain (notable logos), flag repeat-visit or enterprise/target-account registrants (hot leads). Keep it light — don't paginate the whole list.

## Pacing math

`current`, `goal`, `days_left` (to `scheduled_for`), `rate` (recent daily run-rate).
- **% to goal** = current / goal
- **Required run-rate** = (goal − current) / days_left — compare to actual `rate` (most useful single number)
- **Projected final** = current + rate × days_left → on track (≥100%), slightly behind (85–99%), or **behind / "low reg"** (<85%, surface prominently with a lever: extra email, paid, partner promo).

**Known caveat (projection parked):** the trailing-average `rate` is inflated by email-send spikes, so projections overshoot right after a send (a mid-campaign test projected ~554; actual was 469). Planned fix: report projection as a range (organic-baseline floor vs recent-average ceiling). Until then, lead with the **% to goal** and **required vs actual rate**, and treat the single projected number cautiously.

## Output format (required)

```
<Webinar title>
Date: MM/DD/YY | <N> Days till Showtime
Goal: <goal> Registrations
Current: <current> Registrations | <%> of Goal

Notes:
• <spikes — biggest recent day + the promo that likely drove it>
• <new sources of registration>
• <notable logos among recent registrants>
• <hot leads to flag for sales — repeat visits, enterprise/target accounts>
```

The header block is fixed; **Notes** carry the value — include only bullets with something real to say. Don't invent data; if nothing notable since last run, write "Steady period — nothing notable to flag."

## Delivery & cadence (scheduled task)

These are delivered as a **scheduled task in Claude**, anchored to the event date:
- Until the week of the webinar: **weekly**.
- The week of (≤ 7 days out): **daily**.
- **No weekend updates.** After the event: stop and hand off to step 3.

Implement with **one weekday task** (`0 9 * * 1-5` — 9am local, Mon–Fri) and gate inside the prompt by `days_until`:
- `days_until > 7`: weekly phase — only post on **Mondays**; otherwise exit quietly.
- `0 ≤ days_until ≤ 7`: daily phase — post every weekday.
- `days_until < 0`: event over — see *Handoff* below.

The scheduled task's prompt must be **self-contained** (fresh run, no memory): include the webinar's hashed ID, goal, event date, which Wistia tools to call, the gating rule, and the exact output format. Tell Sam the cadence you set so he can adjust or pause it, and suggest he click "Run now" once to pre-approve the Wistia tools so unattended runs don't stall on permissions.

## Handoff → Step 3

When a scheduled run finds the event has passed (`days_until < 0`):
1. Post a brief final note ("Registration closed at <final> / <goal> — <%>").
2. Set `webinar-state.json` `stage: "recapped_pending"` and recommend **disabling this scheduled task**.
3. Prompt Sam to run **`wistia-webinar-recap`** for the performance breakdown (or, if appropriate, invoke it directly).

So the sequence self-advances: the last pre-event run is also the trigger to move to the recap.

## Not in scope

Hot-lead alerting to sales as its own workflow, and CRM/pipeline reporting, are intentionally out of scope (Stage 4 dropped). Hot leads surface only as a Notes bullet here.
