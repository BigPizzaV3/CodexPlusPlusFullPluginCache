---
name: youtube-connect
description: Connect, reconnect, or add YouTube channels to Windsor.ai and resolve which connected channel a request means. Use when the user wants to connect a channel, asks what is connected, or hits a permission error. Do not use for analysis or exports.
---

# Connect YouTube channels

Help the user connect, reconnect, or add a YouTube channel to Windsor.ai (connector id `youtube`), and resolve which connected channel a request refers to.

## Stay in scope
- Use this skill when the user wants to connect a channel, add another one, reconnect after a permission error, or asks which channels are connected.
- For analysis use $youtube-insights; for recurring exports use $youtube-export.

## Workflow
1. Call get_connectors with include_not_yet_connected=True to see whether `youtube` has connected channels.
2. For a connection, call get_connector_authorization_url for a ready-to-open setup link (YouTube uses Google sign-in), or get_connector_connect_info for the auth details. Hand the user the link and tell them to authorize with the Google account that owns or manages the channel.
3. Never ask the user to paste tokens or passwords into the chat, and never describe manual dashboard navigation instead of giving the link.
4. After they finish, call get_connectors again and confirm the new channel by name.

## Channel resolution
- If a request names a channel, match it to a connected account id. If several channels could match, ask which one before any read.
- A permission error on a read usually means the Google account lacks access to that channel; reconnect through the same setup link with the right account.

## Support
- get_windsor_login_url gives an auto-login link into the Windsor.ai dashboard; get_current_user shows who is signed in; contact_windsor files a support or feature request. Never discuss plans or pricing.

## Answer with evidence
State which channels are connected, which are not, and the exact next step with its link.
