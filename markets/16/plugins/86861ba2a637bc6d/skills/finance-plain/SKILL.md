---
name: finance-plain
description: Writes or rewrites finance text in Finance plain, a controlled style based on ASD-STE100 Simplified Technical English. Finance plain puts the answer first, uses short active sentences, gives every figure its unit, period and comparison base, states direction in words, uses points for changes in rates, puts three or more figures in a table, and cuts hedging. Use when writing or editing variance commentary, close or month-end summaries, board pack or investor update text, CFO notes, budget narratives, emails about numbers, or any reply that reports figures, even if the person only says "tighten this" or "make it clearer". Not for computing figures; run an analysis skill first.
---

# Finance plain

Given figures or a draft, produce text that a controller can forward without editing.

> Ground rules: `references/working-rules.md`. This skill has no scripts. Compute any missing figure with the calculator or another skill's script.

Finance plain takes three things from ASD-STE100: short sentences, one meaning per word and the active voice. These remove ambiguity from statements about numbers. It does not take the ASD-STE100 dictionary.

## Rules

| # | Do | Instead of | Why |
| --- | --- | --- | --- |
| 1 | Put the answer in the first sentence: "EBITDA is $4.62M for Jan–Aug 2026, $0.64M (12%) below budget v3." | Context first: "Looking at the data…" | Many readers stop after one sentence |
| 2 | One claim per sentence, at most 20 words, at most 4 sentences per paragraph | Clauses joined with "and", "which", "while", "however" | Each sentence must stay correct when quoted alone |
| 3 | Use the active voice. Choose one name per metric and keep it | "An increase in freight was observed"; revenue, then sales, then top line | Synonyms make readers think there are two metrics |
| 4 | Give each figure its unit, period and comparison base: "61.6% in September, down 0.2 pts on August" | "Margin is 61.6%" | A figure with no base cannot be checked |
| 5 | State direction in words: "$0.61M (1.7%) below budget". In tables, put adverse figures in parentheses: (610) | "A −1.7% variance" | Teams use different sign conventions |
| 6 | Give the difference between two rates in points: "fell 0.2 pts" | "fell 0.2%" | A 0.2% fall of 61.8% is 0.12 pts, a different claim |
| 7 | Put three or more related figures in a table: right-aligned, one unit per column, the unit and period in the header | Figures spread across a paragraph | Readers compare across rows and columns, not across sentences |
| 8 | Cut fillers, praise and closing offers. End with one concrete next step only when there is one | "It's worth noting", "overall", "Great question", "Let me know if…" | These words carry no information |

## Rewriting a draft

1. **Keep every figure exactly:** its value, its rounding and its sign. Add no figure that is not in the draft or computed from the files. Where the draft is missing a period or base, leave a gap for the writer: "[period?]", "[baseline?]".
2. **Find the answer** the draft leads up to and move it to the first sentence.
3. **Apply rules 2–8** in order.
4. **Keep the meaning.** Add no cause, judgement or recommendation. If the draft hedges because the cause is unknown, say that once: "The cause is not known yet."
5. **Check the length.** A rewrite is usually 40–60% of the original.

## Replacements

| Draft says | Write |
| --- | --- |
| came in at, landed at | is, was |
| slightly, notably, meaningfully | the amount: "$0.61M (1.7%) below" |
| approximately $35.6M, for an exact figure | $35.59M |
| was impacted | rose or fell, and by how much |
| headwinds, tailwinds | the cause, by name |
| YoY, MoM, in prose | on last year, on last month |
| in line with | within $X (Y%) of |
| going forward | from October 2026, next quarter |

## Output

- A headline sentence, then up to three short paragraphs, or one table with one or two sentences around it.
- Headings only when there are three or more sections.
- For an email: the subject line states the answer, the first sentence repeats it, then the detail, then one next step if there is one.

## Reference files

- `references/examples.md`: four worked rewrites (budget commentary, a close summary, a board pack paragraph, an email). Read it before your first rewrite in a session.
