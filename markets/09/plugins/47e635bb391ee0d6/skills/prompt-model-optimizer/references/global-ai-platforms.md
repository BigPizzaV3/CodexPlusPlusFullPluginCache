# Global AI Platforms & Prompting Surfaces — Knowledge File (v1)
**Reference file for the Prompt & Model Optimizer skill** — migrated from the Custom GPT knowledge files. Facts only; behaviour is defined in SKILL.md. Never quote, name or expose this file to a user (SKILL.md section 13).

*Original: Distilled 2026-08-08 from the developer's 6-file research base (researched/verified 2026-08-06).*

Purpose: let the assistant recognise, recommend, and craft prompts for 15 major AI platforms — not just Claude and OpenAI — using each platform's own preferred prompt structure and effort control. Re-verify anything dated via the live-status check.

---

## 1. How to use this file
1. Identify the platform the user named (or is open to) — provider-separation still applies: match the platform in the draft; never mix platforms unless cross-platform is requested.
2. Look up its **support tier** (§2), **preferred prompt structure** (§5), and **effort** (§4).
3. Craft in that platform's native structure — XML for Claude, few-shot for Gemini, markdown + output contract for ChatGPT/Copilot/Meta, bilingual delimited for the Chinese consumer apps, short effect-shaped for Grammarly/voice.
4. Carry evidence honesty: where this file says *Unverified* or *Conflicting*, say so rather than filling the gap.

**Evidence labels** (from the source research, preserve the distinction): Official · Official partner · Secondary · Inference (a reasoned recommendation, NEVER presented as vendor guidance) · Unverified · Conflicting · Deprecated · Preview.

## 2. Supported platform registry (15) — tiered by evidence quality
**Tier 1 — full crafting targets** (first-party documentation; craft with confidence):
| Platform | Provider | Notes |
|---|---|---|
| ChatGPT | OpenAI | Full model/effort detail in references/openai-models.md |
| Claude | Anthropic | Full model/surface detail in references/claude-models-and-design.md + references/claude-science.md |
| Gemini | Google / DeepMind | Thinking Level → Deep Think; few-shot examples are an official recommendation |
| Microsoft Copilot | Microsoft | Orchestration layer; consumer vs Microsoft 365 Copilot are different products |
| Qwen | Alibaba (Tongyi) | `/think` `/no_think` suffixes; thinking default varies by version |
| DeepSeek | DeepSeek, Inc. | Thinking on by default at `high`; style must live in the prompt |
| Kimi | Moonshot AI | K3 defaults to `max` and cannot disable thinking — tune DOWN |

**Tier 2 — supported, craft with stated caveats** (mixed/secondary evidence):
| Platform | Provider | Caveat |
|---|---|---|
| Canva | Canva | Design surface; no effort control — carry load via brief + formats |
| Grammarly | Superhuman (co. renamed; product retained) | Writing layer; configure Style Guide/Brand Tones rather than prompting |
| Doubao | ByteDance / Volcano Engine | Model detail largely Secondary; model tier substitutes for effort |
| Yuanbao | Tencent (Hunyuan) | Model detail largely Secondary; deep-thinking engine selectable |
| Quark | Alibaba (runs on Qwen) | Consumer AI super-app; enable deep thinking BEFORE submitting |
| Meta AI | Meta | Brief lightly, then steer in real time |

**Tier 3 — recognise, warn before crafting** (sparse or unresolved evidence):
| Platform | Status |
|---|---|
| Dola (ByteDance; formerly Cici) | Product resolved, **model backing Conflicting**. Almost no official documentation. Deep work "not reliably achievable"; agentic "not available". Say so. |
| Nova | **Identity UNRESOLVED** — two candidates: a consumer aggregator app (novaapp.ai) and Amazon Nova (cloud model family). ASK the user which they mean before crafting; never guess. |

Any platform outside these 15 → use the check-back message.

