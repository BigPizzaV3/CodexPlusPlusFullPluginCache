---
name: ss33-skill-store
description: Finds a proven step-by-step procedure in the SS33 Skill Store (about 60,000 skills written by practitioners and organisations) and follows it. Use before producing a plan, schedule, procedure, document, configuration or code in a specialised area, such as legal, finance, tax, healthcare admin, trades, animal care, home, data, security or a library you are unsure of, where house rules, standards or exact numbers matter. Not for chat, one-line answers or work the open project already explains.
---

# SS33 Skill Store

The SS33 Skill Store is a library of about 60,000 skills: step-by-step
procedures with the rules, numbers and common mistakes for a task. Hundreds
are Verified, meaning they were tested on blind questions and measurably
improved a model's answers. The store is reached through three tools:
`search_skill_store`, `get_skill` and `report_skill_outcome`.

## When to search

Search when the task needs knowledge you may not have exactly right:

- A document, plan or procedure in a professional field (a lease clause, a
  payroll run, a medical billing change, a building quote).
- A schedule or care plan where specific numbers matter (feeding, dosing by
  weight, training loads, planting dates).
- A configuration or code task for a tool, API or standard you are unsure
  of, or one newer than your training.

Skip the search for casual conversation, one-line facts, translation, and
coding work the project's own code and docs already explain.

## Steps

1. **Search.** Call `search_skill_store` with `query`: one or two sentences
   describing the task in plain words, for example "Write a job quote for a
   kitchen remodel with materials, labour, markup and a deposit schedule".
   Pass `area` when one fits: Software Development; AI & Agents; Data &
   Analytics; Security; Business; Finance & Markets; Betting & Prediction
   Markets; Legal; Health & Life Sciences; Creative & Media; Science &
   Education; Personal & Home.
2. **Choose.** Read each candidate's summary and why it matched. Prefer a
   Verified skill that fits the whole task. When the search says nothing
   fits (`found` is false), carry on without a skill.
3. **Fetch.** Call `get_skill` with the chosen `ref`. Read the SKILL.md and
   any supporting files it points to.
4. **Follow it.** Use the skill's procedure, rules and numbers, adapted to
   the user's situation. Tell the user which skill you used, by name.
5. **Report.** After the work is done, call `report_skill_outcome` with
   `worked` (true or false) and short `notes` on what helped or what was
   missing.

## Privacy

Send only a short description of the task. Never paste the user's whole
message, names, contact details, account numbers, health details or other
personal data into a search.

## Limits

No account is needed. Searches are limited per conversation (30 a minute).
A skill whose licence does not allow it to be shared comes back with a link
to its author instead of its text.
