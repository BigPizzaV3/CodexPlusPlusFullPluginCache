---
name: media-kit
description: >-
  Get the user paid by brands: build a media kit page on their Saypage address from their real Instagram numbers (followers, Reel views, reach, engagement, audience by country, age and gender, best posts) plus what Saypage alone can show, how many people act when they ask (keyword comments, DMs, page visits, clicks), with past partners, formats and a contact button; then help price a deal and write the pitch to a brand. Use for requests like "make me a media kit", "how do I get brand deals", "a brand asked for my stats", "how much should I charge for a sponsored Reel", "pitch this brand", "rate card", "sponsorship", "collab", "UGC".
---

# Media kit

Brands pay creators for attention they can trust. Before a deal, they ask for the same
things: who follows, how many see a post, and whether those people do anything. A media kit
answers that on one page the user sends with every pitch, and a link in their bio for the
brands that come looking.

Most media kits stop at reach. Saypage can add what brands rarely get to see: how many
people answered a call to action, commented the keyword, opened the page and clicked. Lead
with it when the user has it.

## What this skill can and cannot do

Saypage reads the user's own insights, posts, automations and page stats, and hosts the kit
on their address. It cannot see other creators' rates or a brand's budget, and it never
messages brands: the user sends the pitch. It cannot edit the Instagram bio (the user pastes
the link). A page is a snapshot: its numbers are those of the day it goes live, so it says
when they were taken and gets refreshed (step 7).

**Every number on the kit must come from a Saypage response**, with its period. A brand
checks numbers against screenshots of Insights; one inflated figure costs the deal and the
user's name. Use medians rather than the best post, and never round up past what was
measured. When Instagram holds a metric back (`unavailable`), leave it off and say why;
never write 0.

**The plan decides how far this goes** (`plan.tier` in `get_account`):

- On **Free** (`none`), Saypage only reads posts and insights: no page can be created,
  previewed or published. Do steps 1 and 2, then give the kit in the conversation (the
  numbers, the rate from step 4 and the pitch from step 5) for the user to send as text.
  Say once that the hosted page comes with a plan ("Plans" in the `saypage` skill), and do
  not call the page tools.
- On **Connector** (`connector`) only the home page goes online. Build the kit as its own
  page all the same and show the preview, say once that it goes live with Creator or
  Premium, and offer the Connector version: a short "Work with me" section on the home
  page, with the three strongest numbers and the contact button.
- On **Creator** and **Premium** the kit is its own page, online.

## 1. Ask what the numbers can't say

In one message, skipping what you already know:

1. Which brands or categories they want to work with, and which they refuse.
2. Brands they already worked with, and any result they may share (the brand agreed, or it
   was public).
3. What they offer: a Reel, a story set, a carousel, UGC (content the brand posts itself),
   usage rights, ads run from their account, a link in bio for a month.
4. Rates, if they have them, and whether the page shows them or says "on request".
5. The email address brands should write to, the languages they post in, the city or
   country they work from.

## 2. Gather the numbers

With Saypage connected:

- `get_account`: handle, bio, plan.
- `get_instagram_insights` with `days` 30 and `demographics: true`: `followers`, `reach`,
  `views`, `accounts_engaged`, `interactions`, and who follows and who engages
  (`followers_by_…`, `engaged_audience_by_…`) by country, city, age and gender.
- `list_instagram_posts` with `insights: true`, for the numbers of the last twelve or so Reels
  and posts: views, reach, likes, comments, shares, saves.
- Saypage's proof: `list_automations` (`links_sent`, and the page each one sends),
  `get_automation_activity` on the two or three automations that did best (`summary.people`,
  `triggered`, `links_sent`), `get_page_stats` with `days` 90 (each page's `instagram_dm`
  loads and `click_channels`), and `list_contacts` (`summary.people` and `came_back`: how
  many people answered across all Reels, and how many came back, since `summary.since`).

Compute, and keep the working:

- **Median views per Reel** over those posts, and the post count it rests on.
- **Engagement rate**: (likes + comments + shares + saves) / reach, per post, then the median.
  Say on the page that it is per reach. Brands also quote it per follower: give that too if
  the user asks, labeled.
- **Raised hands**: distinct people who commented the keyword (`summary.people`) per 1,000
  views of the Reel that asked. `triggered` and `links_sent` count comments, so someone who
  commented twice counts twice: call them "keyword comments" and "links sent", never people.
