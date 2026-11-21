---
name: onboard-brand
description: >
  Review a PostQuickAI brand setup and guide the user through missing account or
  brand details. Use when the user says "set up my brand", "new brand",
  "onboard a client", or is starting PostQuickAI for the first time.
---

# Onboard a Brand

## Goal
Help the user inspect an existing content group and finish setup safely in PostQuickAI.

## Workflow

1. **Find existing brands.** Call `listContentGroups`. Never create or guess a content group.

2. **Handle a missing brand.** If the needed content group does not exist, explain that this connector cannot create one. Direct the user to https://www.postquick.ai/dashboard to create it, then ask them to return.

3. **Review saved context.** For the chosen group, call `getBrandContext` and `getInstructions`. Summarize the saved brand name, audience, tone, topics, and standing instructions. Do not invent missing details.

4. **Check connected accounts.** Call `listAccounts` and `getAccountHealth`. Clearly identify which destinations are connected. Account connections must be completed in the PostQuickAI dashboard.

5. **Identify gaps.** Ask the user for missing brand details, one small question at a time. Explain that this connector can read but cannot update saved brand instructions; provide concise text they can paste into the dashboard.

6. **Update brand labels when asked.** `updateContentGroup` can rename an existing brand or change its description. Confirm the requested change when it affects shared work; it cannot create a brand or replace saved brand instructions.

7. **Research a website when asked.** Use the website-research skill to start and inspect a scan; do not overwrite brand settings based on research.

8. **Offer a draft test.** Once setup is complete, offer to call `generateCaption` and then `createPost` to save one draft. Show the text before saving when the user asks to review it first.

## Never do

- Never claim to create a content group or update saved instructions; the remote connector has no tools for those actions.
- Never enable automatic generation or publishing settings.
- Never invent brand details or connected accounts.
- Never schedule the test draft without separate confirmation of its content, destinations, and time.
