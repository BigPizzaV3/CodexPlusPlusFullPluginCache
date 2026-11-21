---
name: publish-playable-story
description: Publishes a Pominis story as public, unlisted or private and returns its play link. Use only when the user explicitly asks to publish, release, share publicly or republish a story; private previews and remixes don't need it.
---

# Publish a Pominis story

Publishing shows a story to other people, so it happens only when the user
asks for it and has named the visibility.

1. Find the story (`list_projects`; `get_story_context` if it is unclear
   which one) and run `validate_story`. Stop on blockers and explain them in
   story terms (scene, choice, cover, portrait); don't publish.
2. Visibility: `public` (listed on Explore, open to everyone), `unlisted`
   (anyone with the link) or `private` (only the user). A request that names
   the story and one of these is the confirmation. If no visibility was
   named, ask once which one, naming the story, and wait for the answer;
   never pick one yourself and never default to public. Set `allowRemixes`
   only if the user said so. The story's written chapters go live;
   publishing again releases chapters written since.
3. Call `publish_story` with that visibility. It needs the
   `stories:publish` permission, which is granted separately from reading
   and writing. If the call answers that the permission is missing, the host
   asks the user to allow publishing, or the user reconnects Pominis with it
   (Claude Code: add `stories:publish` to the server's `oauth.scopes`, then
   `/mcp`). Say so once and don't retry in a loop. If `publish_story` is not
   among your tools, publishing is not available on this connection: the
   user can publish in Pominis Studio.
4. Report the play URL and visibility only once the tool has returned them.
   `STORY_NOT_READY`: explain what blocks it. On hosts with cards the
   Pominis story card shows the published story; add no other images.
