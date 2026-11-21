---
name: replicating-a-project
description: "Reuse another Donkey Cut project's edit, media or template in this one. Use when the user points at an existing project or share link to copy."
---

# Reusing a project
read_project inspects a source project by id or link, or a share link; list_projects finds the id of a project named by its title. Use its returned ids and document to understand the edit; use watch_video and listen_audio for media you need to judge. Ask for a reference the user can share when access fails.
replicate_project copies the requested edit or items and can map source roles to assets already in this project. Match by content and measured timing. Unmapped media copies from the reference. copy_project_media brings across media for a new arrangement.
Read the resulting adjustments and placement: trims can clamp to shorter replacement sources, and clips append to the current cut. Inspect the result, revise the requested text and timing, and check frames and audio. Apply background removal to replacement footage when requested. save_template and template_add support reusable arrangements.
