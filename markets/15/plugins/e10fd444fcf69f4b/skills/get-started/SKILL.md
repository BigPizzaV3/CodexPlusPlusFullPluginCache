---
name: get-started
description: First steps after connecting Directify. Finds the user's directories, picks the one to work on and shows what can be done with it.
---

Run this once after the plugin is installed, or whenever the user asks what Directify can do here.

1. Call `list_directories`. Three outcomes:
   - It returns directories: continue with step 2.
   - It fails with an authentication error: tell the user to connect the Directify plugin (they are asked to sign in to their Directify account and click Approve), then try again.
   - It returns an empty list: the account has no directory yet. Point the user to https://directify.app to create one, then come back.
2. If there is exactly one directory, use it. If there are several, show their names and ask which one to work on. Remember the chosen directory ID for the rest of the conversation.
3. Call `list_categories`, `list_tags` and `list_custom_fields` for that directory so you know its structure before changing anything. For a multilingual directory also call `list_languages`.
4. Tell the user, in two or three sentences, what the directory contains (counts of listings, categories, tags, articles) and offer the most useful next actions:
   - add or update listings, including many at once from a pasted list or spreadsheet
   - write and publish blog articles and custom pages
   - organise categories, tags and custom fields
   - restyle the directory (colors, fonts, hero text, template) and screenshot the result

Keep the overview short. Do not change anything during setup unless the user asks.
