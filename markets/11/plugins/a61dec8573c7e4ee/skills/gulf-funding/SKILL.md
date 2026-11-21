---
name: gulf-funding
description: Answer questions about startup funding in the six GCC countries (Saudi Arabia, UAE, Qatar, Kuwait, Oman, Bahrain) from GulfPitch's verified map — accelerators, VC funds, grants, government programmes, angel networks, corporate VC, loans, and published application deadlines.
---

# Gulf startup funding with GulfPitch

Use the GulfPitch tools when a user asks about funding, accelerators, investors,
grants, government programmes or application deadlines in Saudi Arabia, the UAE,
Qatar, Kuwait, Oman or Bahrain, or about entering one of these markets as a
founder from abroad.

## Which tool

- `search_gulf_funding` — the question names a need, a country, a type, a stage,
  a sector, or a condition (open now, no equity, open to founders from abroad).
  Combine filters; put sector words such as "fintech" or "climate" in `query`.
- `get_gulf_programme` — the question names one programme or funder. Pass the
  name as the user wrote it; the tool also accepts the GulfPitch id or page slug.
- `gulf_deadlines` — the question is about what closes soon. No arguments.

## How to answer

- Every entry returns the month it was last checked and its page on
  gulfpitch.com. Keep both in the answer: name the check month once, and link
  each programme to its gulfpitch.com page.
- Quote terms as the tool returns them — amount, equity or not, who can apply,
  status. Do not round, convert or complete a figure the tool leaves out; a
  missing figure means the organisation has not published one.
- When a result does not fit a filter the user asked for (for example a
  programme that matches the sector but not the stage), say so instead of
  presenting it as a match.
- For founders from abroad, give the programme's own condition and quote
  (`from_abroad_condition`, `from_abroad_quote`) rather than a summary of it.
- The data covers the six GCC countries only. For other countries say that
  GulfPitch does not cover them; do not guess.
- The tools are read-only. GulfPitch cannot apply, submit, or contact a
  programme on the user's behalf; point to the application link instead.
- This is information, not advice. Do not recommend a programme as the one the
  user should choose or promise an outcome; set out what each programme
  publishes and let the user decide.
