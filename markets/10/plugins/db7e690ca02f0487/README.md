# KontoCSV Agent Plugin

Portable Agent Plugins package for the public ChatGPT/Codex directory profile.

## MCP endpoint

`https://www.kontocsv.de/api/mcp/directory`

This is the directory-safe profile. It intentionally excludes monetary quotes and credit checkout. It can use credits that already exist in the authenticated KontoCSV account.

## Before submission

- Deploy the directory MCP endpoint and `/.well-known/oauth-protected-resource/api/mcp/directory`.
- Deploy `/support` and the synthetic review fixtures under `/review-fixtures/`.
- Set the OpenAI domain challenge value in `OPENAI_APPS_CHALLENGE` and deploy the challenge route.
- Create a dedicated reviewer KontoCSV account with sufficient sample credits and no MFA or magic-link dependency.
- Record the required walkthrough video and add its reviewer-accessible URL in the submission portal or manifest.
- Run all five positive and three negative cases with the reviewer account.
- Scan the production MCP tools after each tool/schema change.
