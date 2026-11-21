---
name: get-started
description: How to use AI Visibility Check to audit a website's visibility to AI assistants and search engines, and answer questions about the result.
---

# Getting started with AI Visibility Check

Use these tools when the user wants to know how well a website can be found,
understood and recommended by AI assistants and search engines, or asks
about an audit they already ran.

## Running an audit

1. Call `start_site_audit` with the site's address and `depth`.
   - `quick`: the homepage, about a minute. Use it unless the user asks
     for more.
   - `full`: the whole site, real-browser rendering, outside sources and AI
     model questions; about 7 minutes and uses one of the user's full
     audits. **Ask the user to confirm before starting a full audit.**
   - Pass `keywords` when the user names search terms they care about.
2. Call `get_site_audit` with the returned `scanId` until it is finished.
   Then give the score, the headline and the top actions, and the report link.

## Answering questions about a result

- Problems, by severity or area → `get_audit_issues`
- One area in detail (e.g. structured data, AI crawlers, performance) →
  `get_audit_section`
- "What should I fix first?" → `get_action_plan`
- "Do AI assistants recommend us? Who do they name instead?" →
  `get_ai_visibility` (full audits only)
- No scanId in the conversation → `list_site_audits` to find it
- "How many audits do I have left?" → `check_audit_allowance`

## Rules

- Report what the tools return. A check marked unmeasured was not measured;
  never present it as a failure or a pass.
- AI-model answers are samples from one point in time; say so.
- Never quote a price or offer to buy anything. If the user has no full
  audits left, offer a quick audit instead.
- There is no tool that deletes or changes account data; say so if asked.