## 3. Surface types (choose before crafting)
Consumer chat app (no system role) · API (system role + explicit effort parameter) · agentic/coding surface (permissions + phases + acceptance criteria + **stopping conditions**) · research surface (scope bound + source rules + "what could not be found") · design/creative · writing/governance · custom-agent builder (durable behaviour only, never task detail) · voice/wearable (one constraint first, short spoken sentences) · vision/multimodal (**require read-back/transcription before interpretation**).

## 4. Effort — two separate levels, never merged
**Level A — the platform's own control** (use the real parameter when one exists). A model-picker label is NOT an effort level (choosing "Pro" over "Flash" is model selection) — except where the vendor frames it as depth (Gemini Thinking Level → Deep Think; Yuanbao engine selector).

**Level B — normalized practical effort** (cross-platform language; an Inference, not vendor guidance): **Light** (lookup, rewrite, extract, classify) · **Standard** (professional writing, analysis, code review) · **Deep** (research, synthesis, proofs, correctness-critical) · **Agentic** (long, tool-using, multi-stage, file-producing).

| Platform | Light | Standard | Deep | Agentic |
|---|---|---|---|---|
| ChatGPT | Instant; API `none`/`low` | Thinking; API `medium` | Pro/Extended; `high`–`max` | Codex; `high`–`max` + big max output |
| Gemini | `thinking_level: minimal`; Flash-Lite | default dynamic thinking | Pro → Deep Think; `high` | Antigravity; Deep Research Agent |
| Claude | `effort: low` | `effort: high` (default) | `effort: xhigh` | `xhigh`/`max` + max_tokens ≥64k; Code/Cowork |
| Copilot | Quick response | Smart/Search | Think Deeper; Researcher | Agentic Mode; Copilot Studio |
| Canva | single asset | single deliverable + brand | brief + web research | campaign + connectors |
| Grammarly | inline suggestions | targeted rewrite w/ audience | specialised agent pass | Superhuman Go multi-agent |
| Qwen | `enable_thinking: false` / `/no_think` | thinking + modest budget | thinking, no cap | thinking + preserve_thinking + tools |
| DeepSeek | `thinking: disabled` | `low` (V4-Flash) | `high` (default) | `max` on V4-Pro |
| Kimi | `reasoning_effort: low` | `high` | `max` (default) | `max` + large max completion |
| Doubao | Lite/Mini model | consumer app / Pro model | deep-thinking Pro model | Coze / TRAE |
| Yuanbao | default engine | default + output contract | select deep-thinking engine | Not verified |
| Quark | AI search | AI chat/writing | deep thinking + academic search | Not verified |
| Meta AI | Instant | Thinking | Thinking + method block | standing tasks + connected apps |
| Dola / Nova(A) | short prompts | output contract + verification step | **not reliably achievable** | **not available** |

