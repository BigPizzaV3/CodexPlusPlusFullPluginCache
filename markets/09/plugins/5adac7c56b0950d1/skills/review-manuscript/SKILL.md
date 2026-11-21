---
name: review-manuscript
description: Get a specialist peer review of a manuscript, thesis chapter, proposal or literature review with CitedEvidence, and help the user act on it. Use when the user asks for a review, critique or readiness check of their academic writing.
---

# Review a manuscript

The review takes several minutes and uses credits from the user's CitedEvidence account.

1. Make sure you have the full text, at least several paragraphs. Ask for the target journal and field if the user hasn't said; both improve the review.
2. Call `start_manuscript_review` with the text, a short title, `review_type` (`manuscript`, `proposal`, `thesis` or `literature`), and the `journal_name` and `field` if known.
3. Tell the user it has started and that the card shows progress.
4. Later, call `get_manuscript_review` with the `review_id`. When it's finished, report the overall score, readiness and recommendation, then the main concerns in order of importance.
5. Offer to work through the fixes one concern at a time, quoting the relevant passage from the user's text. Don't rewrite the whole manuscript unless asked.
6. If the account doesn't have enough credits, state that plainly. Don't suggest buying credits or upgrading.
