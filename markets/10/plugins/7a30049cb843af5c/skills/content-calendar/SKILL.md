---
name: content-calendar
description: >-
  Plan the user's Instagram week: how many posts they can really make, the format and subject of each, the call to action and the Saypage page or automation behind it, daily stories and time for comments. Built from their recent posts and insights when Saypage is connected. Use for requests like "what do I post this week", "make me a posting schedule", "I'm out of ideas", "organise my Instagram for November", "ideas for today's stories".
---

# Content calendar

A plan the user can keep beats an ambitious one they drop on Wednesday. This skill decides
what to make; the other skills write it.

## 1. Start from what is true

With Saypage connected (call `get_account` first):

- `list_instagram_posts`: the last four weeks of posts, their formats and topics, so the
  plan does not repeat a theme from last week.
- `get_instagram_insights` over 28 days, with `demographics: true` when the account has 100
  followers or more: the countries tell you which time zone to plan in.
- `list_automations` and `get_page_stats`: which keywords already run, and which pages
  people visit.
- If `sales-plan` or `performance-review` ran in this conversation, their findings outrank
  every default below.

Then ask, in one message:

1. What is happening this week: a launch, a new dish, an event, a result, a lesson, a
   customer story. A week's news gives better posts than any idea list.
2. What they want from Instagram right now: new followers, visits, bookings, sales, DMs.
3. How many posts they can realistically make: be honest, two good ones beat five rushed.

## 2. The mix

Give each post one job, and vary them across the week:

| Job | Usual format | What it does |
|---|---|---|
| **Discover** | Reel | brings in viewers new to the account |
| **Useful** | carousel or Reel | gets saved and sent: recipes, steps, tips |
| **Trust** | Reel, photo or stories | the person, the place, the process, behind the scenes |
| **Offer** | carousel, Reel or stories | what they sell, said plainly, with the keyword or link |

A week of three posts might be Discover, Useful, Offer, with stories every day.

Give each post a precise subject the user could film tomorrow: "the €4 dinner I make when
the shop closes late" rather than "pasta".

## 3. Wire each post to Saypage

- **The ask**: when a post promises something to send, give it a keyword and say which page
  it sends (an existing one from `list_pages`, or one to build with `reel-funnel`). An Offer
  post needs something to sell: if the user has nothing yet, start with `offer-finder`.
- **The automation**: note which ones to create and on which post. Check the plan's limits
  in `get_account` before promising one on every post. On the Connector plan none runs yet:
  plan the asks and build the pages all the same, and say once that they go live with a
  plan that includes them. On the Free plan, plan the asks only: pages and automations
  need a plan ("Plans" in the `saypage` skill).
- **The bio**: if the plan pushes people to the bio link, make sure it leads to a page
  that matches the offer (`profile-review`).

## 4. When to post

Use the audience's time zone, from the demographics when available. Pick moments when
they browse (commutes, lunch, evenings for most people), check the guess against the
user's own best posts, and then keep a steady rhythm. If the user spends more time on the
hour than on the opening of their Reels, steer them back: a weak opening loses more than
an odd hour.

Saypage has no scheduler: it publishes when the user asks. The plan says when to come back
("Tuesday 6 pm: publish the gnocchi Reel"), or the user posts from the app.

## 5. Around the posts

**Comments**: 15 minutes after each post to answer the first comments (`comment-replies`).

**Stories**: three to six frames a day. They rarely reach new people: they reach followers,
for a day, so use them to give those followers an easy reason to reply, visit or buy.

- **A day's shape**: what is happening now, filmed; a detail, a price or how it is made; one
  sticker around the middle, while most people still watch; the answer, or a reason to come
  back tomorrow.
- **One sticker per job**: a poll for easy taps, a question box to hear what people want
  (keep the answers: they are tomorrow's hooks), a link to a Saypage page, a countdown for a
  launch.
- **Open on something real** (a face, hands, a place), with few words, away from the top and
  bottom 250 px of the 1080×1920 frame.
- **Selling works here**: the context, then the offer, then someone who liked it.
- **What Saypage cannot do**: Instagram's API publishes stories without stickers, so frames
  with a poll or a link go out from the app. Plain frames can go through Saypage when the
  user asks (`prepare_instagram_post` with `kind: "story"`, or `publish_instagram_video`).
  Replies land in the inbox, which Saypage cannot read, and trigger no automation: to send
  something automatically, point the story to a post with a keyword, or add a link sticker.
  Visits from link stickers appear in `get_page_stats` under `instagram_bio`.

## Output

```
WEEK OF 2 NOVEMBER  ·  3 posts  ·  audience mostly in France (Europe/Paris)

TUE 18:30  REEL      Discover  "I salted pasta water wrong for ten years"   ask: follow
THU 12:00  CAROUSEL  Useful    5 weeknight sauces, 10 minutes each           ask: Comment SAUCES -> sauces page (to build)
SAT 10:00  REEL      Offer     Sunday cooking class, 6 seats left            ask: Comment CLASS -> booking page (live)

STORIES   every day; poll on Wednesday, class countdown from Thursday
COMMENTS  15 min after each post

To do with Saypage: build the sauces page, then an automation on Thursday's post.
```

Then offer to write the first post ("write Tuesday"), one at a time with `reel-script`,
`carousel-post` or `instagram-caption`.
