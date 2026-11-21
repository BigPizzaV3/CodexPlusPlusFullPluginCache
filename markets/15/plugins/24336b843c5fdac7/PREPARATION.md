# Beebyte public submission - preparation draft

This is a preparation draft, not ready for submission. Nothing has been uploaded to the public submission portal.
The working private plugin and its app binding remain unchanged.
The technical package name follows the working private source. The display name is Beebyte.

## Confirmed and prepared
- Working private plugin: https://chatgpt.com/plugins/plugin_asdk_app_6aeda0dca4648191b77793b3b4ff16e9
- Verified app binding in private source: asdk_app_6aeda0dca4648191b77793b3b4ff16e9. This binding is intentionally excluded from the public upload copy.
- Official remote endpoint: https://mcp.beebyte.se/mcp
- OAuth discovery advertises DCR and portal scope. Reviewer connection ping returned pong=true for the dedicated demo account with one organisation, beebyte (ID 13884).
- Publisher requested by creator: Beebyte AB. Developer/business verification in the submission portal is still unverified.
- Support and terms URLs fetched and inspected. Privacy PDF fetched and text inspected; creator confirms it applies to the plugin.
- Branding: square 512px PNG derived from the supplied SVG emblem, with a white background for contrast in light and dark interfaces. The logo retains the original #FFAF00 orange. The interface brandColor is #D98C00, a darker orange with contrast 2.727:1 against white. Awaiting creator feedback; no separate dark asset is required.
- Countries: [] means no plugin country allowlist, subject to platform and Beebyte service availability. Provisionally selected from creator's tentative preference; confirm before submission. Change to ["SE"] for Sweden only.
- Paid website creation is included. Creator confirms portal and existing billing handle charges.

## Still needed
1. Website URL supplied and verified: public Beebyte KB article "Sätt upp MCP för ditt konto" explains account requirements and customer-portal AI-agent setup. Added as interface.websiteURL. This listing item is complete.
2. Dedicated reviewer account is prepared and connected; account access verified. Enter its credentials only in secure portal fields, never in this ZIP or chat. Verify reviewers can sign in without the creator's mailbox or phone.
3. Actual fixture: ggjqq.beeweb-orange.io (ID 15862), organisation beebyte (ID 13884), active Linux/PHP hosting. /httpdocs/index.html existed before testing. Added /httpdocs/review-demo.html containing <h1>Beebyte review demo</h1> with overwrite=false; exact readback and search succeeded. No other files were changed.
4. Direct tool smoke checks PASSED: ping, list_websites, get_website_info (PHP 8.4, memory 1024M, /httpdocs), list_website_files, upload_website_files, download_website_file exact readback, and search_website_files. These are tool-level checks, not a complete conversation evaluation. Run the five positive and three negative prompts in the intended host and capture their actual results. The originally specified static-HTML paid-provisioning case is NOT RUN. The creator's video instead demonstrates a Linux/PHP test order after explicit confirmation; website ID 15863, jendp.beeweb-pink.io, label Test website. The video ends with provisioning still pending, accurately explained by the assistant. No new paid order was placed by the preparation agent.
5. Latest supplied tools(2).json metadata reviewed: all 20 tools include explicit boolean readOnlyHint, destructiveHint and openWorldHint. Previous missing fields, paid-order and publishing annotations are resolved. create_website_database is destructive=true and writes /database.php outside /httpdocs; database output schemas omit password. Supplied-metadata review passes. Runtime implementation, secret-file protection and portal scan remain unverified; no claim of live-server or review approval is made.
6. Demo recording URL supplied and added to review.demo_recording_url. Public unauthenticated download succeeded; ffprobe identifies a 241.867-second H.264 video at 1380 x 1116. Sampled frames show readable actual ChatGPT interactions. Full local video decode checked. The MKV URL is download-accessible; in-browser streaming compatibility has not been verified.
7. Before submission: developer verification, domain verification, OAuth connection and tool scan of the saved public draft, legal attestations by the authorised developer.

