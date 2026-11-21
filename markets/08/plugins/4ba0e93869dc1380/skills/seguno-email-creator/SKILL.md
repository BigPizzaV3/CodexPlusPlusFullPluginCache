---
name: seguno-email-creator
description: create or revise Seguno marketing emails by interviewing the user, creating a newsletter by default, grounding content with store search, planning sections, applying valid `update_email` actions, and previewing the saved result. Use for promotional emails, newsletters, product launches, seasonal emails, post-purchase emails, feedback emails, or existing Seguno newsletter updates.
---

# Seguno Email Creator

Build or revise Seguno newsletter campaigns through the Seguno MCP tools. Default to creating a new newsletter unless the user clearly asks to update an existing one.

## Core Flow

1. Decide whether this is a new or existing newsletter.
2. For a new newsletter, call `create_newsletter` first and keep the returned `newsletterId`.
3. For an existing newsletter, identify the target `newsletterId` and call `get_current_sections`.
4. Interview the user briefly for missing campaign details.
5. If the user requests a discount for the email, find the relevant discount with `search_discounts` and add ito the email with `set_discount`
6. Search store data before using store-backed products, collections, links, or images.
7. Share a short plain-language section plan. Do not show raw action JSON unless asked.
8. Build the smallest valid `update_email` action list and include subject or preview text when useful.
9. Call `update_email`; it persists changes immediately and should be treated as destructive.
10. Review the returned sections for clarity, hierarchy, CTA strength, missing values, and leftover boilerplate.
11. Call `preview_newsletter`, summarize the saved preview, and ask whether the user wants changes.
12. Iterate with another `update_email` and preview when changes are requested.

## Tools

- `create_newsletter`: creates a newsletter and returns `newsletterId`.
- `get_current_sections`: returns saved sections for a newsletter.
- `update_email`: persists `actions`, optional `subject`, and optional `previewText`; returns current saved sections.
- `preview_newsletter`: previews the saved current template.
- Store search: use `search_products`, `search_collections`, `search_links`, `search_discounts` and `search_images` as needed.
- `set_discount` set a discount to be sent with an email. Use results returned from `search_discounts` to pick a discount if the user requests one

Never assume section ids. `UPDATE_SECTION`, `MOVE_SECTION`, and `DELETE_SECTIONS` require ids from `get_current_sections` or the latest `update_email` result.

## Interview

Ask only focused questions needed to create the email. Learn the goal, audience or segment, offer, featured product or collection, CTA, destination URL, timing, tone, and any requested or avoided products, imagery, links, colors, or sections.

If the prompt is sparse, ask the highest-impact follow-ups first. Avoid dumping a full questionnaire.

## Store Data Rules

- Search before using store-backed ids, URLs, or images.
- Prefer exact user-provided products, links, or images when reliable.
- Use `search_products` for specific items or product grids.
- Use `search_collections` for collection-led CTAs or category sections.
- Use `search_links` for landing pages, resources, product pages, and unknown destination URLs.
- Use `search_images` for hero, product, category, or lifestyle images from the store.
- If matches are ambiguous, choose the obvious best match or ask a quick disambiguating question.

Never invent products, collections, links, images, discounts, emails, ids, unsupported fields, or placeholder values. If required data is unavailable, search, ask, leave it blank/null only when the schema allows it, or choose a simpler section type.

## Planning Rules

Follow email marketing basics unless the user says otherwise: one clear campaign idea, obvious value near the top, concise benefit-led copy, one primary CTA, mobile-friendly structure, and real urgency only.

A normal promotional structure is intro or hero, primary CTA, supporting product/collection/image section, offer callout, and closing CTA. Adapt it to the goal instead of forcing it.

Use normal Seguno section types first. Use an `HTML` section only when other section types cannot support the requested content or when the user specifically asks for custom HTML.

Lazy-load references only when needed:

- Read `references/section-guidelines.md` when section choice, store-search mapping, or missing-data handling is non-obvious.
- Read `references/recommended-layouts.md` when building out a layout containing multiple sections
- Read `references/metafields-personalization.md` before writing Liquid variables or customer personalization.
- Read `references/post-purchase-feedback-example.md` and then `references/example-results.json` only for post-purchase feedback, reply, review, or photo-response campaigns that need an example structure.

## Updating Sections

Allowed actions are `DELETE_SECTIONS`, `MOVE_SECTION`, `UPDATE_SECTION`, and `ADD_SECTION`. Use the smallest correct change.

- Prefer updating an appropriate existing section.
- Add sections only when the needed structure is missing.
- Delete irrelevant boilerplate or conflicting sections.
- Move sections after the final structure is known.
- Preserve section type unless delete-plus-add is clearly better.
- Keep stable list item ids when updating existing list sections and the tool expects them.
- Generate unique stable ids for new list items when required.
- Use `insertBefore` when order matters.

Every section object must match the allowed schema exactly. When in doubt, simplify the section rather than guessing.

## Review

After `update_email`, check the saved sections for clear top message, strong CTA placement, logical order, concise copy, offer clarity, accurate store data, missing URLs or product data, placeholder-looking content, and alignment with the user goal.

Always call `preview_newsletter` after saved updates. The preview is the review checkpoint; there is no separate save button.

## Response Pattern

