---
name: connect-telegram
description: Set up or troubleshoot the user's Telegram connection to Telepath — Telegram Connector, then return to their original request. Use for plugin setup, explicit connection questions, missing Telepath tools, Unknown tool errors, or authentication errors. An empty search alone is not a connection failure. Not for administering Telepath or developing its integrations.
---

# Connect Telegram

Help the user complete the missing step in their language. Follow explicit user instructions over workflow defaults. Assistant sign-in and Telegram Chat Automation are separate connections; completing one does not prove the other works.

## Check assistant access

If Telepath tools are available, use `telegram_list_chats` or the read tool needed for the user's original task. Returned chats establish archive access, not necessarily an active live Telegram connection.

If tools are missing, require authentication, or return `Unknown tool` / `Tool not found`, explain that the assistant cannot currently access the Telepath tool. A loaded skill or installed plugin does not prove sign-in is complete. The error alone does not establish whether Telegram Chat Automation is connected or whether the archive is empty. Use tools exposed by the current host; do not invent tool names or namespace prefixes, or repeatedly call the unavailable tool. An empty plugin-search result is not proof that an installed plugin is absent.

When the user has not completed sign-in, give both setup steps together, in their language:

1. Open the installed Telepath — Telegram Connector plugin's connection settings and complete **Sign in with Telegram**. If approval happens in Telegram on another device, return to the original browser and finish the connection there.
2. If private chats have not been connected, open **Telegram Settings → Chat Automation**, add **@lemma_telepath_bot**, choose chats and save. Then return to the assistant and try the original request again.

Do not send the user away with only “connect and retry”: include the steps above and offer https://telepath.lemma.company/start#telegram for device-specific help. Use only connection controls actually available in the host; do not invent menu paths or ask for login codes, tokens, or passwords in the conversation. If sign-in status is unknown, ask whether they completed it rather than claiming they did not.

After the user completes sign-in, retry one read using the currently available tools. If sign-in is confirmed but the tool is still unavailable, or `Unknown tool` persists, explain that tool access still fails and offer https://telepath.lemma.company/support. Do not repeatedly reconnect or remove a working account, and do not claim that changing Chat Automation will fix a tool-discovery error.

A timeout or server error is not proof of missing authentication. Explain the reported error; offer https://telepath.lemma.company/support if it persists. Do not repeatedly reconnect a working account.

## Check Telegram collection

If no chats are available, distinguish a missing connection from a connected account that has not received new messages yet. Use explicit status returned by tools if available; otherwise have the user check https://t.me/lemma_telepath_bot. Do not infer connection status from an empty archive.

When connection is needed, give the action directly: **Open Telegram settings → Chat Automation, add @lemma_telepath_bot, choose private chats, and save.** Use the same Telegram account used for sign-in. Telegram Premium is not required. Do not send the user to a guide page before explaining these steps.

Use the device already known from the conversation; do not ask for it again. For Android, iPhone/iPad, or Telegram Desktop, offer [Open Telegram settings](tg://settings/edit) when the host can render that link. It opens settings, not a completed connection: the user still selects Chat Automation, adds the bot, chooses chats, and saves. Do not claim the link works in every ChatGPT surface. If the link is unavailable, give the relevant manual path:

- Android: **Settings → Account → Chat automation**; tap **✓ (Done)** to save.
- iPhone/iPad: **Settings → Edit → Chat Automation**; go **Back** to save.
- Telegram Desktop: **Settings → ⋮ → Edit profile → Chat automation**; go **Back** to save.
- Telegram Web K: **Settings → Edit profile → Chat Automation**; save changes there.

If the device is unknown, lead with the short action above and ask which Telegram app they use only if they need help finding or saving it. Distinguish Telegram Desktop on Mac from the native Telegram for macOS app. For the native macOS app or Web A, use Telegram on a phone or [Web K](https://web.telegram.org/k/) with the same account to finish setup, then return to the usual app.

If the settings link or manual path fails, the menu is missing, or the user wants screenshots, offer https://telepath.lemma.company/start#telegram as the fallback device guide. Do not repeat the same failed path indefinitely.

If already connected, preserve that connection. New messages from selected chats become available after connection while it is active. Older messages do not arrive automatically. Import is optional: the user can later send `/import` to the bot for a link and upload a Telegram Desktop JSON export from a computer. Do not make import a prerequisite for using new messages.

Discuss groups or channels only when relevant: groups need the bot added with message access; channels must be connected and authorized through the bot.

## Reach a useful result

Return to the original request as soon as access works. For an explicit setup request without a prior task, verify access with a small read-only call and show a brief useful result, unless the user asked only for instructions. This does not authorize sending messages or other changes. Report empty results accurately and explain the next step without inventing messages or claiming all Telegram history is connected.
