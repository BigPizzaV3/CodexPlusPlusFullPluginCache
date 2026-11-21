# Sigil ChatGPT plugin

The package source is in this folder. Zip plugin.json, mcp.json, skills/ and assets/ at the ZIP root, then upload to the existing OpenAI plugin.

The profile icon preserves the approved blue square and white mark with padding
for circular and rounded-square crops. Its editable layout is
`../storefront/public/profile-icon.svg`. Rasterize that SVG at 512px and copy the
same PNG to `assets/profile-icon.png` and `../storefront/public/profile-icon.png`.
Inspect both crop shapes at 32px and 48px. Keep the tightly framed favicon separate
from profile artwork. An in-review package keeps its submitted icon until OpenAI
allows another package update; do not cancel review for this asset change.

The reviewer video URL is recorded in `plugin.json` as `demo_recording_url`. It shows recorded public MCP requests and outputs, not the ChatGPT interface. Timing is edited. Its source, evidence and critiques are in the local Launch video lab, artifacts/plugin-review-2026-10-04. The video manifest records hashes and format.

OpenAI validates domain ownership through the storefront's public/.well-known/openai-apps-challenge file. Keep existing plugin identities and verification tokens. The tools provide brand reviews. They do not generate logos or complete brand briefs, or expose customer accounts. Portal submission and approval are separate from deployment.

## Claude directory

On October 15, 2026, the operator checked the existing [Sigil submission](https://claude.ai/directory/manage/sigil-brand-design-agency).
The product icon already used `https://sigil.auto-units.com/icon.svg`, and the
submission was **Published**. No change was necessary. The execution receipt
remains outside the repository at `/tmp/claude-submission-icon-review-20261015.json`.

## Website and tool terminology

The source package uses “brand review” for the free critique and keeps
`start_read` and `check_read` as stable tool names. The paid brand brief remains a
website offer; the plugin does not create or sell it.

Deploying the storefront updates the MCP tool descriptions, `llms.txt` and the
public server card. Installed and submitted plugin packages need the updated ZIP
from this directory. A deployment does not update a directory’s saved listing or
establish that a package is published. Preserve existing submission identities
and review state when applying this copy update.
