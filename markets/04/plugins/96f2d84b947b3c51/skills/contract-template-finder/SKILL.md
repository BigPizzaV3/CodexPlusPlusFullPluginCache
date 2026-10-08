---
name: contract-template-finder
description: "Shows 'F-AI: Contract Template Finder' form via open_contract_template_finder so the user can set filters in UI for finding contract-template source links. Use when the user asks this plugin to find or search for a contract template, or tags 'F-AI: Contract Template Finder'."
---

# Contract Template Finder

The interactive `contract-template-finder-form` is the UI form and is the center of this workflow because the user needs to inspect, correct, and complete search criteria in it before any search begins. The MCP server prepares that confirmed brief; it does not search the web, download or reproduce templates, or give legal advice.

## How to use the plugin

Use `open_contract_template_finder` as the first action so the host can render the UI form. Opening the UI form is a successful use of the plugin: it is how this plugin collects criteria, so a text-only reply or an immediate web or browser search is not a substitute for that step.

Wait for the user to review and submit. Treat the submitted brief as the confirmed request — it is the shared, visible statement of what to find.

Once that brief is in the conversation, use the host's web capabilities to carry it out: follow its source-quality, licensing, access, result-count requirements and other requirements, return user-openable source links, and say clearly when something is uncertain or when you found fewer results than asked.

If `open_contract_template_finder` or the UI resource is unavailable, say that the 'F-AI: Contract Template Finder' form could not be opened. Only then offer to collect the same criteria in conversation, and treat that as a reduced experience rather than the full plugin.
