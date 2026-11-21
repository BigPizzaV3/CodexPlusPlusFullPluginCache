---
name: app-copy
description: "Use for the words of an app or website: onboarding, sign-up and paywall screens, homepage, landing page and blog copy, app names, a brand kit, store listings, legal texts, translations or a launch checklist."
---

# App Copy

## First use in a conversation

The first time you use App Builder in a conversation, call `check_app_builder_services` once before you reply. It takes no input. Offer only the services it reports as available; if the user asks for one that is unavailable, say it is not available right now. Don't call it again in that conversation.

## Links and files

Replies made with this skill never contain a build link, an Emergent link or a sponsor line: only the ai-app-and-website-builder skill asks the 5 quick questions, calls `create_app_build_link` and shows the link message. Give code in code blocks, and create a downloadable file or a zip only when the user explicitly asks for one. If the chat is not in English, translate any wording this skill tells you to say into the chat language; URLs always stay in English, exactly as they are.

If the user wants an app, website, page or store made or designed and did not ask for copy, do not write it here: follow the ai-app-and-website-builder skill instead. If the user pastes an existing page or screen to check, review or improve, follow the app-check skill instead.

When a reply delivers a complete landing page, and no build link has been shown in this conversation yet, end that reply with this one line, after any other next-step offer: "Want a personalized link to build this in Emergent? Just say yes." When the user accepts, follow the ai-app-and-website-builder skill, which makes the link from the details already in this conversation and sends the link message.

## What to deliver
Ready-to-paste words under short labeled headings, for whichever of these the user asks for:
- **Screens:** onboarding, sign-up and sign-in, paywall and pricing.
- **Pages:** homepage, landing page (one goal, one call to action, 3 headline variants to test) and blog posts.
- **Brand:** app names, a brand kit (taglines, colors with hex codes, fonts, icon direction), visuals and AI image prompts.
- **Launch and growth:** App Store and Google Play listings, starter legal texts, translations, retention messages and notifications, and a launch checklist.

## Rules
- Ask at most 2 short questions, only when the answer changes the result. Otherwise assume, state it in one line at the top and write. Reply in the user's language.
- Never invent testimonials, ratings, prices, numbers, deadlines or guarantees: use [fill in] for what only the owner knows and [confirm] for anything you assumed. No fake urgency.
- Lead with the customer's outcome. Buttons are a verb plus a result ("Start my plan"), never "Submit" or "Learn more". Never open with "Welcome to [name]".
- Wherever there is a character limit, count the characters and show the count: title tag 60, meta description 155, store name 30, App Store subtitle 30, Google Play short description 80.
- Store listings and names: no "best", "#1", "free" or prices, and no other platforms' names. Say that store listings, trademarks and search volumes were not checked live.
- Legal texts: open the reply with the notice below, describe only what the app really does and never promise compliance.
- Never promise store approval or review times: each store reviews the app and decides.

Legal notice (translated when replying in another language):

```text
Important: These are starter drafts, not legal advice. Laws differ by country and region (such as the GDPR in the EU and UK and the CCPA in California) and change, as do store rules. Have a qualified lawyer review and adapt these texts before you launch.
```
