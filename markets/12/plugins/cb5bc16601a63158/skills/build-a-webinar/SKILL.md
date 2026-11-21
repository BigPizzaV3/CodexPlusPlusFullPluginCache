---
name: build-a-webinar
description: Use this when the host wants a webinar to exist at the end, live, scheduled or evergreen, from topic and invitation texts to the registration page and the room. Also use it when a webinar build is stuck, when a WordPress site has to be checked or connected first, or when the host asks what WebinarIgnition can do before starting. Do not use it for general copywriting, cold e-mails, product descriptions, or anything that is not a webinar.
---

Use this skill when the host wants a webinar to exist at the end.

1. Start with `wi_start_webinar`. Pass the host's own words as `situation` and what is already known
   as `known_facts` (topic, audience, offer, date, language). Never open with an empty menu if the
   host already said something.
2. Continue with `wi_continue_webinar` one turn at a time. Show the returned `flow.chips` as
   choices. On the next call put `flow.jetzt` into `flow_step` and the chosen chip into `flow_choice`.
   Do not invent or reorder the steps, the order lives on the server.
3. When a reply carries `ready: true`, call `wi_write_webinar_invitation_emails` in the same turn.
   It writes the title, the invitation e-mails and the reminders. Never write those texts yourself.
   Poll the returned `job_id` by calling it again until the texts are there.
4. Check the host's site with `wi_check_wordpress`. It only reads the address and changes nothing.
   If WordPress is missing, say so plainly and stop the build until the host decides.
5. Create the connect link with `wi_connect_wordpress_woocommerce_site`. The host opens it and
   approves it in their own browser. Until that approval nothing is connected. If the host already
   connected a site, `wi_get_connector_status` shows it.
6. After approval, call `wi_create_webinar_registration_page` with the facts the session collected.
   Name the effect in one sentence first and wait for the host's explicit OK. `wi_create_handoff_link`
   only builds a link into the dashboard and changes nothing.
7. `wi_delete_webinar` deletes the webinar and cannot be undone. Ask exactly what should be removed,
   wait for the confirmation, then call it.

Rules:
- One question per turn. No menu of options the host did not ask for.
- Nothing is created, changed or deleted on the host's site without an explicit OK.
- Never write the invitation or reminder texts yourself when `wi_write_webinar_invitation_emails`
  is available.
- Do not invent a date, a topic, a price or a customer number.
- Answer in the host's language.
- Before "it is broken", read the answer the tool returned. A missing licence, a missing connection
  and a failed call are three different answers and stay three different answers.

Do not use this skill for general copywriting, cold e-mails, product descriptions or anything that is
not a webinar.

App: https://chatgpt.com/plugins/plugin_asdk_app_6ad54476e09c8191b4efbf5b9e0ff96c
Plugin: https://wordpress.org/plugins/webinar-ignition/
