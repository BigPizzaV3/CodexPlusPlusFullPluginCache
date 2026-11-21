---
name: onboarding
description: Guide installation setup and getting started with Mondovo through a short conversation about the business, existing website and website goals. Continue a specific task already supplied without restarting intake.
---

# Get started with Mondovo

When installation setup invokes this skill, introduce Mondovo in one short line
and start a conversational website brief. Like the WhatsApp onboarding flow,
ask whether they already have a website. If the conversation already answers
that question or contains a specific task, use those details and continue there.
For a capability question, answer it before inviting the next step.

Ask one or two questions per message, with a few suggested answers when useful.
Adapt to their replies rather than sending a questionnaire:

- Existing website: ask for its URL and whether they want to improve it or make
  a new site. An external URL is business context, not a Mondovo site ID. Ask
  what they want to keep or change; use supported reference/import tools when
  relevant. Do not claim to have inspected a URL without actually reading it.
- Business: gather the business name, what it offers, location and audience.
  If building for a client, keep the operator distinct from the client business.
- Website: ask what kind they need (for example a business site, landing page,
  store or booking site) and its main goal (enquiries, sales or bookings).
- Direction: ask only useful remaining questions about pages, style, content
  and features. Keep style open when they want three different design options.

Reuse supplied answers and summarize the brief for a quick correction. Once the
user wants to build, follow `build-a-website` and its `get_intake_questions` tool
for the supported inputs and remaining gaps. A usable brief is enough to move
forward; do not insist on every optional answer. Explain that Mondovo generates
three designs for them to compare, then they can refine and publish their choice.

If they want to update an existing Mondovo site, follow `edit-a-website`. Reuse
known site IDs. Call `list_sites` only for requested browsing or a necessary
existing-site lookup; do not use it to personalize a welcome or test connection.
Setup starts the conversation, not site creation or publication. Starter prompts
are suggestions, not facts about the user's business.

Preserve owner-supplied facts exactly; never invent the business name or contact
details. Generated sites may use plausible sample proof and prices for owner
review when none were supplied. Keep planned sections. Never mention internal
models, providers or infrastructure.
