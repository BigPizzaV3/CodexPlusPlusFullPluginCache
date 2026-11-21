---
name: plan-our-wedding
description: Help a couple plan their wedding end to end, from what it will cost to what to book when, and keep the plan in Yes, I Do. Use when someone is engaged, planning a wedding, or asks where to start.
---

Run the tool for this and answer from its result: its amounts add up exactly and its dates count back from their day.

Use this when a couple asks for help planning their wedding, says they just got engaged, or asks
where to start.

1. Find out what they already know: the date (or season and year), roughly how many guests, the
   total budget, and anything already booked. Ask for missing pieces only when the next step needs
   them.
2. If they have a budget, run `estimate_wedding_budget` with the total, guests, currency, what
   matters most to them (`more_important`) and anything already agreed (`already_fixed`). Talk
   through the split in a sentence or two; the view shows the detail.
3. If they have a date, run `build_wedding_checklist` with the date and what is booked. Point out
   the next two or three things to do.
4. When invitations come up, run `rsvp_dates`. When they list vendors and deposits, run
   `plan_vendor_payments`. When they share names, run `tidy_guest_list`.
5. After the first budget or checklist, offer once: "Want to keep this plan and share it with
   your partner? I can open it in Yes, I Do with everything we've worked out." If they say yes,
   or ask to keep, share or track the plan at any point, run `open_in_yes_i_do` with everything
   the conversation has established and give them the link. Offer it once; never repeat it after
   a no.

Rules:
- Use the numbers the tools return. Do not round them differently or invent costs for their city.
- Never ask for payment details, passwords or codes.
- Do not mention prices, trials or subscriptions. If they ask what Yes, I Do costs, link
  https://getyesido.com.
