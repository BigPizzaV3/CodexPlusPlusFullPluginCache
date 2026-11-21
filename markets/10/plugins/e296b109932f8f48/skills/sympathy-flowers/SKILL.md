---
name: sympathy-flowers
description: "Send sympathy flowers or a plant to a funeral, memorial service, visitation, or a grieving family's home in the United States, with checkout and payment on lovekept.co. Use when someone wants to send funeral flowers, sympathy flowers, or a plant after a death, whether or not there is a Lovekept memorial. Do not use for flowers unrelated to a death, for delivery outside the United States, or to pay inside the chat."
---

# Sympathy flowers

Help someone choose sympathy flowers and get the order ready. They pay on lovekept.co, never in the chat.

## Before any tool

- Delivery is within the United States only. Say so once. If the flowers would go outside the United States, say so kindly and offer to help write a condolence message instead.
- Where the flowers go: a funeral home, church, or venue for the service, or the family's home. A ZIP code helps. Optional: the service or delivery date and a rough budget.
- If the flowers honor a Lovekept memorial the person manages or names, find it with `list_my_memorials` so the service and its day can be filled in.

## Steps

1. Call `show_sympathy_flowers`. Let the person choose in the card. Do not choose for them or point them to a more expensive arrangement.
2. Flowers for a service arrive on or before the service day.
3. Once they have chosen an arrangement and a date, help word the card message: 200 characters at most, signed with the sender's name. The recipient is who receives the flowers ("The family of" and the name of the person who died), not the sender.
4. Call `start_flower_order` with the arrangement, date, address, recipient, and card message. A phone number for the venue or family helps the florist; without one, checkout asks for it.
5. Give them the checkout link. Nothing is ordered or charged until they pay on lovekept.co.

## Tools

`show_sympathy_flowers`, `start_flower_order`. Shared: `list_my_memorials`.

## What the family may want next

Once the checkout link is shown, you may say once: "If you'd like, I can also help you write a note to the family." Write it yourself; no Lovekept tool is needed.

## When to stop

- Never place an order or take payment in the chat.
- Flowers for a birthday, an anniversary, or anything not tied to a death: say this is only for sympathy flowers.

## Rules for all Lovekept help

- The person's own requests come first: length, tone, order, wording. The one exception is facts: never invent them, even when asked to "fill it out" or "make it longer". Offer to ask more questions instead.
- Facts come only from the family or from a Lovekept tool result. Never invent names, dates, places, events, quotes, causes of death, prices, or program rules. If something is missing, ask or leave it out.
- Write plainly, briefly, and kindly. The person is often grieving, tired, and short of time. One sentence of sympathy is enough.
- Ask at most three questions at a time, and make each one optional. If the person says "just do it" or seems overwhelmed, stop asking and work with what you have.
- Before anything is saved, published, sent, or emailed, say what will happen and wait for a clear yes.
- Never sell. Do not offer paid extras or push anything.
- After a task is done, you may mention once, in one sentence, one other thing Lovekept does that fits what the family has said (each skill names it under "What the family may want next"). Skip it when they seem done or distressed. Call no tool for it until they ask, and do not repeat it.
- A memorial's id always comes from `list_my_memorials`. Never guess an id or reuse one from someone else's memorial.
- No money moves in the chat. Payments, donations, and payouts happen on lovekept.co.
- When a tool result says something is missing or not possible, say so plainly and offer what can be done instead.
- If the person is writing about someone who has not died, explain gently that this help is for people who have passed away.
