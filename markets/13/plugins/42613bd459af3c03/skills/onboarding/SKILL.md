---
name: onboarding
description: Introduce the Ask Daniel Brain plugin when the user chooses Set up or asks what it can do, show the resume card and offer starter questions.
---

# Set up Ask Daniel Brain

This plugin answers questions about Daniel Brain from his resume and everything it links to: 20 posts,
7 conference talks, 2 patents, press coverage, Hacker News threads and 23 open-source READMEs. It is
read-only apart from sending Daniel a message, and needs no account.

1. Say in one sentence what the plugin covers.
2. Call `get_resume` with `{}` so the resume card renders, and point out its PDF button.
3. Offer these starter questions:
   - Give me a two-minute summary of Daniel's career.
   - What is OneText building, and how does OneCheckout keep card numbers away from AI agents?
   - What does Daniel think is wrong with iframes, and what did he build about it?
   - Which of Daniel's conference talks should I watch first, and why?
   - How can I get in touch with Daniel?
4. Mention that the Ask Daniel Brain icon in ChatGPT's left bar opens the library, where they can search
   and read every source and watch the talks, and that its Tour shows everything the plugin can do.
5. Mention that they can send Daniel a message from here; only the message itself is required.
6. If the user installed the plugin in the middle of a task, continue that task in the same conversation.
