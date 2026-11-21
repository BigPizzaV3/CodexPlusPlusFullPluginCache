---
name: rea-analysis-companion
description: Coordinate authorized reverse-engineering investigations with the REA toolset. Use when a user asks to understand shipped software, binaries, package contents, app behavior, runtime traces, or implementation evidence; do not use for ordinary source-repository architecture analysis.
---

# reverse engineering anything

This independent guide helps plan and interpret work with [REA: Reverse Engineer Anything](https://github.com/morluto/rea). It does not include or invoke REA's local MCP server or CLI. Never imply that this skill inspected a file unless actual analysis tools or outputs are present in the current conversation.

## 1. Establish scope and authorization

- Ask what exact artifact, application, or user-owned page is in scope and what question the user needs answered.
- Proceed only when the user states they own the target or have authorization. If ownership/authorization is unclear, pause before guidance that would enable access to a third-party target.
- Keep requests bounded to a named target, feature, version, and evidence question. Do not expand into adjacent apps, hosts, accounts, or endpoints.
- Decline credential theft, malware deployment, stealth/evasion, exploitation of third-party systems, bypassing DRM/licensing/access controls, or unauthorized extraction of proprietary data. Offer legitimate debugging, defensive assessment, compatibility, or interoperability alternatives.

## 2. Verify the capability boundary

- If REA tools are present, inspect the active tool inventory and input schemas before selecting a workflow. Use only advertised tools and supported arguments.
- If tools are absent, say the current chat cannot execute REA analysis. You may provide a plan or explain how the user can configure REA locally; do not claim setup, installation, registration, or analysis occurred.
- Prefer an existing installation or supplied results. Do not run setup/doctor on every request.
- A skill-only installation does not register an MCP server, install analysis engines, or add tools to the active session.

## 3. Route by target

Use `rea-target-routing` for the detailed map. Choose one initial route from the supplied target type. When a route requires an active target and none is selected, ask for the missing path/app rather than choosing an example. For source repositories, use normal repository tools unless a claim depends on shipped artifacts or behavior not represented in available source.

## 4. Investigate summary-first

1. Convert the request into a short checklist of questions and required evidence.
2. Reuse matching sessions and existing findings if available; avoid duplicate identical calls.
3. Start with the smallest overview or inventory that can answer the question.
4. Trace only the relevant module, code path, call, state transition, or observation.
5. Follow up only when a named question remains unresolved.
6. Distinguish direct observations, inferences, and unknowns. Preserve evidence IDs and limitations.
7. Do not equate strings, symbols, pseudocode, or a static graph with execution. Runtime behavior needs runtime evidence.

## 5. Runtime and untrusted-artifact boundary

Before any operation that executes or interacts with a target, confirm the exact target and lifecycle. Warn that local REA providers use the user's permissions and are not a sandbox; processing an untrusted binary can expose the host to parser/provider risk. Never install an engine or change configuration silently. Setup plans, dependency installation, target launch, and interaction must stay within user authorization and host rules.

REA analyzes targets locally, but tool results are delivered to the model provider. Do not include proprietary binaries, credentials, private project files, or sensitive logs in prompts unless the user confirms this is allowed under their policies.

## 6. Deliver a traceable answer

Use `rea-evidence-and-reporting` to produce a concise answer with:

- finding and confidence;
- evidence IDs and what each directly shows;
- inference and reasoning, clearly labeled;
- scope, version, host/provider, and coverage boundary when known;
- unresolved questions and the smallest useful next step.

Check the original checklist before calling the investigation complete. Close tool-created native sessions when supported and the investigation is finished.
