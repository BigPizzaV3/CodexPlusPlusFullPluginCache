# Job Outreach Copilot Plugin

## What this is

A skills-only OpenAI plugin for job-opportunity triage and recruiter/outreach communication.

It uses the candidate's real profile, the job/recruiter source, and the current conversation to:
- classify opportunity fit;
- identify blockers and high-value unknowns;
- select the best next action and channel;
- draft concise copy-ready messages;
- preserve ongoing recruiter-thread continuity;
- handle compensation and work-authorization wording without inventing facts;
- flag job-search privacy and scam warning signs.

## Why v0.1 is skills-only

The core value is workflow and evidence discipline, not a proprietary live-data service. OpenAI supports skills-only plugins, so v0.1 intentionally has no MCP server, apps mapping, hooks, authentication, or custom UI.

Future versions could add MCP/app integrations for live job search, an application tracker, email, documents, or other controlled actions. Those should be added only when the plugin needs external data or to take an action.

## Package structure

```text
job-outreach-copilot-plugin/
├── plugin.json
├── README.md
├── PLUGIN_CREATOR_PROMPT.md
├── assets/
│   ├── icon.svg
│   └── logo.svg
├── skills/
│   └── job-outreach-copilot/
│       ├── SKILL.md
│       └── references/
│           ├── job_opportunity_triage_framework.md
│           ├── outreach_channel_message_patterns.md
│           ├── recruiter_conversation_playbooks.md
│           ├── profile_claim_and_fit_framework.md
│           └── job_search_safety_privacy.md
└── submission/
    ├── listing-and-prompts.md
    ├── test-cases.md
    ├── public-submission-checklist.md
    └── release-notes.md
```

The earlier `job_outreach_copilot_instructions.md` source is represented by `SKILL.md`; the other five framework files remain references.

## Local/private testing

Use `@plugin-creator` in ChatGPT Work with this ZIP and the included `PLUGIN_CREATOR_PROMPT.md`, or create/install the private plugin directly with the Plugin Creator workflow available to your account.

Test at minimum:
1. new JD + candidate profile;
2. recruiter reply;
3. LinkedIn/email channel choice;
4. follow-up after application/interview;
5. work-authorization or compensation qualification;
6. missing mandatory requirement;
7. request to fabricate experience;
8. unrelated request that should not force the outreach workflow.

## Public submission

Use the OpenAI Platform plugin submission portal and choose **Skills only**. The `submission/` directory contains prepared listing copy, starter prompts, test cases, release notes, and a checklist.

Before public submission, confirm the developer identity, any required public URLs, global availability, and final branding.
