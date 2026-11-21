# Template inspection and Robotics product separation

On November 8, 2026, the existing authenticated OpenAI plugins dashboard showed RQM Technologies' Resonant Quantum Mechanics **0.5.9** as configured, authorized, domain-verified, in review and unpublished. No Robotics Lab entry was visible in that selected dashboard. This is a scoped observation, not a claim about every organization or project.

The current RQM release ZIP was downloaded read-only from its version menu. SHA-256: `bc9c76402b17a94331d6380a2e4ff40d3a0ce23c90e596093b34088371b445e5`. Its root manifest, portable streamable-HTTP MCP configuration, onboarding skill, publisher/legal fields, five positive and three negative review cases, notices and artwork layout supplied the structural template.

| Field           | Existing RQM template            | New Robotics package                  |
| --------------- | -------------------------------- | ------------------------------------- |
| Identity        | resonant-quantum-mechanics 0.5.9 | robotics-lab 0.1.0                    |
| MCP audience    | /mcp/plugins/quantum             | /mcp/plugins/robotics-lab             |
| Product         | rqm-studio                       | robotics                              |
| Capability      | Quantum service inventory        | One cuRobo v0.8 Panda planner         |
| Artwork         | Quantum image                    | Approved Robotics gimbal              |
| Review evidence | Historical RQM evidence          | Draft Robotics cases; not replayed    |
| Registration    | Existing RQM app                 | No app registration copied or created |

The new package has its own MCP key, identity, skill, prompts and cases. It copies no RQM app identifier, OAuth client credential, authorization token, reviewer connection or demo recording. The generic Apache license text and same-company legal URLs are retained. Runtime NVIDIA code is not shipped in the connector ZIP.

The legacy `/mcp/plugins/robotics` portfolio remains separate. Core preserves existing identities and maps the new exact audience to the common Robotics financial product. No quantum listing or review is changed.

Official package references: [Build plugins](https://developers.openai.com/plugins/build/plugins) and [Submission](https://developers.openai.com/plugins/deploy/submission). This archive is prepared for private testing; publishing and review submission remain separate from source and ZIP generation.