## Proposed demo recording (about 2-3 minutes)
Use a dedicated test account with sample sites and no unrelated data. Keep passwords, OAuth codes, tokens and database credentials off screen.
1. Start the screen recorder; show the Beebyte plugin and its OAuth connection using the test account.
2. Ask: "List my Beebyte websites." Show returned sample websites.
3. Ask: "What PHP version and memory limit does my ggjqq.beeweb-orange.io website use?" Show the actual settings.
4. Ask: "On ggjqq.beeweb-orange.io, publish review-demo.html in the document root containing exactly <h1>Beebyte review demo</h1>. Replace that file if it already exists and leave every other file unchanged." Show the successful tool result and verify the harmless page.
5. Ask: "Create a new email mailbox for my domain." Show the explanation that mailbox administration is not supported.
6. Explain that new website provisioning is paid through existing billing. Show the confirmation step; only place a real test order after explicit approval and appropriate billing arrangements.
7. Stop recording, play back to check readability and absence of secrets, then host it at a reviewer-accessible URL. Provide that URL to add review.demo_recording_url.

## ZIP validation
- Portable plugin.json and mcp.json with schema declarations.
- One remote server, verified endpoint, OAuth DCR, no embedded credentials or nonempty server headers.
- Exactly five positive and three negative cases, drafted from actual tools.
- Required listing icon exists, 512 x 512 PNG; subtitle is within 30 characters.
- No .app.json or apps declarations in the public copy. Preserve all app bindings in the working private source.
- Missing fields are omitted rather than replaced with placeholder URLs.

## Current recording capability
No screen/video recording tool is available in this session. The creator should record the actual ChatGPT walkthrough using their own screen recorder, following the prompts above. Screenshots or this script are not a demo recording.

## Demo evidence review
- Public source: https://zegve.beeweb-pink.io/simplescreenrecorder-2026-11-06_11.13.58.mkv
- Observed website listing: ggjqq.beeweb-orange.io, ID 15862, beebyte organisation.
- Observed PHP settings: PHP 8.4, 1024 MB memory limit.
- Observed write approval and published /httpdocs/review-demo.html, 28 bytes, expected HTML content shown.
- Observed mailbox limitation explanation; no fabricated mailbox success. The response also offers portal help.
- Observed paid monthly hosting disclosure, user confirmation, one Linux/PHP order and wait-for-provisioning action. Recording ends with status provisioning. Do not describe this video as showing an active new site.
- No passwords, access tokens, or database credentials were visible in the sampled frames.
- OAuth sign-in is not shown in the recording. The private account connection was verified separately.
- Evidence supports listing, PHP settings, file upload, unsupported mailbox handling, and a Linux/PHP provisioning variant. It does not prove every formal case or tool annotation passed. Domain registration and VPS negative cases remain untested.

Follow-up verification: get_website_info for website_id 15863 returned status active, Linux/PHP 8.4, document_root /httpdocs. This verifies eventual provisioning separately from the recorded footage.

Latest package update also replaces outdated review-static/review-php starter prompts with the actual sample website domain. Public submission and publication have not been performed.

## Portal OAuth validation fix - version 1.0.2
Explicit authorizationUrl, tokenUrl and registrationUrl now match the official discovery response. OAuth DCR and portal scope are preserved. Upload this version to the existing draft, inspect MCP settings, and reconnect/scan. No secrets are included.

## Brand contrast fix - version 1.0.3
Changed interface.brandColor from #FFAF00 (1.845:1 against white) to #D98C00 (2.727:1 against white), exceeding the portal minimum of 2:1. Logo image, OAuth endpoints and other submission metadata are retained.

## Requested listing update - version 1.0.4
About text replaced with creator-supplied wording verbatim. Privacy policy URL changed to https://www.beebyte.se/dokument-och-villkor/; public page inspected and identifies the Beebyte personal-data policy. Other listing, branding, OAuth and review settings are retained.

## About grammar correction - version 1.0.5
Changed "and working with your databases" to "and work with your databases". No other listing or connection settings changed.
