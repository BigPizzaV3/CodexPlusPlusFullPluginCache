---
name: improve-ui
description: Review a React + Tailwind project and suggest Uniquel components or blocks that would improve its UI. Use when the user asks to improve, upgrade, or polish their UI, or asks which Uniquel components fit their project.
---

# Improve UI with Uniquel

1. Confirm the project uses React and Tailwind CSS. If it does not, tell the user Uniquel components need both and stop.
2. Read the project's pages and layouts. Note sections that are plain, hand-built, or missing, such as a basic hero, a custom pricing table, or no testimonials.
3. For each one, call `search_catalog` with a short description of the section.
4. Show the top 3 suggestions. For each, give what it replaces or adds, the file it would go in, its preview image, and whether it is free or requires All Access.
5. When the user picks one, call `plan_install` and execute every operation exactly. Do not edit the installed component file; adjust the page that renders it instead.
6. Call `confirm_install` with fresh file contents. If a check fails, fix that item and confirm again.
7. If a tool returns `upgrade_required`, share the `upgradeUrl`. Never recreate a paid component by hand.
