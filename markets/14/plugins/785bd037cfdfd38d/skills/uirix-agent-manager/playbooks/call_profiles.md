# Call profiles: the script of a campaign

Topic `call_profiles` · version 2026-10-16 · served by `uirix_guide({ "topic": "call_profiles" })`.

The stored call profile a campaign or an API call runs under: its parts (script, opening line, voicemail line, tool gating, the details each tool sends, tone), how to read its findings, how to build it with the owner one decision at a time, the paid build, and the test call that proves it.

```
GUIDE call_profiles: the script of a campaign

GOAL
A profile that makes the agent say the right thing on an outbound call: who is calling and why, what to do with a person, a receptionist, a menu and a voicemail, which tools it may use and with which links and numbers, in the right tone. Checked by the server's findings, heard once on a test call, and only then used by a campaign.

FACTS THAT MISLEAD
- The profile's script REPLACES the agent's persona on the call; it does not add to it. A short or empty script lets the agent fall back to "how can I help you?".
- The opening line (greeting_message) is what the person hears first. Without it the agent opens with its inbound greeting ("you have reached ..."), which is wrong on an outbound call.
- The voicemail message is read from the first line of the script, after VOICEMAIL_MESSAGE:. Nowhere else.
- Gating: allowed_capabilities lists exactly the tools the call may use; an empty list is talk only; not set means every outbound tool of the profile's category (its own group plus communication) except send_sms, send_whatsapp, notify_department_whatsapp, send_email, schedule_callback and transfer_call (those always need an explicit grant). Always set it.
- Links go by WhatsApp when send_whatsapp is on (the agent's or the profile's grant), else by SMS when send_sms is, else they are handed to send_email; with none of the three a link tool is not offered. WhatsApp is not billed, SMS is billed per segment.
- A tool that sends something needs its detail in completions, keyed by the catalogue's required_field id (a payment link, a meeting link, a pricing page); transfer_call needs #transfer_number or #extension_list; notify_department_whatsapp uses the agent's own #whatsapp_directory (set on the agent with update_agent_setup and the owner's consent, never in a profile). A calendar tool needs a calendar connected on the agent (list_connectors), not on the profile.
- The findings on get_profile are deterministic: script_missing, greeting_missing, voicemail_message_missing, capability_detail_missing, transfer_number_missing or invalid, connector_not_connected, gating_unbounded, capability_unknown or inactive, profile_inactive, category_retired. A critical finding means a call fails at that point. next_step is the first to fix.
- build_profile (paid) writes the script and the opening line from the inputs (category, label, description, focuses, capabilities, completions, tone, behaviour, refinement rules, the knowledge). It OVERWRITES the current script. Set the inputs first, build once, then adjust by hand with update_profile.
- One agent can hold several profiles (collections, sales, events, confirmations). A campaign takes one stored active profile of its own agent; a one-off call may take an inline profile instead (single_call playbook).

READ FIRST
- list_profiles(agent_id): what exists, active or not.
- get_profile(profile_id): the whole profile with its findings and next_step.
- list_capabilities(catalogue outbound): the tools of the category, each with the detail it needs.
- list_connectors(agent_id) when a calendar tool is wanted: calendars_connected true, or the calendar tool cannot book and the profile or call answer warns connector_not_connected. get_agent_setup for the agent's language, voice and business facts.

RECOMMEND
Settle the profile in this order, one decision at a time, each with your recommendation and the reason: the category and the goal (focuses); the tools, from the catalogue, only those the goal needs; for each tool its detail (ask, never invent a link or a number); the opening line in the call language; the voicemail message; the tone; then build.

ASK
Only what the findings and the goal leave open: the goal in one sentence, a link or a number per tool, who the agent is calling on behalf of, the language. Never ask for what get_agent_setup or the profile already holds.

APPLY: a new profile
1. create_profile with category, label, description (who the calls are for), focuses, allowed_capabilities set explicitly, completions for every tool that needs one, tone. Read the answer's findings.
2. Fix every critical finding before the build (update_profile with the missing detail, or drop the tool).
3. build_profile after the owner's yes to the cost; poll with status_only until done; get_profile to read the script and the opening line.
4. Read the script as the person on the phone would: does it say who calls and why, does it handle a receptionist, a menu and a voicemail (VOICEMAIL_MESSAGE: first line), does it say goodbye before ending? Adjust with update_profile (system_instruction_template, greeting_message).
5. Prove it: a test call to the owner's own phone (single_call playbook: create_call with the profile_id, after the yes), then get_call and get_conversation. What the owner heard decides.

APPLY: an existing profile before a campaign
1. get_profile: findings first. Criticals are fixed before anything else; warnings are the owner's call, with your recommendation.
2. The tools against the campaign's goal: a tool the campaign does not need comes off the list; a tool it needs comes on with its detail.
3. The opening line against the campaign: it names the right business and the right reason.
4. When the script changed substantially: build again (paid) or edit by hand; then the test call.

VERIFY
- get_profile shows no critical finding and next_step is not critical.
- The test call's transcript (get_conversation) shows the opening line, the handling the owner wanted and a goodbye.

MONEY
Paid, explicit yes first: build_profile (model builds), create_call (a real call, the test call included). Free: list_profiles, get_profile, create_profile, update_profile, list_capabilities, list_connectors, get_agent_setup, get_call, get_conversation, uirix_guide.

MISTAKES TO PREVENT
- A campaign on a profile with a critical finding.
- A link or a transfer number written from memory or from a placeholder.
- allowed_capabilities left unset ("the agent will decide").
- Building twice when the inputs did not change.
- Skipping the test call because the script reads well.
- Two profiles with the same label on one agent.

STOP WHEN
The profile has no critical finding, the owner heard it on a test call and approved it, and the campaign or the call that needed it can take it.
```
