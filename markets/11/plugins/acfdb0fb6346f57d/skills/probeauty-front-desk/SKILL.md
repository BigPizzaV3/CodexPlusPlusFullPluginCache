---
name: probeauty-front-desk
description: Use ProBeauty AI to manage a beauty professional's schedule, find appointment openings, look up clients and visit history, book or change appointments, and send payment requests.
---

# ProBeauty AI front desk

ProBeauty AI is booking and client software for independent hair stylists, nail techs, lash artists, estheticians, and small salons. Use its existing remote MCP tools for these workflows.

## Workspace and time

- Always call `list_workspaces` first. If the professional has more than one workspace, ask which one to use unless their request makes the workspace obvious. Do not call other tools until the workspace is resolved.
- Interpret all dates and times in the selected workspace's timezone. Resolve relative expressions such as "tomorrow", "Thursday", and "next week" against the current date in that timezone. Ask when the intended date is ambiguous.
- Send appointment times as `YYYY-MM-DDTHH:MM` in the workspace's timezone, with no offset. Do not substitute the chat or device timezone.

## Read workflows

- Use `get_schedule` to see appointments.
- Use `search_clients` and `get_client` to identify a client and retrieve their available history. Ask which client is intended when results are ambiguous.
- Use `list_services` to resolve the service and its returned duration and available provider information. Never invent identifiers or tool arguments; follow the live tool schemas.
- Client phone numbers, email addresses, birthdays, and notes are private. Show these details only when the professional asks for them. Avoid unrelated private details in schedule summaries and confirmations.

## Availability and writes

- Before `create_booking` or `reschedule_booking`, call `find_availability` for the intended workspace, service or duration, provider, and date range using the live schema. Offer real open times returned by the tool. Never guess a slot or assume a requested time is available.
- Before any write, confirm the client, service, provider, date, and time in one short sentence and obtain the professional's confirmation before executing. Resolve missing or ambiguous details first. For cancellation, confirm the existing appointment; for a payment request, confirm the associated appointment details and amount in the account's currency.
- Client texts for bookings are set by the professional's connection, not by you. When **Let it text your clients** is on, `create_booking`, `reschedule_booking` and `cancel_booking` text the client automatically; clients who opted out are never messaged. Never promise or rule out a text before the write. Each result includes `client_notified` and a `note`; report what actually happened. If the professional asks for a text and the result says it was not sent, pass on the note.
- `create_payment_request` has a `send_text` option that defaults to true. Say in the confirmation that the link will be texted, and set `send_text` to false only if the professional says not to text.
- Payment amounts are in the account's currency, which the server applies. Pass `amount` as a plain number such as "45" or "45.50" with no symbol. Do not ask for a currency or convert amounts; the result shows the formatted amount, so report that.
- If any write tool reports that booking changes are off, tell the professional to turn on **Allow booking changes** for ChatGPT on the **ChatGPT & Claude** page at https://app.probeauty.ai/. Do not retry that write.
- Report success only when the tool confirms it. Explain failures briefly without inventing a completed booking, change, text, or payment request. A sent payment request does not mean payment was received. Return the actual link for payment on the ProBeauty AI page; payment happens outside ChatGPT, by card through Stripe as a direct charge on the professional's Stripe Connect account. If the tool says payment requests are not available in the country yet, explain that message without inventing a link or retrying.

## Example requests

- Who's on my schedule tomorrow?
- Find me an opening for a 90-minute balayage next week.
- Move Maya's Thursday appointment to 4 pm and text her the new time.
- When did Sofia last come in, and what did she get?
- Send Maya a $45 payment request for today's gel fill.
