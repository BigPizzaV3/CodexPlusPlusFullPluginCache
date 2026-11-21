# Plan design rules

Read this when choosing the exercises and building the days of a new plan.

## Difficulty matches the trainee

- Use the trainee's level, not the requester's when a coach plans for a client.
- Search with a difficulty range on search_exercise or browse_muscle_pool: beginner 1 to 4, intermediate 3 to 8, advanced 5 to 10. Shift the range down for someone returning after a long break, deconditioned, or older, unless the user says otherwise.
- When the range leaves too few exercises for a muscle group, use fewer exercises rather than ones outside the range, and tell the user.

## Exclusions are hard limits

- Leave out every exercise the user asked to leave out, and every variant of a movement they ruled out as a whole. When unsure whether an exercise is one they meant, leave it out.
- Leave out exercises that need equipment the trainee does not have. Use list_libraries and its library filter when the user trains in a setting a library describes.
- An exclusion that empties a day is shown to the user with a proposal (another focus for that day, or fewer days), never silently ignored.

## Building the days

- Cover every muscle group the outline gives each day, using browse_muscle_pool or search_exercise with the muscle group filter.
- For a strength or muscle goal with an intermediate or advanced trainee, build each day on multi-joint movements first and add isolation work after. A beginner keeps the more accessible movements.
- Do not repeat the same exercise on two days of the same week unless the user asks for it.
- Prescribe sets, reps or a duration, and rest that fit the goal and the level, grounded in what search_knowledge returned. A timed exercise gets a duration in seconds and no reps.
- Use a technique only when the design calls for it: call list_techniques and give the techniqueId of the technique whose description matches. Never write a technique as free text.

## More than one week

- Design one week, then repeat it for the requested number of weeks (1 to 12) with a gradual progression, and make the last week of a longer block a lighter deload week. Mark each week's emphasis with the day's intensity field (Volume, Intensity, Strength, or Deload).
- Keep the same exercises in every week; progress the sets, reps, or durations.

## The rationale

create_plan stores a rationale with the plan so it can be explained later. Fill it from the conversation only: source "create", the goal in the user's words, the experience level, whether the plan is for the user ("self") or a client ("client"), days per week, missing equipment, the exercises the user asked to leave out, one split line per day, short methodology notes, and the user's language code. Leave a field empty when the user did not give it, and leave empty every field not listed here.
