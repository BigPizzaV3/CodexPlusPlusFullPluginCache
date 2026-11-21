# Destination patterns

These are original templates. Select and shorten them; no section is mandatory. The model executing the task and its actual tool contract matter more than the model writing the prompt.

## ChatGPT

```text
Use [relevant sources] to produce [result] for [audience].
Keep [facts or constraints] unchanged. Return [useful format].
Flag information the sources do not establish.
```

Use connected sources only when that connection is available and authorized. A normal chat prompt cannot set API reasoning or grant access to a local folder. See [official prompting guidance](https://learn.chatgpt.com/docs/prompting).

## Codex

```text
Complete [requested change] in [existing project or exact scope].
Use applicable project instructions and relevant owned skills.
Preserve [important behavior, protected data and concurrent edits].
Authorized work: [specific implementation and verification scope].
Done when: [observable behavior and proportionate checks].
Report the result, actual verification and any remaining dependency.
```

A task prompt handles the current outcome; `AGENTS.md` holds durable project conventions; skills hold reusable workflows. Keep those layers consistent. Avoid pasting the entire documentation library into the task. See [Codex prompting](https://learn.chatgpt.com/docs/prompting#prompting-codex) and [customization](https://developers.openai.com/codex/concepts/customization).

## OpenAI API

Keep stable application instructions separate from user input and retrieved documents. Use delimiters and source labels when structure helps. With Responses, the `instructions` field applies to the current request; when using `previous_response_id`, resend the instructions needed on the next request rather than assuming they carry over. Preserve supported conversation and tool-result state in the application.

For a structured result, choose the actual schema-enforcement mechanism supported by the selected API and model. Specify how to handle missing fields and refusals. A prompt asking for JSON does not itself enforce a schema. A request can return tool calls and other output items; use supported SDK parsing instead of assuming the first output item is final text.

Version the prompt alongside a small set of representative tasks. Keep model and effective effort steady when assessing a prompt-only change. Check tools, output correctness, source use and critical failures; record what was actually executed. Do not claim a live API evaluation from text inspection.

Source: [API prompt engineering](https://developers.openai.com/api/docs/guides/prompt-engineering). For parameters, select [model compatibility](model-compatibility.md).

## Hermes or OpenClaw

```text
Target: [actual agent/profile, provider/model and supported API route].
Outcome: [bounded result].
Context: [minimum relevant sources, current state and exact target].
Tools and authority: [tools actually available; permitted writes/actions].
Preserve: [current model/effort/fallback settings and protected boundaries].
Success: [deliverable and authoritative evidence where applicable].
If blocked: identify the affected step and missing dependency; complete
independent authorized work and do not route around a refusal.
```

This is a portable task contract, not verified Hermes or OpenClaw configuration documentation. The supplied environment owns memory, context compaction, profile visibility, credentials, approval rules and adapter behavior. Identify missing runtime facts instead of guessing defaults. Keep secrets and unrelated private history out of handoffs.
