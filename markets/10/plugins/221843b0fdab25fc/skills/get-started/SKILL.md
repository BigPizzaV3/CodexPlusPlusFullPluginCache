---
name: get-started
description: Set up meeloop after install. Confirm the connected meeloop account and show what the plugin can do. Use right after the plugin is installed or when the user asks how to start with meeloop.
---

Help the user confirm their meeloop connection and choose a first task.

1. Call `get_my_profile`. If it fails because the account isn't connected or a
   permission is missing, ask the user to connect meeloop (or reconnect and
   allow the missing permission). Then stop.
2. Greet the user by their display name and show their username, so they can
   check it's the right account.
3. Briefly list what you can do: publish or schedule posts with photos or
   videos, post stories, edit or delete posts, show post stats and story
   viewers, and update their name, bio or profile picture.
4. Say what you can't do: read or send direct messages, browse feeds, follow
   accounts, or like or comment on posts.
5. Offer two or three starting points, for example drafting a first post from
   something in this conversation, or checking how their latest post did.

Keep it short. Don't post or change anything during setup.
