# Terraform Academy ChatGPT Plugin — Features & Versions

> The complete, granular product specification for the Terraform Academy ChatGPT
> plugin. This document is intended for reviewers, agents, and future development
> sessions that need the full picture without reading the source.

**Live MCP URL:** `https://mcp.terraformacademy.app/mcp`
**Store package:** `terraform-academy` (Developer: Terraform Academy, category: Developer Tools)
**Repo:** `everybitcounts/everybitcounts.github.io` → `chatgpt-plugin/terraform-academy/`

---

## 1. Positioning

Terraform Academy is an AI-native cloud engineering learning platform inside
ChatGPT. It combines certification practice, interactive hands-on labs, HCL
troubleshooting, Foundations courses, timed speed rounds, learning games, and a
branded progress dashboard. It is not just a question bank: learners write real
Terraform code, debug real HCL, and track readiness without leaving ChatGPT.

---

## 2. Version history

### Versioning protocol (SemVer)
- **MAJOR** (X.0.0): breaking changes — removed/renamed tools, auth model changes, manifest schema changes.
- **MINOR** (0.X.0): new features — new tools, skills, content types, UI resources.
- **PATCH** (0.0.X): fixes, doc updates, non-breaking tweaks.
- **Source of truth:** `plugin.json` → `version`. The worker's `SERVER_INFO.version` mirrors it.
- **Release artifact:** `releases/terraform-academy-plugin-<version>.zip`; the current file is also copied to `~/Downloads`.
- **Changelog:** this section. Every iteration gets a new version number before it ships.

### v1.4.0 (current)
- Removed the OAuth declaration from `mcp.json` (MCP connection is now No
  authentication). This works around the OpenAI directory bug where the MCP tool
  scan hangs after an OAuth connection (the relay redirect back to
  platform.openai.com is dropped), leaving the directory on the stale 5-tool
  snapshot. All tools and UI widgets are served without auth, so discovery now
  completes and surfaces all 20 tools and 3 widgets. The worker still accepts a
  bearer token when present, so OAuth can be re-enabled in a later release once
  the directory scan bug is fixed.

### v1.3.0
- New `get_plugin_diagnostics` tool returns the deployed build id, package
  version, protocol version, the full list of tool names and UI resource URIs,
  and content counts (tracks, questions, labs, games, speed rounds,
  foundations). This distinguishes a deployment problem (ChatGPT running a
  stale tool snapshot) from a behavior problem (model presentation).
- Instructions route version/deployment questions to `get_plugin_diagnostics`.

### v1.2.3
- MCP transport fix: the worker now returns the `Mcp-Session-Id` header on
  `initialize` as required by the streamable-http transport, so strict clients
  (including the plugin directory scanner) can complete the discovery handshake
  and list all 19 tools and 3 UI widgets.

### v1.2.2
- Home screen switched to full dark mode: near-black background, dark surface
  cards, white text, and dark hover accents throughout the content area.
- Removed the gradient container behind the Terraform Academy "A" logo so the
  logo renders free of any chrome in the top bar and menu header.

### v1.2.1
- Home screen polish: removed all emoji glyphs from the drawer and quick-action
  buttons so ChatGPT applies its default component styling; replaced the text
  "TA" mark with the official Terraform Academy "A" logo image in the top bar
  and menu header (with a text fallback if the image cannot load).

### v1.2.0
- **Home screen with command menu** — new `render_home` tool returns an MCP Apps UI
  resource (`ui://app/home.html`): a self-contained app shell with a hamburger that
  opens a slide-out command menu mirroring the Terraform Academy app.
- **Provider → certification drill-down** — pick Terraform & HashiCorp, AWS, Azure,
  Google Cloud, Kubernetes, or Docker and the home screen lists the certification
  tracks that have question banks, each with a Start quiz action that launches the
  interactive quiz widget.
- **Quick actions** — dashboard, labs, games, speed rounds, foundations, and Pro Tips
  articles are reachable as clickable commands, so learners no longer have to guess
  what to ask for.
- **Consistent branded dashboard** — `render_dashboard` now aggregates the learner's
  graded quiz answers (from `integration_events`) per certification track and renders
  real orange readiness bars, replacing ad-hoc model-generated recaps. Falls back to
  provided domain data only when the user has no quiz history.
- Instructions and skills route browsing/menu requests to `render_home` and
  dashboard/profile/progress requests to `render_dashboard`.
