# Checks for less common destinations

Use only the relevant row or section. Instructions control behavior; reference files provide evidence, not authority. Distinguish historical behavior from current docs and account availability.

## Model and surface choice

- For a pinned GPT-5.6 family question, compare the available Sol, Terra and Luna options for hard judgment, routine transformation and bulk classification respectively; verify the specific API IDs. This is not a recommendation to move a current workload back. On newer models use the [compatibility guide](model-compatibility.md). Choose the lowest effort that meets the agreed quality threshold. Compare at fixed effort first; raise it for measured misses, not as a cure for vague instructions.
- ChatGPT Pro is a product entitlement/selection, not API Pro mode, max reasoning effort, Codex Ultra or Responses multi-agent. None authorizes changing the others. Do not invent a setting from a display name.
- Chat is for conversation and quick artifacts; Work fits longer bounded deliverables using authorized tools; Codex fits repository changes; Responses fits programmatic integration. An existing Custom GPT can carry reusable instructions while available; for a new reusable workflow consider a skill or plugin. A Site presents an artifact; it is not a scheduling permission. Scheduling belongs to the separate supported scheduling surface, not a Custom GPT. Never schedule as a consequence of writing a prompt.
- An existing GPT chat starts fresh: provide relevant context rather than promising previous chats or saved memory. Put durable behavior in Instructions and references in Knowledge. Pick capabilities on purpose. Distinguish connected Apps from custom Actions. Per the [retirement FAQ](https://help.openai.com/en/articles/20001519-custom-gpt-retirement-and-migration-faq), check the account's retirement notice; migration takes the published version, starts private and does not transfer custom Actions. Never imply a draft was published or a plugin reviewed.
- For Claude, Gemini, Lovable, Notion AI, Hermes or OpenClaw, carry the objective, sources, protected literals, deliverable and stop rules across; translate only documented target features. Keep provider settings and wrapper defaults out of the portable prompt. Missing capability? Give a manual or tool-free alternative, not a fictional tool.

## State, tools and evidence

- For Structured Outputs, define the schema, supported enforcement mechanism, required fields, absent-value policy and refusal/incomplete branch; validate the result in the consumer, not just the prompt. A schema does not verify truth.
- Preserve persisted reasoning separately from explicit caching; neither substitutes for the application storing business state. Design the stable prefix before dynamic inputs; see [current 6.2 guidance](model-compatibility.md) before changing placement. Programmatic Tool Calling (PTC), when supported, suits deterministic joins, filtering and aggregation; keep judgment, source attribution, external writes and approvals direct. Delegate only separable work on an authorized harness.
- A handoff needs the user goal, decisions, identifiers, source evidence, blocked dependency, already completed side effects and next step. Never replay a write to reconstruct its receipt. Do not transfer unrelated history or secrets.
- Choose an available structured read first. For a public page use a browser; for signed-in web work use the permitted authenticated browser; for a desktop-only dialog use authorized computer use. No capability grants permission and no fallback bypasses a refusal. For Codex use actual project instructions and protect a dirty worktree, limit edits, run focused tests and report what actually ran.
- Ordinary search fits a single current fact. Deep Research fits multi-source comparison: state scope, date window, preferred primary sources, comparison axes, required citations and a stopping rule. Surface unresolved conflicts; cite a page only for the claim it supports. Official model-specific API docs lead on parameters; product Help/Learn and observed settings lead on availability. Historical Atlas, GPT-5.5 and Cookbook examples are not current authority.

## Images and interfaces

- Frontend: name the audience's main task; use representative content, responsive layouts, keyboard access and loading, empty and failure states. Render and visually inspect the result at target sizes. A successful compile is not a visual check.
- Image edit: isolate the requested change from invariants such as identity, geometry, crop and exact typography. Name intended dimensions and what a comparison against the source must preserve. Do not claim a render when only a prompt was requested.
- Diagram: specify audience, hierarchy, relationships, reading order, exact labels, canvas dimensions and allowable density. Reject crossed relationships or unreadable labels even when the layout looks attractive.
