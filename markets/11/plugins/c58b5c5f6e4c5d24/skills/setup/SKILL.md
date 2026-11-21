---
name: setup
description: "Connecting the MWM AI plugin to an MWM account and getting its tools working, then the App Store Connect and Google Play connections a task needs, set up in MWM Console. Use when the person says things like \"connect MWM AI\", \"the MWM tools are missing\", \"I get an authorization error\", \"connect my App Store account\" or \"is my Google Play connected?\". Not for what the assistant may do once connected (working-with-mwm)."
---

# Set up MWM AI

## When this applies

Right after installation, whenever MWM's tools are missing or fail to authenticate, and when the person wants a store account connected to MWM. What the assistant may do once everything is connected belongs to working-with-mwm.

## The job and what good looks like

The person ends with MWM's tools working in their host, the store connections their task needs in place, and their original task resumed. Installing the plugin adds its skills; connecting the MWM account is a separate sign-in in the browser, and signing in to MWM Console alone does not connect the plugin. Access is reported as working only after a successful read: `get_publishing_knowledge` answers any store question for free, without a store connection or an app, and proves the tools respond.

## How a pro decides

- **Which of three problems.** No MWM tools means the MCP connection is missing. A store that is not connected means MWM Console needs that store's account. An act refused while the tools work means the person's role or organization lacks the right. Each has its own fix.
- **Missing tools after a sign-in.** Check that the plugin is enabled, refresh the host's tool list, or open a new chat.
- **Authorization or an expired session.** Use the host's reconnect or Authenticate control and check again.
- **A connection without MWM's tools.** The MCP has one permission: reconnect MWM in the host to grant it.
- **A network or server error.** Report it as it came: signing in again does not fix an endpoint that cannot be reached.

## Do

- In Codex desktop, open Settings and MCP servers, select Authenticate for MWM AI, sign in and consent in the browser, come back, and restart the server or open a new chat.
- When the plugin's server is absent there, check that MWM AI is installed and enabled. Only when no MWM server works, add one by hand: Streamable HTTP, URL `https://mcp.mwm.ai/mcp`, and authenticate it.
- In Claude Code, open the MCP panel with the mcp slash command, choose MWM AI and authenticate.
- For a store, send the person to the store connections of MWM Console, where the account is connected in their browser, and check again once they are back.
- Resume the person's original task as soon as access works.
- If a secret is pasted in the chat, don't repeat it; advise revoking it with its issuer and connecting a new one through MWM Console.

## Don't

- Don't ask for passwords, API keys, private key files, service account JSON, one-time codes or browser callback URLs.
- Don't guess a menu path in a host whose interface you don't know; say what to look for instead.
- Don't generate, connect or publish anything to test the connection.
- Don't read a store connection as permission to write or publish.

## Pitfalls

- Sending someone to MWM Console's consent page directly does not start a sign-in: the host has to create the request.
- A missing MCP connection says nothing about whether a store is connected.
- Two servers for the same endpoint confuse the host.

## Store facts

Tool results carry the store rules and limits they depend on, each with its source and the date it was checked. `get_publishing_knowledge` answers questions on this skill's topics the same way (topics: `mwm/store-connections`). When you use one of these facts, give its source and date.
