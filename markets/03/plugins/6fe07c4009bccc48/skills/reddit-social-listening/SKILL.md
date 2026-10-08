---
name: reddit-social-listening
description: Find and respond to Reddit conversations relevant to a brand. Use for social listening, monitoring subreddits, finding threads worth replying to, drafting a Reddit comment, or managing listening keywords. Do not use for publishing articles or for AI visibility reporting.
---

# Reddit social listening

Find conversations where the brand is genuinely relevant, and draft a reply worth posting.

Every tool here is scoped to one brand and takes `brand_id`.

## Step 1: resolve the brand

Call `list_brands`. If more than one, ask which. Keep `brand_id` for every later call.

## Step 2: check what is being listened for

- `manage_reddit_keywords` shows and edits the terms being monitored.
- `reddit_settings` shows the current configuration.
- `search_subreddits` finds communities worth monitoring for a topic.

If nothing is configured, agree the keywords and subreddits with the user before scanning.

## Step 3: get opportunities

Call `list_reddit_opportunities` for threads matching the brand's keywords.

`trigger_reddit_scan` looks for new ones. This takes time, so only run it when the stored results are too old for the user's purpose.

`get_reddit_stats` summarises volume over time.

## Step 4: judge relevance before drafting

Most threads are not opportunities. Before drafting anything, check that the thread is one where the brand has something genuine to add.

Reject a thread when:

- The question is already answered well.
- The brand is only tangentially related.
- The subreddit forbids self promotion. Check the rules.
- The thread is old enough that a reply will not be seen.

Say plainly when a batch contains nothing worth replying to. An honest "none of these are worth it" is more valuable than five forced replies, which read as spam and damage the brand.

## Step 5: draft

Call `generate_reddit_comment` for a thread worth answering.

Review the draft before showing it. It must answer the question asked, and it must read like a person rather than marketing copy. If the draft only works as an advert, discard it and say the thread is not a fit.

Use `update_reddit_opportunity` to record that an opportunity has been handled or dismissed.

## Boundaries

- These tools draft comments. They do not post them. Never tell the user something has been posted. Hand them the draft and let them post it themselves.
- Never present a draft as ready without saying it is a draft for their review.
- Disclosure matters. If the comment recommends the brand, the reply should make the affiliation clear. Most subreddits require this, and undisclosed promotion gets accounts banned.
- Do not draft replies at volume across many threads. That is the pattern Reddit treats as spam.
