---
name: guide-authoring
description: Turn user-provided goals, notes, or procedures into a concise interactive how-to guide using the display-guide tool. Use when the user explicitly asks for a guide, checklist, structured steps, or guide widget, including requests to reorganize existing instructions. Do not trigger for general advice, explanations, or casual how-to questions that do not request structured guide presentation.
---

# Guide Authoring

Create a grounded, easy-to-follow guide and present it with `display-guide`.

## Workflow

1. Identify the outcome, audience, starting point, and constraints from the request.
2. Ask only for details whose absence would make the procedure unsafe, incorrect, or unusable. Otherwise, keep assumptions minimal and disclose material ones in `notes`.
3. Ground the procedure in the user's supplied information and reliable context. Verify volatile or high-stakes facts with authoritative sources when tools are available; never fill a material gap by guessing.
4. Organize the content into the supported guide fields.
5. Review the complete procedure for safety, order, and completeness.
6. Call `display-guide` once with the finished guide and a concise `reason`.

If a safe and useful procedure cannot be produced, do not call the tool. Ask for the missing information or explain the limitation instead.

## Map The Guide

- `requirements`: List only prerequisites, materials, tools, access, or conditions needed before work begins.
- `preparation`: List actions that make the user ready to start, such as setup, backups, isolation, or preheating.
- `instructions`: Provide the required, ordered actions that accomplish the outcome. Include at least one item.
- `wrapUp`: List verification, testing, cleanup, restoration, storage, or next actions after the main procedure.
- `tips`: Include optional advice, shortcuts, alternatives, or troubleshooting hints that are not required checklist actions.
- `notes`: Record concise warnings, assumptions, limitations, or context that does not belong in a checklist.

Omit optional fields that add no value. Do not invent unsupported fields such as a title, duration, difficulty, nested steps, or per-step metadata.

## Write Effective Steps

- Start each checklist item with a clear imperative verb.
- Keep one observable action or tightly coupled action group per item.
- Order prerequisites and safety controls before the actions that depend on them.
- Make each item understandable without relying on ambiguous words such as "it" or "that."
- Use concrete completion cues where they materially reduce uncertainty.
- Keep optional advice out of required checklist sections.
- Avoid embedded numbering because the widget orders the steps.
- Avoid headings, duplicate actions, and unnecessary prose inside list items.
- Preserve meaningful qualifications from the source instead of simplifying away safety or correctness.

## Validate Before Display

Confirm that:

- `instructions` is a non-empty array of non-empty strings.
- Every listed requirement is actually used, and every required prerequisite appears before use.
- The sequence has no unexplained jumps, contradictions, or unsafe implied actions.
- Verification and cleanup appear in `wrapUp` when the task needs them.
- Warnings and assumptions are visible without making the guide sound more authoritative than its sources support.
- The guide contains no secrets or sensitive details that should not be copied or shared from the widget.

After invoking `display-guide`, do not repeat the entire guide in conversation unless the user asks for a text version.
