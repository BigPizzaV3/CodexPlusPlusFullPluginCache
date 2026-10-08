# Production RAG & GenAI Copilot Plugin

Version: 0.1.0

A skills-only, production-focused copilot for RAG architecture, debugging, evaluation, security, observability, latency, cost, and grounded-generation reliability.

## Architecture

```text
Production RAG & GenAI Copilot
└── production-rag-genai-copilot skill
    ├── RAG architecture
    ├── debugging playbooks
    ├── evaluation framework
    ├── security guardrails
    └── observability / latency / cost
```

No MCP server is required for v0.1.

This package cannot inspect live vector stores, execute retrieval queries, run eval jobs, or modify production systems by itself.

## Package structure

```text
plugin.json
assets/
  icon.svg
  logo.svg
skills/
  production-rag-genai-copilot/
    SKILL.md
    agents/
      openai.yaml
    assets/
      icon.svg
    references/
      rag_architecture_patterns.md
      rag_debugging_playbooks.md
      rag_evaluation_framework.md
      rag_security_guardrails.md
      rag_observability_latency_cost.md
      official_source_registry.md
submission/
  listing-and-prompts.md
  test-cases.md
  public-submission-checklist.md
  release-notes.md
docs/
  RESEARCH_NOTES.md
PLUGIN_CREATOR_PROMPT.md
README.md
```

## Recommended next step

Review the package and upload the ZIP through the OpenAI plugin submission workflow when ready.

This package has deliberately **not** been created, installed, or submitted as a plugin.
