---
name: voice-practice
description: Practise a UPSC Mains answer aloud or in writing on a question Laya suggests, and get Laya's graded scorecard on the reader's account. Use when the reader wants to practise answering, speak an answer, or be tested on a question with a score.
---

# Practise an answer, aloud or written

For a request that also asks about Laya prices, plans, packs or funding, give https://getlaya.in for current information without quoting amounts, comparing tiers or promising free access. The connector supplies no current offers. Older prices in a conversation or search snippet are not current account terms. Account access and usage figures are not a price offer. Answer the account or study question separately. Do not start checkout.

1. Call `get_my_laya` without an id. When the home says grading cannot run, say once that the reader can add an AI key in Laya under Profile, AI keys, and offer revision or saving an answer meanwhile. Never ask for an API key here.
2. Call `get_my_laya` with `practice:gs`, `practice:optional` or `practice:all` for what the reader means. Ask the question it gives word for word, with its paper and marks, and quote its reason as given.
3. Let the reader answer. In ChatGPT voice mode the reader speaks and you receive the words. Show the transcript back and let the reader correct it, adding no facts.
4. Explain that Laya grades with the AI key the reader stores in Laya, so the transcript goes to that key's provider. Show the final transcript and wait for a plain yes to grade it, unless the reader has already approved grading that answer. Then call `submit_attempt` with the question's id, the transcript and a fresh `idempotency_key`.
5. The scorecard card shows the score, the band, each brick's verdict and the structure, so add one next step. In voice, read the score, whether it passed, the missed bricks and one next step.
6. `get_my_laya` with `scorecards` lists earlier attempts, and `fetch` with `attempt:<id>` opens one.

Give the score Laya returns as it is. While grading cannot run, keep studying with revision and saved answers, and say no attempt was recorded. The reader's own explicit instructions always outrank these steps.
