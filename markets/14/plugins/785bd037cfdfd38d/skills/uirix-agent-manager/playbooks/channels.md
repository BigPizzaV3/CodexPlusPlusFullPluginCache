# Channels: widget, voice, phone number, demo link

Topic `channels` · version 2026-10-26 · served by `uirix_guide({ "topic": "channels" })`.

Where customers reach the agent and how to make each real: the website widget (on, domains, install code, look), the voice it speaks with, the phone number (bought in the dashboard, never here), and the demo page that shows the agent on the owner's own site. What "on" does and does not mean.

```
GUIDE channels: widget, voice, phone number, demo link

GOAL
Customers can actually reach the agent: the widget is on, bound to the business website, installed there and looking right; the voice fits the business and the language; a phone number exists when calls are wanted; and the owner can see and try the agent before any of it is live.

FACTS THAT MISLEAD
- "Widget on" is not "installed". update_widget switches it on; it reaches customers only once the install code is on the website (or the business uses the demo page to see it). Say both every time.
- The widget is bound to its allowed domains: a widget on with no domain either has no usable install code or can be run from any site (the review's finding widget_open_to_any_domain). allowed_domains REPLACES the whole list: send the existing domains plus the new one.
- The public token is what the install code carries; a widget with no token (widget_enabled_without_token) is not reachable, whatever the switch says. The token is minted in the dashboard, not here.
- A voice belongs to a provider: a voice id of the OpenAI catalogue does not work on a Gemini agent. list_voices filtered by the agent's provider is the only safe source; a marketing name ("Chloe") is not an id.
- A phone number is bought by the owner in the dashboard (Agent, Dashboard, Get Number; it needs a saved payment card). Nothing here buys, moves or releases a number. Without a number there are no inbound calls, no outbound calls and no campaigns.
- In the US, Canada, Israel and Puerto Rico a number is active at once. In the United Kingdom, Germany, France, Australia and the other documents countries the telephony provider first reviews the owner's regulatory documents (entity details, address, a proof of address or identity), 1 to 3 business days; the number is bought on approval. The setup's channels.phone.approval carries the open request (status, country, since when, dashboard_url): say the status and give the link; the documents are uploaded in the dashboard only, no tool does it, and never offer to buy a number while a request is open.
- Voice Chat (voice inside the widget) and the phone are different channels with different instructions; "the agent has a voice" says nothing about the phone.
- The demo page needs no login and shows the real widget over a screenshot of the owner's home page. It is a link to send to the owner or to a colleague, not an install.

READ FIRST
- get_agent_setup: channels (phone number, widget on, token, domains), language, provider, the channel findings.
- get_widget: the exact widget state, the saved appearance of the launcher, install_page_url (the dashboard page with the install code and a live preview), demo_url and embed_snippet (the install code, identical to the dashboard's).
- get_voice and list_voices(provider = the agent's) before any voice change.

CHECKS
1. Widget: on, has a token, at least one allowed domain that is the business website, install code present.
2. Voice: the voice id belongs to the agent's provider; the locale fits the agent's language.
3. Phone: a number exists when the owner wants calls; otherwise say what is missing and where it is bought.
4. The demo page works: get_widget answers demo_url while the widget is on.

ASK
- The business website address (for the domain) when none is set.
- Which voice: offer two or three of the provider's catalogue by gender and personality, each with its sample_url (a short English MP3, public, plays in the chat), and let the owner listen and choose. Every voice of every provider has a sample, the gpt_live voices included.
- Whether calls are wanted, before speaking of a phone number.

APPLY
- Widget: get_widget, then update_widget with only the fields that change (enabled, allowed_domains including the existing ones, colour, position). The launcher's look (AI View, icon, size, tooltip) is edited on the install page, not here.
- Installing: send the owner to install_page_url (copy the code there, with a live preview of what is saved) and offer demo_url to see the widget on their site first. Hand over embed_snippet only when the owner asks for the code itself, whole and unchanged: never retype, shorten or "clean up" the snippet, and never write an install code of your own.
- Voice: list_voices for the provider, set_voice with the voice_id and the locale. The sound is heard from sample_url before the change; a test with test_chat on channel "voice" shows the words, not the sound.
- Phone: nothing to apply here. Tell the owner where to buy a number and what it enables; come back to the setup review afterwards (the phone capabilities become live).
- Demo: the demo_url of get_widget (the widget must be on: switching it on is an update_widget the owner says yes to).

VERIFY
- get_widget shows the state asked for; get_agent_setup shows no widget finding.
- get_voice shows the new voice id; the agent's provider did not change.
- The owner opened the demo page and saw the widget.

MONEY
Metered like a chat: test_chat. Free: get_agent_setup, get_widget, update_widget, get_voice, list_voices, set_voice, uirix_guide. A phone number costs money in the dashboard, not here.

MISTAKES TO PREVENT
- Replacing the allowed domains with the new one alone.
- Calling a widget "live" because it is on.
- An install code typed from memory, or a shortened snippet: the loader then runs with its defaults and ignores what the owner saved.
- Setting a voice of another provider, or a marketing name as the id.
- Promising a phone number, or inbound calls, through these tools.
- Changing the agent's language or provider to make a voice fit.

STOP WHEN
Each channel the owner wants is on, bound and installed or installable, the voice is set and fits, and the owner has the demo link.
```
