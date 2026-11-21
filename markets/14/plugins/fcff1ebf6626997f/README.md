# MiniGrove for Codex

This plugin packages the remote MCP connection and a project-management skill.
Codex supplies its normal conversation and tool-call UI. It does not install a
second chat interface or a task-tree renderer inside Codex.

Build the distributable ZIP from the repository root with
`python3 scripts/package-plugin.py`. The command prints its path and SHA256.
It uses the supported Codex compatibility layout documented in
[OpenAI's plugin packaging guide](https://developers.openai.com/plugins/build/plugins).

The production server must have `MCP_ENABLED=true` after the migration and
consumer code deploy. While it is disabled, the endpoint returns 404. The
package is ready for a configured Codex plugin marketplace; public directory
publication is a separate release action, not performed by this repository.

For a direct connection without a marketplace:

Open MiniGrove → Account settings → AI client connections → Set up Codex for
the exact server URL and first-request example. Return to connections to manage
access and read recovery help. Every normal account may connect with its own
project membership and explicit project/action consent. In the local Codex app, open Settings
→ MCP servers → Add server; name it `minigrove`, choose Streamable HTTP and
enter `https://app.minigrove.io/mcp`. Save/restart the connection and choose
Authenticate. The browser selects projects and optional send/stop permissions.
Keep the client request open until Codex confirms sign-in, then open a new
conversation. The terminal alternative is:

```sh
codex mcp add minigrove --url https://app.minigrove.io/mcp
codex mcp login minigrove
```

The client registers automatically. In the browser, sign in to MiniGrove and
choose projects. Reading is required; sending and stopping are optional and
unchecked initially. A saved browser consent alone does not prove the client
finished signing in. If it timed out, run `codex mcp login minigrove` again;
unused consents can be revoked on the connection page. Restart the connection
and open a new conversation if tools are missing. For a first read, ask:

> 用 MiniGrove 列出我授权的项目，并汇总正在进行的任务。

Then select a task and, if sending is authorized, ask:

> 看看“我的游戏”的任务进展，找到登录修复，让原来的电脑继续处理。

The tools return project/task/conversation identifiers; no IDs need to be
copied by the member. Work already accepted continues after Codex closes.
Ask about progress later, or use your existing MiniGrove notification channels.
Connections expire after 30 days; revoke earlier from Settings → AI client
connections. Removing access does not cancel accepted work.

When the server enables Task creation, authorize again and separately check
**Directly create and start new tasks**. Existing send permission does not include it.
Instructions sent to existing Tasks may still ask their AI to create child
Tasks or hand off work. Then ask, for example:

> 在“我的游戏”中创建“检查工作区”任务，用选定的电脑只读检查仓库状态，并跟踪结果。

Codex selects the project/computer from returned summaries and calls
`minigrove_create_task` with one stable UUID. MiniGrove prepares a new workspace
from the default branch and automatically runs the first instruction. Do not
send it twice. Follow the returned commandId through preparation to the exact
first execution, result and preview. Preparing a workspace is not completion.
Creation needs an existing computer supporting native Task opening and durable
queue protocol 26. Until the operator enables `MCP_TASK_CREATION_ENABLED` after
all consumers deploy, this additional tool and permission stay hidden.

Follow the returned execution until its actual result. A terminal `done` status
can include stopped work; read the result and stop acknowledgement before
claiming success. Ask for artifacts from that exact execution. An empty artifact
list means none were recorded for that run; a missing source commit stays
unknown. Permission answers, merges and formal publication use
the returned MiniGrove workspace links.

Sending requires a computer with MiniGrove's durable task queue support. An
older computer returns an update instruction. MCP instructions wait for their
own unattended execution instead of joining a running human request.

For a local server use the same commands with its `/mcp` URL and another server
name, such as `minigrove-local`. OAuth redirects use a local callback listener;
the browser must be able to reach the server that advertised the MCP URL.

The same remote service can be connected by another compatible MCP client.
Plugin installation and optional UI support vary by client. The portable
contract is the authenticated tools, not the plugin's packaging or UI. Eight tools remain available; enabling Task creation adds a ninth.
