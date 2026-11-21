# The Ad Machine

The Ad Machine interviews you about your offer, then writes a ready-to-use Forever Ad, complete with headlines. No spreadsheets, copywriting skills or tech expertise needed. Just answer some questions and let the machine do the writing.

ChatGPT MCP plugin at https://ads.mikeauton.com/simple. For ad budgets from $5 to $5k a day — lead generation, ecom and direct sales.

## What this does

- Exposes a Streamable HTTP MCP endpoint at `/mcp`
- Server instructions run the full **guided** interview: 16 questions, one at a time, warm coach-like tone, then a finished ad (5 headlines + 5 first lines + shared body)
- Exposes `search_knowledge` and `read_knowledge_document` over the knowledge in `./knowledge`
- `./knowledge/forever-ad-launcher-ad-templates.md` holds the three Forever Ad copy structures (Event/Webinar, E-commerce, Lead Gen/Sales); the matching template is fetched at generation time
- Includes a skill (`skills/the-ad-machine/SKILL.md`) for the plugin submission portal

This first version intentionally has NO OAuth and NO GHL entitlement check. It is for getting the basic experience working before adding authentication.

## 1. Install

Use Node 20+.

```bash
npm install
```

## 2. Run

```bash
npm start
```

Default local endpoint:

```text
http://127.0.0.1:8787/mcp
```

Health check:

```text
http://127.0.0.1:8787/health
```

## 3. Put it behind HTTPS

ChatGPT's remote MCP connection needs a public HTTPS endpoint. OpenAI's docs use `/mcp` as the typical path.

Production endpoint:

```text
https://mcp.mikeauton.com/mcp
```

Use Nginx, Caddy, or another TLS reverse proxy in front of Node. `nginx/ad-machine.conf` and `scripts/install-ubuntu.sh` are ready to use.

## 4. Connect in ChatGPT Developer Mode

Enable Developer Mode in ChatGPT, then add the MCP server using:

```text
https://mcp.mikeauton.com/mcp
```

After connecting, test with: "I want to write an ad for my business."

Refresh the plugin connection after changing tools or metadata.

## 5. Paid access (GHL → OAuth)

For the full setup manual — GHL checkout webhook, entitlements, OAuth user flow, revocation — see **docs/ACCESS-SETUP.md**. Summary of the pipeline:

```text
GHL checkout ($5)
   ↓ webhook (payment received)
VPS entitlement store (SQLite)
   ↓ OAuth 2.1 gate on /mcp (ENFORCE_OAUTH=1)
ChatGPT user signs in with checkout email or license code
```

The GHL Payment Received trigger supports successful one-time purchases, and HighLevel can send outbound webhook requests to an external service. We can therefore keep billing in GHL while your VPS remains the authorization/knowledge layer.

## Important

Do not put GHL API keys, OpenAI API keys, or OAuth client secrets in these source files. Use environment variables on the VPS.

Do not publish this unauthenticated version. It is only the first development milestone.
