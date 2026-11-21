---
name: get-started
description: Start with V30 in ChatGPT — write a social post in your voice, edit it in the V30 panel, and schedule it after your confirmation.
---

# Get started with V30

V30 writes LinkedIn and X posts in the user's voice and keeps them on a calendar. Nothing is scheduled or published until the user clicks Confirm in the V30 panel.

1. Call `get_workspace` to see the user's plan, connected accounts and posting times.
2. To write, call `write_draft` with a brief (facts, audience, language, goal). Do not write the post text yourself. Then call `open_editor` with the new post ID so the user can edit it in the panel.
3. To change a draft, read it with `get_post` and call `revise_draft` with the requested change.
4. For an image or video the user shared in the chat, call `attach_media` with the draft's current revision.
5. To schedule, publish now or cancel a schedule, call `prepare_post_action`. Tell the user to check the account, time and text and click Confirm in V30. Never claim a post was scheduled or published before `get_post_action_status` shows it.
6. If no account is connected, say so. Never ask for passwords or tokens.
