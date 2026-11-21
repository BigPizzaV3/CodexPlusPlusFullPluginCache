---
name: get-started
description: Build a workout program with WLog and give the user a link that opens it in the WLog app.
---

# Build a WLog program

1. Ask only what is missing: training days per week, goal (strength, muscle, general fitness), experience level and available equipment.
2. Call `search_exercises` for every movement you plan to use. Use only ids it returns. Prefer the first, most basic result for common lifts, and use the `equipment` filter when the user has limited equipment.
3. Keep each workout to 4–8 exercises unless the user asks for more. Use rep targets such as `"8-12"` or `"5"`.
4. Call `create_routine` once with all workouts. Write the program and workout names in the user's language and pass the matching `locale`.
5. Show the returned link and a short summary of each workout. Tell the user to open the link on their phone to start the program in WLog.

If `create_routine` reports unknown exercise ids, search for those movements again and retry with the returned ids.
