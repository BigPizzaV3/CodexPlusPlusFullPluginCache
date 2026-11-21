---
name: webinar-texts
description: Use this when the deliverable is text for a webinar, meaning a webinar title, an invitation e-mail, reminders, a follow-up, or copy for a webinar registration page. Also use it when the host wants an existing webinar text rewritten, shortened or translated. Do not use it for general advertising copy, cold outreach for another product, or a landing page that is not a webinar.
---

Use this skill when the deliverable is text for a webinar.

1. If no session exists, open one with `wi_start_webinar` and pass the host's words as `situation`
   and `known_facts`. If a session is already open, continue it instead of starting a second one.
2. Move the session with `wi_continue_webinar` until the reply carries `ready: true`. Ask only what
   the texts need: audience, one promise, date, tone. One question per turn.
3. Call `wi_write_webinar_invitation_emails`. Use `invite_type` for one of the built-in channels,
   `direction` for an angle, `skip_direction` when the host has none. The tool writes the title, the
   invitation e-mails and the reminders.
4. Return the title, the invitation, the reminders and the registration copy as written. Do not
   rewrite them by hand and do not invent a second version beside them.
5. A registration page is built with `wi_create_webinar_registration_page`, not written by you.
   Name the effect first and wait for the host's OK.

Rules:
- The texts are written by the tool, not by you. You may shorten a label, never a promise.
- No new claim and no number that the host did not give.
- Keep the host's language and voice. Answer in the host's language.
- Never write the invitation or reminder texts yourself when `wi_write_webinar_invitation_emails`
  is available.

Do not use this skill for general advertising copy, cold outreach for another product, or a landing
page that is not a webinar.

App: https://chatgpt.com/plugins/plugin_asdk_app_6ad54476e09c8191b4efbf5b9e0ff96c
Plugin: https://wordpress.org/plugins/webinar-ignition/
