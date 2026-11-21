---
name: advanza-reuse-winner
description: Find the user's best-performing posts or emails in Advanza and turn them into new drafts for other channels on free dates. Use when they want to reuse or repurpose what worked.
---

# Reuse the winner

Take what already worked and give it a second life on the user's other channels, as drafts on dates
that are still free.

Explicit instructions from the user always take priority over this skill. Answer in the user's
language. Pass the user's time zone (`timeZone` / `timeZoneId`) to every tool that takes one.

## 1. Find the winners

- Use the period the user names; otherwise the last 90 days.
- `analytics.social-performance` for the top posts, `analytics.email-campaigns-top` for the top emails.
- Rank by the measure the tools return (engagement, clicks or opens) and say which you used. Only
  posts with synced analytics are ranked; if there is too little data, say so and ask which piece the
  user wants to reuse.
- Analytics results carry ids, not links or full text: read each winner with `social-posts.get` (or
  `email-campaigns.get`) for its full text, media and link.
- Show the top three with their numbers and links, and ask which to reuse unless the user already said.

## 2. Plan where and when

- `social-accounts.list`: the connected channels. Reuse on the channels the winner was not on.
- `social.channel-rules`: each channel's length limit, media needs and link handling. Instagram,
  TikTok and Pinterest need an image or video; a TikTok post also needs its audience chosen in Advanza
  before it can be scheduled.
- `calendar.list` for the next 30 days: pick dates with nothing planned on that channel, at the time of
  day the original went out unless the user prefers another, and at least a few minutes from now.

## 3. Write the drafts

- Rewrite for each channel, keeping the message that made the original work. Do not copy the text
  word for word, and do not invent offers, prices or claims that were not in the original.
- Reuse the original's images (its `mediaUrls` from `social-posts.get`).
- To reuse a winning email as a new email, create a draft from the same template where it had one, then
  change only what differs with `email-campaigns.update-draft` `blocks` and the draft's `revision`.
- Create the drafts with `social-posts.create-draft`; its `targets` make one draft per channel in a
  single call. Keep each draft's proposed date and time for the hand-over: a draft gets its time when
  it is scheduled.
- Run `brand.check-text` on each draft and fix what it reports as blocking.

## 4. Hand over

Show each draft with its channel, proposed date and link. Scheduling is a separate step: offer
`social-posts.schedule` for each draft the user approves, with its proposed time. Its card shows the
whole post and the person approves it there. (`social-posts.bulk-schedule` only takes posts whose
content was already approved in Advanza or in a campaign.)
