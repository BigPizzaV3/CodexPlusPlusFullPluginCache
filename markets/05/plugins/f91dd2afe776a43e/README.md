# Sermon Scribe

Sermon Scribe is a skills-only plugin for faithfully handling sermons after they have been preached. It does not write new sermons, critique theology, or reinterpret the preacher's message.

## Why this name

**Sermon Scribe** describes the plugin's full role: receiving and faithfully carrying forward what was preached. **Sermon Chronicle** remains the name of its central reconstruction and publishing skill.

## Architecture

- `sermon-chronicle` reconstructs, expands, condenses, and prepares sermon records for publication.
- `sermon-translate` translates completed sermons while preserving theology, Scripture, voice, and reverence.
- `sermon-visuals` turns a source sermon into an editorial one-page infographic or a coherent image carousel. One-page designs use a dedicated editorial-poster guide; carousel behavior remains concise and card-based.
- `references/fidelity-and-style.md` holds the evidence, theology, quotation, and voice rules shared across the three skills.

The plugin has no app, MCP server, command dependency, or persistent persona. Skills are selected from the user's natural-language intent. Legacy words such as `WRITE`, `PUBLISH`, `TRANSLATE`, or `INFOGRAPHIC` can still express intent, but are never required.

## Example requests

- “Reconstruct these transcript files as a complete sermon narrative.”
- “Make this sermon record shorter while preserving its pastoral warmth.”
- “Prepare this sermon for our church website.”
- “Translate the completed sermon into Simplified Chinese for a Singapore church audience.”
- “Turn this sermon into a seven-card square carousel for WhatsApp.”
- “Create one reverent infographic with the Scripture, four key points, and central takeaway.”
- “@Sermon Scribe create one-page infographic from this sermon.”

If the source is insufficient for a requested claim, the skill identifies the gap instead of inventing content. The skills do not append menus or mandatory closing prompts.

## Version 1.1.0

One-page infographic requests now follow an explicit source-to-delivery workflow: source verification, exact-copy lock, original visual planning, deterministic text composition where available, rendered visual inspection, correction, and delivery of the finished image. The existing sermon fidelity, theological restraint, quotation, and Scripture safeguards remain authoritative.
