# LUCI for Codex

This plugin bundles the LUCI personal-history skill. It reads data through the LUCI desktop app on the same computer.

## Requirements

Install LUCI and enable Settings → Agent access. The plugin discovers the CLI using the app-generated discovery file; no personal token is included in this package.

## Use

Install `luci@personal`, then start a new Codex task and select LUCI. Ask “Summarize what I worked on today” or “Find the error I saw this morning.”

The local Personal catalog is for this computer. Team or public distribution requires publishing the plugin through the relevant marketplace. Each user needs their own LUCI installation and data.

## Updating

The bundled skill is a copy of the installed LUCI skill. Refresh it when LUCI changes its CLI, validate the plugin, and reinstall it.
