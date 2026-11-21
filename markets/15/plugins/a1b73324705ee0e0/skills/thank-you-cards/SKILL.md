---
name: thank-you-cards
description: After an event, stage a thank-you card draft in Excellent from the event's facts and its guest photo wall, for a person to review and publish from the event page. Use for "thank-you card for last Saturday's rehearsal dinner", "draft thank-yous for this weekend's events", "follow up with last week's hosts".
---

# Post-event thank-you cards

This skill stages drafts only. Nothing reaches a guest until a person reviews and publishes the card from the
event's page in Excellent.

## 1. Find the events

1. If the person names an event, `search` it (`kind: "event"`). Otherwise `list_events` with
   `status: "completed"` and keep the recent ones the person means (for example, last weekend's).
2. For each, `get_event` to confirm it is the right one: title, date, host, party size.

Read the list back and ask which events to draft cards for. Each call stages a NEW draft, so don't call it
twice for one event, and check with the person before drafting for an event that may already have one. Don't
draft a card for an event that hasn't happened yet or was lost.

## 2. Draft

For each event the person confirmed, call `draft_thank_you_card` with its `event_id`. Excellent writes it from
the event's own facts and its guest photo wall. Give back what was staged and the review link from the answer;
to find a link again, `get_review_link` with `kind` `card` and the card's `id`. If Excellent refuses one, pass
on the reason it gives.

If the answer says the connection's access does not include this tool, the connection was approved without
draft access: the person disconnects and reconnects the connector, ticking draft access. If it says the
person lacks permission, an administrator grants it on the Team page in Excellent.

## 3. Hand off

End with the links and one line: "These are drafts. Nothing reaches a guest until you review and publish each
one from the event page in Excellent."

Safety: every card is a draft behind its review link; nothing is published or sent to a guest from ChatGPT, and
nothing is changed, charged or deleted.
