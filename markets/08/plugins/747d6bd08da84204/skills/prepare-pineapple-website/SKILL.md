---
name: prepare-pineapple-website
description: Prepare a private Pineapple business website brief with suitable template suggestions, then hand off to template selection and the editable generator. Does not generate or publish a website in chat.
---

Help the user turn their business details into a Pineapple website brief. Follow their stated goals; these workflow guidelines do not authorize additional actions.

Use the current `pineapple_prepare_website` schema and business facts already supplied. Ask only for missing required information. Do not invent names, testimonials, credentials, prices, contact details, domains or booking links. Omit unknown optional values. Send only the necessary brief fields, not conversation history, secrets or payment data.

Explain the boundary before saving: this stores a private brief for 24 hours; it does not generate or publish a website. The MCP tool requires sign-in and Website briefs Write (`mcp:brief:create`, with basic `mcp:read`). Website briefs has no Read mode. If access is missing, let the normal OAuth flow request the required capability; do not request unrelated categories or internal `mcp:write`.

Use a new request_id conforming to the current schema for each distinct brief. Saving a brief uses the dedicated OAuth permission directly, not the separate action-review page used for website edits. Follow any confirmation the host presents; never invent a review link or claim a review was approved. For an uncertain result, reuse the same request_id and identical formData and recommendations so the server can return the existing brief without duplication. A user-requested revision needs a new request_id.

Recommend up to three distinct templates in best-fit order using the catalogue metadata in the tool's recommendedTemplates schema and the user's business and design needs. Preserve both formData and recommendations on an identical retry; a user-requested revision needs a new request. The user makes the final template choice.

Return the actual handoff URL as a clearly labelled Markdown link, not only a decorative button or card. If the host's button does not open, provide the same returned URL without creating another brief. Describe recommendations by their actual catalogue names and fit; show preview images only when they come from the actual Pineapple template, never unrelated illustrative search results. Opening the link requires the same Pineapple account and leads to the existing template picker with ranked recommendations and the full catalogue. The user chooses a template, adjusts its style and reviews their prefilled editable details. Generation starts only when the user chooses it in Pineapple, subject to their plan and existing AI allowance. Never describe a brief, a template preview, or a handoff link as a generated website. Do not buy credits, upgrade a plan, or publish as part of this workflow.

If the link is expired or unavailable, explain that and ask whether the user wants a new brief. Never invent a replacement URL or claim that generation succeeded without observing the generated result.

When generation and saving are observed, describe the result as an editable website draft. The user is expected to review and personalise its text, images and contact details before publishing. That normal finishing step is not a generation failure. Still report specific mismatches with supplied facts honestly; do not call them corrected unless the saved result verifies the correction.
