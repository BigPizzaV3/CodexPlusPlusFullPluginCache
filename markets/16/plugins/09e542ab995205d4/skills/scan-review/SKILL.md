---
name: "scan-review"
description: "Review one scan: what changed since the last scan, which rivals gained, and the first thing to do."
---

# Scan review

Use this guidance to review one scan of a Frontmost AI project, to explain why a metric moved, or to write a team update.

## Steps

1. Call `get_scan` for the project and the scan in the request. It compares the scan with the previous scan.
2. Read the four KPIs: AI Visibility, Win Rate, Position, and Sentiment. Take each value, its counts, and its change.
3. Read the KPIs for each AI app. A change in the total usually comes from one or two AI apps. Name them.
4. Read the questions. List the questions that changed result since the previous scan, with the AI app for each.
5. Read the rivals. List the rivals whose mentions went up, with the counts for both scans.
6. Open the evidence before you explain a change. Copy the row's `answers_filter` into `get_answers`. Do not build a filter.
7. Choose the first thing to do. Use the scan's recommendations when it has them. If it has none, pick the largest gap: the questions where AI apps mention rivals and not the business.

## Rules

- Report each number with its counts, for example "22% · 8 of 36".
- A change needs two scans. If the scan has no previous scan, say that and report the current state only.
- Small counts are not a trend. A move of 1 or 2 answers is a move of 1 or 2 answers. Say the count.
- Give a cause only when the answers show it. If they do not, say "the data does not show why".
- Link the `url` of each screen that you describe.
- Do not promise a result. Each recommendation is a bet that the data supports, not a guarantee.

## Output

For a review, write three parts:

1. **What changed**: up to 5 points, largest change first.
2. **Who gained**: the rivals that gained, with counts.
3. **Do this first**: one action. Name the page or site, the action, and the reason in one sentence each.

For a metric question, write one short block for each metric that moved: the AI apps and the questions behind the move.

For a team update, write fewer than 150 words. Start with the largest change. End with the one action. Use no jargon.
