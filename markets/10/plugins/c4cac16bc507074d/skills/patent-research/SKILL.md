---
name: patent-research
description: Use Clerq when the user wants patent prior-art research, similar-patent discovery, patent-document lookup, or patentability triage.
---

# Clerq patent research

Use the Clerq MCP server for patent research tasks.

## Workflows

- For an invention, technical concept, or problem description, use semantic patent search. Describe the subject matter naturally rather than constructing Boolean or keyword syntax.
- For a known patent, use similar-patent discovery with its publication, application, or grant number.
- For document analysis, retrieve only the patent fields needed for the current task. Request claims or descriptions only when the user actually needs full-text analysis.
- For patentability triage, explain that the workflow is asynchronous. Starting triage consumes the account's configured Clerq triage credit. After starting it, return the workflow ID and do not immediately poll in the same turn. In a later turn, follow Clerq's returned polling instructions and retrieve only the requested result sections.

## Guardrails

- Do not present research results as legal advice or guarantee patentability, validity, infringement outcomes, or grant of a patent.
- Do not invent patent records, tool results, or completed triage results.
- Do not use patent-research tools for unrelated tasks.
- For side-effecting or billable operations, make the user-visible consequence clear before initiating them when required by the host.
