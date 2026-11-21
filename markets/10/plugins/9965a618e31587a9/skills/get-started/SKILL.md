---
name: get-started
description: Orient a new user to UiChemy AI Website Creator, confirm which UiChemy account is connected, and list their projects. Use when the user first connects, asks what UiChemy can do, how to start, or when any UiChemy call is refused.
---

Use this skill when the user has just connected UiChemy, asks what they can do here, or a UiChemy tool returns an access error.

1. Call `uichemy_whoami`. Report the account it returns and what that account can reach. If it says the account lacks access to create projects, say so plainly and point the user to https://app.uichemy.com/support. Do not retry in a loop.
2. Call `uichemy_list_projects` and show the user's projects, newest first, by name. Do not show internal ids unless the user asks for one or a later step needs it.
3. Offer what this plugin does, in one short list, in the user's own language and script:
   - Build a new multi-page website or landing page from a brief.
   - Edit an existing UiChemy project: colours, fonts, copy, sections, pages, dark mode and animations.
   - Build an online store with WooCommerce shop pages (see `build-online-store`).
   - Check a site for SEO and design issues before launch, and set each page's SEO settings (see `seo-and-site-review`).
   - Put the site online: a UiChemy preview link, your own Cloudflare account (with an optional editable CMS), or your own WordPress (see the `choose-where-to-publish` skill).
   - Download the site as code (Astro, HTML, React or Next.js).
   - Open the UiChemy dashboard, editor or a page preview right here in the chat (see the `open-uichemy` skill).

Rules:
- To show the dashboard, a project or a preview, call `uichemy_open_projects` or `uichemy_open_preview`. Never open app.uichemy.com in a browser.
- Only act on the connected user's own UiChemy projects.
- Never ask for a password, API key or token. Sign-in happens through UiChemy's own sign-in screen.
- Do not describe prices, plans or upgrades. If a feature is unavailable on the user's plan, say that, and link https://uichemy.com/pricing/ as information only.
