# Connect JobSpidey

This candidate uses the official standalone Codex layout: a compatibility
manifest, a URL-only remote MCP configuration and a setup skill. It has no
portable root manifest, static bearer header or embedded OAuth credentials.
This local 0.1.1 candidate's actual-client checks, installed-host acceptance and
saved portal OAuth configuration remain pending. Earlier direct acceptance is historical.

## Historically accepted direct MCP path

```text
codex mcp add jobspidey --url https://mcp.jobspidey.com/mcp
codex mcp login jobspidey
```

The client starts OAuth. Sign in or create an account on JobSpidey, verify your
email if required, review permissions and the generation budget, and return to
the client. Never put passwords, verification codes or account tokens in chat.
Read get_account_context before using supported countries/sites and templates.
Search can work without a saved resume. Preparation needs a usable saved resume
or permitted one-off text override and existing account entitlements.

Present one numbered shortlist with consistent numbers in its summary and details.
Keep each number mapped to its originating `search_id` and `job_id` so a later
selection still refers to that job after another search. Numbered text with
Markdown job links is the default; rich cards are optional. Ordinary search needs
neither candidate context nor a resume. Ground personal-fit claims in conversation
facts confirmed for the connected candidate or explicitly attribute retrieved
candidate facts. Keep other profiles separate.
Missing facts about skills, visa or work authorization remain unknown and must
not silently exclude jobs.
Automated relevance hints do not verify personal fit; see the
[tool contract](tool-contract.md) for score and saved-search position semantics.

Prepare only selected jobs. Preserve request IDs across ambiguous retries; read
operation progress and retrieve both PDFs before claiming a complete package.
Refresh links through a package read rather than generating again. File links
are private capabilities and must not be published or logged.

Resume text and outcome writes require separate optional permissions. Outcomes
are agent-reported, not employer-verified. Manage or disconnect connections under
Account -> Connected AI agents. Explain service limits without transaction links
or digital-credit/subscription promotion.

## Plugin installation gate

Use a reviewed local/repo marketplace or an approved public directory listing.
Install the plugin, start a new session, authenticate its actual bundled MCP,
then validate the setup skill and requested workflow on that surface. No listing
or installed-host success is established by this ZIP or the direct commands.

Official references:
- https://developers.openai.com/codex/mcp
- https://developers.openai.com/plugins/build/plugins
- https://developers.openai.com/plugins/deploy/submission
