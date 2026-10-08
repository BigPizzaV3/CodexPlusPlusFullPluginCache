---
name: create-tracker
description: "Create or update a project-specific electrical construction progress tracker from unflattened Bluebeam Count markups. Use when the user asks for an Electrical Progress Tracker, wants marked power, lighting, fire alarm, PA, masterclock, or other electrical drawings converted into an interactive tracker, or needs revised drawings reconciled without losing saved progress, timestamp history, project notes, reports, or manager access."
---

# Electrical Construction Progress Tracker

Create a Site from this template. Keep the source directory unchanged.

## Required inputs

- A project name.
- At least one original PDF containing unflattened Bluebeam Count markups.
- The system and floor represented by each drawing, when the filename or drawing title does not establish them clearly.
- Each device markup's exact Subject must identify its category.

Ask for missing information when it affects device identity, floor, system, or project separation. Never infer ambiguous device categories or locations.

## Workflow

1. Read `artifact-template.json` and resolve its paths relative to this skill directory.
2. Identify the prompt-advertised preinstalled Sites capability and load its sites-building and sites-hosting skills. If unavailable, say so and stop; do not recreate or install it. Copy the sanitized retained application from `<skill-dir>/assets/source`, including hidden files, into a fresh empty project directory. Leave the retained source unchanged and preserve its package configuration, migrations, and logical D1/R2 bindings.
3. Extract annotation Subject values and coordinates from every supplied PDF. Exclude drawing comments, text boxes, and other annotations that are not intentionally counted devices. Render a clean drawing background without the colored markup appearances while preserving the extracted coordinates.
4. Use the copied application as the starting project in the Sites workflow. Replace its sample drawing and device record with the validated project data. Organize available views by system and floor; do not create empty views for drawings the user did not supply.
5. Verify that each marker aligns with its source annotation, every count matches the Bluebeam Subject totals, IDs are unique, and the public view cannot change progress.
   Confirm manager mode supports timestamped individual and bulk status updates, per-device and full-history clearing, coworker manager access by exact ChatGPT account email, and finalized progress reports for Today, This week, and Since last report. Confirm the Notes tab records timestamps. Confirm the public route can read notes and finalized reports but cannot generate or alter them.
6. For a new project, create a separate Site identity and database. Never connect a new tracker to an existing project's database.
7. For a revision to an existing tracker, reconcile by system, floor, category, and position. Preserve existing device IDs, saved statuses, status history, and project notes wherever the source device still matches. Report additions, removals, reclassifications, and ambiguous matches before publishing.
8. Build and validate the Site through the Sites workflow. Unless the user asks to keep it local, follow sites-hosting to save, deploy, and verify the result.

## Fidelity

Preserve the source application's pages, components, styles, assets, package configuration, migrations, and logical D1/R2 bindings.

User instructions control requested content and explicit deviations. The retained reference controls layout and formatting where the user has not requested a change.

## Safety and privacy

- Never include drawings, coordinates, counts, progress records, credentials, or database contents from another project.
- Never expose manager editing without authentication.
- Keep the default public route read-only.
- Keep status history append-only. Do not rewrite prior timestamps when current status changes.
- Clearing history must preserve current device statuses. Require confirmation before clearing, and allow both one-device and all-device clearing.
- Only the project owner may add or remove manager emails. Authorized managers may update statuses, use bulk controls, manage notes, and clear history.
- Keep project notes isolated to the current project's database.
- Keep finalized reports immutable and isolated to the current project's database. Count each device once using its final status in the selected period and include notes from the same period.
- Do not publish or change Site access when the user asks for a private preview or local-only work.
