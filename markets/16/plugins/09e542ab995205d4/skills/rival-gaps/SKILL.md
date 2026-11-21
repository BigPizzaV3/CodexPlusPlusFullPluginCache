---
name: "rival-gaps"
description: "Explain why AI apps mention one rival more than the business, and what the business can truthfully match."
---

# Rival gaps

Use this guidance to explain why AI apps mention a rival, and to find what the business can match.

## Steps

1. Call `get_rivals` for the project and the scan in the request. The default order puts the most mentioned rival first.
2. Pick the first rival unless the person names one. Call `get_rivals` again with its `rival_id`.
3. Read the rival's page: the business and the rival on AI Visibility, Win Rate, Position, and Sentiment, with the gap, for each AI app and each topic.
4. Read the answers that mention the rival. Copy the `answers_filter` into `get_answers`. Read at least 10 answers, or all of them when there are fewer.
5. Count the points that the answers repeat about the rival. A point counts once for each answer. Report "in 7 of 12 answers read", not "often".
6. Sort each repeated point into one of three groups:
   - **You can match it now**: the same thing is true for the business, and the answers do not say it. The fix is to state the fact clearly on the business's own site and on the outside pages that AI apps cite.
   - **You can match it with work**: it is not true today. Say what must change. Do not write copy that claims it.
   - **Do not chase it**: it does not fit the business, or it is the rival's main strength.

## Rules

- Ask the person to confirm each fact about their business before you put it in the first group.
- Find where the rival's mentions come from. Call `get_sources` and look for cited pages that list the rival and not the business. Those pages are the outreach targets.
- The rival's own website is not a target. Read it only to learn the format and topics that work.
- Never suggest contact with the rival, and never suggest a claim about the rival that the answers do not support.
- Report each number with its counts. Link the `url` of the rival's page.
- Do not promise a result. Each step is a bet that the data supports.

## Output

Three parts: **Where the gap is** (the AI apps and topics with the largest gap, with counts), **What AI repeats about the rival** (up to 5 points, each with its count and one short quote), and **What you can match** (the three groups above, with one first action).
