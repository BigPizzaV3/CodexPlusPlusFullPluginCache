# Software, Data & AI Copilot Plugin

Version: 0.1.0

A skills-only, repository-first engineering copilot for software, data, and AI codebases.

## What it covers
- code understanding and debugging;
- focused implementation;
- code review and refactoring;
- testing strategy;
- safe API/schema/dependency/runtime migrations;
- data engineering and Spark/pipeline code;
- ML and LLM integrations;
- notebook-to-production hardening;
- security and compatibility checks.

## Architecture
```text
Software, Data & AI Copilot
└── software-data-ai-copilot skill
    ├── repository workflow
    ├── code review
    ├── implementation safety
    ├── testing strategy
    └── data & AI coding patterns
```

No MCP server is required for v0.1. The package cannot inspect repositories, run tests, edit files, or deploy code by itself unless the surrounding ChatGPT/Codex environment provides those capabilities.

## Recommended next step
Review the package, then upload the ZIP to the OpenAI plugin submission workflow or use `PLUGIN_CREATOR_PROMPT.md` with Plugin Creator.

This package has **not** been installed or created as a personal/public plugin.
