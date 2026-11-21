# Submission package

Everything the ChatGPT plugin directory needs for Langua, in the Agent Plugins
format. Prepared for LAN-1322 on 2026-10-22. **Not submitted. Not published.**

```
submission/
  plugin.json             listing, review cases, publication settings
  mcp.json                one server, no auth, https://chatgpt.languatalk.com/mcp
  assets/                 logo.png, logo-dark.png, icon.png, icon-dark.png (512x512)
  test-cases.md           the 5 positive and 3 negative cases, readable
  video-script.md         2-minute walkthrough shot list
  privacy-addendum.md     the policy section that still has to be published
```

The package has no `skills/` directory: Langua is an MCP-only plugin.
There are no `apps` references and no lifecycle hooks, both of which block
submission.

## Building the ZIP

Validate first, and only build the ZIP if it passes. The ZIP's root must be the
manifest, not the folder:

```bash
python3 scripts/validate-submission.py \
  && (cd submission && zip -r ../langua-plugin-1.0.0.zip . -x '.*')
unzip -l langua-plugin-1.0.0.zip   # plugin.json must be at the root
```

`validate-submission.py` is a manual gate: nothing in `npm run build` or
`npm test` calls it, so run it yourself before every upload. To check the
validator itself still catches a broken manifest:

```bash
python3 scripts/check-validator.py
```

It mutates `submission/plugin.json` seven ways, confirms each one is rejected,
and restores the file.

## Verified

| Check | Result |
| --- | --- |
| Manifest fields against the documented limits | 45/45 pass (`scripts/validate-submission.py`) |
| The validator rejects a broken manifest | 7/7 mutations rejected (`scripts/check-validator.py`) |
| 5 positive cases, each asserted and carried through to a claim link | all `ok` (`scripts/verify-submission-cases.ts`, mock backend) |
| Tool annotations on the live staging server | match the table below |
| Widget CSP vs what the widgets fetch | exact match: the two Google Fonts domains, nothing else |
| `privacyPolicyURL`, `termsOfServiceURL`, `supportURL`, `websiteURL` | all 200 |
| Unit and integration tests | 253 pass |
| `wrangler deploy --env production --dry-run` | builds, deploys nothing |

Two adversarial reviews ran over this work. Their findings are fixed, except
where this file records a decision not to act and says why.

## Decisions a reviewer may ask about

### Tool annotations

| Tool | readOnly | destructive | openWorld | Why |
| --- | --- | --- | --- | --- |
| `build_phrase_deck` | true | false | false | Formats the phrases the learner gave into a card. Stores nothing and calls no API. |
| `start_beginner_lesson` | true | false | false | Reads the Langua lesson catalog to pick a lesson. Writes nothing. |
| `plan_speaking_practice` | true | false | false | Reads the Langua roleplay catalog to match a scenario. Writes nothing. |
| `create_langua_link` | false | false | false | Writes: it stores a pending activation. Not destructive: purely additive, deletes and overwrites nothing, and the record expires on its own after 7 days. Not open world: it reaches only Langua's own API. |

`openWorldHint: false` on all four follows the guideline that "a tool confined
to a bounded private account, workspace, or catalog may use false, even when
externally hosted". Langua's catalog and the learner's own Langua account are
that bounded domain.

### `create_langua_link` is visible to the scan but not to the model

It carries `openai/visibility: private` and `openai/widgetAccessible: true`.
Only a card's button calls it, never the model. It still appears in
`tools/list`, so the scan sees it and its annotations have to be right. They
are.

### No authentication on the MCP server

`mcp.json` declares no auth, which is deliberate. The three model-facing tools
are read-only and personalise nothing, so a reviewer gets a working card from a
cold start with no sign-in. Authentication happens later, on languatalk.com,
when the user opens the claim link: claiming requires a signed-in Langua
account.

The write path is bounded by four controls, none of them in ChatGPT:

