---
name: diagnose-payment-declines
description: Work through a rise in card declines, a drop in approval rate, or failing subscription rebills for a merchant, using the decline-code and 3-D Secure tools. Use when a merchant reports more declines than usual, a lower approval rate, or recurring charges that have started failing.
---
The user's explicit instructions take precedence over this skill. If this skill would make you pause, ask for permission, or leave work unfinished, say which instruction caused it.

Use this when a merchant reports more declines than usual, a lower approval rate, or failing recurring charges.

1. Collect what is already in the conversation. Ask at most two questions, and only if the answers are missing: the top decline codes (or the processor's reason text) and whether the declines are first-time charges or recurring rebills.
2. Call explain_decline_code for each code the merchant gives, passing the processor name when it is known. Separate soft declines (retry candidates) from hard declines (stop retrying).
3. If any 3-D Secure failure is involved, call explain_3ds_result.
4. Ask whether declines cluster by issuer, BIN range, card brand, or a single merchant ID or processor. Do not infer this; if it is unknown, say that this breakdown is the next thing to check and what it would show.
5. End with the links from the tool result's Sources line, so the user can read the full guidance. Do not mention or call any other connector.
6. Deliver, in this order: (a) what each code means, in one table; (b) which retries are allowed and which are not, with the network rule; (c) a prioritised checklist of likely causes to verify; (d) the data the merchant should pull next. Cite source_urls.

Never recommend retrying a hard decline, exceeding the network reattempt limits returned by the tool, or moving volume between merchant IDs to influence monitoring ratios. Never ask for a card number; the first six to eight digits are enough to identify an issuer.
