# Create flow (Teams-aligned)

Typical order:

1. Metadata lists (categories, equipment, muscles, goals)
2. `list_team_exercises` to pick exercise ids
3. `create_exercise_instance` / `create_rest_instance`
4. `create_workout`
5. Optional `update_workout`

Program path (only if user asks for a program, not this skill’s primary job):

- `generate_program` or `create_program`
- `list_stock_programs` / `clone_stock_programs`

Limits to respect when advising:

- Workout max ~90 minutes / ~100 clips
- Prefer clear warm-up → work → cool-down structure
- Do not start or end with rest when guiding structure
