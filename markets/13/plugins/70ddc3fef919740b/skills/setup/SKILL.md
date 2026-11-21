---
name: vibe-party-setup
description: Open Vibe Party and explain how to join the community chat.
---

Open Vibe Party with `vibe_party.open`. Explain that the live public Lobby is readable before signing in. Posting, buddies, private chats, uploads, and account actions require sign-in. The user selects Sign in in browser, signs in on Vibe Party's first-party website with email and password, Google, or GitHub, then selects Connect panel; never request passwords, authentication codes or session credentials in chat. Password entry and recovery codes stay on that top-level website. After approval, the panel connects automatically. Never ask the user to paste credentials, codes, or handoff links into assistant chat.

Tell the user that the Lobby connects people building with AI. They can add buddies with the plus button in the Buddies header and select an accepted buddy for a private conversation. Groups require two accepted buddies. Profile picture and status controls are at the top of the sidebar. Return sends a message on desktop when signed in. A signed-out draft opens sign-in; cancelling or completing sign-in preserves the draft without sending it.

The plugin opens the interface. It cannot read chats or send messages for the user. Do not claim that sign-in completed or that a message was sent without observing that result. If host rendering fails, report the observed blocker; do not replace native-host testing with a browser preview claim.

Account linking through the host is optional. It verifies the Vibe Party account but does not give the assistant access to chats, send messages, or sign the person into the chat interface. They can review and disconnect linked apps at https://vibeparty.dev/connect or through Connected apps in their profile. Never ask for credentials in chat.

Vibe Party does not need health records, biometric identifiers, payment-card details, government ID numbers, or login secrets for chat. Never ask for, echo, or forward those details to a tool. Remind users to keep them out of messages, uploads, profiles, and report explanations. Tools accept empty arguments only.
