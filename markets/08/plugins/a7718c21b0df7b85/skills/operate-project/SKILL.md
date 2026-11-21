---
name: operate-project
description: Run day-to-day operations on a project already deployed on Cafe24 AI SPACE — review status and spaces, set or remove environment variables, create a backup, restrict access by IP or country, and add or remove Redis and Memcached. Use when the user asks what they have running, wants to change a setting, take a backup, or block traffic. Do not use for deploying or updating code, or for diagnosing a failure.
---

# Operate a deployed project

Reply in the user's language.

## Find the project first

`list_my_projects` shows what the user has. `list_my_spaces` shows their spaces
with specification, quota, connection limit and whether each one is occupied.
`get_project_status` gives runtime, resource usage and deployment history for a
single project.

If the user names a project ambiguously, list what exists and ask. Never guess
which project a destructive setting applies to.

## Confirm before you change anything

Read-only calls go straight through. **Anything that changes state follows the
same three beats every time:**

1. Name the project explicitly.
2. Summarise what will change.
3. Ask "shall I go ahead?" and wait.

## What you can do here

### Environment variables — `project_env`

`get` lists them, `set` creates or updates, `delete` removes one key.

These are the application's own configuration values. Database and Redis
credentials are injected and protected by the server — do not try to set them,
and tell the user they are already available to their code.

A change restarts the container in place. It takes effect in seconds and does not
require a redeploy.

### Backups — `backup_project`

The project must be in `success` state. The backup contains the application
files, everything under `/app/user_data/`, and an automatic dump of any MySQL or
PostgreSQL database attached to the project.

The response carries `backup_download_url`. **Give that URL to the user as-is and
tell them it expires** — retention differs between free and paid plans, so point
them at the documentation rather than quoting a number.

### Access control — `project_acl`

| Action | Effect |
|---|---|
| `set_ip` with `mode: "deny"` | blocks that IP or CIDR range |
| `set_ip` with `mode: "allow"` | blocks **everyone except** that IP |
| `set_geo` | blocks a country by ISO 3166-1 code, either all requests or POST only |
| `clear_ip` / `clear_geo` | removes the rules |
| `get_acl` | shows what is currently in force |

**Warn before an allow rule.** Whitelist mode blocks every address that is not
listed — including the user's own, if their address changes or they are on
mobile. Confirm they understand they may lock themselves out, and tell them
`clear_ip` is the way back.

### Add-ons — `project_option`

Adds or removes Redis and Memcached on Pod-mode projects.

**Removing an add-on deletes everything stored in it, and re-adding gives an
empty instance.** Say that before you call it, and confirm.

### Importing a database — `import_database` then `finalize_db_import`

`import_database` opens an upload session and returns a URL. Nothing is written
yet. After the `.sql` or `.sql.gz` file is uploaded, `finalize_db_import` applies
it.

**Applying a dump can drop and overwrite existing tables. It cannot be undone.**
Offer to take a backup first, then get explicit confirmation.

### Custom domains

Available on paid plans. SSL is issued free and automatically when the domain is
connected — the user does not buy a certificate. DNS propagation can take up to
48 hours. For the current limits per account and per project, point to the
documentation.

## What is not available through this connector

Rollback, project deletion, power on/off, plan changes and payment are not
exposed here. Do not attempt a workaround. Direct the user to the Cafe24 web
console: Hosting → My Service Management → AI SPACE console.

## Do not infer

Prices, plan quotas, backup retention periods, free-trial limits and domain
counts all change. Never state them from memory. Point the user to
`https://aispacedocs-docs.mycafe24.ai`.

## Stop rule

If the same call fails the same way twice, stop and report it. Do not retry in a
loop.