- Worker `SERVER_INFO.version` and plugin `version` aligned to `1.2.0`.

### v1.0.0 (initial release)
- 4 skills: `getting-started`, `terraform-associate`, `terraform-troubleshooting`, `cloud-certifications`
- 5 MCP tools: `list_certification_tracks`, `list_labs`, `get_lab`, `get_quiz_questions`, `check_answer`
- Static question bank (Terraform Associate focus) and a hand-curated 8-lab catalog.
- Brand colors: purple `#7B42BC` / cyan `#00D4FF` (later changed).
- Dashboard status at the time: "No authentication" (OAuth not yet reviewed live).

### v1.1.1
- Reduced `defaultPrompt` to the three allowed by the directory guidelines.

### v1.1.0 (superseded by v1.1.1)
- **Interactive quiz widget** — `render_quiz` returns a dedicated MCP Apps UI
  resource (`ui://widget/quiz.html`) with clickable answers, one question at a
  time, progress bar, domain label, in-widget grading and explanations, and a
  results summary. Grading stays server-side via `check_answer`.
- **Working light bulb hint** — expandable "💡 Need a hint?" control inside the
  widget (amber accent, keyboard accessible, preserves the selected answer).
- `check_answer` and `get_quiz_questions` marked `openai/widgetAccessible`.
- Skills now prefer `render_quiz` and fall back to conversational quizzes.
- Worker `SERVER_INFO.version` and plugin `version` aligned to `1.1.0`.

### v1.0.2 (superseded by v1.1.0)
- **MCP analytics pipeline** — every tool call logged to Supabase `integration_events`
  (source `chatgpt_mcp`) with identity, tier, and outcome; fired fire-and-forget.
- **Admin portal "ChatGPT MCP" analytics view** — unique learners, tool calls,
  quiz answers, lab submissions, activity/tier breakdowns, recent events.
- Worker `SERVER_INFO.version` and plugin `version` aligned to `1.0.2`.

### v1.0.1 (released)
- **Branding skill added** (`branding`) — single source of truth for colors and voice.
- **Store metadata rewritten** — subtitle "Cloud & Terraform cert prep", long description
  now covers Terraform Associate 003, Terraform Professional, AWS, Azure, GCP,
  Kubernetes, and Docker; pricing/subscription language removed per directory policy.
- **Chrome brand color** changed to Terraform Academy orange `#FF6B00`.
- **Hint feature** — every quiz question offers a hidden "💡 Need a hint?" conceptual
  nudge (amber `#FFB020`), never penalized, tracked as assisted vs unassisted.
- **Full lab catalog synced** — 8 labs → 312 labs, filterable by provider and level.
- **Interactive code-block lab mode** — `get_lab_content` + `check_lab_code` grade
  learner-written HCL against per-objective server-side regex (solutions never leak).
- **Legacy labs converted** — 26 `Interactive-labs/` code labs merged into the catalog.
- **Pro Tips articles** — `list_articles` + `get_article`, read live from Supabase (auto-sync).
- **Learning games** — `list_games` + `get_game` + `check_game_answer` (matchup + sequence).
- **Foundations courses** — `list_foundations` + `get_foundation` (3 courses, 47 lessons).
- **Timed speed rounds** — `list_speed_rounds` + `start_speed_round` (62 rounds, 1,240 questions).
- **Branded dashboard** — `render_dashboard` renders an MCP Apps UI resource with
  profile (XP, octagons, completions, tier) and domain readiness bars.
- **17 MCP tools total**, plus one served UI resource.
- **Centralized MCP analytics pipeline** — every tool call is logged to a
  Supabase `integration_events` table (source `chatgpt_mcp`) with identity,
  tier, and outcome, fired fire-and-forget via `ctx.waitUntil`.

---

## 3. Architecture

