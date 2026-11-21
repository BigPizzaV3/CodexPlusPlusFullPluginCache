---
name: deploy-existing-code
description: Check code the user already wrote against Cafe24 AI SPACE's platform constraints, fix what would break, then deploy or update it. Use when the user brings existing code — from another AI tool, a local folder, or a GitHub repository — and wants it published or wants an existing AI SPACE project updated. Do not use when the app should be written from scratch (use deploy-new-app).
---

# Deploy code the user already has

Code written elsewhere usually violates one or two platform rules. **Check first,
fix, then deploy.** Deploying straight away wastes a build — and on a free trial
builds are a limited resource.

Reply in the user's language.

## Expected input

Files the user attached, a GitHub repository, or a public Git URL. If it is not
clear which, ask once.

## Step 1 — Pre-flight check

Work through `references/preflight-checklist.md`. Then show the user two lists
before you deploy anything:

```
Fixed
  • server.js now listens on 0.0.0.0:3000 (was 127.0.0.1:8080)
  • database config now reads DB_USER instead of a hard-coded password
  • removed Dockerfile

Left as-is
  • the SQLite file path — tell me if this data must survive redeploys
```

If the stack is Go, Java or Rust, stop here. Those runtimes do not exist on the
platform. Say so plainly and describe what rewriting would involve.

## Step 2 — Choose the path

### The user is deploying something new

Reserve a space first: `list_my_spaces`, and use one where `project_id` is
`null`. If none is free, stop and say so.

**Files attached in chat.** ChatGPT has no shell, so always use the JSON upload
path: `project_upload` with `action: "create_session"` and `mode: "json"`, then
`upload_json`, then `project_upload` with `action: "finalize"`, `deploy: true`
and the `space_id`. Limits are 3 MB per file, 10 files per request, 5 MB total.

**Too large for those limits, or a real repository.** Do not shard the upload.
Use `external_repo` with `repo_connect` to link the user's GitHub account, then
`repo_deploy`. For a public repository with no account linking, `deploy_project`
with the HTTPS Git URL works.

### The user is updating an existing project

**Always call `get_project_status` first and read the `source` field.** Calling
the wrong update tool returns `SOURCE_MISMATCH`.

| `source` | How the project was created | What to call |
|---|---|---|
| `internal` | uploaded files, or a public Git URL | `project_upload` with `update: true`, then `update_project` |
| `github` | linked GitHub repository | `external_repo` → `repo_update`, or `repo_write_file` for a single file |

`update_project` accepts only `project_id`, `rebuild` and `wait`. Parameters like
`mode` or `reset` do not exist.

When one repository is deployed to more than one project, `external_repo` returns
`AMBIGUOUS_PROJECT`. Call `list_my_projects` and pass the exact `project_name`.

## Step 3 — Watch and verify

Call with `wait: false`, poll `get_project_status`, and tick only the steps you
have actually seen succeed. Then call `site_verify` on the project URL — a
successful build is not proof that the site answers.

If the build fails, hand off to the troubleshooting workflow rather than
retrying. Read the logs before changing anything.

## Rules you must not break

- **Stop after two identical failures.** Never retry in a loop.
- **Do not use `force: true`.** If the target space is occupied, offer a
  different project name, an update of the existing project, or deletion through
  the web console.
- An update recreates the application container. Database contents and
  `/app/user_data/` are preserved; anything else in the app directory is not.
- Rollback, deletion, power control and billing are not available here. Direct
  the user to the Cafe24 web console.

## Do not infer

Plan limits, prices and free-trial build quotas change. Do not quote them from
memory — point the user to `https://aispacedocs-docs.mycafe24.ai`.
