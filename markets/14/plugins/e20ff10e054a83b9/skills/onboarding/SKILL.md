---
name: onboarding
description: Check the Simple Affiliate connection, name the connected Shopify store, and show what to ask, when the user chooses Set up for Simple Affiliate or asks how to get started.
---

# Set up Simple Affiliate

Simple Affiliate runs the affiliate program of a Shopify store: affiliates, groups, referrals, commissions and
payouts. The connection acts as the staff member who connected, on one store only.

1. Check the connection by calling `get_program_status` with `{}`. If it fails, tell the user to reconnect Simple
   Affiliate from the plugin's settings, and stop.
2. Name the connected store. The server's instructions say which store this connection reached ("Connected to Simple
   Affiliate for the store …"). Say it in one short sentence. If a check of the result has the status action_needed,
   name it in one line with its link.
3. Offer three things they can ask, one line each:
   - "How did my affiliates do in the last 90 days?"
   - "What do I owe my affiliates, and who can't be paid?"
   - "Raise the commission of the VIP group to 15%."
4. Explain in one sentence that each change in Simple Affiliate happens only after they click Confirm in the card
   that appears, that ChatGPT does not pay affiliates or change the payout settings, and that a
   new affiliate, an approval or a referral is prepared as a link that they save in the Simple Affiliate admin.

Keep it short. If the user installed the plugin in the middle of a task, continue that task in the same conversation.
Never list the affiliates or their data during setup.
