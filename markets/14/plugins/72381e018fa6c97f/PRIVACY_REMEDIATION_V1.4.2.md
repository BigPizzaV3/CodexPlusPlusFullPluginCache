# Privacy review remediation — v1.4.2

The 6 November 2026 review requested complete disclosure of data collected,
purposes, recipients, retention and user controls. The public policy remains
https://layoverpilot.com/privacy and now covers the website and all five MCP tools.

## Verified source inventory

- `shared/plugin-contract.ts`: connection inputs (including optional preferences,
  country code, labels, food query and journey estimates), airport/programme
  requests and connection comparison. `server/mcp.ts` returns structured planning
  results and equivalent text to ChatGPT, using the synchronous planning engine.
- `server/app.ts`: calculation endpoints do not save plans; separate optional
  counter, product-event and explicit-feedback endpoints can write to PostgreSQL.
- `server/privacyRetention.ts` and `server/index.ts`: the owner approved a 90-day
  product-event / 12-calendar-month feedback retention schedule on 6 November.
  Startup and hourly sweeps enforce it when the database is available, with retry
  on failure. This touches only the two named tables, never historical account,
  billing, plan or counter-total tables. The policy explains retry/availability
  limits instead of promising deletion at the exact expiry minute. PostgreSQL
  integration tests use session-local temporary tables to prove the boundaries.
- `server/planViewStore.ts`: counter hashes over 30 days are removed on a later
  counter update; aggregate totals remain. Session storage is logically 24 hours.
- `client/src/lib/connectionIntelligence.ts`: consent-based product events can
  contain page URLs, including a shared-plan fragment, and a random browser ID.
  Policy discloses this instead of claiming no planning context can be retained.
- `client/src/lib/feedbackContext.ts`: optional feedback context and visitor ID.
- `server/services/travelContext.ts`: MET Norway receives public coordinates;
  Frankfurter receives a currency pair. Travel date is filtered locally on server.
- Current `App.tsx` does not mount the legacy Google analytics loader. This change
  does not enable analytics. A privacy-page opt-out clears the legacy consent and
  visitor identifier for future product events, separately from counter choice.
- External directions/food links can carry a selected destination/search query.
  Remote images involve normal third-party browser requests. Hosted guide videos
  do not automatically load external creator embeds.

The policy distinguishes infrastructure/provider retention and OpenAI-held
conversation data from application memory. It explains access/deletion requests,
limitations for anonymous calculations, browser storage, shared links and legacy
records. The production build prerenders the same policy component into HTML so
the complete notice is readable without JavaScript, including by review crawlers.
No actual analytics figures, Google account/property IDs, dashboard URLs,
credentials, private reports or support inbox content are included in this record.

## Submission scope

Portable package version 1.4.2 preserves the endpoint, publisher/listing URLs,
real demo, and exactly five positive plus three negative cases. Update the existing
Layover Pilot plugin, not a second plugin identity. Validate the saved connection
and current scans; do not infer readiness from this source document. Owner legal
attestations remain an owner action where required by the portal.
