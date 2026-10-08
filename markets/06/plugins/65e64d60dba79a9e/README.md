# Technical Interview Copilot Plugin

Version: **0.1.0**

This is a **skills-only** plugin for ChatGPT and Codex. It intentionally has no MCP server, app connection, hooks, or custom network dependency in v0.1.0.

## Why skills-only first

Technical Interview Copilot is primarily a reusable reasoning and coaching workflow. Its core job is to interpret a candidate profile and job description, route to the right interview domains, teach at the right depth, run realistic practice, and give evidence-grounded feedback. None of that requires a custom external service.

Add MCP later only when the product needs a service that the plugin itself must own, such as persistent candidate profiles, a custom interview-question database, coding sandbox execution, proprietary assessment data, or another controlled external action.

## Package structure

```text
technical-interview-copilot-plugin/
├── plugin.json
├── skills/
│   └── technical-interview-copilot/
│       ├── SKILL.md
│       └── references/
│           ├── interview_role_taxonomy.md
│           ├── technical_interview_frameworks.md
│           ├── behavioral_experience_deep_dive.md
│           └── interview_preparation_playbooks.md
├── submission/
│   ├── listing-and-prompts.md
│   ├── test-cases.md
│   └── public-submission-checklist.md
└── PLUGIN_CREATOR_PROMPT.md
```

## Local testing path

1. Open ChatGPT **Work** mode.
2. Invoke `@plugin-creator`.
3. Attach this plugin folder/ZIP and paste the prompt from `PLUGIN_CREATOR_PROMPT.md`.
4. Ask Plugin Creator to create a **personal marketplace entry** for local testing.
5. Refresh the Plugins Directory if needed and install the local plugin.
6. Test direct and indirect activation, incomplete inputs, and non-interview requests.

The package uses the current portable Agent Plugins layout with a root `plugin.json`. Plugin Creator may add a `.codex-plugin/plugin.json` compatibility manifest or local marketplace metadata for the current host.

## Public submission path

When local testing is solid:

1. Open the OpenAI plugin submission portal.
2. Choose **Skills only**.
3. Use the final skill bundle from this package.
4. Complete publisher identity verification and listing information.
5. Add up to three starter prompts.
6. Add exactly five positive and three negative test cases.
7. Choose supported countries/regions and complete policy attestations.
8. Submit for review. After approval, publish from the portal.

## Important publishing note

`developerName` is currently set to **Krishna Sathvik**. Before public submission, make sure it exactly matches the verified developer or business identity you intend to publish under. Change it if your verified identity uses a different name.
