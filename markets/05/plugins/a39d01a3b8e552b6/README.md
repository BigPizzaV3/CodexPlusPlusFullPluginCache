# Session Chronicle

Session Chronicle is a skill-only Codex plugin for turning event transcripts into faithful professional records. It contains four skills: `session-chronicle`, `session-publish`, `session-compare`, and `session-visuals`.

Version: 1.1.0

The publication package includes a transparent composer icon plus light- and dark-surface logo assets. No external service, authentication, app connector, or MCP server is required.

## Install

Add the unpacked plugin folder to a local Codex marketplace, then install `session-chronicle` from that marketplace. When iterating on an installed local copy, reinstall the plugin and start a new task so Codex loads the revised skills.

Before submitting it to a managed marketplace, replace the manifest's publisher identity with the publishing person or organization if required by that marketplace. Add homepage, repository, support, legal, or license metadata only when real URLs and ownership details are available.

## Quick tests

1. Paste a panel transcript with no instruction. Expect a detailed chronicle without intake questions.
2. Prefix a transcript with `OUTLINE`. Expect a structured outline rather than full prose.
3. Ask `SUMMARISE this for an executive audience`. Expect a concise, qualified summary.
4. Supply two transcripts and ask for convergence and divergence. Expect evidence-grounded comparison without invented contrasts.
5. Ask for a five-card carousel. Expect source-grounded panel copy or generated visuals, with no invented numbers or quotations.
6. Supply a reference for a dense one-page infographic. Expect its hierarchy and module rhythm to guide an original design, with editable deterministic text layout and image generation limited to supporting visuals.
7. Say `INFOGRAPHIC` after supplying a keynote, policy address, technical presentation, panel, or roundtable transcript. Expect a source-responsive architecture, verified source ledger, concise visual language, and direct generation when suitable rendering is available.
8. Combine `COMPARE → INFOGRAPHIC` or `PUBLISH → INFOGRAPHIC`. Expect the first command to determine the content basis and INFOGRAPHIC to determine the visual output.
