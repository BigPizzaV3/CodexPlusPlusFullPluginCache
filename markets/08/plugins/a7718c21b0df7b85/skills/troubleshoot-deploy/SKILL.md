---
name: troubleshoot-deploy
description: Diagnose a Cafe24 AI SPACE deployment that failed, a site that returns an error or will not open, or a connector that reports an authorization error. Use when the user says the build failed, the page is blank or 500, the database will not connect, uploaded files disappeared, or a tool call keeps failing. Do not use for a first deployment that has not been attempted yet.
---

# Diagnose a failed deployment

**Read the evidence before you change anything.** Most failures here have a
known cause, and a blind retry costs the user one of a limited number of builds.

Reply in the user's language.

## The stop rule comes first

If the same call has already failed the same way twice, do not call it a third
time. Stop, report what you saw, and work out the cause with the user.

Never treat an authorization error as a code problem. Fixing code will not fix
authentication, and you will burn build quota discovering that.

## Step 1 — Gather

1. `get_project_status` — is the state `success`, `failed`, or still building?
   Note the `runtime` and the `source` field.
2. `get_project_logs` — the build and runtime log. This is where the real cause
   is. Read it before forming a theory.
3. `site_verify` on the project URL if the deployment reports success but the
   user says the page does not load.

Deployment success and site reachability are two different things. Check them
separately.

## Step 2 — Match against the known causes

Work through `references/failure-catalog.md`. In order of how often each one is
the actual answer:

1. A `Dockerfile` or `docker-compose.yml` in the repository
2. The app bound to `127.0.0.1`, or to the wrong port (Node must use 3000,
   Python 8000, both on `0.0.0.0`)
3. `DB_USERNAME` used instead of `DB_USER`
4. A missing entry file at the repository root, so the runtime was misdetected
5. A dependency that fails to install, or a syntax error — visible in the log
6. Files written outside `/app/user_data/`, so they vanished on redeploy
7. Memory exhausted during the build

## Step 3 — Explain, fix, redeploy once

Tell the user what the log actually said, in plain language, before proposing a
fix. Then make the change and redeploy **once**. If it fails again for a
different reason, repeat this workflow. If it fails again for the same reason,
stop.

Before any redeploy of an existing project, check `source` with
`get_project_status`:

- `source: "internal"` → `project_upload` with `update: true`, then
  `update_project`
- `source: "github"` → `external_repo` with `repo_update` or `repo_write_file`

Calling the wrong one returns `SOURCE_MISMATCH`.

## Authorization errors

If a tool call returns an authorization or re-authorization error, this is not a
deployment problem and there is nothing to fix in the code.

Tell the user to reconnect the AI SPACE plugin in ChatGPT's settings and sign in
to their Cafe24 account again. Do not send them to a login page inside the
product — the connector's own authorization flow is what needs to run.

After two consecutive authorization failures, stop and report rather than
retrying.

## The build failed but the site still works

That is expected. A failed build leaves the previous version running. The user
has not lost their live site — say so, because the failure message alone reads
as though everything is down.

## What you cannot do here

Rollback, project deletion and power control are not available through this
connector. If recovery needs one of those, direct the user to the Cafe24 web
console: Hosting → My Service Management → AI SPACE console.

## Do not infer

Build quotas, plan limits and retention periods change. Do not quote numbers from
memory — point the user to `https://aispacedocs-docs.mycafe24.ai`.
