---
name: pollen
description: Draft a portable product or business page from public copy using Pollen.
---

# Pollen

Use Pollen when a person requests a draft product, business or portfolio page. Ask for missing public business copy before calling a tool. Call `pollen:start_draft` with `name` (1–120 characters), `brief` (1–2000), optional `headline` (up to 160) and `style`: `editorial` for Portfolio, `studio` for SaaS, or `bold` for Consumer. The default is `editorial`.

Call `pollen:check_draft` once with the returned `id` to retrieve the filename and standalone HTML. Give the person the HTML to save and review. Pollen saves a guest draft without an account; anyone holding its ID can read it. Use public business copy only. Never send credentials, private contact lists or personal identifiers. Do not ask for an email address.

Hosting, domain purchase, publishing, custom imagery, payments and messages are separate. These tools cannot perform those actions. The generated site has no MCP server of its own. Preserve tool errors, and do not invent a draft when an ID is unknown.
