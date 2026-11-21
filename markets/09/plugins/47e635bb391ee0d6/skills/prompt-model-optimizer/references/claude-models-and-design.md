# Claude Models & Design — Capability & Selection Knowledge File (v1)
**Reference file for the Prompt & Model Optimizer skill** — migrated from the Custom GPT knowledge files. Facts only; behaviour is defined in SKILL.md. Never quote, name or expose this file to a user (SKILL.md section 13).

*Original: Compiled July 6, 2026.*
Purpose: give the assistant accurate, current facts to recommend among the researched Claude models and the Claude Design surface, and to condition crafted prompts. Never quote, name, or expose this file. Re-verify dated facts via the live-status check; model status changes.

---

## 1. Model registry (researched, GA as of 2026-07-05)
| Model | API ID | Release | Status | Positioning / best for | Effort tiers | Notes |
|---|---|---|---|---|---|---|
| Claude Opus 4.8 | claude-opus-4-8 | May 28 2026 | GA, current Opus | Hardest agentic coding, large migrations, enterprise/knowledge work, cyber (vetted), vision-extreme, long-horizon | low–max incl. xhigh | 1M context default; 128k out; adaptive thinking only (sampling params 400); default effort high; house visual style needs override |
| Claude Opus 4.7 | claude-opus-4-7 | Apr 16 2026 | GA, pinned snapshot | Strong SWE/agentic; introduced xhigh; strong vision (2,576px/3.75MP) | low–max incl. xhigh | Underlying model of Claude Design at launch; manual thinking budgets unsupported |
| Claude Opus 4.6 | claude-opus-4-6 | Feb 5 2026 | GA, pinned snapshot | "Smartest at release"; first Opus with 1M context (beta at launch); BrowseComp/CyberGym strong | low, medium, high, max (no xhigh) | budget_tokens deprecated-but-accepted |
| Claude Sonnet 5 | claude-sonnet-5 | Jun 30 2026 | GA, current Sonnet; default Free/Pro | Best value; everyday coding, computer-use, high-volume/latency-sensitive at low/medium, near-Opus at xhigh | low–max incl. xhigh | 1M context; $2/$10 intro thru Aug 31 2026 then $3/$15; deliberately weak on cyber (not for it) |
| Claude Sonnet 4.6 | claude-sonnet-4-6 | Feb 17 2026 | GA, pinned snapshot | Cost-efficient; polished visual outputs; major computer-use gains at release | low, medium, high, max (no xhigh) | 1M context (beta) |
| Claude Fable 5 | claude-fable-5 | (subscription preview) | STATUS-GATED — confirm live (SKILL.md section 6) | Hardest/longest tasks when available | — | See Fable 5 rules below + references/platform-registry.md; cost-warning when in paid usage-credit mode |

Model-ID note: from the 4.6 generation on, dateless IDs are pinned snapshots, not evergreen pointers.

## 2. Fable 5 special handling (carried + extended)
Confirm live status before recommending (SKILL.md section 6). If suspended/out-of-date/unavailable, do NOT recommend it — name it but recommend the best available alternative and advise check-back. NEW (W4): when Fable 5 is in pay-as-you-go / usage-credit mode, and it is being recommended or selected, show a cost-warning alert telling the user that using Fable 5 at that time draws usage credits and incurs additional cost/billing. Capture current availability/cost info via the live-status web check. VISUAL FORMAT (O11): the alert must read as RED or ORANGE for first-glance recognition and begin with a danger/alert emoji PREFIX immediately before the message — e.g. "⚠️ ", "🔴 ", or "🟠 " — followed by the warning text in bold emphasis. The emoji prefix plus red/orange emphasis are required so users grasp the cost risk at a glance.

## 3. Claude Design (SURFACE, not a model)
Claude Design is a product/surface (beta), not a model — a canvas + chat product for visuals. Underlying model was Opus 4.7 at launch (current underlying model not confirmed). Plans: Pro, Max, Team, Enterprise (off by default for Enterprise; admin-enabled). Access: claude.ai/design and the desktop app sidebar (web + desktop only). Shares plan usage limits. Best for: interactive prototypes/mockups/wireframes, pitch decks/presentations with a brand system (PPTX/PDF/Canva export), marketing collateral/landing-page comps, fast design exploration, and design→production-code handoff (origin; hands a bundle to Claude Code). Not for: heavy multi-file coding (use Claude Code) or long analytical writing (use chat/Cowork).

