# CertArc plugin

This package connects to the read-only CertArc MCP endpoint (`https://certarc.com/mcp`); Claude connects to `https://certarc.com/mcp/claude` (CR-629). It is listed in ChatGPT’s plugin directory as [CertArc](https://chatgpt.com/plugins/plugin_asdk_app_6ac10753370881918540799af4b9e5d7) (published 2026-10-20). Release and submission steps are in [the runbook](../../docs/runbooks/agent-integration.md).

The package includes the portable Agent Plugins manifest and Streamable HTTP configuration, plus the Codex compatibility files. Both manifests carry the same listing text (CR-552). No credentials are bundled. Connections use OAuth with a CertArc-registered public client, an exact HTTPS callback and S256 PKCE; dynamic client registration is not implemented.

## Setup

After install, the `setup` skill (`skills/setup/SKILL.md`, CR-578) asks which certification the learner is preparing for and offers a first practice question.

## Tools

No account needed:

- `practice_question` and `check_practice_answer`: CertArc's public practice set, 10 questions per certification that has one. Results show the correct option and an explanation for every option. Nothing is recorded.
- `get_exam_domains`: exam domains and weights, with links to public guides and the public practice set.
- `search_learning_resources`: published CertArc guide links. With a connection, it uses the learner's latest certification.

With a CertArc connection (read-only, covering every certification the learner studies; the latest studied is the default):

- `open_study_panel`: the study overview and the full-screen app (Readiness, Patterns, Results).
- `get_readiness`, `get_study_patterns`, `get_results`, `get_result_review`: the dashboard's readiness, patterns, pace, knowledge areas and results, from CertArc's own calculations.
- `get_study_summary`, `get_study_plan`, `get_next_study_action`: progress, the live calendar, access and the next study option.

The plugin never shows the learner's own question text, options or answer keys. It does not handle payments, change plans or finish sessions, and it never reads another learner. Missing evidence is unknown, never zero. Certification names in the tool metadata come from CertArc's program catalog.

## Submission

OpenAI review comes after the private connection is working. It needs:

- publisher verification;
- the domain challenge;
- a dedicated reviewer account;
- at least five positive and three negative test cases;
- a walkthrough.

Category and listing fields are confirmed in the portal at submission.

Sources: [OpenAI packaging](https://developers.openai.com/plugins/build/plugins), [private testing](https://developers.openai.com/plugins/deploy/connect-chatgpt), [submission](https://developers.openai.com/plugins/deploy/submission), [guidelines](https://developers.openai.com/plugins/plugin-guidelines). Checked October 3, 2026.
