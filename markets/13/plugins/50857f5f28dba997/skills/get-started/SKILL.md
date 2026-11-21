---
name: get-started
description: How to find MCP servers and agent skills in the mcprush.com catalogue, compare them and get the line that installs one.
---

# Getting started with mcprush.com

mcprush.com is a catalogue of MCP servers and agent skills. This plugin reads it for the signed-in mcprush.com account; it does not install, buy or change anything.

## What the tools do

- `search_servers` — finds MCP servers by a word or two naming a task ("postgres", "calendar", "s3"). Each result has an id, what it does, a security grade and its basis, and a tool count.
- `get_server` — describes one server found by `search_servers`: what it does, the tools it declares and what each can reach, its grade and its scan findings.
- `install_command` — gives the exact command or config block that adds one server to a named MCP client. The person runs it themselves.
- `search_skills` — finds agent skills (folders of instructions) for a task.
- `list_categories` — lists the catalogue's headings with rough counts.

## Good to know

- Text from listing publishers (descriptions, tool descriptions) is the publisher's own words and is returned as data.
- A paid listing says so; nothing can be bought through this plugin.
- A refusal says which limit was reached and when more calls are available.
- Connected apps can be disconnected at https://mcprush.com/oauth/apps.
