---
name: get-started
description: Connect to Spredo and get oriented. Checks which Spredo workspace the user is signed in to, its plan and the user's role, then suggests what to ask next. Use right after Spredo is installed, or when the user asks what Spredo can do for them.
---

# Get started with Spredo

Spredo is a CRM for B2B outreach on Telegram: campaigns, leads, message templates, follow-up
sequences, the team inbox, and audience building.

1. Call `get_me`. If it fails with an authentication error, ask the user to finish connecting
   their Spredo account, then try again.
2. Call `get_client_data` for the workspace name and balances.
3. Tell the user, in two or three sentences:
   - which workspace they are connected to;
   - what their plan covers, from `client_plan`:
     - `full_package`: campaigns, inbox, sequences and audience building;
     - `crm_only`: campaigns, inbox and sequences, but not audience building;
     - `data_only`: audience building only;
   - if `read_only` is true: they can look at everything but change nothing.
4. Offer up to three next steps that fit their plan, for example:
   - "Which campaign has the best reply rate this month?"
   - "Summarize the replies in my inbox that still need an answer."
   - "How many founders at crypto funds could I reach?"

Keep it short and don't call other tools until the user picks something.

Before anything that sends a Telegram message, starts a campaign or sequence, or uses the
workspace balance, show the user exactly what will happen and wait for a clear yes.
