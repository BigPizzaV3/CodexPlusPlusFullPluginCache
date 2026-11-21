---
name: publish
description: Publish an existing Maker website or provide its live link and embed codes, following the project's publication confirmation and propagation status.
---

# Publish a Maker website

Resolve the user's project from `list_projects` when its identifier is unknown. For a request for an already published link or embed code, call `get_embed_codes` and report the returned state.

For a publication request, call `publish_project` without a confirmation token. Follow the returned pre-publish review and confirmation steps. Show the confirmation summary and wait for the user's fresh explicit approval before sending the returned token. This approval concerns the artifact described by that quote; if files changed and the tool requests a new quote, repeat the confirmation for the current artifact.

When the publish result reports pending propagation, use `check_publish` with the returned project and version. Report pending or failed deployment accurately and share the live URL once the tools report successful publication.

Example: “Publish my landing page” starts the quote. A subsequent “Yes, publish that version” approves the quoted version. A preview link alone does not establish successful publication.
