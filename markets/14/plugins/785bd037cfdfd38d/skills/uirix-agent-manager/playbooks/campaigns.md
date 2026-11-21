# Call a list of people (campaign)

Topic `campaigns` · version 2026-10-16 · served by `uirix_guide({ "topic": "campaigns" })`.

Calling a list or a spreadsheet of people (a campaign) is set up and run in the UiriX dashboard, or from Claude, not in this chat. What can be done here instead: one call to one person, and reading what the calls said.

```
GUIDE campaigns: call a list of people

GOAL
The owner knows where a list of people is called and gets what can be done here. A campaign (a list or a spreadsheet of people called inside chosen days and local hours, at a set pace, with a report) is set up, started, paused and stopped in the UiriX dashboard, or from Claude. In this chat you place one call at a time and read what calls said.

FACTS THAT MISLEAD
- No tool in this chat imports a list, creates a campaign, starts, pauses or stops one, or reads its report.
- A list of people is never called with a loop of single calls: one person, or a handful the owner names one by one, is the limit here (single_call playbook).
- A campaign's calls are conversations of the agent: once they ended they are read here like any other conversation.

READ FIRST
- get_agent_setup(agent_id): whether the agent owns a phone number. Without one there are no outbound calls, and a number is bought in the dashboard.

ASK
What the owner wants: to call a list (the dashboard), to call one person now (single_call), or to know what the calls said (the conversations).

APPLY
- A list of people: say in one line that calling a list is set up in the UiriX dashboard, or from Claude, and offer what can be done here.
- One person: create_call after the person, the number, the goal and an explicit yes (single_call playbook). For the owner's own errand on a personal agent: call_for_me (personal_agent playbook).
- What the calls said: list_conversations for the agent and the period, then get_conversation for one transcript. Summarise the outcomes; never paste phone numbers unless asked.
- Before a campaign in the dashboard, the best preparation here is one test call to the owner's own phone with the script the campaign will use (single_call and call_profiles playbooks).

MONEY
Paid: create_call and call_for_me, each a real call billed to the subscription: an explicit yes first. Free: get_agent_setup, list_conversations, get_conversation.

STOP WHEN
The owner knows where the list is called, and the one call or the reading they asked for here is done.
```
