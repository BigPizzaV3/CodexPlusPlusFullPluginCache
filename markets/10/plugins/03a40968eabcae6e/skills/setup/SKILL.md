---
name: setup
description: First run after installing monity.ai. Set up the user's first monitor for a page they care about and show them where the evidence and alerts appear.
---

# Set up monity.ai

Goal: within a couple of minutes the user has one monitor watching a page they actually care about, knows what will trigger an alert, and has seen where changes show up. Keep it short and conversational; ask one thing at a time.

1. Ask which page they want watched and what about it matters. Offer examples only if they hesitate: a product's price or stock, a job board, a policy or terms page, a competitor's pricing page, a release-notes page.
2. Call `list_monitors` and check whether they already watch that address. If they do, say so and show it with `get_latest_result` instead of creating a duplicate.
3. Turn what matters into a plain alert condition in their words, such as "price drops below $500" or "the size M option becomes available". Confirm it back to them in one sentence.
4. Pick how often to check from the page type: prices and stock every few hours, job boards and news daily, policy or terms pages daily or weekly, within what their plan allows (`get_account`). Say what you chose; they can change it.
5. Call `create_monitor` with the address, a short name, the condition as `notifyWhen` and the frequency. If the account has several workspaces (`list_workspaces`), ask which one before creating.
6. Show the saved monitor (the result is shown as a card) and explain in one or two sentences:
   - monity.ai keeps checking on its own schedule after this conversation ends, in its own cloud browser;
   - every check keeps a full-page screenshot and a full HTML copy of the page;
   - alerts arrive by email (the card and the result say to which address), not as a ChatGPT message, and the card shows what the schedule costs in credits;
   - the card shows the first check as soon as it has run.
7. Tell them they can open monity.ai from the sidebar to see every monitor and its history, or ask "what changed this week?" any time.

Do not ask for passwords, cookies, API keys or one-time codes. If a page needs a login or clicking through steps, say that setup happens in the monity.ai dashboard and offer the link from the saved card.
