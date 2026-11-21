---
name: get-started
description: Connect a Shika Cloud workspace and get the first website building — pick the right site, confirm what it is for, and show a preview before going further.
---

# Get started with Shika Cloud

## 1. Confirm the connection

Call `get_account` first. It returns the account's sites, their status, and how
many site slots the plan has left.

- If the call fails or returns no workspace, the connection is not authorized.
  Ask the user to reconnect Shika Cloud from their ChatGPT plugin settings.
- If the workspace is full, say how many slots are free and offer to continue an
  existing site instead of creating another one.

## 2. Choose continue or start fresh

Call `list_sites` when the user has not named a site.

- If a site's name or purpose matches the request, continue that one. Confirm
  which site you are working on before writing files.
- If nothing matches and the plan has room, call `create_site` once. Do not
  create a second site for the same request.

## 3. Learn what the site is for

Ask a few grouped questions: what the business or organisation does, the name,
the town or service area, a phone or WhatsApp number, and what a visitor should
do first (call, WhatsApp, book, or send an enquiry).

Never stall on a missing fact. Use a clearly marked placeholder and tell the user
what is still needed.

## 4. Build the first page

Call `load_site_recipe` for the kind of site described, then build one complete
page — usually the home page — before starting the rest. The preview updates as
files are written; share the preview URL from `get_site` so the user can look.

## 5. Finish deliberately

- Keep phone numbers, prices, and locations exactly as the user gave them.
- Create a form with `create_form` when enquiries or bookings are wanted, and
  embed the URL it returns.
- Run `run_site_check` before calling the site finished, and fix anything it
  blocks.
- Publish only when the user asks. `publish_site` refuses while the check is
  blocked, so run the check again after fixes.
