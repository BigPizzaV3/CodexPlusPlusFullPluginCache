---
name: flow-get-started
description: Explain AI Video Generator Flow and check the connected account when a user asks to set up or start using Flow image and video generation.
---

# Start using AI Video Generator Flow

Flow creates images and videos through a connected Flow account. Explain briefly that generation uses that account's existing credits and model entitlements. Never ask for a password, API key, OAuth token, or payment details in the conversation.

1. If the account is not connected, use the host's connection flow. Do not construct authorization URLs or suggest sharing credentials.
2. When the user asks what is available, call `list_models`. Report the live supported settings instead of a static list of provider brands.
3. When the user asks about their balance or before planning generation that needs credits, call `get_credits`. Do not buy credits, change a subscription, offer discounts, or direct the user to checkout.
4. Ask for a creative brief only if the user's requested image or video lacks essential information. For generation, follow `flow-create-media`.

The four workflows are text-to-image, AI photo editing, text-to-video, and image-to-video. Reference workflows require a completed supported upload or a usable image already belonging to the connected account. Use the available upload tools and their live schemas; never invent a file URL or claim a ChatGPT attachment was imported before the server confirms it. If the current client cannot supply the upload, explain the available supported upload path. Do not silently omit the user’s reference.

Do not generate sample media merely to demonstrate setup. Setup and account checks do not authorize spending credits.
