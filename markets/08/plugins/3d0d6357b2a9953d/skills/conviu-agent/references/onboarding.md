# Onboarding — from an e-shop to a live feed

For "I'm new here", "set me up", "I need my products on Heureka and I have nothing yet". This chains
the other playbooks into one end-to-end path: **get data in → check it landed → get data out → check
the feed is good.**

Run it as a guided sequence, not an interrogation: one step at a time, each step's result confirmed
in plain words before moving on. Use the live `get_workflow` checklist for each build step.

## The path

### 1. Orient
`whoami` (who, which language, agency account?) → `get_organization` / `list_organizations` (which
organization are we setting up?). If they have several, ask which one. If an organization already has
imports, this isn't a from-scratch setup — check `get_organization_modules` first and pick up from
where they are (see `health-check.md`).

### 2. Get the data in — create the import
Call `get_workflow` (`create_import`) and follow it; the depth is in `imports.md`. The short version:
you need **where the data comes from** (usually a feed URL) and **what format it is** — and detection
does the format work for you (`detect_feed_format`). Everything else you propose as a default.

### 3. Check the data actually landed
This is the step people skip, and it's why exports come out empty later:
- `get_data_source` — did it run? Check `state`, `lastImportedAt`, `itemCount` vs `totalItemCount`.
- `get_data_source_job_logs` — if it failed, the reason is here (unreachable feed, wrong login, parse error).
- `list_items` (small `limit`) — do real products exist now, and do the fields look sane? This also
  shows you the **real field names** for any filtering later (see `fql.md`).

A newly created import may not have run yet. Either wait for its schedule or offer
`trigger_data_source` to run it now — that consumes resources, so ask first.

### 4. Get the data out — create the export
Call `get_workflow` (`create_export`) and follow it; depth in `exports.md`. Two things to settle: the
**source** (`list_data_queries` — with one import there's only one, so don't ask) and the **format**
for the target platform. Destination defaults to Conviu storage; don't raise it.

### 5. Check the feed is good
- `get_data_writer_job` — `state`, `active`, `itemCount`, `lastWrittenAt`.
- `get_data_writer_job_latest_validation` — errors and warnings in the produced feed. See
  `validation.md` (remember: counts only, never invent specific issues).

### 6. Hand it over
Tell them, in their words: the feed exists, roughly how many products are in it, when it refreshes,
and where to find its address in Conviu to paste into the platform. Then offer the obvious next step
— another channel, or checking back after the first scheduled run.

## Scheduling: the one thing that bites beginners

Import and export have **separate schedules** and the export can only write what the import already
brought in. So:

- **Let the import run first**, with a comfortable gap before the export — not the same minute.
  Products once a day early morning, then the export an hour or two later, is a sane default.
- Orders usually want hourly; products rarely need more than daily.
- Remember the cron limits (single minute number, no ranges, no `*/n` steps, hourly at most) — the
  rules are in `imports.md`.

## Keep the first experience easy

- **Propose, don't interrogate.** Derive everything you can and ask only what you genuinely can't —
  in practice that's the feed URL and sometimes the format.
- **One thing at a time.** Import working, confirmed, *then* export. A user who sees products land is
  ready to trust the next step.
- **Say what happens next.** "It'll refresh every morning; nothing else to do" is what turns a setup
  into a finished job.
- **Don't promise what the tools can't do.** Custom formats need mapping in the visual wizard, and
  new export rules can't be created via the MCP at all — see `gotchas.md`.
