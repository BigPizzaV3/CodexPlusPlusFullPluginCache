---
name: ask
description: Ask Louvain, the person's company memory, a question and show the checked answer with its sources.
---

Ask Louvain the person's question, on their behalf.

1. If no question was given, ask the person what they want to know, and stop.
2. Call `louvain_ask` with `question` set to the question as written. Use `mode: "thorough"` only if the person asked for everything or for completeness.
3. Present the answer.
   - Keep each citation next to the sentence it supports, as a numbered reference.
   - Below the answer, list the sources it cites by title.
4. Follow the rules for reading a Louvain answer:
   - **Refused** (`refused: true`): say that nothing the person can see supports an answer, then list what `findings` does establish. Do not ask again in other words.
   - **`inferred`**: if present, add it after the answer under "Suggested, not verified".
   - **`last_known`**: give the value with its date.
   - **`retrievalDegraded`**: add that the search was cut short, so the list may not be complete.
5. Offer to open any cited source with `louvain_read_source`.