```
chatgpt-plugin/terraform-academy/
├── plugin.json                  Store manifest (metadata, branding, skills, review test cases)
├── mcp.json                     MCP server declaration (streamable-http, mixed auth)
├── skills/
│   ├── getting-started/SKILL.md
│   ├── terraform-associate/SKILL.md (+ references/question-bank.md)
│   ├── terraform-troubleshooting/SKILL.md
│   ├── cloud-certifications/SKILL.md
│   └── branding/SKILL.md
├── assets/icon.png, logo.png
└── tools/export-*.mjs           Question bank exporters

max/cloudflare-worker/mcp-worker/
├── worker.js                    MCP server (raw JSON-RPC over streamable-http)
├── wrangler.toml                Cloudflare Worker config (name: terraform-academy-mcp)
└── data/
    ├── cert-tracks.js           15 certification tracks
    ├── question-bank.js         25 tracks / 2,831 questions
    ├── labs.js                  312-lab catalog
    ├── lab-content.js           309 interactive labs (starter files, objectives, hints, solutions)
    ├── legacy-labs.js           26 converted legacy labs
    ├── legacy-lab-content.js    26 legacy interactive labs
    ├── games.js                 8 games (matchup + sequence)
    ├── speed-rounds.js          62 timed rounds / 1,240 questions
    ├── foundations.js           3 courses / 24 modules / 47 lessons
    └── dashboard-ui.js          Branded dashboard HTML (MCP Apps UI resource)

scripts/
├── export-mcp-labs.py           Regenerates labs.js + lab-content.js from max/labs/*.html
├── export-legacy-labs.py        Regenerates legacy-labs.js from Interactive-labs/
├── export-mcp-games.mjs         Regenerates games.js from Interactive-labs/Games/
├── export-mcp-speedrounds.mjs   Regenerates speed-rounds.js from Interactive-labs/V2/speed-rounds/
└── export-mcp-foundations.py    Regenerates foundations.js from max/*foundations*.html
```

- The MCP server is a **Cloudflare Worker** implementing MCP `streamable-http`
  directly (no SDK). It handles `initialize`, `ping`, `tools/list`, `tools/call`,
  `resources/list`, and `resources/read`.
- The dashboard is served as an MCP Apps UI resource with
  `mimeType: text/html;profile=mcp-app`, using the `ui/*` JSON-RPC bridge over
  `postMessage`.
- **Analytics pipeline:** the `tools/call` dispatcher resolves identity once
  (Supabase user + tier via `max-api`), builds an anonymized event
  (`source: chatgpt_mcp`, tool, tier, track/domain/provider/slug, `is_correct`
  for grading tools, OpenAI `openai/subject`/`openai/session`/`openai/organization`
  hashed with SHA-256), and persists it to Supabase `integration_events` with the
  service key via `ctx.waitUntil`. Analytics writes are non-blocking and disabled
  when `SUPABASE_SERVICE_KEY` is unset.

---

## 4. MCP tools (18)

All tools are read-only. Tier gating is enforced server-side using the request's
Authorization token (see §7).

| # | Tool | Purpose | Key inputs | Gating / data source |
|---|------|---------|-----------|----------------------|
| 1 | `list_certification_tracks` | List cert tracks | `provider?` | Free. `cert-tracks.js` (15 tracks) |
| 2 | `list_labs` | List labs | `provider?`, `level?` | Free list; premium labs flagged `locked`. `labs.js` + `legacy-labs.js` (338) |
| 3 | `get_lab` | Lab metadata + description | `slug` | Premium labs locked for free users. Fetches live page meta |
| 4 | `get_lab_content` | Start interactive lab | `slug` | Premium locked. `lab-content.js` / `legacy-lab-content.js` (335) |
| 5 | `check_lab_code` | Grade learner HCL vs objective | `slug`, `objectiveId`, `code` | Premium locked. Server-side regex grading; solution never revealed |
| 6 | `get_quiz_questions` | Serve quiz questions | `track?`, `domain?`, `count?` | Free: 3-question sample cap; subscribers: full bank up to 20. `question-bank.js` |
| 7 | `render_quiz` | Render interactive quiz widget | `track?`, `domain?`, `count?` | Free. Returns `ui://widget/quiz.html` with questions, hints, and server-side grading |
| 8 | `check_answer` | Grade quiz or speed-round answer | `questionId`, `answer` | Free. Grades both question-bank and `speed:` IDs; widget-accessible |
| 9 | `list_articles` | List Pro Tips articles | `category?` | Free list (excerpts). Live Supabase read → auto-sync |
| 10 | `get_article` | Full article | `slug` | Gated articles return title+excerpt for free users |
| 11 | `list_games` | List learning games | — | Free. `games.js` (8) |
| 12 | `get_game` | Start a game | `slug` | Free. Answers withheld server-side |
| 13 | `check_game_answer` | Grade a game answer | `slug`, `term?`, `definition?`, `order?` | Free. Correct answer revealed only after grading |
| 14 | `list_foundations` | List Foundations courses | — | Free. `foundations.js` (3) |
| 15 | `get_foundation` | Course module/lesson outline | `slug` | Free. Includes lesson excerpts |
| 16 | `list_speed_rounds` | List timed rounds | `provider?` | Free. `speed-rounds.js` (62) |
| 17 | `start_speed_round` | Start a timed round | `slug`, `count?` | Free. Questions without answers; grade via `check_answer` |
| 18 | `render_dashboard` | Render branded dashboard | `domains?`, `readiness?` | Fetches profile server-side when signed in. Serves UI resource |

