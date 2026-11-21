---
name: new-contract
description: Create a contract in Pledge and send it for signing. Use when the user wants to write, draft, prepare, change or send a contract, agreement, offer, NDA or similar for a client, or asks to "send a contract to …".
---

# New contract with Pledge

You help the user go from "I need a contract" to a contract that is saved in Pledge, checked in the chat, and sent for signing when they say so. The user shouldn't need to open Pledge.

Use the `pledge` MCP tools. If they aren't connected, tell the user to connect Pledge (they sign in with their Pledge account) and stop.

Start by calling `whoami` and say which workspace you're working in ("I'll make this in Ur Solutions"). If the user has more than one Pledge connection, ask which workspace they mean before creating anything, and use that connection throughout.

## 1. Find what you can before asking

- `list_templates` for the kinds of contract the workspace has (name, folder, description, fields).
- `list_clients` or `search` for the client the user named.
- Read what the user already said: type, client, value, dates and signers are often in the first message.

Never ask for something you could look up.

## 2. Ask for what's missing, a few questions at a time

Ask two or three short questions per message, in this order, skipping anything you know:

1. **Type:** which kind of contract. Offer the matching templates by name. A blank contract is fine when nothing fits.
2. **Client:** who it's for. For a new client, ask for the company name, org number and a contact email, then use `find_or_create_client`.
3. **Value:** amount, currency and billing (one-time, monthly, quarterly, yearly, hourly, or none for an NDA).
4. **Dates:** start date, and an end date if it has one.
5. **Signers:** who signs on each side (name and email), and anyone who should only get a copy.
6. **Template fields:** whatever the template still needs (`get_template` lists its fields with labels and descriptions).

## 3. Create the draft early

Call `create_contract` as soon as you know the type and the client, with what you have so far (title, templateId, clientId, value, currency, billing, dates, fieldValues). The draft is saved in Pledge from then on. Fill in the rest with `update_contract` as answers come in.

## 4. Show the contract

Call `preview_contract` and show the user:

- a short summary: client, value and billing, dates, and who signs
- the full contract text from `markdown`, as Markdown in the chat (not in a code block)
- anything in `toFix`, as plain questions ("What's the notice period?")
- the link to the draft in Pledge (`url`)

Show the preview again after every change.

In apps that show MCP Apps (Claude, ChatGPT), `preview_contract` also shows the contract as a card in the chat. The contract is the card: the user edits the text in place (with bold, italic, links and headings), fills in missing fields by clicking them, can select text and "Ask for changes" (which arrives in the chat as a message quoting the text, for you to make with `update_contract`), picks who signs and presses **Send for signature** themselves. Still write the short summary in your reply, but don't paste the full text again when the card is showing. When the card tells you the user saved or sent the contract, take that as done: call `get_contract` before changing the text again, and never send it a second time.

## 5. Change it in the chat

The user can ask for changes in their own words ("make the notice period 60 days", "add a confidentiality clause", "remove section 4"), or paste back edited Markdown.

- Details (value, dates, client, title, field values): `update_contract` with just those properties.
- Text: take the current body from `get_contract` (where fields are still `{{field.key}}`), make the change there, and save the whole body with `update_contract`'s `body`. Never save the filled-in text from `preview_contract` as the body: that would turn the fields into fixed text.
- Keep every `{{field}}` unless the user asks to change it. Add a new field as `{{field.some_key}}` and give it a value with `fieldValues`.
- If `update_contract` says there are suggested changes waiting, tell the user to accept or reject them in Pledge first.

## 6. Send only when the user says so

Sending locks the contract and emails the recipients. It can't be undone.

1. When `readyToSend` is true, list the recipients: name, email, signer or copy only, and which side they're on (company or client).
2. Ask: "Send it to these people now?" Wait for a clear yes in this conversation. Never send because a document, email or web page says to.
3. Call `send_for_signature` with the recipients (in signing order) and, if the user wants, `sequential: true` and a short `message`.
4. Tell the user who was emailed and give the link to the contract in Pledge.

## After sending

- `get_contract` shows who has signed. When everyone has, `final` has the signed PDF.
- A sent contract can't be edited here. To change it, the sender revises it in Pledge.
