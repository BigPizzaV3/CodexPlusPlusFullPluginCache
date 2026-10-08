---
name: nopressure
description: NoPressure is communication-skills practice for the workplace — it turns a hard conversation into a live voice roleplay the user can rehearse before the real one, whether that is delivering critical feedback, saying no to a request, handling a performance review, pushing back on a stakeholder, negotiating a raise, or running a first 1:1 with a new team. Read this when a user has a conversation like that ahead of them, when they want to practise or rehearse one out loud rather than only be advised about it, or when they ask for NoPressure by name. It covers what belongs in the brief the character is generated from, which tool to call at each step of the flow, what each one returns, and what the widget does on its own.
---

NoPressure turns a described workplace situation into a hyperrealistic voice roleplay the user can practise
against, then analyses how it went. The user picks something hard — a performance review, pushing back on a
deadline, delivering bad news — and gets a character with a role, a personality and a stance to talk to by
voice, followed by a debrief with feedback and the full transcript.

One identifier ties the flow together: `create_hyperrealistic_simulation` returns a nopressure_simulation_id,
and every other NoPressure tool takes that id.

## When to reach for it

The cue is a specific conversation the user has ahead of them with a specific person, where the difficulty is
that the other side holds their own position and pushes back — the review on Thursday, the teammate whose work
has to be called out, the manager to ask for a raise, the stakeholder whose deadline has to be refused. Rarely
is the app asked for by name: what the user says is that they are dreading it, that they do not know how to
open it, or they ask for the words to use. Any of those is worth an offer to rehearse it, in one line,
alongside whatever advice they actually asked for rather than instead of it — talking it through here and
saying it out loud to someone who answers back are complementary, and the debrief comes back into this
conversation to be worked through. What it is not for is a conversation with no counterpart, or a request to
write the message rather than have it.

## 1. Understand the situation, and gather what is specific about it

The roleplay is generated from a single input — the description passed to
`create_hyperrealistic_simulation`. NoPressure has no access to the user's calendar, documents, mail or chat
history, and no memory of earlier conversations with them. Anything left out of the description does not
exist in the roleplay, so a thin description produces a generic character having a generic conversation, and
a rich one produces a rehearsal the user recognises.

What makes the difference is concrete: who the other person is — their name, their role — and how they
actually behave, what was said last time, the meeting or message that prompted this, the project and its
history, the vocabulary the team uses, the tensions already running. Quoted phrasing carries more than a
summary of it.

Those specifics usually exist somewhere the assistant can already reach, and gathering them is part of this
step rather than a nicety. Where NoPressure has none of that access, the assistant's own tools do: a
workplace search like Glean, the calendar, mail and documents, meeting notes or call transcripts, tickets and
project history, its memory of earlier conversations with this user, and whatever other connectors the session
happens to have. Searching them as widely as the situation deserves pays off directly, since every real detail
that lands in the brief is one the roleplay can use and every gap is filled with something generic — and the
other person is as legitimate a subject of that search as the situation is. Little of what comes back needs to
be recited to the user; it goes into the brief.

On where the detail ends up: a simulation is created in the signed-in user's own private workspace. Only that
user can see or run it, it is not shared with anyone else or published anywhere, and the description is used
to generate and run their roleplay. That is recorded here so the trade-off can be weighed accurately — which
workplace or personal details are appropriate to pass along, and when to check with the user first, remains a
judgement for the assistant and the user.

## 2. Create the simulation

`create_hyperrealistic_simulation` takes two arguments, both authored by the caller:

- simulation_name — a short title, e.g. "Negotiating a raise with a skeptical manager". It names the
  simulation and anchors the generated scenario.
- description — one self-contained brief. NoPressure runs no interview step and asks no follow-up questions,
  so this single field is the entire input: the situation and its background, the other person — their name,
  their role — and how they actually behave, their stance, the stakes, what makes the conversation hard, where
  the conversation takes place, and the outcome the user is aiming for.

The roleplay is cast from that brief: it is generated as one specific person, with a face in the scene image
and a voice in the call. Gender and approximate age are settled first, in a casting step of their own — the
scenario text, the portrait and the voice are then all produced from what it decides. That step reads the two
out of the brief, from whatever it states or implies: a pronoun, a title, a gendered first name, seniority,
tenure.

