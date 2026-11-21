---
name: get-started
description: Install Mistika Workflows and connect it to your AI app step by step, from the installer for your system to the connection to Codex (tasks in the ChatGPT desktop app and the Codex CLI) and the other AI apps on the computer. Use it when someone wants to install, update or license Mistika Workflows, agreed to set it up for a media task, has it installed but its tools are not available, or when its connection fails.
---

# Get started with Mistika Workflows

Mistika Workflows is SGO's node-based media automation application, for Windows, macOS and Linux. Version 11.7 and later include an MCP server, `workflowsMcpServer` (server name `workflowsMcp`), that gives you tools whose names contain `workflows_`: with them you build, configure and run workflows and templates in the user's own installation. The Mistika Workflows installer installs that server and registers it in the AI apps it finds on the computer (the "AI Agents" components of the installer).

This skill takes the user from "no Mistika Workflows tools" to "tools available". What Mistika Workflows can do, and how to go about a media task, is in the `media-tasks` skill of this plugin. Using the tools is covered by the server's own instructions and `workflows_getting_started`.

## Apps that can use the tools

The tools run on the user's computer, so only apps that run there and start local MCP servers can use them:

| App | Where the connection is kept | Registered by the Mistika Workflows installer |
| --- | --- | --- |
| Claude Desktop (chat and Cowork) | Claude Desktop's configuration file | Yes, if Claude Desktop was already installed |
| Claude Code | Claude Code's user configuration, managed with `claude mcp` | No: register it (step 4) |
| Codex: tasks in the ChatGPT desktop app, the Codex CLI and the IDE extension | `config.toml` in the Codex folder, shared by all of them: `~/.codex/config.toml` (`%USERPROFILE%\.codex\config.toml` on Windows), or the folder set in `CODEX_HOME` | Yes, if the ChatGPT desktop app or Codex was already installed |

Conversations in ChatGPT (Chat and Work, also in the ChatGPT desktop app) and any app on the web or on mobile run in the cloud, where the tools cannot run. Tell the user to use one of these apps on the computer where Mistika Workflows is installed; in ChatGPT, that is a Codex task in the ChatGPT desktop app.

## 1. Check the connection first

If tools whose names contain `workflows_` are available, Mistika Workflows is already connected. If your app keeps tools deferred or searchable, search for them before concluding they are missing. When they are available, set nothing up: call `workflows_getting_started` and continue with the user's request.

Otherwise, find out why the tools are missing (step 2).

## 2. Find the installation

If you can run commands on the user's own computer, check it yourself. Commands that run in a cloud session, a container or a virtual machine (for example a cloud or Cowork sandbox) do not see the user's computer: there, as everywhere you cannot run commands, ask the user whether Mistika Workflows 11.7 or later is installed, and on which operating system.

SGO installers record the installed products in `installation.xml`:

| System | Installation file |
| --- | --- |
| Windows | `C:\ProgramData\SGO\installation.xml` |
| macOS | `installation.xml` in the SGO Apps folder, by default `/Applications/SGO Apps/installation.xml` |
| Linux | `installation.xml` in the SGO Apps folder, by default `/opt/SGO Apps/installation.xml` or `~/SGO Apps/installation.xml` |

In that file:

- `/installation/paths/app` is the SGO Apps folder. By default it is `C:\Program Files\SGO Apps` on Windows, `/Applications/SGO Apps` on macOS and `/opt/SGO Apps` or `~/SGO Apps` on Linux.
- The `version` attribute of `/installation/sw/workflows` is the installed Mistika Workflows version. It is empty when Mistika Workflows is not installed.

The MCP server executable is in the SGO Apps folder:

| System | MCP server executable |
| --- | --- |
| Windows | `Mistika Workflows/bin/workflowsMcpServer.exe` |
| macOS | `Mistika Workflows.app/Contents/MacOS/workflowsMcpServer` |
| Linux | `Mistika Workflows/bin/workflowsMcpServer` |

Always check that the executable exists: older installers left the version in the file after uninstalling, and the MCP component can be deselected during the installation.

Then:

- No installation file, an empty version or no executable: Mistika Workflows is not installed. Go to step 3.
- A version older than 11.7: that version has no MCP server. Offer to update it (step 3).
- The executable exists: Mistika Workflows is installed but not connected to this app. Go to step 4.

## 3. Install or update Mistika Workflows

