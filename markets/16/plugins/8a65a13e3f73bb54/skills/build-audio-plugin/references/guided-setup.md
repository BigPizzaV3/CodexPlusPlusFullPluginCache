# From an idea to an approved brief

Use this route for a new effect. Keep the interaction short and explain choices
in ordinary audio language. Reuse answers already given; do not restart intake.

## Start with the missing essentials

Ask at most three short questions together, and only when the answers matter:

1. What should happen to the sound, and what should remain recognizable?
2. Which controls must the first version expose?
3. Where will it run: named host, operating system and plugin format?

Offer concrete choices when the user is unsure. State assumptions in the brief
so they can correct them. Avoid a catalogue of every framework or DSP technique.
Describe an unfamiliar choice by its effect on sound, latency or usability.

For an explicit request to try Dispro, the available default is the unchanged
mono LV2 gain example: one input/output and a linear gain control from 0 to 2,
default 1, without a custom UI or state extension. It has no smoothing and can
click under abrupt gain changes. A new effect is a separate design: do not make
it look validated by running the gain example. Target-format support and SDK
rights must be established before promising a native build.

For new designs, prefer a small control set and one named target for the first
version. Leave optional browser UI, accounts, analytics and commercial licensing
out unless requested. Signal order, gain staging, smoothing and latency are
design decisions with explicit reasons, not universal defaults.

## Show one coherent first proposal

Present a visual mockup alongside this brief. If graphical tools are unavailable,
use a clearly labelled wireframe or control/signal-flow diagram. Each important
control needs a readable label, purpose and visible value; icons are supplementary.
Make the current step, available action and next step obvious.

| Field | Record for this proposal |
|---|---|
| Working name and audible goal | One sentence; distinguish reference inspiration from copied behavior |
| Audio path | Channels, stage order, dry/wet behavior and latency budget |
| Controls | Essential controls, units, ranges and defaults; link the parameter contract |
| State | What a saved session must reproduce; identify deliberate exclusions |
| Target | One format, OS/architecture and named host; mark support not yet demonstrated |
| Mockup | File/revision and which states are shown, including resizing if relevant |
| Acceptance | Small observable checks for sound, state and controls; initially unrun |
| Approval | Exact approved revision and scope, or pending; never invent approval |

Obtain approval of this mockup before new DSP implementation. Existing approval
continues to apply to the same scope; do not repeatedly ask about routine steps.
If the user changes the design materially, show the change before relying on the
old approval. Delivery-only repairs preserve approved sound and UI.

## Hand off one small implementation slice

After approval, agree the first observable behavior and its acceptance check.
Keep processor/DSP, parameter/state, UI and release metadata responsibilities
clear; do not copy a product's implementation to fill a template. Use existing
authorized local tooling, and report unavailable execution access honestly.

Choose only the next needed reference: `parameter-state-contract.md` for
controls/recall, `realtime-safety.md` for processing ownership, or
`audio-comparisons.md` for a sound change. Keep the entry prompt short instead
of loading every effect family, signing manual or historic investigation.

The handoff should name the approved brief, changed source, exact evidence and
one next open gate. A scoped source draft is useful even when native execution
is unavailable, provided it is labelled unbuilt/unverified.
