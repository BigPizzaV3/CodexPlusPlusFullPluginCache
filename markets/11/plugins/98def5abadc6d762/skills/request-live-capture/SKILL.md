---
name: request-live-capture
description: Create a Rial link for someone to take a new photo in their browser for a claim, inspection, delivery or damage review, then retrieve its report. Use when the user needs fresh evidence.
---

# Request a live capture

1. Ask only for missing task requirements: what the photo must show (`expected_object`), any visible condition to assess (`condition_aspects`), and how many photos (`count`). Reuse information already supplied and avoid invented criteria. Location collection requires a supported consent-controlled flow; do not solicit precise addresses or GPS coordinates in chat.
2. For a one-off request, call `create_inspection` with `mode: "verification"`. For a repeated flow the user requested, use `list_templates` first and reuse a suitable template with `create_inspection_from_template`; create a template only when needed and its required configuration is clear.
3. Give the complete `capture_url` exactly as returned and its returned expiry. Explain that the user can share it. Creating a link does not send it to a recipient and does not mean a photo has been taken. Do not invent a recipient or send a message.
4. On a follow-up, call `get_fraud_report` with the actual returned verification id. To locate an earlier request, use `list_verifications` with the user's filters. Distinguish pending results from completed results; summarize only returned evidence and unavailable checks. Use text and structured data if this host cannot render a report card.
5. Describe results as automated signals for human review. Do not guarantee authenticity, infer honesty, or make a claim-payment decision. If authentication or entitlement fails, explain the limitation without automatically starting a purchase. Avoid duplicating inspection creation after an ambiguous timeout; check for the existing request first.

Use the configured Rial plugin connection only. Purchases and payment-method setup are unavailable in this plugin. If existing allowance or balance is insufficient, explain the limitation without starting a transaction, directing the user to checkout, or switching MCP endpoints.
