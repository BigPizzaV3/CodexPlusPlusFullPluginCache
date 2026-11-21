---
name: store-readiness
description: Use when a store owner asks whether their store or products show up in ChatGPT or other AI shopping assistants (AI visibility), how to get recommended by ChatGPT, or why an AI assistant shows a wrong price, stock, variant or link for their products. Works for Shopify and WooCommerce stores.
---
# Store readiness for AI shopping assistants

1. If the merchant gives a store address and confirms they own or manage it, call `check_store` with `user_owns_or_manages_store: true`. If ownership is not confirmed, ask first; never assume it.
2. If the result status is `running`, wait a few seconds and call `get_check_result` with the returned `check_id`.
3. Report the counts (critical, needs review, passed, not testable) and the top findings with their fix, in the merchant's language. Say that items that could not be tested are neither passed nor failed, and that causes are probable unless proven.
4. For general questions, call `find_guides` with the merchant's topic and language, and link the most relevant guide.
5. Never claim a problem in a store without evidence from a check. The check is read-only: nothing is changed in the store and no order is placed.
