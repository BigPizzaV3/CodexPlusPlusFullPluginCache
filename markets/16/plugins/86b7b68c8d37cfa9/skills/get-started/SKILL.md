---
name: get-started
description: Help a new Satcat user connect their Satcat account and choose a first workflow. Use when the user runs Satcat setup or asks how to get started with Satcat or what it can do.
---

Use this skill when the user runs Satcat setup or asks how to start using Satcat.
Explicit user instructions take priority over this skill.

1. Call `satcat_capabilities`. If ChatGPT asks the user to connect Satcat, tell
   them to sign in with their Satcat account and approve the requested access,
   then call it again.
2. Summarize only the workflows the result marks as available, in plain
   language, with up to three of its example prompts.
3. Ask which workflow the user wants to try first, then follow the Satcat tool
   descriptions for that workflow.

Do not ask the user to share passwords, access tokens or one-time codes in the
conversation; account linking happens only through ChatGPT's sign-in prompt.
Do not describe Satcat website features that `satcat_capabilities` does not
list as available, and do not guess the user's location. When a workflow needs
observer coordinates or dates, ask for them.
