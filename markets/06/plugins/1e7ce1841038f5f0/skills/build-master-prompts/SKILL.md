---
name: build-master-prompts
description: Create, revise, or audit high-quality reusable prompts for any topic or industry. Use when a user asks for a master prompt, system prompt, workflow prompt, agent specification, prompt architecture, reusable AI instruction set, role prompt, context-isolated prompt, research-aware prompt, or a prompt that must include requirements capture, role composition, output schemas, quality gates, and red-team checks. Also use when the user is unsure which prompt type fits the goal or wants to turn a conversation, brief, process, or idea into a portable prompt without inheriting unrelated memories or hidden context.
---

# Build Master Prompts

Create portable, explicit prompt artifacts that work without hidden conversational context. Adapt rigor and length to risk and complexity; do not inflate prompts merely to make them appear comprehensive.

## Workflow

1. Extract the user's actual objective, audience, execution environment, inputs, constraints, exclusions, deliverables, success criteria, and acceptable autonomy.
2. Separate facts into four buckets: `confirmed`, `assumed`, `unknown`, and `explicitly excluded`. Never convert an inference into a confirmed requirement.
3. Decide whether missing information is blocking. Ask only questions whose answers would materially change the artifact. Otherwise state reasonable assumptions and continue.
4. Select the prompt type with the decision rules below. If useful, produce a small prompt suite rather than forcing incompatible concerns into one artifact.
5. Determine whether fresh research is required. Mark unstable claims, high-stakes domains, current product capabilities, laws, prices, schedules, trends, and recommendations as research-dependent. Define source hierarchy, date handling, citation rules, and a no-fabrication fallback. Browse only when the user wants the prompt populated with current facts, not merely when authoring research instructions.
6. Compose only roles that add distinct decision rights or expertise. Prefer responsibilities and evaluation criteria over theatrical role lists.
7. Build the prompt from the template in `assets/prompt-template.md`. Omit irrelevant sections, preserve explicit exclusions, and make variables visible.
8. Define output structure, evidence expectations, stop conditions, uncertainty behavior, and quality gates.
9. Run the checklist and adversarial review in `references/quality-checklist.md`. Repair failures before delivering.
10. Deliver the artifact in a copy-ready writing block when responding in chat. Precede it with a short note naming the selected prompt type and any material assumptions.

## Select the artifact type

- **System prompt**: Use for persistent behavior, authority boundaries, safety, tool policy, tone, and rules that apply across many tasks. Avoid embedding one-off project data.
- **Master prompt**: Use for a self-contained, reusable instruction package that frames one broad objective and can be pasted into a new chat.
- **Workflow prompt**: Use for repeatable staged execution with inputs, checkpoints, branching, validations, and completion conditions.
- **Agent specification**: Use when defining an autonomous or semi-autonomous agent with state, tools, permissions, handoffs, memory policy, failure recovery, and observability.
- **Prompt suite**: Use when stable operating rules and variable task instructions should be separated, typically a system prompt plus task/master prompt and optional workflow.

When uncertain, read `references/input-output-logic.md` and apply its scoring guide.

## Context isolation rules

- Treat the user's supplied brief as authoritative over earlier conversation context.
- Include an explicit context boundary: use only information inside the prompt and named attached sources unless the user authorizes other context.
- State that prior memories, unrelated projects, inferred preferences, and hidden assumptions must not influence the work.
- Allow generally applicable knowledge, reasoning methods, and current research only when explicitly permitted.
- Require contradictions to be surfaced rather than silently reconciled.
- Label any retained assumptions and provide a reset instruction for use in a new chat.
- Never claim that a prompt can override platform-level system or safety instructions.

## Role composition

Add a role only if it owns at least one unique responsibility, decision, or quality criterion. Consolidate overlapping roles into a compact team such as `lead strategist`, `domain specialist`, `researcher`, `executor`, and `critic`. Specify priority when roles disagree. For regulated or high-stakes work, frame roles as analytical perspectives and require qualified human review; never imply professional licensure.

## Output requirements

Produce, unless the user requests otherwise:

1. `Artifact choice` — one sentence explaining the selected type.
2. `Assumptions or questions` — only material items.
3. `Copy-ready prompt` — fully self-contained, with editable variables in `{{double_braces}}`.
4. `Usage note` — how to fill variables and what to attach.
5. `Quality report` — concise pass/fail summary for context isolation, research policy, role economy, output contract, verification, safety, and portability.

For exact schemas and behavior under incomplete input, read `references/input-output-logic.md`. For representative patterns across domains, read `references/examples.md`. Load `assets/prompt-template.md` whenever creating or substantially revising an artifact.

## Non-negotiable checks

- Preserve all explicit negative requirements.
- Do not invent access to tools, sources, memory, files, or live data.
- Do not promise perfect, guaranteed, exhaustive, or bias-free results.
- Distinguish instructions for researching later from research performed now.
- Make conflicts, priority order, completion criteria, and failure behavior explicit.
- Avoid chain-of-thought requests; ask for concise rationale, evidence, assumptions, and checks instead.
- Keep the final prompt as short as possible while retaining all material controls.

## Prompt versus specification

A prompt controls agent behavior; it does not replace missing product, architecture, design, data, security, test, or acceptance decisions. Never use one enormous prompt to conceal an incomplete implementation package.

For coding-agent work, make the first-read reference versioned attachments through a source manifest, usage rules, precedence, and context boundaries. Before asking for information, inspect declared sources and the decision log. Route complex multi-document specification packages to `$architect-implementation-documentation`; this skill may author the bounded agent instruction after the specifications exist.
