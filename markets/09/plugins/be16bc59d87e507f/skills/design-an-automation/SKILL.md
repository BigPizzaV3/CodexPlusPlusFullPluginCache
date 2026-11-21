---
name: design-an-automation
description: Design, preview and test-drive an event-triggered email automation in Send & Retain, and enable it only on the user's explicit go-ahead. Use when the user wants welcome emails, cart recovery, win-back or any automation that sends on an event.
---

# Design an automation

1. Resolve the company (`email_list_projects`) and agree the design: the
   trigger event, the exit event, who it is for (filters, and priority when
   variants compete), the cadence (delays, send windows) and which template
   each step sends. Author missing templates first (`author-a-template`).
   Confirm the company's app actually emits the trigger event.
2. `email_create_automation`. It is **always created paused** and returns a
   readable timeline. `email_preview_automation` renders every send step, so
   the user sees the real emails before anything is enabled.
3. Test-drive: `email_upsert_contact` a test contact (the user's own address,
   with realistic attributes including timezone), `email_emit_contact_event`
   with the trigger, then `email_list_automation_runs` to confirm enrolment and
   timing. Emitting an event can send real mail to that contact, so say so
   before calling it.
4. `email_pre_launch_check`, then walk the remaining items: every template
   published, suppressions imported if the company is migrating, and volumes
   sensible for the domain's age.
5. Enable with `email_set_automation_status` only when the user explicitly
   decides to, in this conversation. Then watch the first cohort with
   `email_get_automation_metrics`.

Adding steps to a live automation never disturbs contacts already in it; inserting,
moving or removing a step requires pausing first.

For each rendered email, open its `previewUrl` in the client browser panel when
available, or show a clickable link. Links expire after 15 minutes; anyone with
the link can view the sample. A preview does not send mail or enable a flow.
