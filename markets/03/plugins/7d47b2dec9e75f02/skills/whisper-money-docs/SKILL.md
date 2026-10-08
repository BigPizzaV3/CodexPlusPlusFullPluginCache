---
name: whisper-money-docs
description: Read Whisper Money's product documentation before answering how the app works — how accounts, imports, categories, automation rules, cashflow or budgets behave, what a feature does or does not do, pricing, privacy and which banks connect. Use when the user asks a "how does Whisper Money…" or "can Whisper Money…" question instead of answering from memory.
---

# Whisper Money documentation

Every page is served as Markdown by appending `.md` to its URL. Fetch that
version — it is the same content without the page chrome.

## The pages

| Topic | URL |
| --- | --- |
| Getting started | https://whisper.money/documentation/getting-started.md |
| Accounts, connecting a bank | https://whisper.money/documentation/accounts.md |
| Transactions | https://whisper.money/documentation/transactions.md |
| Imports (CSV and friends) | https://whisper.money/documentation/imports.md |
| Categories | https://whisper.money/documentation/categories.md |
| Automation rules | https://whisper.money/documentation/automation-rules.md |
| Cashflow | https://whisper.money/documentation/cashflow.md |
| Budgets | https://whisper.money/documentation/budgets.md |

Add `?lang=es` for Spanish: `https://whisper.money/documentation/budgets.md?lang=es`.

## Anything else

`https://whisper.money/llms.txt` is the index of everything public — the product
summary, roadmap, privacy policy, terms, the list of banks and apps that can be
connected, and the comparison pages. Fetch it first when the question is not
covered by the table above, then fetch the page it points at.

## How to answer

- Read the page before answering. These pages change; memory does not.
- Answer from what the page says, and link it (the human URL, without `.md`) so
  the user can read the rest.
- If the docs do not cover it, say so rather than inferring. The roadmap page
  is where "not yet" lives.
