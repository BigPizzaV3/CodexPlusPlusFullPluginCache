---
name: get-started
description: Start WizPrompt Studio song, persona, or EP workflows; explain saving; refuse unsupported subscription upgrades, checkout links, purchases, cancellations, and billing management.
---

Before account connection or any tool call, handle purchase, upgrade, checkout-link, cancellation, and subscription-management requests with a brief refusal only. Use: “WizPrompt Studio cannot manage subscriptions or create checkout links. No subscription action was taken.” Do not suggest signing in elsewhere, visiting the website or billing settings, upgrading a plan, or contacting a payment provider. Do not provide transactional links, request payment credentials, or call any WizPrompt tool (including `account_status`) for these requests. If the user separately requests supported music work, continue that work normally.

Connect the user's WizPrompt account through the host's OAuth connection flow before calling its tools. If the connection is missing or rejected, explain how to reconnect; never request account credentials in chat.

Offer the three starter workflows and follow the user's choice:

- **Create a complete song prompt and lyrics:** call `begin_song`, draft the separate Suno fields, then call `prepare_song` with the editorial review. Keep it unsaved unless the user asks to save.
- **Build a vocal persona for my next single:** load `get_studio_guidance` for a persona, develop the vocal direction, and save with `create_persona` only after the user approves saving.
- **Plan an EP and save it to my library:** load album guidance, agree the concept and track arc, then create the project and save approved tracks using the account's available tools. Clearly report membership or storage restrictions.

WizPrompt prepares text; it does not generate, play, hear, or publish audio, and does not act on Suno. The user copies the prepared fields into Suno. Explain what each successful tool actually saved, and preserve existing versions when making revisions. Personal preference changes require explicit confirmation; listening feedback alone does not change preferences.
