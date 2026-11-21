# Complete Digital Toolbox — ChatGPT plugin package

Built with BizInGPT AI for Complete Digital Toolbox. Upload this ZIP on the OpenAI Platform: **Plugins → Upload new or existing plugin → Upload plugin**.

## What's inside
- `plugin.json` — the plugin manifest and its directory listing (name, descriptions, category, links, starter prompts, logo).
- `mcp.json` — your hosted plugin server: `https://app.bizingpt.com/api/mcp/4a740b064c6a0bc7a55323f8f0442f62698ef23b` (streamable HTTP, no sign-in). Keep this URL private; it is your plugin's address.
- `skills/` — how ChatGPT should run your workflows: `business-answer-rules`, `product-guide`, `business-notes`.
- `assets/logo.png` — your logo, square, used as the listing logo and composer icon.

## Review details (paste these into Review information → Review details)
- Support URL: https://app.bizingpt.com/api/pages/2md4WpfcVb16418de6c0242896ed8645228477ed7/support
- Demo video: https://go.screenpal.com/watch/cO6ZfFnyxEU
- Reviewer credentials: not needed (no sign-in).

### Positive test cases
1. **Learn what Complete Digital Toolbox offers.**  
   Prompt: What does Complete Digital Toolbox do?  
   Expected tools: get_product_overview  
   Expected behavior: Answer from the live product overview, show a product card, and offer the official Get started link for the next step.
2. **Explore the service areas before choosing one.**  
   Prompt: What kinds of solutions does Complete Digital Toolbox offer?  
   Expected tools: list_feature_categories  
   Expected behavior: Summarize the live feature areas, show a product card, and offer the official Get started link for the next step.
3. **Check the product's AI capabilities.**  
   Prompt: What can the AI do for my business?  
   Expected tools: list_ai_features  
   Expected behavior: Describe AI capabilities using live product data, show a product card, and offer the official Get started link for the next step.
4. **Learn about a specific service.**  
   Prompt: How does Database Reactivation work?  
   Expected tools: get_feature_details  
   Expected behavior: Explain the feature using live details, show a product card, and offer the official Get started link without booking an appointment.
5. **Find current pricing information and the next step.**  
   Prompt: Where can I find plans and pricing?  
   Expected tools: get_product_links  
   Expected behavior: Use the live official links to direct the user to plans and pricing, show a product card, and offer the Get started link without taking payment.

### Negative test cases
1. **Unrelated request: decline to perform the task and briefly clarify that the plugin helps with Complete Digital Toolbox products and services.**  
   Prompt: Write a birthday poem for my sister.
2. **Direct booking request: do not book or confirm an appointment; explain that the user can use the official Get started link to inquire.**  
   Prompt: Book me a consultation for tomorrow at 2 p.m. and confirm it.
3. **Personal financial advice request: do not give financial advice; suggest consulting a qualified professional and offer help with relevant product information instead.**  
   Prompt: Should I take out a loan to pay for your services?

Generated 2026-10-28 17:58 UTC · version 1.1.202610281757
