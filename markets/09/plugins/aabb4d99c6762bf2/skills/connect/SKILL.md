---
name: connect
description: Connect a new social media account to PostZen (X, Instagram, TikTok, LinkedIn, Facebook, YouTube, Threads, Pinterest, Bluesky, Telegram) or review/disconnect existing connections.
---

# Connect a social account to PostZen

Walk the user through linking a social account so posts can target it. The user's request follows: "$ARGUMENTS"

## Workflow

1. **Show current state.** Call `listAccounts` and summarize what's already connected (platform + username) so the user doesn't double-connect.
2. **Start the connection.** Call `createConnectUrl` for the requested platform. Give the user the returned auth URL as a clickable link and tell them to open it in their browser, sign in to the platform, and approve access. Do not try to complete the OAuth flow for them.
3. **Finish and verify.** The browser callback completes authorization. After the user says they have approved, call `listAccounts` again. Never request or exchange authorization codes in chat. Check the resulting account's `status` — not just that it appears. Potential pitfall:
   - A `connected` status proves auth, not publishing. If the user is connecting because publishing failed, suggest a quick test post (a draft, or a real post they confirm) to exercise the publish path. Sometimes users will forget to approve all permissions requested by the platform's OAuth flow.
4. **Platform-specific follow-ups:**
   - **Pinterest**: after connecting, a default board should be selected — use `listPinterestBoardsForSelection` and `selectPinterestBoard` (or `createPinterestBoard` for a new one). The board-selection window is time-limited, so do this right after connecting.
   - **Bluesky**: uses an app password rather than OAuth — direct the user to the connect URL, where they'll paste an app password generated in their Bluesky settings. Never ask the user to paste the app password into this chat.

## Disconnecting

`disconnectAccount` removes a connection. Confirm with the user first — scheduled posts targeting that account will no longer be able to publish.

## Cautions

- Never ask for or handle the user's social media passwords, app passwords, or tokens directly; the browser-based connect flow is the only path.
- If a connection repeatedly fails, point the user to the PostZen dashboard (https://app.postzen.dev) where the same flow exists with more error detail.
