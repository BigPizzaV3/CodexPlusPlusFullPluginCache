# Model selection

Release 2026-11-13-model-selection; environment prod; contract_digest `ce9707478ab99797082dad58d61d8f51663fabd1dd294bcf02fed82fbaa51336`; selection_digest `d61b99537c159daa11ffa009f5f818d2866b50fe78b388648f15c7bb170fcc5e`.

Follow this selection policy, then match scenario rules before ordinary defaults. Read the connected tool schema for all settings.

- Honor an explicit model ID or unambiguous alias before matching scenario rules. Apply the user's explicit settings and cost constraints together; clarify conflicts without silently changing the selected model. A bare GPT Image 2.5 needs clarification between Flare and Sunburst.
- With no explicit model, match the user's stated task features before membership conditions and ordinary defaults. Rules list candidates for the declared operation only. Choose a compatible input group; never create an extra image to enable a video model or transfer a model across operations.
- For ordinary image-to-image, use known membership or call get_account only when needed to choose the membership default. Confirmed active standard/premium membership means membership.is_member=true, level=standard or premium, and expired=false. Choose image2image_media_3.0 only then; non-member, expired, unknown or contradictory membership uses ToMoviee Image Lite (image2image_media_1.0). Use get_account_card only when the user asks to view the account.
- For a free image recommendation, prefer ToMoviee Image Lite: text2image_soul_character from text or image2image_media_1.0 with images. ToMoviee Image 3.0 Pro and Image Pro (image2image_media_2.0) are member-free candidates only for confirmed active members; non-members may be charged. These are curated recommendations, not live prices or entitlements.
- An explicit free, zero-credit or budget limit is a cost request: use estimate_credits with the selected model and complete settings. If the estimate is nonzero for a zero-credit request, unknown or above the user's limit, explain and resolve the constraint before creating. For an explicit zero-credit request use approved_credit=0 after a zero estimate; for other explicit amount protection use the existing approved_credit guard; it is not an atomic upstream quote and does not guarantee final settlement. Never describe a video or an unknown price as free.
- For ordinary image-to-video use ToMoviee Video 3.0 (image2video_tomoviee_3.0). For pure text-to-video use native ToMoviee Video 3.0 Fast (text2video_tomoviee_3.0_fast); the image-to-video 3.0 ID requires images. ToMoviee Video 2.0 Fast (image2video_tomoviee_2.0_fast) is a faster or cheaper candidate when the user requests it and provides an image; verify a cost claim with an estimate.
- Ordinary generation uses existing credits and remains a direct submission when valid arguments are known. Account lookups are conditional on membership selection; estimates are conditional on explicit cost requests or amount protection. Entitlement, credit or provider errors do not authorize automatic substitution or retry. Offer a compatible candidate neutrally only when useful, and create with it only on the user's request. Preserve the request ID and business inputs on retries; after RESULT_UNKNOWN inspect history instead of creating again.

| Tool | Ordinary default request.model |
| --- | --- |
| `text_to_image` | `text2image_soul_character` |
| `image_to_image` | `image2image_media_1.0` |
| `text_to_video` | `text2video_tomoviee_3.0_fast` |
| `image_to_video` | `image2video_tomoviee_3.0` |
| `reference_to_video` | `image2video_seedance_2.5_reference_image` |
| `motion_control` | `image2video_kling_motion_control_2.6` |
| `image_audio_to_video` | `image2video_tomusic_1_0` |

