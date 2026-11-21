---
name: feedback-analysis
description: Analyze what customers ask for in teem and suggest what to build next. Use when someone asks for top requests, themes in feedback, what to prioritize, or wants a request's status changed.
---

# Feedback analysis

## Gather

1. Call `list_posts` with `sort: "top"` for the open board. Add `status: "open"` or
   `status: "planned"` when the question is about what's next. Follow `meta.next_cursor` when the
   person wants the whole board. `meta.counts` gives totals by status.
2. Call `get_post` for any request you recommend, so you have its body, verified authors and the
   team's updates.
3. For a theme ("exports", "SSO"), call `search` with `type: "posts"`, then `search` with
   `type: "conversations"` to find support threads about the same thing. Conversations show
   demand that never reached the board.

## Report

- Rank by votes, then by how many support conversations mention it. Give each one its title,
  votes, status, a one-line why, and its `url`.
- Say when a request's votes come mostly from unverified authors. A verified author's own server
  signed who they are.
- Keep bugs (`kind: "bug"`) apart from feature requests.
- Recommend two or three to build next, with the reason in one line each. The team decides.
- With no requests, or none on the topic, say so. Don't fill the gap with guesses.

## Change a status

- Call `update_status` only when the person asks for it, for one request at a time.
- Moving a request to `planned`, `in_progress` or `shipped` emails everyone who voted. Before
  you call it, say how many voters will get the email (`votes`) and ask to confirm. Pass
  `notify: false` only when the person says not to email anyone.
- `note` is public on the board. Show it to the person before you send it.
- To announce something that shipped, use the release-drafting workflow instead: publishing a
  changelog entry ships its linked requests and emails their voters in one step.
- Don't call `create_post` for a customer unless the person asks. It puts a request on the public
  board under that customer's name.
