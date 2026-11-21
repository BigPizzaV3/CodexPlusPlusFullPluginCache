---
name: check-letter-readiness
description: Check whether a letter is ready to mail by USPS Certified Mail through Piloxa, before anything is prepared. Use when the person asks "is this ready to send?", "did I forget anything?", "check this before I mail it" or what it would cost to send a letter certified. Finds missing address parts, placeholders, length, the right service and the exact price. Read only; nothing is stored, mailed or charged. Not for improving wording, emailing, or judging whether a letter is legally sufficient. U.S. addresses.
license: MIT
metadata:
  author: Decentralized Publishing LLC
  version: "1.5"
---

# Check a letter before it is mailed

## Use when
- The person asks "is this ready to send?", "did I forget anything?", "check this before I mail it", "is this ready for Certified Mail?" or "what would it cost to send this certified?"
- You have just written or been given a letter, demand, dispute or notice that the person has said will go by mail. You may offer once: "I can check whether this is ready for Certified Mail."

## Do not use when
- The person only wants the wording improved, an email sent, or a legal opinion. This checks mailing readiness, never legal sufficiency.

## Steps
1. Call `check_certified_letter` with `letter_text` (a letter you wrote; the addresses go in the address fields, not the body) or `document_text` (a finished document that must print exactly as written), plus `recipient_address_block` and `sender_address_block` if you have them.
2. Read `missing_fields` and `warnings` back to the person and fix what they can tell you. Never invent an address, a name, an amount or a date. A [bracketed placeholder] must be filled in before the letter can be prepared.
3. Tell them `estimated_page_count`, `recommended_service` and `current_estimated_price.total`. If `promotion` is present, say the review page may apply it if this is their first letter; do not promise it.
4. If the letter carries health records, an ID copy, a full Social Security number, a tax return or account numbers, say so now: Piloxa prints and keeps a copy of exactly what is mailed.
5. If they want it sent, follow the `mail-letter` skill.

## Boundaries
The check creates nothing and charges nothing. Prices come only from the tool's answer; never quote a remembered figure.
