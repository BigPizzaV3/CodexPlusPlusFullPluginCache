---
name: write-a-course-review
description: Resolves a golf course and saves the user's rating and review text, handling course-name disambiguation and the sign-in requirement. Use when the user wants to write, save, leave, or update a review for a golf course.
---

# Write a course review

## Steps

1. Resolve the course: prefer `course_id`. If only `course_name` is given, call `write_course_review` with it directly.
2. If the response is `status=similar`, show the `courses` candidate list and ask the user to pick one, then retry with the chosen `course_id`.
3. If the response is `status=sign_in_required`, tell the user to sign in at https://auth.teemeup.ai, then retry the same call once they confirm sign-in.
4. On success, confirm the saved rating and course. If `action` indicates an update, tell the user their existing review was updated rather than duplicated — `write_course_review` upserts one review per user per course.

## Boundaries

- Never invent a rating or review text the user didn't provide.
- Identity for the save comes from the signed-in session, not from a tool argument.
