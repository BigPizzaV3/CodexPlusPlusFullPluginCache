---
name: review-progress
description: Review training progress in Outlift - weekly history and completion, training stats over closed weeks (consistency, performance, sets per muscle group), the body-weight trend, and recording the weekly weigh-in. Use this whenever the user asks how their training is going, whether they are progressing, what they did last week or last month, about volume, consistency or missed sessions, or about their weight; also for a trainer checking which trainees trained or went quiet. Apply it even when the user does not say "Outlift" or "stats".
---

# Review progress

Progress questions have an honest answer only when it comes from the logged data. Report what the tools return, say when there is not enough yet, and do not infer health conclusions from the numbers.

## Start

Call `whoami` for the role, `timezone` and `locale`; pass `tz` and `locale` to the tools that take them. Trainees see their own data. A trainer asks about a trainee by passing `trainee_id` (uid from `list_my_trainees`) to the tools below.

## Pick the right view

| The user asks about | Tool |
|---|---|
| This week or a given week: what was trained, done or partial | `get_week_history` (Monday-based week, any date inside it) |
| The last weeks or months: consistency, performance, sets per muscle group | `get_stats` with `weeks` (for example 4 or 12), or `from_week` and `to_week` (Mondays) |
| The individual sets of one finished week | `get_week_sets` with that week's Monday |
| Weight and the trend | `get_body_measurements` |
| (Trainer) who trained this week, who has gone quiet | `get_stats_roster` |
| (Trainer) who has what scheduled | `get_trainer_overview` |

`get_stats` and `get_week_sets` cover closed weeks only, so the current week is not in them; use `get_week_history` for it and say which period the numbers cover. Stats need a plan that includes them. If a tool says the plan does not include stats, tell the user plainly, offer what `get_week_history` shows instead, and stop there.

## Summarize honestly

- Lead with the answer to the question, then two or three numbers that support it: sessions completed versus scheduled, which direction performance moved, which muscle groups got few sets.
- Use the values and labels the tools return. "No comparison yet" or an empty week is a result: say so instead of filling the gap.
- Keep it short. Offer a next step (for example "want the sets from that week?") rather than listing everything.
- Do not give medical advice or judge a weight as good or bad. Describe the direction and size of change and leave interpretation to the user or their trainer.

## Weekly weigh-in

`record_body_weight` saves the weight for a week. There is one entry per week, so recording again for the same week replaces the earlier value. Confirm the number in kilograms before saving, use this week unless the user names another (`week_start` is that week's Monday), and tell them afterwards what was saved and whether it replaced an earlier entry. If the user only asks about their weight, use `get_body_measurements` and do not record anything.

## Errors

Recording needs write access; if the connection is read-only, ask them to reconnect and allow changes. For any other tool error, repeat the message in plain words and say what you can still do.

## Example

User: "How has my training been this month and what is my weight doing?"

1. `whoami`, then `get_stats` with `weeks: 4` and `get_body_measurements`.
2. Reply: "Over the last 4 closed weeks you completed 7 of 12 scheduled sessions, and your leg volume is up while back work stayed flat. Your recent weigh-ins went from 82.0 to 81.1 kg. This week is not in these numbers yet; say the word and I will check it."
