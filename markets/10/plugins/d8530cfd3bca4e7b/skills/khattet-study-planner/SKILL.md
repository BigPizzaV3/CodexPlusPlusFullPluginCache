---
name: khattet-study-planner
description: Use Khattet to explore supported university catalogs, find course sections, build a conflict-free candidate schedule, calculate GPA, or prepare a schedule wallpaper layout.
---

# Khattet study planner

Use the Khattet tools when the user asks about supported university catalogs, courses, sections, schedule options, GPA calculations, or a schedule wallpaper layout. Reply in the user's language; use English by default.

## Catalog and schedules

- If the university or catalog context is unclear, call `list_universities` and ask the user to choose from the returned universities. Never invent university, campus, major, term, or section identifiers.
- Use `resolve_catalog_context` with the chosen university slug and any known values. If it reports an incomplete context or candidates, ask for the missing choice instead of guessing.
- Use `search_courses` for course-name or course-code searches. Apply returned university, term, campus, and student-group values only when the user has provided or selected them.
- Use `get_course_sections` to show sections for a named course. Summarize returned meeting times, instructors, availability, and campus in the user's language.
- Use `build_schedule_from_catalog` only with section IDs returned by Khattet. Use `build_schedule` only when the user supplies section details. Explain any skipped courses and schedule conflicts using the tool's result.
- These tools produce a proposed schedule only. They do not register, add, or save courses to a university or Khattet account.

## GPA and wallpaper layouts

- Use `calculate_gpa` only with grades and credit hours the user supplies. Ask which 4.0 or 5.0 scale to use when unclear. Do not infer grades or prior GPA data.
- Use `generate_wallpaper` with the schedule entries supplied by the user. It returns a layout description and geometry, not a rendered PNG; never claim an image was generated.

## Account and access boundaries

- A Khattet account and active subscription are required. Let the user complete Khattet's OAuth sign-in and consent flow; never request their password or copy credentials into the conversation.
- The tools can read Khattet's supported course catalog and calculate or preview results. They cannot access a university registrar account, retrieve unprovided grades, register or drop courses, make payments, delete data, or change saved schedules.
- Do not expose raw JSON when a concise explanation or table would answer the request.
