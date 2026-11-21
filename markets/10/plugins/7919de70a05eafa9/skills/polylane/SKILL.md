---
name: polylane
description: Investigate production with the Polylane tools. Use when the user reports a production issue, outage, error spike, latency regression, or failed deploy; asks what broke, what changed, or whether production is affected; wants a service's logs or metrics, or a query in a connected observability tool; wants to know what depends on a service, who owns it, or which repository deploys it; or wants to work with Polylane issues, investigations, or fixes.
---

# Polylane

Polylane keeps a graph of the user's production stack: the resources in their connected cloud accounts, how those resources connect, who owns them, and the repositories that deploy them. It reads those resources' logs and metrics, runs queries in connected observability tools, records issues, a feed of recent changes, investigations, fixes and memories, and reads the commits of connected repositories.

## How the tools work

Each tool does one thing, named after what the user wants: `listIssues`, `getAuditLog`, `getBlastRadius`, `findOwner`, `listCommits`. Tools marked read-only change nothing.

- **Workspace:** most tools take a `workspaceId`. When the connection can read more than one workspace, get it from `listWorkspaces` and ask the user which one to use.
- **Resources:** a tool that takes a resource takes one string: the id another Polylane tool returned, or a plain name. A name that matches several resources returns the candidates with their ids; call again with the right id. When nothing matches, search with `findResources`.
- **Times** are ISO-8601 strings such as 2026-01-31T09:00:00Z.
- **Incomplete answers:** when the graph returned only a sample, or a tool reached its own limit, the result says so. Tell the user, and narrow the request rather than presenting a partial answer as complete. A result too large to return comes back as an error that says how to narrow it.

## Investigating a production issue

1. **Anchor.** Polylane may already have flagged it: check `listIssues`, then read the issue with `getIssue` and `getIssueTimeline`, and any investigation with `getInvestigation`. With only a symptom, find the service with `findResources`.
2. **Check what changed first.** Most incidents follow a change. `getAuditLog` reads who changed what on the cloud account (deploys, configuration and IAM edits) for the window before the symptom started; `findDeployingRepository` and `listCommits` show the code that shipped.
3. **Read the evidence.** `queryLogs` reads the service's log lines for the window, optionally only those matching a search; `getMetrics` compares its metrics with the previous window; `getLogPatterns` shows which messages are new or growing; `getResourceHealth` gives metrics and open issues together. A cause is credible when the timing lines up and the errors match what changed.
4. **Size the impact.** `getBlastRadius` shows what a failure reaches; `listDependents` and `whoCalls` show what depends on the service and what is calling it now.
5. **Correlate with code.** `findDeployingRepository` names the repository; `listCommits` and `getCommitDiff` read its recent changes.

Lead the answer with the cause, or the most likely cause and the evidence that would confirm it. Then give the evidence with timestamps, then the next step. Include console links when the results carry them.

## Understanding a service

- `explainResource` says what a resource is, where it runs, and what it is close to.
- `listDependencies`, `listDependents`, `getConnections` and `findPath` show how it connects; `mapService` draws its neighbourhood.
- `findOwner` names who owns it; `findDeployingRepository` and `listRepositoryResources` link it to code.
- `findSinglePointsOfFailure`, `listMonitoringGaps` and `listAdvisories` show where the stack is fragile or unwatched.

## Logs, metrics and queries

- `queryLogs`, `getLogPatterns` and `getMetrics` take one resource. `queryLogs` covers Cloudflare, AWS, Vercel, Fly, Render, Supabase, Railway and Trigger.dev resources; for anything else it says Polylane does not read its logs. When it returns a cursor, pass it to read the next page; otherwise narrow the window with `from` and `to`.
- For an exact query, use the connected tool's own query language: `runCloudflareTelemetryQuery` and `runCloudflareGraphql`, `runAxiomQuery` and `runAxiomMetricsQuery`, `runHoneycombQuery`, and `getDatabaseQueryInsights` for PlanetScale. Read the dataset's fields first (`listAxiomDatasetFields`, `listHoneycombColumns`, `listCloudflareTelemetryKeys`) so the query uses real names.
- `listLogSources` lists the log groups and datasets of the connected tools.
- A tool for a provider the workspace has not connected says what to connect.

## Checking a change before it ships

1. Find the resources the change touches with `findResources`.
2. Get what a failure would reach with `getChangeImpact` (several resources, or a pull request Polylane reviewed) or `getBlastRadius` (one resource).
3. Check `listIssues` for open issues on those resources. Do not recommend shipping into an open incident.
4. Check `getAuditLog` and `listCommits` for other recent changes to the same resources.

## Fixes, investigations and the rest of the workspace

- `listFixes` and `getFixDiff` show the fixes Polylane opened. `startInvestigation` and `replyToInvestigation` ask Polylane to look into something; `listInvestigations` and `getInvestigation` read what it found.
- `getWorkspaceOverview` summarizes the workspace; `searchEverything` searches its resources, repositories, investigations and memories.
- `searchMemory` reads what Polylane knows about the team's systems; `remember` and `forget` change it.
- `listEscalations` shows what was handed to people; `listTickets` reads Linear issues.

## Changing anything

Tools that change data need read-write access, which the user chooses when connecting Polylane, and the user confirms each change before it runs. Only call a write tool when the user asked for that change, after reading the current state with the matching read tool. Some writes reach outside Polylane, and their descriptions say so: merging or closing a fix acts on GitHub, cancelling a fix stops its hosted code agent, creating or updating a ticket acts in Linear, muting an alarm changes CloudWatch, and refreshing an AWS account can update its CloudTrail and alarm setup. If a write is refused for lack of access, tell the user how to reconnect with read-write access.

## Nothing connected yet

If the tools return little, the workspace has not connected much. Connecting a cloud provider in the console (https://console.polylane.com) populates the graph, and connecting GitHub adds code. Docs: https://docs.polylane.com.