1. Rails rejects any request to `POST /internal/chatgpt/activations` without the plugin service token. The Worker holds it; nothing else can reach the endpoint.
2. An activation is inert. It belongs to nobody and changes no account until someone opens its link while signed in.
3. The claim page shows a preview first. Adding the content takes a separate authenticated POST, so the user sees what they are accepting.
4. Links are single use, expire after 7 days, and the claim path is rate limited.

Residual risk, and its mitigation, is recorded under "Known gaps" below.

### Commerce

`commerce: false`. The plugin sells nothing and starts no checkout. The listing
copy names no plan, price, trial or upgrade, which
`scripts/validate-submission.py` checks. A learner with no Langua plan still
gets every card; the button opens Langua, which handles entitlement itself.

### `activation_request` in the model-facing output

Each card's `structuredContent` carries an `activation_request`, which the
card's button passes back to `create_langua_link`. It holds the language
settings and the activity payload: for a lesson, a Langua catalog lesson id;
for a scenario, the catalog roleplay key and group, or the learner's own
scenario text; for a deck, the items the learner gave.

This is deliberate. The fields are public catalog identifiers plus content the
learner supplied in the same turn. None of it is a session id, a trace id, a
request id, an internal account id, or telemetry, which is what the response
minimization rule targets. Moving it to widget-only `_meta` would be tidier and
is worth doing later; it is not a blocker and was not worth the regression risk
before submission.

## Known gaps

Each one blocks submission unless stated otherwise.

1. **Rails is not deployed.** `lytham-labs/languatalk` PR #2139 is open, so
   `/internal/chatgpt/catalog` and `/internal/chatgpt/activations` do not exist
   yet. Against staging today, `build_phrase_deck` works and the other two
   tools return "Langua could not set this up right now". The five positive
   cases pass in full against the mock contract. Re-run
   `scripts/verify-submission-cases.ts` against production once #2139 ships.

2. **Privacy policy.** The published policy says nothing about ChatGPT or this
   data path. `privacy-addendum.md` is the drafted section. It must be
   published before submitting.

3. **No reviewer test account yet.** The review team needs a Langua account
   that reaches the activities without MFA, an email code, a magic link, or a
   private network. The three model-facing tools need no account, but the
   card buttons do. Create a dedicated account with sample data, confirm it
   signs in from outside the company network, and enter it in the portal's
   **Review details**, never in this package.

4. **No video yet.** `video-script.md` is the shot list. Record it, host it
   where the review team can open it without signing in, and put the URL in
   `plugin.json` at `extensions.com.openai.review.demo_recording_url`.

5. **Developer verification.** Publishing as "LanguaTalk, Inc." needs business
   verification completed in the OpenAI platform dashboard first, on the
   organization and project that will own the plugin. The project cannot have
   EU data residency. Unverified.

6. **Countries: all.** Don chose all countries on 2026-10-22.
   `publication.countries` is `[]`, which the docs define as "removes country
   restrictions". Omitting the key would keep existing targeting instead.

7. **No Worker-side rate limit** on `create_langua_link`. Rails rate limits
   claiming, and an unclaimed activation expires after 7 days and is purged,
   so the exposure is pending rows rather than account changes. A KV or
   Durable Object counter on the Worker would close it properly. Not a
   submission blocker; worth a follow-up issue.

8. **`category` is unconfirmed.** Set to `Education`, which has to match a
   category title the dashboard offers. Check it at upload.

9. **No video URL in `plugin.json`.** `demo_recording_url` is absent until the
   walkthrough is recorded and hosted. The portal needs it before submission.

## Worker names

Three names, deliberately distinct, so no command can hit the wrong one:

| Name | What it is | How it is deployed |
| --- | --- | --- |
| `langua-chatgpt-plugin` | Production, on `chatgpt.languatalk.com` | `wrangler deploy --env production` |
| `langua-chatgpt-plugin-staging` | Staging | `wrangler deploy --name langua-chatgpt-plugin-staging` |
| `langua-chatgpt-plugin-dev` | Top-level name, for local `wrangler dev` | not deployed |

The top-level name used to match production, so a `wrangler deploy` that
forgot `--env production` would have overwritten the live endpoint. It is now
`-dev`, which makes that mistake harmless.