Briefly acknowledge the request, gather only needed details, use store search where helpful, share a compact section plan, update the saved newsletter, preview it, and ask for changes.

## Copy rules

These apply across all sections and all flows.

---

### 1. Headlines, hooks, and first impressions

**Keep headlines specific** — generic headlines ("Check out our new arrivals") convert worse than specific ones ("The summer collection is here — 6 new styles").

**Pair subject line and preview text like a conversation** — don't waste preview text by repeating the subject line; use it to build momentum and curiosity. These are separate fields in the builder — treat them as a two-part hook.

**Kill the passive "We" in the opening line** — reframe copy instantly around what the shopper gets, not the merchant's internal excitement.

**Keep urgency authentic, not manufactured** — avoid artificial pressure on evergreen stock. False scarcity degrades long-term subscriber trust. Only use Countdown sections and deadline-driven copy when a real deadline exists.

---

### 2. Body copy and readability

**Lead with the shopper benefit** — focus on the value to the subscriber, not the merchant's perspective.

**Speak to a single human, not a stadium** — email is a 1-to-1 medium. Write as if sending a message to a smart friend, not broadcasting to a crowd.

**Write for the skimmer, not the scholar** — keep paragraphs to 1–2 sentences. Use bold text for key takeaways so the value is obvious at a two-second glance.

**Address friction directly in the body copy** — weave reassurance (sizing help, free returns, guarantees) into the copy before the subscriber reaches checkout.

**Pair visual sections with Rich text sections** — don't build an email using only image or media sections. Every email should contain live HTML text in Rich text sections alongside any visual content. This supports deliverability and accessibility.

---

### 3. Offers and CTAs

**Don't stack multiple offers in one email** — pick the single strongest offer and commit to it.

**Repeat the primary CTA only when it genuinely helps flow** — appropriate in long emails or as a post-content placement. Not every email needs a repeated CTA.

**Use low-friction, value-driven CTA verbs** — swap high-commitment words like "Buy Now" for benefit-focused verbs like "Explore the Collection" or "Get My Guide."

**Ensure the CTA completes the sentence "I want to..."** — button copy should be a logical continuation of the reader's intent. "Get 20% off" works; "Click here" does not.

---

### 4. Layout and design hierarchy

**Match copy to the actual visual assets** — text should align precisely with the specific products, collections, links, and images selected from the store. Never write copy for assets that haven't been confirmed.

**Pass the "Squint Test" in under two seconds** — the headline, primary product or offer, and CTA button should still be identifiable when the email is blurred. If they don't pop, the hierarchy needs work.

**Keep the hero message above the fold** — the hook, core value proposition, and initial CTA should be visible without scrolling.

**Use the inverted pyramid format** — guide the eye naturally: broad headline → focused supporting sentence → prominent CTA.

**Section count** — aim for at least 4 content sections (Dividers and Spacers don't count). A soft cap of 8–10 content sections keeps the email focused. Exceptions: brand story and plain text-style emails can work with fewer sections by design.

---

### 5. Personalization

**Use personalization tokens where they add warmth** — first name and last name tokens are available in subject lines, preview text, and Rich text body fields.

Syntax:

- First name: `{{ customer.first_name | default: 'friend' }}`
- Last name: `{{ customer.last_name | default: '' }}`

Always include a default value. For first name, ask the merchant what fallback they prefer — don't assume `friend` without confirming.

Custom account-level values are also available — ask the merchant if they have custom tokens configured for their account.

**Personalization works best when it's contextual, not decorative** — adding a first name to a subject line can improve open rates, but personalization in body copy should feel natural, not like a mail merge.

---

### 6. Subject lines and preview text

Subject line and preview text are separate fields in the builder. Treat them as a two-part entry point into the email.

**Subject line** — specific, benefit-led, and honest. Personalization tokens are available. Keep it tight enough to avoid truncation on mobile.

**Preview text** — should extend the subject line, not repeat it. Use it to add context, build curiosity, or state the offer more explicitly.

Personalization tokens work in both fields. Use first name where it adds genuine warmth rather than inserting it mechanically.

---

### 7. Audience and timing considerations

**Ask the merchant who the audience is before writing copy** — a campaign going to lapsed buyers should sound different from one going to the full list. Tailor the copy to make the message feel relevant to that specific segment.

- Lapsed buyers: acknowledge the time since their last interaction — don't pretend it didn't happen
- VIP customers: make them feel recognized and rewarded, not just marketed to
- First-time buyers: focus on building trust and encouraging the second purchase
- Full list: write for the broadest relevant denominator without being generic

**Flag send time when a short deadline is involved** — if the campaign has a deadline of 24–48 hours or less, remind the merchant to consider when the email will land relative to the deadline. A flash sale email sent at 11pm the night before a noon cutoff may not give subscribers enough time to act.

---

### 8. Campaign-type copy nuances

**For social proof campaigns** — match the testimonial or review to the specific objection it addresses. Don't use generic praise; curate reviews that debunk specific customer doubts.

**For re-engagement campaigns** — acknowledge the gap honestly. Be direct about the time since their last interaction and give them a genuine reason to come back.

**For post-purchase campaigns** — sound human and genuinely curious. Write with a conversational tone rather than an automated receipt template.

**For feedback campaigns** — make the ask feel easy and appreciated. Keep the barrier low and make clear that their input is valued.
