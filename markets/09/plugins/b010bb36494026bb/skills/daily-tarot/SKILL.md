---
name: daily-tarot
description: Create a personal Hunch tarot card of the day from a confirmed selfie and profile, with the complete reading. Use for daily cards and personal tarot questions, and to arrange recurring daily cards when the user requests them and the chat supports scheduling with Hunch tools and uploaded files.
---

# Daily Tarot

Use the Hunch MCP tools available in this chat. Card generation and readings come from Hunch; never fabricate a generated card, ticket or successful schedule.

## Find and confirm the details

Before asking questions, review the current conversation and use focused, authorised memory, previous-chat search or file-library tools only if the host actually provides them. Find the user's own name, date of birth, stated artwork preference, current question and chosen selfie. Do not claim access to unavailable history or files. Do not extract or infer a birthday, identity, gender, personality or private circumstances from a face. A selfie supplies the artwork reference, not verified profile facts.

Reuse the most recent unambiguous information. Resolve conflicting facts and ask which image to use when several are plausible. Ask only for missing required information. The current creation tool requires name, birthday, gender (woman/man, used as the confirmed artwork option), challenge and a host-resolvable selfie file. Explain the supported artwork options if needed; never silently choose one from appearance.

Present a short filled-in summary with name, birthday, artwork option, question/theme and selfie filename or preview. If no theme is known, propose “What should I pay attention to today?” as an editable default. Say “Hunch uses these details and your photo to create your personal card.” End with “Confirm or edit.” No separate processing-consent checkbox or repeated confirmation for unchanged details already explicitly approved. Pass only approved profile fields and the selected selfie, never the conversation history.

## Create and present one card

1. After confirmation call `hunch_prepare_card` once. Keep its ticket private and preserve it for this request's retries.
2. Call `hunch_create_personal_card` with the ticket, confirmed fields, `consent=true`, and a current host-provided selfie file reference. Allow the host to resolve the file to a fresh download URL. Never invent a URL or reuse an expired download link.
3. While it runs, show “Creating your card…”. The creation call waits for completion. Do not automatically poll or call `hunch_get_personal_card` after it.
4. On completion, show its single artwork widget and send the returned `message` verbatim as normal chat Markdown, preserving the entire reading and all emoji and formatting. The widget itself contains no reading.
5. For an interrupted/unknown result, retain the ticket and explain that creation is still unconfirmed. Check the same request only when the user asks. Never generate a replacement for an uncertain result. On an upload failure before generation, reuse the ticket with a refreshed authorised file reference. Honour quota/errors; do not create tickets to bypass limits.

When asked to reopen a card, use `hunch_get_personal_card` with the existing unexpired ticket and show its full reading. WhatsApp, Telegram and iMessage buttons transfer the same completed card; the user sends the prepared message or presses Start. Opening a button is not confirmed delivery.

## Offer or arrange daily delivery

After a successful first card, unless the user already declined or a schedule exists, offer once: “Would you like a fresh Hunch card here every day? What time and time zone?” Installing the plugin or requesting a single daily card does not authorise a recurring task.

If the user already explicitly requested daily delivery, use that authorisation. Ask only for missing time/time zone, and confirm reuse of the approved profile, selfie and daily theme as part of the setup if that reuse was not already requested. Do not infer a time zone from birth data or language. Do not add a second permission question when recurring use and timing are clear.

Use the host's actual scheduling tool, following its schema and permission requirements. Discover it if discovery is available; never invent a tool, a manifest schedule field or raw scheduling directive. Prefer a task in this same chat so the confirmed context remains accessible. Inspect existing tasks where permitted and update the matching Hunch daily task rather than creating duplicates. Do not create a local-desktop task as an undisclosed substitute for cloud delivery.

Before creating a generation schedule, establish that scheduled runs in this host can access Hunch and the approved uploaded selfie. A public image URL is not required: an authorised persistent upload whose download URL can be refreshed is suitable. Never put a temporary download URL, private card ticket or messenger transfer code in the saved schedule prompt. Keep the selfie in the approved chat/upload context; do not publish it or copy it to unrelated storage.

The scheduled prompt must explicitly invoke Daily Tarot and retain the following behaviour:

- Use the previously approved profile, artwork choice, selfie and recurring theme in this chat. Reuse that approval on later runs; do not request the same confirmation every morning. Use a general daily theme unless the user chose an ongoing question; do not silently reuse a stale sensitive question.
- Resolve the current date in the agreed time zone. Create at most one new card for that date. Review this task/chat's latest run result; if that date is complete, do not generate again. If a previous attempt for that date is pending or uncertain, retain its ticket and report the uncertainty instead of starting a replacement. Do not automatically poll. If run history/state is unavailable, ask for attention rather than risk a duplicate generation.
- A new date is a new user-authorised request: obtain a fresh ticket with `hunch_prepare_card`, then create once with a fresh host-resolved selfie reference. Tickets expire after 24 hours; never reuse yesterday's ticket for a new card. The current backend has no persistent ChatGPT identity or recurring subscription and enforces a shared generation limit. Do not promise unlimited daily cards or bypass a limit with another ticket.
- Return the completed artwork widget and full canonical reading to this chat. Do not send messages to external messengers automatically.
- If a required file, profile field, tool permission or entitlement is missing, do not guess or generate. Explain the missing prerequisite and ask the user to restore it. Respect cancellation and changes made through the host scheduler.

Only confirm scheduling after the scheduling tool reports success. State the daily time, time zone and where results will appear; distinguish a host-managed schedule from a Hunch subscription. Availability of device push/email notifications depends on the user's ChatGPT settings. Do not claim recurring generation is proven until an actual scheduled run has succeeded.

If scheduling, Hunch access or durable selfie access is unavailable, explain the exact missing capability. Offer a daily reminder to open Hunch as an alternative only with the user's acceptance; label it a reminder, not automatic card generation. If a scheduler rejects the setup, report the failure and do not claim success.
