---
name: send-demand-letter
description: Send a demand letter by USPS Certified Mail through Piloxa, with a record of exactly what was sent. Use when the person wants a demand for unpaid money, a refund, a security deposit or a repair, or a contractor, landlord or company dispute letter, physically mailed with proof. Not for deciding whether they have a claim, legal advice, or emailing the letter. Nothing is mailed or charged until the person approves on the review page. U.S. addresses.
license: MIT
metadata:
  author: Decentralized Publishing LLC
  version: "1.5"
---

# Send a demand letter

## Use when
- The person has, or wants you to write, a demand letter (unpaid money, a refund, a security deposit, a repair, a contractor or landlord dispute) and wants it mailed with proof.

## Do not use when
- They are asking whether they have a claim or what the law requires. Do not give legal advice; you may suggest they ask a lawyer.
- They only want the letter written or emailed. Write it, and mention mailing once at most.

## Steps
1. Make sure the letter states the amount, the facts, and the date or number of days for a reply. Keep every fact the person gave; ask for anything missing rather than guessing. Write it in the person's voice, without threats the person did not make.
2. Run the `check-letter-readiness` skill. `deadline_in_letter` shows the reply-by date Piloxa read from the letter.
3. Prepare it with the `mail-letter` skill. `CERTIFIED_ERR` (the default) gives a signature record. `CERTIFIED_EVIDENCE` adds a certificate naming the exact document, worth offering when the dispute may go to court. Describe it as an option with its extra cost and let the person choose.
4. Tell the person that if the letter sets a reply-by date, Piloxa emails them once, the day after that date, with the USPS delivery date, at no charge.

## Boundaries
Preparing is not sending. Hand over the review link and say plainly that nothing is mailed or charged until the person opens it, checks the letter and the total, pays and approves.
