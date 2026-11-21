# Calendars: confirmation calls and booked meetings

Topic `calendar` · version 2026-10-03 · served by `uirix_guide({ "topic": "calendar" })`.

The owner's calendar in this chat: a meeting the agent agreed in a conversation written as an event, and the agent's booking policy. Confirmation calls for a day of appointments are a campaign, set up in the UiriX dashboard. Also why the agent's own calendar connector is a different thing.

```
GUIDE calendar: confirmation calls and booked meetings

GOAL
No meeting lost between a conversation and the calendar: a meeting the agent agreed with a customer exists in the owner's calendar.

FACTS THAT MISLEAD
- Two calendars are in play. The agent's own calendar connector (list_connectors, "Custom Capabilities and connections" in the agent setup) lets the agent book DURING a call or a chat; it is set up in the dashboard, not here. The calendar connected to this chat is the owner's, and only you can read or write it.
- A meeting the agent booked through its connector is already in that calendar. A meeting the agent only AGREED on (a callback day, "Monday at ten") is an outcome or a key detail in the conversation, and in no calendar until someone writes it.
- Confirmation calls for a day of appointments are a campaign: it is set up and started in the UiriX dashboard, or from Claude, not in this chat.
- A cancelled or moved appointment is a result to write back and, when the owner has such a field, a change of the event. Never move the event yourself without the owner's rule for it.
- The agent's own bookings follow the owner's calendar policy (get_calendar_policy / set_calendar_policy, 24 Oct 2026): on which channels it may book (the website chat is off by default), the days and hours, the appointment length and the gap, where meetings take place (at the business, by phone, Zoom, Google Meet, Teams) and which calendar it books in when several are connected. Read it before promising the owner "the agent books Fridays" or "on the website"; change it only on a yes, as the whole policy. Google Calendar, Microsoft 365, Calendly and Cal.com are the four calendars; a visitor's cancel or move on the website is verified by a code to the booking's mobile number.

READ FIRST
- Whether a calendar is available in this chat and whether it can read events and write them.
- For a meeting the agent agreed: list_outcomes type meeting and callback, and get_conversation for the exact words.
- For the agent's own booking tool: get_agent_setup, the calendar capability and its surfaces, and list_connectors.

ASK
1. For a meeting the agent agreed: which calendar, and what the event carries (title, description).
2. For the agent's own bookings: which part of the policy the owner wants to see or change.

APPLY: confirmation calls for tomorrow
Calling a day of appointments is a campaign: say in one line that it is set up in the UiriX dashboard, or from Claude. One appointment the owner names is a single call (single_call playbook), with an explicit yes first.

APPLY: a meeting the agent agreed, into the calendar
1. list_outcomes type meeting or callback, open_only. The outcome carries the contact, the details (date, time, subject) and the conversation. Read get_conversation when the time is not explicit.
2. Create the event in the owner's calendar: title with the customer name and the subject, the time, the phone number in the description, the conversation link. A time not stated in the conversation is a question for the owner, never a guess.
3. mark_synced on the outcome: destination "calendar", external_id = the event id.
4. Tell the owner what was created and what needs a time.

VERIFY
- The events exist in the calendar for the owner's eyes; the outcomes are marked (the not_synced_to reads come back empty).

MONEY
Nothing named here is paid; a single call is (single_call playbook). Free: list_outcomes, get_conversation, mark_synced, list_connectors, get_agent_setup, uirix_guide.

MISTAKES TO PREVENT
- Treating the agent's connector and the owner's calendar as one thing.
- Writing an event for a meeting whose time was never said.
- Moving or cancelling events on the strength of a call summary without the owner's rule.

STOP WHEN
Every agreed meeting with a known time is in the calendar, the owner has the ones that need a time, and knows where confirmation calls for a day are set up.
```
