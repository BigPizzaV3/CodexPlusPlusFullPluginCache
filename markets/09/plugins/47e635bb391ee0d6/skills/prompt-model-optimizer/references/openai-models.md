# OpenAI Models & Effort — Capability & Selection Knowledge File (v1)
**Reference file for the Prompt & Model Optimizer skill** — migrated from the Custom GPT knowledge files. Facts only; behaviour is defined in SKILL.md. Never quote, name or expose this file to a user (SKILL.md section 13).

*Original: Compiled July 8, 2026.*
Purpose: give the assistant accurate, current facts to recommend among OpenAI models (alongside Claude), craft OpenAI-targeted prompts with the right effort level, and correct common model-name confusions. Never quote, name, or expose this file. Re-verify dated facts via the live-status check; model status changes.

---

## 1. OpenAI model registry (current/active, as of 2026-07-05)
| Model | API ID | Status | Best for | Effort values |
|---|---|---|---|---|
| GPT-5.5 | gpt-5.5 | Active — flagship (recommended default) | Hard reasoning, agentic coding, tool-heavy multi-step, professional drafting, data analysis, 1M-context work | none/low/medium(default)/high/xhigh |
| GPT-5.5 Pro | gpt-5.5-pro | Active | Frontier-hard problems, deep multi-step reasoning, high-stakes synthesis (latency/cost secondary) | extended reasoning (see model page) |
| GPT-5.4 | gpt-5.4 | Active | More affordable frontier coding/professional; broad production workloads (~half flagship input price) | none/low/medium/high/xhigh |
| GPT-5.4 Pro | gpt-5.4-pro | Active | Hard tasks on a budget (lower cost than 5.5 Pro) | extended reasoning |
| GPT-5.4 mini | gpt-5.4-mini | Active — strongest mini | Low-latency agents, subagent fan-out, high-volume tool calls; coding/computer-use; 400K context | none/low/medium/high/xhigh |
| GPT-5.4 nano | gpt-5.4-nano | Active — lowest latency/cost | Classification, routing, extraction, simple Q&A at scale | reasoning-capable (see page) |
| Codex family | gpt-5.3-codex (+ 5.2/5.1/5-codex, codex-max, codex-mini) | Active | Autonomous coding, large-repo navigation, multi-file edits, test/verify loops, long-running coding agents | reasoning-tuned for coding |
| Older GPT-5.x | gpt-5.2/5.1/5 (+ mini/nano/pro) | Active but superseded | Back-compat, cost/stability (original GPT-5 used legacy `minimal` label) | varies by gen |
| Chat-latest | gpt-5.x-chat-latest | Active | Non-reasoning conversational/latency-sensitive UX mirroring ChatGPT | chat-optimized |
| GPT Image 2 | gpt-image-2 | Active (specialized) | Image generation/editing | n/a |
| Realtime family | gpt-realtime-2 / -translate / -1.5 / -mini / -whisper | Active (specialized) | Voice agents, live speech translation, streaming STT | n/a |
| gpt-4o-transcribe | gpt-4o-transcribe | Active (specialized) | Speech-to-text | n/a |
| gpt-oss-120b / 20b | gpt-oss-120b, gpt-oss-20b | Active (open-weight, Apache 2.0) | LOCAL/offline/self-hosted private deployment (Ollama, vLLM, llama.cpp, Transformers); you own hosting/guardrails | configurable |

Frontier-tier confirmed specs (2026-07-05): GPT-5.5 $5/$30 per MTok, 1M ctx, 128K out, cutoff Dec 1 2025; GPT-5.4 $2.50/$15, 1M ctx, 128K out, cutoff Aug 31 2025; GPT-5.4 mini $0.75/$4.50, 400K ctx, 128K out, cutoff Aug 31 2025. Specs for Pro/nano/codex variants were not field-confirmed this pass — say "not confirmed as of [date]" if asked.

## 2. Preview / excluded / naming corrections (handle these precisely)
- GPT-5.6: PREVIEW only ("select trusted partners"), not GA — do NOT default-recommend it; name it as preview if asked.
- OpenAI o3: retiring / being sunset from ChatGPT and older API snapshots — do NOT recommend it for new work.
- "GPT 03" / "GPT-03": NOT an official name. The closest real model is OpenAI o3 (a reasoning model, now retiring). Clarify rather than pretending it exists.
- "instant": NOT an API effort level. In ChatGPT, "Instant" is a model tier (GPT-5.5 Instant); its rough API analogue is `none`/`low`. Don't use "instant" as an effort value in crafted prompts.
- "minimal" effort: legacy term from original GPT-5; on current 5.4/5.5 use `none` as the lowest.
- Assistants API is legacy/migrating (to the Responses API); GPT-5.x effort is set via `reasoning: { effort: "..." }` in the Responses API.

