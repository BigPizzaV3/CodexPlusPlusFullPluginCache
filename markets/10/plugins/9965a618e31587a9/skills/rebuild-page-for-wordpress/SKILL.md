---
name: rebuild-page-for-wordpress
description: Rebuild or redesign one page of an existing UiChemy project, for example a weak homepage, a pricing page or a landing page, using the section library and fresh copy so it is ready for Elementor or Gutenberg. Use when the user asks to redo, redesign, refresh or rebuild a page, or make a page cleaner and more WordPress-ready.
---

Use this skill when one page needs a rebuild, not the whole site.

Steps:
1. Identify the project and page. Call `uichemy_get_project`, then `uichemy_get_page` for that page so you know its sections, slot tokens and current copy.
2. Tell the user what you plan in plain words: which sections stay, which are replaced, which are added, and that the page's current layouts will change. If the page has copy the user wrote, ask them to confirm before replacing it.
3. Copy limits come from `uichemy_template_slots` for each layout. Do not guess them.
4. For each section to change, find a layout with `uichemy_search_layouts` or `uichemy_find_templates`, read `uichemy_template_slots`, and write copy that fits each slot. Use `uichemy_replace_section` to swap a layout, `uichemy_add_section` to add one, and `uichemy_set_text` for copy. To keep an original untouched, use `uichemy_duplicate_page` first and rebuild the copy.
5. If the library has no layout for something the user wants, use the `add-custom-section` skill.
6. Run `uichemy_check_responsive` for the page and `uichemy_validate` for the project. Fix what they report.
7. Call `uichemy_open_preview` and summarise what changed, section by section.

Rules:
- Keep the facts already on the page. Do not invent awards, statistics, testimonials, prices or addresses.
- Removing a section or page cannot be undone from here. Name it and wait for a clear yes before `uichemy_remove_section` or `uichemy_remove_page`.
- Change only the page the user named.
