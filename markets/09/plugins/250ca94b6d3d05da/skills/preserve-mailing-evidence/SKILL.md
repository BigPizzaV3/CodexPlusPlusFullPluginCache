---
name: preserve-mailing-evidence
description: Explain and obtain proof of what was mailed through Piloxa by USPS Certified Mail - the exact document and its SHA-256 fingerprint, USPS tracking, the Electronic Return Receipt and the Evidence Pack certificate. Use when the person asks "can I prove what I sent?", "do I have proof they got it?" or what records they will have. Not legal advice on whether the proof is enough for a court or a rule.
license: MIT
metadata:
  author: Decentralized Publishing LLC
  version: "1.5"
---

# Preserve mailing evidence

## Use when
- "Can I prove what I sent?", "do I have proof they got it?", "what records will I have?"

## Steps
1. For background (what Certified Mail proves and what it does not), call `search` with the question and `fetch` the best result.
2. Before sending: Certified Mail alone proves a mailpiece was delivered, not what was inside. Piloxa keeps the exact approved document beside the USPS record. When proof of contents may matter, describe `CERTIFIED_EVIDENCE` (a Certificate of Mailing naming the document by its SHA-256, record kept 7 years) as an option with its extra cost, and let the person choose.
3. After sending: `get_certified_letter_status` (same conversation) or `get_my_letter` (an earlier chat, once connected) shows tracking and the return-receipt state. The full record and downloads are at piloxa.com after sign-in.

## Boundaries
Do not say a signature or delivery exists until the status shows it. "No record yet" means USPS has not reported, not that delivery failed. Do not say the evidence will satisfy a court or a rule.