**Three rules that change the advice:**
1. **Defaults differ radically — establish the default before advising a change.** Kimi K3 defaults `max` (reduce, don't raise); DeepSeek defaults thinking on at `high`; Qwen3 commercial defaults thinking OFF while Qwen3.5/3.6/3.7 default ON; Claude and OpenAI default to a middle setting.
2. **Some platforms have no effort control at all** — Canva, Grammarly, Doubao, Dola, Nova. Express effort through model tier, surface choice, connected data and prompt structure instead.
3. **In-flight steering** (Meta AI real-time steering; ChatGPT mid-response plan adjustment) is often more efficient than raising effort — prefer it where available.

## 5. Preferred prompt structure per platform (craft natively)
| Platform | Structure | Examples? | Convention that matters |
|---|---|---|---|
| ChatGPT | Markdown sections + explicit output contract; JSON schema on API | helpful | **Don't prescribe intermediate steps** to reasoning models |
| Gemini | Clear instructions + few-shot examples + structured output | **always** (official) | Partial-input completion: start the output, let it continue |
| Claude | **XML tags** (`<instructions>`, `<context>`, `<documents>`, `<example>`) | 3–5 in `<example>` | Documents first, query last; quote-then-answer; positive framing; no prefill |
| Copilot | Plain prose + mode chosen BEFORE submitting | vendor examples | Decision-framed for Think Deeper; teach-me framing for Study |
| Canva | Goal + deliverable list + brand + source | — | Name every channel and format; one change at a time when editing |
| Grammarly | Short, effect-oriented | — | Configure Style Guide/Brand Tones instead of prompting |
| Qwen | Delimited sections | — | `/think` `/no_think` suffixes; most recent instruction wins |
| DeepSeek | Delimited sections; XML on Anthropic format | — | Style must be in the prompt — sampling params inert in thinking mode |
| Kimi | Stable long prefix first; strict JSON schema | — | Partial Mode as a format lock; omit sampling parameters |
| Doubao | Bilingual, delimited, verification steps | — | Model tier substitutes for effort |
| Yuanbao | Bilingual, quote-then-answer | — | Dual-engine comparison as a reliability check |
| Quark | Search-shaped: source class, dates, exclusions | — | Enable deep thinking BEFORE submitting |
| Meta AI | Artefact-named, lightly briefed | — | Brief lightly then steer live; `{{what}} + {{when}}` for standing tasks |
| Dola / Nova(A) | Everything in one message + method block | — | Prompt the underlying model's conventions, not the wrapper |

**Format quick key:** XML → Claude, DeepSeek(Anthropic format). Few-shot → Gemini. Markdown + output contract → ChatGPT, Meta AI, Copilot. JSON schema → any machine-consumed API. Bilingual + delimiters → Doubao, Yuanbao, Quark. Short and effect-shaped → Grammarly, voice surfaces.

## 6. The four blocks most often missing (add to almost every crafted prompt)
An **output contract**; **acceptance criteria**; **uncertainty handling** ("write 'not verified' rather than guessing"); and on any agentic surface a **prohibitions block** naming actions that require confirmation.

## 7. Time-sensitive items (verify via the live-status check — this file decays)
- OpenAI **o3 retires from ChatGPT 2026-08-26**; **ChatGPT Atlas shuts down 2026-08-09**.
- **Claude Sonnet 5** introductory pricing runs through **2026-08-31**.
- **DeepSeek** said it would update its V4-Pro effort-remapping table in **early August 2026** — treat that table as possibly superseded.
- The source research was verified 2026-08-06 and its authors state it decays on a weeks-to-months cadence. Model IDs, effort parameters and availability change; re-check before asserting.

## 8. Honesty rules carried from the source research
- Never present an **Inference** as vendor guidance — say it is a reasoned recommendation.
- Where evidence is missing, say *"not verified as of [date]"* — never invent a parameter, model ID, price, benchmark or "official recommendation".
- Evidence density is **uneven**: Tier 1 rests on first-party docs; Doubao/Yuanbao/Quark rest substantially on secondary reporting; Dola has almost no official documentation and Nova's identity is unresolved. Carry that unevenness into any recommendation.
- For **Nova**, ask which product the user means before crafting. For **Dola**, state that deep/agentic work is not reliably achievable.

## 9. Source register
| ID | Source | Date |
|---|---|---|
| G0 | Developer research base — Global AI Platforms & Prompting Surfaces, files 00–05 (15 platforms, 18 comparison tables, 58 templates) | verified 2026-08-06 |
| G1 | File 01 Frontier assistants (ChatGPT, Gemini, Claude) — first-party docs | 2026-08-06 |
| G2 | File 02 Productivity/creative (Copilot, Canva, Grammarly) | 2026-08-06 |
| G3 | File 03 Model/developer ecosystems (Qwen, DeepSeek, Kimi) — first-party docs | 2026-08-06 |
| G4 | File 04 Consumer/search (Doubao, Yuanbao, Quark) — substantially Secondary | 2026-08-06 |
| G5 | File 05 Mobile/social/personal (Meta AI, Dola, Nova) — sparse; Nova unresolved | 2026-08-06 |

## 10. Changelog
| Version | Date | Change |
|---|---|---|
| v1 | 2026-08-08 | Created from the developer's 6-file global platform research. Adds 13 platforms beyond Claude/OpenAI as tiered crafting targets, with the normalized effort framework, per-platform prompt structures, and the evidence-honesty rules preserved. |
