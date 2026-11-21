# Training day exercise fields

Each item in `exercises` (create or update) describes one planned exercise. Only `exercise_id`, `sets` and `reps` are needed; everything else is optional and a plan that uses none of it works as a plain list of sets and reps.

| Field | Meaning | Format |
|---|---|---|
| `exercise_id` | The library id. Never a name. | from `search_exercises` |
| `sets` | Number of working sets | whole number, 1 to 100 |
| `reps` | Reps per set | a number (`10`) or a range (`"8-12"`) |
| `track_weight` | Ask for weight (kg) when logging | true by default |
| `track_time` | Ask for time (seconds) when logging | false by default; use for holds such as planks, together with `track_weight: false` |
| `notes` | The trainer's cue for the exercise | short text |
| `warmup_sets` | Warm-up sets before the working sets | number or range (`"1-2"`) |
| `warmup_reps` | Reps per warm-up set | number or range (`"10-12"`) |
| `target_rir` | Reps in reserve to aim for | number or range (`"2-3"`) |
| `rest_seconds` | Rest between sets, in seconds | number or range (`"120-180"`) |
| `tempo` | Four phases, for example `3-1-1-0` (`X` means explosive) | four values joined by `-` |
| `group_id` | Marks a superset or circuit | the same string on consecutive exercises |

## Supersets and circuits

Give two or more consecutive exercises the same `group_id` (any string works, for example `A`). They are performed back to back. Put the rest on the last exercise of the group; rest on earlier members is not used. Three or more exercises in a group are shown as a circuit.

## Reading a trainer's shorthand

- "4x8-10" means `sets` 4 and `reps` "8-10".
- "2 min rest" is `rest_seconds` 120; "90s" is 90.
- "RIR 2" is `target_rir` 2; "RPE 8" is not the same thing, so ask before converting.
- "3-1-1-0" style numbers are `tempo`.
- Keep the trainer's wording of cues in `notes`.

## Weekly schedule assignments

`set_weekly_schedule` takes assignments of `trainingDayId` and `dayOfWeek`. `dayOfWeek` is 0 for Sunday, 1 for Monday up to 6 for Saturday. The same training day can be assigned to several days, and a day can hold more than one training day.