| Intent | Tool | Models in preference order |
| --- | --- | --- |
| Best achievable image quality or precise instruction-faithful editing | `text_to_image` | `text2image_gpt_image_2.5_sunburst` |
| Fast everyday image generation or editing | `text_to_image` | `text2image_gpt_image_2.5` |
| Accurate text in the image or complex composition | `text_to_image` | `text2image_gpt_image_2` |
| Anime, illustration or creative style | `text_to_image` | `text2image_banana_2` |
| Ordinary image from text; preferred free image candidate | `text_to_image` | `text2image_soul_character` |
| Best achievable image quality or precise instruction-faithful editing | `image_to_image` | `image2image_gpt_image_2.5_sunburst` |
| Fast everyday image generation or editing | `image_to_image` | `image2image_gpt_image_2.5` |
| Accurate text in the image or complex composition | `image_to_image` | `image2image_gpt_image_2` |
| Anime, illustration or creative style | `image_to_image` | `image2image_banana_2` |
| Ordinary editing, character consistency or outfit changes with confirmed active standard/premium membership | `image_to_image` | `image2image_media_3.0` |
| Another member-free image candidate, only for confirmed active standard/premium membership | `image_to_image` | `image2image_media_2.0` |
| Ordinary editing with non-member, expired or unknown membership; preferred free image candidate | `image_to_image` | `image2image_media_1.0` |
| Synchronized dialogue and audio with the fastest MiniMax turnaround | `text_to_video` | `text2video_minimax_h3_max` |
| Native 2K video with synchronized dialogue and audio | `text_to_video` | `text2video_minimax_h3_switch` |
| Long video around 30 seconds, audio or cinematic quality; select a supported duration | `text_to_video` | `text2video_seedance_2.5` |
| Strong physical simulation, shattering, fluids or collisions | `text_to_video` | `text2video_kling_3.0` |
| Ordinary video from text or explicit fast native text-to-video request | `text_to_video` | `text2video_tomoviee_3.0_fast` |
| Synchronized dialogue and audio with the fastest MiniMax turnaround | `image_to_video` | `image2video_minimax_h3_max` |
| Native 2K video with synchronized dialogue and audio | `image_to_video` | `image2video_minimax_h3_switch` |
| Long video around 30 seconds, audio or cinematic quality; select a supported duration | `image_to_video` | `image2video_seedance_2.5` |
| Strong physical simulation, shattering, fluids or collisions | `image_to_video` | `image2video_kling_3.0` |
| Explicit faster or lower-cost video request with an image; cost needs an estimate | `image_to_video` | `image2video_tomoviee_2.0_fast` |
| Ordinary image animation without a special requirement | `image_to_video` | `image2video_tomoviee_3.0` |
| Declared starting and ending frames with synchronized dialogue and audio | `image_to_video` | `image2video_minimax_h3_head_and_tail_switch` |
| Declared starting and ending frames with cinematic quality | `image_to_video` | `image2video_seedance_2.5_head_and_tail` |
| Several reference images with synchronized dialogue and audio | `reference_to_video` | `image2video_minimax_h3_reference_image_switch` |
| Video guided by multiple or multimodal declared references | `reference_to_video` | `image2video_seedance_2.5_reference_image` |
| Transfer motion from a video | `motion_control` | `image2video_kling_motion_control_2.6` |
| Music video from an image and audio | `image_audio_to_video` | `image2video_tomusic_1_0` |