- **What they did next belongs to that Reel only when the numbers belong together**, the
  checks `funnel-review` makes: the loads are this automation's own (its entry in the page's
  `automations`, or the page's `instagram_dm` total when it alone sends the page), it stayed
  on this Reel (a moved automation carries the old Reel's history: ask the user if unsure),
  and its whole life fits in the 90 days `get_page_stats` covers (the activity summary covers
  13 months). Then those loads and clicks can go in that Reel's sentence. Otherwise give them apart, with their own window: "312 clicks from my DM
  pages over the last 90 days". Clicks are taps, not people.
- **Best work**: the three posts with the most reach or the most raised hands, with their
  permalinks.

Under about six posts, or with no automation yet, say the kit is thin and build it anyway
with what holds: a kit with honest numbers beats no kit.

## 3. Build the page

Call `get_page_guide` first and follow it. Path `/media-kit` unless the user picks another.
In this order:

1. **Who**: name, handle, one line on the niche and who follows, the city or country.
2. **In numbers**: three or four large figures, each with its period: followers, median
   Reel views, reach over 30 days, engagement rate.
3. **Who follows**: the top countries, the main age band and the gender split, from
   `demographics` only.
4. **When I ask, they act**: the Saypage numbers, as a sentence a brand can repeat: "On my
   last guide Reel, 1,180 people commented GUIDE to get it by DM, and the page they got was
   clicked 312 times." The clicks go in that sentence only when the step 2 checks hold. Add
   the loyal core when it is real, with its window: "Since March, 380 people asked on two
   of my Reels or more."
   Leave the section out when there is no automation yet.
5. **Best work**: the three posts, each with its number and a link to it.
6. **Partners**: only the brands the user named, and quotes only word for word. Logos only
   if the user has the rights.
7. **Work with me**: the formats, and the rates or "Rates on request".
8. **Contact**: a large button `mailto:` the user's address with a subject filled in
   ("Partnership with @handle"), and a second, smaller one to their Instagram DMs
   (`https://ig.me/m/<handle>`).
9. A footer: "Numbers from Instagram Insights and Saypage, updated <month year>".

Write the text with `natural-voice`: confident, plain, no superlatives the numbers don't
carry. `preview_page`, show the user, and publish **only once they agree**.

Then add a "Work with me" link to `/media-kit` on the home page, and suggest the user
mention it in their bio ("Brands: link below"). `get_page_stats` counts taps on the contact
button (`destinations` shows the `mailto:` address). Call them "contact-button taps": a tap
opens an email the visitor may never send, and the same visitor can tap twice, so it is not
how many brands wrote. Ask the user for that number.

## 4. Price a deal

You have no market data, so give a method and two or three prices to try, and leave the
choice to the user:

- Start from the **median views**, never the best post: a brand pays for what usually
  happens.
- Price the post from a cost per 1,000 median views the user chooses (ask what creators of
  their size around them charge), then check it against the time the content takes.
- **Usage rights** (the brand reuses the video), ads run from the user's account,
  exclusivity and extra revisions cost more, each priced on its own line.
- When a brand cares about action more than views, show the Saypage numbers from step 2:
  page clicks are taps, not sales, and a few are missed, so quote them as such.

Never quote another creator's rate that the user did not give you, and promise no result.

## 5. Write the pitch

For a brand the user names, 80 to 120 words they send themselves, by email or DM:

1. One line showing they know the brand (a product they really use, a recent campaign).
2. Who follows, in one sentence, with one number.
3. One content idea, specific to that brand and the user's format.
4. The media kit link, and a small ask: "Open to a call next week?"

Run it through `natural-voice`. Offer a follow-up of two lines for a week later.

## 6. Answer a brand that asked

When a brand asked for stats or a rate: the kit link, the rate for the format they want
(step 4), what is included (one Reel, one revision, usage for 30 days…), and a date. Ask the
user before stating anything they have not agreed to.

## 7. Keep it fresh

Numbers older than three months make brands doubt the rest. Once a month, or before a big
pitch, rerun step 2, `update_page` the figures and the date, and publish again. Each refresh
is one page update (`plan.limits.monthly_publish_limit`).

## Output

```
MEDIA KIT  ·  @toto.cooks  ·  14 posts, Oct 10 – Nov 9

FOLLOWERS        48,200
MEDIAN REEL      31,400 views (12 Reels)
REACH, 30 DAYS   412,000 accounts
ENGAGEMENT       6.8% of reach (median)
AUDIENCE         US 41%, UK 12%, Canada 8% · 25–34 · 72% women

WHEN I ASK       1,180 people commented GUIDE on one Reel (37 per 1,000 of its views)
                 1,240 keyword comments, 1,100 links sent by DM
                 312 clicks on that Reel's page (it alone sends it, 60 days old)

PAGE     toto-cooks.saypage.page/media-kit  (preview, not live)
PRICING  Reel $600–900 from your median views; usage rights priced apart
NEXT     publish, add "Work with me" to your home page, then pitch [brand]
```
