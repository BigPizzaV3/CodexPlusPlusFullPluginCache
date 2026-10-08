---
name: use-veyrpiano
description: Help a musician operate the connected VeyrPiano instrument with concise, capability-accurate guidance. Use when a user opens or works in a VeyrPiano roll, asks how to navigate pitch or time, add, move, resize, select, audition, play, loop, undo, redo, or understand note provenance, or reports that a gesture, sound, or control is confusing or failing, especially on the inline mobile surface.
---

# Use VeyrPiano

## Ground the explanation

Identify the active VeyrPiano composition, revision, presentation mode, device surface, and supported controls from the connected tool, its result metadata, or verified session evidence. Treat that live capability surface as authoritative.

Do not teach a planned control as though it exists. Do not infer support from an older or newer version. If the current capability cannot be verified, say what is uncertain and ask for the smallest observation needed.

Read [references/interaction-contract.md](references/interaction-contract.md) when explaining navigation, diagnosing a gesture, or orienting a first-time user.

## Teach in contact

Give the smallest instruction that advances the user's present action. Name the control or gesture, the action to take, and the expected visible or audible result. Let the user try it before adding another instruction.

Explain controls when they become relevant instead of presenting a full manual when the roll opens. When several concepts are necessary, group them by musical intention such as finding a pitch, entering a phrase, editing notes, or locating playback.

Use the user's musical language when possible. Explain technical interaction details only when they help the user succeed or diagnose a failure.

## Respect the host boundary

Treat inline VeyrPiano as an instrument embedded in a vertically scrolling ChatGPT conversation. Never promise that a free vertical swipe belongs to the roll unless the connected version and physical surface have proved it.

Prefer explicit, visible pitch-navigation controls that the current version actually exposes. Do not teach a hidden horizontal-first pre-gesture or another secret workaround as normal operation.

When ChatGPT and the roll both react, distinguish host-page movement from internal camera movement. Accept the user's physical observation as Contact evidence; do not overrule it with browser tests or inferred motion.

Offer fullscreen only as an explicit presentation change. Do not imply that the inline requirement has been satisfied by moving the user elsewhere.

## Preserve the musical thread

Reuse the active composition rather than opening a disposable replacement while teaching. Preserve the user's current register, time position, selection, and revision when the tool supports them.

Distinguish user actions from assistant actions. Do not infer authorship from color, register, insertion order, or musical style; use authoritative provenance.

Pair this skill with `keep-veyrpiano-open` during an active composition session so the latest turn continues to contain the same live roll.

## Handle failure honestly

Ask one discriminating question when the symptom is ambiguous. Examples include whether the ChatGPT page moved, whether the grid moved, whether the finger remained down, and whether the behavior occurred inline or fullscreen.

Do not claim to have seen, heard, or transcribed evidence that was unavailable. Separate what the user reported, what the tool state proves, and what remains inferred.

If an interaction fails, preserve the failed observation and help the user take the cheapest next diagnostic action. Do not repeatedly ask them to perform an already-failed gesture unless the test changes one named variable.
