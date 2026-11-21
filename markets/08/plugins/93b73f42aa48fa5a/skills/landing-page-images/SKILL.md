---
name: landing-page-images
description: Create product landing-page section images with the UGCBuilder MCP. Use for UGCBuilder landing pages, product creative sections, or adapting supplied copy into landing-page images.
---

Use the connected UGCBuilder MCP and its current advertised tool schemas. Authenticate through the client's OAuth connection flow; never ask for passwords or embed tokens in files. If connection is required, present the connection flow.

Preserve the user's supplied product image, exact approved copy, language or dialect, section order, aspect ratio, and offer. Do not replace an explicit image reference. Prefer the attached product image when the tool accepts it. Chat attachments are not public HTTPS URLs; never invent image URLs. Ask only for genuinely missing required inputs.

For a complete page without a supplied structure, use Hero, Before & After, Ingredients / Features, Authority / Trust, How to Use, and Social Validation. Adapt ingredients to components/features where appropriate. Use custom section types for sections without a native mapping. Do not invent reviews, endorsements, certifications, scarcity, medical outcomes, or product facts. Frame before/after around supportable use cases. Respect requested Moroccan Darija, RTL hierarchy, and copy formatting.

Prefer prepare_landing_page for one or multiple sections. Supply the original requirements and exact requested copy in userBrief, with a product-specific design prompt for every section. Maintain consistent colors, typography, product identity, and visual hierarchy. The card collects format and total-credit approval and starts generation. Preparing the card does not spend credits; do not ask a separate format or budget question before opening it. Do not additionally call generate_landing_page for sections submitted through that card.

Use direct generate_landing_page only with a user-selected supported aspect ratio and sufficient explicit credit authorization for the entire requested set. Check current account prices when needed; never infer a credit budget from a request alone. Reuse the exact idempotency key and identical arguments for a retry. Do not retry an uncertain charge as a new request.

Use get_landing_page_request for prepared-request status, or get_generation for direct jobs. Immediately share returned downloadMarkdown as sections complete, with the expiry time. Poll direct jobs no more often than every 10 seconds. Retrieve existing jobs when the user asks for links; do not regenerate. Explain actual failure or expiry without claiming success. These outputs are section images, not published HTML websites. Use a separate authorized workflow if a working website is requested.
