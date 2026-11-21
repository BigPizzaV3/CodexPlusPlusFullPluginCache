# Known failure causes, in order of frequency

Each entry: what the user sees, what to look for, and how to fix it.

## 1. A Dockerfile is present

**Symptom** — the build fails early, often before any dependency install.

**Look for** — `Dockerfile`, `docker-compose.yml`, `.dockerignore`, `nginx.conf`,
Apache vhost files.

**Fix** — delete them. The platform builds from its own runtime images. There is
nothing for the user to configure about the container, the web server, the port
mapping or TLS.

## 2. Bound to the wrong host or port

**Symptom** — the build succeeds, the deployment reports success, and the site
never answers. `site_verify` times out or returns a gateway error.

**Look for** — `localhost` or `127.0.0.1` in a `listen` call; a port that is not
3000 for Node.js or 8000 for Python; a `PORT` environment default that overrides
the correct value.

**Fix** — bind `0.0.0.0` on 3000 (Node.js) or 8000 (Python). PHP and static sites
are served by the platform and need no port configuration.

This is the failure users find hardest to diagnose alone, because every status
message says the deployment succeeded.

## 3. `DB_USERNAME` instead of `DB_USER`

**Symptom** — the site loads but every database operation fails; the log shows an
access-denied or authentication error, often with an empty user name.

**Look for** — `DB_USERNAME` anywhere in the code, in `.env`, or in a framework
config file. Some Laravel and Node ORM templates default to it.

**Fix** — the injected variable is `DB_USER`. Change every reference.

The full injected set is `DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER`,
`DB_PASSWORD`, plus `REDIS_HOST` and `REDIS_PORT`. The server owns these — they
cannot be overridden through `project_env`.

## 4. Runtime detected incorrectly

**Symptom** — the wrong runtime appears in `get_project_status`; a Node app is
served as static files, or a Python app is treated as PHP.

**Look for** — no entry file at the repository root. Detection reads the root
only: `package.json` → Node.js 20, `requirements.txt` → Python 3.11,
`composer.json` or `*.php` → PHP 8.2, `index.html` alone → Static.

**Fix** — hoist the deployable app to the root, or add the entry file there.

A runtime mismatch cannot be repaired with `update_project`. The project must be
deleted in the web console and deployed again.

## 5. Dependency or syntax failure

**Symptom** — the build log ends inside the install or start step.

**Look for** — the last 20 lines of `get_project_logs`. A missing package, a
version that does not exist, a lockfile that disagrees with the manifest, or a
plain syntax error.

**Fix** — read the actual error to the user rather than guessing, correct it, and
redeploy once.

## 6. Files disappeared after a redeploy

**Symptom** — uploads, a SQLite database or generated files are gone after an
update.

**Cause** — they were written outside `/app/user_data/`. The application
directory and `/tmp` are rebuilt from scratch on every deployment.

**Fix** — repoint the write paths under `/app/user_data/`. The already-lost data
cannot be recovered unless the user took a backup. Say that plainly rather than
implying recovery is possible.

## 7. Build ran out of memory

**Symptom** — the build stops abruptly with no clear application error.

**Look for** — large front-end builds, bundlers running with default heap
settings, very large dependency trees.

**Fix** — reduce the build's footprint, or the user needs a plan with more
memory. Check what their space actually provides with `list_my_spaces` before
suggesting an upgrade.

## 8. Upload was too large

**Symptom** — the JSON upload path returns a 4xx, or the file list was rejected.

**Cause** — inside ChatGPT the limits are 3 MB per file, 10 files per request,
5 MB total.

**Fix** — never shard endlessly. Exclude `node_modules`, `vendor`, `.git` and
build output, which the server rebuilds anyway. If it is still too large, switch
to GitHub (`external_repo`) or a public Git URL (`deploy_project`).

## 9. Wrong update tool for the project's origin

**Symptom** — a `SOURCE_MISMATCH` response.

**Cause** — `update_project` was called on a GitHub-linked project, or
`repo_update` on an uploaded one.

**Fix** — call `get_project_status` and read `source`. `internal` →
`project_upload(update: true)` then `update_project`. `github` → `external_repo`
with `repo_update` or `repo_write_file`.

## 10. One repository, several projects

**Symptom** — an `AMBIGUOUS_PROJECT` response from `external_repo`.

**Fix** — call `list_my_projects`, and pass the exact `project_name` instead of
relying on automatic matching from the repository name.
