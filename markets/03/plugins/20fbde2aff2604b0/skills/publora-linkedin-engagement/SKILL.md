---
name: publora-linkedin-engagement
description: >
  Comment, react and reshare on LinkedIn through Publora, and mention people
  correctly. Use when the user wants to respond to a LinkedIn post rather than
  publish their own. Not for metrics — Publora exposes no LinkedIn analytics
  here.
---

# LinkedIn engagement

Publishing is only half of LinkedIn. This skill covers the other half:
responding to what is already there. Every action below happens on a live post
under the user's own name, in public, and the platform notifies people.

## Before anything

```
list_connections
```

Engagement needs a connected LinkedIn account, and the `platformId` goes into
each call verbatim. If LinkedIn is not connected, say so and stop.

## What is available

| Action | Tool | Reversible? |
|---|---|---|
| React to a post | `linkedin_create_reaction` | Yes, `linkedin_delete_reaction` |
| Remove a reaction | `linkedin_delete_reaction` | The original is gone |
| Comment | `linkedin_create_comment` | Yes, `linkedin_delete_comment` |
| Delete a comment | `linkedin_delete_comment` | **No** |
| Reshare to the feed | `linkedin_create_reshare` | Delete the reshare as a post |

Reactions and comments need the target post's URN. Take it from what the user
gives you — a link or an id — and never construct one. A guessed URN either
fails or, worse, hits someone else's post.

## Comments are text the user signs

Show the exact comment text and the post it lands under, and wait for a yes.
"Leave a nice comment on that post" is not consent to a specific sentence.

Keep drafted comments short and specific to the post. Do not add hashtags,
emoji or a pitch for the user's own product unless they asked.

## Mentions

`linkedin_list_mentionables` lists people captured from engagement on the
user's connected company pages, each with the app-scoped person id — the only
id namespace LinkedIn resolves in a mention. Look the person up there and use
the returned id. A name typed into the text is plain text, not a mention, and a
guessed id will not resolve.

If the person is not in the list, say so. They have not engaged with the
account, so there is nothing to mention them by.

## Reshares

`linkedin_create_reshare` puts an existing post on the user's own feed,
optionally with commentary. The commentary is the user's public voice: draft
it, show it, then post it. The original post is untouched.

A scheduled reshare of the user's own upcoming post is set instead through
`platformSettings.linkedin` on `create_post` — see the `publora-publishing`
skill.

## Never

- React, comment or reshare without an explicit go-ahead on the exact content.
- Delete a comment because it "looks wrong". It cannot be brought back.
- Bulk-engage: no reacting to a list of posts, no repeated comments across a
  feed. That is what platforms remove accounts for.
- Claim engagement numbers or reach. Those are not available through this
  connector.
