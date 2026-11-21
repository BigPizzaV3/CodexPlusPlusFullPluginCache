# Use LystBot in ChatGPT

Draft for lystbot.com and README. Publish only after approval and availability
of the LystBot connection; this draft does not claim a directory listing exists.

1. In the LystBot app, open **Settings → ChatGPT** and generate a pairing code.
   In older versions, generate it under **Settings → Alexa** instead.
2. Open the LystBot connection in ChatGPT and select Connect. For an authorized
   private test, add the supplied MCP app/connector with OAuth first.
3. Enter the six-digit code on LystBot's authorization page and select
   **Verbinden** (Connect). The app code expires after 10 minutes and works once.
4. Return to ChatGPT and ask, for example, “Show my LystBot lists” or “Add apples
   to Weekly Groceries”, using a list that actually exists on your device.

ChatGPT can read your device's own/shared lists and reminders, create lists,
add items, edit text or checked status, and create reminders. Access follows
list membership, roles and approved scopes. There are no delete or sharing tools.
Disconnect through connection management in ChatGPT or **Settings → ChatGPT**
in LystBot. This withdraws access without deleting lists or previous chats.

[Privacy](https://lystbot.com/legal/privacy-en.html) ·
[Terms](https://lystbot.com/legal/terms-en.html) · Support: hello@touraround.io

Internal evidence: pairing/OAuth/MCP services and `plugins/lystbot/README.md`.
Connection-flow reference: [official OpenAI documentation](https://developers.openai.com/plugins/deploy/connect-chatgpt).
