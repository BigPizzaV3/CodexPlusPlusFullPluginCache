# Terraform Academy ChatGPT Plugin

A ChatGPT / Codex plugin that delivers Terraform Academy education inside ChatGPT: Terraform Associate (003) certification practice, HCL troubleshooting, guided Terraform labs, and multi-cloud certification coaching (AWS, Azure, GCP, Kubernetes, Docker).

> **Full feature & version specification:** see [VERSIONS.md](VERSIONS.md).

## Live status

Published in the ChatGPT plugin store. Both the skills and the MCP server are live, including OAuth sign-in.

- **MCP URL:** `https://mcp.terraformacademy.app/mcp`
- **Sign-in URL:** `https://mcp.terraformacademy.app/oauth/authorize`
- **Token URL:** `https://mcp.terraformacademy.app/oauth/token`
- **OAuth discovery:** `https://mcp.terraformacademy.app/.well-known/oauth-authorization-server`
- **MCP server key:** `terraform-academy-mcp`
- **Auth mode:** `mixed` — free tier without an account, subscriber unlock via OAuth sign-in
- **Skills:** `getting-started`, `terraform-associate`, `terraform-troubleshooting`, `cloud-certifications`, `branding`
- **Tools:** `list_certification_tracks`, `list_labs`, `get_lab`, `get_lab_content`, `check_lab_code`, `get_quiz_questions`, `render_quiz`, `check_answer`, `list_articles`, `get_article`, `list_games`, `get_game`, `check_game_answer`, `list_foundations`, `get_foundation`, `list_speed_rounds`, `start_speed_round`, `render_dashboard`

## Where this lives in the repo

- MCP worker (Cloudflare Worker): [`max/cloudflare-worker/mcp-worker/`](../../max/cloudflare-worker/mcp-worker/)
- Repo index: [`README.md`](../../README.md)

## What is inside

```
terraform-academy/
├── plugin.json                  Portable Agent Plugins manifest
├── mcp.json                     MCP server declaration (streamable-http)
├── skills/
│   ├── getting-started/         Onboarding skill
│   ├── terraform-associate/     Certification quiz coach + question bank
│   │   └── references/question-bank.md
│   ├── terraform-troubleshooting/  HCL debugging + guided labs
│   ├── cloud-certifications/    AWS, Azure, GCP, Kubernetes, Docker coaching
│   └── branding/                Brand system: colors, typography, voice
├── assets/
│   ├── icon.png                 Composer icon (brand gradient)
│   └── logo.png                 Directory listing logo
└── tools/
    ├── export-questions.mjs     Regenerates the Terraform Associate question bank
    └── export-all-questions.mjs Regenerates the multi-provider bank for the MCP worker
```

## Branded dashboard (MCP Apps UI)

The plugin ships two branded MCP Apps UI resources:

- **Dashboard** (`ui://widget/dashboard.html`) — the `render_dashboard` tool renders
  profile (XP, octagons, completions, tier) and domain readiness bars.
- **Interactive quiz** (`ui://widget/quiz.html`) — the `render_quiz` tool renders
  clickable questions one at a time with a working light bulb hint, in-widget
  grading via `check_answer`, and a results summary.

Both are served via `resources/read` with `mimeType: text/html;profile=mcp-app`,
use the MCP Apps `ui/*` bridge over `postMessage`, and follow the UI guidelines:
light system surface with Terraform Academy orange accents. Widget sources live in
`data/dashboard-ui.js` and `data/quiz-ui.js`.

## Analytics (chatgpt_mcp)

The worker logs every MCP tool call to the Supabase `integration_events` table
(source `chatgpt_mcp`) with identity, subscription tier, and outcome (e.g.
`is_correct` for graded answers). Writes are fire-and-forget and disabled until
`SUPABASE_SERVICE_KEY` is set. See `max/supabase/20261106_chatgpt_integration_analytics.sql`
for the table DDL and reporting queries.

## Branding

Colors are contextual and follow the content a user is looking at:

| Surface | Color |
|---------|-------|
| Plugin chrome (anything that is not a quiz or lab) | Terraform Academy orange `#FF6B00` |
| Terraform / HashiCorp courses & quizzes | HashiCorp purple `#7B42BC` |
| Azure labs & courses | Azure blue `#0078D4` |
| GCP labs & courses | Google Cloud multi-color `#4285F4` / `#EA4335` / `#FBBC05` / `#34A853` |
| AWS labs & courses | AWS orange `#FF9900` |
| Security & IAM | Deep red `#B91C1C` |
| Foundations courses | Keep their current branding |

