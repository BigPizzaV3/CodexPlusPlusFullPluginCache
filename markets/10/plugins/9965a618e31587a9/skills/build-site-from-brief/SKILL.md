---
name: build-site-from-brief
description: Build a new multi-page WordPress-ready website in UiChemy from a business brief, choosing real section layouts from the UiChemy library and writing the copy. Use when the user asks to create, generate, draft or design a website, landing page or site for a business, client or idea.
---

Use this skill when the user wants a new website built from a description, a client brief, or a business type.

Inputs to gather from the user's message first: business name and type, audience, tone, pages wanted, colours or fonts if any. If the business type or name is missing, ask one batched question. For everything else, make a sensible choice and state it.

Steps:
1. Copy limits come from `uichemy_template_slots` for each layout. Do not guess them.
2. Call `uichemy_list_section_kinds` to see which section kinds exist.
3. For each section on each page, find a layout:
   - Describe what you want to `uichemy_search_layouts`, or narrow a kind with `uichemy_find_templates`.
   - Call `uichemy_template_slots` for the chosen layout and write copy that fits each slot and its character cap.
   - Before building, call `uichemy_check_layouts` on the shortlist so two layouts that share slots do not show identical copy.
4. Pick a palette (hex values) and a heading and body font that suit the brand.
5. Call `uichemy_create_project` with the pages, palette, fonts and the copy you wrote. A real page has a navbar, five to eight sections and a footer, with every slot filled.
6. Call `uichemy_validate`, then `uichemy_check_responsive` for each page. Fix what they report with `uichemy_set_text`, `uichemy_set_section_style` or the other edit tools, then re-run the check.
7. Give the user the project name, the page list with each page's sections, the palette and fonts, and anything you could not fix.

Rules:
- Every site is built from UiChemy library layouts. Do not write HTML, CSS, JavaScript or JSX for the site. If the user asks to bring their own code or site, say UiChemy builds sites from its own templates and offer to build it that way.
- Write copy from the brief only. Do not invent awards, client names, statistics, testimonials, prices or addresses. Where a fact is missing, write neutral copy or ask.
- Images: use only URLs the user supplied or that `uichemy_upload_image` returned. Leave an image slot empty rather than inventing a link.
- This skill creates a project in the user's own UiChemy account. Say so before you create it.
