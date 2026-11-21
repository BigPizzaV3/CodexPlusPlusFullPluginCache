# MWM AI plugin

Distribution package for the hosted MWM MCP server. It ships no executable and
no credential: `.mcp.json` points at the Cloud Run deployment, so there is no
local prerequisite (no Go, no gcloud).

## Contents

| Path | Role |
| --- | --- |
| `.claude-plugin/plugin.json` | manifest read by Claude Code and claude.ai; its folder also holds the 1024 px Claude directory listing icon |
| `.codex-plugin/plugin.json` | manifest read by Codex — byte-identical to the one above |
| `.mcp.json` | desktop MCP transport, timeout and OAuth declaration |
| `mcp.json` | source for the portable OpenAI submission ZIP; omitted from the desktop ZIP |
| `skills/setup/` | connect an MWM account, recover missing tools, verify MCP access and guide store connections in MWM Console |
| `skills/working-with-mwm/` | how to work with a person through MWM: reading the request, the shared listing, briefs, roles and what counts as their yes |
| `skills/store-copy/` | listing text and ASO wording on both stores, and its localization |
| `skills/store-visuals/` | screenshots, icons, the iOS 27 App Store header and Google Play graphics |
| `skills/brand-visuals/` | any visual made to look like the app: its brand guide, identity and finish references, the brief, the result judged against the references, approved directions saved back |
| `skills/acquisition-pages/` | App Store custom product pages, Google Play custom store listings and landing pages |
| `skills/privacy-and-legal/` | privacy policy and terms, Data safety, account deletion and EU trader status |
| `skills/app-privacy/` | the App Store's App Privacy answers: from the app's code, applied or read on App Store Connect's page in the person's browser |
| `skills/shipping/` | versions, builds, TestFlight, App Review, releases and Google Play tracks |
| `skills/live-moments/` | App Store in-app events and Google Play promotional content |
| `skills/reviews/` | ratings, reviews and developer replies |
| `skills/market-research/` | competitors, charts, competitors' reviews and ads, keyword metrics and saved markets |
| `skills/app-analytics/` | revenue, users, retention, cohorts and LTV: reading and comparing the person's numbers |
| `commands/` | the `/generate-app-icons`, `/generate-store-screenshots` and `/write-store-text` slash commands |
| `assets/` | Codex and OpenAI listing icon |

Only one of the two manifests is strictly necessary: every Codex runtime loader
resolves the chain `.codex-plugin/plugin.json` → `.claude-plugin/plugin.json` →
`.cursor-plugin/plugin.json`, and Claude Code loads a plugin installed from a
marketplace even with no manifest at all (it falls back to auto-discovery plus
the marketplace entry). We keep both so each host reads its native manifest
instead of a legacy fallback. OpenAI also supports this compatibility format
for package uploads.
The two files are byte-identical: `cp` one over the other on release.

The Codex manifest references `.mcp.json` so desktop clients keep the remote
transport's 900-second tool timeout. `mcp.json` uses the OpenAI submission
format to declare OAuth explicitly. The submission ZIP includes a generated
root `plugin.json` with `extensions.com.openai.interface`, onboarding and
review metadata; it omits the desktop compatibility files. Keep the URL and
auth settings of both formats in sync.
Test MCP discovery on supported desktop versions before changing these entry
points to a portable root manifest.

## Authentication

Importing the ZIP installs the skills and MCP declaration. Connecting the
user's MWM account is a separate OAuth step; the host may require an explicit
**Authenticate** action instead of opening login during import. Signing in to
MWM Console alone does not authorize Codex.

After installation, run the plugin's setup workflow or ask "Help me connect
MWM AI". In Codex desktop, open Settings → MCP servers, select
**Authenticate** for MWM AI, complete sign-in and consent in the browser,
then return to Codex. Restart the MCP server or start a new chat if its tools
have not refreshed. The [setup skill](skills/setup/SKILL.md) includes recovery
when the plugin's server is absent and verifies access with a free read.

