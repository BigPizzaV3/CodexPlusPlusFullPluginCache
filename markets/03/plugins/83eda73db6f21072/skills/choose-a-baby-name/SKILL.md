---
name: choose-a-baby-name
description: >
  Guide expecting parents in choosing a baby name using NiceBabyName's Holistic Nameology
  ("Four Aspects") tools: gather preferences and the parents' first names, build a shortlist,
  compare the candidates against the book's four newborn criteria, and present each name's
  reading with its strengths and pitfalls. Use when someone is choosing or evaluating a baby
  name, or asks for a nameology reading of candidate names (also known in Persian/Arabic as
  علم اسماء, چرتکه اسم, or محاسبه طالع).
---

# Choose a baby name with the Four Aspects

Holistic Nameology reads a name — not a birthdate — and derives four aspects: Governing
Planet, Temperament, Rising Sign, and Rising Degree. Planet + Temperament describe the
**outer self** (personality); Rising Sign + Degree the **inner self** (life themes and
fortune). The method comes from the book "The Four Aspects" by Dr. Saadat Bagherigaleh; the
tables for interpreting every aspect — planet characters, temperament meanings, the
fortune element-pairs, and the book's naming process — are in
`references/four-aspects-reference.md`. Read that file before presenting readings. The
server resource `nameology://guide` carries the same method from the server side.

One rule above all (from the book): the reading uses the name the child will be **called in
daily life** — if the plan is a formal name but a different daily nickname, read the daily
name too.

## Step 1 — Gather context, one question at a time

Collect, in separate short turns (never as a questionnaire):

1. Is the baby a boy or a girl (if known)? Gender enables gender-specific notes — the book
   generally advises against Venus as Governing Planet for boys.
2. The parents' first names — the **mother's matters most** to the calculation (it drives
   Governing Planet and Rising Sign; the father's shapes Temperament and Rising Degree).
   Without them a reading is partial; say so if the user declines.
3. Candidate names they already like, or the style they want (culture/origin, first letter).
4. If the parents have a goal for the child, match it to a planet when discussing results:
   nurturing/newborn-best → Moon or Jupiter · leader → Sun · intellectual → Mercury ·
   fighter → Mars · commander → Saturn · artist → Venus (not boys).

## Step 2 — Apply the name-input rules (critical for correctness)

- **Persian, Arabic, or Islamic names** (for the baby OR a parent — e.g. Hossein, Zahra,
  Ali): pass them in **native script** (حسین، زهرا، علی). These are read exactly from their
  own letters. If the user typed a Latin transliteration, convert it to script yourself and
  show the script you used so they can correct it. Never send the Latin spelling — it would
  be misread through the sound-based path.
- **English/Western names**: pass the Latin name. These are read from their **sound**, so the
  pronunciation must be confirmed (Step 5).

## Step 3 — Build a shortlist

- If the user has candidates, use those (2–5 for a comparison).
- Otherwise call `search_names` with their filters (name prefix, gender, origin) and offer a
  handful of results, then let them pick candidates.

## Step 4 — Compare with `compare_names`

Call `compare_names` once with all candidates plus `mother_name`, `father_name`, `gender`,
and the conversation language. Interpret the result strictly:

- Each candidate's `book_criteria` shows the book's four newborn criteria with reasons:
  ① Moon or Jupiter Governing Planet, ② Fire or Air Temperament, ③ a Fire- or Earth-element
  Rising Sign, ④ good-or-excellent fortune. `holistic_score` = how many are met (0–4).
- The ranking already applies the book's order for ties; the engine's livelihood rating is
  only a final tiebreaker, never the reason a name wins. Do not re-rank by livelihood.
- If a name appears in `not_recommended` (Venus Governing Planet for a boy), do not present
  it as the pick; explain the book's reasoning gently.

## Step 5 — Confirm pronunciations before trusting sound-based readings

If the response sets `confirm_pronunciation`, show the `confirm_prompt` to the user — it
lists every sound-based name with how it was read and a link to hear it. If any
pronunciation is wrong, call the tool again with the corrected `pronunciation` /
`mother_pronunciation` / `father_pronunciation`, then continue from the new result.

## Step 6 — Present the comparison

- One short block per candidate: the canonical aspects line from `format` (for example
  "Sun, Air, Virgo Earth, 9° Taurus Earth"), which criteria it meets and misses (use the
  `reason` texts), and its `pitfalls`.
- Name the top candidate, but **never as simply "best"** — always state its downsides from
  `pitfalls_to_mention` alongside its strengths.
- If no candidate meets the planet criterion (common), say so and offer to widen the
  shortlist with `search_names` rather than overselling the least-weak option — the book's
  own advice is to discard misaligned names and keep looking.
- Explain aspects in the book's language (use `references/four-aspects-reference.md`): the
  planet's character, how the temperament tunes it, the Rising Sign as recurring life
  themes, and the fortune verdict from the Sign × Degree element pairing.
- The aspects are not the whole decision. When candidates tie or the user hesitates, bring
  in the book's other factors: meaning, family tradition, easy pronunciation, timelessness —
  and the book's warning that unusual spellings burden the child.
- Reply in the language the user is speaking; keep the reading concise and warm.

## Step 7 — Deepen on request

For the favourite name, call `get_nameology_report` to give the full single-name reading
(personality, fortune, meanings). The same input and pronunciation rules apply.

## Output requirements (always)

- Present this as a **traditional interpretive system** offered for reflection and meaning.
  Never call it scientific, never promise outcomes, and never claim a name determines a
  child's destiny, health, wealth, or success.
- Do not invent aspects, scores, or criteria that the tools did not return.
- If asked whether they are talking to a human, say plainly it is an AI.

## When NOT to use this skill

Daily horoscopes or birth-chart astrology (this method uses no birthdate), baby health or
parenting questions, and naming companies, products, or brands.
