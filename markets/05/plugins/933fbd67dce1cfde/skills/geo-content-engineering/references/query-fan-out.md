# Query fan-out coverage

Answer every sub-question of a complex prompt on one page, so the page serves as
a universal source donor.

## The mechanic

Systems like AI Overviews split a complex prompt into several sub-queries and
answer each separately. A page that covers many of those sub-questions in
standalone blocks gets pulled into the composite answer more than once.

## Rules

1. **Anticipate the expected questions.** Write adjacent topics as their own
   blocks or FAQ entries: price, risks, alternatives, step-by-step, common
   mistakes.

2. **"It depends" scenarios.** Build in conditions and decision trees: when each
   approach fits, with clear criteria. These blocks have above-average
   extraction value.

3. **Direct comparisons.** Set up "X versus Y" with named criteria, ideally as a
   real table (markup requirements in `semantic-html.md`).

4. **Questions as subheadings.** Each sub-question gets its own H2 or H3 question
   with a self-contained block underneath, per the chunking rules.

## Where the questions come from

Derive the sub-questions from the tracked prompt pool for the cluster (see
`measurement.md`), not from the author's internal logic. Do not invent alibi
questions.
