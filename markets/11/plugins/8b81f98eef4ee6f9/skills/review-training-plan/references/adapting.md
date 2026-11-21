# Adapting a plan

Read this when the user asks to change a plan they already have.

## What stays

- Change only what the user asked for, or what the workout history or an exercise the user now wants left out makes necessary. Every other day, exercise, set, rep, rest, and technique stays exactly as the plan stores it.
- Keep the user's original exercise wording (userTerm), the week structure, and the order of the days.

## Replacing an exercise

- Find the replacement with search_exercise or browse_muscle_pool. Prefer one from the same muscle group, within the trainee's level, that is not one the user asked to leave out, and that is not already on that day.
- Never leave a day empty. When no allowed replacement exists, keep the day with fewer exercises only if the user agrees; otherwise keep the original exercise and say why.
- A request to make the plan easier or harder moves the difficulty of the affected exercises down or up and keeps the rest.

## Saving

- The adapted plan is a NEW plan created with create_plan. Name it after the original with an "(adapted)" suffix in the user's language, unless the user gives a name.
- Its rationale starts from the original plan's rationale, with source "adapt" and the change described in the notes.
- Never delete or overwrite the original plan. There is no tool for it, and the user keeps it as history.
