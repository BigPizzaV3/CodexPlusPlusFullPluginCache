# Migration record

Source: theaiqs-main (3).zip, Gather 0.16.0. Target: Gather 0.16.1.

| Source component | OpenAI edition |
|---|---|
| Claude manifest | Portable root manifest plus supported OpenAI compatibility manifest |
| 59 skills + nine agents | 66 workflows; red-team front door merged with its specialist |
| Agent model names and tool allowlists | Removed; host-selected model and discovered tool schemas |
| Claude root variables | Relative resource paths resolved from each document |
| Slash-command examples | Skill references and natural-language invocation |
| Shared folder inside skills | Root shared folder; references updated |
| Three post-tool hook checks | Explicit runtime checks and retained deterministic helpers; no automatic hooks installed |
| Desktop/cloud routines | Capability-aware OpenAI scheduling workflow; 26 templates retained |
| HTML reports | Standalone file output where supported; conversation fallback where execution is unavailable |
| OAuth fields in Claude config | Remote endpoint retained; authentication delegated to host/server discovery |
| Live connection registration | Must be completed with a real account-specific connection ID in ChatGPT |

The source had malformed YAML descriptions; metadata was normalised. Domain procedures, calculations, templates and source licence were retained. Contract and professional-standard content was not independently re-audited.

Not verified: Gather OAuth, live schemas/permissions, ChatGPT skill selection, each commercial workflow, host file rendering or scheduled execution. Static validation is not certification of commercial calculations or contract advice. See TEST_CASES.md for the bounded live checks.

Public candidate: removed development app mapping, normalised MCP result envelopes and nested form answers, and distinguish empty report schemas from usable schemas.
