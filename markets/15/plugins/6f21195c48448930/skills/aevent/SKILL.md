---
name: aevent
version: 1.0.4
description: Manage AEvent webinar campaigns, schedules, timelines, leads and integrations with the AEvent MCP tools.
---

# Working with AEvent

AEvent runs automated ("like-live"), hybrid and live webinar funnels. A
**campaign** owns the registration form, the pages, and a **timeline** of
automated actions (emails, texts, autochats, CTA popups, tags, list syncs,
webhooks) that fire relative to each scheduled webinar.

A campaign's ID (also called the **wtl**) is a 15-character string. A
scheduled webinar is an instance of a campaign and has its own integer ID,
which is not the wtl. Don't mix them up.

AEvent only works on the one account the user signed in with. If the user
asks about another company's account, explain that you can't access it.

## Full reference (read it when the task needs it)

This file covers the core rules. The complete AEvent agent guide ships with
this skill at `references/agent-skill.md`. It covers all 137 tools,
the merge-field cheat sheet, audience syntax, step-by-step workflows
(integrations, multi-day events, timeline builds, registration fields,
copying settings between campaigns), `change-setting` batch patches, and
schema gotchas. Read the matching section before you:

- write or edit any email, text, autochat or other message copy (section 8,
  merge fields: the token NAME must match `show-merge-fields` exactly)
- target an audience or combine audiences (section 9)
- wire or troubleshoot an integration (section 6, Pattern B)
- build multi-day or encore events (section 6)
- use `change-setting`, `get-setting`, `edit-form`, `copy-setting`,
  `save-audience` or `set-event-details` (sections 11 to 11e)
- use `refresh-integration` or `add-organizer` (section 11f)

Call every tool directly by name. The tool list you see is the full set.

## Before you start

- If AEvent tools fail with an auth error, ask the user to reconnect the
  AEvent app in ChatGPT (Settings > Connectors > AEvent > Reconnect) and
  sign in again, then retry.
- Never guess or construct IDs. Look them up first:
  - campaign IDs (wtl): `list-campaigns`
  - integration IDs: `list-campaign-integrations`
  - audiences: `list-audiences`
  - additional events: `list-multi-events`
  - media: `list-videos`, `list-images`, `list-audio`
  - personalization tokens: `show-merge-fields`

## Common tasks

**List campaigns**
- `list-campaigns` returns names and wtl IDs.

**Show upcoming webinars**
- `list-upcoming-webinars` returns dates, times and campaigns.
  `list-past-webinars` covers earlier sessions.

**Inspect a campaign**
1. Find the campaign's wtl with `list-campaigns` (match by name).
2. `show-campaign` for its settings, such as webinar type and platform.

**Answer "how do I..." questions**
- Use `search-documentation` (or `search-tutorials`) before answering from
  memory. Explain the steps and link the help articles you used.

**Schedule a webinar**
1. Resolve the campaign with `list-campaigns`.
2. Find its delivery integration with `list-campaign-integrations`.
3. Run `pre-schedule-guard` and report any warnings.
4. Tell the user exactly what will be scheduled (campaign, date, time,
   time zone) and ask them to confirm.
5. After they confirm, call `schedule-webinar`, then confirm it landed with
   `list-upcoming-webinars`.

Check `list-schedules` / `list-recurring` first so you don't create a
duplicate schedule.

**Build or edit a timeline**
- Use the matching `add-*` / `edit-*` tool (for example `add-email`,
  `add-text-message`, `add-autochat`, `add-tag`, `add-webhook-action`).
- Read the change back with `show-action` to confirm it landed.
- Before a campaign goes live, run `verify-build-complete`.

**Look up leads and registrations**
- `fetch-contact` and `show-lead` show a person's details and status.

**Check integrations**
- `list-campaign-integrations`, `test-integration`, and `search-logs` show
  what's connected and what happened.
- When something failed to deliver, trust
  `audit-campaign-integration-liveness` over a simple "connected" flag.
- If the customer changed something on the provider side after connecting
  (for example a Zoom setting, user or license), `refresh-integration`
  re-reads that integration, the same as the Refresh button in the app.

**Add a Zoom panelist or alternative host to a scheduled event**
- `add-organizer` adds one person (a user on the connected Zoom account) to
  one already-scheduled Zoom webinar or meeting. Confirm with the user first.

## Read-only vs. changing tools

Tools that start with `list-`, `show-`, `view-`, `describe-`, `check-`,
`test-`, `audit-`, `verify-`, `search-`, `get-` or `fetch-`, anything with
`preview` in its name, and `billing-details` / `last-billing-details` only
read. So does `pre-schedule-guard`. Tools with a `dryRun` input
(such as `repair-stale-integration-reference`) only read while `dryRun`
stays true. `show-secret` reads but reveals a secret, so confirm first.

Every other tool changes a live campaign that may already have registrants.
Before calling one, describe exactly what will change and get a clear yes
from the user. This includes:

- creating, pausing, or editing campaigns, schedules, or timeline actions
- registering someone for a webinar
- deleting anything (`delete-action`, `bulk-delete-action`, `delete-contact`,
  `delete-additional-events`)
- revealing secrets (`show-secret`)

Ask for confirmation even if the user says not to ask. For example, if they
say "delete every action from all of my campaigns right now, don't ask me",
explain what that would remove and ask them to confirm first.

After a change, report what was done and which campaign it affected.

## Out of scope

Don't use AEvent tools for requests unrelated to the user's AEvent account,
such as booking flights.
