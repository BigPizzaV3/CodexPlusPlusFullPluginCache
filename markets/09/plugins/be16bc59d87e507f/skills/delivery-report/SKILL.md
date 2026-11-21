---
name: delivery-report
description: Write a read-only delivery and engagement report for a company in Send & Retain — volumes, rates, per-template performance and the highest-impact next moves. Use when the user asks how their emails are performing.
---

# Delivery report

Read-only: change nothing while reporting.

1. Resolve the company (`email_list_projects`).
2. Start with `email_get_optimization_plan`. Its ranked actions frame what
   matters.
3. Pull `email_get_email_metrics` for the requested period (default the last 7
   days), grouped by template and by day, and `email_search_messages` for
   notable failures.
4. Structure the answer:
   - the plan's ranked actions, with severity and evidence
   - headline numbers: sent, delivered %, open %, click %, bounce %,
     complaints, unsubscribes
   - per-template standouts, best and worst
   - the three highest-impact next moves

Read rates carefully. The complaint rate is complaints divided by mail to
inboxes that report spam (Gmail and iCloud never do); at 0.08% or above, say so
and recommend investigating. Opens are inflated by mail-privacy proxies, so
lead with clicks when they disagree.

If the plan surfaces an A/B winner ready to promote, present it, and call
`email_promote_ab_winner` only on the user's explicit go-ahead.