Rules:

- Quizzes keep whatever branding they already carry; never re-skin a quiz to the
  plugin chrome color.
- The plugin chrome (`brandColor` / `brandColorDark` in `plugin.json`) is the
  Terraform Academy orange `#FF6B00`.
- The logo keeps the Terraform Academy "TA" mark on the dark `#0B1020` panel.

> Note: Terraform uses HashiCorp purple `#7B42BC`. Azure's official color is
> blue, not purple.

The authoritative color and voice rules live in `skills/branding/SKILL.md`.
Apply that skill to any content you generate so the palette stays consistent.

## Legacy learning content (partially converted)

Older standalone learning-scenario labs and practice quizzes live in the repo
but are only partially wired into the MCP server:

- `Interactive-labs/` — 200+ legacy code/selector labs. The 26 Terraform and
  cloud code labs (with starter files + a checkable solution) are converted into
  the MCP interactive mode by `scripts/export-legacy-labs.py`
  (`data/legacy-labs.js` + `data/legacy-lab-content.js`). CI/CD, Docker, game,
  and speed-round files remain unconverted because they are not Terraform code labs.
- `Provider Tests/` — older practice quizzes (Azure AZ-104/204/305/500, GitOps).
- `Quuizzes/` — academy quizzes (API, Azure, CI-CD, GCP, Google Cloud).
- `Preview/` — preview builds (Azure DevOps CI-CD lab, Consul Associate 003).

Converting the remaining quiz and speed-round content is a follow-up task.

## Quiz hints

Every quiz question offers a "💡 Need a hint?" affordance. Hints are hidden by
default, are conceptual (they guide reasoning without revealing the answer or
eliminating choices), never change the score, and are tracked as assisted
answers in the readiness report. The hint accent color is warm amber `#FFB020`.

## Regenerate the question banks and lab catalog

- `tools/export-questions.mjs` regenerates the Terraform Associate markdown reference for the skill.
- `tools/export-all-questions.mjs` regenerates the combined multi-provider bank for the MCP worker (2,800+ questions across Terraform, AWS, Azure, GCP, Kubernetes, and Docker).
- `scripts/export-mcp-labs.py` regenerates `data/labs.js` (full lab catalog, 300+ labs) and `data/lab-content.js` (interactive code-block content) from `max/labs/*.html`.
- `scripts/export-legacy-labs.py` regenerates `data/legacy-labs.js` and `data/legacy-lab-content.js` from the converted `Interactive-labs/` code labs.
- `scripts/export-mcp-games.mjs` regenerates `data/games.js` from the `Interactive-labs/Games/` matchup and build-sequence games.
- `scripts/export-mcp-speedrounds.mjs` regenerates `data/speed-rounds.js` from the `Interactive-labs/V2/speed-rounds/` timed MCQ rounds.
- `scripts/export-mcp-foundations.py` regenerates `data/foundations.js` from the `max/*foundations*.html` courses.

```bash
node tools/export-all-questions.mjs
python3 scripts/export-mcp-labs.py
python3 scripts/export-legacy-labs.py
node scripts/export-mcp-games.mjs
node scripts/export-mcp-speedrounds.mjs
python3 scripts/export-mcp-foundations.py
```

## Test locally in ChatGPT desktop

1. Install the ChatGPT desktop app.
2. Restart it so it picks up `.agents/plugins/marketplace.json` at the repo root.
3. Open the Plugins Directory, choose the "Terraform Academy (local)" marketplace, and install the plugin.
4. Start a new chat and try: "Quiz me on Terraform Associate concepts."

## Package the ZIP for submission

From the plugin folder:

```bash
cd chatgpt-plugin/terraform-academy
zip -r /tmp/terraform-academy-plugin.zip . -x ".*"
```

## Submit to the directory

1. Go to https://platform.openai.com/plugins and select **Upload new or existing plugin**.
2. Choose your verified developer identity.
3. Upload `terraform-academy-plugin.zip`.
4. Resolve any automated findings in **Metadata & Skills**.
4. Complete the review information and submit. Connect and scan the MCP server and resolve any findings first.
6. After approval, choose **Publish plugin**.

## MCP server (subscriber content)

The MCP server is a Cloudflare Worker at `max/cloudflare-worker/mcp-worker/`. It implements the MCP `streamable-http` transport and exposes these tools:

