---
name: onboarding
description: Set up Polylane right after it is installed. Use once, when the plugin is first added or the user asks how to start with Polylane, to confirm the connection, pick the workspace, show what is connected, and suggest first questions about their production.
---

# Getting started with Polylane

Walk the user through these steps in order, briefly. Read only; do not call any tool that changes data during setup.

## 1. Confirm the connection and pick a workspace

Call `listWorkspaces`.

- One workspace: say which one Polylane is connected to.
- Several: list them by name and ask which one to use for this conversation. Use its id as `workspaceId` from then on.
- An error that the connection is not authorized: tell the user to reconnect Polylane from the plugin settings and sign in again.

## 2. Show what is connected

Pass the chosen `workspaceId` to every call below.

- `getInventory` with `groupBy: ["provider", "account"]`: which providers and accounts the graph holds, and how many resources each has.
- `listIssues` with `unresolvedOnly: true` and `status: "new,confirmed,failed,skipped"`: the open issues. Dismissed issues stay unresolved, so the status filter leaves them out. Report the result's `count` as the number open, not the number of rows returned.
- The most severe open issue: `listIssues` with the same filters, `severity: "critical"` and `limit: 1`. If its `count` is 0, repeat with `severity: "high"`. Name the issue that comes back with its resource and say how many open issues share that severity; if both counts are 0, say no open issue is high or critical.
- `listCriticalResources`: the resources the workspace depends on most, for real names in step 4.

Tell the user, in a few lines, what these reads returned. Report only what they returned:

- If a read fails, say that part could not be read. Do not report it as zero or as nothing connected.
- If the inventory has no resources, say the graph is empty for now: it fills once a cloud account is connected in the Polylane console (https://console.polylane.com) and its first sync finishes, and connecting GitHub adds code. An account that is still syncing also shows an empty graph, so do not say that no account is connected. Stop there.

## 3. Say what the connection can do

The user chose read-only or read-write access when connecting. Explain in one sentence: read tools work with either; tools that change something (starting an investigation, updating an issue, merging a fix) need read-write access and always ask the user to confirm first.

## 4. Suggest three first questions

Base them on what step 2 returned, with real names from it:

- an open issue: "Why is `<resource>` failing? Show its issue and its error logs from the last day."
- a critical resource: "If `<resource>` goes down, what else is affected?"
- a critical resource: "Map the services around `<resource>`: what does it connect to, and what depends on it?"

If no issue is open, suggest asking for the workspace's single points of failure or its monitoring gaps instead.

End by saying the user can ask about any service by name, and that `@Polylane` brings Polylane into any conversation.
