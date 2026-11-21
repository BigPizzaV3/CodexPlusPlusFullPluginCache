---
name: setup
description: Connect an existing Badger account, show the authorized app groups, and explain how to send a reasoned focus request. Use when the user starts Badger setup after installing this plugin.
---

# Set up Badger

1. Call `list_app_groups`. If account linking is required, let the host open Badger's OAuth sign-in. The user signs in in the browser and chooses the exact app groups to share. Never ask for a phone verification code or review password in chat.
2. If the user has no Badger account, direct them to download Badger: Your Willpower Agent from the App Store (https://apps.apple.com/us/app/badger-your-willpower-agent/id6817999408) and create one in the app first, then return to the host and connect.
3. Show the authorized group names. If none are available, explain how to create a group in Badger and reconnect with that group selected. Do not infer which apps are inside a group.
4. Give one example using an actual returned group name: “Block [group] while I work, because I need to focus.” Explain that each block or unblock requires a reason and that success means Badger accepted the request, not that the iPhone applied it.
5. Link to https://gobadger.app/connect for pause and disconnect. Finish setup without sending a control request unless the user has explicitly requested one.

For a later requested action, resolve the exact authorized group, preserve a previously established group for “block it” or “unblock it,” and include a concise reason based on the user's stated purpose. Ask when the group or purpose is genuinely unclear. Never invent a schedule, claim phone enforcement, or expose app membership/usage. Use a fresh idempotency key for each new request and reuse the same key and inputs after an ambiguous timeout.
