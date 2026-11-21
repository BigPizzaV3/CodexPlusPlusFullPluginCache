---
name: deploy-new-app
description: Build a web application from the user's description and deploy it live on Cafe24 AI SPACE. Use when the user wants a new site, page, or app created and published — for example "make me a coffee shop homepage and put it online", "build a simple booking form and deploy it", or "I need a landing page for my product". Do not use when the user already has code to upload (use deploy-existing-code) or when a deployment has already failed (use troubleshoot-deploy).
---

# Deploy a new app on Cafe24 AI SPACE

You write the code, then publish it with the AI SPACE tools. The platform handles
the container, the domain and the SSL certificate. Reply in the user's language.

## Expected input

A description of what the user wants. If the description is one line, do not
interrogate them — pick sensible defaults, build it, and let them refine it after
they can see the live site.

## Steps

### 1. Reserve a space

Call `list_my_spaces`. A space is deployable when `project_id` is `null`.

- No empty space → stop. Tell the user to free one or add a space in the Cafe24
  web console. Do not try to deploy into an occupied space.
- Exactly one empty space → use it.
- More than one → ask which one, then pass its `space_id`.

### 2. Choose the runtime yourself

Decide from what the user asked for. Do not ask them.

| What they want | Runtime | Entry file that must exist at the repo root | Port your code must listen on |
|---|---|---|---|
| Landing page, brochure site, portfolio | Static (Nginx) | `index.html` | n/a |
| API, Express or Next.js app | Node.js 20 | `package.json` | **3000**, host `0.0.0.0` |
| FastAPI, Flask or Django app | Python 3.11 | `requirements.txt` | **8000**, host `0.0.0.0` |
| PHP app, board, WordPress-style site | PHP 8.2 (Apache) | `composer.json` or `index.php` | n/a |

Go, Java and Rust are **not supported**. If asked, say so and offer one of the
four above.

### 3. Write the code under the platform's rules

Read `references/runtime-rules.md` before writing files. The four rules that
break deployments most often:

1. Never create `Dockerfile`, `docker-compose.yml`, or Nginx/Apache config files.
2. Never write database credentials. The server injects `DB_HOST`, `DB_PORT`,
   `DB_NAME`, **`DB_USER`** (not `DB_USERNAME`), `DB_PASSWORD`. Read them only.
3. Anything that must survive a redeploy goes under `/app/user_data/`.
4. Node listens on 3000, Python on 8000, both on `0.0.0.0`.

Pick a `project_name` that describes the site only — for example `coffeeshop`.
Never put the user's account ID in it; the server prefixes it automatically.

### 4. Upload the files

**You are running inside ChatGPT, which has no shell. Always use the JSON path.**

1. `project_upload` with `action: "create_session"`, `mode: "json"`, the file list
   and the repo name. The mode is locked at this moment and cannot be changed
   afterwards — a new session is required to switch.
2. `upload_json` with the returned `batch_id`. Limits: **3 MB per file, 10 files
   per request, 5 MB total.** Send text files as plain text with no `encoding`
   field. Only binary files get `encoding: "base64"`.
3. `project_upload` with `action: "finalize"`, `deploy: true`, and the `space_id`
   from step 1.

If the project is larger than those limits, do not try to split it endlessly.
Tell the user and offer the two alternatives: connect a GitHub repository with
`external_repo`, or deploy from a public Git URL with `deploy_project`.

On a failed upload: a 4xx means stop immediately, a 5xx is worth one or two
retries, a timeout is worth one. **Every retry starts from a new
`create_session`** — never reuse a `batch_id` whose first attempt failed.

### 5. Report progress honestly

Call with `wait: false` and poll `get_project_status` every 5–10 seconds. Show a
checklist and tick only what you have actually observed in a response. Never mark
a step complete because you assume it finished.

```
[AI SPACE deploy — coffeeshop]
✅ 1/4 files uploaded
✅ 2/4 runtime detected: Node.js 20
⏳ 3/4 building and starting…
⬜ 4/4 domain and SSL
```

### 6. Confirm it is actually reachable

A successful deployment is not the same as a reachable site. Call `site_verify`
on `https://{account}-{project}.mycafe24.ai` before you tell the user it is live.
Then give them the URL.

## Rules you must not break

- **Stop after two identical failures.** If the same call fails the same way
  twice, stop and report. Never loop — on a free trial each build consumes one of
  a limited number of builds.
- **Do not use `force: true`.** If a space is occupied, offer a different project
  name, an update of the existing project, or deletion in the web console.
- Never put an API key or any secret into client-side JavaScript on a static
  site. Every visitor can read it. Use a server runtime and environment variables.
- Rollback, project deletion, power control and billing are **not available
  through this connector.** Direct the user to the Cafe24 web console.

## Do not infer

Free-trial limits, prices, plan quotas and refund policy change. Do not state
them from memory — point the user to `https://aispacedocs-docs.mycafe24.ai`.
