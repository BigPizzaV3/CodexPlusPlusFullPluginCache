---
name: get-started
description: Show what Roar AI can do and start a first job. Use when the person sets up the Roar AI plugin, asks what they can do with Roar AI, or asks how to get started.
---

# Get started with Roar AI

Tell the person what Roar AI does in a few lines, ask one question, and get them to a first result.

## 1. Find out where they are

Call `get_started`. It returns what Roar AI is (`about`), what this account already has (`account`), what to do about the account's name (`setup`), and the question to ask (`next.ask`).

## 2. Say what it does, then ask one question

In two or three short lines, in your own words, say what `about` says. Then ask `next.ask` exactly as `get_started` returns it. The wording can change, so always use the one in the response.

Ask nothing else, and do not turn it into a list to pick from. Do not ask for the person's name or their company's name as a separate step.

If `account.apps` is more than zero, add one line saying they can also ask you to change an app they already have.

## 3. Save the business name from their answer

Follow `setup`. If the workspace has no name yet and the person tells you what their business is called, save it with `set_up_account` (`company`). If they are on their own and give their name, pass it as `fullName`. Use only a name they told you. If they gave no name, carry on and do not ask for one.

If `set_up_account` says the account is already set up, carry on. Do not try again or try another way to rename it.

## 4. Build what they asked for

- If they described a business and nothing else, build a one-page website for it.
- If they described a thing they want, build that.
- If they already have an app, put it online.

Keep a first app small, so it goes live in this chat, and share the live link. The `build-and-change-apps` skill has the steps.

## Keep it simple

- Short messages, plain words. The person may not be a developer.
- No prices, credit or offers.
- One question at a time, and only what the job needs.
