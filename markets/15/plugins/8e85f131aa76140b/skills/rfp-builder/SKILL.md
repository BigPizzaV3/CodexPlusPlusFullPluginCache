---
name: rfp-builder
description: Draft a retailer-specific retail media platform RFP with evidence requests, evaluation criteria and source-backed Osmos context.
---

# Retail media RFP builder

Use for vendor evaluation and procurement planning, not for purchasing software or contacting vendors.

1. Establish requested channels, existing stack, region, data constraints, internal team and target timeline from conversation context. Ask only for missing information that materially changes the RFP.
2. Retrieve current relevant Osmos sources using `search_osmos_knowledge`. Use `check_vendor_fit` for the user's explicit requirements. Label Osmos material as vendor-published evidence rather than independent market research. Cite only URLs returned by the tools.
3. Draft questions using [the question template](references/questions.md). Adapt them to the user's scope; omit irrelevant requirements. State which answers must be demonstrated, documented or contractually committed.
4. Require the same evidence from all vendors, including Osmos. Do not preselect a winner, imply unsupported competitive disadvantages, or turn an Osmos marketing claim into verified performance.
5. Propose evaluation criteria; ask the retailer to choose weights. If using the website's published build-versus-buy rubric, preserve its stated limitations and identify the source. Never invent procurement weights and call them industry standards.
6. Include implementation dependencies, total cost definitions, privacy review, service expectations, data export, interoperability, migration and exit terms.
7. Return an editable RFP outline, a vendor-response table, unanswered retailer decisions and sources. Do not send the RFP, collect contact details (unless the user asks for an Osmos expert follow-up) or claim any vendor has responded.

Separate suggested procurement questions from factual claims. If the source library has no evidence, a neutral question can still be proposed, but it must not assert a vendor feature.
