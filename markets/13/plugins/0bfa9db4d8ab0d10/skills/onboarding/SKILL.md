---
name: onboarding
description: Welcome the user to KeptInFlow in ChatGPT, check that their PC is reachable, and show them their recent saved items when they choose Set up or ask how to get started.
---

# Set up KeptInFlow

KeptInFlow is a Windows app. This plugin reads what it saved on the user's PC:
recorded meetings, copied text and snips, notes, and text seen on screen.

1. Call `list_recent_items` with `{}`. This checks that the PC answers and
   shows the user their newest items.
2. If it answers with items, tell the user in one or two sentences what they
   can ask, for example "What did we decide in my last meeting?" or "Find the
   link I copied yesterday."
3. If it answers with nothing saved yet, explain that items appear once they
   record a meeting, copy or snip something, or write a note in KeptInFlow.
4. If it answers that KeptInFlow isn't running on the PC, ask them to open
   KeptInFlow on the PC and try again. If it says ChatGPT access is turned
   off, point them to Settings, ChatGPT in KeptInFlow.

Keep it short. If they installed the plugin in the middle of a task, go back to
that task after step 2.
