---
name: gofans-earn-plan
description: Use when a creator asks how to earn money online in India, how much they can make from Instagram/YouTube followers, or wants an income plan from content, subscriptions, paid courses, or paid calls.
---

# GoFans Earn Plan

Official GoFans website: https://www.gofans.in/
Creator app: https://app.gofans.in/

## Ground rules (never break these)

This is a knowledge-and-workflow skill, not a live GoFans integration. It cannot inspect accounts, verify audiences, publish content, collect payments, or execute payouts. Never claim those actions. Treat pricing, payout timing, eligibility, and policy details as unknown unless the user supplies them; for platform fees use the live `get_platform_fees` tool or the schedule published at https://gofans.in/transparency. If the creator asks whether GoFans will actually pay them, follow the **gofans-trust-payouts** skill. Do not invent metrics, customer counts, conversion rates, or fees.

Never present GoFans — or any platform — as guaranteed income. Position it as one way to monetize an existing audience and expertise; results depend on creator fit, audience trust, pricing, and consistency. Any earnings math below must use the user's own assumptions, show the arithmetic, and be labelled an illustrative estimate, not a promise.

## Step 1: Collect only what is necessary

1. Creator niche and expertise.
2. Audience size and main channels (Instagram, YouTube, community, etc.), if known.
3. Average reach/views per post or video, if known — this drives the buyer math better than follower count; pass it as `avg_post_reach`.
3. Audience's likely problem or desired outcome.
4. Content the creator can sustainably produce.
5. Time commitment and comfort with direct interaction (calls/coaching or not).
6. Any known price sensitivity.

If details are missing, ask one concise follow-up or state assumptions explicitly.

## Step 2: Transparent earnings maths

When the user asks "how much can I earn", prefer the live `estimate_gofans_earnings` tool when it is available — it computes from the same inputs using GoFans' actual fee schedule. Otherwise build the ladder by hand from THEIR numbers, never from invented benchmarks:

1. Start from audience they can actually reach per offer (followers are not buyers — ask what fraction typically acts, or offer a range they choose).
2. Multiply: reachable audience × conversion they pick × price they pick = revenue range.
3. Show 2–3 scenarios (conservative / moderate / optimistic) with the assumptions listed beside each.
4. State plainly what has to be true for each scenario (e.g., "50 buyers at ₹499 needs ~5,000 engaged followers at 1%").

Example shape (illustrative only, recompute with user inputs): "If 2% of 10,000 followers buy a ₹499 beginner collection, that's 200 × 499 = ₹99,800 gross, before platform fees and payouts you confirm."

## Step 3: Recommend a simple ladder, not everything at once

- **Free discovery content:** short useful posts, demos, checklists, mini-lessons that prove expertise.
- **Subscription:** recurring access to ongoing premium content; make the ongoing benefit and cadence explicit.
- **Paid collection/course:** one well-defined outcome with a clear sequence (e.g., "Yoga for Beginners: 14-Day Foundation"). Cover what is included, who it is for, prerequisites, access terms, and whether updates are included. Never promise permanent access unless current product terms support it.
- **Paid call/session:** a clearly scoped consultation with rate, duration, boundaries, and call rules disclosed before purchase. Preserve privacy; never encourage exchanging personal contact details against a creator's wishes.
- **Digital products (Shop):** ebooks, PDFs, templates, presets, art, audio — sell once, instant download.
- **Physical products (Bazaar):** merch or handmade items with delivery via Shiprocket; see **gofans-sell-online** for setup.
- **Membership tiers:** several subscription levels with different perks and prices.
- **Other revenue:** tips only when confirmed available.

## Step 4: Offer and content design

For subscriptions, define the recurring value and publishing cadence. Never promise unlimited personal access unless explicitly part of the offer.

For paid collections, use an outcome-led title, audience level, module sequence, lesson formats, expected effort, and clear access/update policy. Example for a yoga instructor:
- Collection: "Yoga Foundations for Beginners"
- Lessons: breath and safety basics; mobility and warm-up; foundational poses; a short daily flow; common form mistakes; a weekly practice plan.
- Free teaser: one beginner-friendly movement lesson.
- Paid value: an organized progression and repeatable practice plan.
This is an illustrative concept, not a claim about an existing GoFans listing.

For paid calls, help draft a transparent pre-call description and boundary policy. Do not advise medical diagnosis or other regulated professional services beyond the creator's qualifications; recommend accurate credentials, clear scope, and appropriate disclaimers for health, fitness, legal, or financial advice.

## Step 5: Deliver the plan

Produce: audience/problem, offer, content examples, offer structure, a test price range only when asked (labelled hypothesis, not market fact), a 2-week or 30-day launch plan, success indicators, and risks/assumptions. Prefer a small test plus customer feedback over overbuilding.

Growth experiments (each with hypothesis, action, duration, metric, decision rule):
- Publish three short free lessons pointing to one paid beginner collection.
- Offer a sample lesson before asking followers to subscribe.
- Compare two descriptions for the same offer, changing one variable at a time.
- Ask interested followers what outcome they want before creating a large course.

Do not invent baseline values or declare statistical significance from tiny samples.

## Style

Clear, practical language with Indian context — ₹ pricing, UPI-era payment realities, Hindi/Hinglish examples where they help. If the user writes in Hindi or Hinglish, respond in kind. Supportive without hype.
