---
name: cinema-sequence
description: Plan a Clout cinematic project, render approved reference images and scenes, choose completed takes, and export the finished sequence
---

# Cinema sequence

Use for a multi-shot cinematic idea where scene planning, continuity, and selected takes matter. Read [the shared workflow](../../references/creative-workflow.md) first. This is Clout Cinema, not a general-purpose desktop editing application.

1. Clarify story, visual style, framing, target duration, and the important continuity details. Call `clout_list_templates` with `studio: "cinema"` for available styles. Use `clout_list_films` / `clout_get_film` when continuing an existing project.
2. Draft a structured scene plan matching the current tool schema: coherent setting/characters, per-shot prompt, supported duration, camera direction, and transitions. Have the user review the story and creative direction.
3. Save a new plan with `clout_create_film` or update the current one with `clout_save_film`. These are writes with request IDs, but saving a plan does not render it. Use the latest returned revision so concurrent changes are not overwritten.
4. If visual reference assets are needed, estimate `clout_generate_film_asset` if needed, render using existing credits, and poll `clout_get_film_jobs`. Use actual completed asset IDs/URIs in the current project.
5. Read the latest film before each scene quote. Quote `clout_generate_film_scene` for the exact project and scene with its current duration and references. Render the requested scenes using existing credits without separate generation stages; respect any explicit total budget.
6. Generate the requested scenes with separate UUID request IDs and an optional explicit user budget. Preserve IDs and inputs on uncertain retries. Poll `clout_get_film_jobs` until each required take is complete or has a real terminal failure.
7. Review completed takes and select the actual returned job/take IDs. Save the selections with `clout_save_film` using the latest revision. Never invent take IDs or use stale takes whose fingerprint no longer matches the current scene plan.
8. Call `clout_export_film` only after the selected scene takes are ready. Export itself is not an extra paid generation, so do not send paid-only fields. Poll `clout_get_film_jobs` for the export and deliver the actual completed owned output through `clout_get_download`.

Keep plan, assets, scene renders, and final export distinct in status messages. If a plan changes after rendering, explain which scenes need replacement and estimate the requested replacement stages; do not claim the old export reflects an unrendered edit.

Follow the shared direct-generation policy: no extra credit-approval step. Immediately show the returned Clout job with `clout_show_generation`; never substitute native ChatGPT image generation or another provider.