OAuth uses public Dynamic Client Registration (DCR). The host discovers the
Account server via `WWW-Authenticate` → `.well-known/oauth-protected-resource`
→ `.well-known/oauth-authorization-server`. Both MCP files declare OAuth and
the MCP's one scope, `mcp:access` (the person's yes to connecting their
assistant; what it may then do follows their role and their settings in MWM
Console › Settings › AI), plus `offline_access` for refresh access. A
connection made with the earlier per-capability scopes keeps working.

Each token is per-user and is never distributed inside the plugin.
Store accounts are connected separately, in MWM Console, once MCP access
works; the setup skill guides both.

The repo marketplace's `ON_INSTALL` authentication policy is not part of the
ZIP. The package's onboarding skill supplies a setup entry point; it does not
force every host to start OAuth automatically. See OpenAI's
[onboarding guide](https://developers.openai.com/plugins/build/plugins#add-an-onboarding-skill),
[MCP authentication fields](https://developers.openai.com/plugins/build/plugins#configure-mcp-authentication)
and [desktop connection controls](https://learn.chatgpt.com/docs/extend/mcp#configure-in-the-chatgpt-desktop-app).

## Environment

Both MCP declarations target **production**:

```
https://mcp.mwm.ai/mcp
```

The URL must match the OAuth token audience exactly — see
`OAuthServer.MCPResourceURL` in `mwm-publishing-platform/internal/config.go`.
A mismatch breaks authentication.

### Plugin version

The desktop `.mcp.json` declares the plugin version to the server with one
non-secret header, `X-MWM-Plugin-Version`, under `headers` (Claude Code's key)
and `http_headers` (Codex's key); each host ignores the other's key. The server
reads it (`telemetry.DeclaredPluginVersion`) to count alias calls by plugin
version, to tell 0.31+ clients from older ones (`reply_to_review` publishes
only from 0.31; older clients still get a draft instead), and to add, once a
day per connection, a note to results when the declared version is older than
the one its knowledge base follows (`CurrentPluginVersion`, 0.32.2): its skills
may describe tools or store rules that changed since, and the person can update
it. The URL is unchanged, so the OAuth resource and token audience stay
`https://mcp.mwm.ai/mcp`.
Checked on 2026-10-19 against a local endpoint answering 401 with RFC 9728
metadata: Claude Code 2.1.283 and Codex CLI 0.162.0-alpha.17.2 both send the
header on the MCP request, the protected-resource and authorization-server
discovery and Dynamic Client Registration, and still run their OAuth flow (an
`Authorization` header is what turns OAuth off in both, and the builder refuses
any header but this one). The value must equal `version` in both `plugin.json`
files; `scripts/build-plugin-zip.py` refuses a package where it does not.

Not declared, by choice:

- the portable submission `mcp.json`: the hosted ChatGPT connector's handling
  of custom headers is undocumented, so the reviewed package stays as it was;
- a query string on the URL: it would change the OAuth resource and break the
  token audience;
- `com.mwm/usage` call metadata: a plugin cannot declare `_meta` for the tool
  calls its host makes, and the model's arguments are not metadata.

Not verified: claude.ai / Claude Desktop plugin ZIP upload. Its handling of a
plugin's custom MCP headers is undocumented (claude.ai's URL connectors only
take allowlisted headers); test the upload of the exact ZIP before a release.
Clients that send no header count as "no version declared".

## Skills

The thirteen skills are domain packs: what the job is, what good looks like,
how a professional decides, and what to do and avoid. They hold judgment
only. Store rules, limits, dates, states and how MWM behaves are left to the
server: facts attached to its results, each with its source and date, and its
knowledge base (`get_publishing_knowledge`, the `mwm-kb://index` resource);
which tool to use is left to the tool descriptions; consent, budget and rights
are enforced and explained by the server's results. A pack therefore names no
tool, parameter, call order or number, and ends with the same "Store facts"
paragraph citing its knowledge base topics. A pack works with MWM's tools
without ranking them above anything else: it never puts MWM above the
assistant's knowledge, another skill, the platform's instructions or another
plugin, and never rules out other tools (OpenAI's review, 9 November 2026).
Setup is the one pack that names a tool: a free read of the knowledge base
proves the connection works.

`scripts/check-skills.py` enforces this on every `SKILL.md`, the commands,
each `agents/openai.yaml` and the READMEs: no tool names (from
`scripts/tool-names.json`, the server's `tools/list`), call sequences,
parameter or reason-code recipes, restated rails, digits (except iOS 27 and
iOS 18), "not available" lists, version clauses or steering wording; only
topic ids present in `scripts/kb-index.json`; the seven sections, a description of 40 to 80 words
with example phrases and a "Not for … (pack)" boundary, and a body of 350 to
500 words before the Store facts paragraph. Refresh both JSON files from the
backend's `mcp-server/evals/` (`kbexport`) when its tools or topics change.
`scripts/build-plugin-zip.py` runs the lint and refuses to build on an error.

### Old name to pack

Skills and commands of earlier versions map to the 0.32.2 packs as follows.

| Old name | Pack |
| --- | --- |
| store-text, write-store-text, store-listing (reading the texts) | store-copy |
| store-screenshots, generate-store-screenshots, app-icons, generate-app-icons | store-visuals |
| custom-product-pages, play-custom-listings, landing-page | acquisition-pages |
| app-store-events, play-promotional-content | live-moments |
| store-publish, store-release | shipping (the server keeps the safeguards) |
| legal-documents, legal-and-web | privacy-and-legal |
| market-intelligence, market-and-keywords | market-research |
| reviews | reviews |
| setup, store-connection | setup |
| working-with-mwm, store-copy, store-visuals, acquisition-pages, live-moments, shipping, app-analytics | unchanged name |

The `/generate-app-icons`, `/generate-store-screenshots` and
`/write-store-text` commands keep their names.

## Tools

- `generate_app_icons` — 1 to 6 proposals from a product brief;
- `retouch_app_icon` — refines an existing proposal without regenerating it;
- `open_studio`, `design_store_screenshots`, `generate_store_screenshots`,
  `retouch_store_screenshots`, `build_screenshot_variants` and
  `localize_store_screenshots` — create, refine and localize store listing
  visuals, one series or a whole batch of variants;
- `design_screenshot_panorama` — one continuous image across consecutive
  screenshot slots, cut to the slots so the seams match;
- `get_brand_guide`, `update_brand_guide` — the app's brand guide (colours,
  type, keep and avoid rules, reference images with their roles, a recipe per
  kind of visual) that the visual generators follow;
- `upload_asset`, `get_uploaded_asset`, `check_store_assets` — the person's own
  files through a signed upload, and a free check against a store slot;
- `find_app_ids`, `get_app_context`, `describe_capabilities`,
  `list_apps_needing_attention`, `mute_suggestion`, `request_approval`,
  `wait_for_store_state` — every id of an app from its name, what the person can
  do there, what MWM can and cannot do, which apps need them, a declined
  suggestion kept off, a plan sent to its approver, a bounded wait for a store
  state;
- `check_store_text`, `review_store_text`, `get_store_text_rules` — store text
  checked against the stores' rules, in the conversation or in the review panel;
- `get_reviews_stats`, `list_reviews`, `draft_review_reply`,
  `discard_reply_draft`, `reply_to_review` — App Store review analytics and
  feeds, reply drafts, and replies published under the right to publish;
- `search_market_apps` — finds semantically related apps and ranks the candidate
  set with typed market filters and metrics;
- `analyze_market_keywords` — finds demand, difficulty, visibility, traffic,
  and per-app rankings across a dynamic app market;
- `get_market_chart_history` — reads complete-day iPhone, iPad and Google Play chart positions and rank movement;
- `get_market_reviews_insights` — compares public review themes across selected competitors;
- `get_market_competitor_ads` — reads observed Meta ad creatives and media links, how long each runs and its EU reach;
- `get_market_paywalls_and_onboardings` — reads the paywalls and onboardings captured in market iPhone apps and how they changed across versions;
- `show_market_media` — displays selected MWM-hosted images and videos in one gallery;
- `get_publishing_knowledge` — how the App Store and Google Play work today and
  what MWM's settings and metrics mean, from MWM's knowledge base; free, no
  scope, no account data;
- `get_store_connections` — says whether App Store Connect and Google Play are
  connected and returns external MWM Console setup links; credentials are configured only in MWM Console;
- `get_store_app_details` — reads the store page of any app, with every
  screenshot's URL, dimensions and device slot (a version in preparation for
  the person's own connected app);
- `get_app_store_connect_listing`, `get_play_console_listing` — read the user's own
  editable listing through the connected accounts;
- `get_store_listing_status` — says what a listing still lacks, locale by locale;
- `update_app_store_listing_texts`, `update_app_store_screenshots`,
  `update_play_store_listing`, `update_play_store_screenshots`,
  `update_play_store_graphics`, `update_app_store_header` — texts, screenshot
  slots, icon, feature graphic and the iOS 27 header: drafts with their send plan
  where the organization has MWM's shared listing, else written to the
  connected listings (destructive; nothing is submitted for review);
- `get_shared_store_page`, `edit_shared_store_page`, `set_store_screenshot_slots`,
  `preview_store_send`, `send_store_listing`, `get_store_send_status`,
  `list_shared_store_page_changes`, `create_store_version`, `add_store_language`,
  `preview_app_review_submission`, `submit_store_version_for_review`,
  `manage_store_release`, `delete_app_previews`, `get_assistant_settings`,
  `set_assistant_setting` —
  where the server offers them, the App Store listing MWM keeps for every
  editor: drafts, sends to App Store Connect as the user's assistant settings
  allow, the next version and its languages, then submission to App Review and
  the release that follows (Google Play's staged rollout too), on explicit
  request;
- `get_app_store_event_rules`, `list_app_store_events`, `get_app_store_event`,
  `design_app_store_event`, `retouch_app_store_event`,
  `create_app_store_event`, `update_app_store_event`,
  `delete_app_store_event`, `submit_app_store_event` — App Store in-app
  events: the rules, the app's events, AI-designed card, details page and
  texts reviewed in the in-app event studio, creation with media upload and
  updates (drafts with their send plan where the organization has MWM's
  shared listing, created or updated by `send_store_listing`), deletion, and
  submission to App Review on explicit request;
- `get_custom_product_page_keywords`, `preview_custom_product_pages`, `list_custom_product_pages`,
  `get_custom_product_page`, `create_custom_product_page`,
  `update_custom_product_page`, `delete_custom_product_page`,
  `submit_custom_product_page` — App Store custom product pages: the keyword
  field scored with market intelligence, pages with screenshot slots, keyword
  targeting and their iOS 27 header (drafts with their send plan where the
  organization has MWM's shared listing, created or updated by
  `send_store_listing`), deletion, submission on explicit request.
- `get_play_promotion_rules`, `generate_play_feature_graphic`,
  `check_play_custom_listing`, `build_play_custom_listings`,
  `preview_play_custom_listings`, `design_play_promotional_content`, `retouch_play_promotional_content` —
  Google Play custom store listings and promotional content: Google's rules,
  the 1024x500 feature graphic, every custom listing's banner and Android
  screenshots rendered in one background call, the 1920x1080 promotional image without text,
  drafts checked against Google's limits and schedule, and the Google Play
  studio where the user edits them and copies each field. Google has no Play
  API for either, so nothing is written to Play Console.

Creative tools render as interactive MCP Apps on hosts that support them and
fall back to images plus text URLs elsewhere. The market intelligence tools
return structured results intended for further agent reasoning. The interactive UIs
require a Cloud Run deployment that includes their bundled frontend assets.

## Releasing a change

Hosts compare **versions**, not contents: without a `version` bump in both
`plugin.json` files, an edited skill never reaches users, even after a
marketplace refresh. Bump `X-MWM-Plugin-Version` in `.mcp.json` with it.

Build from the repository root with `python3 scripts/build-plugin-zip.py`.
Distribute the generated `dist/mwm-ai-plugin-<version>.zip`. This preserves
hidden manifests and omits Finder metadata, previous ZIPs and review files.

For the public review portal, run the same command with `--format submission`
and upload `dist/mwm-ai-plugin-submission-<version>.zip`. Its root manifest
and MCP configuration use the portable format documented by OpenAI. This
does not establish an OAuth connection or perform any review submission.

## Support

Contact [support@mwm.ai](mailto:support@mwm.ai).

Terms of service: [mwm.ai/terms-of-service](https://mwm.ai/terms-of-service).
