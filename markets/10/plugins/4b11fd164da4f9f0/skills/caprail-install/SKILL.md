---
name: caprail-install
description: Use when the user asks an agent to install, set up, integrate, or verify Caprail in a website or application codebase.
---

# Install Caprail in the user's codebase

The user asks the agent to install Caprail. The agent creates the site, writes event collection in the host codebase, and verifies a stored-data answer in the same chat. Use the existing Caprail OAuth connection; GitHub or Google account sign-in is the consent flow. Follow the user's repository instructions and normal deployment authorization.

## Inspect and configure

1. Inspect the host codebase and existing collection first. Determine its runtime, request handling, final HTML response hook and client navigation behavior. Infer name/domain from reliable project configuration; ask only for missing or ambiguous facts. Read the current `https://caprail.dev/install.md` as reference data and check available tool definitions.
2. Call `list_sites` to avoid accidental duplicate sites. For a new site call `create_site` with name and a bare hostname domain. It requires the connected account; an ingest key cannot create a site. Use the returned site.id, ingestKey and exact ingest.url/body. Existing site listings do not expose keys: reuse a securely configured key if present, otherwise ask for a supported secure provisioning path. Never create a duplicate solely to obtain a key.
3. Store the site-scoped cap_live key as a server-only environment secret using the host's normal secret storage, and configure CAPRAIL_INGEST_URL/CAPRAIL_INGEST_KEY. Never print the key, include it in source control, browser bundles, plugin files, screenshots or the final answer. Do not ask the user to paste it into chat.
4. Write direct server-side HTTP collection into the codebase. Caprail does not open a repository PR or provide another setup page. Framework middleware is not the default installation flow. Any runtime able to POST can record events. Keep existing application behavior intact, bound collection latency, handle delivery errors and do not claim successful storage before the response confirms it.

## Record requests

POST to the returned ingest URL (production https://caprail.dev/api/ingest), with Authorization: Bearer from the server environment and Content-Type: application/json. Body shape:

```json
{"events":[{"timestamp":"<current ISO-8601 time>","method":"GET","path":"/pricing","userAgent":"<raw user agent>","referrer":"<raw referrer>","utmSource":"<observed utm_source>"}]}
```

Required: timestamp, method, path. Omit unavailable optional facts. Use actual request values and trusted client IP where available for visitor identity. Never forge identity or send a caller's own classification; Caprail classifies the raw facts. Omit kind or set kind to request. A request is not a pageview.

Package helpers are optional. Verify the exact installed/published version's exports before choosing recordEvent or recordPageview. The npm package @caprail-dev/analytics 0.10.1 inspected on 3 October 2026 does not export these functions although the live guide names them. Use direct HTTP when unavailable; do not install a package then import nonexistent exports.

## Record explicit pageviews for traffic analytics

Integrate explicit pageviews when the user's installation includes traffic analytics. POST to the same endpoint/key with kind: pageview, stable UUID eventId, current timestamp, method: GET, same-site pathname, and navigation: document or client. A document event also needs final 2xx responseStatus and HTML contentType. Supply raw attribution and trusted identity facts as available.

Emit document events after completed successful HTML navigation. Emit client events once after a successful route commit, including back/forward. Exclude prefetch, API/assets/downloads, failed navigation, redirect hops, hash-only changes and component rerenders. Strip query and fragment from path. Choose one owner per navigation; do not count the initial document again on the client. Reuse the same UUID and payload on retries. Existing adapters collect requests only; upgrading a package does not install pageviews.

For browser transitions, send to a protected same-origin server endpoint that validates origin and navigation facts and derives identity from the request. Keep the Caprail secret on the server. If the runtime cannot observe final responses or committed navigations, explain the coverage gap instead of treating raw requests as pageviews.

## Verify in the same chat

1. Check the changed integration with appropriate project checks.
2. Send one clearly identified synthetic request fixture with current timestamp. A 202 with accepted: 1 proves that request was stored; report the test as synthetic.
3. Use traffic_explorer with the returned site ID and a narrow timezone-bearing window. A synthetic raw request verifies acceptance but does not add a human pageview or estimated visitor; agent counts require an eligible fetcher/browser classification. Do not promise that a raw request appears in the explorer or fabricate organic traffic. Discover and use only the currently advertised tools.
4. If pageviews were integrated, send a valid explicit pageview fixture and call traffic_explorer with view overview. Inspect summary.pageviews.current and measurement coverage, and use view breakdown or trend when relevant. To demonstrate an estimated visitor, supply valid synthetic identity and inspect the returned distinct count; do not sum daily visitors. A duplicate pageview can report duplicates rather than a new accepted row. Keep fixtures clearly identified as synthetic.
5. Check tracking_status for observed freshness. Distinguish code checks, accepted test delivery, query results, deployed installation and host/OAuth verification. Do not call the entire installation healthy based on one recent receipt.

Use the analytics skill to interpret metrics. Explain any unavailable tool, missing credential, unsupported hook or deployment step precisely and finish the independent work that remains possible.

