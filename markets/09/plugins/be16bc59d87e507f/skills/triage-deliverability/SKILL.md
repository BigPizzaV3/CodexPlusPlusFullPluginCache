---
name: triage-deliverability
description: Triage a deliverability problem in Send & Retain — bounce or complaint spikes, blocked or failing sends — by quantifying it, finding where it comes from, and recommending a fix. Use when the user reports bounces, spam complaints, or mail not arriving.
---

# Triage deliverability

1. **Quantify.** `email_get_email_metrics` for the affected window: bounce and
   complaint rates against the period before it.
2. **Localize.** `email_search_messages` filtered to bounced, complained or
   failed: which template, which recipient domains, and when it started.
3. **Inspect.** `email_get_message` on representative failures, and read the
   provider's bounce classification in the event timeline.
4. **Check infrastructure.** `email_get_connection_status`, then
   `email_verify_domain` to re-read it: is the domain still verified, are the DNS
   records intact?
5. **Diagnose** — list hygiene, content, infrastructure, or a volume spike — and
   recommend the fix. If sending should stop while it is fixed, say so
   explicitly: `email_set_sends_paused` is the user's call to make, so call it
   only on their go-ahead.
6. **Confirm suppressions** are in place for the bad addresses
   (`email_list_suppressions`). Never remove a complaint suppression; the
   platform refuses to.
