# Access & Payments Setup — GHL → VPS → ChatGPT

Manual for connecting the $5 GHL checkout to the plugin's OAuth-protected MCP server. Built for: one-time $5 = lifetime access, admission by checkout email (`same-email` match) with license-code fallback, refunds revoke access.

```
Buyer flow:

1. ads.mikeauton.com/simple  →  GHL checkout ($5, buyer enters email)
2. GHL "Payment Received" workflow  →  webhook POST to VPS  { action: "grant", email }
3. VPS SQLite: email → active license (+ license code)
4. GHL confirmation email tells the buyer: "Open ChatGPT, add The Ad Machine, sign in with this email"
5. In ChatGPT: user adds/connects the plugin → server answers 401 → ChatGPT shows oauth login page
6. User enters checkout email...
      email matches an active license  →  token issued  →  plugin works
      email not found                  →  enter license code from receipt email → server binds
                                                                 that ChatGPT email to the license → works
      neither works                    →  "no active license" + link to checkout page
7. Refund / chargeback workflow in GHL  →  webhook { action: "revoke", email }  →  access dies on next request
```

Money lives in GHL. Identity + authorization + the knowledge base live on your VPS. ChatGPT is just the OAuth client.

---

## 1. Deploy the new server (VPS side)

The access layer ships in the same repo (`server.mjs` v1.1.0 + SQLite). New `.env` keys:

| Key | Value |
| --- | --- |
| `PUBLIC_URL` | `https://mcp.mikeauton.com` (OAuth issuer; no trailing slash) |
| `ENFORCE_OAUTH` | `0` while you build the GHL side → `1` when live (section 4) |
| `OAUTH_SECRET` | `openssl rand -hex 32` (signs tokens; rotating kills all issued tokens) |
| `ENTITLEMENT_SECRET` | `openssl rand -hex 32` (shared secret for the GHL webhook) |
| `DB_PATH` | `./data/ad-machine.db` |
| `OPENAI_APPS_CHALLENGE` | rotate per portal challenge, as before |

Deploy (same machine as before):

```bash
# from your Mac
scp Drop-Dead-Simple-Ad-Machine.zip you@your-vps:/tmp/

# on the VPS
sudo systemctl stop ad-machine
sudo cp /opt/drop-dead-simple-ad-machine/.env /tmp/env-backup      # keep secrets!
cd /opt && sudo rm -rf drop-dead-simple-ad-machine
sudo unzip /tmp/Drop-Dead-Simple-Ad-Machine.zip -d /opt/
sudo mv /opt/Drop-Dead-Simple-Ad-Machine /opt/drop-dead-simple-ad-machine
sudo cp /tmp/env-backup /opt/drop-dead-simple-ad-machine/.env
cd /opt/drop-dead-simple-ad-machine
sudo npm install --omit=dev
# add the NEW keys to .env (PUBLIC_URL, OAUTH_SECRET, ENTITLEMENT_SECRET, DB_PATH, ENFORCE_OAUTH=0)
sudo mkdir -p data && sudo chown -R www-data:www-data .
sudo systemctl daemon-reload
sudo systemctl restart ad-machine
```

Verify before touching OAuth:

```bash
curl http://127.0.0.1:8787/health                                   # {"ok":true}
curl http://127.0.0.1:8787/.well-known/oauth-authorization-server    # JSON with token_endpoint
curl http://127.0.0.1:8787/.well-known/oauth-protected-resource      # JSON with authorization_servers
```

With `ENFORCE_OAUTH=0` the existing approved plugin keeps working with no login — nothing changes until you flip the switch.

Self-test the whole auth loop locally anytime:

```bash
cd /opt/drop-dead-simple-ad-machine && sudo -u www-data npm run smoke
# expect: 20 passed, 0 failed
```

---

## 2. GHL side

### 2.1 Product & checkout

- Products → create **"The Ad Machine — Lifetime Access"**, one-time price **$5**.
- Checkout form must collect the **email** (it does by default). This email is the primary identity.
- Landing CTA (already live at ads.mikeauton.com/simple) links to that checkout.

### 2.2 Grant workflow

Workflow trigger: **Payment Received** (choose the $5 product in the filter).

Action 1 — **Webhook**:

- URL: `POST https://mcp.mikeauton.com/entitlement`
- Headers:
  - `X-GHL-Secret: <value of ENTITLEMENT_SECRET>`
  - `Content-Type: application/json`
- Body (raw JSON):

```json
{
  "action": "grant",
  "email": "{{contact.email}}"
}
```

No license code needed in the webhook — the server generates one (`AD-XXXXXXXX`) and returns it in the webhook response (visible in the workflow execution log). If you'd rather control the code yourself (e.g. use the order reference), add `"license_code": "{{order.public_id}}"` or any unique string — the server will store what you send.

Action 2 — **Email** ("Your Ad Machine access is ready"): buyer instructions (copy in section 5).

### 2.3 Revoke workflow

Workflow trigger: **Payment Refunded** (add a second trigger or workflow for chargebacks if you track them).

Action — **Webhook**, same URL + secret header:

```json
{
  "action": "revoke",
  "email": "{{contact.email}}"
}
```

Revocation is effective on the user's next request — no token TTL to wait out, because the middleware re-checks license status on every MCP call.

---

## 3. Flip enforcement on

Only after 2.1–2.3 are wired and you've done one test purchase:

