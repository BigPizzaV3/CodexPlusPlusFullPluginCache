---
name: google-reviews
description: Answer Google Business Profile reviews with the SocialAPI app. Find the reviews that have no reply yet, sort them by star rating, draft a reply for each in the business's voice, and post only the replies the user approves. Use when the user says "reply to my reviews", "Google reviews", "answer reviews", "unanswered reviews", "bad review", "1 star review", "review responses", "reputation", or asks about the rating of their business on Google.
---

# Google reviews

Requires the SocialAPI app in ChatGPT. Every tool name starts with `social_api_`. The `socialapi` skill holds the parameters, ids and error codes: follow it for every call.

Reviews work on Google Business Profile only. For any other platform, say so.

## 1. Find the locations

`list_review_accounts` with `platform: google`. These review tools return capitalised keys (`AccountID`, `Name`, `Status`, `Summary`).

- Use the accounts whose `Status` is `ok`.
- `reconnection_required`: say that location must be reconnected and offer `connect_account` for `google`.
- No account: say no Business Profile is connected and offer `connect_account`.
- Several locations: cover all of them, one section per location, unless the user named one.

## 2. Collect the reviews

`get_reviews` with `account_id` set to the `AccountID`:

- `order: newest` for "what came in", `rating_asc` to start with the worst.
- Up to 50 per page. Follow `next_cursor` until it is empty or the reviews are older than the period the user asked about.
- Each review has `ID`, `Rating` (1 to 5), `Text`, `Author`, `CreatedAt` and `Reply`. `Reply: null` means the business has not answered.
- The top-level `summary` holds `AverageRating`, `TotalCount` and `LastReviewAt`: open the report with them.

## 3. Sort

1. **1 and 2 stars, unanswered**: answer first.
2. **3 stars, unanswered**.
3. **4 and 5 stars, unanswered**.
4. **Already answered**: list them only when the user asks, or when the existing reply looks wrong.

A review with a rating and no text still deserves a short thank-you.

## 4. Draft

- Address the reviewer by the name in `Author`, mention one specific thing they wrote, and keep it short.
- Negative review: thank them, acknowledge the problem without arguing or admitting legal fault, and invite them to continue privately (`[phone or email]` placeholder unless the user gave one).
- Never invent facts, offer refunds or discounts, or quote prices the user did not give. Put a `[placeholder]` instead and point it out.
- Never put a customer's private details in a public reply.
- Up to 2200 characters, but most replies should fit in 2 to 4 sentences.

Show the review, its rating and the draft side by side, and wait for approval.

## 5. Post

- Call `reply_to_review` (`account_id`, `review_id` set to the review `ID`, `text`) once per approved reply. Each reply costs 1 interaction credit: when there are many, check `get_usage` first.
- `state: PENDING` means Google is checking the reply. That is a success: say it will appear once Google approves it. `REJECTED` means Google refused it: offer to rewrite it.
- A review has one business reply. Replying again replaces the existing reply and costs another credit, so warn before replacing one.
- A reply cannot be deleted with these tools.

Finish with what was posted, what is pending and what was left unanswered.
