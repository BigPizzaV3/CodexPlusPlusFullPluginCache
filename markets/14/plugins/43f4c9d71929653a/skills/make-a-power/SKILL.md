---
name: make-a-power
description: Create or revise a Wildcards Storm design and its consenting harbor or music works, then issue a power to give someone.
---

Read [the shared contract](../../references/contract.md) and use the connected Wildcards app. Start from the user's own idea and describe which parts Storm currently supports. Get capabilities with get_wildcards_info when scope is uncertain; list_wildcards(kind=designs or works) before creating duplicates. Use render_wildcards for native creation and revision when helpful.

Creators need their existing ArkheOS entitlement. A gift recipient needs none. Do not sell a subscription or provide a checkout inside ChatGPT. Authentication and entitlement are separate; report the actual returned condition.

For a new design, create one or two requested works with save_wildcard_work, expected_revision=0 and a fresh request_id per action. Supported templates are harbor and music; private is the default. Ask before making a work public unless the user already specified publication; its credited effects become visible too. Use returned IDs as targets of save_wildcard_design. Confirm or infer ordinary creative details: title, explanation, creator display credit, intensity 1–3, duration 8–30 seconds. Never invent a recipient's identity.

For changes, read_wildcard_design or read_wildcard_work first, retain identity and expected_revision, and save only the intended change. A revision conflict requires a fresh read. The work template stays fixed. A private remix uses parent_id from the user's own design and keeps source credit. Existing issued cards retain pinned terms.

When the user requests a gift, issue_wildcard from the saved design. Reuse request_id only for recovery of that exact issue. Return its private claim link to the user; do not post it, send messages, or claim that anyone received it. Expiry is 1–30 days. Link possession lets the first valid recipient claim the power. Use withdraw_wildcard only for a requested, still-unclaimed card; claimed cards cannot be revoked by their issuer.
