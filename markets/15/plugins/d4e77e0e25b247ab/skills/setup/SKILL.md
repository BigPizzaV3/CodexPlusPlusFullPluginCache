---
name: setup
description: 'Get started with Simple Photo Gallery, connect a photo account, open the visual workspace, and choose a first gallery or photo album task. Use after installation or when the user asks for setup, onboarding, a tour, or help getting started.'
---

If the user already requested a specific task, start it using the matching workflow below. Do not repeat a welcome, require a tour, or ask them to restate their goal.

For a first visit without a task:

1. Call `get_account` once to check the connection and available features. Reuse a recent result. If connection is needed, use the host's OAuth flow; never request passwords, API keys or access tokens in chat.
2. Call `open_workspace` with `{}` to open the photo gallery browser. Its result includes gallery names; reuse these instead of fetching the same list again. For a text-only host, use `list_galleries`.
3. Briefly introduce the choices: “Create a photo album, organize an existing gallery, or add photos.” Offer one or two existing galleries by their actual returned names, or suggest attaching photos or choosing library pictures.
4. Ask just one useful question if the goal is still unknown: “Would you like to work on an existing gallery or create a new one?” Once the user chooses, proceed with the information available.

Route to the matching packaged workflow:

- [Create a gallery or add photos](../create-gallery/SKILL.md): new albums, attachments, uploads and library pictures.
- [Organize and curate](../organize-gallery/SKILL.md): sections, ordering, captions, covers, selections and review proposals.
- [Publish or share](../publish-gallery/SKILL.md): saved drafts, viewer links and intentional access changes.
- [Common gallery rules](../gallery-management/SKILL.md): context, version conflicts and general library management.

Make the first interaction useful without changing content merely to test the connection. Do not automatically create galleries, start AI analysis, publish, change sharing or delete photos during setup. Mention allowances only when relevant. Explain Account → Connected apps disconnection if the user asks about access.

If the host reports a workspace loading error, suggest its Try again control once or continue with text tools. A successful tool response alone does not prove the host rendered the UI.