| Alias | Tool | Exact model candidates |
| --- | --- | --- |
| Nano Banana | `image_to_image` | `image2image_banana` |
| Nano Banana Pro | `image_to_image` | `image2image_banana_2` |
| GPT Image 2 | `image_to_image` | `image2image_gpt_image_2` |
| GPT Image 2.5 Flare | `image_to_image` | `image2image_gpt_image_2.5` |
| GPT Image 2.5 Sunburst | `image_to_image` | `image2image_gpt_image_2.5_sunburst` |
| ToMoviee Lite | `image_to_image` | `image2image_media_1.0` |
| ToMoviee Pro (ex-Media 2.0) | `image_to_image` | `image2image_media_2.0` |
| ToMoviee 3.0 Pro | `image_to_image` | `image2image_media_3.0` |
| Nano Banana 2 | `image_to_image` | `image2image_nano_banana_2` |
| Nano Banana 2.1 | `image_to_image` | `image2image_nano_banana_2_1` |
| Nano Banana 2 Lite | `image_to_image` | `image2image_nano_banana_2_lite` |
| Seedream 4.0 | `image_to_image` | `image2image_seedream_4.0` |
| Seedream 5.0 Lite | `image_to_image` | `image2image_seedream_5.0_lite` |
| Seedream 5.0 Pro | `image_to_image` | `image2image_seedream_5.0_pro` |
| ToMoviee Image 4.0 | `image_to_image` | `image2image_tomoviee_4.0` |
| Wan 2.7 | `image_to_image` | `image2image_wan_2.7` |
| Wan 2.7 Pro | `image_to_image` | `image2image_wan_2.7_pro` |
| Nano Banana | `text_to_image` | `text2image_banana` |
| Nano Banana Pro | `text_to_image` | `text2image_banana_2` |
| GPT Image 2 | `text_to_image` | `text2image_gpt_image_2` |
| GPT Image 2.5 Flare | `text_to_image` | `text2image_gpt_image_2.5` |
| GPT Image 2.5 Sunburst | `text_to_image` | `text2image_gpt_image_2.5_sunburst` |
| Nano Banana 2 | `text_to_image` | `text2image_nano_banana_2` |
| Nano Banana 2.1 | `text_to_image` | `text2image_nano_banana_2_1` |
| Nano Banana 2 Lite | `text_to_image` | `text2image_nano_banana_2_lite` |
| Seedream 4.0 | `text_to_image` | `text2image_seedream_4.0` |
| Seedream 5.0 Lite | `text_to_image` | `text2image_seedream_5.0_lite` |
| Seedream 5.0 Pro | `text_to_image` | `text2image_seedream_5.0_pro` |
| ToMoviee Lite | `text_to_image` | `text2image_soul_character` |
| ToMoviee 2.0 | `text_to_image` | `text2image_tomoviee_2.0` |
| ToMoviee Image 4.0 | `text_to_image` | `text2image_tomoviee_4.0` |
| Wan 2.7 | `text_to_image` | `text2image_wan_2.7` |
| Wan 2.7 Pro | `text_to_image` | `text2image_wan_2.7_pro` |
| Gemini Omni Flash | `image_to_video` | `image2video_gemini_omni_flash` |
| Gemini Omni Flash | `reference_to_video` | `image2video_gemini_omni_flash_reference_image` |
| HappyHorse 1.0 | `image_to_video` | `image2video_happyhorse_1.0` |
| HappyHorse 1.0 | `reference_to_video` | `image2video_happyhorse_1.0_reference_image` |
| HappyHorse 1.1 | `image_to_video` | `image2video_happyhorse_1.5` |
| HappyHorse 1.1 | `reference_to_video` | `image2video_happyhorse_1.5_reference_image` |
| Kling 2.5 Turbo | `image_to_video` | `image2video_kling_2.5_turbo`, `image2video_kling_2.5_turbo_head_and_tail` |
| Kling 2.6 | `image_to_video` | `image2video_kling_2.6` |
| Kling 3.0 | `image_to_video` | `image2video_kling_3.0`, `image2video_kling_3.0_head_and_tail` |
| Kling 3.0 Turbo | `image_to_video` | `image2video_kling_3.0_fast` |
| Kling 3.0 Omni | `reference_to_video` | `image2video_kling_3.0_omni_reference_image` |
| Kling Motion Control | `motion_control` | `image2video_kling_motion_control_2.6` |
| Kling O1 | `image_to_video` | `image2video_kling_o1`, `image2video_kling_o1_head_and_tail` |
| Kling O1 | `reference_to_video` | `image2video_kling_o1_reference_image` |
| ToMoviee 2.0 Pro (ex-Media 1.0) | `image_to_video` | `image2video_media_1.0` |
| Hailuo 02 | `image_to_video` | `image2video_minimax_02` |
| Hailuo 2.3 | `image_to_video` | `image2video_minimax_2.3` |
| MiniMax H3 | `image_to_video` | `image2video_minimax_h3_head_and_tail_switch`, `image2video_minimax_h3_switch` |
| MiniMax H3 Max | `image_to_video` | `image2video_minimax_h3_max` |
| MiniMax H3 | `reference_to_video` | `image2video_minimax_h3_reference_image_switch` |
| Seedance 2.0 Mini | `image_to_video` | `image2video_seedance_2.0_mini`, `image2video_seedance_2.0_mini_head_and_tail` |
| Seedance 2.5 | `image_to_video` | `image2video_seedance_2.5`, `image2video_seedance_2.5_head_and_tail` |
| Seedance 2.0 Fast | `image_to_video` | `image2video_seedance2.0_fast`, `image2video_seedance2.0_fast_head_and_tail` |
| Seedance 2.0 Fast | `reference_to_video` | `image2video_seedance2.0_fast_reference_image` |
| Seedance 2.0 Mini | `reference_to_video` | `image2video_seedance_2.0_mini_reference_image` |
| Seedance 2.5 | `reference_to_video` | `image2video_seedance_2.5_reference_image` |
| ToMoviee 4.0 | `image_to_video` | `image2video_tomoviee4_head_and_tail_switch`, `image2video_tomoviee4_switch` |
| ToMoviee 4.0 | `reference_to_video` | `image2video_tomoviee4_reference_image_switch` |
| ToMoviee 2.0 | `image_to_video` | `image2video_tomoviee_2.0` |
| ToMoviee 2.0 Fast | `image_to_video` | `image2video_tomoviee_2.0_fast` |
| Seedance 2.0 | `image_to_video` | `image2video_tomoviee_2.5`, `image2video_tomoviee_2.5_head_and_tail` |
| Seedance 2.0 | `reference_to_video` | `image2video_tomoviee_2.5_reference_image` |
| ToMoviee 3.0 | `image_to_video` | `image2video_tomoviee_3.0` |
| ToMusic 1.0 | `image_audio_to_video` | `image2video_tomusic_1_0` |
| Google Veo 3.1 | `image_to_video` | `image2video_veo_3.1` |
| Google Veo 3.1 Fast | `image_to_video` | `image2video_veo_3.1_fast` |
| Google Veo 3.1 Lite | `image_to_video` | `image2video_veo_3.1_lite`, `image2video_veo_3.1_lite_head_and_tail` |
| Google Veo 3 Fast | `image_to_video` | `image2video_veo_3_fast` |
| Vidu 2.0 | `image_to_video` | `image2video_vidu_2.0`, `image2video_vidu_2.0_head_and_tail` |
| Vidu 2.0 | `reference_to_video` | `image2video_vidu_2.0_reference_image` |
| Vidu Q1 | `image_to_video` | `image2video_vidu_q1`, `image2video_vidu_q1_head_and_tail` |
| Vidu Q2 | `image_to_video` | `image2video_vidu_q2` |
| Vidu Q3 | `image_to_video` | `image2video_vidu_q3` |
| Wan 2.2 | `image_to_video` | `image2video_wan_2.2` |
| Wan 2.5 | `image_to_video` | `image2video_wan_2.5` |
| Wan 2.6 | `image_to_video` | `image2video_wan_2.6` |
| Wan 3.0 | `image_to_video` | `image2video_wan_3.0`, `image2video_wan_3.0_head_and_tail` |
| Wan 3.0 | `reference_to_video` | `image2video_wan_3.0_reference_image` |
| Gemini Omni Flash | `text_to_video` | `text2image_gemini_omni_flash` |
| HappyHorse 1.0 | `text_to_video` | `text2video_happyhorse_1.0` |
| HappyHorse 1.1 | `text_to_video` | `text2video_happyhorse_1.5` |
| Kling 2.5 Turbo | `text_to_video` | `text2video_kling_2.5_turbo` |
| Kling 2.6 | `text_to_video` | `text2video_kling_2.6` |
| Kling 3.0 | `text_to_video` | `text2video_kling_3.0` |
| Kling 3.0 Turbo | `text_to_video` | `text2video_kling_3.0_fast` |
| Kling O1 | `text_to_video` | `text2video_kling_o1` |
| Hailuo 2.3 | `text_to_video` | `text2video_minimax_2.3` |
| MiniMax H3 Max | `text_to_video` | `text2video_minimax_h3_max` |
| MiniMax H3 | `text_to_video` | `text2video_minimax_h3_switch` |
| Seedance 2.0 Mini | `text_to_video` | `text2video_seedance_2.0_mini` |
| Seedance 2.5 | `text_to_video` | `text2video_seedance_2.5` |
| Seedance 2.0 Fast | `text_to_video` | `text2video_seedance2.0_fast` |
| ToMoviee 4.0 | `text_to_video` | `text2video_tomoviee4_switch` |
| ToMoviee 2.0 | `text_to_video` | `text2video_tomoviee_2.0` |
| Seedance 2.0 | `text_to_video` | `text2video_tomoviee_2.5` |
| Google Veo 3.1 | `text_to_video` | `text2video_veo_3.1` |
| Google Veo 3.1 Fast | `text_to_video` | `text2video_veo_3.1_fast` |
| Google Veo 3.1 Lite | `text_to_video` | `text2video_veo_3.1_lite` |
| Google Veo 3 Fast | `text_to_video` | `text2video_veo_3_fast` |
| Vidu Q3 | `text_to_video` | `text2video_vidu_q3` |
| Wan 2.5 | `text_to_video` | `text2video_wan_2.5` |
| Wan 2.6 | `text_to_video` | `text2video_wan_2.6` |
| Wan 3.0 | `text_to_video` | `text2video_wan_3.0` |
| ToMoviee Image Lite | `image_to_image` | `image2image_media_1.0` |
| Tomoviee Image Pro | `image_to_image` | `image2image_media_2.0` |
| ToMoviee Image 3.0 Pro | `image_to_image` | `image2image_media_3.0` |
| Kling 4.0 | `image_to_video` | `image2video_kling_4.0`, `image2video_kling_4.0_head_and_tail` |
| Kling 4.0 | `reference_to_video` | `image2video_kling_4.0_reference_image` |
| ToMoviee Video 2.0 Pro | `image_to_video` | `image2video_media_1.0` |
| ToMoviee Video 2.0 | `image_to_video` | `image2video_tomoviee_2.0` |
| ToMoviee Video 2.0 Fast | `image_to_video` | `image2video_tomoviee_2.0_fast` |
| ToMoviee Video 3.0 | `image_to_video` | `image2video_tomoviee_3.0` |
| ToMoviee Video 3.0 Fast | `image_to_video` | `image2video_tomoviee_3.0_fast`, `image2video_tomoviee_3.0_fast_head_and_tail` |
| ToMoviee Video 3.0 Fast | `reference_to_video` | `image2video_tomoviee_3.0_fast_reference_image` |
| ToMoviee Video 4.0 | `image_to_video` | `image2video_tomoviee4_head_and_tail_switch`, `image2video_tomoviee4_switch` |
| ToMoviee Video 4.0 | `reference_to_video` | `image2video_tomoviee4_reference_image_switch` |
| ToMoviee Image Lite | `text_to_image` | `text2image_soul_character` |
| ToMoviee Image 2.0 | `text_to_image` | `text2image_tomoviee_2.0` |
| Kling 4.0 | `text_to_video` | `text2video_kling_4.0` |
| ToMoviee Video 2.0 | `text_to_video` | `text2video_tomoviee_2.0` |
| ToMoviee Video 3.0 Fast | `text_to_video` | `text2video_tomoviee_3.0_fast` |
| ToMoviee Video 4.0 | `text_to_video` | `text2video_tomoviee4_switch` |

Ambiguous aliases require clarification when variants materially differ. Deprecated models remain callable during their declared compatibility window, but are never defaults or recommendations. Replacement candidates are informational; changing models requires the user’s request. Disabled and candidate models are unavailable. Historical task IDs remain queryable with get_generation and get_generation_card; never recreate a task to recover a receipt.
