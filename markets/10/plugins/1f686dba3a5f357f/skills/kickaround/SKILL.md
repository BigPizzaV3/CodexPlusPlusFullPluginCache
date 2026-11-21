---
name: kickaround
description: Get one verdict from several AI models on Kickaround. Use when the person asks for Kickaround in any form ("kickaround this", "Kickaround whether...", "kick it around", "run it by Kickaround") or asks for several AI models to discuss a question and give a verdict. Not for a kickaround in sport.
---

Use this skill when the person asks Kickaround a question.

1. Call `kickaround` with the question in the person's words, with the details they gave and any request about length or format. Pick `mode`:
   - `critique` to poke holes in a plan or draft
   - `research` to check facts on the web
   - `brainstorm` for ideas
   - `summarize` for the short version
   - `opine` otherwise (the default)
2. A run takes a few minutes. If the result says the run is still going, tell the person once, then call `kickaround_result` with the `thread_id` until it says the run is finished.
3. Start your reply with the verdict exactly as Kickaround wrote it, with the share link, the link to the full thread and the cost line. Don't reword or shorten it. Anything of your own goes after it.
4. For a follow-up on the same question, call `kickaround` again with the same `thread_id` once the run is finished.
5. If the account is out of credit, say so, and that credit is added on the Kickaround website. Don't try to buy credit or make a payment.

The person's own instructions come first: if they ask for something different, such as only the bottom line, do what they ask.
