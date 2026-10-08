---
name: videogen-education-video
description: >-
  Make lesson, course, or explainer videos for education (teachers, students,
  courses). Prefer script_to_video or slideshow_to_video. Do not use for
  corporate training, ads, news recaps, or film scenes.
---

# Education video

School, course, and lesson explainers (not corporate L&D).

Also follow `references/always.md`.

If a tool fails because of credits or account access, tell the user to open https://app.videogen.io and manage their VideoGen account, then retry.

## When to use

A teacher, student, tutor, or course creator wants a lesson, concept explainer, or lecture-style video.

## Steps

1. Call `get_me` if this chat has not already confirmed a linked account.
2. If they have slides, `open_uploader` then `slideshow_to_video`.
3. Otherwise write a spoken lesson script and call `script_to_video` with `{ width: 16, height: 9 }` unless they asked otherwise. Optional instructor: `ACTOR` entity as `actorEntityId`.
4. Keep language at the level they named (grade, course, or audience). Do not invent facts, dates, or citations; ask or omit.
5. Poll until `succeeded`. `remix_project` with `CAPTIONS` and `TRANSITIONS`. `export_project` and share `downloadUrl`.

## Output

A lesson MP4 and `projectId`. Do not invent ids.

## Do not

- Treat workplace onboarding as education (use videogen-training-video).
- Pad a short concept into a many-scene storyboard.
