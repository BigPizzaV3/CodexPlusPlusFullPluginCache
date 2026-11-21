# Badger

Your iPhone app blocker. Manage screen time through chat.

This package connects to the production hosted Badger MCP at https://api.gobadger.app/mcp using OAuth and Streamable HTTP. OAuth configuration is declared in `mcp.json`. There are no secrets in this package.

## Connect

1. Install this package in a compatible plugin host, or add the remote MCP address in your agent's settings.
2. Continue to Badger's browser sign-in. Use your existing Badger phone number, then enter the verification code.
3. Select the exact app groups your agent may control, then choose **Allow and connect**.
4. Ask: “Show my Badger app groups.” Then say which group to block or unblock and why, for example: “Block Distracting Apps because I need to focus on writing.”

Create your account and app groups in Badger first. Download [Badger: Your Willpower Agent on the App Store](https://apps.apple.com/us/app/badger-your-willpower-agent/id6817999408). Manage, pause or disconnect agents at https://gobadger.app/connect.

## What success means

`accepted: true` means Badger durably received the request. It does not prove your iPhone applied it. Group discovery exposes only authorized group names and opaque IDs; app membership, usage, phone state and Badger conversation contents remain private. A reason is required for each request. After an ambiguous timeout, retry the same inputs with the same idempotency key.

The three tools work conversationally in compatible MCP clients. This package provides no custom in-chat UI or form. The host manages any action confirmation.

This package is prepared for submission. Public directory approval and publication are separate steps.
