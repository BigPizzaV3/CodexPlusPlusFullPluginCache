---
name: build-audio-plugin
description: Build a small audio-plugin scaffold, turn an effect idea into a concrete implementation brief, or check build and release evidence. Use Dispro for audio-plugin development and bounded verification, not unrelated media editing.
---

# Dispro

This release candidate is free to use under the proprietary toolkit LICENSE. Users may modify, distribute and sell generated audio plugins under OUTPUT-LICENSE.txt, including the supplied template material. That permission does not cover modifying or redistributing the reusable toolkit or branding. Preserve upstream notices. Independently authored user work retains its existing rights. Public directory publication remains a separate gate. Support: support@kaizendsp.com.

Help the user move from an audio-effect idea to a small, reviewable artifact.
Start with the smallest useful change and reuse already verified results.
Do not launch extra agents, repeated model calls, CI, paid services, or native
build loops for routine checks. The deterministic scripts need no model API.

## Choose the current deliverable

For a new effect, start with `references/guided-setup.md`: reuse known answers,
ask only the missing sound/control/target choices, state defaults and show one
coherent mockup. Keep the first interaction short. Load the parameter, real-time
or comparison reference only when that part of the work is needed.

For a new plugin or DSP design, produce a concise brief and visual mockup first:
signal path, channel layout, controls/ranges, state/automation behavior, one
target format/OS and observable acceptance checks. Obtain explicit approval of
the mockup before implementing new DSP. Do not interpret approval of a concept
or another product as approval of this mockup. If image/design tools are absent,
provide a clearly labelled wireframe and keep implementation pending approval.
For a headless effect, show a control/signal-flow mockup and seek the same approval.
See `references/engineering-lessons.md#visual-first` for the handoff.

An explicit request to exercise the existing mono LV2 gain example may use its
unchanged recipe directly; this is not a new DSP design. During delivery repairs,
preserve the product's approved sound/UI. Do not expand a repair into a redesign.

For a first working artifact, use the original fixed gain recipe in `scripts/`.
It is a real LV2 bundle with input, output and a linear 0–2 gain control. It has
no custom UI, MIDI or state extension. Model-assisted design and code edits
are a separate phase; v0.1's trusted runner intentionally refuses modified
recipes. A new DSP design can be delivered as clearly unverified source and a
reviewable validation plan, but must not be passed off as a tested recipe.

## Check execution access truthfully

On ChatGPT web/mobile, provide the brief, source/commands when file tools are
available, and a local handoff. An uploaded skill or ZIP does not grant access
to the user's computer. Do not fabricate a local process, ask for credentials,
deploy an execution bridge, or install persistent access. If the current host
offers an authorized sandbox, distinguish that sandbox from the user's machine.

On a local Codex/runtime host, use a new dedicated workspace chosen for this
task. Do not touch another product checkout, installed plugins, DAWs, global
settings, signing keys, or running processes. Use the optional Dispro MCP tools
only if already configured; otherwise the bundled CLI works without installing
anything. Inspect `references/workflow.md` before execution and
`references/release-gates.md` before claiming release readiness.
Use `references/release-checklist.md` to review an existing candidate. Consult
only the applicable entries in `references/engineering-lessons.md`; these are
general lessons, not permission to copy product code or a claim of new support.

For controls/recall, use `references/parameter-state-contract.md`. For a changed
processing path, use `references/realtime-safety.md`. For a sonic change or
regression, use `references/audio-comparisons.md`: declare the control/tolerance
first, bind exact artifacts and preserve failed comparisons and golden references.
For asset staging, platform floors, installers or signing claims, use
`references/platform-release-review.md`. Separate AAX verification from Windows
publisher signing, and confirm current publication state and exact approval scope
before any saved-release or public-submission change.

## Run once, record evidence

The scripts directory is adjacent to this skill. From that directory, run:

```sh
python3 -m dispro --workspace /absolute/dedicated/dispro-work init
python3 -m dispro --workspace /absolute/dedicated/dispro-work scaffold first-gain
python3 -m dispro --workspace /absolute/dedicated/dispro-work run first-gain --timeout 30
```

Substitute an actual approved output directory. Never use a user's home,
repository root, or another owner's workspace as the output directory.
`init` refuses nonempty unmarked directories; `scaffold` refuses overwrite.
Use project slugs, never shell fragments. The CLI needs Python 3.10+ and, for
native compilation, macOS/Linux with `/usr/bin/cc`. Windows native build is
unsupported. Ctrl-C cancels the owned child process group. MCP jobs use
`cancel_job`; `job_status` reads status without rerunning.

If the run fails, read its receipt first. Make one focused correction only when
evidence justifies it. Do not automatically retry builds or change system tools.
Report stage statuses verbatim: passed, failed or unrun, plus cancelled/timed
out outcomes. Receipts are local process evidence, not signed attestations.
Separate historical evidence, source inspection, mock/syntax fixtures and exact
native-host acceptance. Bind each claim to its artifact, dependency identities,
format, OS, architecture and named host. Preserve failed evidence and unresolved
gates; a successful adjacent test cannot replace them. Do not rerun unchanged
work solely to accumulate passes.

## Handoff

Return the scaffold and exact archive location/hash, host/architecture, passed
checks, and the next unrun release gate. Offline contract validation is distinct
from DAW discovery, live audio, automation, session recall, signing, notarization
and publication. Explain SDK/licensing requirements before suggesting another
format. Never copy proprietary DSP, branding, credentials, customer data or
licence headers from unrelated products into a deliverable.
