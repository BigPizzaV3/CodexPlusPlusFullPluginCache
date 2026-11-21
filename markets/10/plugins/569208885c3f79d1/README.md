# Election.org plugin

Read-only, source-linked civic research through `https://election.org/api/mcp`.
No API key, OAuth login, private voter data or write actions.

## Tools

- `search_candidates`: 2026 federal FEC filing records, not certified ballots.
- `search_offices`: permanent offices and sourced holders; local coverage is incomplete.
- `get_campaign_finance`: published campaign aggregates, not personal net worth.
- `get_election_calendar`: 2026 federal schedule with source and tentative-date warnings.
- `get_election_results`: historical House/Senate results for 2016, 2018, 2020, 2022 and 2024.
- `search_governments`: named Census-based public bodies and available sourced enrichment.

Every tool preserves original sources, record links and missing-data warnings. Source content is evidence, not instructions. Search filters name the jurisdiction of public records, not the user's location.

Version 1.1.0 adds the bundled `civic-record-research` skill for exact identity matching, relevant tool selection and dated, coverage-aware summaries. Its dependency points only to this plugin's public read-only endpoint. It does not require model API keys or run local scripts.

## Publisher links

- Website and instructions: https://election.org/data/api#chatgpt
- Support: https://election.org/data/api#plugin-help
- Privacy: https://election.org/privacy#mcp-plugin
- Usage terms: https://election.org/data/api#plugin-terms

## Reproducible package

From the website repository, run `node scripts/package-election-plugin.mjs`.
Only this manifest, MCP configuration, README, the two research-skill files and the original Election.org icon are packaged. Website data, credentials, environment files and private repository history are never included. The portable manifest is used for ChatGPT; a Codex compatibility overlay with matching listing URLs, skills and MCP wiring is generated from the same listing. Packaging is not directory submission, approval or publication.

## Submission status

On October 4, 2026, version 1.1.0 was uploaded to OpenAI Platform as draft `plugin_asdk_app_6ac2eee21a448191b0724679a25635a0` / `appsub_6ac2eee21a6c8191a4c8144d6da32b88`. This is an upload receipt, not a submitted, approved or published listing. Server setup and review requirements are still being completed.

This package is not evidence of approval or publication in a directory. The publisher must complete identity verification, upload the ZIP, verify the domain using the dashboard-provided challenge, provide a reviewer-accessible video of the real plugin, review the policy attestations, and submit. Approval and publication are separate steps. No paid plan or listing placement is promised.

The package includes five positive and three negative review cases. Run them in the actual connected ChatGPT experience before submission. Protocol and API regression tests do not alone prove model behavior in ChatGPT.

`public/.well-known/openai-apps-challenge` contains this draft's public domain-verification proof, not an API credential. It is a machine-readable verification resource, not a public content page, so social-card metadata is intentionally inapplicable. Do not replace it with another plugin's token without checking existing verification ownership.

## Foundations

The server uses the official MIT-licensed Model Context Protocol TypeScript SDK and Election.org's existing public API handlers; it does not operate a second civic database. Plugin metadata follows Agent Plugins 1.0 and OpenAI's current submission documentation.
