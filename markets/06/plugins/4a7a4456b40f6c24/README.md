# LLM & Agent Builder Copilot Plugin

Version: 0.1.0

A skills-only copilot for designing reliable LLM applications, tool-using workflows, MCP integrations, agent systems, state, guardrails, approvals, evaluation, and observability.

## Architecture

```text
LLM & Agent Builder Copilot
└── llm-agent-builder
    ├── LLM system patterns
    ├── agent design patterns
    ├── tool contracts
    ├── MCP design
    ├── state and memory
    └── evaluation framework
```

No MCP server is required for v0.1.

This plugin can **design** MCP/agent architectures but cannot itself call external tools, deploy agents, or modify external systems without future integrations.

## Package structure

```text
plugin.json
assets/
  icon.svg
  logo.svg
skills/
  llm-agent-builder/
    SKILL.md
    agents/
      openai.yaml
    assets/
      icon.svg
    references/
      llm_system_patterns.md
      agent_design_patterns.md
      tool_contract_patterns.md
      mcp_design_reference.md
      agent_state_memory_patterns.md
      llm_agent_evaluation_framework.md
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

Review the package and upload it to the OpenAI plugin workflow only when ready.

This package has deliberately **not** been created, installed, or submitted as a plugin.
