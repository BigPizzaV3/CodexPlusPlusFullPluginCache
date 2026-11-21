---
name: ugc-product-video
description: Create a finished creator-style product video in Clout using an owned product and AI influencer with a reviewed brief and credit quote
---

# UGC product video

Use this for a creator-led product promotion, demonstration, or everyday-use scene. Read [the shared workflow](../../references/creative-workflow.md) first. Do not present an AI performance as a real customer's verified experience.

1. Clarify the product, audience, platform/format, intended length, and one concrete message. Prefer supplied product facts and claims. Do not invent efficacy, results, price, offers, endorsements, testimonials, or guarantees.
2. Find the product with `clout_list_products` and the creator with `clout_list_influencers` / `clout_get_influencer`. If the product is missing, use an authorized product upload/analyze/save flow or `clout_import_product` for the exact public URL the user supplied. Review extracted facts and wait for ready product images.
3. Plan a natural hook, demonstration or benefit grounded in the product profile, and a concise ending. Align visuals with what can be shown, avoiding unsupported claims. Confirm speech, aspect ratio, and creative direction using supported schema choices.
4. Create an owned video project with `clout_create_ugc_project`. This does not itself render a finished video. Preserve the returned project ID and ready influencer/product references.
5. Quote `clout_generate_product_video` with the complete input. This full product-video operation includes its own planning/frame/video stages; do not charge or quote unrelated stages as substitutes. Generate using existing credits without asking for separate credit approval.
6. Call `clout_generate_product_video` using existing credits and one UUID request ID preserved across retries. Poll `clout_get_ugc_video` for planning, frame, and video progression.
7. Deliver the actual completed media using `clout_get_download`. Check product appearance, creator continuity, speech pacing, and whether visible claims match the approved facts. Report failed/pending stages precisely.

For a template-led marketing UGC variation, `clout_list_templates` and `clout_generate_marketing` can be the better workflow; use the `marketing-campaign` skill. Do not silently launch both flows. Additional hooks, language versions, or variants require a new explicit brief and quote.

Follow the shared direct-generation policy: no extra credit-approval step. Immediately show the returned Clout job with `clout_show_generation`; never substitute native ChatGPT image generation or another provider.
