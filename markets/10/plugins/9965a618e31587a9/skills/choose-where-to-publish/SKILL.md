---
name: choose-where-to-publish
description: Help the user pick how to get a finished UiChemy project online or out of UiChemy, then hand off to the right skill. Use when the user says publish, launch, host, put online, go live, deploy, get a link, share, export or download and has not said where.
---

Use this skill when the user wants the site "live", "online", "published", "exported" or "downloaded" but has not said where. Do not use technical words they did not use. Reply in the user's own language and script (for example Roman Hinglish stays Roman Hinglish).

Ask one short question, offering only the options their account supports, with the first as the default:
1. A quick link to show someone: a UiChemy-hosted preview. Use `publish-live-site`. Tell the user plainly whether it is a 24-hour temporary preview or a permanent one before you create it.
2. Their own WordPress site: use `deploy-to-own-wordpress`. If they only want the project marked ready for the UiChemy WordPress plugin, use `export-to-wordpress`.
3. Their own Cloudflare account, with an optional editable CMS: use `publish-to-cloudflare`.
4. The code to host anywhere (Astro, HTML, React or Next.js): use `download-site-as-code`, or `export-astro-project` for an Astro zip.

Rules:
- Do not choose Elementor versus Gutenberg for a user who has not heard of them. If the route needs a builder, ask once in plain words ("Do you use Elementor or the standard WordPress editor?") and offer to pick the simpler one for them.
- This plugin does not connect custom domains or change DNS. Say so if asked.
- Do not describe prices or plans. If the account cannot do something, say that and link https://uichemy.com/pricing/ as information only.
