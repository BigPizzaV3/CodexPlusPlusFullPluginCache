---
name: export-astro-project
description: Give the user a download link for their UiChemy project as a ready-to-run Astro project (.zip). Use when the user asks for an Astro project, Astro export, Astro zip, or the site as Astro code. For other code formats use download-site-as-code. To put an Astro site live on Cloudflare use publish-to-cloudflare.
---

Use this skill when the user wants the project as Astro code to run locally, put in Git or host anywhere.

Steps:
1. Identify the project with `uichemy_list_projects` if the user did not name it.
2. Run `uichemy_validate`. Report faults and offer to fix them first; continue if the user says to.
3. Say: "I will prepare an Astro project zip of this project." Then call `uichemy_export_astro`.
4. Give the user the download link at once. Tell them the link works for 15 minutes and for up to 5 downloads, and that they can ask again for a new one.
5. Tell them how to run it: they need Node.js 22.12 or newer, then `npm install`, `npm run dev` to preview, and `npm run build` to create the static site in `dist/`, which any static host can serve.

Rules:
- The zip is built from the saved project. If the project changed a moment ago, say it may take up to a minute.
- Do not claim the site is online. A download is code, not a hosted site. For hosting use `publish-to-cloudflare` or `publish-live-site`.
- Do not describe prices or plans. If the account cannot export, say that and link https://app.uichemy.com/support.
