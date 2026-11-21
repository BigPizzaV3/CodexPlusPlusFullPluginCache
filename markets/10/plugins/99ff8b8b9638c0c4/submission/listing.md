# LystBot

- Short description: Manage your LystBot lists, checklist items and reminders in ChatGPT.
- Suggested category: Productivity
- Publisher: TourAround
- Support email: hello@touraround.io
- Privacy: https://lystbot.com/legal/privacy-en.html
- Terms: https://lystbot.com/legal/terms-en.html
- MCP: https://lystbot.com/api/v1/mcp
- Requested countries: EU member states and USA

## Long description

Connect ChatGPT to a LystBot device using a pairing code and OAuth approval.
Read that device's own and shared lists, view their items and reminders, create
lists, add items, edit item text or checked status, and create reminders.
Access follows the connected device's list memberships, roles and approved
scopes. There are no tools for deleting lists or items or changing sharing.
Disconnecting withdraws access without deleting list content or previous chats.

## Internal evidence and readiness

Sources: `backend/src/Controllers/McpController.php`, `ListMember.php`,
`OAuthAuthorizationService.php`, `backend/public/legal/imprint-en.html` and
Paket G of `plans/01-altair-chatgpt-plugin-genius.md` (publisher/regions).
The short description is below 80 characters. This is submission copy, not a
claim of publication or availability in these countries. The existing Paket E
manifest/README still use `https://lystbot.com/lystbot/api/v1/mcp`; the proposed
submission URL above matches the backend's `/api/v1/mcp` route and deployment
routing documentation. TARS must reconcile the deployed OAuth resource and
package endpoint before submission. No endpoint or manifest was changed here.
