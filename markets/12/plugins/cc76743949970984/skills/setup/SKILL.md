---
name: setup
description: Use when the user runs setup for SVG Lab or asks how to get started. Checks the SVG Lab account, says where designs are saved, asks what to design and starts the first design with the live view.
---

# Set up SVG Lab

1. Call account_status with {}. If the account has no access to the SVG Lab MCP, say so plainly, give the plans link the reply carries, and stop there. Do not recommend or push a plan. If the reply has heads_up, tell the user that first.
2. Tell the user in two short sentences how it works: SVG Lab designs in their own SVG Lab editor on SVG Lab's servers, and every design is saved to My Projects in their SVG Lab account, where they can open it at svglab.app and edit it by hand.
3. If the plugin was installed during a task, carry on with that task. Otherwise ask one question: what do they want to design (app screens, a website, a logo or icons, an illustration)?
4. Every design starts with new_project. Its first reply lists the questions to ask, as docs guide plan-with-the-user describes, and a line about ChatGPT's permission prompt: ask them all in one message, each with a recommended answer, then call new_project again with the answers. The screens are built with SVG Lab's tools, never as a picture from your own image generation.
5. Imagery follows the user's ChatGPT plan, which you know. On ChatGPT Free, offer stock photos only and recommend them: no drawn illustrations, because ChatGPT Free makes only a few images a day. On other plans, ask whether the screens use photos, drawn illustrations or a mix, with a recommendation.
6. new_project's reply carries live_view: give the user the live view link so they watch the design being made.
7. For every drawn illustration, follow the drawing-from-references skill.
8. At the end, say what was made, anything not finished and why, the project link, and the credits left.
