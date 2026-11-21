---
name: setup
description: Connect OfferCopilot and check the connection works. Use right after installing the plugin, or when an OfferCopilot tool says the connection is missing, expired, revoked or not allowed to do something.
---

1. Call `list_offers`. If it returns offers, tell the user how many live deals they have and stop.
2. If it fails because the user isn't connected or the connection expired, ask them to connect OfferCopilot from this plugin's settings. A browser tab opens OfferCopilot's sign-in and then one screen listing three permissions; they tick what they want and click Allow.
3. Explain the three permissions in one line each:
   - Read my deals: see offers, deal status, signers and what clients owe.
   - Add clients: add a client to their client list.
   - Remind signers, email clients and mark offers received: every email is read back for approval before it goes out.
4. If a tool later says the connection isn't allowed to do something, the user needs to disconnect OfferCopilot under Profile → AI Agent Access, connect again and tick that permission.

Never ask the user for their password or an API key in the chat.
