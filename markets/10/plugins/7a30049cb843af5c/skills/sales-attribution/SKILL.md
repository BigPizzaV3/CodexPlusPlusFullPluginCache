---
name: sales-attribution
description: >-
  Tell which Reels sold: join Saypage's numbers (raised hands, links sent, page visits and clicks per automation, emails collected) with the sales in the user's own shop, checkout or booking tool through the connector they already have in this assistant, using three keys Saypage puts in place (a tagged link, the email address, a code per Reel). Saypage itself never reads a sale. Use for requests like "which Reel made me money", "did this Reel sell anything", "where do my sales come from", "how many sales from Instagram", "track my sales per Reel", "is Instagram worth it".
---

# Sales attribution

Every shop knows the order, few know the channel, none knows the Reel. Saypage knows the Reel
up to the click: who raised a hand, who got the link, who opened the page and tapped the
button. The shop knows what came after. This skill joins the two in the conversation, with
keys that both sides can see. Saypage reads no sale and stores none: the join happens here.

## 1. Find where the sales are

Ask in one message, starting from what you see in the pages' buttons (`get_page` on the pages
the automations send):

1. What do they sell, and where does the buyer pay or book? (Stripe, Shopify, Kajabi, Stan,
   Systeme.io, Gumroad, Teachable, Calendly, a bank transfer…)
2. Is that tool connected to this assistant? If it is, use its tools to read orders. If not,
   say which connector or export would do (most export a CSV of orders with the customer's
   email and the link's UTM fields), and go on with what the user can paste.
3. Do they boost Reels? The official Meta Ads connector, added to this assistant, gives the
   paid side; Saypage's views are organic only.

Never ask for API keys or passwords in the conversation.

## 2. Put the keys in place, from now on

Each key ties a sale to the Reel that brought it. Set them up with the user's go-ahead, before
reading results: a sale without a key stays "not attributed", never guessed.

| Key | How | Works with |
|---|---|---|
| **Tagged link** | add `utm_source=instagram&utm_medium=dm&utm_campaign=<keyword>` to the checkout or booking link on the Reel's page (`update_page`, then `publish_page`) or in the automation's `url` (`update_automation`) | Shopify, Stripe Payment Links, Kajabi (on the checkout link itself), Gumroad, GA4 |
| **Email** | the address the automation's email request collected (`list_emails`, the `email` gate on the automation) matches the buyer's email in the shop | any tool that records the customer's email |
| **Code per Reel** | a discount or referral code made in the shop for this Reel (`<KEYWORD>10`), named in the last DM (`update_automation`) and on the page | any tool with codes, sales by call or in person too |

Write the tag on the link the user sees, in the page or the automation: never shorten or
redirect it. Keep one keyword per Reel, so `utm_campaign` names it.

## 3. Read both sides

From Saypage, for the period (most often the last 30 or 90 days):

- `list_instagram_posts` with `insights: true`: each Reel's views and, per automation,
  `triggered`, `links_sent`, `page_views` and `page_clicks`.
- `get_page_stats`: each page's `automations`, its DM `clicks` and their `destinations` (the
  checkout link among them).
- `list_emails` with the automation's id, for the email key. Keep the addresses in this
  conversation only: never put them in a page, a caption or a reply.

From the shop, through its connector or the user's export: each order's date, amount, email,
UTM fields and code.

## 4. Join and report

Match each order, in this order: its code, then its `utm_campaign`, then its email against the
automation's collected addresses. An order with none of the three is "not attributed".
Count a sale once, by its first key that matches.

```
SALES BY REEL  ·  last 30 days  ·  from Shopify (orders 143, 41 attributed)

Reel            keyword   raised hands  links  page visits  checkout taps  sales  revenue
"3 mistakes…"   GUIDE     212           188    174          39             14     €546
"My morning…"   PLAN      61            55     49           12             2      €78
Not attributed                                                             102    €4,113

What it says
1. GUIDE sells 1 in 13 raised hands; PLAN 1 in 30, from a page with no price above the fold.
2. 102 sales have no key: most came before the tags went in (12 Nov).
Next   tag the bio page's checkout link too (utm_medium=bio), and remake the PLAN page's top.
```

Say how each number was matched, and that taps and visits count taps and loads, not people.
Never estimate a revenue for orders without a key, and never call the result a conversion
rate when the steps count different things (a person can visit twice).

## 5. Keep it going

Offer to run this again in a week (a scheduled task in this assistant if it has one), and to
give the next Reel its own keyword, page and code from the start (`reel-funnel`).
