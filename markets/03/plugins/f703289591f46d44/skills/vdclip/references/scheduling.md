# Bulk scheduling

`schedule_clips_bulk` distributes many clips across many accounts over time. Use
`publish_clip` for a single clip.

## Parameters

| Field | Required | Limits |
| --- | --- | --- |
| `clip_ids` | yes | 1–50 clips, from `list_clips` |
| `accounts` | yes | 1–10 accounts, verbatim from `list_social_accounts` |
| `frequency` | yes | `2h` `4h` `12h` `1d` `2d` `1w` — spacing between consecutive posts |
| `start_datetime` | yes | First post, ISO 8601 UTC |
| `timezone` | no | IANA name (e.g. `America/Sao_Paulo`). Omit = UTC |
| `clip_overrides` | no | Per-clip `title`/`description`, keyed by `clip_id` |

Note the tighter account cap here: `publish_clip` allows 20 accounts, this allows 10.

## Distribution behavior

The backend spreads posts inside an **08:00–22:00 local window**, where "local" is set by
`timezone`. Posts that would land outside the window roll to the next available slot, so
the real schedule can extend past a naive `frequency × count` estimate. Always show
`schedule_preview` rather than predicting times yourself.

The backend also enforces the plan's daily and monthly post limits. Check them with
`list_calendar` before promising a schedule.

## Output

| Field | Meaning |
| --- | --- |
| `total_requested` | clip × account posts requested |
| `total_created` | posts actually created |
| `post_ids` | internal scheduled-post ids — needed for `reschedule_post` / `cancel_post` |
| `schedule_preview` | resolved times: `clip_id`, `clip_title`, `scheduled_at`, `platform`, `account_name` |
| `skipped_clips` | clips dropped, each with a `reason` (e.g. `not_rendered`, `daily_limit_exceeded`) |
| `warnings` | non-fatal notices; surface them |

When `total_created` is lower than `total_requested`, say so and name the skipped clips
and why. A partial schedule reported as complete is a failure.

## Timezone care

`start_datetime` is UTC. `timezone` only controls the daily posting window. Someone in
São Paulo asking for "9am" needs `start_datetime` at `12:00Z` **and**
`timezone: "America/Sao_Paulo"` — setting one without the other silently shifts posts.
