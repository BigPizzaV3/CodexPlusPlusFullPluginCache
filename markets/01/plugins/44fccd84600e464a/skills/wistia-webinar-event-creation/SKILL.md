---
name: wistia-webinar-event-creation
description: Create a Wistia webinar from a brief — gather the title, description, speakers, date/time, and registration goal, then create the event and save shared state for the rest of the workflow. This is STEP 1 of a three-skill webinar workflow (create → registration updates → post-event recap). Use whenever Sam wants to create, set up, schedule, or build a new webinar or live event. After the event is created it offers to set up registration reporting (step 2).
---

# Webinar Event Creation (Step 1 of 3)

Turn a rough idea ("we're doing a webinar on X") into a real Wistia webinar, and capture the details the later skills depend on. Half interview, half API call.

This is the first of three sequential skills:
1. **webinar-event-creation** ← you are here
2. **webinar-registration-updates** — scheduled pre-event pacing reports
3. **wistia-webinar-recap** — performance page after it airs

They coordinate through a shared **`webinar-state.json`** (see *Shared state*).

## What Wistia can and can't store

`create-webinar` (Wistia MCP) accepts: `title`, `description` (basic HTML), `scheduled_for` (ISO 8601 **UTC**, `...Z`), `time_zone` (IANA, e.g. `America/New_York`), `event_duration` (**minutes**, min 15), `folder_id` (optional).

Two things Sam cares about have **no native Wistia field**, so this skill owns them:
- **Speakers** — capture into `webinar-state.json` and fold into the `description` (a "Hosted by…" line). Be honest that Wistia has no speaker field.
- **Registration goal** — not a Wistia concept; store in `webinar-state.json` for steps 2–3.

**Two confirmed quirks:**
- **Timezone label is misleading.** Send `scheduled_for` as a true UTC instant; Wistia echoes it back as the *local wall-clock* time stamped `+00:00`. (Send `2026-08-21T17:00:00Z` for 1pm EDT → it returns `13:00:00+00:00`, i.e. 1pm ET.) When reading any `scheduled_for` later, interpret its clock time in the webinar's `time_zone`, not as UTC.
- **Auto-publishes.** New webinars come back `registration_status: published` — registration opens immediately at the `audience_link`. No separate publish step.

## Collect the brief

Check the conversation first; ask only for the gaps, **in one consolidated message**:
1. Title
2. Description / topic (offer to draft from the topic)
3. Speakers (names + roles)
4. Date & time + duration + time zone
5. Registration goal

For genuinely-unknown optionals (e.g. duration), suggest a default (60 min) rather than blocking.

## Steps

1. **Gather** the brief (one consolidated ask for missing items).
2. **Normalize the date** to a UTC `scheduled_for` + IANA `time_zone`. Double-check the conversion and state the local time back for confirmation — an off-by-timezone webinar is a real failure.
3. **Compose the description**, appending the speaker line.
4. **Create** with `create-webinar`; capture the returned `id` and `audience_link`.
5. **Write `webinar-state.json`** (see schema below) with `stage: "created"`.
6. **Confirm** back: title, local date/time, duration, speakers, goal, `audience_link`. Note registration is already open.

To edit an existing event instead of duplicating, use `update-webinar` (same fields + `id`).

## Shared state

All three skills read/write **`webinar-state.json`** in the user's working folder (the connected Cowork folder). It's the baton that hands the webinar from one skill to the next:

```json
{
  "webinar_hashed_id": "32fei7lgyv",
  "title": "...",
  "scheduled_for_utc": "2026-08-21T17:00:00Z",
  "time_zone": "America/New_York",
  "event_duration_minutes": 45,
  "speakers": [{"name": "Sam Balter", "role": "Host"}],
  "goal": 500,
  "audience_link": "https://home.wistia.com/live/events/32fei7lgyv",
  "stage": "created",
  "reporting_scheduled": false
}
```

`stage` advances through the workflow: `created` → `promoting` → `recapped`.

## Handoff → Step 2

After confirming the event, **offer the next step** rather than ending: ask Sam whether he wants to set up **registration reporting** now (the `webinar-registration-updates` skill). It will schedule recurring pacing updates anchored to the event date.

- If **yes** → invoke `webinar-registration-updates`. It reads `webinar-state.json`, so it already knows the webinar and goal.
- If **not now** → leave `reporting_scheduled: false`; he can start step 2 anytime.

Keep the offer short, e.g.: "Event's live and taking registrations. Want me to set up the registration tracker so you get scheduled pacing updates as it ramps toward Aug 21?"
