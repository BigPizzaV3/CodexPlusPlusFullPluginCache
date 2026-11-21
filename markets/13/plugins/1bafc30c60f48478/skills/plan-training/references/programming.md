# Programming a Lifterly session

These are the rules Lifterly's own coach follows. Use them unless the user asks
for something else; the user's explicit instructions always win.

## Workout types and split parts

| workoutType | splitPart values |
| --- | --- |
| `fullBody` | none (`null`) |
| `upperLowerSplit` | `upper`, `lower` |
| `ppl` | `push`, `pull`, `legs` |
| `broSplit` | `chest`, `back`, `shoulders`, `arms`, `legs` |
| `arnoldSplit` | `chest_back`, `shoulders_arms`, `legs` |
| `custom` | none (`null`) |

To find exercises, call `search_exercises` with `workoutType` and `splitPart`.
For a muscle-based search, the muscles are: Abductors, Abs, Adductors, Biceps,
Calves, Chest, Forearms, Glutes, Hamstrings, Lats, Lower Back, Upper Back,
Quads, Shoulders, Traps, Triceps, Obliques.

## Choosing exercises

- Only ids returned by `search_exercises` (or seen in the user's history), each
  exercise once per session.
- Fit the split part, the user's equipment and level (`search_exercises`
  already filters by both and leaves out banned exercises).
- Balance against the user's recent sessions (`list_workouts`): do not repeat
  the same session.
- Respect what the user said about injuries, equipment and preferences in the
  conversation.
- By goal: `strength` → compounds, lower reps, heavier; `muscleGain` → mix of
  compounds and accessories, moderate reps (6–12); `fatLoss` → efficient,
  denser sessions, moderate-to-high reps; `endurance` → stable movements,
  high reps or timed sets; no goal → balanced.
- By level: `BEGINNER` → conservative loads, execution first; `INTERMEDIATE`
  → gradual progression from history; `ADVANCED` → challenging but safe.

## Sets, weights and rest

- 2 to 6 sets per exercise. Sets can differ: ramp up to a top set, back-off
  sets, fewer reps as the weight rises.
- Every set has at least one goal: `reps`, `weightKg` or `durationSeconds`
  (active time only, never rest).
- `weightKg` is in kg, per dumbbell for dumbbell work, omitted for bodyweight
  work. Base it on `get_exercise_progress` (best weight and recent sets): a
  small step up from what the user last managed, never a dangerous jump.
  Without results, choose a conservative weight for the exercise and level.
- Rest in seconds, fitted to the effort: about 120–180 s after heavy compounds,
  60–90 s for accessories, 30–60 s for isolation or density work. Do not use
  one value everywhere.
- Fit the session to the time the user has: count each set's active time
  (about 3–4 s per rep) plus the rests between sets.

## Supersets

- A superset is two or three exercises done one set of each, back to back,
  resting only after each round. Give them the same `superset` label (`"A"`,
  then `"B"` for the next one) and list them one after the other.
- Use them when they fit: antagonist pairs (biceps and triceps, chest and
  back), an accessory after a compound for another muscle, `fatLoss` or a short
  session. Keep heavy compounds for strength work out of them.
- The exercises of a superset take the same number of sets. Put the rest after
  each round on the sets of its last exercise; the rest of the others is not
  used. Count one rest per round when fitting the session to the time.

## Talking to the user

- Speak in their weight unit (`get_training_profile` → `weightUnit`); convert
  from kg (1 kg = 2.2046 lb) and round to sensible plate steps.
- Name exercises, never show ids.
- Say in two or three sentences what you chose and why it fits their goal,
  week or constraints.
