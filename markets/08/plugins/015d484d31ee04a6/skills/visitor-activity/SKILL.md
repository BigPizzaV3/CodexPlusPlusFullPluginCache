---
name: visitor-activity
description: List recent anonymous visitors to an OpenRevenue site and show one visitor's journey. Use when the user asks who visited recently, for the latest visitors or sessions, or what a particular visitor did. Do not use for headline traffic totals, referrers, funnels, goals, or performance.
---

# Visitor activity

Use this skill for recent visitor rows and single-visitor journeys on a site the user can access. Visitors in OpenRevenue are anonymous: there are no names or email addresses.

1. Resolve `domain` (ask, or call `list_projects` if needed).
2. For recent visitors, call `list_visitors` with `domain`, period (`24h` default, or the period the user names; `yesterday` is accepted) and `limit` (10 unless they ask for more, at most 100).
3. For one visitor's journey, call `get_visitor` with `domain` and a `visitorId` taken from a `list_visitors` row. Never invent a visitor id.
4. Show lists as a compact table and journeys as pages in order, using only fields the tools returned.
5. Do not guess who a visitor is or try to identify a person from location or device details.

If a tool errors or access is denied, say so and stop.
