---
name: set-up-my-registry
description: Use when a signed-in EasyRegistry owner wants to set up, check or tidy their own gift registry — review its title, event date, location, description, hashtag or thank-you message, see how it is going, or get it ready to share. Requires EasyRegistry sign-in. Not for creating a brand-new registry (that happens on the website) and not for bank or payment details.
---

# Set up my registry

Use this when the user talks about "my registry", "our wedding list", "the baby shower registry" and wants it configured, reviewed or made ready to share. The user must be signed in to EasyRegistry through the app's OAuth flow; if a tool returns an authentication error, ask them to sign in and try again.

## Workflow

1. **Find the right registry.** Call `get_my_registries`. If there is exactly one, use it and say which one you are working on. If there are several, list them by title and event date and ask the user to pick before doing anything else. If there are none, explain that registries are created on the EasyRegistry website (https://www.easyregistry.com.au) and offer to help once one exists. There is no tool that creates a registry.
2. **Show the current state.** Read back the title, event date, location, description, hashtag and thank-you message from `get_my_registries`, and use `get_my_registry_gifts` to say how many gifts are on it. Keep this to a short summary.
3. **Collect changes in one pass.** Ask what they want to change. Gather all the edits (title, description, event date, location, hashtag, thank-you message, open or closed state, notification preferences) before writing.
4. **Confirm, then write once.** Repeat the exact new values back and get a yes. Then call `update_my_registry` once with only the fields that change. Do not call it repeatedly for each field. A repeated identical call is safe and writes nothing.
5. **Report the result.** Confirm what changed and remind them that title, date, location, description and hashtag are visible on their public registry page. If they want gifts added next, switch to the "add gifts to my registry" workflow.
6. **Progress check (optional).** If they ask how the registry is going, call `get_my_registry_stats` for totals and `get_my_registry_gifts` for what is still open, and summarise in plain language.

## Boundaries

- Never ask for, guess or set bank account details, PayID, payment configuration or custom styling. Those are managed on the website only and are not exposed by any tool.
- Do not close a registry unless the user asks for that explicitly and confirms.
- Do not invent dates or locations. If a value is unclear, ask.
- Do not claim a registry was created, paid out, or shared. The tools only read and update settings.
- Contribution details from `get_my_registry_purchases` are the owner's private data; never repeat them into a message intended for guests.

## Output

A short confirmation of the registry worked on, the fields changed with their new values, and the next suggested step (add gifts, or share the public page).
