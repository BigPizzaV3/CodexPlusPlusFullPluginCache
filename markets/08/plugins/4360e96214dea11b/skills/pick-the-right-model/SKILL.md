---
name: pick-the-right-model
description: Use when choosing an image or video model for a FXI Studio generation, or when the user asks about cost, speed, or quality. Teaches the cost/speed tiers, the fast defaults, and when a pricier model is actually worth it.
---

1. Call `list_models` before picking a model you have not already confirmed with
   the user this conversation. Each entry returns `speed_tier` (fast, balanced, or
   quality), `credits`, `typical_seconds` when known, and `best_for`.
2. Default to the fast, lowest-cost model unless the user names a different model
   or explicitly asks for higher detail:
   - Images default to `z-image-turbo`.
   - Video defaults to `p-video-2`.
3. Do not upgrade to a pricier model just because the prompt reads as cinematic,
   premium, or photoreal. A fast model handles most drafts.
4. For dialogue, multi-shot continuity, or complex camera moves, suggest
   `seedance-2-mini` and state its credit cost from `list_models` before switching
   — it costs more but is the right tool for those cases.
5. When a higher-detail image option exists (for example `nano-banana-2` or
   `nano-banana-pro`), name it and its price from `list_models`, and only switch
   once the user agrees. An explicit model request from the user always runs
   exactly as asked, at its listed price — never silently downgrade it to save
   credits.
6. Call `get_credits` before a generation if the user's balance might be close to
   the cost. If a call returns `insufficient_credits`, tell the user their actual
   balance and share the `next_step_url` from the result — don't just say the
   generation failed.
7. State credit costs honestly. Never describe a generation as "free" when it
   spends credits, and never use manufactured urgency ("only a few credits left!")
   to push a purchase. Refused or failed generations are not charged — say so if
   one errors out, so the user isn't left thinking they lost credits.
