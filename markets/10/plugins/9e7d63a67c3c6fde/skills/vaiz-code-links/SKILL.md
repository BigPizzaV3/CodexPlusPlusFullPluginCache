---
name: vaiz-code-links
description: Connect code to work in Vaiz — discover GitHub and GitLab repositories connected to the space, search branches, pull or merge requests, and commits, and link or unlink them on tasks and Space Memory entries so PR/MR state syncs into Vaiz.
---

# Vaiz code links (GitHub and GitLab)

Vaiz can attach branches, pull requests (GitHub), merge requests (GitLab), and commits to a task or to a Space Memory entry. Linked pull and merge requests show up in the Vaiz UI and their state is synced automatically. Linking changes nothing on GitHub or GitLab; it only records the relationship inside Vaiz.

## Prerequisite

The Vaiz MCP server (`https://api.vaiz.com/mcp`) must be available through the installed Vaiz plugin and authorized with OAuth (open the Vaiz connection and complete OAuth sign-in), and the space must have the GitHub or GitLab integration configured by a space admin. Reading needs the `github:read` / `gitlab:read` scope of the connection, linking and unlinking need `github:write` / `gitlab:write`. If `get_code_repositories` returns nothing, the integration is not set up or the scope was not granted — tell the user instead of retrying.

Vaiz tools can appear under different names depending on how Vaiz is connected: `mcp__Vaiz__query_tasks` for a directly configured MCP server, or `mcp__codex_apps__vaiz_query_tasks` (sometimes with a longer app prefix such as `vaiz_testing_`) when Vaiz is installed as an app. Match tool names case-insensitively and by the tool suffix (`query_tasks`, `show_tasks`, …), not by an exact `Vaiz` prefix. Tools may also be loaded lazily: a Vaiz tool that is not in the current tool list is not missing — load it through tool search (for example `Vaiz get_code_repositories`) before concluding it is unavailable. Work with Vaiz only through these tools: do not open app.vaiz.com in a browser or drive the Vaiz desktop app with Computer Use, even if the user's `@Vaiz` mention also resolves to that app.

## Flow

1. `get_code_repositories` — repositories connected to the current space. Use the returned repository key (for example `github.com/acme/api` or `gitlab.acme.com/team/api`) as `repository` in the next steps; a bare `acme/api` works only when exactly one connected repository has that path.
2. `search_code_entities` — search a connected repository for branches, pull/merge requests, or commits by name, number, title, or sha. `type: "pull_request"` covers both GitHub pull requests and GitLab merge requests.
3. `link_code_entity` — attach the entity to a task (`taskId`, id or HRID) or to a memory entry (`memoryEntryId`), exactly one of them. Pass `number` for a PR/MR, `branchName` for a branch, `commitSha` for a commit. Details are verified against the provider before linking; linking is idempotent.
4. `get_code_links` — list existing links on a task or memory entry; each has a link `_id`.
5. `unlink_code_entity` — remove a link by its `linkId` (the `_id` from `get_code_links`), not by PR number or sha. Only the Vaiz-side link is removed.

## When to link

- A branch, pull request, or merge request is opened for a task — link it to the task as soon as the ref exists.
- A commit fixes a recorded Problem or implements a Decision — link it to that memory entry, or pass it in `relatedCodeEntities` of `create_devlog` (see `vaiz-memories`).
- A pull or merge request is merged — check `get_code_links` on the task so the state is reflected; nothing else is needed.

Linking or merging a PR/MR can trigger board automations with `code_change_*` conditions (see `vaiz-automations`).

## When not to link

- Do not link every commit of a long branch; link the branch or the pull/merge request instead.
- Do not link refs from repositories that are not connected to the space; `link_code_entity` will reject them.
- Leave `linkCodeEntitiesToRelatedTasks` at `false` in `create_devlog` unless the same code link genuinely belongs on every related task.

## Working with the current repository

When you are inside a git checkout, read the current branch and remote (`git rev-parse --abbrev-ref HEAD`, `git remote get-url origin`) to find the host, `owner/repo`, and branch name, then confirm the repository appears in `get_code_repositories` before linking. Never guess a PR or MR number; find it with `search_code_entities`.

Further reading: https://vaiz.com/help/tutorials/how-to-connect-vaiz-to-mcp · https://vaiz.com
