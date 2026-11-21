---
name: review-drafts
description: Gather what is waiting for a person's decision in Excellent — social posts and guest campaigns to approve, thank-you cards, pre-shift notes, training courses and event emails to publish, replies to inquiries to send, draft invoices, shifts and documents (Partner pro formas, pitch decks and investor updates included) to keep or discard, staged imports to commit — and give a review link for each, to decide in Excellent. Use for "what's waiting for my approval", "send me the review links", "approve this week's posts", "which drafts are still open".
---

# Review drafts

Read-only. This skill never approves, publishes, sends, commits or discards anything. Each decision is made by
the person on Excellent's own review page, signed in as themselves; the link works only for them.

## 1. Find the drafts

- Social posts and guest campaigns: `marketing` lists both queues with each draft's status.
- Documents: `list_documents` (drafts carry a draft status) — proposals, BEOs, contracts, training documents
  and Partner documents. Invoices: `list_invoices` with `status: "draft"`.
- Staff shifts: `schedule_week` shows each venue's unpublished changes.
- A draft made earlier in this conversation — a course, an event email or a staged import among them: use
  the id its tool returned.

## 2. Get a link for each

Call `get_review_link` with the draft's `kind` and its `id`: `post`, `campaign`, `card`, `reply`, `invoice`,
`preshift`, `shift`, `document` (a Partner document too), `course`, `template` (an event email) or `import`.
The answer gives the link and until when it works when the person may decide that draft; otherwise it says
who can.

## 3. Hand off

One line per draft: what it is, what the person will be asked, and the link:

- post or campaign — approve or reject;
- thank-you card, pre-shift note, course or event email — publish or discard;
- reply — send or discard;
- invoice, shift or document — keep or discard (an invoice is sent, and a document finalized, from its own
  page);
- import — keep it to review (each row is checked and the import committed on its own review page) or discard.

If the person wants a post, campaign or invoice changed before deciding, revise it (the `marketing-week` and
`money-owed` skills; an invoice is read in full with `get_invoice` first, and revised only while its
`revisable` is true). End with: "Nothing is approved, published, sent or added until you decide it on
Excellent's page."

Safety: this skill only reads and hands back review links. Nothing is approved, published, sent, committed or
discarded from ChatGPT.
