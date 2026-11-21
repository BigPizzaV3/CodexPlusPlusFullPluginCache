---
name: pixverse-video-script
description: "Video script and YouTube copy: write the full spoken body with a clear hook, scene beats, visual cues and a usable ending. Script-only work needs no media generation."
---

# Write Video Scripts

## Execution Surface

Read `../../skills-shared/execution-surface.md` before execution. Prefer a usable managed CLI; local execution follows `../../skills-shared/cli-workflow.md`.
In MCP mode, read `../../skills-shared/mcp-workflow.md` and follow the MCP scope below.
Do not execute the local setup, queue, filesystem, QA or finishing instructions below in MCP mode.
Script-only work needs no login or tools.

### MCP Scope

Write the complete editable script, dialogue, narration, hooks and scene cues in chat. No account or media calls. A script does not authorize generation or finishing.

Deliver the complete spoken body and ending, not only an outline unless requested. Separate narration from visual suggestions. Preserve the requested language and use sources for factual claims. Mark estimated duration as an estimate. Avoid fabricated quotes, testimonials or unsupported claims. Do not require account login, tools or media generation for script-only work.

When the user also requests media, activate the matching image, video or audio Skill after the script is ready.

# Video Scripts


## Shape The Argument Or Story

Establish audience, desired duration, central question and available evidence. Infer the tone from the brief; a practical tutorial, personal commentary and historical documentary need different language.

Choose the structure that serves the subject:

- Explanation: question, concrete example, mechanism, implication.
- Review: use context, observed evidence, trade-offs, who it suits.
- Commentary: position, reasons, strongest objection, conclusion.
- Documentary/history: sourced event, cause, turning point, consequence; distinguish reconstruction from fact.
- Creator ad: need, visible product proof, practical demonstration, appropriate invitation.
- Narrative: a character wants something, faces an obstacle and makes a consequential choice.

Use sources for factual claims. Avoid fabricated quotations, testimonials, personal experience and unsupported health or performance claims. Keep provisional facts out of finished sales copy.

## Write The Full Body

Write the opening, all spoken sections and the ending. Use contractions or conversational phrasing appropriate to the requested language. Give transitions enough context to be spoken naturally. Maintain a pronunciation list for names, brands and mixed-language terms.

Separate spoken text from visual intentions and source notes. A visual intention states what the viewer must understand; it need not dictate a lens for every sentence. Estimate duration from language and delivery, then label the estimate; actual recording or TTS will set timing.

## Hand Off

For script-only work, deliver the complete editable text and unresolved factual questions. For production, the parent workflow uses this text as its canonical spoken source. Do not add image/video tasks or ask for account login to finish a script.

## Execution

Read `../../skills-shared/production-brief.md` for reference roles, prompt construction and revisions.
For media execution, follow `../../skills-shared/cli-workflow.md`; load the gateway before manual
CLI commands or queue specs. Resolve the plugin root from this skill's installed path:
set `PIXVERSE_RUNTIME="<absolute-plugin-root>/scripts/pixverse-runtime"` and invoke `"${PIXVERSE_RUNTIME}"` with the documented arguments.
Prompt-only work ends with the usable plan and prompts; it needs no account or generation calls.