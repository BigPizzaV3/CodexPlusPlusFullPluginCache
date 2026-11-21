---
name: helpcenter-get-started
description: Set up a HelpCenter.io connection, identify the help center available to it, and link to its dashboard when the user connects or asks what it can access or where to manage it.
---

HelpCenter.io tools use the user's OAuth connection. Authentication belongs in the sign-in flow; never request passwords, API keys, access tokens, or verification codes in conversation.

Call `helpcenter_list_sites` to show the help centers granted to this connection. For the standard plugin connection, choose one help center during OAuth consent so content operations have an unambiguous target. A list of sites is evidence of access, not evidence that any one site is selected.

Dashboard links use `https://helpcenter.io/app/sites/{subdomain}`, where `{subdomain}` is the site's exact `subdomain` returned by `helpcenter_list_sites` with `response_format: json`. Match the user's intended help center; do not infer this value from its name, numeric ID, custom public domain, or subfolder. Append `/articles` for the content dashboard, `/articles/{article_id}/edit` for an article editor, `/stats` for analytics, or `/settings` for site settings. Use actual article IDs. These links require HelpCenter.io sign-in and the user's dashboard permissions; OAuth access does not create dashboard membership. If the target's subdomain is missing or ambiguous, use the help center picker at `https://helpcenter.io/app/sites`. For reader-facing links, use the returned public `url` instead.

If a content operation returns `site_required`, explain that the connection needs an explicit help center. Ask the user to reconnect with consent for one help center. Developer connections also support a connection URL with `?site=<id>` from the returned list. There is no tool argument that switches the selected site; never invent one. If no sites are returned, explain that authorization or current membership does not grant a usable help center.

Use permissions needed for the user's task: content reads, content writes, analytics, private notes, and template design have distinct scopes. Template reads need `design.read`; template writes need `design.write`, which can change visitor-facing CSS and scripts after publication. Content access does not imply design access. Treat 401 as a need to reconnect and 403 as a permissions or entitlement problem; do not search for other credentials or initiate an upgrade.

Describe the next step relevant to the user's request. This setup does not authorize content or template writes, publication, moderation, or reader replies. Explicit user instructions govern the task and take precedence over workflow defaults.
