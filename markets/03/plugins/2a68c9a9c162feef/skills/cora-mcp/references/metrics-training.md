# Activity, training, and measurement tool map

Choose tools by whether the user needs an exact day, an aggregate, a series,
advice, completed history, or a future plan.

## Activity summaries, training guidance, and app help

| Tool | Choose it for | Avoid or verify |
|---|---|---|
| `cora_get_stats` | Min/mean/max-style summaries for up to ten metric slugs. | Not a raw series or exact-day score table. |
| `cora_get_recovery` | Quick readiness summary over a window. | Use daily scores for a named day. |
| `cora_get_sleep` | Overnight duration and score summary over a window. | Use daily scores for a named night/day. |
| `cora_get_metric_timeseries` | Ascending per-day values for one metric; graphs, changes, correlations, and trends. | Call once per metric when comparing metrics; do not invent missing days. |
| `cora_get_daily_scores` | Exact-date rows combining overnight, readiness, and activity scores. | A row for day D represents the overnight period ending that morning. |
| `cora_get_app_help` | App navigation, score definitions, feature behavior, and troubleshooting. | Product knowledge, not a personal-record lookup or guidance request. |
| `cora_ask_coach` | Personalized fitness guidance using Cora context. | Slow paid AI; not a generic data fetch and not proof of a write. |

Use only returned values. Do not infer a score from another metric. If data
available only from a connected device is unavailable, state that limitation rather
than treating an empty result as zero.

## Training and measurements

| Tool | Choose it for | Resolve, confirm, or verify |
|---|---|---|
| `cora_get_training_plan` | Current plan and upcoming workout IDs. | Read before any scheduled-workout mutation. |
| `cora_get_workouts` | Completed workout history. | Do not use for upcoming training. |
| `cora_get_workout_details` | Exercises and sets for one planned workout. | Resolve `workout_id` from the current plan. |
| `cora_get_saved_workouts` | Saved workout templates and template IDs. | IDs go to `cora_add_workout_from_template`, not plan management. |
| `cora_get_cardio_goals` | Weekly cardio and zone-minute goals. | Read-only. |
| `cora_get_weight_history` | Scale readings logged in Cora. | May exclude readings available only from a connected device. |
| `cora_log_weight` | A new scale reading in kg or lb. | Not exercise/lift load; re-read reading history. |
| `cora_log_body_measurement` | New circumference measurements. | Use the user's preferred length unit. |
| `cora_log_workout` | An already-completed strength, bodyweight, or HIIT workout. | Not future planning and not a generic cardio/yoga import. |
| `cora_manage_training_plan` | Add, move, rename, or remove scheduled workouts. | Resolve exact plan workout ID; explain/confirm data-losing operations and re-read. |
| `cora_generate_training_plan` | Generate and activate a complete personalized plan. | Read first; it replaces and archives the current plan, so confirm replacement unless explicitly requested with that scope. |
| `cora_add_workout_from_template` | Schedule a saved template on a date. | Resolve template ID with saved-workout read, then re-read plan. |
| `cora_save_workout_template` | Save a reusable workout template. | Availability-sensitive: present in source but not every client. Verify returned template identity. |

## Keep training records distinct

- Treat a completed workout, a planned workout, and a saved template as three
  different record types with different IDs.
- Use `cora_log_workout` only when the workout actually happened.
- Use `cora_manage_training_plan` for current-plan workout IDs.
- Use `cora_add_workout_from_template` for saved-template IDs.
- Re-read the plan after add/move/rename/remove/generate actions. Re-read
  workout history after logging a completed workout.

## Stop at unsupported boundaries

Do not claim the external MCP can propose one workout, plan only one week,
fetch muscle status, write to a connected device service, or set a workout-specific
reminder. Use a coarser available training-plan operation only when it truly
satisfies the request; otherwise explain the gap or use app help.
