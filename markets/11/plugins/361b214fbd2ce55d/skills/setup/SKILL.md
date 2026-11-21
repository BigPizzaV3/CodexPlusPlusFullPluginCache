---
name: setup
description: Get a recruiter or search firm started with Formatix after installing the plugin - check the account, find or build the firm's CV template, check the brand, see any connected ATS or CRM, and format a first CV. Use when the user says "set up Formatix", "get started" or "how do I start", or right after the plugin is installed.
---

# Set up Formatix

Done when: the user knows which template they will use and what to do next, or knows the
one thing they still need to do. Keep it short: a few questions, no lecture.

Explicit instructions from the user take priority over this skill.

## Ground rules

- Reply in the user's language.
- Nothing here uses credits, and nothing is created without the user's yes.
- If a tool says sign-in is needed, ask the user to connect Formatix and stop. If they have
  no account, point them to https://formatix.ai.
- Do not discuss prices, plans or trials.

## Steps

1. **Templates:** `list_templates`. Tell the user what they have in one or two lines.
   - They have one that fits: note it and go on.
   - They have none: ask for a document they already send clients (Word, PowerPoint or
     Excel) and follow build-our-template.
2. **Brand:** `list_brand_kits`. Mention the firm's brand and any client brands. If there are
   none, say the firm's own templates already carry its design.
3. **ATS or CRM:** `ats_connections`. If something is connected, name it and say what can be
   done from the chat (format-cvs lists this). If not, say it can be connected on the
   Integrations page in Formatix if they use JobAdder, HubSpot, Salesforce or Ezekia.
4. **Automation, only if they ask for it:** get_activity shows the daily limit, and
   daily-cv-run sets up a recurring run.
5. **First document:** offer to format one CV now (format-cvs). Stop here if they say no, and
   give them two example requests in their own terms.