### UI resources

| URI | MIME type | Purpose |
|-----|-----------|---------|
| `ui://widget/dashboard.html` | `text/html;profile=mcp-app` | Branded learning dashboard (profile + readiness) |
| `ui://widget/quiz.html` | `text/html;profile=mcp-app` | Interactive quiz (clickable answers, light bulb hint, grading, results) |

---

## 5. Content inventory (exact counts)

### Certification
- **15 certification tracks** exposed by `list_certification_tracks`:
  HashiCorp (Terraform Associate 003, Terraform Professional, Vault Associate 003,
  Consul Associate 003), AWS (Solutions Architect Associate, Developer Associate),
  Azure (Fundamentals, Administrator, Developer Associate, Security Engineer Associate),
  CNCF (CKA, CKAD), GCP (Terraform on Google Cloud).
- **Question bank: 2,831 questions across 25 tracks** (a superset of the 15 tracks,
  adding OpenTofu, Docker, more AWS/Azure/GCP, and GCP Service Quizzes).
  - Terraform Associate (003): 9 domains / 90 questions.
  - Free users get a 3-question sample per call; subscribers get up to 20.

### Labs
- **338 labs total** (312 modern + 26 converted legacy), filterable by provider and level.

| Provider | Count |
|----------|-------|
| AWS | 95 |
| GCP | 72 |
| Azure | 66 |
| Kubernetes | 59 |
| Security | 33 |
| HashiCorp | 7 |
| Multi-Cloud | 5 |
| OpenTofu | 1 |

- **335 labs** have interactive code-block content: starter HCL files, build
  objectives (each with a grading regex), hints, and a solution (solution held
  server-side, never sent to the client).

### Articles
- **48 live Pro Tips articles**, read from Supabase on every call (new posts sync
  automatically). 4 categories: SRE Pro Tips, Pipeline Perspective, From the Source,
  HashiCorp Solutions. Gated articles require Pro/MAX for the full body.

### Games
- **8 games**: 4 term-definition matchup (90 pairs) + 4 build-sequence (40 steps).

| Game | Type | Size |
|------|------|------|
| AWS CLF-C02 Matchup | match | 20 pairs |
| Azure DevOps Matchup | match | 20 pairs |
| GitOps Matchup | match | 25 pairs |
| Google Cloud Matchup | match | 25 pairs |
| Terraform: AWS S3 Build Sequence | sequence | 10 steps |
| Terraform: AWS IAM Build Sequence | sequence | 10 steps |
| Terraform: AWS VPC Build Sequence | sequence | 10 steps |
| AWS EC2 + GitOps Build Sequence | sequence | 10 steps |

### Foundations courses
- **3 courses / 24 modules / 47 lessons.**

| Course | Provider | Modules | Lessons |
|--------|----------|---------|---------|
| Terraform Foundations (HCL) | HashiCorp | 10 | 14 |
| OpenTofu Foundations | OpenTofu | 6 | 18 |
| Terraform Cloud Foundations | HashiCorp | 8 | 15 |

Each lesson carries a text excerpt of the real course body so ChatGPT can teach
actual content; full interactive lessons live on the site.

### Speed rounds
- **62 rounds / 1,240 questions** (45-second timer each).

| Provider | Rounds | Questions |
|----------|--------|-----------|
| AWS | 20 | 400 |
| Azure | 21 | 420 |
| GCP | 21 | 420 |

---

## 6. Skills (5)

