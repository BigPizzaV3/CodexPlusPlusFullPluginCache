# Prompt for a coding agent

Frontmost AI published this prompt in its guide [How to tell if AI is sending you customers](https://frontmost.ai/blog/is-ai-sending-you-customers). It adds the question to a product with a sign-up. It covers the screen, the server, the database, analytics, and tests.

Change the list of answers to fit the business before you use it.

```text
Add an optional "Where did you first hear about us?" question to our onboarding. Read the codebase first. Use our existing frameworks, components, design tokens, database, and migration tools.

Screen
1. Show the question once, on the first screen a new user sees after signup. Do not add a required step. Existing users never see it.
2. Show ten answers as a plain single-choice list, one per row, with thin dividers and radio marks. No icons and no new colors:
   An AI assistant; Google or another search engine; YouTube; LinkedIn; Reddit; X (Twitter); Other social media; A friend or colleague; Podcast, newsletter, or article; Other.
   If a channel above does not fit our business, swap it for one that does (for example TikTok or Instagram for a store). Keep ten rows or fewer.
3. When "An AI assistant" is picked, open an optional "Which one?" row directly under it, indented to the label, with small single-choice chips:
   ChatGPT; Claude; Gemini; Google AI Mode or AI Overviews; Perplexity; Microsoft Copilot; Grok; Another.
4. When "Other" is picked, show a short text field (up to 200 characters). Keep its border neutral in every state.
5. Sizes: rows 48 px tall with 16 px text, 20 px radio marks, and dividers that start at the label. Chips are 36 px tall with a 44 px touch target. Buttons are 44 px tall.
6. "Continue" stays disabled until an answer is picked. "Skip" is a quiet text button. Changes take under 150 ms with no bounce. Support the keyboard, screen readers, phones, and reduced motion.

Server and data
7. Add one endpoint or server action that saves the answer for the signed-in user only. Accept only the listed keys and reject anything else.
8. Store these fields on the account, or in a small table linked to it: source key (for example "ai"), AI app key (for example "chatgpt", optional), the "Other" text, answered_at, and skipped_at. Write a migration.
9. Skip saves skipped_at and no answer. Never store a skip as "Other". Do not show the question again once answered_at or skipped_at is set.
10. If we send product analytics events, send one event on answer, with both keys, and one on skip.
11. If we sync customers to a CRM or billing system, copy both keys to that customer record, so paying customers can be counted by source.

Tests
12. Test that answering saves the keys and the time, skipping saves only skipped_at, an unknown key is rejected, and the question does not come back.

Before you change code, list the files you will change, the fields you will add, and how the answer gets from the screen to the database.
```
