# Slideworks for Claude

Build consulting-grade, editable PowerPoint decks in Claude from Slideworks' curated layout library.
The plugin adds the Slideworks connector (`https://mcp.slideworks.io/mcp`) and a skill that guides
Claude from storyline to finished deck.

Requires a Slideworks account. You sign in at app.slideworks.io the first time Claude uses it.
Get access at [slideworks.io](https://slideworks.io).

## Install

In Claude: Customize → Plugins → Slideworks.

In Claude Code:

```
/plugin marketplace add slideworks-io/slideworks-plugin
/plugin install slideworks@slideworks
```

## Data

The slide content Claude writes is sent to Slideworks, which renders the deck. See the
[privacy policy](https://slideworks.io/privacy) and [terms](https://slideworks.io/terms).
Support: info@slideworks.io.
