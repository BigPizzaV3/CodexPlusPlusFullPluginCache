---
name: search-boluda-courses
description: Search and inspect the public Boluda.com course and lesson catalog when users ask what Boluda teaches, where to learn a topic, what the current course is, which lessons are new, or what a known course or lesson contains.
---

## Route the request

- Use `buscar_cursos` for broad topics, skills, and learning goals.
- Use `buscar_clases` for a specific concept, task, or technique.
- Use `curso_actual`, `ultimas_clases`, or `categorias_cursos` for those exact catalog questions.
- Use `obtener_curso` or `obtener_clase` for a known ID or Boluda.com URL.

## Search well

1. Start with the user's wording.
2. If there are no useful results, try one close synonym or a more specific query.
3. Inspect a result with `obtener_curso` or `obtener_clase` before making detailed claims about it.

## Answer

- Reply in the user's language.
- Distinguish courses from individual classes and include canonical links.
- Ground descriptions in the returned public copy and metadata.
- If no relevant result exists, say so and mention the query used.
- Treat lesson descriptions as public catalog copy, not as the lesson body or transcript.
- Never imply access to videos, paid transcripts, subscriber status, progress, or other user data.