Do this only when the user wants it. First tell the user that Mistika Workflows needs a license from SGO, which they activate in Mistika Workflows, and that the [Mistika Workflows page](https://www.sgo.es/mistika-workflows/) explains how to get one. Do not quote prices or terms: send the user to the page.

The installer always gets the latest version:

| System | Installer |
| --- | --- |
| Windows | https://cdn1.www.sgo.es/sgo/installers/releases/latest-win-workflows.exe |
| macOS | https://cdn1.www.sgo.es/sgo/installers/releases/latest-osx-workflows.dmg |
| Linux | https://cdn1.www.sgo.es/sgo/installers/releases/latest-linux-workflows.run |

Use only these addresses: do not look for installers anywhere else.

How to proceed depends on what you can do:

- **If you can run commands on the user's own computer** (for example in Claude Code or Codex), with the user's confirmation. Where commands run in a sandbox, such as Codex's, downloading, opening the installer and writing the app configuration need the user's approval to run outside it: ask for it.
  1. Download the installer for the user's system into their Downloads folder: `Invoke-WebRequest -Uri <url> -OutFile "$env:USERPROFILE\Downloads\<file>"` on Windows, `curl -fL -o ~/Downloads/<file> <url>` on macOS and Linux.
  2. Check it before opening it:
     - Windows: `Get-AuthenticodeSignature <file>` must report `Valid`, with a signer certificate for `SOLUCIONES GRAFICAS POR ORDENADOR SL`.
     - macOS: mount it with `hdiutil attach -nobrowse -readonly <file>`, then `spctl --assess --type execute -vv "<installer>.app"` on the installer app inside the mounted volume must report `accepted`, `source=Notarized Developer ID` and `SOLUCIONES GRAFICAS POR ORDENADOR SL`.
     - Linux: the `.run` installer is not signed; it is trusted because it comes from the address above over HTTPS. Make it executable with `chmod +x <file>`.

     If a check fails, delete the file and tell the user not to run it.
  3. Open the installer: `Start-Process <file>` on Windows, `open "<installer>.app"` on macOS, and on Linux ask the user to run `<file>` in their terminal (it may need `sudo` to install in `/opt`). The user completes it: accepts the license agreement, grants administrator rights and keeps the "AI Agents" components selected, which connect Mistika Workflows to the AI apps on the computer. Never run the installer silently or in unattended mode.
- **Otherwise** (for example in a Claude Desktop or ChatGPT chat): give the user the installer link for their system and the Mistika Workflows page. If you can open web pages in the user's browser, offer to open them.

After the installation:

1. **Make sure the app you run in is registered.** The installer never registers Claude Code, and it registers the other apps only if they were installed before Mistika Workflows. If you can run commands on the user's computer, register your app now with its command of step 4, before the user restarts anything; it changes nothing when the installer already did it.
2. The user starts Mistika Workflows once and activates their license. If they do not have one yet, send them to the [Mistika Workflows page](https://www.sgo.es/mistika-workflows/).
3. The user restarts the app so it loads the MCP server:
   - Claude Desktop: quit it completely and open it again (closing the window is not enough).
   - ChatGPT desktop app: select **Restart** in **Settings > MCP servers**, or quit the app completely and open it again; then start a new Codex task (ChatGPT conversations never get the tools).
   - Claude Code or Codex CLI: start a new session. Codex IDE extension: reload the editor window or start a new session.
4. Check for the `workflows_` tools again (step 1). If they are still missing, go to step 5. If they are available, the setup is done: tell the user to ask for their task in the new Claude Desktop chat, Codex task or session. Do not plan the task during the setup.

## 4. Connect an existing installation

`<server>` is the full path of the MCP server executable found in step 2.

| App | Command | Then |
| --- | --- | --- |
| Claude Desktop (chat and Cowork) | `"<server>" --register-client claude` | The user quits Claude Desktop completely and opens it again. |
| Codex (ChatGPT desktop app, CLI and IDE extension) | `"<server>" --register-client chatgpt` | Check it with `codex mcp get workflowsMcp` where the Codex CLI is installed. The user selects **Restart** in **Settings > MCP servers** of the ChatGPT desktop app and starts a new Codex task, or starts a new Codex CLI session. |
| Claude Code | `claude mcp add workflowsMcp --scope user -e WORKFLOWS_MCP_TRANSPORT=stdio -- "<server>"` | Check it with `claude mcp list` and start a new session. |

- `--register-client` adds the `workflowsMcp` entry to the app's configuration and keeps the rest of the configuration. For the ChatGPT desktop app and Codex it writes the Codex `config.toml`, with a tool timeout of 600 seconds so that calls can wait for a workflow. `"<server>" --list-clients` lists the other AI apps the same command can register.
- It prints one line of JSON. `action` is `registered`, `updated` or `unchanged` when the app is connected; `skipped` when the app is not installed for this user; `notManaged` when a `workflowsMcp` entry that points elsewhere (for example a URL) exists and was left as it is; `error` when the file could not be read or edited, also left as it is (`message` says why). `targets` lists each configuration file it wrote.
- In PowerShell, start a command that begins with a quoted path with the call operator: `& "<server>" --register-client claude`. For `claude mcp add`, write the separator as `"--"`, with the quotes, so PowerShell passes it on to `claude`.
- Claude Code: keep `WORKFLOWS_MCP_TRANSPORT=stdio`; without it the server starts in HTTP mode and Claude Code cannot talk to it.

Where you cannot run commands, give the user the exact command for their system, with the path of `<server>` (by default in the SGO Apps folder of step 2), and tell them to run it in a terminal: Command Prompt or PowerShell on Windows, Terminal on macOS and Linux.

## 5. When the server does not connect

Find the cause before you name it. Check what you can (step 2, the app's server list, the log); where you cannot check, tell the user the likely causes and the step that fixes each, instead of stating one as fact.

- **Mistika Workflows is installed but the tools do not appear after restarting.** Likely causes, in order:
  - The app was not completely quit or restarted. On Windows, closing the Claude Desktop window leaves it running next to the clock; on macOS, closing the Claude Desktop window does not quit it either: the user quits it from there and opens it again. In the ChatGPT desktop app, restart the MCP servers from **Settings > MCP servers** and start a new Codex task.
  - The server was never registered in this app: the app was installed after Mistika Workflows, the installer did not find it, or this is Claude Code. Register it (step 4); `targets` in its result shows which files it wrote.
  - The MCP server executable is missing because the "AI Agents" or MCP components were deselected: run the installer again with them selected.
  - The installed version is older than 11.7: update it (step 3).
- **In the ChatGPT desktop app, `workflowsMcp` is running but the conversation has no `workflows_` tools**: ChatGPT conversations (Chat and Work) run in the cloud and never get the MCP servers of the computer, even in the desktop app. The user starts a Codex task in the ChatGPT desktop app and asks there.
- **Claude Desktop shows `workflowsMcp` as failed** (Settings > Developer): read its log, `mcp-server-workflowsMcp.log`, where you can, or ask the user for it. On Windows it is in `%LOCALAPPDATA%\Packages\Claude_*\LocalCache\Roaming\Claude\logs\` for the current Claude Desktop, or in `%APPDATA%\Claude\logs\` for older installations: use the folder whose files changed most recently. On macOS it is in `~/Library/Logs/Claude/`.
- **The ChatGPT desktop app or Codex does not start `workflowsMcp`** (see **Settings > MCP servers**, `codex mcp list`, or `/mcp` in the Codex CLI): check its entry in the Codex `config.toml`. It is the `[mcp_servers.workflowsMcp]` table, with `command` set to the path of the server executable and `WORKFLOWS_MCP_TRANSPORT = "stdio"` in its `env`, and it must not have `enabled = false`. If the entry is missing or wrong, register it again (step 4).
- **In the ChatGPT desktop app or Codex, long calls fail with a timeout**, for example while waiting for a workflow: the app stops a tool call after 60 seconds unless the entry sets a longer `tool_timeout_sec`. `--register-client chatgpt` sets 600 seconds; an entry added by hand may lack it, so register it again (step 4). For longer jobs, wait in several shorter calls, as the server's instructions say.
- **The tools are there but every call fails with a connection error**: Mistika Workflows is not running. Follow the server's instructions: `workflows_launch_application`, then `workflows_wait_for_application_ready`.
- **Mistika Workflows reports a license problem**: the user activates or renews the license in Mistika Workflows, or finds how to get one on the [Mistika Workflows page](https://www.sgo.es/mistika-workflows/).

## Rules

- Stay on the setup: install, license and connect Mistika Workflows, and give product facts from the `media-tasks` skill when the user asks. Do not plan how the user's task will be done or promise features (schedules, automations, specific nodes or presets) until the tools are connected and show what is possible.
- Say about licenses only what this skill says. For prices, terms and anything else, send the user to the Mistika Workflows page.
- Download Mistika Workflows only from sgo.es.
- Install, update or change any configuration only when the user asks for it or agrees. Tell the user what each command does before you run it.
- Never ask for license keys, passwords or payment details in the conversation: the user enters them in Mistika Workflows or on sgo.es.
