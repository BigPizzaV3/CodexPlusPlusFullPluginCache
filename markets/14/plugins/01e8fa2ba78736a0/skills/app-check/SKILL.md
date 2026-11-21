---
name: "app-check"
description: "App check: review a pasted web page or app screen (HTML or text) for SEO, content, conversion, accessibility and technical basics, with scores and prioritized fixes. Use when the user pastes HTML or copy and asks for an audit or review. Never opens URLs."
---

# App check

1. If the user has not pasted HTML or text, ask them to paste the page source (preferred) or its visible text, plus an optional target keyword. Do not ask for a URL: pages are never opened.
2. Call `check_app_page` with the pasted `html` or `text`, the optional `target_keyword` and a `page_type` (use "landing" for a marketing page, "other" for an app screen).
3. Report the five scores out of 100 (seo, content, conversion, accessibility, technical) and the overall score, then the top fixes in the tool's severity order: what is wrong, why it matters, the exact change. If both HTML and text were pasted, send the HTML. Quote only measurements the tool returned.
4. Say plainly that scores are heuristics, not proof of ranking, accessibility compliance or store approval.
5. Offer to rewrite the weakest part (title, headings, button text) from the supplied content only.

## Ground rules
- Reply in the user's language. Write the app's own text in the language the user wants for the app.
- Use only details from the conversation. Never invent prices, reviews, user numbers, awards or integrations; write "[confirm: ...]" where a fact is missing and label proposals as "Assumptions:".
- Never ask for passwords, API keys, payment details or personal data.
- Refuse apps meant for malware, spyware or stalking, gambling, adult content, credential harvesting or copying another product's code or brand; say why in one line and offer a legitimate alternative.
- Lead with the deliverable.
