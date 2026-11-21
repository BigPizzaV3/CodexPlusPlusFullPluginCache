# Zaelion plugin preview 0.1.3

Read and search your own Zaelion lists and tasks through https://zaelion.com/mcp.
The server stays hosted; no database, wallet, API key, or local service is needed.
The SVG is a provisional package icon.

## Install for local testing

Use the companion `zaelion-test-bundle-0.1.3.zip`, which includes a local
marketplace. Extract it to a permanent folder. With the Codex CLI installed, run:

```sh
codex plugin marketplace add /absolute/path/to/zaelion-test-bundle
```

Restart the desktop app, open Plugins, select the **Zaelion Test** source, and
install **Zaelion**. Local marketplace availability depends on the client version.
This is not a public directory listing or a universal one-click ZIP installer.

## Authentication status

Package installation and OAuth authentication are separate tests. This archive
does not contain credentials and does not register an OAuth client.

Zaelion currently has a manually registered ChatGPT OAuth client. Its client ID
is `tpc_jXy12hbYFFfgdLAhEVqmRK`, with callback
`https://chatgpt.com/connector_platform_oauth_redirect`, public-client PKCE,
and scope `zaelion:read`. DCR remains disabled. CIMD discovery is now enabled,
and ChatGPT's official `https://chatgpt.com/oauth/client.json` is registered as
`tpc_4jzCjtcci4cCko3PytzbJ4` with only delegated `zaelion:read` access.
Do not assume this client works with a different Codex callback.

A fresh Codex connection may fail at client registration or callback validation.
If that happens, record the error and the callback requested by the client;
Zaelion's OAuth configuration must be made compatible before tools can run.
Do not disable authentication or copy another user's tokens to work around it.

For ChatGPT developer-mode testing, add `https://zaelion.com/mcp` with OAuth,
the above manual client ID, and no client secret, then sign in with Google.
This separately registered connection is not embedded as a personal app ID in
the archive and is not automatically shared with another ChatGPT account.

## Smoke test after connecting

1. Ask "Which Zaelion account am I connected to?" (`get_profile`).
2. Ask "Show my Zaelion lists." (`list_lists`).
3. Read tasks from one returned list, then search for a known task.
4. On a separate Google account, confirm it only returns that account's data.
5. Ask to create a task; the plugin has no write tools and must not claim success.

New users receive separate accounts. Public browser sign-in now lets them create
lists and tasks at https://zaelion.com using the same Google identity as MCP.

## Package formats and publication

`plugin.json` and `mcp.json` provide the portable format. The `.codex-plugin`
manifest and `.mcp.json` support clients using the compatibility format.
Both configurations point to the same single remote service.

`zaelion-plugin-0.1.3.zip` contains only this plugin folder. For public submission,
upload using the MCP route and complete OAuth, publisher/domain verification,
listing metadata, policy URLs, and review requirements in the portal. This preview
is not yet a completed public submission.

Official documentation: https://developers.openai.com/plugins/build/plugins

## Publishing checkpoint — 4 October 2026

Publisher identity verification passed and the owner uploaded version 0.1.2.
The draft is plugin_asdk_app_6ac198ed375c819196992c5a96f6f161.
The public domain challenge was deployed and the portal confirms Domain verified.
The support page is deployed at https://zaelion.com/support.html; the existing
privacy notice is available at https://zaelion.com/privacy.html.
Version 0.1.2 adds publisher metadata, all three policy/support links, and the
updated description reflecting public browser onboarding. The portal accepted the
upload and reports No Issues for metadata.
The owner approved the terms on 4 October 2026. The page is deployed at
https://zaelion.com/terms.html and its live content matches the approved source. Proposed review test cases are not completed tests.
The portal now reports Authorized and Configured and discovered all five tools.
The initial scan flagged missing explicit safety annotations. The tested server
update is deployed, and a fresh portal scan reports no issues for all five tools.
The owner created and reset the password for the separate contact@zaelion.com
reviewer identity (`auth0|6ac1fb9ef07ae94fcdfd8c6b`). Auth0's password connection
test succeeded. With explicit approval, the database connection was promoted to
domain level, public password sign-ups disabled, and Zaelion Web enabled for the
connection. The website still enforces Google identities in its login code;
password-based reviewers must connect through ChatGPT rather than the website.
The demo identity connected to the personal ChatGPT development plugin as
"Zaelion reviewer demo"; the owner's existing primary connection was preserved.
Zaelion provisioned a distinct active user, 1d878889-1f8c-4ed4-a968-faf99db1ee7b.
The approved demo data was added through the audited list/task services: Demo
Garden (Plan spring gardening; Water the herb pots) and Demo Personal (Prepare a
weekend checklist). Service read-back confirmed all three tasks. The owner entered
the demo password directly into OpenAI's reviewer form; Save details returned
"Progress saved". No password was read into local source or archives.
The portal confirms five complete positive and three complete negative test cases.
Version 0.1.3 includes `extensions.com.openai.review.demo_recording_url` pointing
to https://zaelion.com/review/zaelion-plugin-walkthrough.mp4. The 96-second silent,
captioned screenshot walkthrough shows actual ChatGPT responses for all five
read tools on the reviewer demo account. A combined negative prompt was blocked
by ChatGPT before a tool call; this does not verify server-side account isolation.
A separate capability response confirms no write tools are exposed. MP4 duration
and two decoded frames were verified locally. The new ZIP still needs upload,
review validation, and the owner's final policy attestations before submission.
Auth0's manual CIMD preview successfully validated
https://chatgpt.com/oauth/client.json, but ignored the plural
`token_endpoint_auth_methods_supported` field and mapped the singular preference
to `private_key_jwt`. Auth0 documents that method as Enterprise-only; the tenant
currently displays a trial. Registration and the delegated read grant succeeded;
machine access remains denied. Long-term availability after the trial has not
been confirmed, and no paid upgrade was accepted.
This package is not published and is not a working shared ChatGPT installation.
