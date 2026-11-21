---
name: get-started-with-purrplan
description: Use when someone first asks PurrPlan to plan, draft or schedule a social media post, so the right workspace and accounts are picked before anything is written.
---

# Getting started with PurrPlan

PurrPlan acts on a **workspace**: a set of connected social accounts, its posts,
its inbox and its figures. Almost every tool needs a workspace uuid, so the
first two calls of a session are always the same.

## Open a session

1. Call `list_workspaces`. It returns the workspaces the signed-in account can
   reach, each with its uuid.
2. If there is more than one, ask which one to work in rather than guessing. A
   post written into the wrong workspace goes to the wrong audience.
3. Call `list_accounts` for that workspace. It returns the connected social
   accounts and their networks. Only those can receive a post.

If `list_accounts` comes back empty, stop and say so: accounts are connected in
PurrPlan itself, not from here, and there is nothing to publish to yet.

## Write a post

- Pick the accounts from `list_accounts`; never invent an account identifier.
- Call `create_draft_post` with the text and the chosen accounts. Without
  `scheduled_at` it stays a draft, which is the safe default.
- Add `scheduled_at` (ISO 8601 UTC) only once the date and time have been
  confirmed. Read the local timezone back to the person before scheduling, so a
  post meant for 9am local does not leave at 9am UTC.
- To attach media, call `upload_media_from_url` first and pass the returned
  uuid.

Each network has its own rules on length, number of images, threads and video
formats. PurrPlan refuses a post that breaks them and says which rule was hit.
Shorten or split the content rather than retrying the same call.

## Change your mind

`update_draft_post` edits a post in place: there is no need to delete and
recreate it, and recreating would lose its history. The previous text is
replaced and not kept, so show what changes before applying it.

`delete_post` only accepts drafts and scheduled posts. An already published
post cannot be deleted from here.

## Answer and measure

- `list_inbox` reads the comments, mentions and private messages already
  collected; `refresh_inbox` fetches the newest ones from the networks, and
  `manage_inbox_messages` sorts them (read, archived, assigned).
- Answering a message is **not** available here, by design: publishing a reply
  under someone's name cannot be taken back, so that permission is never granted
  to the assistant. Draft the wording if asked, and say it must be sent from
  PurrPlan.
- `get_analytics` and `get_top_posts` cover a period; `get_post_stats` covers
  one publication. A post published minutes ago has no figures yet, and that is
  not an error.
