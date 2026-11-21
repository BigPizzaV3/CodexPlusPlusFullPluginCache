---
name: setup
description: Set up the Wile plugin's OAuth connection and explain how work updates and feedback operate.
---

Check whether Wile's `post_context` tool is available. If it is missing, direct the user to connect the bundled Wile MCP in the host's connection settings. If `post_context` is available but `get_feedback` is absent, the connection may be BCC-linked; that alone is not a connection failure. Explain that feedback arrives separately and do not ask the user to reconnect solely to obtain `get_feedback`. Authentication runs through `https://api.wile.ai/mcp` and Wile's OAuth pages using the user's existing sign-in options. Do not ask for a password or token in chat, create another authentication method, or change the user's global MCP configuration.

Explain that sharing work sends the selected context to Wile, where the user's rules and daily video limit determine whether a video is created. Answers stay tied to the same work thread. Video processing is asynchronous, and an empty feedback list means no answer has arrived. Closed-session resumption requires Wile's separate BCC integration.

Offer a small factual sample update. Post it only if the user asks to send it. Do not post a synthetic update or consume feedback merely to check connectivity.
