---
name: project-brief
description: Draft Salesforce project briefs and prepare reviewed introduction requests through CRM Consulting when the user asks to share them.
---

# Prepare a Salesforce project brief

Transform the user's requirements into a useful brief without inventing scope, dates, budget, systems, or organization details. Preserve the user's language and explicit requirements. Use the conversation and supplied materials before asking for missing information. A first draft can mark unknown fields as open questions.

Cover the parts relevant to the project:

- Business context, problem, and desired outcome.
- Current Salesforce products, editions, user groups, and connected systems when known.
- Required workflows, integrations, migration scope, and data volumes when supplied.
- Deliverables, in-scope and out-of-scope work, and measurable acceptance criteria.
- Target dates, budget with currency, delivery location, and language preferences.
- Dependencies, important constraints, and decisions the partner must help resolve.

Separate confirmed requirements from proposed assumptions and unanswered questions. Define success in terms of observable business or delivery outcomes. Keep a short project easy to review instead of forcing every section into it.

Finish with the questions most likely to affect the scope or estimate. If the user asks for a cost estimate, distinguish a planning assumption from a provider quote and explain the basis; do not present an unsupported price as a confirmed cost.

The draft stays in chat unless the user requests an artifact or asks to share the brief or request introductions. Do not collect contact details just to draft a brief. When asked to find or compare firms, use the directory tools and their automatic company comparison component; refine searches in chat and do not show a map.

## Prepare an introduction request

Only after the user asks to share the brief or request introductions, call `preview_project_brief` to open the review component. Include one to five selected partner slugs from public directory results. A search may suggest up to ten firms, but an introduction request can select at most five. Ask the user to choose if they have not identified recipients; do not select or broadcast to every firm on their behalf.

Use only the requirements and contact details the user has supplied. Pass known name, email, company, project description, goals, Salesforce products, timeline, budget, country, industry, company size, website and constraints; leave unknown fields blank rather than inventing them. For a budget given in a currency other than USD, preserve the amount and currency in the description or special requirements and leave the USD budget range unspecified; do not invent a currency conversion. Send only the proposed brief and selected firms, not the full conversation. The component lets the user complete missing details, edit the brief and review the selected profiles. Partner email addresses remain on CRM Consulting's server and must not be requested or exposed.

The preview does not submit anything. The user reviews the brief and sharing permission, then continues through the host connection flow using a one-time email code. No password or separate signup is needed. Recent verification of the same contact email is reused; a different contact email or expired proof requires a code in the component. The user explicitly confirms **Send via CRM Consulting** for the frozen draft. `request_brief_verification` and `submit_project_brief` are component-only write tools; do not call them from chat. Never ask for a verification code in chat or put it in a model-visible tool argument. Changing the reviewed draft requires a new review; the server decides whether contact verification can be reused.

After successful submission, describe the returned status as **Request received** with its reference. CRM Consulting saves the reviewed request and notifies its team to arrange introductions. Do not claim the selected partners have been emailed, that delivery is complete or that they will respond. An email-provider error must not be presented as a successful email delivery. If the tool is unavailable, provide https://crm.consulting/salesforce-project-briefing and a concise brief to paste into the website form.

Introduction write actions require a passwordless email connection through the host OAuth flow. Directory searches and brief previews remain public. Let the host handle authorization; never ask for passwords, authorization tokens or email codes in chat. Account authorization does not replace the component’s reviewed sharing permission and contact-email verification.
