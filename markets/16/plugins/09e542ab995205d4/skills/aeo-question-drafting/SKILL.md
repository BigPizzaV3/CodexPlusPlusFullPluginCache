---
name: "aeo-question-drafting"
description: "Draft, audit or expand the questions tracked in a Frontmost AI project. Review branded and unbranded questions, intent clusters and buyer phrasing. Add questions only after approval."
---

# AEO question drafting

Use this when someone wants new tracked questions for a Frontmost AI project, wants the current set reviewed, or asks whether their questions are good. The goal is a question set that measures discovery honestly and gives a realistic chance of a first unbranded mention.

## What the research says (keep these in mind throughout)

- The same prompt almost never returns the same brand list twice. How often a brand appears is stable; its rank is not. (SparkToro and Gumshoe, Jan 2026)
- One run of one prompt is close to uninformative. Use several wordings per intent and read results over a rolling 2 to 4 week window. (University of St. Gallen preprint, Apr 2026)
- Rewording barely changes results while the meaning stays close. Format matters more: list-style and short keyword prompts surface roughly 20 to 25 percent more brands. A changed qualifier (budget, location, team size, named rival) is a new intent. (Peec AI study, Jun 2026, vendor-sponsored)
- Judge clusters of prompts, not single prompts, and keep branded and unbranded separate. (Ahrefs guide)
- Nobody outside the AI companies has reliable data on what people actually ask. Say so. Never present a drafted question as a known real query.

## Step 1: Read the current set

Call `list_projects`, then `get_questions` for the project (and `get_scan` with `include_branded: false` for the unbranded split). For each existing question, note:

- Scope: branded (names the project's brand) or unbranded.
- Buying stage: early research, comparing options, or ready to buy.
- Format: list ("best X"), short keyword, "what do X recommend", problem-first, persona, comparison, or alternatives-to.
- Qualifiers: budget, team size, location, platform, named rival.

Flag weak questions, with evidence from saved answers:

- Ambiguous: answers drift into another product category. Check which business each answer named first.
- Unwinnable: the question asks the AI to choose among a closed list of named rivals, so the brand can never be named. Useful for rival intelligence, but it adds guaranteed zeros to the unbranded count.
- Off-target: aimed at a buyer the business does not sell to.
- Monoculture: most questions share one format or one stage.

Do not reword, pause or remove anything in this step.

## Step 2: Gather real phrasing

Use, in this order:

1. `get_sources` with `include_branded: false`: titles of the cited list articles and the cited Reddit threads. Thread titles are real people asking.
2. `get_rivals`: the most-named rivals, for "alternatives to" and comparison questions.
3. `get_queries`: the web searches ChatGPT ran. Treat as weak evidence, because they mirror the questions already tracked.
4. Anything the person supplies: Search Console questions, support chats, sales calls, forum threads.
5. The business's own differentiators (price point, integrations, method). Verify each one before using it. Do not claim "cheapest" or similar unless checked.

## Step 3: Draft

Defaults, unless the person says otherwise:

- Ratio: about 3 unbranded to 1 branded.
- Stage mix for unbranded: roughly 25 percent early research, 50 percent comparing options, 25 percent ready to buy.
- Organise by intent cluster. Give important intents 2 to 4 wordings in different formats.
- Always include the plain head term in list format ("What are the best <category> tools right now?"). It is the format that surfaces the most brands.
- Include the category's own vocabulary (for AI visibility: AEO, GEO).
- One "alternatives to <rival>" question per top rival not already covered.
- A few questions built on verified differentiators. These are where a first mention is most plausible, but do not promise it.
- Branded set: what it is and who it is for, one comparison per top rival, a trust question ("is it legit, are there reviews"), "alternatives to <brand>", and pricing.

Wording rules:

- Write the way a buyer would type it. Plain, first person where natural.
- Unbranded questions never contain the brand name.
- State the category unambiguously. If a phrase could mean another product category, add the words that pin it down.
- One intent and at most one qualifier per question.
- Never ask the AI to pick among a fixed list of rivals in an unbranded question.
- No year in the question, no leading claims, keep it under about 25 words.
- No accidental near-duplicates. A deliberate cluster variant must differ in format, not just in a word or two.

Check every draft against the examples in `references/aeo-question-drafting-examples.md` before presenting it.

## Step 4: Present for approval

Show one table: question, scope, topic, stage, format, cluster, and what it is based on (cited thread, cited article, rival data, differentiator, or judgment). Then state:

- How many questions the project and the plan will have after the change.
- That the unbranded denominator changes, so day-over-day comparisons break on the day they start.
- Which drafts rest on evidence and which are judgment.
- Any weak existing questions found in step 1, as a separate recommendation.

Do not add anything yet. A question about whether you can add them is not permission.

## Step 5: Add, only on an explicit go-ahead

- Add in one `edit_questions` batch with a topic for each.
- Rewording an existing question pauses the old wording and starts new history. Only do it when asked, and say what it costs.
- After the next scan, confirm each new question was sorted as branded or unbranded correctly. Fix a wrong one with `branded_override`.
- Report the new totals and when the first results arrive.

## Step 6: Reading the first results

- Report total, branded and unbranded visibility together, each with counts.
- Compare the original questions separately from the new ones for at least a week. A drop in branded visibility after adding branded questions is usually the mix changing, not a decline.
- Compare formats separately (list against list, persona against persona).
- One day is a first read. Draw conclusions from a rolling 2 to 4 week window.
- Look for what the new questions reveal beyond the score: brand confusion with a similarly named company, trust gaps, new cited pages that do not list the brand.
- If unbranded visibility is still zero, say so plainly and point to the leading measures: cited pages that list the brand, and answers that cite those pages.

## Required examples

Before drafting, read the bundled `references/aeo-question-drafting-examples.md`. Read its examples and source links. Stop if the file is unavailable.
