---
name: export-to-wordpress
description: Mark a finished UiChemy project as exported for Elementor or Gutenberg and show which projects are ready for the UiChemy WordPress plugin to pull. Use when the user says the site is done, asks to export it to WordPress, Elementor or Gutenberg, or asks what has been exported. If the user names a WordPress site or URL to put it on, use deploy-to-own-wordpress. For a live UiChemy-hosted link, use publish-live-site.
---

Use this skill when the user wants a finished project ready for WordPress but has not named a WordPress site.

If the user gives a WordPress site, a wp-admin link, or asks to import, install or deploy the project on their WordPress, switch to the `deploy-to-own-wordpress` skill now. It does these same steps and then gets the project imported into that site.

Steps:
1. Identify the project with `uichemy_list_projects` if the user did not name it.
2. Run `uichemy_validate` and `uichemy_check_responsive`. If either reports faults, tell the user and offer to fix them first. Do not mark a project exported while known faults remain unless the user says to go ahead.
3. Ask which builder, Elementor or Gutenberg, if the user has not said.
4. Call `uichemy_mark_exported` with the project and builder. It also publishes the builder code for projects imported from code; `uichemy_sync_builders` is only needed to check that result first.
5. Call `uichemy_list_exported` to confirm the project now appears.
6. Tell the user the next step happens inside their WordPress site (UiChemy, then Home, then AI Website Creator), and offer to take them through it: if they give the site address, continue with `deploy-to-own-wordpress`.

Rules:
- To put a project live on a UiChemy address, or take one offline, use the `publish-live-site` skill. For Cloudflare use `publish-to-cloudflare`; for code use `download-site-as-code`. If the user has not heard of Elementor or Gutenberg, ask once in plain words and offer to pick the simpler one.
- This plugin does not connect custom domains or change DNS or hosting.
- Do not describe pricing or plans. If the account cannot export, say that and link https://app.uichemy.com/support.
