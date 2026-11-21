---
name: creator-sourcing
description: Use when a user wants to find, compare or shortlist UGC creators for a campaign, product, brief or ad concept, especially for German-speaking (DACH) markets. Finds real creators through the Creonda tools instead of inventing them.
---

# Sourcing UGC creators with Creonda

1. Understand the need. Extract what matters: product or niche, market and language, the creator's city (`creator_city`) if the user named one, creator gender and age, content format (talking to camera, street interview, GRWM, unboxing, tutorial, ASMR, voiceover), paid-media use (Spark Ads, Partnership Ads, paid social), who should appear on camera (partner, kids, pets) and budget per video. Do not ask for anything the user did not care about.
2. If you are unsure which values Creonda supports, call `get_search_options` once.
3. Call `search_creators` with structured filters only (unknown argument names are rejected). Put the budget in `price_max` (EUR, excluding VAT). Use `languages_mode: "any"` only when the user accepts either language.
4. If `unmatched_filters` is not empty, no creators were returned. Tell the user which value is not available (use the hint), suggest the closest option, and search again only with values that resolve. Never present creators for an unresolved request.
5. Present the results. When the creator cards are shown, do not repeat every card: summarise, point out the best fits and link their `profile_url`. Without cards, give first name, age, city, languages, main niches, starting price and the `profile_url` link for every creator you mention. Say that prices are starting prices for a 30-second video with 1 hook and 3 months of usage rights, excluding VAT.
6. Follow-ups:
   - "Tell me more about X" -> `get_creator_profile` with the slug from the results.
   - "Show their videos" -> `get_creator_portfolio`.
   - "More like X", "similar but cheaper" -> `find_similar_creators` (set `price_max` for cheaper).
   - "Next page" -> `search_creators` again with `page` + 1 and the same filters.
7. Booking: this plugin cannot book, message or pay creators. Point the user to the creator's `profile_url` on Creonda, where they create a project, invite the creator and pay securely.

Never:
- invent creators, prices, ratings or links, or edit the returned URLs;
- ask for or guess a creator's last name, email, phone, address or social media handle (not available by design);
- promise availability or a final price: the creator confirms both on Creonda.
