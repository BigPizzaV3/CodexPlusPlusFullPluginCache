---
name: setup
description: Set up the Écran Papier plugin after installation by asking for the owner's screen link and checking that screen through MCP.
---

# Connect your Écran Papier screen

Answer in the owner's language. Explain simply that they can give you the
personal page opened by their screen's QR code, then ask for messages,
photos or services in the conversation. No account or API key is needed.

1. If no screen link was supplied in this conversation, ask for it:
   “Copiez ici le lien de votre écran, celui qu'ouvre son QR code.” Wait
   for the answer before calling screen tools. The public website and the
   shared MCP address are not a personal screen link. Never invent an ID.
2. Use the supplied link as the `device` argument of `describe_device`,
   then `get_state`. The plugin already connects to `https://mcp.ecranpapier.com/`; the owner
   does not need to add another server for each screen.
3. On an invalid or unknown screen, explain the returned error and ask
   them to copy the personal page link again. Do not provision a screen,
   scan for identifiers or try a different device.
4. On success, confirm its name and summarize the current service and
   any preparation error in everyday language. Keep the name-to-link
   association in this conversation. Do not promise to remember it in
   future conversations: ask again when the link is unavailable. If several
   screens are known and the target is ambiguous, ask which one to use.
5. If the owner already requested an action, continue with that action
   using the bundled `wignet` skill. Otherwise offer examples such as
   “Affiche Bonjour pendant cinq minutes”, “Affiche cette photo” or
   “Mets la météo de Paris”. Setup itself only reads the screen.

The personal link grants control of that screen. Keep it out of public
documents, images and examples. Do not repeat its identifier unnecessarily.
Explain that prepared content appears at the next physical wake-up; a
successful server response does not prove it is already on the panel.

If MCP tools are unavailable, say the connection could not be checked and
refer to https://ecranpapier.com/support.html. Do not claim setup succeeded.
