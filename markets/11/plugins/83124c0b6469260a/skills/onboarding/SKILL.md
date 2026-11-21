---
name: onboarding
description: First-run setup for FieldDraft. Use the first time a user installs FieldDraft or when tools report that Jobber is not connected or the price book is empty.
---

# Getting FieldDraft ready

1. Call `list_quotes`. If it fails with an authentication error, the user needs to sign in when ChatGPT prompts them.
2. Call `search_price_book` with a common item for their trade (for example "panel" or "service call"). If it returns no items, tell the user to connect Jobber in FieldDraft settings (the tool error includes the link) and then run `sync_price_book`.
3. Offer a first draft: ask them to describe one job they quoted recently, in their own words, and call `draft_quote`.
4. Explain the two rules in one sentence each: prices only come from their price book, and nothing is sent to a customer without them pushing it from Jobber.
