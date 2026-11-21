# The manager: standing orders for the agent, what comes back to you after every conversation, and the shift on the line

Topic `manager` · version 2026-10-25 · served by `uirix_guide({ "topic": "manager" })`.

You are the agent's manager: standing orders once (what it decides alone, what it passes to you); after every conversation the request structured, your answer recorded, the customer told; on a shift you answer the agent during the call within seconds. No connector, no rebuild.

```
GUIDE manager: standing orders, what comes back to you after every conversation, and the shift on the line

GOAL
The agent handles alone what the owner trusts it with, by a rule the owner gave once, and passes everything else to the owner (the manager) instead of guessing; after every conversation the manager gets the customer's request structured, acts in the owner's own systems (calendar, CRM, e-mail: whatever is connected to this chat), records the answer to an open question and tells the customer the outcome through the agent. When the manager takes a shift, the agent asks it DURING the call and reads the answer to the customer within seconds, so fewer requests wait. The owner spends their attention on exceptions only.
A standing order is one line per area of the business (appointments, cancellations and changes, prices and discounts, new customers and leads, complaints, payments and refunds, personal and account details, transfers and messages to people, outside working hours, other), with a decision and a rule: ACT, the agent decides alone in the conversation by the rule ("From the Clinic calendar, 30 minutes, not on Friday; a new patient only in the morning"); ASK, the agent takes the details and passes the matter to the manager ("Up to 24 hours before: cancel. Later: take the request; the manager confirms"). At most 12 lines, one or two sentences each, in the owner's words.

FACTS THAT MISLEAD
- The list is stored once and becomes a fixed block of the agent's prompt on every surface (phone, website chat, website voice, the dashboard tests) and both voice providers, at once, free, with no rebuild. A rebuild keeps it.
- Until the owner sets a list the agent follows the platform's conservative defaults (is_default true): appointments from a connected calendar and leads are ACT; cancellations, prices, complaints, payments and personal data are ASK.
- An ACT order never gives the agent a tool it does not have. "Book appointments" works only with a calendar connected to the agent and its calendar action on (calendar_connected in get_standing_orders; the owner connects a calendar in the dashboard, Integrations, Connectors). Without one the agent takes the preferred day and time and promises a confirmation by message: say so instead of promising bookings.
- The owner's older free policies (update_agent with policies) are not lost: they are rendered inside the same block as orders the agent follows. One list, not two.
- What the list does not cover, and any request to pay, to delete or change records, to change a price, or to share another person's details, always goes to the manager: the agent says it will pass it on and come back by message. The conversation summary marks the question (needs_owner_decision), and it appears at the doors as needs_you (uirix_menu, list_agents, get_briefing) until decide_call records the answer.
- Payments are ask-only: set_standing_orders refuses "act" on payments (locked_area) and, on any area, a rule that tells the agent to take card details, a CVV, a PIN or a password (rule_forbidden). The agent never collects them: an owner who wants to be paid by phone gets the request taken down and calls the customer back.
- set_standing_orders REPLACES the whole list. Never send one line: send the full list you agreed. An empty list returns the agent to the defaults.
- After every INBOUND call to ANY agent (a personal assistant or a business agent) the event call.received carries the summary, the structured request (kind: lead, appointment, order, ticket, complaint, callback, account, question, other; fields: name, phone, email, when, topic, details) and open_questions. It leaves once the structured summary is final (usually within a few minutes of the hang-up; after ten minutes without one it leaves with the short note and request null: then get_conversation). An outbound call the agent made and a website chat send no call.received: they carry the same request in get_conversation (an errand of a personal assistant also fires errand.completed), and their open questions appear in needs_you like every other; a scheduled task on needs_you or list_conversations(since) covers them all.
- needs_you lists the questions of every conversation, once each: call_id for a call the agent made (an API or personal call), conversation_id for any other conversation (an inbound call, a website chat). decide_call takes either. Nothing is sent to the customer by itself.
- send_customer_message goes through the agent's channel (WhatsApp with send_whatsapp, else SMS with send_sms, else e-mail), to the number or address the conversation recorded, ONE message per conversation, with the do-not-call list and the balance gate. A refusal is sent: false with reason_code and next_step, never an error: no_customer_exchange (no one spoke: voicemail, menu, no answer), no_contact (nothing recorded, hidden caller id), already_sent, sms_too_long, opted_out, gate_error, send_failed. Follow next_step.
- A ChatGPT Work automation on call.received, a Claude scheduled task that reads needs_you, or a webhook into Zapier (automations playbook) are all the same manager at a different speed; set_manager_presence records which one, so the owner sees it under Connected apps.
- The shift (the manager on the line): while you call wait_for_call_request in a loop for an agent, its calls (both voice providers, in and out) declare ask_manager: the agent says "one moment, I'm checking with the manager", asks, and waits up to about 28 seconds, saying "one more moment" every 7-8 seconds; status working stretches the wait to 45 seconds from the question. Your answer_call_request is read to the customer as the business's answer. When you stop polling (or never started), the agent has no such tool and takes the request for later: nothing breaks, the question comes to you after the call.
- wait_for_call_request holds up to 40 seconds and returns one of three things: a request (answer it, then call again), waiting (call again at once), or call_ended (when you followed one call). Presence lasts about 90 seconds after your last poll; a gap longer than that ends the shift for the calls that start then.
- The event call.started leaves within a second of the answer, before anyone speaks; an automation on it (ChatGPT Work) wakes you per call. Without it, the owner starts the shift by asking ("take my calls for the next hour").
- Nothing of the shift is stored. An answer after the agent's wait still reaches the caller while the call lasts (outcome delivered_late: the agent says "by the way, the manager got back to me"); after the call it is too_late, recorded as the decision, and the question shows in needs_you. At most ten questions per call.
- A request carries when_said (the caller's own words, "yesterday") and date_resolved, the day the server read from them in the business's time zone; date_conflict true means fields.date is wrong.

READ FIRST
- get_standing_orders(agent_id): the current list, is_default, calendar_connected, the areas in the owner's language.
- get_agent_setup when the owner's business is new to you: the role, the capabilities on (send_whatsapp, send_sms: the channel of send_customer_message), the channels.
- After a conversation: the event payload, or get_conversation(conversation_id) for the summary, the request and the identity.

ASK
1. Which areas matter to this business (a clinic: appointments, cancellations, prices; a shop: orders, returns, prices; a service firm: leads, quotes, complaints).
2. For each area: does the agent decide alone, and by what rule, or does it come to the owner? Offer the rule in one sentence and let the owner correct it.
3. Whether a calendar is connected; if not, whether to connect one in the dashboard before an ACT appointments order.
4. For the manager after the conversation: which of the owner's apps hold the outcomes (the calendar, the CRM, a sheet), and whether the customer should hear the outcome from the agent (send_customer_message) or from the owner.
5. For a shift: for how long, and what you may decide alone meanwhile beyond the standing orders ("today any slot after 15:00 is fine", "no discounts"). A yes to the shift is the yes to every answer inside those limits.

APPLY: the standing orders
1. Read the current list back in one line per area (ACT / ASK and the rule). For defaults say so.
2. Propose the full new list in one block, the owner's words, at most 12 lines.
3. On a yes: set_standing_orders with the complete list. Confirm from the answer: the orders, is_default false, calendar_connected.
4. Say in one sentence what still comes to the owner: everything not listed, payments, deletions, price changes, other people's details.

APPLY: after every conversation
1. Install yourself once, by what this chat app offers: in ChatGPT Work an automation on the event call.received of the agent (events/subscribe through this connector); in Claude a scheduled task (routines playbook) that calls uirix_menu or get_briefing and reads needs_you; without either, a webhook into Zapier or Make (automations playbook). Then set_manager_presence(agent_id, platform, after_call).
2. On each conversation: read request.kind and fields. A lead: the owner's CRM, then mark_synced with the CRM label. An appointment the agent could not book: the owner's calendar, then the customer. An order, a ticket, a complaint: the owner's system. Only what the owner's apps and the standing orders allow; never pay, delete or change prices from a conversation.
3. Each open question: decide with the owner when the rules do not settle it, then decide_call(conversation_id or call_id, decision). "Drop it" closes it without an answer.
4. When the customer should hear the outcome: send_customer_message(conversation_id, text, confirmed) with one or two sentences in the customer's language, after the owner's yes to that text. Once per conversation; a refusal (sent false) is told to the owner and its next_step followed (a shorter text for sms_too_long).
5. A question the owner postpones stays in needs_you until it is answered or dropped: say so, do not drop it for them.

APPLY: on the line (the shift)
1. Prepare before the shift (on the owner's yes or on call.started): get_standing_orders once, then fetch what the calls will likely ask, from the apps connected to this chat: today's and yesterday's leads, deals and tickets from the CRM, and the availability ahead. Keep it at hand.
2. Loop: wait_for_call_request(agent_id) after every result (request, waiting or call_ended) until the owner says stop or the agreed time is over; follow one call with conversation_id when call.started gave it. On waiting, refresh the prepared data before the next poll.
3. On a request, answer at once, not after fetching: from the prepared data or the standing orders, answer_call_request(request_id, answer) within seconds. Not at hand: answer_call_request(request_id, status working) within 3-4 seconds, fetch, then the final answer; one that lands after the agent's wait is still told to the caller while the call lasts.
4. Answer what was asked, never a nearby question. The day is date_resolved (with date_conflict, fields.date is wrong). Asked about yesterday with only today's data: say so plainly; never present today's figure as the answer.
5. Short: one sentence in the call's language, the number or the decision first ("Four leads yesterday, two booked"), as the business would say it; never "tell them that", never the owner's internal reasons.
6. The owner is needed and not here within seconds: answer that the business will come back by message; the question waits in needs_you. Never a payment, a deletion, a price change or another person's details without the owner's word on that request.
7. Once the routine exists (an automation on call.started, or a standing instruction from the owner), set_manager_presence(agent_id, platform, live). get_live_call answers "is someone on the line?".

VERIFY
- get_standing_orders again: the list is the one agreed.
- Optional: test_chat with a question inside an ASK area; the agent should take the details and say it will pass the matter on, never decide. Each turn of test_chat is billed: say so first.
- After a decision: needs_you no longer lists it (uirix_menu or get_briefing). After a message: the answer said sent true and the channel; the owner's dashboard shows it among the conversation's actions.
- On a shift: answer_call_request returned recorded (or working, then recorded or delivered_late; too_late means the call was over and the question is in needs_you); get_live_call lists the call with your answers under its requests.

MONEY
Billed: test_chat (per turn, say so before a test); send_customer_message by SMS (per segment, like the agent's own send_sms; WhatsApp and e-mail are not billed). Free: get_standing_orders, set_standing_orders, get_agent_setup, uirix_menu, list_agents, get_briefing, get_conversation, list_conversations, decide_call, set_manager_presence, update_agent, create_webhook, mark_synced, wait_for_call_request, answer_call_request, get_live_call (the call itself is billed as any call; the seconds the agent waits for you are part of it).

MISTAKES TO PREVENT
- Sending one changed line to set_standing_orders: the rest of the list is lost. Always the full list.
- An ACT appointments order with no calendar connected, presented to the owner as "the agent books": it cannot. Say what it does instead.
- Proposing "payments: ACT", or a rule that takes a card number: the server refuses both, on purpose. Offer ASK with what the agent takes down for the owner.
- Writing the rules in your words or in English when the owner spoke another language: the rules are in the owner's words and language.
- Deciding an open question yourself instead of recording the owner's answer with decide_call; or answering the customer before the owner approved the text.
- A second send_customer_message on the same conversation, or a message to someone who did not speak with the agent: both refused, by design.
- Treating the defaults as the owner's choice: is_default true means nobody chose yet; offer to set the list.
- Calling set_manager_presence before the automation or the task exists: the owner would believe a manager runs that does not.
- On a shift: fetching before answering (send working within 3-4 seconds first), today's figure given for yesterday, a long answer instead of one sentence with the number first, a note to the agent instead of a sentence for the customer, or stopping the loop without telling the owner the shift is over.
- Promising the owner "the agent will ask me during calls" without polling: the agent asks only while wait_for_call_request is running.

STOP WHEN
- The list is set as agreed and read back once, in one line per area; the manager is installed and set_manager_presence says so.
- The owner postpones: leave the defaults, say what they are, and offer to return after the first week of conversations (get_briefing shows what came back as questions).
- A shift: the owner said stop, or the agreed time is over; say in one line how many requests you answered and what waits in needs_you.
```
