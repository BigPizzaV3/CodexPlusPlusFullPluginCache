---
name: get-started
description: Set up Beste right after the plugin is connected. Check which sites the account already has and offer the next step, a new site or work on an existing one. Use when the person chooses Set up for Beste or asks how to start.
---

Help the person take their first step with Beste. Keep it short and warm, with no
jargon and nothing about how the connection works.

1. Call `list_websites` with `{}`.
2. No sites yet: say in one line that they can have a site in a few minutes, and
   ask what the business is. When they answer, follow the `new-site` skill.
3. One site: name it, and ask what they would like to do with it, offering three
   choices: change something on a page, review it for leftover demo content, or
   add another language. Follow `edit-page` or `review-site` for the answer.
4. Several sites: list them by name, one line each, and ask which one to work on.
   Then ask what they would like to do, as in step 3.

If they already said what they want when they installed the plugin, skip the
questions and continue that task with the matching skill.

Never publish during setup. Every change goes to the draft until the person asks
for it to go live.
