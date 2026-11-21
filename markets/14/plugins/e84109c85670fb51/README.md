# Corsair

Work in [Corsair](https://corsair.dev) from your agent: track issues and projects in Corsair's PM, keep people, companies and deals in its CRM, search across all of it, set up routines that run on a schedule, and save skills every agent on your link can load. Other apps you connect to Corsair work through the same tools.

The plugin adds the Corsair MCP server, `https://mcp.corsair.dev/mcp`, and six skills:

| Skill | Covers |
| --- | --- |
| `corsair-workspace` | Corsair's PM and CRM: filing and updating issues, and keeping people, companies, deals, notes and tasks |
| `corsair-connect-apps` | Finding an app, handing over its sign-in link or pointing to the Connect button on Corsair's card, and confirming the connection |
| `corsair-data` | When to search, read live, make a change or wait on a long job; when to send Corsair feedback |
| `corsair-automations` | Building routines from plain English, then checking their runs |
| `corsair-approvals` | Permission modes, and what to do when an action needs approval |
| `corsair-skills` | Loading the user's saved skills, finding new ones on skills.sh, and saving or uploading skills so every agent on the link has them |

In Claude Code:

```
/plugin marketplace add corsairdev/agent-plugins
/plugin install corsair@corsair
```

Other clients: see the [repo README](../../README.md#install).

The first time your client connects, it asks you to sign in to Corsair and approve the connection.

Questions or problems: email [primary@corsair.dev](mailto:primary@corsair.dev).

[Privacy policy](https://corsair.dev/privacy-policy) · [Terms](https://corsair.dev/terms-of-service)