1. On the VPS: set `ENFORCE_OAUTH=1` in `.env`, then `sudo systemctl restart ad-machine`.
2. Smoke check: `curl -o /dev/null -w "%{http_code}" https://mcp.mikeauton.com/mcp -X POST -H 'content-type: application/json' -d '{}'` → expect **401**.
3. Open the **OpenAI portal → Plugins → MCPs → your server → Connect**. It now needs OAuth:
   - MCP Server URL: `https://mcp.mikeauton.com/mcp`
   - Authentication: OAuth (the portal discovers your endpoints from `/.well-known`; if it asks for the issuer, enter `https://mcp.mikeauton.com`)
   - Authorize with an email that has an active license (your test purchase).
4. Wait for the tool scan, confirm both tools still green.

Server-side tool changes aren't part of the ZIP, so no re-upload is needed for this step.

---

## 4. Buyer-facing text (post-purchase page + confirmation email)

```text
YOUR AD MACHINE ACCESS IS READY

Step 1 — Open ChatGPT and add the plugin
  Settings → Apps & Connectors → Developer mode ON (Settings → Apps & Connectors → Advanced).
  Then find "The Ad Machine" in the plugin directory and click Add.
  When asked to sign in, continue to Step 2.

Step 2 — Sign in
  Use the SAME email you used at checkout.
  That's it — the plugin is yours for life.

Different email than your ChatGPT account? No problem.
  On the sign-in screen, enter your license code from this receipt:
  Your license code: {{license_code}}
  (leave the checkout email box empty and use the license code box instead)

Start with: "I want to write an ad for my business."

Questions? eugene@mikeauton.com
```

For the email version, replace `{{license_code}}` with the code from the webhook response if you generate it in GHL; if the server generates it, either (a) fetch it from the workflow execution log manually, or (b) send your own code via `license_code` in the webhook and mail that value. Simplest reliable setup: GHL sends `license_code` = the GHL order/payment reference in both the webhook and the email — then the email always matches the license.

---

## 5. Test matrix (run before and after going live)

| # | Scenario | Expected |
| --- | --- | --- |
| 1 | Test purchase, then connect with the same email | Ad machine works immediately |
| 2 | Connect with a *different* email, enter license code from receipt | Works, email bound once |
| 3 | Connect with an email that never bought | Sign-in screen rejects; offers checkout link |
| 4 | Reuse one license code to bind a *third* email | Code is already bound → rejected (protects against sharing one code door-to-door); contact support to rebind manually |
| 5 | Refund the test buyer in GHL | Next request from that user → 403 "License no longer active" |
| 6 | Wrong webhook secret to /entitlement | 401 |
| 7 | `npm run smoke` | 20/20 |

---

## 6. Admin cheatsheet (VPS)

License data is one SQLite file: `/opt/drop-dead-simple-ad-machine/data/ad-machine.db`.

```bash
sqlite3 /opt/drop-dead-simple-ad-machine/data/ad-machine.db

.tables               -- entitlements, oauth_clients, auth_codes, refresh_tokens
SELECT email, license_code, status, updated_at FROM entitlements ORDER BY updated_at DESC;

-- re-bind a license to a new email (support case)
UPDATE entitlements SET email='new@email.com', updated_at=datetime('now') WHERE license_code='AD-XXXXXXXX';
UPDATE entitlements SET status='active', updated_at=datetime('now') WHERE email='new@email.com';

-- revoke manually
UPDATE entitlements SET status='revoked' WHERE email='someone@email.com';
DELETE FROM refresh_tokens WHERE email='someone@email.com';
```

(Rebinds require the previous email to not exist as another row — if it does, merge first.)

Backup = copy the one `.db` file. Restores are trivial.

---

## 7. Troubleshooting

| Symptom | Fix |
| --- | --- |
| `/mcp` returns 200 without login after flip | `ENFORCE_OAUTH` not `1`, or service didn't restart (`systemctl show ad-machine -p EnvironmentFiles`) |
| User stuck in connect loop | They're signing in with an email that has no license → use the license code path (section 4) |
| "License is no longer active" right after purchase | Revoke workflow fired early, or webhook `action` typo — check the workflow execution log + this server's `/entitlement` 401s in `journalctl -u ad-machine` |
| better-sqlite3 fails to install on VPS | `sudo apt install -y build-essential python3` then `npm rebuild better-sqlite3` (prebuilt binaries cover most cases) |
| Portal can't discover OAuth | `PUBLIC_URL` must match your real HTTPS origin with no trailing slash; both `/.well-known` URLs must answer 200 over the public domain |
| Challenge token circle | `OPENAI_APPS_CHALLENGE` unchanged + `systemctl restart ad-machine` |

## 8. Security notes

- Both secrets live only in `/opt/drop-dead-simple-ad-machine/.env` — never in the repo/ZIP.
- All OAuth state (verifiers, authorization codes) is single-use, 10-minute TTL, server-side stored — replay is rejected.
- Access tokens are HS256 JWTs (30 days) with refresh rotation (1 year); entitlement status is checked on **every** MCP request, so refunds cut access instantly regardless of token TTL.
- Revocation also deletes refresh tokens, so a revoked user can't silently mint new tokens.
- No user conversation content is stored anywhere; the knowledge base files are static.
- HTTPS only (nginx + certbot already in place); consider nginx `limit_req` on `/authorize*` and `/token` if you ever see abuse.
