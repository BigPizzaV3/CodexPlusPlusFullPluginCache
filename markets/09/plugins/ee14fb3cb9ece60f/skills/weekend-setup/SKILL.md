---
name: weekend-setup
description: Help someone who explicitly asks how to get started with Minerva Weekend. Do not activate on installation or during an ordinary weekend-planning request.
---

Minerva needs no introductory setup conversation. Use this skill only when the person asks for help getting started. Installation alone is not a request to start a chat, inspect preferences, save a plan or enable reminders.

If they have already described an outing, continue it using the [plan-weekend skill](../plan-weekend/SKILL.md). Reuse the details in the conversation and ask only for something that changes the recommendation.

Otherwise, give one short invitation in the conversation language, such as: "What sounds good this weekend — a day out or a night away? Tell me where you're starting from." Omit questions the conversation already answers, then wait for their reply. No product lecture or account checklist.

This introduction needs no tool calls, profile lookup or search through files and memory. Keep the response focused on the person's weekend; do not narrate technical preparation. Once they provide a planning request, use the planning skill and its normal tool workflow.

Keep the introduction and initial ideas in native chat. Do not open the app home or a route widget as setup. A request to list saved plans uses `get_saved_weekends` and a concise chat answer; a visual route is reserved for an explicit request to see one chosen route in detail or on a map.

If a required tool actually asks for an account connection, use the host's normal OAuth flow at that point. Never ask for passwords, access tokens or one-time codes in chat. Explain a real connection failure briefly without claiming it succeeded.

Saving plans, remembering preferences and recurring reminders each require the person's explicit request. Do not enable them during an introduction. Follow the planning skill for any requested changes and report success only after a confirming result.
