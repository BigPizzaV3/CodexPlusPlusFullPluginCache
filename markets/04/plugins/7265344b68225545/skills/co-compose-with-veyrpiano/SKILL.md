---
name: co-compose-with-veyrpiano
description: Take a responsive musical turn in the active VeyrPiano composition while preserving the musician's material, provenance, and authoritative revision. Use when a VeyrPiano session is active and the user says “your go,” “your turn,” “continue,” “add something,” asks for a musical response or variation, or otherwise hands creative agency to the assistant.
---

# Co-compose with VeyrPiano

## Read before answering

Treat the active composition as a shared musical object, not a blank prompt. Resolve its exact `compositionId` from the conversation or recent tool result. Never invent, guess, or substitute an ID.

Call `get_composition` before editing whenever the latest authoritative revision is not already present in the current response. Read the notes, timing, register, density, velocity, tempo, sustain, and `createdBy` provenance. Reason from this symbolic state; do not claim to have heard audio unless audio was actually available.

## Take one musical turn

When the user gives an open cue such as “Your go,” act without asking them to design the contribution for you. Infer a plausible response from the existing material and add one bounded, recognizable idea: a reply, continuation, counterline, harmonic support, rhythmic answer, or intentional contrast.

Let the amount of existing material set the scale. Seed an empty roll with a short motif. Answer sparse material without flooding it. Extend dense material selectively. Prefer a contribution the musician can hear, judge, revise, and answer over a complete arrangement.

Preserve the musician's notes unless they explicitly request transformation or removal. Do not move, resize, recolor, or delete their material merely to make room. Use `edit_composition` for assistant-authored mutations so new notes retain assistant provenance. Use `remove_composition_elements` only when the user clearly asks to remove identified elements.

Make the edit against the exact current `expectedRevision` with a fresh unique `operationId`. Reuse an operation ID only for an identical retry. On `REVISION_CONFLICT`, reread authority, reconsider the contribution against the new state, and retry lawfully with the correct revision.

## Return the instrument

After the mutation succeeds, call `open_piano_roll` with the same exact `compositionId` as the final presentation-producing tool action. Do not create a replacement roll. Put any brief musical explanation before that final call so the newest visible object is the live shared instrument.

If the latest successful tool result already presents the correct composition and revision, do not render it twice.

## Keep authorship honest

Describe the contribution plainly and briefly. Distinguish what the musician made from what the assistant added using authoritative provenance. Do not call a musical choice successful until the musician has encountered it; offer it as a turn in the conversation, not a verdict.
