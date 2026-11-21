# LogRocket

Connect ChatGPT and Codex to LogRocket to investigate session replays, debug network requests, triage issues, and query product analytics.

The plugin connects to LogRocket's hosted MCP server at `https://mcp.logrocket.com/mcp`. When you install it, sign in to LogRocket through the OAuth prompt; the plugin can then access the same organizations and projects as your LogRocket account. The package contains no credentials and runs nothing locally.

The bundled `use-logrocket` skill helps the agent pick the right tool for each request, select a project, follow long-running analyses through to completion, handle timezones and pagination, and cite the LogRocket sessions, issues, and metrics behind its answers.

Try:

- “Find sessions for this user from yesterday and investigate their checkout problem.”
- “Show severe untriaged issues from the last week and prioritize them by impact.”
- “Analyze this saved funnel metric over the last seven days and investigate example drop-offs.”
- “Inspect failed network requests in this LogRocket session.”

## Connection options

Edit the server URL in `mcp.json` before installing a customized copy:

- Organization scope: `https://mcp.logrocket.com/mcp/<organizationID>`
- Project scope: `https://mcp.logrocket.com/mcp/<organizationID>/<projectID>`
- Toolsets: `?toolsets=sessions,metrics` (supported: `sessions`, `metrics`, `issues`, `ask-galileo`, `all`)
- Default timezone for time-bucketed results: `?timezone=America/New_York`
- Combined: `?toolsets=sessions,metrics&timezone=America/New_York`

The default package leaves all tools available and does not set a timezone. Scoped connections hide unneeded discovery tools. Toolset restrictions limit exposed tools; they do not replace server authorization.

OAuth is the default. LogRocket also supports project-scoped API keys for clients that need them; use the client's secret/environment configuration rather than committing credentials. For a standalone Codex connection using an API key, the documented command is:

```sh
codex mcp add logrocket --url https://mcp.logrocket.com/mcp --bearer-token-env-var LOGROCKET_API_KEY
```

Set `LOGROCKET_API_KEY` outside this package. This standalone connection is an alternative to the plugin connection, and adding both can expose duplicate tools.

See [LogRocket MCP documentation](https://docs.logrocket.com/docs/mcp) for current setup details.

## License

MIT, except for the LogRocket name and logo, which are trademarks of LogRocket, Inc.
