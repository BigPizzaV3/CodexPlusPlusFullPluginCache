---
name: commercetools-openai-setup
description: "Setup for the commercetools plugin in ChatGPT and Codex: checks whether a commercetools Project is already connected, and explains the optional ways to connect one, as a custom MCP server in ChatGPT or a per-repository connection in a coding agent. Use when the plugin's setup runs after installation, or when asked to set up commercetools or connect a commercetools Project in ChatGPT or Codex."
when_to_use:
  - "The commercetools plugin's setup was started in ChatGPT or Codex"
  - "Asked to set up commercetools, or to connect a commercetools Project, in ChatGPT or Codex"
metadata:
  contentType: SKILL
  area:
    - Foundations
---

# commercetools setup for ChatGPT and Codex

The plugin is ready to use as installed: it brings the commercetools skills and access to the
commercetools documentation and API reference. Connecting a commercetools Project is optional. It
lets the agent read and change that Project's data, through a managed MCP server in the Merchant
Center.

Don't change settings or configuration yourself, and don't search the filesystem. Explain, let the
user choose, and give the steps for their choice only.

## 1. Check for a connection

If a tool from a commercetools MCP server, such as `read_project`, is available, call it and
report:

> Connected to `{projectKey}`: `{project display name}`. You're set up.

Then stop. Otherwise continue with step 2.

## 2. Explain the options

Tell the user:

> commercetools is ready: you can ask about commercetools and build with it now. To also let me
> work with your Project's data, you can connect a Project:
>
> 1. **In ChatGPT conversations:** add the Project's managed MCP server as a custom MCP server.
> 2. **In a code repository** (for example in Codex): connect the Project to that repository, so
>    your team shares the connection.
>
> Or skip this: nothing else needs setting up. That's also the choice if your ChatGPT workspace
> admin sets up plugins for you: they provide the connection.
>
> What would you like to do?

If the user skips, or their admin sets things up, confirm that the plugin works as it is, and stop.

## 3a. ChatGPT conversations

> Create a managed MCP server for your Project in the Merchant Center, then add its URL in ChatGPT
> as a custom MCP server (**Plugins → Add → Add custom MCP server**). See
> [managed MCP servers](https://docs.commercetools.com/merchant-center/managed-mcp-servers.md).

## 3b. Code repository

Continue with the `commercetools-mcp` skill, Repository connection. It needs a code repository open
in the agent. If none is open, say so and stop.

## Checklist

- [ ] An existing connection reported, without offering more
- [ ] Connecting presented as optional, with both options and the choice to skip (or leave it to the admin)
- [ ] Only the chosen option's steps given; nothing configured on the user's behalf
