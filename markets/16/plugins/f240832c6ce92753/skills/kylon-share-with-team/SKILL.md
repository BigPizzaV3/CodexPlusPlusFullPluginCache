---
name: kylon-share-with-team
description: Shares a result from this chat (a summary, plan, draft, decision or file) with teammates in a Kylon Room or thread, and mentions the people who should see it. Use when the user asks to share, send, post or forward this work to their team or to named colleagues. Not for creating a public link to this ChatGPT conversation or posting to social media.
---

Use this skill when the user wants teammates in Kylon to see something from this chat.

1. Call `get_connection_context` to confirm which workspace and person the connection acts as.
2. Decide what to share. Use the user's words; if they said "this", take the latest result in the chat. Do not add facts that are not in the chat.
3. Find the destination. If the user named a Room or thread, look it up with `read_rooms` (`list` with a `query`) or `search`. If they named people but no place, find them with `read_members` and pick the Room they share; ask when more than one Room fits.
4. Before posting, tell the user in one line where it will go and who will be mentioned, unless they already said both.
5. Post it:
   - Short content: `manage_messages` `send` to the Room, or `manage_threads` `reply` to an existing thread. Pass the people to notify in `mentions`.
   - Long content such as a plan or report: save it with `manage_files` `write` under the Room's path, then post a short message or thread that links the file and mentions the people.
   - A new discussion: `manage_threads` `create` in the Room with a clear first line.
6. Reply with what was posted, where, who was mentioned, and the link the tool returned.

Posting notifies people and can start an Agent in that Room. Never post to a Room or person the user did not choose. If the user only wants a ChatGPT share link or a social post, say this skill does not do that.
