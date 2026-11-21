---
name: daily-leads-and-replies
description: Use when the broker asks what they have to do today, which buyers are waiting for a reply, or wants help answering a buyer enquiry.
---

1. Call `get-my-day` to list today's and overdue tasks, buyers waiting for a reply and new leads.
2. To reply to a buyer, first read the lead with `get-lead` (enquiry, conversation, notes).
3. Write the reply in the buyer's language, specific to the boat. Do not promise prices, dates or conditions the broker has not confirmed; ask the broker if needed.
4. Save it with `draft-lead-reply`. It is not sent: tell the broker that the reply is pre-filled in BrokerForBoat for them to review and send.
5. If the broker asks, add a note (`add-lead-note`), a follow-up task (`create-lead-task`) or move the lead to another stage (`set-lead-status`; for "lost", ask for the reason).
