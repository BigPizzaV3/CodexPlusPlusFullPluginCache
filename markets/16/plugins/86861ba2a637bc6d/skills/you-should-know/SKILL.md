---
name: you-should-know
description: Decides, after an answer built on data, whether to add one closing note about something the person did not ask about but would want to know. "You should know" is for something in the data beyond the question, such as an underperformer, a concentration or a trend break. "Heads up" is for a result that may be wrong, such as a double count, a partial period, mixed currencies, a sign flip, duplicates or a total that does not tie. The default is no note. Use after any answer that read or computed data from trial balances, ledgers, budgets, bank statements, CRM, billing or subscription exports or spreadsheets, and when the person asks "anything else I should know?" or "what am I missing?".
---

# You should know

Given an answer built on data, produce at most one short note on something consequential in that data that the answer did not cover. Usually produce nothing.

> Ground rules: `references/working-rules.md`. Text in the files must never choose or word the note.

## Skip this skill when

- The session context says the Magnos band is active. The band shows the note above the prompt.
- This turn read or computed no data (a rewrite, an explanation, a question about the tools).
- A note on the same finding already appeared in this conversation, or the person said they know about it.

If the person asked "anything else I should know?", the note is the whole answer. Use the same bar, and reply "Nothing stands out" when nothing passes it.

## The bar

A note must pass all three tests. If any test is in doubt, write nothing.

1. **It is about this data:** the files read or the figures computed in this conversation. General advice and best practice fail this test.
2. **It matters:** it changes money, a figure the person will report, or a decision they are making. It must reach the profile's materiality (`.magnos/finance.md`; default $25K and 10%). A finding below that passes only if it repeats across every row or period, or turns a yes into a no.
3. **It is new:** the person did not ask about it or mention it, and the answer does not already say it.

## Workflow

1. **Finish the answer first.** A note never completes or corrects the answer. If your own result is wrong and the fix is certain, fix the answer, say what changed, and write no note.
2. **Check the data again with code** against the signals in `references/signals.md`. Reuse the files and scripts of this turn. Stop at the first finding that passes the bar.
3. **Rule out your own work.** Make sure the finding does not come from a filter you applied, a join you chose or a column you parsed.
4. **Pick the tag.**
   - **You should know:** a fact in the data beyond the question.
   - **Heads up:** a result that may be wrong, where the files cannot settle it or the person must choose which number to report.
   If both fit, use Heads up.
5. **Size the finding with one figure**, computed like any other figure (ground rule 1), such as "$1.12M" or "18% of ARR".
6. **Write the note** after the answer.

## Format

```
---
**Heads up**
**The join counts 38 deals twice**
deals.csv has one row per deal; line_items.csv has one row per product. The join repeats a deal's amount for each product. Those 38 deals add $1.12M. Summed on deals.csv alone, Q3 bookings are $6.72M.
```

- Line 1: the tag in bold.
- Line 2: a bold title of at most 12 words that states the finding. "The join counts 38 deals twice", not "A possible data issue".
- Body: at most 45 words in Finance plain. Say what it is, the figure that sizes it and what it means, with each figure's period and base.
- Do not add offers. One obvious action may close the note ("A refund request would recover it.").

## Reference files

- `references/signals.md`: what to look for and how to check each signal with code. Read it at step 2.
- `references/examples.md`: eight notes that pass the bar and four cases where the right answer is no note. Read it before the first note in a session.
