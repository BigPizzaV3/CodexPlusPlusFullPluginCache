---
name: social-media-connect
description: Connect, reconnect, or add accounts for Instagram, Facebook Pages, TikTok, YouTube, LinkedIn Pages, Threads, and Google Business Profile to Windsor.ai and resolve which account a request means. Use when the user wants to connect a source or asks what is connected. Do not use for analysis or changes.
---

# Connect social media sources

Help the user connect, reconnect, or add an account for Instagram, Facebook Pages, TikTok, YouTube, LinkedIn Pages, Threads, and Google Business Profile to Windsor.ai,
and resolve which connected account a request refers to. Connector ids are instagram, facebook_organic, tiktok_organic, youtube, linkedin_organic, threads, google_my_business.

## Stay in scope
- Use this skill when the user wants to connect a source, add another account, reconnect after a permission error, or asks which accounts are connected.
- For analysis use $social-media-insights; for changes use the manage or create skill of this app.

## Workflow
1. Call get_connectors with include_not_yet_connected=True to see the seven sources and which have accounts.
2. For a connection, call get_connector_connect_info for the connector: it returns the auth type and a connect_url. For OAuth sources hand the user the connect_url and tell them to authorize. For manual sources, list the credential fields it names and give the connect_url so they enter them there.
3. Never ask the user to paste API keys, tokens, or passwords into the chat, and never describe manual dashboard navigation instead of giving the link.
4. After they finish, call get_connectors again and confirm the new account by name.

## Account resolution
- If a request names an account, match it to a connected account id. If several accounts could match, ask which one before any read or write.
- Write actions need write actions enabled for the account at https://onboard.windsor.ai/app/settings/account. If a write is refused for that reason, send the user there and retry after they confirm.

## Answer with evidence
State which sources are connected, which are not, and the exact next step with its link.
