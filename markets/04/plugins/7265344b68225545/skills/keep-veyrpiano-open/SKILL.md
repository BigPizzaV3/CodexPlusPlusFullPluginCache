---
name: keep-veyrpiano-open
description: Maintain visual and state continuity for an active VeyrPiano session by re-presenting the same live composition at its latest authoritative revision. Use after a VeyrPiano roll has been opened whenever the user continues composing, asks the assistant to inspect, discuss, play, or change the music, says “continue,” “your turn,” “your go,” “open it,” “where is it,” or otherwise expects the instrument to remain available across conversation turns.
---

# Keep VeyrPiano Open

## Hold the active instrument

Treat an opened VeyrPiano roll as the shared workspace for the active musical session, not as a disposable tool result. Keep the same composition visually present in the newest assistant turn while that session remains active.

Maintain these bindings:

- the exact VeyrPiano connector;
- the composition identifier;
- the latest authoritative revision;
- the chosen inline or fullscreen presentation mode;
- camera, selection, playhead, loop, and other view state when the tool supports them.

Do not upgrade versions, switch endpoints, create another composition, or reset view state merely to render the instrument again.

## Re-present after every meaningful turn

Perform reads, mutations, and reasoning first. Before mutation, call `get_composition` when the revision may have changed. After any requested change, call `open_piano_roll` with the same exact `compositionId` as the final presentation-producing tool action. It resolves the latest authoritative revision.

Follow the rendered roll with only the prose needed to orient the user. The instrument is the primary continuation surface; prose supports it.

Re-present the roll after:

- an assistant-authored musical change;
- a state inspection or discussion that continues the composition;
- playback, navigation, selection, loop, tempo, or meter work;
- a short continuation cue such as “your turn,” “go,” or “continue”;
- any report that the roll disappeared or is no longer visible.

Do not issue a duplicate render inside the same response when the latest successful tool result already presents the correct composition and revision.

## Protect authority and provenance

Never use a stale snapshot to overwrite newer user work. If the active revision is uncertain or a mutation reports a conflict, reread authority before rendering or changing anything.

Render calls must be observational: they must not mint a new composition, create notes, advance the musical revision, or change authorship. If the available “open” operation has such side effects, do not use it as a continuity mechanism.

Preserve authoritative note provenance. An assistant mutation must remain assistant-authored; a passive re-render must not restamp either user's notes.

## Recover the surface

When the user asks “Where is it?” or says the piano vanished, re-render the same current roll immediately. Do not direct the user to scroll back to an older card, provide only a composition identifier, or open a blank replacement.

If more than one composition could be active, resolve the ambiguity from recent authoritative tool state. Ask the user only when the correct composition cannot be determined safely.

If the required VeyrPiano connector or rendering tool is unavailable, say that the roll cannot be re-presented in the current turn. Do not claim that it is open.

## Respect the host limitation

Do not claim that the roll is permanently pinned. ChatGPT controls card placement and may move older turns offscreen. This skill provides practical continuity by placing the same live roll in the newest relevant response.

Do not silently move to fullscreen as a substitute for keeping the inline roll visible. Preserve the user's chosen presentation mode unless they request a change.

## End the session deliberately

Stop re-presenting the roll when the user explicitly closes it, selects another composition, requests prose-only discussion, or clearly leaves the piano-roll session. A temporary explanatory exchange about the active music does not end the session.

Use `use-veyrpiano` alongside this skill when the user needs help operating the visible instrument.
