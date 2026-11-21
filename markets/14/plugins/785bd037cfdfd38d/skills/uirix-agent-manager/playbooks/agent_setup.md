# Review and set up an agent

Topic `agent_setup` · version 2026-10-25 · served by `uirix_guide({ "topic": "agent_setup" })`.

The full review of one agent and how to build it properly: learn the business from its knowledge, check role, style, focus topics, tasks, actions and their details, custom capabilities, greetings and whether the instructions are out of date, then recommend, apply and verify.

```
GUIDE agent_setup: review the agent and build it properly

GOAL
The owner ends with an agent that fits the business: the right role and style, focus topics backed by real knowledge, tasks and actions that work on the channels in use, every needed detail filled in, greetings that sound right, and instructions that are up to date. You own this outcome. The owner is a business person, not a technician: you decide what matters and explain why, they decide the business questions.

READ FIRST
1. get_agent_setup(agent_id), one call. It returns identity and settings (name, business, role, interaction mode, tone, description, language, the four greetings), focus topics, tasks, actions with their details, custom capabilities, connections, the knowledge state with the start of the summary, its outline and its gaps, the instructions per channel (size, when built, improvement rules, out of date or not and why), the channels (phone number, widget, voice), 30 days of activity (conversations, leads, average quality) and findings.
2. Learn the business from the knowledge block before you form an opinion. The outline and the gaps are enough for a first picture. Read more of the summary with get_kb_summary only for a topic you must judge. No summary at all means the agent answers from its instructions alone: knowledge comes first, in the Knowledge section of the menu.
For a review do not call the single readers (get_agent, get_prompts, get_kb_status, get_widget, get_voice, list_connectors): get_agent_setup already carries what they return.

LEARN THE BUSINESS (from the summary, never from imagination)
Extract and keep in mind:
- What it sells: products, services or both. One line of business or several.
- How customers buy: appointment, online order, quote, reservation, walk in, subscription, contract.
- Prices: in the knowledge or not. If not, the agent must not quote prices.
- Opening hours, address, service area, branches.
- People and departments a caller may ask for.
- Languages the customers use.
- After sale needs: support, returns, warranty, invoices and payments.
- Gaps: every "[NOT FOUND" marker is a fact the agent does not have.
Say the business back to the owner in one sentence and let them correct you before you change anything. If the summary and the owner disagree, the owner is right and the knowledge needs a correction.

CHECKS
Before presenting any findings, you MUST first state in one sentence whether the agent's role, tone, and actions fit this specific business. Learn the business from the knowledge summary, then judge fit against the business model: before you read out the rule-based findings, never after. With no knowledge summary yet, say that the fit cannot be judged yet, ask the owner in one question what the business does, and judge on their answer.
1. The judgement first, the one that rules cannot make:
- Do the role and the tone match how this business serves its customers? Treat the role as a default until you have judged it.
- Is every focus topic backed by facts in the summary?
- Is there a customer need (from the business model, or from the top issues of recent conversations) that no task or action covers?
- Is something switched on that this business has no use for?
2. Then the findings. Each has a severity (critical, warning, info), an area, a message and a fix. They were found by rule, so treat them as true. In owner words: critical = "Needs fixing now", warning = "Worth improving", info = "Nice to have". The other checks:
- Do the greetings name the business and sound like it?
- Does the knowledge use what the plan allows? knowledge.allowance says how many pages the crawl may store and how many it did, how many files the plan allows and how many were uploaded. Little of the allowance used on a real business: recommend crawling more of the website or uploading the owner's documents (knowledge playbook). Say the numbers as they are (for example "20 of 50 pages, no file yet").
- account.paid_actions: when billed actions are blocked, say so once, send the owner to Profile, Billing, and offer the free changes only.
Rule-based findings are never the whole review. An agent built from a website starts with a generic default role (Office Secretary, unless the owner picked another one when creating it) that may not fit the business. You have not completed the review until you have explicitly asked: is this the right role for this business? If you have not answered that, you are not done, regardless of how few findings the system returned. It is answered when the owner said yes to keeping the role or to the role you recommend; once answered, do not raise it again in this conversation.

RECOMMEND: settings
Role:
- Office Secretary (secretary): appointment and reception businesses (clinics, salons, garages, offices). It is also the role preselected when an agent is built from a website, so there it may be a default nobody chose: keep it only when customers book a time or come to a reception desk.
- Customer Service (customer_service): many existing customers and after sale questions.
- Technical Support (technical_support): products that need troubleshooting.
- Sales & Closing Deals (sales): the goal of a conversation is a lead, a quote or a sale.
- General Inquiry (general): an information line with several departments.
- General Consultant (general_consultant): the agent explains options and helps people choose.
- A Personal AI Agent (personal) is a different world: one person, not a business, created in the dashboard wizard. Never set it here, and never move a personal agent to a business role.
Interaction mode: active is the default. passive for law, medicine, finance and other fields where the agent should answer and take details only. aggressive only on the owner's explicit request, and say that it pushes every conversation toward a sale.
Tone: Polite & Friendly (service_friendly) by default. Formal & Respectful for law, finance and corporate. Calm & Empathetic for health and care. Technical & Clear for support. Enthusiastic & Persuasive for sales led consumer brands. Professional & Concise when customers want speed. Sexy & Sensual (sensual_playful) only when the owner asks for it by name: never suggest it.
Description: one or two sentences that say what the agent is for in this business. The builder reads it: a vague description gives vague instructions.

RECOMMEND: focus (what the agent knows)
A focus topic adds no facts. It tells the agent how to use facts the summary already holds. Switch a topic on only when the summary has the facts.
- Always: Business Hours, Location and Frequently Asked Questions.
- Policies & Terms when the summary holds cancellation, returns, privacy or payment terms.
- Products: Product Descriptions, or Product Catalog & Pricing. Choose the pricing one only when prices are in the summary and the owner wants them quoted. Add Product Variants & Options, Shipping & Returns, Specifications & Features, Warranty & Support when the summary covers them.
- Services: Service Descriptions, or Service Types & Pricing, by the same price rule. Add Duration & Process, Service Areas & Locations, Qualifications & Expertise, Consultation & Assessment when the summary covers them.
A topic that is on while the summary has a gap for it is a finding: get the facts from the owner (Knowledge section) or switch the topic off.

RECOMMEND: tasks and actions by business model
Tasks work with no setup. Actions need a detail from the owner. A callback request is captured with Create Lead or Create Support Ticket. A booking is offered with Send Appointment Link, or with the calendar actions when a calendar is connected (the new-appointment card can send its booking link instead).
- Appointment business (clinic, salon, garage, studio): Send SMS, Send Email, End Call, and exactly one booking path from the line above, or Create Lead so a person calls back when there is neither. Transfer Call to reception or an urgent line.
- Online shop: Create Support Ticket, Create Lead, Send Email, Send Website Link, Accounting Message for invoices and refunds, Send Payment Link on the phone. Create Order only if the owner wants orders taken in conversation.
- Leads and quotes (contractors, agencies, real estate, insurance): Create Lead sent to the person who follows up, Transfer Call to sales during working hours, Send Appointment Link for a consultation, Send Website Link. Role Sales & Closing Deals.
- Support desk: Create Support Ticket, Send Email, Transfer Call to the support line, Accounting Message for billing questions. Role Technical Support or Customer Service.
- Restaurant and hospitality: Send Appointment Link with the reservation link, Send SMS, Transfer Call to the host, Create Lead for events and catering, Create Order only for takeaway by phone.
- Professional services (law, accounting, consulting, medicine): Create Lead for new client intake, Transfer Call to named people or departments, Send Appointment Link, Accounting Message, Send Contract Link when agreements are signed online. Mode passive, tone Formal & Respectful, and an improvement rule that the agent gives no professional advice.
Every agent with a phone number: End Call on. Every agent: at least one way to keep a customer who needs a person (Create Lead, Create Support Ticket or Transfer Call). An agent with none of them loses customers: raise it early.
Links and messages to customers go by WhatsApp when Send WhatsApp is on (free), else by SMS (billed per segment), else by e-mail. WhatsApp a Department passes a message on when a call cannot be transferred.

CHANNELS DECIDE WHAT CAN RUN
Not everything the catalogue offers really runs. Website Chat runs only Create Lead, Send Email, Create Support Ticket, Create Order, Accounting Message, Send WhatsApp, WhatsApp a Department and calendar booking, plus the built in website search. Voice Chat has no call transfer and SMS does nothing there. Calendar booking runs on the channels the calendar policy allows (phone, website chat, website voice; the chat is off by default): get_calendar_policy, never "phone only".
get_agent_setup gives every task and action a surfaces status per channel: works, stub (answers success and does nothing), no_handler (the platform does not perform it today), not_offered. Recommend and rely on a capability only on channels where its status is works.
A capability that is switched on but works on no live channel is a finding: tell the owner plainly that the agent may promise something the platform does not do, and recommend switching it off or using the working alternative. Never tell the owner that chat visitors will be transferred or texted.

DETAILS (the values actions need)
- Ask with the capability's own question and show its example. One detail per message.
- Validate before you save. A link starts with https:// and is a real page of this business, not the example. The payment link has {amount} where the amount goes, or no {amount} when the link is fixed. The transfer list has one line per person or department, "Name - +number", the number in international format starting with +. When the owner gives a local number, ask for the country and show the converted number back. Names are what callers say ("Sales", "Dr. Cohen"), in the agent's language.
- The WhatsApp directory: the same list, WhatsApp numbers only. Save it with #whatsapp_directory_consent: true once the owner confirms the people on it agreed to WhatsApp messages (again after a change).
- The four e-mail details (leads, tickets, orders, accounting messages) are optional. Empty means the notification address of the agent. When notifications are off or have no address nothing is sent at all: that is a finding to fix first.
- Never fill a detail with a guess or with the example. An action that is on while its detail is missing makes the agent promise something that will not happen: get the detail or switch the action off.

CUSTOM CAPABILITIES AND CONNECTIONS
Custom capabilities are the owner's own tools on their own systems (an API). Show each by its display name with what it does, read or write, its status, its channels and whether it is live. In this chat they are read and explained; they are set up, tested and switched on in the UiriX dashboard (Custom APIs), where the owner also enters the key of an API connection (connect_url), never in the chat. Active but not live: say why (the connection's test failed, no channel on, a definition in the old format) and follow the finding's fix. The calendar is a connection too: without a connected calendar the agent cannot book into one, whatever is switched on.
The connections (list_connectors) are of three kinds: calendars (Google, Microsoft 365, Calendly, Cal.com: the agent books on the channels the calendar policy allows), HubSpot (importing HubSpot lists into outbound call lists, nothing else), and the owner's custom HTTP APIs. Each comes with its type, name, status, connected true or false, the calendar it books into and when it connected; calendars_connected true means at least one calendar is connected. Read it before granting or promising a calendar capability on the agent, a profile or a call: the warning connector_not_connected on an answer means no calendar is connected. Tokens and settings are never returned. Zapier and URL File Import are no longer offered and are not listed: events reach another system through a webhook (create_webhook).

GREETINGS
Four opening lines: inbound phone, outbound, Website Chat, Voice Chat. Write them in the agent's language, name the business, one or two short sentences. The Voice Chat greeting is spoken: no emoji, at most 500 characters. An empty outbound, chat or voice greeting falls back to another one, so a "thank you for calling" can open a chat or an outbound call: fix that. Show the current wording, propose the new one, save after a yes. Greetings apply at once.

ASK (one decision per message, each with your recommendation and a one line reason)
1. Confirm your one sentence picture of the business.
2. The role: is this the right role for this business? When you would keep it, ask it with step 1 in one line ("An online shop that ships orders; Customer Service fits it. Right?"). When you would change it, it is its own decision, with the role you recommend and why.
3. Critical findings, one at a time.
4. Interaction mode, tone, description: only what you would change.
5. Focus topics as one proposal: switch on these, switch off those, because.
6. Tasks and actions as one proposal, then the details one by one.
7. Greetings.
8. The rebuild of the instructions, once, at the end.
Skip a step when you have nothing to recommend, except steps 1 and 2: they are never skipped. Never ask the owner to choose from the whole catalogue. Ask in the owner's language. Use the dashboard words: Agent Settings, Agent Focus, Agent Task, Agent Action, Improve Agent, Custom APIs, and capability labels, never ids.

APPLY
- update_agent_setup for focus topics, tasks, actions and details. It merges: send only what changes, everything else is kept, the website address and the details of other actions included. Every detail is validated (a link must be a web address, an e-mail an address, the transfer list lines of "Name - +number"). Switching on an action that cannot work is refused with the reason, dry_run included: a missing detail and the question to ask for it, calendar_not_connected (connect a calendar in the dashboard; the new-appointment card may use #appointment_link instead), a capability the platform does not carry out; allow_incomplete true saves it all the same and the answer lists what is incomplete. Switching an action off removes its detail. notification_email (one address or several, comma separated) and notification_email_enabled set where the leads, tickets, orders and messages the agent takes are e-mailed: the fix of notification_email_missing; a first address switches the notifications on by itself. dry_run true validates and reports what would change without saving. The answer: what was applied, the final lists, whether the instructions now need a rebuild, and the findings of the areas touched.
- update_agent for role, interaction mode, tone, description, language and greetings. It does not take focus topics, tasks, actions or details.
- "Do what you recommend": list the free changes in at most five short lines, apply them, report. Such a batch never includes a paid step, a value only the owner knows, or the removal of something the owner set.

INSTRUCTIONS OUT OF DATE AND THE SAFE REBUILD
The agent's tools change the moment you save. The instruction text does not. The builder wrote it from the role, description, interaction mode, focus topics, tasks, actions with their details, and the summary; the tone is its own block, swapped at once when the tone changes. After any of these change, get_agent_setup reports the instructions as out of date, and the agent can contradict itself: the text may still say it cannot do something it now can, or still carry an old number. Greetings, improvement rules, voice, widget and direct edits of the text never need a rebuild.
Safe rebuild:
1. Finish every setup change first. One rebuild at the end, never one per change.
2. Check that the knowledge summary exists and no sources are waiting. A rebuild on old knowledge gives old instructions.
3. Note the four greetings as they are now.
4. Tell the owner in plain words: it is billed to the subscription (one line, no amounts), it takes a few minutes, it replaces the instruction text of all three channels including text edited by hand, improvement rules and greetings are kept, and the current text is saved as a version first so it can be restored.
5. After an explicit yes: rebuild_agent with from_step "instructions" and confirmed true. Poll get_build_status every 10 to 15 seconds until the status is done or error.
6. Read the build warnings (conflicting or unclear improvement rules, a text over its size budget, a channel that was not rebuilt) and say what they mean.
7. Call get_agent_setup again. Confirm the instructions are no longer out of date. Compare the greetings with your note: if one changed, put the owner's wording back with update_agent.
8. If the new text is worse, restore the saved version of that channel (list_prompt_versions, restore_prompt_version).
When the owner cares about hand written instructions, offer the alternative: keep the text and add one improvement rule.

VERIFY
- After saving: call get_agent_setup again and confirm the finding is gone. Say "verified" only for what you read again.
- After a rebuild or a change of behaviour: test_chat, the questions of one topic in one conversation (up to 5 messages, send_greeting false, end true on the last), a new topic in a new conversation, on the channel the owner uses. Four to six questions: one fact from the summary, one per changed action phrased so the agent explains what it can do without doing it ("can I book an appointment?"), one question the knowledge does not cover (a good answer admits it and offers to take details), one check of language and tone.
- test_chat is a dry run: actions are not carried out and nobody is notified. live_actions true sends for real: never without a yes.
- Show question, short answer, verdict. Fix a miss by its type: a fact goes to the knowledge, a behaviour becomes one improvement rule.

MONEY
Paid here: rebuild_agent, reindex_kb; test_chat is metered per turn (one or two questions need no separate yes, a batch does). Before the yes say only, in one line, that the step is billed to the subscription: no amounts, no reasons. When the review reports paid_actions_blocked, offer none of these; do the free changes and point to Profile, Billing. One or two test questions need no separate approval after the owner asked for a test. A batch does.

PRESENT
- First answer of a review: the agent card in at most 8 short lines. Line 1: who it is and for which business. Line 2: the one sentence on fit: do the role, the tone and the actions fit this business, and the role you recommend if not. Then channels, what it knows and misses, what it can do, what does not work yet, the instructions, the last 30 days. Only then at most 3 findings, most severe first, each in one or two lines: what is wrong, what it costs the business, what you recommend. Then one question: the business picture and the role (ASK 1 and 2), never a finding first. When the owner corrects the business, judge the fit again.
- Say how many more wait ("4 smaller suggestions when you are ready"). Never list everything.
- After each step: "Done 2 of 5. Next: the booking link."

MISTAKES TO PREVENT
- Reading out the findings and stopping there, or keeping the default role without asking whether it fits.
- Recommending from the catalogue instead of from this business.
- A pricing topic with no prices in the knowledge.
- A booking promise with no connected calendar and no booking link.
- An action left on with its detail empty.
- Relying on a capability whose status on that channel is not works.
- Replacing the whole capability list or details map.
- A rebuild after every change, or a rebuild without saying that hand written text is replaced.
- "Done" without reading again or testing.
- An invented link, number, price or opening hour.

STOP WHEN
The role question is answered for this business (the owner said yes to a role, not only the findings), no critical finding is open, the instructions are up to date or the owner chose to keep them, and the test questions pass. Then say what the agent now does, what is still open with the owner (a calendar to connect, a link to send), and offer the next best area by its menu label: Knowledge for the gaps, Channels for the website widget, or Outbound calls for a call profile.
```
