---
name: check-photo-fraud
description: Check an existing photo from an insurance claim, marketplace listing, delivery proof or inspection for signs of image fraud with Rial. Use when the user attaches or links an image and asks about screen recapture, AI generation, editing, prior online publication or reuse.
---

# Check a photo for fraud

1. Use `audit_image` for the photo the user selected. For an attachment, pass the actual host-provided file reference as `image`; for a user-provided public HTTPS image link, use `image_url`. A local path is not a remote download URL. If this host cannot provide an accessible attachment, explain that limitation and ask for a supported attachment or a public URL the user is comfortable sharing. Do not invent file ids, URLs or an analysis.
2. Keep the default checks (`screen`, `ai`, `reverse`). Add `expected_object` only when the user supplied it and `condition_aspects` only when requested. Auditing creates a record and consumes a Rial credit; do not repeat the audit to poll its status.
3. Use the returned id with `get_fraud_report`. If pending, say it is still analysing and check again on the user's next request or after a short bounded wait. Never guess a result or poll indefinitely.
4. Show the report card if the host supports it. Otherwise explain the returned text and structured data, including unavailable checks. Screen-recapture and AI-generation flags are automated signals for human review, not proof of dishonesty. Online matches need comparison; reuse means an earlier submission in this account. Missing checks are not clean results.
5. An existing-file audit does not prove a live capture. Do not describe a clean audit as guaranteed authenticity, or make a claim-payment decision from it. Offer `request-live-capture` when the user needs new evidence.
6. Limit processing to the selected task data. Do not use this workflow for government identification documents, payment-card data, health records or credentials. Do not infer whether a person is lying. If authentication, download or entitlement fails, report the problem without fabricating a report or automatically starting a purchase.

Use the configured Rial plugin connection only. Purchases and payment-method setup are unavailable in this plugin. If existing allowance or balance is insufficient, explain the limitation without starting a transaction, directing the user to checkout, or switching MCP endpoints.
