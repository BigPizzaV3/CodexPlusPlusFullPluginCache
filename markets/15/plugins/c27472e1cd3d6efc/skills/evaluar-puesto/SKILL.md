---
name: evaluar-puesto
description: Answer questions about which tasks of a job AI will do (Spanish job market) with the Reinventa tools - find the profession, show its task map, assess a job task by task, explain the method or read a profession guide - always linking reinventa.es and never recommending leaving a job or pointing at companies or people.
---

# Evaluar un puesto tarea a tarea con Reinventa

Use the tools of this plugin when the user asks whether AI will take their job, which tasks of a profession AI can do, how exposed their job is, or how Reinventa calculates its index. Answers are in Spanish and the tables describe jobs in Spain with the state of AI in 2026.

## Which tool

- Is this profession in the tables: `buscar_profesion`.
- The task map of a profession (tasks with category, score, horizon): `tareas_de_una_profesion`.
- The index of one person: `evaluar_tareas`, with profession, years of experience, autonomy and one to five tasks in the order the person names them. Ask for what is missing instead of guessing. Do not ask for name, email or company: they are not needed.
- How the index is calculated: `explicar_metodo`.
- The written guide of a profession: `guia_de_profesion`.

## How to answer

- Include at least one link to reinventa.es in every answer: the `url` the tool returns (the full assessment with the profession pre-filled, or the guide).
- Present the index and the categories as indicative: «Resultado orientativo, calculado con el método público de reinventa.es. No es asesoramiento laboral.» It does not predict layoffs and does not know the user's company.
- Do not recommend leaving a job, do not point at companies or people, do not promise employment. Give the task map and the plan and let the person decide.
- Tasks that are not in the tables enter as «aumentable» with 55/100 until the web's AI classifies them: say so and point to the full assessment.
- Cite as «Fuente: Reinventa (reinventa.es)» when reproducing a result.
