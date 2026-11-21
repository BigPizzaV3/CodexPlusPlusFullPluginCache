---
name: get-started
description: Explains how to use Brvvo from a chat - plan a site, confirm the brief, build, check progress, open a preview, change a project and publish. Use when someone asks what Brvvo can do or how to begin.
---

# Getting started with Brvvo IDE

Brvvo IDE (by Codeblaze AI) builds websites and apps from a description. The build itself runs in the Brvvo app on the person's own computer, so the app has to be open there.

## Suggested flow

1. If the person only has an idea, use `plan_site` to turn it into a short brief and show it to them.
2. Ask them to confirm or adjust the brief. Do not start a build until they clearly agree.
3. Use `start_build`, then `get_build_status` when they ask how it is going. If the status says it is waiting for Brvvo to be open on their computer, tell them to open Brvvo and check again.
4. When the build is done, share the preview link with `get_preview_link`.
5. For edits, name the project exactly (use `list_projects` if unsure), confirm the change with the person, then use `make_change`.
6. Publishing makes a site visible to everyone. Use `publish_site` only when the person clearly asks for it and says yes in this conversation.

## Good to know

- A Brvvo account is needed for everything except planning. The person signs in on a Brvvo page when they connect.
- Never ask for passwords, keys or other secrets.
- Only the connected person's own projects are visible, and nothing is ever deleted.
