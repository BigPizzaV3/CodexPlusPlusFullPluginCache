# Traviz plugin

Discuss a trip in English or Chinese, validate formatted notes, and open them in Traviz.

## Hosted tools

The public package uses `https://traviz-plugin.ahi-lab.com/mcp` with no account or API key required. `get_planning_prompt` returns the app's planning and formatting prompt. `prepare_trip` validates a confirmed itinerary and returns a share link. The Cloudflare service processes notes transiently and does not store trips or call an AI provider. The host conversation supplies the AI.

The link contains readable itinerary data. Anyone with the complete link can read it. Do not include passport, payment, or private booking identifiers.

## App compatibility

Traviz 1.1 opens the import preview: tap Import, then Visualize trip. Compatible newer builds support automatic visualization after import. Draft protection, matching, and saved-trip limits remain applicable. A desktop plugin cannot silently open an app on another device; users may need to tap the link on their phone.

## Development

The optional Node helper remains available in this repository for local testing. The public ZIP excludes it and uses the hosted tools instead. Bundled parser, codec, and prompts mirror the app sources.

Run `node --test plugins/traviz/tests/*.test.cjs plugin-service/test/*.test.mjs` from the repository root. Deploy the Worker using `plugin-service/wrangler.jsonc`. Public policy pages are served by the same Worker at `/support`, `/privacy`, and `/terms`.

The portable root manifest contains portal metadata, including supportURL. The legacy compatibility manifest omits that field because the bundled local validator does not support it yet.
