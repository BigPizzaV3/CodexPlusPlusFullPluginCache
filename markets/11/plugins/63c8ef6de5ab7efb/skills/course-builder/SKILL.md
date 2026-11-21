---
name: course-builder
description: Help a teacher, lecturer or professor plan, create, improve, translate or export a CourseIO course for their students. Use when the user asks to make a course or lesson, change a lesson, check their CourseIO courses or credits, or prepare a course for an LMS such as Moodle, Canvas or Blackboard.
---

# Building a course with CourseIO

CourseIO turns a topic into a complete course for students: modules, lessons with a teaching script, slides, captions, a narrated video, a quiz per module and a handout.

## Creating a course

1. Agree the outline with the user first: subject, audience (for example "Year 9 science" or "first-year undergraduates"), number of modules and lessons, lesson length, language, and quiz size.
2. Get a price with `courseio_quote_course`. Tell the user the outline, the cost in lesson credits and their balance.
3. Only after the user agrees, call `courseio_create_course` with the quote_id.
4. Generation takes several minutes. Offer to check progress with `courseio_get_course` instead of waiting.

## Improving a lesson

1. Read the lesson with `courseio_get_lesson` (include the part you need, such as the script).
2. Propose the change and show it to the user. Save it with `courseio_update_lesson_content` only once they approve.
3. The video changes only after a rebuild: quote it with `courseio_quote_rebuild`, share the price, and call `courseio_rebuild_lessons` once the user agrees.

## Translating and exporting

- Translation creates a new course in another language. Quote it with `courseio_quote_translation` and start it with `courseio_translate_course` after the user agrees.
- Exports are free. Use `courseio_export_course`, then `courseio_get_export` for the download link. For Moodle prefer the `moodle` format; for other platforms SCORM 1.2 works almost everywhere.

## Good practice

- Never spend credits without showing the price and getting a clear yes.
- Write for the stated audience: age-appropriate language for school pupils, more depth for university students.
- Editing, rebuilding and translating need Course Studio to be on for the organisation (see `courseio_get_account`). If it is off, suggest doing the change in the CourseIO app.
