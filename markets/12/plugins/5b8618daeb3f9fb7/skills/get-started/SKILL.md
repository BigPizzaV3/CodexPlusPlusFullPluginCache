---
name: get-started
description: Help a user who asks to set up Designkit, browse its available experts
  or presets, or choose a first marketing design workflow. Do not activate for every
  ordinary creation or revision request.
---

# Get started with Designkit

When the user wants to browse or open the visual studio, use the available `designkit_open_studio` tool (or `designkit_open_studio_panel` in a conversation). Opening the studio is read-only and does not authorize generation. Do not invent a tool if it has not appeared: use the workflow menu below instead and explain that the visual studio requires a compatible ChatGPT host and an updated Designkit connection. The sidebar/fullscreen entry is separate from the five packaged skills. If a complete creative request is already given, follow its expert workflow directly rather than forcing a trip through the studio.


Read [the workflow menu](references/workflow-menu.json) when the user asks what is available or needs help choosing a workflow. Offer the five expert entries with relevant examples instead of dumping every preset. Support natural-language choices; local aliases are not required.

- New marketplace/product assets, including A+: `ecommerce-design`.
- New promotional or social visuals: `social-campaign-design`.
- New identity concepts and branded applications: `brand-visual-design`.
- Changes to an existing design: `design-revision`.
- Product promotion, UGC-style or close-up video generation, briefs and shot plans: `video-creation`.

Follow the chosen packaged skill and its selected preset. Reuse context rather than repeating the whole briefing process. If the user has already asked for a specific design, hand over that request directly. Browsing or setup alone does not authorize a paid sample.

Use the host's normal account-connection flow if tools require login. Never ask for passwords, email codes, tokens or API keys in chat. Explain account credit use when relevant. Authentication does not authorize unrelated generation, public sharing, purchases or a change of account.

Images and videos use the same `designkit_create_task` tool, with progress and actual media from `designkit_get_artifacts`. The absence of a separate video tool does not mean video generation is unavailable. `designkit_get_profile` identifies the connected account; it is not a capability inventory.

For video requests, distinguish a concept or storyboard from an actual completed video, and follow the video expert's returned-media checks. Do not claim live competitor metrics, social-account access, automatic publishing, precise layering, manufacturing output, voice cloning or garment fitting unless an available tool actually supports the requested operation. Explain a specific missing capability and offer a relevant available workflow when helpful.