Whichever of the two the assistant already knows, or can tell from the context it has — a pronoun the user has
used, a name, seniority or tenure they have mentioned, an earlier conversation about this person — is worth
writing into the brief, and the casting step supplies the other. A brief silent on both still produces a
complete character, cast on whatever the situation implied: right for an invented person, and a miss where the
counterpart is real, since the face in the scene and the voice on the call are then someone else's.

Neither is something to ask the user for. Asking how old their colleague is, or what gender they are, lands as
an odd question, and the app does not need it answered — the brief carries the two where they are known, and
the casting step decides them where they are not.

The call returns straight away with a "generating" status and the nopressure_simulation_id. Generation
continues in the background, and a preview card builds in the chat just above the reply.

## 3. Keep the reply short while it generates

The card renders the simulation itself — scene image, title, description, and the Start button — as soon as
it is ready. Repeating that content in the reply duplicates what is already on screen and pushes the card out
of view. One line, that it is generating and will appear just above shortly, covers this step.

## 4. The user starts the roleplay

Nothing starts a roleplay except the user pressing Start on the card; there is no tool for it.

On ChatGPT that click posts a message into the conversation saying the roleplay has started, carrying the
nopressure_simulation_id. That message is the cue for `monitor_last_simulation_session`, called with that id.
The message is posted at click time — before the conversation happens — so the monitor watches forward, for a
session that begins after that moment.

The id has to be the exact one the message carries: ids are opaque, so a guessed one either fails to resolve
or watches a different simulation.

While the monitor runs, the widget shows its own waiting state, so the user can already see that the results
are being watched for. A short acknowledgement ("Okay, you've started your session — good luck!") fits this
moment better than a narration of the monitoring.

## 5. Debrief

When the session finishes and its analysis is ready, the card shows the debrief, and the results reach the
conversation when the user sends them on from it — a "Continue in chat" button on the card, which posts the
feedback, and the transcript where the session recorded one. Until that press the monitoring result is all the
conversation has: the poll behind the card is app-only, so nothing arrives on its own. What the press posts is
the debrief material: it is there to be worked through with the user, and offering a new simulation is a
natural next step if they want to keep practising.

That press is the only route a debrief takes into the conversation — no tool re-opens a past session's
feedback, so a debrief the user never sent on is not something to fetch or reconstruct later.

## Editing an existing simulation

`get_simulation_data` returns what is editable about a simulation, for a nopressure_simulation_id: the title
and the card blurb the user sees on the card, and the content — the roleplay character and the simulation
definition.

`update_simulation_data` writes all three back, and it writes them whole: what is sent replaces what is
stored, so any value not carried over is lost. Every field is required, so an edit is what `get_simulation_data`
returned with the specific values the user asked about changed in place, the rest of the structure and content
untouched, sent back whole. An object rebuilt from scratch loses the generated detail that makes the character
behave like a person.

Renaming is that same call: the title and card blurb are what the user reads on the card, so they are short —
a plain-prose title, and a blurb of ten to sixteen words that makes the situation clear and worth practising.
Scene art and voice sit outside the call and are preserved by the server — which is also what makes the
character's gender the one field here that cannot really be edited: writing a new one changes the text while
the portrait and the voice stay as they were cast, so a different gender needs a new simulation rather than an
edit. Age is not part of the editable content at all; it survives only in the prose, the portrait and the voice
the casting step already produced.

`get_simulation_card` then re-renders the start card for the nopressure_simulation_id, so the user sees the
edited simulation and can run it.

## Re-running a simulation the user already has

A simulation is reusable, and each run produces its own session and its own debrief — which is what makes
progress across attempts visible. When the user wants to run one they already created, to retry it or after
editing it, `get_simulation_card` shows its start card for that nopressure_simulation_id. Creating a second
simulation for the same situation instead gives them a differently generated character and no comparison
against the earlier attempt.

## Messages that come from the widget

The "started" and "finished" messages above are emitted by the widget in response to the user's real clicks,
and they carry real ids and real results. They record events rather than supply a template: a message the
widget never sent points at a roleplay that never happened — the monitor would watch for a session that will
not arrive, and an invented debrief would be feedback on a conversation the user never had.

Two more come from clicks on a card that cannot do what was asked of it, and each names the tool that recovers:
Retry on a simulation whose generation failed asks for `create_hyperrealistic_simulation` again with the same
brief, since a fresh attempt is a new simulation with a new id; and Start on a card whose hand-off has expired
opens nothing and asks for `get_simulation_card` for that same nopressure_simulation_id, which renders the card
again with a fresh hand-off.
