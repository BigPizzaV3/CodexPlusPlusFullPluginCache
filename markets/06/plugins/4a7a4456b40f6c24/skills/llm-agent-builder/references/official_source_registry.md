# Official Source Registry

Use current primary documentation whenever an answer depends on SDK behavior, model/tool capabilities, MCP protocol details, guardrail behavior, pricing, limits, or deprecated features.

## OpenAI plugin packaging
- Build plugins: https://developers.openai.com/plugins/build/plugins
- Build skills: https://developers.openai.com/plugins/build/skills
- Submit plugins: https://developers.openai.com/plugins/deploy/submission
- Submission errors and limits: https://developers.openai.com/plugins/deploy/submission-errors

## OpenAI Agents SDK
- Overview: https://openai.github.io/openai-agents-python/
- Agents: https://openai.github.io/openai-agents-python/agents/
- Agent orchestration: https://openai.github.io/openai-agents-python/multi_agent/
- Handoffs: https://openai.github.io/openai-agents-python/handoffs/
- Guardrails: https://openai.github.io/openai-agents-python/guardrails/
- Tracing: https://openai.github.io/openai-agents-python/tracing/

Current guidance distinguishes direct Responses API usage from the Agents SDK:
- use direct model/Responses APIs when the application should own a small loop and tool dispatch;
- use an agent runtime when managed tool execution, guardrails, handoffs, sessions, tracing, or agent loops materially help.

## Model Context Protocol
- MCP specification and docs: https://modelcontextprotocol.io/
- TypeScript SDK v2: https://ts.sdk.modelcontextprotocol.io/v2/
- Tasks extension: https://tasks.extensions.modelcontextprotocol.io/

The current stable TypeScript SDK line implements the 2026-07-28 MCP specification. MCP evolves quickly; verify the current specification and host support before implementation.

## Security
- OpenAI agent safety guidance: https://developers.openai.com/api/docs/guides/agent-builder-safety
- OWASP GenAI Security Project: https://genai.owasp.org/

## Usage rule
Treat this file as a registry of primary sources, not frozen platform truth.
Verify the exact SDK/runtime/model/provider version named by the user before giving version-sensitive implementation guidance.
