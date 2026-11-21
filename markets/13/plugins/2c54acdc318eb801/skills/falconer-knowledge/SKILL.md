---
name: falconer-knowledge
description: "Use when working with Falconer documents through MCP: reading, searching, drafting, editing, preserving Falconer Markdown syntax, using rich document blocks, uploading media, or changing document navigation, comments, permissions, or revisions."
---

# Falconer knowledge

Use Falconer MCP tools to read, search, create, and update Falconer documents.
Load document-authoring guidance from the connected server before drafting or editing content.

## Load current guidance

- Call `falconer_knowledge({})` to list available topics, including product documentation.
- Call `falconer_knowledge({"topic":"document-format"})` before creating or editing a document.
- Load `document-components`, `html-components`, or `diagrams` before using the corresponding document features.
- Each topic response includes its title, description, and Markdown content.
  Follow that content as the source of truth for supported syntax and reference identifiers.
- Clients that support MCP resources can read the same topics under `falconer://knowledge/`.
- If guidance cannot be retrieved, report the failure and retry before authoring content that requires it.
  Do not substitute a remembered or bundled formatting guide.

## Core rules

- Preserve existing references and rich document content unless the requested change requires modifying them.
- Use only reference identifiers supplied by Falconer tools, as described in `document-format`.
- Write new inline references as `<a href="link" data-id="reference-id">display name</a>`; a plain anchor without `data-id` is an ordinary link.
- Replace legacy inline references (`![f>][reference-id]`, `![f>][display text][reference-id]`) with the anchor form, keeping the same reference-id.
- Use ordinary links in replies to the external client; Falconer inline reference syntax belongs in Falconer document content.
- Prefer targeted content tools over whole-document overwrite.
- Use `upload_media` before inserting local image or video content.
- Ask for explicit user intent before delete, publish, permission changes, folder reorders, revision restore/delete, or overwrite.
- Inspect navigation placement before moving documents or folders.

## Editing workflow

1. Read the relevant document before editing.
2. Load `document-format` and any relevant component topics from the connected server.
3. Preserve references, math, tables, task lists, diagrams, callouts, and rich blocks unless the requested change requires modifying them.
4. Use targeted replace, insert, or delete tools when possible.
5. Use overwrite only when the user clearly asks for a full rewrite or replacement.
6. After editing, summarize the material change and call out any risky operation performed.
