---
name: redact
description: Open a private local text-redaction panel before the user shares sensitive text with a conversation.
---

Call `open_redactor` with no arguments. Tell the user to download/load the models in the panel, paste the original text directly into that panel, review detected highlights and any Keep decisions, then click Redact and review the final message before sending it to chat.

Never request original private text in a chat message or tool arguments. Never claim to intercept the host composer or that redaction guarantees all personal information is removed. The input and inference remain in the panel's worker; only the user's explicit Send action shares the result.