| Skill | Trigger | Behavior |
|-------|---------|----------|
| `getting-started` | First install / "how do I start" | Determines level + goal, recommends a mode (cert practice, fundamentals, troubleshooting, articles, games, speed rounds, dashboard) |
| `terraform-associate` | Terraform Associate 003 study requests | One-question-at-a-time quiz across 9 domains, 💡 hints, running score, per-domain readiness report |
| `terraform-troubleshooting` | Failing plans / HCL errors / lab requests | Root-cause debugging workflow + interactive code-block labs (`get_lab_content` + `check_lab_code`) |
| `cloud-certifications` | AWS/Azure/GCP/K8s/Docker study + articles/games/rounds/dashboard | Combines MCP content with web search for current exam objectives |
| `branding` | Any content generation | Authoritative colors, typography, and voice rules |

### Hint behavior (v1.0.1)
- Hidden by default behind "💡 Need a hint?".
- Conceptual nudge based on domain/learning objective; never reveals the answer or
  eliminates choices; never restates the stored explanation.
- Never changes the score. Tracked as assisted vs unassisted in the readiness report.
- Hint accent: amber `#FFB020`.

---

## 7. Authentication & tier gating

- **Mode:** `mixed` — free tier without an account; subscriber unlock via OAuth 2.1.
- **Sign-in URL:** `https://mcp.terraformacademy.app/oauth/authorize`
- **Token URL:** `https://mcp.terraformacademy.app/oauth/token`
- **Discovery:** `https://mcp.terraformacademy.app/.well-known/oauth-authorization-server`
- The worker runs a small OAuth bridge over the existing Supabase auth (PKCE, HMAC
  authorization codes). No third-party IdP.
- **Tier resolution:** Supabase user JWT → `max-api.terraformacademy.app/verify-subscription`
  → `free` / `pro` / `max`.

| Access | Quiz | Labs | Articles |
|--------|------|------|----------|
| Not signed in | 3-question sample | Premium locked | Free full, gated title+excerpt |
| Pro/MAX | Full bank (≤20/call) | All labs unlocked | All articles full |

Games, Foundations, speed rounds, and the dashboard render for everyone; the
dashboard only shows profile stats when signed in.

---

## 8. Branding system

- **Plugin chrome** (non-quiz, non-lab): Terraform Academy orange `#FF6B00`.
- **Provider colors:** HashiCorp/Terraform purple `#7B42BC` · Azure blue `#0078D4` ·
  GCP multi-color `#4285F4/#EA4335/#FBBC05/#34A853` · AWS orange `#FF9900` ·
  Security & IAM deep red `#B91C1C` · Foundations keep their current branding.
- Quizzes keep their own branding; never re-skinned to the chrome color.
- Dark panels use `#0B1020`. Light surfaces use ChatGPT system backgrounds/text with
  brand colors reserved for accents, badges, and primary buttons.
- Voice: friendly, direct, no em dashes, no decorative emoji (💡 is the one functional glyph).

---

## 9. Data & analytics model (Supabase)

The worker reads live data through Supabase (public anon key + RLS; the user's JWT
is mapped server-side):

| Table | Purpose | Dashboard field |
|-------|---------|-----------------|
| `protips_articles` | Pro Tips blog content | — |
| `pvp_profiles` | `total_xp` | Total XP |
| `user_inventory` | `octagons` | Octagons |
| `user_completions` | `xp_earned`, `octagons_earned`, completions | Completions |
| `max_subscriptions` | subscription tier | Tier |
| `integration_events` | MCP tool-call events (`source: chatgpt_mcp`) | — |

Quiz sessions and hint-usage analytics are currently conversation-scoped (computed by
the skill). The underlying `user_completions` table already records XP/octagons per
completion, which the dashboard aggregates.

---

## 10. Known limitations & roadmap

**Live now:** all 17 tools + dashboard resource are deployed to the worker.

**Pending store review:** v1.0.1 manifest (expanded description, orange branding,
`branding` skill, `mixed` auth registration).

**Not yet built:**
- PvP/multiplayer games (`VS-Battle`) — requires realtime infrastructure.
- Remaining legacy quizzes (`Provider Tests/`, `Quuizzes/`, speed-round extras beyond
  the 62 extracted rounds).
- Server-side hint-event persistence (currently tracked per conversation, not per
  question attempt in Supabase).
- Assistance Profile analytics (independent vs assisted mastery) — data model exists,
  dashboard surface not yet built.
- Admin portal reporting UI for `integration_events` (the table, worker pipeline, and
  reporting queries are ready; the visual admin view is not yet built).

**Data-quality note:** the legacy lab extractor converts `Interactive-labs/` code labs
only (26 of ~200+). CI/CD, Docker, game, and speed-round files are handled by their
own extractors or intentionally excluded.
