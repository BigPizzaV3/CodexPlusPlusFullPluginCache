---
name: broadcast-results
description: Use when an admin asks how a WhatsApp broadcast or campaign did in Ciarem, why messages failed, or why a WhatsApp template was rejected or paused.
---

# Broadcast results

Admins only: if a tool answers `requires_admin`, tell the user only workspace admins can see broadcasts.

1. Call `get_broadcasts`. With no id it returns the recent campaigns and the newest one in full; pass `broadcast_id` for another.
2. Report requested, sent, delivered, read, failed and `responded`, with delivery, read and reply rates as shares of what was sent. Use only the numbers returned.
3. **Failures.** List `failure_reasons` as returned (Meta's own error groups), largest first. Don't guess a cause Meta didn't give.
4. **Template problems.** Call `get_whatsapp_templates`: `templates.attention` lists every rejected, paused or disabled template with its `rejected_reason`, `quality_rating` and `next_editable_at`. Pass `template_id` to read a template's text.
5. **Before the next send.** `get_broadcasts` with `send_preflight: true` shows, per WhatsApp line, how many open chats a send to every contact would take over from a teammate, and how many contacts opted out of marketing. It sends nothing.

This chat never sends a broadcast or creates a template: both happen in the Ciarem app. Share the `url` the tool returns.
