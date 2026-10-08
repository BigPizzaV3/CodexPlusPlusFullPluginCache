# VDClip: publish & schedule

Publish a rendered clip to connected social accounts, or distribute many clips over time.
Every action here is **user-visible on external platforms** — confirm before acting.

## Non-negotiable rules

- Publish or schedule only after explicit user approval of destination, copy, and time.
- Account fields are copied verbatim from `list_social_accounts`. Never construct or guess
  `account_id`, `connection_id`, `platform`, `user_name`, or `user_handle`.
- Only render-complete clips can be published. Check `rendering_status` from `list_clips`
  or `get_clip` first — see [rendering.md](rendering.md).
- `cancel_post` is destructive and irreversible — a cancelled post cannot be un-cancelled,
  only re-scheduled from scratch. Confirm the exact posts before calling.
- Never retry a publish after a timeout or uncertain result. Read `list_calendar` first to
  see whether it landed; a blind retry double-posts.
- Never imply platform success before a terminal status comes back.

## Workflow

### 1. List destinations

`list_social_accounts` returns each connected account with `account_id`, `platform`,
`connection_id`, `user_name`, `user_handle` and `needs_reauth`.

Pass those objects through unchanged into `accounts`. `needs_reauth: true` means the token
expired — that account cannot publish until the user reconnects it, so exclude it and say
so rather than letting the call fail.

### 2. Confirm with the user

Show destination(s), the title, the description, and the time. Get an explicit yes.

### 3a. Publish or schedule one clip

```
publish_clip({ clip_id, title, description?, accounts, is_scheduled?, scheduled_date? })
```

- `accounts`: 1–20 entries from `list_social_accounts`.
- `title`: 1–500 chars. `description`: up to 5000.
- Immediate: omit `is_scheduled` or set it `false`.
- Scheduled: `is_scheduled: true` **and** `scheduled_date` (ISO 8601).

### 3b. Schedule many clips

Use this only for multiple clips — see [scheduling.md](scheduling.md) for the
distribution rules and limits.

```
schedule_clips_bulk({ clip_ids, accounts, frequency, start_datetime, timezone?, clip_overrides? })
```

Returns `total_created`, `total_requested`, `post_ids`, `schedule_preview` and
`skipped_clips` (each with a `reason`, e.g. `not_rendered`). **Report skipped clips** — do
not present a partial schedule as complete.

### 4. Manage the calendar

- `list_calendar({ start_date?, end_date?, cursor?, limit? })` — scheduled/published posts in
  a `YYYY-MM-DD` range, plus the plan's posting quota under `stats`: `day_used`/`day_limit`
  and `month_used`/`month_limit`. Remaining is `limit - used`; check it before promising a
  schedule.
- `reschedule_post({ post_id, title?, description?, ... })` — partial PATCH; omitted fields
  keep their current value. `post_id` comes from `list_calendar`.
- `cancel_post({ post_ids })` — 1–100 ids. Destructive; confirm first. Pass a
  single-element array to cancel one.

## Public link sharing

For a read-only link instead of a social post:

- `get_project_share({ project_id })` — current `external_id` and visibility.
- `set_project_share({ project_id, visibility })` — `public` exposes the finished clips,
  `private` restricts them. Defaults to `public` when omitted.

## Failure handling

| Situation | Action |
| --- | --- |
| Plan forbids scheduling | Stop; explain the plan gate. Do not retry |
| Daily/monthly quota hit | Show `day_used`/`day_limit`; offer a later date |
| Clip not rendered | Render it first ([rendering.md](rendering.md)), then publish |
| Account disconnected | Ask the user to reconnect; do not substitute another account |
| Timeout / unknown result | `list_calendar` to check, then decide. Never blind-retry |

## Response style

Lead with what was posted or scheduled, where, and when. Give post or schedule ids. Name
skipped clips and quota limits explicitly. Offer at most three next actions.
