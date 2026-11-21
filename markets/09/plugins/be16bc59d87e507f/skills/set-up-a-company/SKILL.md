---
name: set-up-a-company
description: Take a company from nothing to a live email programme in Send & Retain — understand the business, install starter templates and paused automations for its type, rewrite them in its voice, then set up sending. Use when the user wants to start email for a new or empty company.
---

# Set up a company

The order matters. Templates and automations need no provider, domain or sender,
so do not ask for DNS records or API keys until the last phase. Show the user
something worth having before asking for the hardest work.

## 1. Understand

`email_list_projects`, or `email_create_project` with the company's website (it
reads the site and infers the brand). Then learn, two questions at a time and
never as a form, what you cannot read off the site:

- which events their app already emits — this decides every automation's
  trigger, and an automation wired to an event nobody sends looks alive and is dead
- who is on the list, and whether it exists elsewhere already
- the one customer moment they most want handled (signup, an abandoned
  checkout, a lapsed customer)
- the domain they will send from — call `email_create_domain` as soon as they
  name it, so verification runs in the background

## 2. Programme

`email_get_brand` first; if it is empty, read the website and save
colours, fonts and voice with `email_update_brand`, because the starters bake the
brand in. Then `email_list_sequence_packs`, propose an archetype (saas,
ecommerce, newsletter-media, marketplace) and its automations in plain language,
naming each automation's trigger. On agreement, `email_bootstrap_company`. It
publishes the starter templates and creates every automation **paused**.

## 3. Content

Rewrite each starter in the company's voice (`email_update_template`), check it
with `email_render_template`, then `email_publish_template_version`. Start with
the email for the moment they said hurts most. `email_preview_automation` shows
a whole automation's emails.

## 4. Live

`email_get_connection_status` → if no provider is connected, give the user its
`settingsUrl`, where they connect sending themselves (never take a key in chat)
→ `email_verify_domain` → `email_register_webhooks` → `email_create_sender`. The
user mints their app's API key on the same page; give them a
`POST /api/v1/events` snippet for exactly the triggers the chosen automations use.
Then `email_pre_launch_check`, and enable automations one at a time with
`email_set_automation_status`, each only on the user's explicit go-ahead.

Done is an automation live, its trigger seen, and a real send from their own domain.
