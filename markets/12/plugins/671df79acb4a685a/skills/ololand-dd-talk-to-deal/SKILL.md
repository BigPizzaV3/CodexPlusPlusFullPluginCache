---
name: ololand-dd-talk-to-deal
description: "Use when the user asks to run the OloLand ololand-dd-talk-to-deal workflow.\
  \ Ask a question about a deal and get a conversational, voice-optimized response\
  \ \u2014 concise answers with rounded numbers and clear recommendations."
---


# Workflow for ololand-dd-talk-to-deal

Follow the OloLand command instructions below when the user asks for `ololand-dd-talk-to-deal` or the equivalent workflow.

# Talk to Your Deal

Have a natural conversation about a deal. Returns voice-optimized responses suitable for hands-free review, supported voice interfaces, or quick deal check-ins.

## Usage

```
ololand-dd-talk-to-deal <deal_id> <question>
```

## Arguments

- `deal_id` (required) — The deal to ask about.
- `question` (required) — Natural language question about the deal.

## Execution

1. Classify the request before choosing a rail:
   - For a simple lookup-style question covered by `ololand-dd-plan`'s no-plan exceptions, call `talk_to_deal` from the MCP server with the deal_id and question.
   - Before every other non-trivial deal question, follow `ololand-dd-plan`: create or reuse the conversation session, submit the user's verbatim question with `submit_plan_for_approval`, render the proposed steps, and stop for the user's approval. Never invoke either MCP message tool for that planned execution. After approval, direct the user to continue the same session in the OloLand app or normal SSE/message endpoint with the returned plan payload supplied as `approved_plan` on `SubmitMessageRequest`. That field supplies execution context; it is not a persisted or hash-validated approval identity. The MCP `talk_to_deal` and `ask_deal_agent` tools cannot carry it, and quoted plan text is not a substitute. If the client cannot use the normal session endpoint, report governed execution as unavailable on this rail.
   - Do not fall back to an MCP message call after planning, even if `required_sections=["answer", "evidence", "assumptions", "open_questions"]` would otherwise be supported. Completion headings and a read-only boundary do not replace the normal endpoint's `approved_plan` execution context.
2. For the lookup-only `talk_to_deal` path, relay any returned `boundary_gate`, `completion_contract`, and `grader_passed` fields. A response is not a completed or verified answer merely because text was returned. If any applicable field is absent, unavailable, or failed, say so plainly and do not replace it with an inferred pass.
3. Every deal fact, figure, date, risk, or recommendation must retain its returned inline source citation. Voice style may round a cited number (for example, "about $160 million [3]"), but must not remove its citation or convert missing evidence into an estimate. State unavailable evidence and the resulting limitation instead.
4. Do not state a buyer's or acquirer's identity, strategy, mandate, interest, expected synergies, or likely action unless it is supported by a tenant-authorized returned source citation. A caller-supplied premise may be discussed only when labeled as a hypothetical, not as a fact about the buyer.
5. The response uses voice-mode directives:
   - Concise (2-3 sentences per point)
   - Rounded numbers ("about 160 million" not "$164,501,234")
   - Narrative style, no markdown tables
   - Clear recommendation or next question at the end

## Examples

- `ololand-dd-talk-to-deal deal123 What are the top three risks?`
- `ololand-dd-talk-to-deal deal123 Is this a good deal at 8x EBITDA?`
- `ololand-dd-talk-to-deal deal123 Summarize the financials in 30 seconds`
- `ololand-dd-talk-to-deal deal123 What did we learn from similar deals?`
- `ololand-dd-talk-to-deal deal123 What's the risk-adjusted IRR?`

## Use Cases

- **Morning deal check**: Quick verbal summary of overnight analysis results
- **Commute review**: Hands-free deal assessment via supported voice interfaces
- **IC prep**: Rapid-fire Q&A to prepare for investment committee
- **Telegram/Discord**: Quick deal updates via supported messaging interfaces


## OpenAI execution requirements

Use the connected MCP server's current tool schemas. Do not invent tool arguments, job-status endpoints, inputs, or outputs. If a referenced tool is unavailable, explain the limitation and request the needed connection or data. Invoke writes only when the user has requested the corresponding action. Do not initiate purchases or payments. An unrun, unsupported, or unavailable procedure is a gap, never a passing result.


OpenAI cannot execute local lifecycle hooks. Use the packaged explicit setup/review workflow when requested. Server-side MCP auditing remains authoritative; preserve evidence blockers and human-only approval gates.

Claim-correction submission is unsupported in this OpenAI upload because the current handler records surface=cowork. Do not invoke submit_agent_claim_correction from OpenAI. Explain the limitation and retain proposed correction text for human review without claiming submission. See unsupported-workflows.json for the excluded canonical workflow.
