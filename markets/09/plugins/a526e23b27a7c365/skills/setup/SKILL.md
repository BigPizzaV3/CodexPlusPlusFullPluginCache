---
name: setup
description: First-run setup for Adly. Use whenever the user has no brand yet, the first time they use Adly, or when they ask to set up, connect or get started. Creates their brand, then checks which social accounts are connected.
---

Welcome the user to Adly in one short sentence, then run these steps in order. Never design anything before a brand exists, and never invent a brand.

1. Call list_brands. If it says the account cannot add another brand and the user asked for a new one, say so before collecting any details and offer to use or update the existing brand. If the user already has a brand, show its name and ask whether to use it, then call select_brand and go to step 4.
2. If there is no brand, ask for these in one short message: the business name, what it sells or does, the language for their posts, and their website if they have one. Wait for the answers.
3. Call create_brand with them. Use a short category such as "Restaurant", "Clothing store" or "Marketing agency", and write a one or two sentence description from what the user said. Then ask for their logo: Adly takes the colors and style of every design from it, so designs look generic without one. They can send the logo image here in the chat: call upload_product_image with it, then update_brand with logo_url set to the returned image_url. A logo link or their website also works.
4. Call list_social_accounts and tell the user which of Facebook, Instagram, LinkedIn, X and TikTok are connected. If one is missing, tell them to connect it once at https://getadly.com in Settings, then come back. Do not try to connect accounts from chat.
5. Finish by offering three things to try: a single post design, a 5-slide carousel, or a short video. Answer in the user's language.

Creating content counts toward the user's Adly usage limit. Mention that once, plainly.
