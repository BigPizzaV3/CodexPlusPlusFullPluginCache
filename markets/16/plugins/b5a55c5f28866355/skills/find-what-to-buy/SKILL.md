---
name: find-what-to-buy
description: "Ask Deal.ai's shopping agent what to buy: it researches the request and recommends picks with each one's best store price. Use for 'best X under $Y', 'what should I get for...', and follow-ups that narrow the picks."
---

# Find what to buy

## How to run it

1. Call `ask_deal_ai` with the user's request in their own words, including budget, must-haves and who it's for. Don't rewrite it into keywords.
2. It waits about 20 seconds. If the answer isn't ready, it returns `running` with a `search_id`: tell the user Deal.ai is researching (answers take about 1 to 3 minutes) and call `get_deal_ai_answer` with the `search_id` every 15 to 20 seconds until it's done.
3. Give the agent's recommendation in a few lines, then each pick: name, why it was picked, its best store price with when it was seen, and its store link. Keep any store-link notes at the end.
4. For a follow-up ("cheaper ones?", "only Sony"), call `ask_deal_ai` again with the same `search_id` and the follow-up in the user's words.

## Rules

- If the agent asks a question back, ask the user the same question, then pass their answer as a follow-up.
- Don't add picks or prices the agent didn't return.
- One question at a time in a conversation: wait for the last answer before a follow-up.
