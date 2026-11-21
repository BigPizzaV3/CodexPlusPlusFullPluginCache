---
name: sitehaus-website-builder
description: Use when the user wants to connect to SiteHaus to create, edit, inspect, or manage a website through supported SiteHaus MCP tools.
---

# SiteHaus Website Builder

Use the connected SiteHaus MCP server for website creation and management tasks whenever its tools are available.

## Workflow

0. Call `get_guidelines` first and follow it. It explains how SiteHaus builds WordPress themes, web apps and client proposals. A client proposal, quote or estimate is not a project: use `create_proposal` for it.
1. Identify what the user wants to build or change. For new websites, gather the business or project purpose, audience, key pages, visual direction, and important functionality. Ask only for essential missing information; otherwise proceed with sensible assumptions.
2. Use the available SiteHaus tools to create or update the project. Prefer the supported project workflow and inspect existing files before changing them.
3. Make coherent, related edits together when supported. Follow the SiteHaus server's instructions and validation workflow.
4. Verify results using available checks or previews. Do not claim an operation succeeded unless the tool confirms it.
5. Do not publish a website (`publish_project`) unless the user explicitly asks to publish it. Ask the user to confirm before deleting files with `delete_files`, and never delete more than they asked for. SiteHaus tools cannot delete whole projects.
6. Respect account permissions and the capabilities exposed by the connected server. Never invent tools, endpoints, project details, or completed actions.

## Example requests

- Create a modern website for my business.
- Build a store homepage and individual product pages.
- Improve the mobile layout and hover animations.
- Inspect my current project and fix the broken navigation.
- Review the website and prepare it for launch.
