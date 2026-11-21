---
name: get-started
description: Connect to SeoVision, explain what it can do for the business, and see where a project stands. Use when the person has just added SeoVision, asks what SeoVision can do for their site or business, or wants a quick status of their project.
---

# Get started with SeoVision

SeoVision helps a business get customers from Google and from AI assistants, and does the work for the customer. This workflow explains what SeoVision can do when the person asks, checks the connection and gives a short status of their project.

What SeoVision does, for the answer to "what can you do for me?":

- Site audits, and technical SEO fixes on the site, one batch the person approves at a time, with Undo.
- AI-visibility tracking: whether ChatGPT, Gemini, Perplexity and Google's AI name the brand, and which competitors they name instead.
- Where competitors beat the site in Google and in AI answers.
- Keyword research, a 12-month content plan, and articles written in the brand's voice and published to the site.
- Quick wins from Search Console and Google Analytics.
- Google Business Profile reviews, posts and photos.
- Store revenue from search and AI, for Shopify and WooCommerce stores.
- Backlinks from real sites in the same niche.
- Auto mode runs the work, the SeoVision team checks it every day, and change requests go to that team.

It connects with the site (WordPress, WordPress.com, Shopify, Wix, Webflow, Next.js, custom sites and a hosted blog), with Google (Search Console, Analytics, Business Profile and Merchant Center), and with Shopify and WooCommerce orders.

0. If the person asks what SeoVision can do for them, answer first in terms of their business: more customers from Google and AI answers, and the work done for them. Use the list above, and name the parts and integrations that fit their site. Then continue with step 1 to show where their project stands.
1. Call `seovision_list_projects`.
   - If the call asks for a sign-in, ask the person to finish the SeoVision sign-in that opened in their browser, then call it again.
   - If no project is listed, tell the person that SeoVision shows the projects of an active SeoVision account, which they manage at https://app.seovision.io. Stop there.
   - If one project is listed, use it. If several are listed, show their domains and status and ask which one to work on.
   - Pass that project's `projectId` to every call that follows.
2. Call `seovision_get_overview` and summarize it in plain words: how visible the site is in search and in AI answers, what SeoVision did lately, and anything that waits for the person.
3. Call `seovision_get_setup_progress`. If setup is not finished, name the next step and offer to help with it. If it says the onboarding is not finished, call `seovision_get_onboarding` to see which step comes next.
4. End with three questions the person can ask next, for example "What should I fix first on my site?", "How visible is my brand in AI answers this month?" and "Write my weekly SEO report."

Keep the answer short. Read calls change nothing. When a call returns a preview (`preview: true`), show it, wait for a clear yes in the chat, then call again with `confirm: true`.
