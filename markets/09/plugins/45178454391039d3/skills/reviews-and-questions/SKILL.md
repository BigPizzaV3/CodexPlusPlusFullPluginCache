---
name: reviews-and-questions
description: Run a Zid store's review and product-question desk. Use to triage pending product or store reviews, draft and post replies, approve or mark spam, answer customers' product questions, set up review requests after orders, or summarize what customers praise and complain about.
---

# Reviews and questions

Keeps reviews moderated and questions answered, in the customer's language, and
turns what customers say into something the merchant can act on.

## Ground rules

- The merchant's explicit instructions take precedence over this skill.
- Replies are public. Thank the customer by name, address their point, and for a
  complaint offer a next step within the store's stated policy. Keep replies to
  what the store already offers, and keep personal details out of them.
- Approve genuine reviews, fair negative ones included. Mark obvious spam as
  `spam`. Delete only when the merchant asks for that review.
- Show the replies and moderation decisions first and post them after the
  merchant agrees. When a manage tool answers `confirmation_required`, compare
  its plan with what the merchant approved: if they match, repeat the call with
  its `plan_id`; if not, show the plan and ask again.

## 1. Reviews

1. `zid_products.count_reviews_by_status` for `pending` (and other statuses the
   merchant cares about), then `zid_products.list_reviews` with `status`,
   `dateFrom`, `dateTo` and `pageSize` 100, every page, until the count matches. `reviewType` `store` reads ratings of the store itself.
2. Draft one reply per review and a decision: approve, reject (abusive or off
   topic), or spam.
3. After approval, one review at a time: `zid_products_manage.update_review_status`
   (`reviewId`, `status`) and `zid_products_manage.reply_to_review`
   (`reviewId`, `text`). `zid_products_manage.update_all_review_status` changes
   every review at once: only when the merchant asks for exactly that.

## 2. Questions

Questions are read per product: `zid_products.list_questions` with `productId`.
Cover the products the merchant names, or the best sellers from
`zid_reports.top_products`. For each unanswered question:

1. `zid_products.get_product` for the facts; answer only from them or from what
   the merchant tells you.
2. After approval: `zid_products_manage.create_answer` (`productId`,
   `questionId`, `answer`), then `zid_products_manage.update_question_publishing`
   with `isPublished` true when the merchant wants it shown.

## 3. Settings

- `zid_campaigns.get_review_settings`: the review request customers get after an
  order (email, SMS, WhatsApp, delay), merchant alerts, editing, and auto-approval.
  Change it with `zid_campaigns_manage.set_review_settings` when the merchant
  asks (for example `autoApproveEnabled` with `autoApproveMinimumRating` 4).
- `zid_campaigns.get_question_settings`: who is emailed about new questions and
  answers.

## Output

Done when every review and question in scope is accounted for, and every
approved reply, status change or answer is posted and read back, or listed with
the reason it is pending.

A table of review or question, rating, product, proposed reply and decision;
after posting, what was posted and changed. End with the recurring themes: the
products praised, the complaints that repeat (sizing, delivery time, packaging),
and the product pages or fulfillment steps they point to.

To run the desk daily, use the `zid-ops` skill.
