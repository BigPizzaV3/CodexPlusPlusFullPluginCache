---
name: release-drafting
description: Draft teem changelog entries and Help Center articles from what shipped, and publish them when asked. Use when someone wants release notes, a changelog entry, a help article, or to tell customers something is live.
---

# Release drafting

Everything in this workflow starts as a draft. Drafts stay inside the team. Publishing is a
separate step that happens only when the person says "publish".

## Find what shipped

1. Call `list_posts` with `status: "shipped"` for requests the team marked shipped.
2. Call `list_changelog` to see what's already written. An entry with `status: "published"` is
   live; `status: "draft"` isn't. Its `posts` list shows which requests it covers.
3. Requests that shipped but appear in no entry are the ones to write up. Call `get_post` on each
   for the details and the customers' own words.

## Write a changelog draft

1. Write for customers: what they can do now and where to find it. Name the request it answers.
   No internal names, tickets or code.
2. Call `create_changelog_entry` with `title`, `body` and the request ids in `post_ids`. The
   result has `status: "draft"`.
3. Show the person the title and body and say it's saved as a draft in teem's changelog.
4. To change a draft, call `list_changelog` first, check the entry is still a draft, then call
   `update_changelog_entry`. On a published entry, a title or body edit goes live at once: say
   so and confirm before you call it.

## Publish

- Call `publish_changelog_entry` only after an explicit "publish". It marks the linked requests
  shipped and emails everyone who voted on them. Before you call it, add up the `votes` on the
  linked requests and say how many people will get the email.
- Publishing is safe to retry: teem never sends the same announcement twice.

## Help Center articles

1. `create_help_article` saves a new draft. Nothing goes public.
2. To edit an article, call `get_help_article` right before `update_help_article` and pass its
   `revision` as `expected_revision`. A revision conflict means someone else edited it;
   read it again and show the person what changed.
3. `get_help_article` returns the editable draft and the current publication side by side.
   Customers see only the publication. Say which one you're quoting.
4. Use `preview_help_article` to show how the Markdown renders, without saving.
5. Call `publish_help_article` only after an explicit "publish", with the revision you just read.
