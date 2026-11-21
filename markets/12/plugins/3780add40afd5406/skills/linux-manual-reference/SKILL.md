---
name: linux-manual-reference
description: Use when the user needs authoritative or version-specific Linux command, system call, library, file-format, configuration, or administration documentation from manual pages.
---

# Linux manual reference

Use the manpage.ai tools to ground answers in indexed Linux manual pages and
their exact package provenance.

## Choose a tool

- Use `get_manual` when the user names a command or manual and wants its
  behavior, syntax, options, files, exit status, or examples explained.
- Use `search` when the user describes a topic, flag, error, capability, or
  phrase but does not know the relevant manual name. Use `manual_name` without
  `query` to find name and alias matches or to page through alternatives.
- Use `get_targets` before adding a distribution, release, repository, or
  architecture filter whose exact indexed value is not already known.

## Preserve scope and provenance

- Carry every distribution, release, repository, architecture, package,
  package-version, section, and locale constraint the user supplies into the
  tool call. Filters are exact and case-sensitive.
- Do not silently broaden an explicit scope. If it has no match, say so and
  offer an available scope or an unfiltered lookup.
- When scope is omitted, explain any meaningful distro or package selection
  using the provenance returned by the tool.
- Treat a returned manual as version-specific evidence, not as a claim that
  every Linux distribution or software version behaves identically.

## Retrieve efficiently

- Start with a small search result limit and increase it only when needed.
- When following `next_cursor`, repeat the same search arguments and change
  only `cursor`.
- Prefer section `1` for user commands and section `8` for administration only
  when the user's request or ambiguity makes that distinction relevant.
- For punctuation-only manual names such as `[`, pass the literal name to
  `get_manual`.

## Answer clearly

Summarize the relevant manual text instead of reproducing an entire manual.
Name the distribution, release, package, and version when they materially
affect the answer. Distinguish facts supported by the retrieved manual from
general guidance or inference.
