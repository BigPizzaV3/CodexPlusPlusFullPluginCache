# SS33 Skill Store for agents

Search about 60,000 agent skills in the [SS33 Skill Store](https://ss33.ai/skills)
and follow the one that fits the task. A skill is a step-by-step procedure
written by practitioners and organisations: the rules, numbers and common
mistakes for a job, from legal and finance to healthcare admin, trades, home,
data, security and software. Hundreds are Verified: tested on blind questions,
where the skill measurably improved the model's answers.

This plugin gives your agent the store's three tools and a skill that tells
it when and how to use them:

- **Search the skill store:** describe a task in a sentence; get the closest
  skills and why each matched, or a plain "nothing fits".
- **Get skill:** the skill's SKILL.md and its supporting files.
- **Report skill outcome:** whether the skill helped, which feeds its rating.

No account or sign-in is needed.

## Install

### Claude Code

```
/plugin marketplace add afterpartyai/ss33-skill-store-for-agents
/plugin install ss33-skill-store-for-agents@ss33
```

### Claude (claude.ai and the desktop app)

Find **SS33 Skill Store** in the Claude connector directory, or add
`https://mcp.ss33.ai/claude` as a custom connector.

### ChatGPT and Codex

Find **SS33 Skill Store** in the plugin directory, or in Developer Mode add
`https://mcp.ss33.ai/chatgpt` as a custom connector.

### Any other MCP client

Use `https://mcp.ss33.ai/mcp` (streamable HTTP). Set-up steps for 13 coding
agents are at [ss33.ai/skills/mcp](https://ss33.ai/skills/mcp).

## What's in this repo

| Path | For |
|---|---|
| `skills/ss33-skill-store/SKILL.md` | The skill: when to search the store and how to use what comes back |
| `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json` | Claude Code |
| `plugin.json`, `mcp.json` | OpenAI (ChatGPT and Codex) and other clients using the [agent-plugins](https://agent-plugins.org) format |
| `assets/` | Icons |
| `scripts/build_openai_zip.py` | Builds the ZIP for OpenAI's plugin directory |

## Privacy

Searches send a short description of the task, never your conversation.
See the [privacy policy](https://ss33.ai/skills/privacy) and
[terms](https://ss33.ai/skills/terms).

## Licence

MIT. The skills in the store keep their own authors' licences.
