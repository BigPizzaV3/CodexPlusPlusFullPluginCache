---
name: publish-live-site
description: Publish a finished UiChemy project as a live preview website on a UiChemy address (uichemysites.com), check whether it is online, list the user's published sites, take one offline, or sign the user in to that site's WordPress admin. Use when the user asks to publish, launch, put online, get a live link, share a preview link, unpublish a site, or open the admin of a UiChemy-hosted site. For a WordPress site the user already owns, use deploy-to-own-wordpress.
---

Use this skill for sites hosted by UiChemy. If the user names their own WordPress site or hosting, switch to `deploy-to-own-wordpress`.

Steps:
1. Identify the project with `uichemy_list_projects` if the user did not name it.
2. Run `uichemy_validate` and `uichemy_check_responsive`. Report faults and offer to fix them first.
3. Say plainly: "I will put this project live on a UiChemy address." Wait for a clear yes, then call `uichemy_publish_site`.
4. Call `uichemy_publish_status` until it says the site is live. If it is still setting up, say so and check again. Report the address and the status. Do not claim it is online before the status says so.
5. `uichemy_list_sites` shows the user's published sites and their status.
6. To take a site offline, name it, ask the user to confirm, then call `uichemy_unpublish_site`.
7. If the user asks to open the site's WordPress admin or dashboard, confirm which site, then call `uichemy_open_site_admin` and give them the one-time link at once. It signs them in without a password, works once and expires after about a minute. If it expired, call it again. Only if the user asks for a username and password they can keep, call `uichemy_site_admin_login`, warn that it sets a new password and signs out anyone already in, and tell them to save it. Show the password only in that reply and never store or repeat it.

Rules:
- Before you create the site, tell the user plainly if it is a temporary 24-hour preview or a permanent one, using what the tool offers. A temporary link stops working after 24 hours unless made permanent. If the user wants to keep it online, call `uichemy_keep_site_live` to make it permanent or turn it on for another 24 hours, and say it uses one of their site slots.
- If the user wants the site on their own Cloudflare account or as downloadable code, use `publish-to-cloudflare` or `download-site-as-code`.
- This plugin does not connect custom domains or change DNS. Say so if asked.
- Never send the user to wp-login.php for a UiChemy-hosted site. The admin account was created by UiChemy.
- Do not describe prices or plans. If the account cannot publish, say that and link https://app.uichemy.com/support.
