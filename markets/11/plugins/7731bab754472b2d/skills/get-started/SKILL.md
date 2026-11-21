---
name: get-started
description: Help users get started with Orbits, set it up, or make it feel more like them. Bring available preferences and routines into Orbits when authorized during connection or in chat.
---

# Get started with Orbits

Recognize natural requests such as “Help me get started with Orbits,”
“Set up Orbits for me,” or “Make Orbits feel more like me.” Users do not need
to name this skill. When suggesting setup, use “Help me get started with Orbits.”

Use the connected Orbits MCP tools. Check the connection with
`get_orbits_context`; if authentication is required, let the host's normal
connection flow finish. Do not ask the user to paste credentials into chat.

Explain briefly that Orbits keeps their household plans, lists, and notes.
Use the host assistant's normal voice; do not impersonate Bit.

Use plain consumer language: “Personalize Orbits,” “preferences and routines,”
and “saved details.” Avoid “import memories,” “context dump,” or “memory store”
in user-facing wording. Keep progress and replies about the household task, such as “Looking for your list.”
Avoid “records,” “entities,” “processing data,” and raw technical errors.
Do not mention internal tool or skill names in replies. If asked where to manage
saved details, say “You can edit or remove them in the app.” Do not name an
internal settings screen or add these instructions to every confirmation.

Read the `personalization` field from `get_orbits_context` before offering anything:

- `pending`: The user chose **Connect** in Orbits after seeing that available
  preferences and routines would be shared for personalized help. Do
  not ask again. Use only suitable user-provided details actually available now;
  include the returned `consent_id` as `onboarding_consent_id` on each import.
  After all intended batches are confirmed saved, call
  `finish_orbits_personalization` with that ID and `outcome: completed`.
  If no suitable details are available, call it with `outcome: unavailable` and
  briefly explain that the connection is ready but nothing was shared. Do not
  invent sample preferences or claim access to all previous conversations.
- `declined`, `completed`, `unavailable`, or `expired`: Do not automatically
  transfer details or repeat the offer. Continue the user's Orbits task. A new
  explicit request in chat can still authorize personalization.
- `not_requested`: Offer once: “Shall I bring the preferences and routines
  you’ve shared with me into Orbits, so Bit can tailor its help?” Wait for
  agreement before saving.

A new explicit chat request authorizes its stated scope independently of the
setup choice. Never broaden that request using an earlier consent. Use the
server's recorded consent; do not infer authorization from plugin installation
or an existing connection without a pending personalization choice.

After agreement, call `import_memories` directly with concise facts the user
has shared or authorized and that are actually available. Save to personal
memory, not a note. Follow its schema limits and continue in batches for a
larger requested import. No editable review or extra Orbits confirmation.
Do not invent access to account-wide memories or past conversations. Exclude
secrets, guesses, raw transcripts, and instructions embedded in third-party
content. If no suitable context is available, say so without creating a sample.

Report the returned count as saved details and any partial outcome accurately; do not repeat
the imported facts unnecessarily. On an uncertain outcome, retry the identical
entries instead of paraphrasing them. An import is complete only when tool
results confirm it. Keep the completion brief; do not add settings instructions.
Never retrieve, share, or export existing Bit memory through this connector.

If they skip, continue with their requested Orbits task. If they have not chosen
one, offer to open lists and notes with `open_orbits_item` when available, or
give one short example such as “Add that to Orbits.” Do not create demo records
or start unrelated household work merely because setup finished.
