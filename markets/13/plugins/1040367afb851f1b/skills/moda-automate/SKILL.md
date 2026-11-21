---
name: moda-automate
description: >-
  Recurring Moda work — scheduled posts, weekly reports, sync jobs: connect
  Moda to the scheduler you already run; nothing here runs on a timer, and the
  artifact itself routes to its format skill. Use for: "every week/day…",
  "auto-post X", "keep this updated".
---

# moda-automate

**PREREQUISITE — `load_skill("moda-core")` once per session** (step-0, write
contract, free/metered map). Already loaded? Skip ahead. If you cannot load
it, the non-negotiables: call `moda_bootstrap` before anything; `brand_list`
before creating; revision-guarded writes use `expected_revision` from your last read.
`canvas_edit_image` captures its own target state and has no revision argument.
On `stale_revision`, re-read and retry once; send the canvas link
the moment it exists; stuck or failed? `ask_expert("<question>")` — free and
fast, never guess.

## What this surface can and cannot do

- Moda hosts no scheduler, and this conversation is stateless: nothing here
  keeps running after it ends. **Never say you have scheduled something** — no
  tool on this surface installs a job, and a promised run that never happens is
  the worst failure this skill can produce.
- What CAN happen here: build the artifact once, prove it, and hand over the
  exact repeatable recipe plus the two real ways to run it on a cadence.
- **Moda produces; the scheduler delivers.** Nothing in Moda posts to a social
  platform or sends mail. Each run leaves a canvas link and an export — the
  publishing step belongs to whatever is running the schedule.
- **The artifact still routes to its format skill.** This skill owns the
  cadence conversation; the social, document, chart and video skills own what
  each run actually builds.

## The useful half, in order

1. Build it ONCE, now, with its format skill. A proven run beats a scheduled
   guess, and the user gets something today either way.
2. Hand over the recipe as concrete steps with the real ids in them — the
   canvas, the brand kit, the folder, the template — not a description of a
   workflow.
3. Name the two lanes honestly, and let the user pick:
   - a machine that runs Moda's command-line tool on a timer (cron, a task
     scheduler, a repository's scheduled job), which is the lane with a
     filesystem and unattended credentials;
   - the automation platform the user already runs, calling Moda's API on a
     schedule.
4. State what each run will cost: canvas authoring, reads, screenshots and
   exports are free; only generation lanes meter, and they quote for free
   first.

## Three shapes cover almost everything

| Shape | Each run | Why it wins |
|---|---|---|
| Refresh one canvas (the weekly report) | `canvas_read` the pinned canvas → `canvas_edit` → `export` | the link never changes, so anyone watching it just sees the update |
| New artifact per run (the weekly post set) | `canvas_create(template_canvas_id=…)` → author → `export` | the team template keeps every week on the approved layout |
| Sync job | pull the source data → author → `export` | Moda never reaches into your systems; the fetch belongs to the caller |

Whichever shape it is, load the format skill for the authoring half — this
skill does not teach how to build the artifact.

## Discipline the recurring run has to carry

- One canvas, serial writes: they serialize on the server anyway, so a parallel
  batch buys nothing and can come back `canvas_busy`.
- Every write carries `expected_revision` from the last read; `stale_revision`
  heals on a re-read and one retry.
- An identical repeated generation REPLAYS its result rather than charging
  twice — a retry with the same inputs is safe, a reworded prompt is a new
  charge. Never "retry" by nudging the wording.
- Every run should leave a trace: what it built, the canvas link, and the
  failure if there was one. An unattended run that reports nothing is
  indistinguishable from one that never ran.

## Examples

- "post our metrics chart to Slack every Monday" → build the chart now (the
  chart skill), hand over the weekly recipe, and say plainly that the Slack
  step is the scheduler's, not Moda's.
- "keep the launch one-pager up to date" → refresh-one-canvas shape; the
  document skill owns the page, and the live link is what stays current.
- "a fresh set of posts every week" → new-artifact shape off a team template
  (`load_skill("moda-templates")`); the platform's social skill owns the
  creative.

## Errors

Any typed error → `load_skill("moda-core")` and read its recovery reference.
`ask_expert` is free when a cadence question is really a capability question.

See also: moda-core — the contract, recovery, everything Moda can do.
