---
name: download-site-as-code
description: Give the user their UiChemy project as downloadable code for hosting anywhere: HTML, Astro, React or Next.js. Use when the user asks to download the code, source, a zip, an HTML export, a React or Next.js version, or wants to host the site themselves. For an Astro zip only, export-astro-project does the same.
---

Use this skill when the user wants the site's code instead of a hosted site.

Steps:
1. Identify the project with `uichemy_list_projects` if the user did not name it. Run `uichemy_validate`; offer to fix faults first.
2. Ask which format they want: HTML, Astro, React or Next.js. If they are unsure, suggest HTML for a simple static site and Astro for a developer workflow. If the chosen format offers an optional CMS, ask which one, or none.
3. For Astro, call `uichemy_export_astro`. For HTML, React or Next.js (or Astro with the EmDash CMS), call `uichemy_download_site`. CMS options: Astro with EmDash, React with Sanity, Next.js with Payload or Sanity, or none. If the user has not chosen, call it without `format` or `cms` and show the question it returns.
4. Give the download link at once and say it works for 15 minutes. Ask again for a new one if it expires.

Rules:
- A download is code, not a live site. Say so, and offer `publish-live-site` or `publish-to-cloudflare` if they want it online.
- Do not invent a format, a CMS or a tool name. Offer only what the tools return.
- Code downloads are available to every signed-in UiChemy account. A guest (try-before-signup) account must sign up first. If a tool still refuses, say that and link https://app.uichemy.com/support. Do not describe prices or plans.
