# Privacy and call compliance

Topic `privacy` · version 2026-10-25 · served by `uirix_guide({ "topic": "privacy" })`.

The account's privacy and call-compliance settings: what the platform's rules say the countries it calls ask for (AI disclosure, recording notice, opt-outs, do-not-call registries), what is worth it, how to explain each, and how to change one: weakening or deleting only after an explicit yes.

```
GUIDE privacy: privacy and call compliance

GOAL
The account's calls and data follow what the platform's rules say the countries it calls ask for, and the owner knows in plain words what each setting does and why it is on. Required items first, one decision at a time, nothing weakened or deleted without the owner's explicit yes.

FACTS THAT MISLEAD
- "Required" is not legal advice. It means the platform's rules say the law of a country the account calls (or is called from) asks for it, plus the national do-not-call registries (US, IL, GB) for marketing calls. An unlisted country asks for nothing. Never call the account "compliant".
- The advice follows the last 90 days and the calls still waiting. A new country counts once calls to it exist: a draft campaign or a queued call is enough, a plan is not.
- "rules" says it only on the calls whose destination country asks for it; "always" on every call; "off" never.
- The recording starts after the notice sentence. With recording off no notice is needed.
- Key 9 is offered only on the calls the agent places, in the line's announcement: with both announcements off, nobody hears it.
- The owner's own announcement text is for those calls too; incoming calls hear the built-in sentence.
- A deletion period deletes for good: the next nightly cleanup removes the texts, recordings or summaries older than the period. Keep forever is the other choice; 365 days is the platform's default.
- The national registry files (the US National Do Not Call Registry, Israel's "Do Not Call Me", the UK TPS) are loaded by the owner on the dashboard, Profile > Privacy. Nothing here loads them.
- The owner's own consent to be called by UiriX is changed on the dashboard only; it is not part of the advice.

WHEN TO RAISE IT
- Before the account's first outbound calls or campaign, and before calls to a country it has not called.
- A marketing purpose (offers, sales): consent and the national registries come in.
- Recording turned on, or the owner asks about recording.
- The briefing's attention holds an item whose code starts with privacy_, or a new call or campaign answers that required privacy settings are not in place.
- The owner asks about privacy, consent, opt-outs, the do-not-call list, how long data is kept, or GDPR.
Raise it in one line, then read. Never open with a lecture.

READ FIRST
- get_privacy: the settings, the advice (open actions first, required first), the open actions counted, what the account did (countries called and calling in, marketing, messages, block lists loaded) and the latest changes.
- list_dnc only when the owner asks about the do-not-call list itself.
- A setting's exact meaning: the resource uirix://docs/privacy.

WHAT EACH SETTING DOES (say it this simply)
- AI disclosure: before the agent speaks, the line says the caller is an AI assistant.
- Recording notice: the line says the call is recorded, then the recording starts.
- Every party's consent: where all parties must agree to a recording (some US states, some countries), notify_record announces and records, never_record does not record those calls.
- Opt-outs: key 9 during a call the agent places puts the number on the do-not-call list at once; the agent's opt-out tool does the same on "do not call me again"; the transcript check catches an opt-out the agent missed; a STOP reply stops messages.
- Forget me: "forget me" to the agent (its tool forget_me) marks the conversation - no memory of the person next time - and opens a privacy_request in list_outcomes (open) until the owner erases their conversations on the dashboard.
- Do-not-call at dial: the list is checked again right before each dial, so a number added while calls wait is not called. On by default.
- National registries: marketing calls skip the numbers on that country's registry. The file is loaded on the dashboard; the block-list check must be on for it to count; the hold on out-of-date lists stops marketing calls there until a fresh file is loaded.
- Consent: the consent fields keep each person's consent at import (type, how, when); the consent block refuses a marketing call to a contact with no recorded consent; the declared default covers an import without consent of its own, and only what the owner states.
- Deletion periods: texts, recordings and summaries older than the period are deleted for good.
- Masking: e-mails, phone and card numbers are masked in what the API, this connector and webhooks return.
- Abusive callers (on by default): a caller who used a call for sexual content or crime is warned, then blocked; never a rude one, the owner or a hidden number. Off lifts those automatic blocks; the owner's own blocks stay.
- Blocked callers: a blocked number cannot call any agent (a busy line) and no agent calls it, until released. get_privacy's caller_blocks counts them; caller_blocks_limit lists them with their ids. Numbers are always masked.
- Block: block_caller with the number as the owner says it, after their explicit yes (confirmed true). A person on the personal card is refused once with who it is: block only after a second yes (person_confirmed true). The owner's own numbers and a hidden number cannot be blocked.
- Release: release_blocked_caller with the id, after the owner's yes; an abusive caller then starts over with a warning.

RECOMMEND
- At most 3 items, the required ones first, each in one plain sentence with the country and what it means for the calls: "Your calls to the US must say it is an AI; that is off now."
- Recommend the suggested value with its reason. "rules" is usually enough; "always" when the owner wants one behaviour everywhere.
- Count the rest ("2 more worth a look") and offer them once the required ones are settled.
- Quote a basis line only when the owner asks why, and say it is the platform's rules, not legal advice.

ASK
One decision per message, your recommended answer and the reason last. For a deletion period ask how long, recommend the platform's default, and say that older data is deleted for good at the next nightly cleanup.

APPLY
- update_privacy with only the settings that change.
- Strengthening a protection (a check, an announcement or an opt-out turned on, a stricter value): the owner's specific request, or their yes to your recommendation, is enough.
- Weakening a protection (turned off or down, never_record to notify_record) or deleting data (a deletion period switched on or shortened): say first what it weakens or deletes, get an explicit yes, then send confirmed true. Without it the tool answers confirmation_required with what it weakens and deletes and saves nothing: explain those and ask.
- A national registry file: send the owner to Profile > Privacy on the dashboard, then read again.

VERIFY
The answer of update_privacy is read back after the save: check that changed holds exactly what the owner agreed to, then name the required actions still open (none: the required settings are in place). After a step on the dashboard, get_privacy again.

MONEY
Free: get_privacy, update_privacy, block_caller, release_blocked_caller, list_dnc. Nothing here places a call or spends money.

PRESENT
About 8 lines. No field names, codes or JSON. Countries by name. Every change you report says what it does for the calls.

MISTAKES TO PREVENT
- Calling the account compliant, or a setting required beyond what the advice says.
- confirmed true sent before the owner said yes to what it weakens or deletes.
- A deletion period presented as a tidy-up: it deletes for good.
- Offering to load a registry file, or to change the owner's own consent to calls from UiriX, here.
- Ten findings at once, or the basis lines read out unasked.
- Key 9 turned on while both announcements are off.

STOP WHEN
Every required item is in place or the owner decided about it, the owner knows what is left for the dashboard, and every change was read back.
```
