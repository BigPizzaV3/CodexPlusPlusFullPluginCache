---
name: review-site
description: Review one RankYak site, with the articles that RankYak wrote lately, the content plan for the next two weeks, the keyword research that waits for approval, and the decisions that wait on the user. Use it when the user asks for a review, a status update, or a weekly check-in of a RankYak site, or asks what needs their attention in RankYak.
---

# Review a RankYak site

Use this skill for a periodic review of one site. The review reads the state of the site and lists the decisions that wait on the user. The review changes nothing.

An explicit instruction from the user takes priority over this skill. For example, the user may ask for a different time window or for one part of the review only.

## Input

The user may name a site by its name or its domain. The user may give a time window. Without a window, review the last 14 days and the next 14 days.

## Steps

1. Call `list-projects` and choose the site.
    - When the user named a site that is not in the list, say that the connected RankYak account does not hold that site. Name the sites that it holds. Stop.
    - When the list holds more than one site and the user named none, ask which site to review.
2. Call `get-recent-activity` for what RankYak did lately and for `setup_gaps`, which lists what holds the site back.
3. Call `list-articles`, and keep the articles that RankYak created in the window. For each article with `error_at` set, call `get-article` and read `publish_error`.
4. Call `get-content-plan` with `from` set to today and `to` set to the end of the window.
5. Call `list-keyword-research`. Collect each run with status `in_review` and the clusters that it proposes.
6. Call `list-money-page-suggestions` for the pages that wait for an answer from the user.
7. Call `get-site-audit`. When `has_site_guard` is true, call `list-page-audits` if `fixes_ready` is above zero, and call `list-cannibalization-issues` if `open_cannibalization_issues` is above zero.

Skip a step that the user's request does not need.

## Output

Write at most 300 words, in this order:

1. Recent articles: the title and the state of each article. The states are published, generating, failed to publish, and changed after the last publish.
2. Coming up: the planned articles in date order, with the date and the keyword of each.
3. Waiting on you: each decision, with the action that settles it. Put first the items that stop publishing, such as a failed publish or a missing CMS. Then list the research runs to review, the article changes to publish, the money page suggestions, and the Site Guard fixes.
4. One question that offers to act on the first decision.

When a part has no items, say so in one sentence.

## Facts not to infer

- Report only the titles, keywords, dates, states, and numbers that the tools return.
- Do not guess why a publish failed. Quote `publish_error`, or say that the CMS gave no reason.
- Do not report a change in traffic when Google Search Console is not connected.
- Do not count an article as published unless `published_at` is set.

## Stop or decline

- Change nothing during the review. Do not approve research, publish an article, plan a keyword, or apply a fix. When the user asks for one of these, handle it as a new request after the review.
- When a tool returns an error, show the error message in the part of the review that needed the tool. Do not fill that part with a guess.
