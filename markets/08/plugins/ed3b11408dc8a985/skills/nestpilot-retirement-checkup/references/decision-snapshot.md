# Decision Snapshot

Use this after the widget reports a completed baseline or follow-up through model
context. The persistent widget remains the source of truth for full results.

Answer in the same four short parts in every host (ChatGPT and Claude say the
same thing — DES-0194 J3):

1. **Modeled result** — one sentence with the completed step's main outcome,
   naming the one assumption it depends on most.
2. **One trade-off** — the decision implication the completed result supports.
3. **One uncertainty** — the limitation most likely to change the result.
4. **Next step** — the one button the widget now offers, or the one question
   that continues; or say that the requested steps are complete.

Plain words: no raw keys, JSON or unformatted decimals, and no "FRA", "Δ" or
"HC Bridge" — the precise term may follow in parentheses. Never suggest
Medicare as a next step.

Do not invent values, summarize a step that has not completed, or call another
calculator from the conversation. If a calculation fails, say that no result
was produced and leave prior valid tabs intact.
