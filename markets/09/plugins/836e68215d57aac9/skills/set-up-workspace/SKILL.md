---
name: set-up-workspace
description: Use when get_profile says `setup_required`, or a new Ciarem user wants to get started, set up their AI agent, or asks what to do first.
---

# Set up a new workspace

This skill also runs right after the plugin is installed, so start with `get_profile`. If `setup_required` is false, the workspace is already set up: skip these steps, say it's connected, and offer to show how the AI would answer a customer or what to improve.

Admins only: if a tool answers `requires_admin`, tell the user a workspace admin has to do the setup.

1. **Ask the onboarding questions**, one or two at a time, in the user's language: company name, industry, what they offer, their website (optional but it makes the AI much better), what the AI should help with (`objectives`), and which channels they will use. Don't guess an answer.
2. **Call `set_up_workspace`.** Write one `agents` entry per kind the objectives give (the tool description lists the mapping), with a short name and when-to-use in the language the AI should answer in. If it answers `invalid_arguments` naming the kinds, call again with exactly those. Share each `connect_channels` link from its answer right away: connecting WhatsApp, Instagram or Messenger needs their Meta login in the Ciarem web app, and it is the last step before the AI answers real customers. The web chat is the one channel that connects from here: when they have a website, offer it (the `add-web-chat` skill).
3. **Wait for the website.** While `get_setup_status` shows `website.ready: false`, tell the user it takes a few minutes, ask how they want the AI to sound (`update_ai_settings`: tone, reply length, welcome message), then check again. If `website.status` is `ERROR`, the site couldn't be read: say so and add the key facts (prices, hours, policies) with `add_knowledge_text` instead. The AI answers only from its knowledge, so with or without a website ask for what customers ask most (products or services with prices, hours and location, payment, delivery or booking, policies) and add each topic with `add_knowledge_text` to the `knowledge_base_id` that `set_up_workspace` returned. A business that sells products can list them in a catalog (the `product-catalog` skill).
4. **Show it working.** Call `test_ai_reply` with two or three messages a real customer of theirs would send (a price question, a hours or location question). If `knowledge_still_indexing` isn't empty, wait and test again. Fix what's off the way the `tune-ai-agent` skill does. Share `playground_url` so they can keep trying the AI in the web app, with no Meta login.
5. **Finish.** When the user likes the answers, call `finish_setup` and remind them to connect a channel.

If any tool answers `subscription_required`, stop and share the payment link it gives.
