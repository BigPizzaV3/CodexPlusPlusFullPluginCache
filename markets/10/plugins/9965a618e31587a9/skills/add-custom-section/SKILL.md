---
name: add-custom-section
description: Design and add one new section to a UiChemy page when the library has no layout that fits, for example a pricing table, a gallery, a timeline or an unusual hero, or redesign an existing section. Use when the user asks for a custom section, a section the library does not have, or a fresh design for one section.
---

Use this skill when the library layouts do not cover what the user wants. UiChemy designs the section the same way its editor's Designer does, so it matches the rest of the site and stays editable.

Steps:
1. Identify the project and page. Use `uichemy_get_project` if needed. Say that a new section will be added to that page.
2. Call `uichemy_design_section` with `projectId`, `pageName`, the section `kind` and the `position` where it should go. Follow the design rules and the technical contract it returns exactly, and match the copy and style of the neighbouring sections it shows you.
3. Write the section file, then save it with `uichemy_add_designed_section`. It only adds one section and never replaces an existing one. If the call is refused, read the reasons it returns, fix the file and try again.
4. To redesign a section that already exists, call `uichemy_design_section` with `replace` instead of `position`, then save with `uichemy_update_designed_section`. That call OVERWRITES the section, including copy the user edited, so tell the user and wait for a clear yes first.
5. Run `uichemy_check_responsive` and `uichemy_validate`, then `uichemy_open_preview`.

Rules:
- Write copy from the user's brief only. Do not invent statistics, testimonials, prices or awards.
- Do not load scripts or styles from a source the user did not ask for.
- Do not put keys, tokens or personal data into a section.
- Do not import or paste in the user's own site code. UiChemy builds sites from its own templates and designed sections.
