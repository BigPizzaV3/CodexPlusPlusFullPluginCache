---
name: publish-to-cloudflare
description: Publish a UiChemy project as a fast Astro site in the user's own Cloudflare account on a free workers.dev address, with or without the EmDash CMS, then check, update or take it down. Use when the user asks for Cloudflare, workers.dev, EmDash, a site a client can edit in a CMS, or to host on their own Cloudflare. For a UiChemy-hosted link use publish-live-site.
---

Use this skill when the user wants the site on their own Cloudflare account.

Steps:
1. Identify the project with `uichemy_list_projects` if the user did not name it. Run `uichemy_validate` and offer to fix faults first.
2. Ask what to publish, in plain words:
   - Astro with EmDash: the site comes with an editable admin area so the user or their client can change text, images, pages and blog posts. It is required if the site has a blog.
   - Astro frontend: static pages only.
3. Say: "I will publish this project to your own Cloudflare account." Wait for a clear yes. For Astro with EmDash call `uichemy_publish_emdash` (if it returns a jobId, check it with `uichemy_emdash_status`). For the Astro frontend call `uichemy_deploy_to_cloudflare`.
4. The first time, the user must connect their Cloudflare account on Cloudflare's sign-in screen and approve every permission it shows. Give them the link the tool returns and wait. Never ask for a Cloudflare password or token in the chat.
5. Report the live address and status only from what the tool returns. For EmDash sites, the admin area is locked behind a one-time setup link after the first publish: get it with `uichemy_open_cms_admin` and give it only to the user. After setup the admin is at the site address followed by `/_emdash/admin` and signs in with a passkey (Touch ID, Windows Hello or their phone).
6. To update after design changes, call the same tool again. EmDash updates keep the CMS content and users.
7. For an Astro frontend site, `uichemy_site_versions` lists every published version, and `uichemy_restore_site_version` puts an earlier one back online. Name the version and wait for a clear yes before restoring.
8. To take the site down, name it, ask for confirmation, then call `uichemy_unpublish_cloudflare`. For EmDash it keeps the CMS content by default. Only pass `deleteData` after the user clearly agrees that the CMS content and logins will be deleted for good.

Rules:
- The site lives in the user's own Cloudflare account. Cloudflare's own limits and charges apply; a free workers.dev address is not a promise of unlimited hosting.
- Custom domains are not available through this plugin. Say so if asked.
- If the tool says Cloudflare publishing is not available, offer `export-astro-project` instead.
- Do not describe prices or plans. If the account cannot publish, say that and link https://app.uichemy.com/support.
