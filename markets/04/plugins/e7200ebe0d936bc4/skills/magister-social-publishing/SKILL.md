---
name: magister-social-publishing
description: Draft, schedule, and publish social posts through Magister, and read post and follower analytics. Use when the user wants to write a social post in their brand voice, schedule content, publish a draft, see how posts performed, or find the best time to post.
---

# Social posts through Magister

Drafting and scheduling are ordinary writes. **Publishing to a public account
requires a person's approval** and cannot be forced from this connector.

Resolve `project_id` from `list_projects` first; never guess one.

## Every post needs a real account

Call `list_social_accounts` before creating a post. Each platform you post to
needs its **`account_id` from that list** — supplying a platform name alone is
rejected. Do not invent an account id and do not carry one over from a previous
conversation.

If several accounts are connected for a platform, ask which one.

## Drafting

`create_social_post` creates a draft. Read `get_brand` first so the copy matches
the brand's actual voice, audience, and messaging pillars rather than a generic
tone.

`update_social_post` edits an unpublished post. Note that it **overwrites the
caption with no revision history**, so if the user may want the previous version,
show it to them before replacing it.

## Scheduling commits to a future public post

Supplying a schedule time is not the same as saving a draft. Once approved, the
post will publish publicly at that time, and **this connector has no tool to
unschedule or delete it afterwards** — that has to be done in the Magister app.

Say that before scheduling, and confirm the time and time zone.

## Publishing requires approval, and that is not a failure

`publish_social_post` does not publish on the call. It creates a permission
request describing the exact post, and a person must approve it in the Magister
app before anything goes live.

When the tool returns that it needs approval:

- Tell the user the post is waiting for their approval and give them the
  approval link the tool returned.
- **Do not call the tool again.** A second call does not publish it and only
  creates confusion; the request is already waiting.
- Do not describe the post as published, live, or sent.
- `get_action_approval` checks one request's status and
  `list_action_approvals` lists pending ones, if the user asks what is waiting.

## Reading performance

`list_social_posts` returns the project's posts and their status.
`get_social_analytics` returns per-post metrics, daily numbers, follower stats,
and best-time-to-post insights for the connected accounts.

Use the posting-time data when the user asks when to post, rather than offering
generic advice about optimal posting times.

## Do not infer

- Never state engagement, reach, or follower numbers the tools did not return.
- Never claim a post published without a completed publish.
- Never work around the approval step, even if the user asks you to skip it.
