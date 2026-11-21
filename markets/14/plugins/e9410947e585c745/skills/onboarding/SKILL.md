---
name: onboarding
description: Check the Simple Chat connection, name the connected Shopify store, and show what to ask, when the user chooses Set up for Simple Chat or asks how to get started.
---

# Set up Simple Chat

Simple Chat is the support inbox and AI agent of a Shopify store. The connection acts as the staff member who
connected, on one store only.

1. Check the connection by calling `list_inbox_conversations` with `{}`. If it fails, tell the user to reconnect
   Simple Chat from the plugin's settings, and stop.
2. Name the connected store. The server's instructions say which store this connection reached ("Connected to Simple
   Chat for the store …"). Say it in one short sentence, and mention how many conversations are waiting, if any.
3. Offer three things they can ask, one line each:
   - "What's waiting for me in Simple Chat?"
   - "Show the drafts and proposals that need my approval"
   - "Why is AI resolution low for Returns and refunds? Replay it for the last 90 days."

   When they ask what needs their approval, show the drafted replies (`list_pending_customer_drafts` for each open
   conversation) and the refund, cancel, order change, customer record and replacement order proposal cards
   (`list_staff_proposals`). While a list call returns hasMore true, call it again with offset set to nextOffset.
4. Explain in one sentence that sending or discarding a drafted customer reply, rejecting a proposal card, approving an
   order change or customer record card, and running a paid topic replay only happen after they click Confirm in the
   card that appears, that refund, cancel and replacement order cards are approved in the Simple Chat dashboard, and
   that topic replay needs the Premium plan.

Keep it short. If the user installed the plugin in the middle of a task, continue that task in the same conversation.
Never quote customer messages back during setup.
