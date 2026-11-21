---
name: youtube-hook-review
description: 'Score and improve the opening of a YouTube video with Prepublish''s audit_hook tool, sentence by sentence, then compare hook variants and pick the strongest. Use when the user shares an intro, hook, cold open, first 15 to 30 seconds, or first paragraph of a YouTube or Shorts script and asks "is this hook good", "rate my intro", "make my opening stronger", "how do I stop people clicking away in the first 30 seconds", "which of these hooks is better", or wants hook rewrites. Also use when the user wants a fast check of the opening before auditing the whole draft. Do not use for a full script (use the full audit) or for writing a brand new hook with no draft.'
---

# Review a YouTube hook

The opening is where a draft most often loses a viewer who has not yet decided to stay. This skill scores the opening lines with `audit_hook` and turns the result into a short, practical decision.

Read `references/tools.md` for the tool's exact inputs and outputs, `references/research-notes.md` before giving general hook advice, and `references/claims-and-limits.md` before describing what a score means.

## Inputs

- **The hook text, verbatim**: 10 to 5,000 characters. Best is the first 15 to 30 seconds of speech, which is roughly 40 to 90 words. If the user pasted a whole script, take only the opening lines up to the first section change, tell them which lines you are scoring, and offer a full audit afterwards.
- **Niche**: only if the user said it (for example "personal finance", "true crime", "coding tutorials").
- **Email**: only if the tool says the free anonymous hook check for the day is used. Explain first that Prepublish stores the address and may send a few follow-up emails with an unsubscribe link. Never invent one.

## Workflow: one hook

1. Call `audit_hook` with `hook_text` and, if given, `niche`.
2. Present:
   - `overall_score`, `grade` and the `one_sentence_verdict`.
   - A compact sentence table: each quote with its attention pull (0 to 10), curiosity gap (0 to 10) and payoff distance (near, mid or far), plus the `note` for the weakest sentence.
   - The `top_issues`, each with the quoted line and the `why`.
   - The `rewrites`, each labelled with its `style` and `why_works`. Keep them verbatim.
3. Recommend one rewrite, or a merge of two, and say which line of the original it fixes. If you merge or edit, label the result as your version.
4. Offer: "Want me to re-score your revised opening?" If yes, score the revised text once. Report the change honestly; a higher score is a better read of the text, not a promise of better performance.

## Workflow: compare several hooks

When the user has two to four candidate openings:

1. Score each with `audit_hook` separately (one call per variant; do not combine them into one text).
2. Show a comparison table: variant, score, grade, verdict, main issue.
3. Pick a winner and explain the deciding difference in one or two sentences, using the tool's notes.
4. If scores are within a few points, say they read about the same and let the user choose on voice and fit with the title and thumbnail.

Do not score more than four variants in one go; free checks are limited per day.

## Honest hook guidance

Use `references/research-notes.md`. In short:

- Prepublish's own studies found that speaking faster and reaching the point a few words sooner did not separate hits from flops. Do not tell users to talk faster.
- A concrete reason to keep watching, and delivering what the title promises, are better levers to discuss.
- Openings that begin with a greeting leaned toward flops in both studies; mention it as a pattern worth testing, not a rule.
- For small channels, topic and packaging usually matter more than the hook. Say so if the user is diagnosing a flop.

## Output format (no inline card for this tool)

```
Hook score: 58 (C). Verdict: <one_sentence_verdict>

| Line | Pull | Gap | Payoff | Note |
| "<quote>" | 6/10 | 3/10 | far | <note> |

Top issue: "<quote>": <why>

Rewrites:
A. (<style>) "<hook>": <why_works>
B. (<style>) "<hook>": <why_works>

My pick: B, because it fixes "<original line>" by <reason>.
This scores the text of the opening only; delivery, pacing of the edit and the thumbnail are outside what it reads.
```
