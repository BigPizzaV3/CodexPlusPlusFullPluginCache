---
name: webinar-numbers
description: Use this when the host asks for numbers about a webinar, for example who registered, how many showed up, where the funnel drops, which offer tier sold, or what a webinar earned. Also use it when the host wants those numbers explained or compared. Do not use it for planning a webinar, for writing texts, or for numbers from a site that is not connected.
---

Use this skill when the host asks for numbers about a webinar.

Pick one tool per question:
- `wi_list_webinar_leads_registrants` for single people: who registered, who attended, what one lead
  bought. It returns names and e-mails from the host's own site.
- `wi_get_webinar_attendance_stats` for the show-up rate and replay viewers.
- `wi_get_webinar_funnel_conversion_stats` for the whole funnel and the step to fix first.
- `wi_get_webinar_revenue_woocommerce` for money, orders, refunds and which offer tier sold.

Rules:
- Read-only. Never change data in this skill.
- Never invent a number. If a rate needs at least 20 people in the earlier step, say so.
- Never add two currencies. Each line stays separate.
- If the answer carries `sample: true`, the numbers come from a static demo file. Say "example
  numbers" and never present them as the host's own data.
- If the answer carries `license_required`, pass that answer through as it is, with the explanation.
  Do not rebuild a registrant list from other tools.
- Without a connected site, say what is missing and how to connect, then stop. `wi_get_connector_status`
  shows whether a site is connected, `wi_get_setup_plan` explains what to install.
- Answer in the host's language.

Do not use this skill for creating a webinar or for writing texts.

App: https://chatgpt.com/plugins/plugin_asdk_app_6ad54476e09c8191b4efbf5b9e0ff96c
Plugin: https://wordpress.org/plugins/webinar-ignition/
