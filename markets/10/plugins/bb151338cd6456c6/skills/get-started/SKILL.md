---
name: get-started
description: Set up Artil after it is installed. Listen for new messages, email the user a welcome, and tell them when they reply. Use when the user runs the plugin's setup or asks how to start with Artil.
---

# Get started with Artil

1. Call `status`. It gives your name, your addresses, and in `signedInBy` the user's email address.
2. If this chat can subscribe to events, subscribe to the Artil event `message.received`. When a message arrives, read it with `messages.read` and tell the user who wrote and what they want.
3. Send the user a short welcome email at `signedInBy` with `messages.send`, without asking first: say hello from your own address, sign it with your name, and ask them to reply. If `signedInBy` is empty, find the user among the members in `team.list`; if you cannot tell which one they are, offer them the members' addresses to choose from.
4. Tell the user you just emailed them, give your email address and phone number, and ask them to reply.
5. If you could not subscribe, ask the user to tell you when they replied, then find the reply with `messages.list`.
