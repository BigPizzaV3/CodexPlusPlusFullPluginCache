# Cafe24 AI SPACE — platform rules for generated code

Violating any of these causes a build failure or silent data loss.

## Runtime detection

The platform decides the runtime from the files at the repository root.

| Runtime | Detected by | Version | Port your app must bind |
|---|---|---|---|
| Static | `index.html` alone | Nginx | n/a — served directly |
| Node.js | `package.json` | 20 | `3000` on `0.0.0.0` |
| Python | `requirements.txt` | 3.11 | `8000` on `0.0.0.0` |
| PHP | `composer.json` or `*.php` | 8.2 (Apache) | n/a — port 80 handled by Apache |

Go, Java and Rust are not supported.

Binding to `127.0.0.1` instead of `0.0.0.0` produces a project that builds
successfully and then never answers a request.

## Forbidden files

Never generate any of these. The platform builds from its own runtime images and
terminates TLS and routing itself.

- `Dockerfile`, `docker-compose.yml`, `.dockerignore`
- `nginx.conf`, Apache `httpd.conf` / `vhost` files
- Any file that sets the listening port from outside the app code

## Databases

MySQL, PostgreSQL, SQLite and Redis are available. Connection details are
injected by the server as environment variables. **Read them. Never write them.**

```
DB_HOST   DB_PORT   DB_NAME   DB_USER   DB_PASSWORD
REDIS_HOST   REDIS_PORT
```

The variable is `DB_USER`, **not** `DB_USERNAME`. Using the wrong name is the
single most common cause of "cannot connect to database" after a successful
deployment.

Do not put database credentials in `.env`, in code, or in a config file. The
server protects these variables; attempting to set them through `project_env`
will not take effect.

A SQLite file must live under `/app/user_data/`.

## Persistence

Only `/app/user_data/` survives a redeploy. The application directory and `/tmp`
are recreated from scratch every time.

Anything the user will expect to still be there tomorrow — uploads, generated
files, a SQLite database, cached artifacts — must be written under
`/app/user_data/`.

## Secrets

Application secrets go in environment variables through `project_env`, and are
read by server-side code only.

Never place a secret in a static site's JavaScript, in HTML, or in any file
served to the browser. Everything under a static runtime is public.

## Naming

`project_name` describes the site and nothing else: `coffeeshop`, `blog`,
`invoice-tool`. It must not contain the user's account ID — the server adds that
prefix when it builds the domain:

```
https://{account-id}-{project-name}.mycafe24.ai
```

SSL is issued automatically. The user does not buy or configure a certificate.