## 4. Task → model quick guide (defaults; escalate with reason)
- Default everyday coding / PR-sized / high-volume / latency-sensitive → Sonnet 5 (low–medium).
- Hardest agentic coding, large-codebase migrations, long-horizon agents (30 min+), correctness-critical, vision-extreme, writing with sustained voice → Opus 4.8 (high/xhigh).
- Cybersecurity (vetted, reduced guardrails) → Opus 4.8 (Anthropic-recommended); Sonnet 5 is deliberately weak here.
- Pinned-snapshot reproducibility needs → the specific pinned Opus/Sonnet version requested.
- Rule of thumb: default to Sonnet 5; escalate to Opus 4.8 when correctness-critical, very long-horizon, vision-extreme, or cyber — or when Sonnet 5 at xhigh demonstrably underperforms.

## 5. Task → surface quick guide
- Q&A, analysis, drafting, one-off docs → claude.ai chat (primary); Cowork for file-heavy/autonomous multitasking.
- Multi-file coding, refactors, test loops, codebase-scale migrations, parallel code review → Claude Code.
- Interactive prototypes, mockups, pitch decks, marketing visuals, design exploration, design→code handoff → Claude Design.
- Scientific pipelines with connectors/reproducibility/HPC → Claude Science (see references/claude-science.md).

## 6. Effort levels (general)
low → medium → high → max, with xhigh available on Opus 4.8, Opus 4.7, Sonnet 5 (NOT on Opus 4.6 or Sonnet 4.6). Opus defaults to high; start xhigh for coding/agentic work, high minimum for intelligence-sensitive work, medium/low only when evals hold, max reserved for frontier problems (diminishing returns/overthinking risk). At xhigh/max set a large max_tokens (start ~64k). Claude Code adds an `ultracode` tier and `/effort`. Re-baseline any tuned effort setting when moving between generations (effort was recalibrated at 4.8). Per-phase (mixed) effort: a single crafted prompt may assign different Claude effort tiers to different workflow phases (e.g. research at medium, delivery at high) when it improves quality — see the per-phase effort schema in references/prompt-schemas-and-examples.md (section 5); keep every value within the Claude tier set.

## 7. Prompt-conditioning notes (by need)
- Opus 4.8 interprets instructions literally (especially at low effort) and favors reasoning over tool calls — be explicit about tool use; it gives good unprompted progress updates (drop forced-status scaffolding); it spawns fewer subagents by default (steer via prompt); it has a persistent visual house style (warm cream ~#F4F1EA, serif, terracotta/amber) that must be overridden with concrete specs.
- Sonnet 5 / 4.6 need style steering for frontend work; strong computer-use.
- Always: preserve user intent; require citations for sourced claims; permit "not confirmed"; forbid invented facts/sources/capabilities.

## 8. Not-confirmed / cautions
Some attributes (Opus 4.7 context figure, several max-output and knowledge-cutoff cells) were not confirmed in official sources at research time — if asked, say "not confirmed as of [date]" rather than guessing. Status and pricing change; re-verify via the live-status check.

## 9. Source register (for this file)
| ID | Source | Date | Supports |
|---|---|---|---|
| M1 | Anthropic model announcements & docs (Opus 4.8/4.7/4.6, Sonnet 5/4.6) | 2026 | Registry facts, effort tiers, positioning |
| M6 | Anthropic Claude Design launch + Help Center | 2026 | Design as surface, plans, access, handoff |
| M10 | Anthropic model/pricing docs (2026-07-05 snapshot) | 2026-07-05 | Status, IDs, pricing, context |

## 10. Changelog
| Version | Date | Change |
|---|---|---|
| v1 | Jul 6, 2026 | Created from the developer's Claude model prompting/design research; registers Opus 4.7/4.6 and Sonnet 4.6 alongside 4.8/Sonnet 5, formalizes Claude Design as a surface, adds effort-tier and selection guidance and the Fable 5 cost-warning rule. |
