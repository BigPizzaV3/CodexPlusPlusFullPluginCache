---
name: background-removal
description: "Remove or replace the background behind a person or subject in a Donkey Cut clip. Use when the user asks for a cutout or a background swap."
---

# Background removal
set_removal mode auto starts the free person matte. remove background keeps the subject; remove subject keeps the surroundings. mode custom tracks the described subject and spends credits. refine requests the paid quality pass when the user asks for an upgrade. mode off retains the stored settings.
The matte prepares in the editor. Read each clip's removal readiness and progress with inspect_project; a command returning successfully can still leave matting in progress. Check capture_frame after it is ready. Poll a returned command job with get_job_status; that job's completion and the matte's readiness are separate results.
For one exact instance among similar subjects, ask the user to use Custom, Brush and Erase in the Cutout inspector and press Apply. set_removal_stroke adds an outline, and set_removal_background fills behind the kept subject. A lower video track can carry independently editable scenery.
