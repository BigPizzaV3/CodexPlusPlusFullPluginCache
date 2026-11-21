---
name: my-esims
description: Use when the user asks about or wants to manage the Gjirafa eSIMs they already have, such as "show my eSIM", "how much data is left?", "when does my eSIM expire?", "rename my Germany eSIM", "did my gift arrive?" or "remove the gift I never paid for". Reads them with list_my_esims, get_my_esim and list_sent_gifts, and changes them with rename_my_esim and remove_unpaid_gift.
---

# The user's own eSIMs

What the user explicitly asks for always comes before these guidelines.

## 1. Find the eSIM

- Call `list_my_esims` with `language` set to the user's language.
- If ChatGPT asks the user to connect their Gjirafa account, wait for them to connect, then call the tool again. Don't ask for an ICCID, an email or an order number instead.
- If the user means one eSIM ("my Germany eSIM"), pick it from the list. If several match, ask which one.

## 2. Answer

- For "how much data is left" or "how many days", answer from the list: `remainingGb` of `totalGb`, `remainingDays` of `totalDays`. Unlimited plans have no GB figures.
- For package history or the exact expiry date, call `get_my_esim` with the `esimId`.
- When `lowData` is true, say the data is running low. If the user asks what they can do, the eSIM's page on Gjirafa Travel (`manageUrl`) has the options; don't push them to buy more.
- When the status is `not_installed`, say the eSIM hasn't been installed yet; the install steps and QR code are on the `manageUrl` page and in the Gjirafa eSIM app.

## 3. Changes

- **Rename**: `rename_my_esim` with the `esimId` and the new name (up to 40 characters) changes the label only; the plan and data stay the same. Use the name the user gave; don't invent one. If they haven't said a name, call it without one: ChatGPT shows them a form to type it. If the result says forms aren't available, ask them for the name.
- **Gifts**: `list_sent_gifts` shows the eSIMs the user gifted (recipient's first name, destination, data, whether it was paid and sent). `remove_unpaid_gift` removes a gift that was never paid. Ask the user to confirm first; paid gifts can't be removed.
- If ChatGPT asks the user to allow changes, wait for them to allow, then call the tool again.
- The widget has the same buttons. If the user renames or removes something there, the widget tells you; don't repeat it.

## 4. Installing, topping up, credits

- ChatGPT can't install, activate or top up an eSIM, and never shows the activation code. Give the `manageUrl`.
- For installation help, or an eSIM that doesn't connect or is stuck on Activating, call `get_esim_help` with the `troubleshoot` or `install` topic and walk the user through its steps in order; the `manageUrl` page has this eSIM's QR code. When the status is `not_installed`, start with installing; when it's `active` but there's no internet, start with the troubleshooting steps.
- `get_my_travel_credits` gives the Travel Credits balance and tier; `get_credit_history` explains how they were earned or spent.
- Emails and SMS from Gjirafa Travel (newsletter, offers, review requests, reminders): `get_email_preferences` shows them, `set_email_preference` turns one off or on.

## Rules

- Only talk about eSIMs and gifts the tools return; don't guess usage.
- Quote data as the tools give it, and say usage can lag by a few minutes.
- For a plan for a new trip, use `choose-esim-plan` instead.