- `list_certification_tracks` - provider, exam code, level, premium flag
- `list_labs` - labs with locked flags for free users
- `get_lab` - lab details fetched from the live site; premium labs gated
- `get_quiz_questions` - Terraform Associate questions without answers
- `check_answer` - grades a question and returns the explanation
- `render_quiz` - renders the interactive quiz widget (clickable answers, light bulb hint, grading, results)
- `list_articles` - lists Pro Tips blog articles (SRE Pro Tips, Pipeline Perspective, From the Source, HashiCorp Solutions); read live from Supabase so new posts sync automatically
- `get_article` - returns a single article by slug; gated articles require Pro/MAX
- `list_foundations` - lists the three Foundations courses (Terraform, OpenTofu, Terraform Cloud)
- `get_foundation` - returns a course's module and lesson outline with excerpts
- `list_speed_rounds` - lists timed quiz speed rounds by provider (AWS, Azure, GCP)
- `start_speed_round` - starts a timed round; grade with check_answer
- `render_dashboard` - renders the branded learning dashboard widget (profile, XP, readiness)
- `list_games` - lists interactive learning games (term-definition matchup and Terraform build-sequence)
- `get_game` - starts a game and returns terms/definitions or shuffled build steps (answers withheld)
- `check_game_answer` - grades a matchup or sequence answer and reveals the correct answer after grading
- `get_lab_content` - starts the interactive code-block lab mode: instructions, starter Terraform files, and build objectives
- `check_lab_code` - grades a learner's HCL block against a lab objective (server-side regex, never reveals the solution)

Each tool response includes the resolved `tier` (`free` / `pro` / `max`) so the
model can present subscriber content without a separate tier tool.

Worker data files live in `max/cloudflare-worker/mcp-worker/data/`:
`cert-tracks.js`, `labs.js`, and `question-bank.js`. They are regenerated by
`tools/export-questions.mjs` and `tools/export-all-questions.mjs`.

### Tier gating

With no account token the tier is free. With a token, the worker maps the Supabase JWT to the user using the public anon key, then asks `max-api` for the subscription tier. No service key is stored on this worker. Free users get a sample quiz and see premium labs locked.

### Deploy

1. `npm install -g wrangler` and `wrangler login`
2. Copy the folder out of the repo (required, Wrangler 4.x bug) and deploy:

   ```bash
   rm -rf /tmp/mcp-worker
   cp -r max/cloudflare-worker/mcp-worker /tmp/mcp-worker
   cd /tmp/mcp-worker && wrangler deploy
   ```

3. Configure the worker (generates the one OAuth signing secret; no other secrets needed):

   ```bash
   bash max/cloudflare-worker/mcp-worker/setup-secrets.sh
   ```

The worker is deployed at `https://terraform-academy-mcp.white-cloud-7acd.workers.dev`.

### Custom domain

MCP traffic is served at `https://mcp.terraformacademy.app` (CNAME to `terraformacademy.app`, proxied). `mcp.json` already points at it.

### Test tier gating

Run the live OAuth flow test with your own Terraform Academy account (no service key needed):

```bash
TEST_EMAIL='you@example.com' TEST_PASSWORD='your password' \
  node max/cloudflare-worker/mcp-worker/test/oauth-flow-test.mjs
```

It signs in through the OAuth bridge, exchanges the code, and prints the tier the worker resolves with and without the token.

### Before you submit the MCP version

- Deploy the worker and verify it with a curl POST to `/mcp`.
- Review and finalize the privacy policy and terms pages at `/max/privacy.html` and `/max/terms.html`.
- Replace `review.demo_recording_url` with an accessible walkthrough video.
- Tighten `ALLOWED_REDIRECT_HOSTS` in `worker.js` to OpenAI's OAuth callback host once you have it.
- When OpenAI asks for domain verification, set the token: `wrangler secret put OPENAI_APP_CHALLENGE '<token>'`. The worker serves it at `/.well-known/openai-apps-challenge`.
- Submit one ZIP that includes both the skills and `mcp.json`.

### OAuth (same Supabase auth, free)

The worker runs a small OAuth 2.0 bridge that fronts your existing Supabase auth, so users sign in with their current Terraform Academy credentials. No third-party identity provider and no extra cost.

- `GET /oauth/authorize` shows a branded sign-in form and exchanges Supabase credentials for an authorization code (PKCE).
- `POST /oauth/token` exchanges the code for the Supabase access token.
- `GET /.well-known/oauth-authorization-server` publishes discovery metadata.

`mcp.json` declares `auth.type: "mixed"`: free users get the free tier without logging in, and Pro/MAX users connect via OAuth to unlock subscriber content. The authorization code is an HMAC-SHA256 signed blob keyed by `OAUTH_SIGNING_SECRET`, generated automatically by `setup-secrets.sh`.
