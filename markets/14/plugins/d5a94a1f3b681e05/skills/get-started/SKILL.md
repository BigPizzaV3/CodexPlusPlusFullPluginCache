---
name: get-started
description: Set up Conxt after installing it - confirm the connection works, show what is already in the user's memory, and explain how Conxt reads and saves memories. Use right after the plugin is installed, or when the user asks how Conxt works.
---

# Getting started with Conxt

Conxt is the user's memory across their AI tools: decisions, preferences,
coding rules, tool choices, workflows, open questions, and the people and
projects they work with. The same memory is read by every other AI tool
they connect to Conxt.

## Steps

1. **Check the connection.** Call `get_pinned`. If it answers, Conxt is
   connected. If it asks the user to sign in, tell them to finish signing in
   to Conxt and try again; do not continue until it works.

2. **Show what is already there.** Call `get_memories` with no filter and
   summarise in a few lines what kinds of memory the user has (for example,
   "9 decisions, 4 coding rules, 2 open questions") and two or three
   examples. If the memory is empty, say so plainly and suggest one thing
   worth saving, such as a current project and what it is for.

3. **Explain how it works, briefly.**
   - Before answering a question about the user's work, you look up their
     memory (`get_context`) instead of asking them to re-explain.
   - When they make a decision or settle a question, you can save it
     (`add_memory`), and it will be there in their other tools too.
     Ask before saving anything they did not ask you to remember.
   - Team memory: you can read a team's approved memories and propose new
     ones (`propose_memory`). A proposal has no effect until a person on the
     team approves it at conxt.dev; you cannot approve it.
   - They can see, edit or delete every memory, and see which tool read
     what, at https://conxt.dev/dashboard.

4. **Offer a first use.** Suggest one prompt that fits what you found, such
   as "What have I already decided about <their project>?"

## Rules

- Never save secrets, passwords, API keys or access tokens to memory, even
  if asked. Say why.
- Never claim a team memory is approved or in effect when you only
  proposed it.
- If memory and the conversation disagree, say which memory you used and
  when it was recorded, and ask which is current.
