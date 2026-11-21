---
name: pixverse-ugc-video
description: "Desktop CLI required; unavailable in MCP-only sessions. UGC ad: create a creator-led or product-led social ad, with a clear hook, believable demonstration and measured spoken delivery."
---

# UGC Videos

## Execution Surface

Read `../../skills-shared/execution-surface.md` before execution. Prefer a usable managed CLI; local execution follows `../../skills-shared/cli-workflow.md`.
**Desktop required: do not activate this production skill in MCP mode.**
Stop before setup, generation or local production. Recommend [ChatGPT desktop](https://chatgpt.com/download/) with this plugin and a supported local executor. A reduced deliverable requires explicit user acceptance and a supported Skill.

## Installed Command

Before running helper commands, resolve the absolute plugin root from this `./SKILL.md` path: it is two directories above this skill directory and contains `scripts/pixverse-runtime`. In every new shell session, set:

```bash
PIXVERSE_RUNTIME="<absolute-plugin-root>/scripts/pixverse-runtime"
```

Run helper commands through `"${PIXVERSE_RUNTIME}"`. Do not assume the user's current working directory is the plugin checkout, and do not bypass the installed wrapper with a module invocation.

## CLI Execution

Apply `../../skills-shared/quality-policy.md` to all generated images/videos: Sunburst 2K/high,
Seedance 2.5 1080p with automatic prompt enhancement, and an explicit upgrade/fallback
choice for Free/Basic or model-entitlement rejection.

For an explicitly selected Canvas project or node, read
`../../skills-internal/pixverse-agent-canvas/SKILL.md` first and follow its Canvas
preflight and delivery contract; the ordinary queue/local route below does not replace it.

For ordinary creation or editing, read `../../skills-shared/cli-workflow.md` before
executing this workflow. It contains the existing account-aware routing, paid-work
confirmation, progress, preview and project-handoff rules. Studio and Production are
not prerequisites. The shared account, confirmation and direct-medium rules govern the
examples and defaults below. Read the gateway only when writing manual CLI commands or queue specs.
Creation command examples below are queue-task fragments, not permission to submit paid
`pixverse create` commands directly.

## Select And Read The Full Recipe

| Intent | Required reading | Production structure |
| --- | --- | --- |
| Product hero, casual UGC, off-screen voice; no speaking face | `./references/product-demo.md` | Four panels/cuts: intro, two distinct demonstrations, result |
| Visible creator review, topic, routine or story | `./references/creator-story.md` | Eight panels/cuts; story arc, native performed speech, optional product |
| Explicit silent single product beat | `../pixverse-create-video/SKILL.md` or `../pixverse-product-video/SKILL.md` | Follow that direct brief |

Read the selected reference and `../../skills-shared/ugc-production.md` before writing
boards or prompts. Their cut counts, time budgets, mandatory board refinement, reference
order, hand/prop rules and speech contract are required parts of these named recipes.
Generic short-video simplicity does not remove them. Explicit user shot lists and tone
choices override defaults. Preserve no-face intent and accepted identities.

For product mode, use four distinct physical events and native off-screen VO; auxiliary
people remain silent. For creator mode, a productless topic/routine/story is a complete
supported mode: omit product references instead of inventing a brand or sales prop.
An open brief needs a story, not eight repeated product poses. Do not invent purchases,
customer testimonials, clinical outcomes or unsupported measurable benefits.

Split longer work into 4-15s clips using the shared duration rule. Build and refine boards
sequentially, then write all motion prompts with full numbered cuts and exact dialogue.
No default extra hook variants, music, external TTS or additional posts. Series intent is
different from one multi-board video.

## Related Deliverables

- Wearing or fit: `../pixverse-fashion-video/SKILL.md`
- Package opening and reveal: `../pixverse-unbox-video/SKILL.md`
- A repeatable physical procedure: `../pixverse-howto-video/SKILL.md`
- Independent edits of an existing ad: `../pixverse-ad-variants/SKILL.md`
- Deliberately art-directed brand film: `../pixverse-product-video/SKILL.md`

## Finish And Revise

Watch the complete action. Check that the visible proof supports the spoken claim, the item remains the same, contact is plausible and dialogue is intelligible. Listen to native audio before replacing it. Deliver the completed clip with requested exact overlays. Preserve accepted shots; fix only the failed action, spoken take or local layout.

For prompt-only work, deliver the complete board plan, refinement prompt, all four or eight timed motion sections, exact speech and reference roles without account or generation calls. Do not describe planned control assets as generated.