# Privacy and data summary

## Data exchanged

ChatGPT receives tool results for the connected device's authorized list
memberships and reminders. The current MCP projection includes list IDs, titles,
types, emoji, shared/hidden-completed flags and update timestamps; item IDs,
category IDs, text, quantities, units, order and checked status; reminder IDs,
titles, schedule, time zone, recurrence, enabled status, delivery mode and
creation/update timestamps. Writes send the requested list/item/reminder fields
and an operation key to LystBot. Tools do not return device credentials, FCM
push tokens, attachment contents, Alexa links or OAuth token hashes. The privacy
notice also mentions membership roles; the current MCP projection does not
return that field.

OAuth connects a device grant to the client, scopes and resource. ChatGPT holds
the access/refresh credentials needed to call the connection; LystBot stores
hashes of these tokens. Pairing and review codes are also stored only as hashes.
Review codes are bound to explicitly marked, isolated demo devices, not an
account login. A review code never grants access to another device.

## Lifetimes and retention in LystBot

| Record | Code/notice behavior |
| --- | --- |
| Normal pairing code | App default 10 minutes; admin default 7 days, maximum 30 days; single use. Expired normal codes are removed during subsequent pairing operations. |
| Demo review code | Default 90 days, CLI range 1-180 days. Reusable until expiry or revocation; replacement invalidates the previous code. The demo row/hash has no automatic deletion on expiry or revocation and remains until device deletion or explicit administrative removal. |
| OAuth request / CSRF cookie | 10 minutes; cookie cleared on completion. |
| Authorization code | 2 minutes, single use. |
| Access token | 1 hour. |
| Refresh token | 30 days; rotation preserves the original expiry. |
| Expired OAuth rows / attempt counters | Removed on new authorization starts / subsequent attempts respectively. IP and global attempt window is 10 minutes. |
| Grants and revoked tokens | Disconnection invalidates access, without deleting records. Device deletion cascades to grants and tokens. Review-code expiry/revocation alone does not revoke existing grants. |
| Write receipts | Hashes and result JSON, potentially containing content; no automatic expiry, remain after disconnection, cascade on device deletion. |
| Device/list/reminder data and operational history/logs | Retained as necessary for the service, traceability and security under section 9; the notice does not assign a fixed duration. Uninstalling does not delete server data. |

OpenAI receives and may retain returned content under its own policies and the
reviewer's ChatGPT settings. This repository cannot establish which content
OpenAI actually stores or a universal OpenAI deletion deadline. Disconnecting
stops authorized access; it does not erase earlier chats or independently
stored copies. Privacy/deletion requests: hello@touraround.io.

Evidence: `McpController.php` projection/receipts, `AlexaPairingService.php`,
`OAuthAuthorizationService.php`, `OAuthController.php`, migrations 030-033,
and [LystBot privacy notice, sections 7.4, 8 and 9](https://lystbot.com/legal/privacy-en.html)
(local source: `backend/public/legal/privacy-en.html`). The public notice states
ordinary pairing/OAuth lifetimes; demo-review retention above is a code-derived
submission disclosure. These files are drafts, not live privacy-page changes.
