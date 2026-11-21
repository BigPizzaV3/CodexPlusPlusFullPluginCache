---
name: setup
description: Set up Pageform after the plugin is connected. Use when the user is approving the Pageform connection, has no workspace, or wants to upload documents and create a data room in this chat.
---

Follow the user's request. Use this skill to finish Pageform setup in the chat and to turn attached files into a data room.

Sign-in and connection approval happen on Pageform. Do not send the user through the Pageform website setup wizard. A user who already has a workspace skips setup and continues with the action they asked for.

1. Call `get_workspace`.
2. When the list is empty, call `create_workspace`. Use a name the user already gave. Ask for a name only when they have not given one. Pass `workspace_type` when the request already makes it clear: `startup`, `venture_capital`, `private_equity_family_office`, `mna_advisory`, `real_estate`, or `other`. Ask which type only when it is not clear. Pass `website` only when the user gave one. Use the returned `org_id`.
3. When there is one workspace, use it. Do not create another.
4. When there is more than one workspace, ask which one, then pass that `org_id`.
5. When the user attached files, call `upload_documents` with those files and the `org_id`. Omit `folder_id`. Do not ask for a folder upload or a zip. Continue when at least one file is stored and the user wants a room. Tell the user about a file that failed to store.
6. Call `generate_room` with the stored document ids and a `dataroom_type` that matches the request: `sales`, `product`, `real_estate`, `startup_fundraising`, `lp_fundraising`, `lp_portal`, `spv`, or `mna`. Ask which room type only when it is not clear. Do not start a room when no document was stored.
7. When the build returns, show the review: score, summary, gaps, and offers, plus the room link. Do not place or move a file until the user accepts that offer.
8. If a tool says the plan does not include an action, say that and stop. Folder structure, billing, and other workspace settings stay in the Pageform app.

Do not invent a workspace, document id, room id, or link.
