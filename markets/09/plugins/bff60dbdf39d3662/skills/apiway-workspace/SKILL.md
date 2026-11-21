---
name: apiway-workspace
description: Work in the person's Apiway account through the Apiway MCP tools — their Gmail, tasks and booking links, email marketing, Lead Transfer, Instagram Comment → DM automations, reports, the Apiway assistant's memory. Use when the person asks for anything in Apiway that is not building an app.
---

# Apiway workspace

The Apiway tools act as the person, on their own Apiway account. The tool descriptions say what each
tool does; this skill says how to use them well. Apps (App Factory) have their own skill,
`apiway-apps`.

## Show, or do

`open_apiway` opens the Apiway panel inside the chat — their apps with addresses, the newest gallery files
and the credit balance. Use it when the person wants to SEE their Apiway ("show my Apiway", "show my
apps"). Mail, tasks and dates are not in the panel: "what is on today", "what did they answer" are
`search_workspace` and the tools below.

## The person decides what leaves the account

- **Sending** (`send_email_message` with `action: "send"`, `send_telegram_message`,
  `send_discord_message`) and **deleting** (`manage_mail_folders` delete, `lead_transfer`
  delete_automation) need `confirm: true`. Set it only after the person said yes to that exact
  message or deletion in this conversation — show them the text and the recipients first. Without
  `confirm` the tool refuses and says so; that is expected, not an error to work around.
- Default to a draft: `send_email_message` with `action: "draft"` puts a draft in their Gmail;
  `propose_email_draft` returns the text without touching Gmail.
- A recipient Apiway protects is held for the person to send by hand — tell them that plainly.
- Comment → DM: a new automation is created switched off. Switching it on, and the link its DM
  carries, the person sets in Apiway (the tool returns the address) — do not claim it is live.
- Plans and payments change only in Apiway (`/app/account`); `mail_settings` billing_get only reads.

## Mail

- Start with `search_workspace` for anything that was said, agreed or assigned — it reads what Apiway
  already stored and returns links to the exact block. Use `search_mail` for the rest of the mailbox;
  put spellings of one name into one call (`queries`, up to 6) instead of calling again.
- `read_thread` opens a thread found by search. For a question the person answers often (prices,
  services), read their own most recent sent answer (`in:sent …`) — the newest answer wins.
- Cite results by the `url` they carry, unchanged. For counts ("how many unread") use
  `mailbox_stats`; "unknown" means still warming up — say so rather than guessing.
- A person's name is not a folder condition — find their address with `search_mail`, then
  `manage_mail_folders` add_rule with the address or the company domain.
- Project tools (`project_mail_rules`, `project_notifications`) take the project id; list
  destinations before attaching one, and never invent a Telegram chat id — pass on the `setup` text.

## Tasks and dates

`create_task` and `propose_email_draft` take the person's `time_zone`. Resolve dates yourself from
the conversation ("next Tuesday" is a date, not a question); a bare date becomes that morning.

## Email marketing

`extract_email_brand` on the exact page the email promotes, then `compose_email` with those fields
(it saves a draft and returns preview and builder links — give the person both). For a sequence:
`email_sequence` action=context, agree the plan with the person, then action=save; the sequence is
saved switched off — tell them where to switch it on (`editorUrl`).

## Lead Transfer

Start with `lead_transfer` overview. For a Telegram destination the person adds @Apiway_official_bot
to the group or channel as admin, sends /id inside that group and gives you the Chat ID it replies
with. A Google Sheets link goes in unchanged (its `#gid` picks the tab).

## Memory

`remember_instructions` without `instructions` returns the current layer; with `instructions` it
replaces the whole layer — read it, keep what is still true, then write the complete new text, and
pass `confirm: true` once the person agreed to the new text.
