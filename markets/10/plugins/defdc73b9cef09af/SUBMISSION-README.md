# YouCaps PT — OpenAI app/plugin submission package

Draft submission package for uploading in the OpenAI Platform (Apps SDK / app directory).
Built against the current submission flow: **upload this ZIP for automated metadata
validation, then complete the remaining steps in the developer dashboard.**

- Public MCP endpoint: https://mcp.pt.youcaps.app/mcp
- Website: https://pt.youcaps.app
- Nothing in the live MCP was changed or deployed to build this package.

## 1. Files in this package
```
plugin.json                 Manifest + listing metadata (see "still needed" for blanks)
mcp.json                    { name, url } -> points to the live MCP endpoint
assets/logo.png             512x512 PNG, square (YouCaps logo) — the required "logo"
assets/composer-icon.png    512x512 PNG (same mark) — composer icon
assets/screenshot-goblet-squat.jpg          Exercise-card visual (Goblet Squat)
assets/screenshot-bulgarian-split-squat.jpg Exercise-card visual (Bulgarian split squat)
assets/screenshot-exercises-overview.jpg    8-exercise overview visual
review/test-cases.json      5 positive + 3 negative review cases (enter in dashboard)
SUBMISSION-README.md         This file
```

## 2. Field status
Filled (confirmed):
- **developerName** — Anneke Bakelaar
- **websiteURL** — https://pt.youcaps.app
- **supportURL** — https://youcaps.app/support.html
- **privacyPolicyURL** — https://youcaps.app/privacy-policy-nl.html
- **termsOfServiceURL** — https://youcaps.app/04-Terms-of-Service.html

Still open:
- **category** — left blank on purpose. "Health & Fitness" is NOT a valid submission category.
  Allowed values (choose one): BUSINESS, COLLABORATION, DESIGN, DEVELOPER_TOOLS, EDUCATION,
  ENTERTAINMENT, FINANCE, FOOD, LIFESTYLE, NEWS, PRODUCTIVITY, SHOPPING, TRAVEL.
  (No health/fitness option exists; the closest is LIFESTYLE, but pick it yourself — not chosen here.)

Dashboard-only (cannot live in the ZIP; prepare these):
- **Identity/publisher verification** (individual or business) in Platform settings.
- **Apps Management: Write** permission on the account doing the submission.
- **Domain verification**: OpenAI gives a challenge token; it must be served at
  `https://mcp.pt.youcaps.app/.well-known/openai-apps-challenge` returning **only that exact token**.
  The endpoint already exists and currently returns 404 ("Not configured"); it will serve the token
  once `OPENAI_APPS_CHALLENGE_TOKEN` is set on the Render service (a later, separate deploy — not done here).
- **CSP domains** to declare for the exercise-card component: resource/image host `https://mcp.pt.youcaps.app`
  (already set in the component's widget CSP). No connect domains needed.
- **Reviewer credentials**: not required — the MCP is public and needs no login (auth: false).
- **Demo recording URL** — a short video walkthrough is required; please record and provide.
- **Real in-ChatGPT screenshots** — the included JPEGs are the demonstration visuals; a screenshot of the
  card rendered inside ChatGPT is recommended for the listing.

## 3. Notes / assumptions avoided
- No company, privacy, support or legal URLs were invented; blanks are listed above.
- `$schema` in plugin.json points to the documented agent-plugin schema; OpenAI's automated
  validation on upload will flag any field/schema mismatch to resolve in the dashboard.
- version mirrors the service (0.2.0).

## Tools the MCP exposes (read-only, stateless, no personal data)
search_training_knowledge, fetch_training_article, get_trainer_profile, get_coaching_options, show_exercise.
