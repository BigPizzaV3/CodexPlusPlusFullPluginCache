# Personal Control Plane

A skills-only OpenAI plugin that makes ChatGPT act as a single conversational entry point for persistent personal/work state.

## Why skills-only first

The workflow can use tools/apps already available to the model. No custom MCP server is required until you need capabilities the existing tools cannot provide (for example, a unified private state store, reconciliation service, custom API, or bespoke permissions).

## Structure

```text
personal-control-plane/
├── .codex-plugin/
│   └── plugin.json
├── skills/
│   └── personal-control-plane/
│       ├── SKILL.md
│       └── references/
│           ├── routing-policy.md
│           ├── examples.md
│           └── quality-gates.md
├── SUBMISSION.md
└── README.md
```

## Local development / testing

OpenAI's current plugin packaging format requires `.codex-plugin/plugin.json`. A minimal skills-only plugin only needs that manifest plus the `skills/` tree.

For local/personal marketplace testing, use ChatGPT desktop/Codex plugin authoring flows and point the marketplace entry at this plugin folder. Current OpenAI documentation notes that local plugin authoring/testing surfaces can differ from ordinary Chat.

## Platform public submission

The OpenAI Platform submission portal supports **Skills only** submissions. Use `SUBMISSION.md` as the draft for listing copy, starter prompts, five positive tests, three negative tests, and release notes.

Public submission requires a verified developer/business identity and Apps Management write permission in the Platform organization. Publishing makes the plugin available through the universal Plugins Directory after review; it is not a private-personal deployment mechanism.

## Existing app assumptions

The skill conceptually routes to:

- Notion — durable knowledge
- TickTick — personal tasks/reminders
- Google Calendar — fixed-time events
- ChatGPT Automations — conditional/recurring monitoring
- Linear — shared team work
- Gmail — email
- Google Drive — files/docs
- Google Contacts — recipient/attendee resolution

The skill intentionally does not hard-code credentials or API identifiers. It uses whichever compatible tools are connected and available to the current ChatGPT environment. If a required capability is unavailable, it must not fabricate success or silently store data in the wrong system.

## Versioning

Start at `0.1.0`. Tune the skill description first when activation is wrong; tune the body/references when activation is correct but routing or output is inconsistent.
