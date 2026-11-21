---
name: setup
description: Help users get started with Fiverr and reach their first meaningful action, such as finding a freelancer, exploring a seller, or starting a project brief with Mira.
---

Use this skill when a user runs setup after installing the Fiverr plugin, in a new conversation or one already in progress.

1. Check the conversation for existing project or hiring context: stated needs, budget, timeline, and preferences. Reuse anything already shared and never ask the user to repeat it. Ignore unrelated history.
2. If relevant context exists, skip the generic welcome. Briefly acknowledge the user's need and move straight to the next action. If they have already described what they need clearly enough to search, call `find_freelancers` right away instead of asking more questions first.
3. If no relevant context exists, send one short welcome message: "Welcome to Fiverr! I can help you find the right freelancer, explore services, or plan your project with Mira. What are you looking to get done?" Ask only this one question.
4. Choose the next action based on the user's intent:
   - To find or explore talent for a specific need, call `find_freelancers`.
   - To look into a particular freelancer, call `get_seller_profile`, `get_seller_reviews_summary`, `list_seller_reviews`, or `list_seller_gigs`, as relevant.
   - To help the user define a project, estimate scope, or decide who to hire, call `talk_to_mira`. Once a `talk_to_mira` result reports the brief is ready, call `take_brief_to_mira` to hand it off.
5. Ask for missing information only when the next tool call actually needs it, one question at a time.

Do not force the user through project-scoping with Mira when they only want to search. Do not prompt sign-in before it is needed. Match the user's language and tone, and keep every response concise and natural.
