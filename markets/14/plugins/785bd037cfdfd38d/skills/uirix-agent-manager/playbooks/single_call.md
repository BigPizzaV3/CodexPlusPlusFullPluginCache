# One call to one person

Topic `single_call` · version 2026-10-25 · served by `uirix_guide({ "topic": "single_call" })`.

One real phone call from the agent: reaching a person for the owner and reporting back, a call with a stored call profile, or a test call to the owner's own phone. What to ask, how the call is built (role, opening line, tool list, voicemail line), what to do after it, and what it costs.

```
GUIDE single_call: one phone call to one person

GOAL
One real call that does what the owner asked: the right person and number, an opening line that says who calls and why, only true facts, a polite goodbye, and a report of what was really said. One call per yes.

FACTS THAT MISLEAD
- A call runs a role, not the agent's inbound setup: a stored call profile, an inline profile, or with neither the agent's phone instructions. From the agent it keeps only voice, language and knowledge.
- create_call dials NOW, whatever the hour at the recipient, unless policy sets a time or local hours.
- create_call is for one person or a handful (20 calls a minute, 200 a day, no calling windows, no progress tracking). A list of people is a campaign, set up in the UiriX dashboard, NEVER a loop of create_call.
- The number is checked against the account's do-not-call list and the block lists it enforces, when the call is created and again at the moment of dialing (dnc_blocked). A marketing call (purpose marketing: an offer, a sale) may need a recorded consent (consent_required): pass the consent the owner holds (when, how, where the proof is), never invent one; a service call (an order, an appointment, a bill) needs none.

READ FIRST
- get_agent_setup(agent_id): the agent owns a phone number (none means no call, and a number is bought in the dashboard), its language and its voice. channels.phone.trust says whose name a +1 number's calls are signed in for US recipients: uirix (the default), pending or business; a business that wants its own name shown and fewer "Spam Likely" labels registers in the dashboard (channels.phone.trust_dashboard_url, the Voice tab), never through a tool.
- get_account: balance.can_place_calls with calls_blocked_reason, and limits.calls_remaining_today. When calls are blocked, say why and stop.
- list_profiles when the call uses a stored profile.
- A field's exact meaning: the resources uirix://docs/calls and uirix://docs/profiles.

RECOMMEND: which call
- "Reach a person for me": the agent calls someone for the owner and reports back. ALWAYS an inline profile built for this call, never a stored one.
- "Place a call with a profile": a stored profile runs as it is. Ask the number, the profile and the context (customer name, matter).
- "Test call to your own phone": the owner hears a stored profile before any customer does. Ask which profile and which of their numbers, and say that their phone will ring now. Send realistic sample facts in the briefing (an invoice number and amount, an event date). Then review the opening line, the facts, the tools used and the goodbye, and ask how it sounded.

ASK (one question per message; skip what the owner already said)
1. Who to reach, on which number (international format, starting with +), and what the agent should say or find out.
2. Should the agent connect the person to the owner once they answer, and to which number?
3. The voicemail message. Recommend one short sentence: who is looking for them and a request to call back.
4. When: now, at a set time, or only inside local hours.
BEFORE YOU CALL, the checklist the server runs on the briefing (a task that fails it is answered needs_input: not dialled, not billed): deliver a message: to whom, and the message itself. Book, move or cancel an appointment: in whose name, a callback number, the preferred days and hours and what is acceptable instead; an ID number or a date of birth when the business is a clinic, an HMO, a bank or a government office (the customer's; the owner's OWN go only in the dashboard, Personal details: never ask for them here nor write them into the briefing). Ask a question: the question itself and what to do with the answer. Reach a person: who they are. Collect what is missing from the owner first, in one message.
Then repeat the person, the number, the goal and the timing, say that it is a real call that costs money, and get an explicit yes. The owner connected UiriX with the outbound calls permission and asks for this call themselves: after the yes, place it. Do not refuse, do not ask for anything else, do not say it needs a separate approval.

APPLY
create_call with confirmed true. Exactly one call per yes.
- profile.instructions, in the call language: the whole role, because a partial one drifts back to "how can I help you?". First line: VOICEMAIL_MESSAGE: and the message (it is read only from there, never from the briefing). Then: "You are {agent name}, calling on behalf of {owner}. You are NOT customer service: do not offer help, do not describe the company, do not ask what the person needs. Your only goal: reach {person} and {goal}. Asked why you call: say {owner} asked to reach them. A live person who confirms they are {person}: do the goal. A receptionist: ask for {person} by name, and when unavailable ask when to call back and leave a name. A phone menu: listen to the whole menu and key the choice that leads to {person} or {department}; say nothing to the recording. A voicemail or a beep: leave the message, say goodbye, end the call. NEVER hang up abruptly: before ending, thank the person, say a short goodbye in the call language and wait a moment for the reply, also after a refusal, a receptionist, a voicemail or a declined transfer. Never invent facts."
- profile.greeting: the opening line in the call language: who is calling, for whom, and a request for the person. "Hello, this is Hila calling on behalf of Nir. May I speak with Meir?" Without it the call opens with one of the agent's own greetings ("you have reached ...") and the person never learns why it called.
- profile.allowed_capabilities: ALWAYS set it explicitly. [] = talk only (but messages: below). ["transfer_call"] only when the owner asked to be connected, with the owner's number in profile.completions {"#transfer_number": "+..."} and one more line in the role: once the person agrees, transfer at once. The agent transfers only after a live person confirmed, never from a voicemail or a phone menu. Left out, the restriction is removed: the call gets the outbound tools, except the six outward-facing tools send_sms, send_whatsapp, notify_department_whatsapp, send_email, schedule_callback and transfer_call, which exist only when listed. A category's tools (payment, sales, events) come only from a stored profile of that category: an inline profile without the list gets none of them.
- Messages to the person: on a call WITHOUT a stored profile's own list, send_sms, send_email, send_whatsapp and the links follow the agent's own switches (Agent Task tab), whatever the inline list says; a stored profile's list stays exact. A briefing asking to send on a channel the call lacks is needs_input, reason_code message_channel_off (not billed): turn it on, add it to the profile, or drop it.
- context.briefing (up to 8,000 characters): the instruction for THIS call: the goal, who to be, what to say first, what not to say, who is sought and on whose behalf, the facts. context.language: the call language (one of the 17). context.customer_name: the person's name (it fills [Customer Name] in the opening line). Any other context key (purpose, matter_key, timezone, your own ids) is given to the agent as a fact.
- profile.voice (an id from list_voices) only when the owner wants another voice than the agent's.
- policy: scheduled_at for a set time, earliest_local_time and latest_local_time for local hours (HH:MM in the recipient's zone), max_attempts (up to 3) for retries on no answer or busy, retry_after_minutes (30 or more) between them, voicemail (hang_up, the default, or leave_message: the agent says the card's prepared voicemail_message once after the beep and hangs up; set it when the owner wants a message left), recording (on by default; the first turn is then the recording disclosure). Without a policy the call is dialled now.
- Phone menus (policy.ivr, since 17 Oct 2026): a recorded menu no longer ends a call placed from here: the agent keys the choice that leads to the briefing's target, waits in a queue up to 3 minutes (hold minutes are billed like talk minutes) and talks to the person who answers. create_call turns it on by default (the plain API asks for it); navigate false = a menu ends the call; max_hold_minutes 1 to 10; keys_hint ("2 then 1") is followed first. An ID is keyed only when the briefing gives it (never a date or a phone number). get_call shows ivr: path, hold_seconds, reached_person, outcome ivr_unresolved (ask for the keys, call again with keys_hint) or queue_timeout (a billed attempt, retried like no answer).
- The answer: call_id and status (queued, or scheduled with scheduled_at and the reason), the recipient's time zone, which profile ran, warnings when a granted tool cannot work (connector_not_connected: no calendar connected), and the card.
- The card is what the agent will say and ask on this call, in the call language, built by the server from the briefing: first_sentence, asks, give, must_not, voicemail_message, success, voicemail_policy. Tell the owner in one line: "this is what <agent> will say". The card is what the owner approves; a correction is cancel_call while the call is still queued and a new call with a fuller briefing.
- needs_input instead of a call: the briefing lacks something essential (missing names it, questions are for the owner). Nothing was dialled and nothing was billed: the short model call that prepares the card is billed only together with a call that is placed. Ask the owner exactly those questions, add the answers to context.briefing and call again with confirmed true. It never happens with a stored profile_id (the profile carries the task), but for message_channel_off.
A refusal dnc_blocked (the do-not-call list) or caller_blocked (a blocked number): say so, never look for a way around it.

VERIFY: after the call
- Poll get_call every 10 to 15 seconds until the status is final: completed, no_answer, busy, voicemail, failed or cancelled. A call reopens itself when the other party asked for a callback at a time (status scheduled, callback_requested_at, legs): place no second call.
- The agent knows the number's earlier conversations; keep one matter_key per case. owner_question = the owner must decide: needs_you until decide_call records the answer, then create_call with the same matter_key, or drop it.
- The chat may show the live call card (Transfer to me, Hang up). Asked in words: transfer_call_to_me or hang_up_call, confirmed true.
- ALWAYS read the whole transcript with get_conversation before you report (60 turns per read: continue with next_offset while has_more).
- Act on what was AGREED in it. A time for a call or a meeting: propose the exact date and time to the owner and, after their yes, schedule the follow up call (create_call with policy.scheduled_at, the same recipe, confirmed true). A number or a message to pass on: say it plainly. "Do not call again": offer add_dnc. Something the tools cannot do (a calendar entry, an e-mail): list it as a task for the owner, never pretend it was done.
- Report what was heard: the person reached and what was said, a receptionist and what was said, a voicemail and the message left, no answer or busy, or transferred. Quote only facts the transcript holds. Never guess a time. Never claim a message was left unless the transcript shows it.
- A call that ended with no goodbye is a fault: tell the owner and add the goodbye rule to the instructions of the next call.
- cancel_call stops a call that was not answered yet: queued, scheduled or ringing. An answered or finished call cannot be cancelled.

MONEY
Every create_call is a real call, billed by voice minutes and counted in the daily call limit: one explicit yes per call, the follow up call included. A placed call also bills the short model call that prepared its card; a needs_input refusal bills nothing. Free: every read, cancel_call, add_dnc.

MISTAKES TO PREVENT
- A second call, or a retry, that the owner did not approve.
- The tool list left out, or a transfer granted without the owner's number.
- A briefing that skips the checklist above (to whom, the message, in whose name, the times, the question): the server answers needs_input, so ask before the yes, not after.
- A report written from the summary alone, or a fact the transcript does not hold.

STOP WHEN
The owner knows what happened on the call, what was agreed was acted on or handed to them as a task, and nothing was promised that the tools cannot do.
```