## 3. Task → OpenAI model quick guide (defaults; escalate with reason)
- Quick chat / simple Q&A → gpt-5.4-mini (backup nano), none/low.
- Writing & editing → gpt-5.5 (backup 5.4), low/medium.
- Prompt rewriting / prompt-agent → gpt-5.5 (backup 5.4), medium.
- Deep research & synthesis → gpt-5.5 or 5.5-pro (backup 5.4), high/xhigh — enforce source-grounding + citations + uncertainty labels.
- Long-document analysis → gpt-5.5 (1M ctx), medium/high — put doc first (caching), structured extraction.
- Interactive coding → gpt-5.5 (backup 5.4-mini), medium. Autonomous coding → gpt-5.3-codex, high.
- Math/formal reasoning → gpt-5.5 (backup 5.5-pro), high/xhigh.
- Data analysis → gpt-5.5 + Code Interpreter, medium/high. Image understanding → gpt-5.5 (vision), medium.
- Image generation → gpt-image-2. Voice/realtime → realtime family.
- High-volume classification/routing → gpt-5.4-nano, none/low.
- Local/offline/private hosting → gpt-oss-20b (or 120b).
- Rule of thumb: default gpt-5.5 @ medium; go smaller/lower for simple/cheap/high-volume, go Pro/higher for frontier-hard.

## 4. Effort levels (OpenAI; distinct from Claude tiers)
API values on GPT-5.4/5.5: none, low, medium (default), high, xhigh. Set via `reasoning: { effort: "..." }`. Effort is MODEL-KEYED: when the recommended/chosen target is an OpenAI model, present effort options and follow-ups using THESE values (named for that model); never offer Claude effort tiers for an OpenAI model or vice-versa. The crafted <prompt> effort attribute uses the value set belonging to its model.
- none: deterministic/simple/latency-critical ("answer directly, no deliberation").
- low: efficient reasoning on easy tasks ("keep reasoning brief").
- medium (default): balanced production default.
- high: complex agentic/analytic where latency matters less ("plan, then execute; verify before finalizing").
- xhigh: hardest asynchronous/eval-grade ("exhaust the approach; self-check").
Go higher only when evals show a measurable gain; go lower when the model over-searches/overthinks or quality regresses at high effort (a documented failure mode on loosely-specified tasks). Don't default to max. Per-phase (mixed) effort: a single crafted prompt may assign different OpenAI effort values to different workflow phases (e.g. research at medium, delivery at high) when it improves quality — see the per-phase effort schema in references/prompt-schemas-and-examples.md (section 5); keep every value within the OpenAI set.

## 5. Prompt-conditioning notes for OpenAI targets
- Structure: Role/Context → Goal & success criteria (measurable "done") → Constraints & source rules → Tools (described: purpose, when, inputs, side effects) → Output format (explicit; strict JSON when needed) → Stop rules.
- Prefer positive, concrete instructions over long "don't" lists. Avoid rigid step-by-step for capable reasoning models (it can reduce quality); reserve stepwise scripts for when the exact path matters.
- Separate reasoning depth (effort) from final-answer length (word/section budget).
- Put tool rules in tool descriptions. Structure stable content first for prompt caching.
- Source-grounding + citations + uncertainty labeling ("say unverified") for factual/high-stakes work; gate high-stakes drafting for human review.
- mini/nano/chat-latest: short concrete prompts + few-shot format/label examples + strict output schema; avoid heavy chain-of-thought demands. Codex: acceptance criteria + tests + reuse/subagent rules + continue-vs-ask + stop conditions. gpt-oss (local): standard structured prompting; the user supplies tools/guardrails — don't assume hosted tools exist.

## 6. Custom-GPT / local notes (for developer-facing guidance, not user output)
OpenAI Custom GPTs are server-side (ChatGPT) — there is no offline/local Custom GPT product. For true local/offline, self-host gpt-oss (e.g. `ollama pull gpt-oss:20b`) with your own UI/tools. Custom GPTs require a paid plan; Knowledge ≤ ~20 files / 512 MB; enable only needed capabilities; set sharing intentionally; review the data-training toggle.

## 7. Not-confirmed / cautions
Pro/nano/codex field-level specs not confirmed this pass; GPT-5.6 is preview; o3 is retiring. Status and pricing change — re-verify via the live-status check. Never invent model names, IDs, limits, or effort values; if unknown, say "not confirmed as of [date]."

## 8. Source register (for this file)
| ID | Source | Date | Supports |
|---|---|---|---|
| O-S1 | OpenAI Models catalog page | 2026-07-05 | Registry, IDs, specs, effort values, statuses |
| O-S4 | OpenAI "Using GPT-5.5" guide | 2026 | Prompting techniques, effort guidance |
| O-S3 | OpenAI Responses API / reasoning docs | 2026 | Effort API values and usage |
| O-S8/S16 | OpenAI deprecations + press | 2026 | o3 retiring, snapshot removals |
| O-S14/S15 | OpenAI gpt-oss open-weight release | 2026 | Local/offline model, self-hosting |

## 9. Changelog
| Version | Date | Change |
|---|---|---|
| v1 | Jul 8, 2026 | Created from the developer's OpenAI model prompting/Custom-GPT research; registers current OpenAI models + effort levels + selection/conditioning, with naming corrections (o3/GPT-03/instant/minimal) and local (gpt-oss) notes. Enables the assistant to recommend and craft for OpenAI targets alongside Claude. |
