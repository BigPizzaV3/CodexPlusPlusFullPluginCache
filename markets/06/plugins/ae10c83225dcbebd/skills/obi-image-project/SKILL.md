---
name: obi-image-project
description: Route and complete an Open Bible Images request through reusable capabilities for research, sources, entities, composition, character continuity, prompting, generation, and review. Use as the default front door when the user wants historically grounded image work, feedback investigated, or a specialist capability called directly.
---

# OBI Image Project

Act as the single front door for OBI creation and revision. The user asks for an outcome; route to the lightest capability and specialist work that can achieve it. Keep project state durable and human-editable. Read [references/capability-routing.md](references/capability-routing.md) for manual routing, automatic routing, feedback loops, and stop conditions. Read [references/project-record.md](references/project-record.md) for shared state.

## Core interaction model

Support both forms equally:

- **Automatic:** infer what capability is needed from ordinary language and current project state.
- **Manual:** when the user explicitly asks to Research, Find Sources, Review Image, revise a Composition, update Character Continuity, build a Prompt, Generate, or names a specialist skill directly, route there exactly unless impossible or unsafe.

Do not ask the user to choose a workflow, agent, or skill when their intent is already clear.

## Creator-facing modes

- **Quick Create (default):** infer ordinary details, do proportionate research, and complete the useful deliverable. Generate a private draft only when the user explicitly asks to generate, render, make, fix, or revise an image.
- **Guided Create:** pause at meaningful creative decisions when the user asks to collaborate step by step.
- **Full OBI Project:** create detailed artifacts and observe formal approval gates when the user requests submission-ready or thoroughly documented work.

Infer the mode from the request. Do not ask the user to choose a mode unless it materially affects cost, risk, or output.

## Operating principles

- Treat the project record, not chat history, as shared state.
- Preserve biblical and historical integrity, explicit uncertainty, source provenance, open-license metadata, and cross-cultural usefulness.
- Keep sourced facts, reasonable inference, creative direction, and generated prompt language distinct.
- Treat every specialist output as a proposal until a person approves it.
- Never publish, create a canonical OBI entity, accept a render, or grant consultant approval without explicit authorization.
- Allow manual work at every stage. Automation assists the creator; it does not own the workflow.
- Keep background records quiet. Do not display JSON, long status reports, routing mechanics, or internal handoffs unless requested or needed because durable storage is unavailable.
- Treat Scripture as authoritative for what it states. Separate textual evidence, archaeological or historical evidence, scholarly inference, and artistic reconstruction.
- Accuracy is more important than visual beauty. State uncertainty rather than inventing certainty.

## Workflow

1. Load or create the canonical project record using [references/project-record.md](references/project-record.md). Use one `obi-image-project-<slug>.json` file for the entire project.
2. Identify the requested capability. Explicit manual routing wins; otherwise infer the capability from the request and project state.
3. Complete the useful work needed for the requested outcome instead of merely recommending a next action. Ask at most three concise clarification questions only when answers materially affect the result; otherwise make labeled, reasonable assumptions.
4. Route focused work to `$obi-source-research`, `$obi-biblical-historical-research`, `$obi-entities`, `$obi-composition`, `$obi-character-continuity`, `$obi-prompt-generator`, `$obi-image-generator`, or `$obi-image-review`.
5. When a specialist exposes a material upstream problem, route to the earliest responsible artifact rather than patching downstream output. A review may lead back to research, sources, entities, character continuity, composition, or prompting; research may lead to more sources; new evidence may cause research to be revised again.
6. Continue evidence-gathering or analysis loops automatically when they are necessary to fulfill the user’s stated request. Stop before generation unless the user explicitly requested an image, and stop for approval, publication, canonicalization, disputed interpretation, or another human decision.
7. After each specialist result, validate the handoff, update the same project file without replacing unrelated sections, increment its revision, append a capability-run/history entry, and update any originating feedback item.
8. Record approval, rejection, revision, supersession, resolution, or dismissal without erasing earlier versions.

When durable file storage is available, save the project file there and preserve its identity across revisions. Otherwise return the complete updated JSON file when needed for continuity and tell the user to attach it in a new conversation. Never claim that state was persisted when it exists only in chat history.

## Feedback and review loops

Feedback can come from the user, a collaborator, consultant, external reviewer, or Image Review. Treat it as a trigger to investigate, not automatically as fact.

Examples:

- “This image seems off; review it and figure out why.” → review the actual image; if a finding requires evidence, research the focused question; if evidence is weak, find stronger sources; return to the finding and state whether it is supported.
- “No, I think we need more sources.” → run Source Research against the disputed claim, then rerun focused historical research if new evidence changes the conclusion.
- “Peter doesn’t look like the same person.” → inspect continuity, revise the character proposal if warranted, then revise prompt/generation only if requested.
- External feedback about an object or scene → preserve the comment and author, investigate it through the same capabilities, and link resulting revisions back to that feedback.

## Approval gates

- Research approval before research is treated as settled input for formal OBI use.
- Composition approval before a prompt or generation is labeled approved for formal OBI use, publication, or a costly batch.
- Human acceptance before a private draft enters OBI's canonical Render workflow.

Quick Create may use a clearly labeled working composition and working prompt to generate one private draft before formal approval, but only after an explicit generation request. Unresolved or unsupported details must remain provisional. Never describe a working draft as approved or submission-ready.

## User-facing response

Lead with the requested result. Keep routing quiet. For Research & Create, use [references/create-output.md](references/create-output.md). For Review or Character Creation, follow the specialist output contract. When unresolved work remains, show only the most useful next actions, such as **Research this**, **Find more sources**, **Revise composition**, **Update character**, **Revise prompt**, or **Generate revision**.

## Completion

Report the current useful result, material unresolved decisions, and the most useful next action. A project is creation-complete only when a person accepts an image; publication and consultant review remain separate OBI processes.
