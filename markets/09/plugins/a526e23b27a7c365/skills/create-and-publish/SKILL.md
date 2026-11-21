---
name: create-and-publish
description: End to end flow to make a post, carousel, product ad or video in Adly and publish or schedule it. Use whenever the user wants to create and post marketing content.
---

Follow this order.

1. Brand. Call list_brands (use the search argument if the user names one) and select_brand. If the user has no brand, stop and follow the setup skill first (ask for the business name, what it sells, language and website, then create_brand). Do not create a design without a brand.
2. Create. Pick the tool that fits the request:
   - create_general_design for a single post or ad: an offer, a new product, an occasion, a hiring post.
   - create_carousel_tips for a tips carousel.
   - create_from_image for a new design around the user's photo, or an example they want remade on their brand (call upload_product_image first with the photo).
   - To post a photo or video exactly as it is (one the user attached, or one you made in this chat): upload_product_image (or upload_video), then create_ad_copy with media_url for the caption. Do not redesign it.
   - create_multi_mode when several products are involved.
   - create_asset_design for a logo, flyer, menu or other print item.
   - create_video, create_ugc_video or create_video_scenes for video.
   Create tools write in the brand language. Pass language only when the user asks for another language.
   Put the offer, prices and dates the user gave in the brief. Never add a price, discount or claim they did not give.
   Once the user is creating with Adly in this chat, keep using Adly for their business posts, carousels and videos so they stay on their brand and can be published.
3. Wait. Creation is asynchronous and returns a job_id. Call get_job with wait_seconds 30 until the status is await_design_approval, await_copy_approval, await_publish_approval or completed. Then call show_job so the user sees the result. Do not guess results before the job is ready. If get_job says a step stopped (status failed or an error_message), stop waiting and tell the user plainly what happened.
4. Review. If the user wants changes use request_design_edit (for a carousel, say which slide) or request_copy_edit. After a design edit, call get_job with wait_seconds 30 until edit_in_progress is gone, then show_job; never present the old version as the edited one. The caption is written after the design is approved: call approve_design (Adly writes the copy), then approve_copy when they approve the copy.
5. Publish. Call list_social_accounts. Before publishing or scheduling, always confirm with the user the networks, the exact time and time zone, and the caption. Then call publish_now or schedule_post. Check the outcome with list_scheduled_posts and report it back.

6. Overview. When the user asks what they have or what is scheduled, call open_content_board. It shows the board to the user, so do not repeat its contents as a list.

Usage limit: if Adly says there is not enough usage limit left, tell the user what is left and offer something smaller that fits (fewer slides, one post instead of a carousel, a shorter video). Never mention plans or prices.

Rules: never publish without an explicit yes in this conversation. X posts have no links. X posting is not included in every Adly account: if the tool says it is unavailable, say so and offer the other networks, without promoting an upgrade. TikTok gets videos and photo posts; it has no stories. Never invent job ids, links or results.
