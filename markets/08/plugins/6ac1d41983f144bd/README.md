# AISEO: AI SEO, AEO & GEO

AISEO connects ChatGPT and Codex to the AISEO Brand Monitor server.
The listing uses AISEO: AI SEO, AEO & GEO as its public name.
It connects visibility checks with content creation and optimization workflow discovery.

## Tools

- `check_ai_visibility` checks public AI mentions for a supplied brand or domain.
- `list_playbooks` lists AISEO search optimization workflows and their required inputs.
- `describe_playbook` explains one workflow's inputs.

The server requires no authentication.
Workflow execution, ongoing tracking, and competitor benchmarking use the AISEO dashboard.

## Content workflows

Content Create helps users create researched articles from a target keyword.
Content Optimizer improves an existing file or page for search engines and AI answers.
The plugin explains these workflows and helps users gather their inputs.
Users run content creation and optimization in the AISEO dashboard.

## Package

- `.codex-plugin/plugin.json` contains listing metadata and proposed review cases.
- `.mcp.json` points to the hosted Brand Monitor server.
- `assets/icon.svg` contains a square visibility icon.

## Review preparation

The package includes five positive cases and three negative cases.
These cases describe expected behavior; they do not certify completed review testing.
Before submission, run every case and record a walkthrough with an accessible video URL.
Add that URL through the dashboard or the documented `review.demo_recording_url` field.

The existing OpenAI plugin uses the same MCP URL.
Its package name is `app-6aa8f833bc3c8191806484ce7eec22a3`.
Update that draft when preparing submission.

Submission guide: https://developers.openai.com/plugins/deploy/submission
