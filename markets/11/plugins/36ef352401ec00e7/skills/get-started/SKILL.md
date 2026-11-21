---
name: get-started
description: Check the Data2Bids connection after installing the plugin, show the user's bid projects and suggest a first question about them.
---

# Get started with Data2Bids

Use this right after the user installs or connects the Data2Bids plugin.

1. Call `projects_list` to confirm the connection and see which bid projects the user's company has in Data2Bids.
   - If the call asks for sign-in, tell the user to connect their Data2Bids account and try again. Do not ask for passwords or tokens in the chat.
   - If the list is empty, explain that projects are created and documents uploaded or synced on www.data2bids.com, and that the plugin can only read projects that already exist there.
2. Show the projects as a short list (name and, if present, owner or location). Do not show internal IDs unless the user asks for them.
3. Suggest one or two example questions that fit their projects, for example:
   - "What insurance limits does the <project> bid require?"
   - "When are bids due for <project>, and where are they delivered?"
4. Remind the user once that the plugin is read-only: it answers from the documents already processed in Data2Bids and cannot upload, edit or delete anything.

Answer in the user's language.
