---
name: vana-create
description: Create or revise a saved protocol. Use when the user wants a repeatable plan or asks to change one.
---

# Protocol author

This skill owns protocol content. Use `/vana-run` to continue the protocol, record progress, or review what has happened.

Reference files:

- [Protocol spec](references/protocol-spec.md): the required section shape, the style rules, and an example of the density to match.
- [Question strategy](references/question-strategy.md): when a prompt is too thin to draft, when a rich brief can draft immediately, and how to fill leftover gaps.

Workflow:

1. Judge how much detail the user gave. Follow the question strategy. Ask about missing details only when the answer would change the protocol.
2. Use external sources only when the request depends on them.
3. Draft one content-only Markdown protocol per the protocol spec.
4. Check every section and rule in the protocol spec. Fix each problem before you save. Ask one targeted question when a missing fact blocks a complete draft.
5. Save the protocol to `protocols/<slug>/protocol.md` in the user's Data, with a short kebab-case slug. The user's Data is behind the Vana MCP server. Save with its `write_file` tool. A revision replaces the same file.
6. After `write_file` succeeds, keep the usual concise summary and link the user to the full protocol. Build the link by adding `https://vana.so` before the returned `publicPath`. Say whether you created or updated it, for example: `I created your protocol. [Open it on VANA](https://vana.so/p/<protocol-id>).`
