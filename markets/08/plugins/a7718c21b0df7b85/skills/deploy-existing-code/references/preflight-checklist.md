# Pre-flight checklist for code written elsewhere

Run every item before deploying. Each one corresponds to a failure that is
common enough to be worth checking every single time.

## 1. Is the runtime supported?

PHP 8.2, Node.js 20, Python 3.11 and static HTML are supported. **Go, Java and
Rust are not.** If the project is one of those, stop and tell the user before
touching anything else.

## 2. Is there an entry file at the repository root?

The platform detects the runtime from the root, not from a subdirectory.

| Runtime | Required at root |
|---|---|
| Node.js | `package.json` |
| Python | `requirements.txt` |
| PHP | `composer.json` or `index.php` |
| Static | `index.html` |

If the app lives in `src/` or `app/` with nothing at the root, add the entry file
or restructure. A monorepo needs the deployable app hoisted to the root.

## 3. Does it bind the right host and port?

- Node.js → `3000`
- Python → `8000`
- Both must bind `0.0.0.0`, never `127.0.0.1` or `localhost`

Look for `app.listen(...)`, `uvicorn.run(...)`, `PORT` defaults, and Procfile-like
start scripts. Binding to loopback produces a project that builds cleanly and
then never answers a request — one of the hardest failures for a user to diagnose.

## 4. Are database credentials hard-coded?

Replace every hard-coded host, user, password and database name with the
server-injected environment variables:

```
DB_HOST   DB_PORT   DB_NAME   DB_USER   DB_PASSWORD
REDIS_HOST   REDIS_PORT
```

The variable is `DB_USER`, **not** `DB_USERNAME`. Frameworks that default to
`DB_USERNAME` (some Laravel and Node ORM setups do) must be adjusted.

Delete the database entries from `.env`. Anything the app still needs from `.env`
becomes an environment variable set through `project_env` after deployment.

## 5. Where does it write files?

Only `/app/user_data/` survives a redeploy. Everything else is rebuilt from
scratch.

Check upload directories, log paths, generated files, cache directories and any
SQLite file. Repoint them under `/app/user_data/`. If you leave one as-is, say so
explicitly in the "left as-is" list so the user can decide.

## 6. Are there forbidden files?

Delete `Dockerfile`, `docker-compose.yml`, `.dockerignore`, `nginx.conf` and any
Apache vhost config. The platform builds from its own images and handles routing
and TLS. Leaving them in place fails the build.

## 7. Does it fit the upload limits?

ChatGPT has no shell, so uploads go through the JSON path: 3 MB per file, 10
files per request, 5 MB total.

Over the limit? Do not shard endlessly. Switch to GitHub (`external_repo` →
`repo_connect` → `repo_deploy`) or a public Git URL (`deploy_project`).
`node_modules`, `vendor`, `.git` and build output should never be uploaded — they
are rebuilt on the server.

## 8. Are there secrets in client-side files?

Any key in front-end JavaScript, HTML or a static asset is public. Move it to an
environment variable read by server-side code, and tell the user the key should
be rotated if it was already committed somewhere public.
