---
name: get-template
description: Get a template. Use when the user asks for one of their Delegent templates, or wants a PowerPoint, Excel or Word file built in a personal or firm-shared template's style.
---

# Get a template

Delegent returns the template's compiled instructions and style, never the template file. You build the new file with your own tools.

## 1. Find it

- With a `template_ref`, or a name the user gave, call `delegent_get_template`.
- No match or several matches: show `available_templates` or `matches` and ask which one. `delegent_list_templates` lists everything with readiness.
- **No template of their own?** Delegent still has its own standard for PowerPoint, Excel and Word (scope `built_in`, always ready, in the user's brand colour). Call `delegent_get_template` with `name` set to "PowerPoint", "Excel" or "Word", or with the `built_in` template_ref from `delegent_list_templates`. Use it by default instead of your own plain styling; a template the user uploaded always takes priority.

## 2. Check it is ready

- `usable: false` or a file with `ready: false` has a `reason` (still analysing, failed, unsupported type). Tell the user and offer to go without it.
- A file marked `omitted` was left out for size. Call again with `file` set to its name.
- A built-in standard can span several parts (the PowerPoint one does). When the result has `next_part`, call again with `part` set to it and read every part before you build.

## 3. Build the file

- Use the template file whose `format` matches what the user wants (pptx, xlsx, docx).
- `generation_instructions` are binding. Apply `design_tokens` (hex colors, fonts, sizes) and `style_profile`:
  - PowerPoint: canvas ratio, palette, typography, density and the `slide_roles` sequence with box positions in percent of the slide.
  - Excel: sheet order, `anchor_cells` addresses for titles and headers, header/body/section styles, column widths, number formats and `formula_examples` logic.
  - Word: structure, headings and wording from the instructions; there are no extracted style tokens.
- Fill it with the user's sourced facts (`delegent_get_context_for_task`, `delegent_get_source`). Never copy example facts from the template.
- For a full client deliverable with evidence checks, follow `draft-the-deliverable`.

## 4. Save, if asked

On the user's request, `delegent_save_file` saves the finished file to a workstream with a summary and its text.
