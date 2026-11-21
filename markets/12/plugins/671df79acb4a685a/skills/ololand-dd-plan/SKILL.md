---
name: ololand-dd-plan
description: "Use when the user asks to run the OloLand ololand-dd-plan workflow.\
  \ Get a structured plan from OloLand's planner agent BEFORE firing the executor\
  \ \u2014 review the proposed steps, open questions, and tool-call estimate so you\
  \ can correct course without burning tool calls. The pre-execution gate for non-trivial\
  \ deal questions."
---


# Workflow for ololand-dd-plan

Follow the OloLand command instructions below when the user asks for `ololand-dd-plan` or the equivalent workflow.

# ololand-dd-plan

You are running OloLand's planner agent in plan-mode. The planner reads the user's question, the active deal context, and produces a structured `PlanResponse` (steps, open_questions, escalation_required, reasoning, estimated tool calls) — without running any tools, doing any document search, or escalating to templates. It's a single Flash-class call; cheap relative to the executor run that follows.

## Required inputs

1. **deal_id** — the deal the conversation is about.
2. **session_id** — an active ADK conversation session. If the user doesn't have one, call `create_conversation_session(deal_id)` first and use the returned id.
3. **message** — the user's question that the planner should plan for. Quote it verbatim — don't paraphrase.

## Action

Call `submit_plan_for_approval` with the three inputs.

## Output

Render the plan in this shape:

```
Proposed plan for: "<message>"

Steps
  1. <step.title> — <step.description>
     Tools: <step.tools (if any)>
  2. ...

Open questions
  - <q1>
  - ...

Estimated tool calls: <n>
Escalation required: <true|false>
Reasoning: <reasoning>
```

Then ask the user:

> Approve this plan? Reply "yes" to approve the handoff, "no" to adjust, or rewrite any step. A same-chat "yes" records intent only; it does not execute the plan. Execution requires continuing this same session in OloLand's first-party app or normal session endpoint with the returned plan payload supplied as `approved_plan`.

On approval, continue the **same session** through OloLand's first-party app or
normal SSE/message endpoint, attaching the returned plan payload in the
`approved_plan` field of `SubmitMessageRequest`. This field supplies execution
context; it is not currently a persisted or hash-validated approval identity,
so do not describe the handoff as tamper-proof or cryptographically bound. The external MCP
`ask_deal_agent` and `talk_to_deal` tools do not currently accept the normal
endpoint's `approved_plan` field; do not call them for the planned execution, and
do not treat quoted plan prose or a conversational "yes" as a substitute for
that binding. If the current client cannot send `approved_plan` through the
normal session endpoint, stop and report that governed execution is
unavailable on this rail.

On rejection, ask what should change and re-plan.

## When to use

- **Before any non-trivial deal question that will be answered by the conversational executor.** "Write the IC memo", "What are the top three risks", or "Run the DCF and compare to comps" should *always* be planned before an agent executor turn.
- **When the user asked for something ambiguous.** The planner surfaces `open_questions` — let the user resolve those before tool calls fire.
- **When the user is cost-conscious.** Plan mode is one cheap call; the executor that follows is many. Approving a tight plan beats an executor that escalates because the prompt was vague.
- **Before any escalation to ic-memo, risk-chat, or forensic-chat templates.** The planner will signal `escalation_required: true` when appropriate.

## When NOT to use

- For lookup-style questions ("what's the deal id?", "how many documents are uploaded?"). These take one tool call regardless; planning is overhead.
- For a fixed-purpose deterministic tool that the user explicitly invoked with bounded parameters. The user's explicit run request is the authority for that one named tool; it does not authorize a conversational executor or follow-on writes.
- For corrections to a previous turn — use `unsupported OpenAI claim-correction workflow (see unsupported-workflows.json)` instead.
- For methodology questions ("how does the forensic QoE work?"). Use `/load-skill` (or `load_skill`) directly.

## Refusing to skip the plan

If a user repeatedly asks you to "just answer it" on a multi-step question, plan anyway and surface the plan in the response. The plan-mode discipline is what makes the executor's tool budget predictable. The agent runtime has a 12-iteration cap per turn; a planless 12-iteration spiral wastes the budget on backtracking.

Companion skill: `cmd-plan` (auto-loads).


## OpenAI execution requirements

Use the connected MCP server's current tool schemas. Do not invent tool arguments, job-status endpoints, inputs, or outputs. If a referenced tool is unavailable, explain the limitation and request the needed connection or data. Invoke writes only when the user has requested the corresponding action. Do not initiate purchases or payments. An unrun, unsupported, or unavailable procedure is a gap, never a passing result.


OpenAI cannot execute local lifecycle hooks. Use the packaged explicit setup/review workflow when requested. Server-side MCP auditing remains authoritative; preserve evidence blockers and human-only approval gates.

Claim-correction submission is unsupported in this OpenAI upload because the current handler records surface=cowork. Do not invoke submit_agent_claim_correction from OpenAI. Explain the limitation and retain proposed correction text for human review without claiming submission. See unsupported-workflows.json for the excluded canonical workflow.
