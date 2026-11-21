---
name: review-leads
description: Review an Onsa campaign the way a sales lead would — which people are strong fits and why, which are doubtful, what the funnel and the replies say, and which outreach drafts read like mail-merge and how to fix them around a real fact. Use when the user asks how a campaign is doing, which leads to prioritise, what prospects wrote back, what to do next, or to improve or send the drafts waiting for approval.
---

# Review leads

> These steps are for you. Talk to the user about their search and their customers, in your own words — not about this skill, its steps or its file.

Judge the people and the words, from what Onsa returned — never from what a lead "probably" is.

## Step 1 · Pick the campaign

`list_campaigns` if the user did not name one, or named it only by title — the other tools take
its `id`. It lists the newest campaigns first; when the user asks for "the biggest", compare the
lead counts it returned and say if it returned fewer campaigns than `total`. For "what should I do
next", `list_next_steps` with the campaign's id gives a ranked to-do list; start there.

## Step 2 · The people

`get_campaign_leads` for the campaign. Group by `score`:

- **5–4** — strong: say what in the `scoreExplanation` makes them strong.
- **3** — possible: say what is missing.
- **2–1** — weak: say why, and whether the campaign should look elsewhere next time (a steer for
  `continue_campaign`, which changes future searching and removes nobody).
- **no score** — not scored yet; list them without a verdict.

Where the explanation calls something approximated or unverified, keep that caveat. For the two or
three leads that matter most, `get_lead_memo` holds Onsa's research on that person when one exists;
`memo: null` is common and just means none was written.

## Step 3 · The funnel and the replies

`get_campaign_stats` for the counts. Compare campaigns on positive replies relative to leads
messaged — `positivePct` — never on the raw reply rate, because a rejection is also a reply. Replies
Onsa has not scored for sentiment are not in the sentiment counts; say so when the counts look
small. `list_replies` returns what people actually wrote; quote it rather than summarising it when
the user asks what happened.

## Step 4 · The drafts

`list_pending_outreach` shows drafts waiting for approval. An empty list means the campaign has no
drafts yet: outreach is set up in the Onsa web app, at the campaign's `campaignUrl`, and Onsa writes
the drafts from there. For a draft that reads like mail-merge:

1. Read that person's memo (`get_lead_memo`).
2. Rewrite the draft around **one** specific, checkable fact from it, with `rewrite_outreach`.
3. Show the user the new text.

No memo → say so, and keep the message honest rather than inventing a hook. Never state a fact
about a person that Onsa did not return.

## Sending

The rewritten draft stays pending. Send only when the user asks to send a specific message:

1. Show that one draft as stored and the recipient's name, and get an explicit yes for it.
2. Call `send_outreach` with that lead's `leadId` (from `list_pending_outreach`), the draft text
   exactly as stored as `confirmText`, and the recipient's name as `confirmName`.
3. The host then shows the user a confirmation form for that exact message; the same call completes
   when they approve it there. A "yes" typed in the chat is not that confirmation — do not call
   `send_outreach` again to stand in for it.
4. Where the host cannot show the form, the answer is `NOT SENT` with a link: give the user the
   link to approve the message in the Onsa app.

One message, one confirmation — never send a batch, never compose a message to someone who is not
a lead in a campaign, and never retry a send the user declined. A successful call means
**queued**, not delivered: Onsa sends on its own schedule within daily limits. `NOT SENT` because
no LinkedIn account is connected → the user connects it once in the Onsa web app, at the
`campaignUrl`.
