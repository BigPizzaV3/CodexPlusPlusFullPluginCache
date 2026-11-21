---
name: get-started
description: Show a RankYak user the site that RankYak manages for them, the state of that site, and the articles that RankYak writes next. Use it right after the user connects RankYak, and when the user asks how to start with RankYak, which sites RankYak manages, or what RankYak does for their site.
---

# Get started with RankYak

Use this skill to orient a user in their RankYak account. The user leaves with three facts: the site that RankYak manages, what holds that site back, and the next articles on its content plan.

An explicit instruction from the user takes priority over this skill.

## Input

The user may name a site by its name or its domain. The user may also name no site.

## Steps

1. Call `list-projects`.
    - When the list is empty, say that the account has no site yet. Tell the user to add a site in the RankYak app at https://rankyak.com. Stop.
    - When the user named a site that is not in the list, say that the connected RankYak account does not hold that site. Name the sites that it holds. Stop.
    - When the list holds more than one site and the user named none, name each site with its domain. Ask which site to start with.
2. Call `get-recent-activity` for the site. Read `coming_up` for the next articles and `setup_gaps` for what holds the site back.
3. When `coming_up` is empty, call `list-keyword-research`. Tell the user about each run with status `in_review`, because its clusters wait for their review.

## Output

Write at most 150 words, in this order:

1. The site: its name, its domain, and whether it is active.
2. What holds the site back, from `setup_gaps`. Leave this part out when `setup_gaps` is empty.
3. The next articles: the date and the keyword of each, at most five.
4. Two or three requests that the user can make next, such as a review of the site, a summary of an article, or a change to the content plan.

## Facts not to infer

- Report only the dates, keywords, titles, and numbers that a tool returned.
- Do not estimate traffic, rankings, or results.
- Do not say that an article is published unless a tool says so.
- Do not assume that a CMS or Google Search Console is connected. Report the state that the tools return.

## Stop or decline

- When a tool returns an error, show the error message to the user and stop. Do not call the tool again with guessed arguments.
- This skill only reads. Do not change a site, the content plan, or an article while it runs. Handle a request for a change as a new request.
