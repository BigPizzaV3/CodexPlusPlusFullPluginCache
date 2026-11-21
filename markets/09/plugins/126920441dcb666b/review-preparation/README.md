# Dasha.fm review preparation

Prepared 1 October 2026.

**This is a partial review-preparation bundle, not a complete submission package, ready-to-submit plugin ZIP, or approval.**

## Contents

- `review-cases.partial.json`: five positive and three negative cases, with reproducible setup and observable pass conditions
- `evidence/synthetic-tests.json`: actual results from read-only tests using fictional adult birth details or nonpersonal place/sky queries
- `evidence/public-tool-schemas.json`: live public MCP tool definitions

The case fragment covers the four public tools at https://dasha.fm/mcp. For a package with exactly one MCP server, merge its `extensions.com.openai.review.test_cases` into the actual package. Multiple-server packages need cases on their respective servers instead.

## What was checked

Passed at the tool level:
- Exact natal chart, approximate-time warning and ambiguous-place lookup
- Fixed-date dasha timeline, sky-only transits and natal transit overlays
- Consistency of sky positions and dasha dates across tools
- Helpful error for an invalid 25:00 birth time
- Anonymous MCP initialization, discovery and transit calculation

All four public tools explicitly supply boolean read-only, destructive and open-world annotations.

**The five complete natural-language cases and three negative cases are Not run.** Direct tool calls do not establish correct tool selection, clarification, refusal or presentation in ChatGPT or Claude. Run them against the exact version being submitted. No independent astronomical-accuracy comparison was performed.

No account was signed into, no birth profile was read or saved, and no review submission was made.

## Remaining technical checks

1. The calculation tools automatically geocode place names but declare `openWorldHint:false`. Check the implementation: if they themselves query an external public geocoder, update that annotation. The public schema alone cannot establish whether lookup is local or external.
2. Public tools omit explicit `securitySchemes`; declaring `noauth` would make the anonymous policy clearer. Anonymous execution already works.
3. Tighten input constraints and test missing places, incomplete coordinates, invalid dates/timezones and partial birth details. The tested invalid clock time was rejected correctly.
4. Consider adding output schemas for the structured results.

## Saved-profile functionality

OAuth discovery identifies a separate protected endpoint: https://dasha.fm/mcp/me. Anonymous discovery there returned HTTP 401 with a resource-metadata challenge. Published metadata advertises S256 PKCE, authorization-code and refresh-token grants, and dynamic registration.

That verifies discovery, **not end-to-end OAuth or account isolation**. The account tools are outside this case set. Before submitting them:
- Verify authenticated tool annotations, especially the save tool's write/overwrite behavior
- Provide a dedicated reviewer account with synthetic data and repeatable sign-in access
- Test no-profile recovery, confirmed save/replacement, all saved-profile reads, refresh/revocation and account isolation
- Keep credentials in secure review fields, never this bundle or a recording

## Demo and completion

Record actual host interactions: exact chart; Springfield clarification with unknown birth time; dated natal transits; unsupported tropical/Placidus request. If including account features, also demonstrate the dedicated account workflow. Verify playback and provide a reviewer-accessible recording link. This bundle contains a suggested sequence, **not a recorded demo**.

Still needed for a complete submission: actual package/source, confirmed publisher and listing details, intended countries and commerce information, final review runs, recording, and applicable account-access/portal requirements.

## Sources

- [Dasha connection guide](https://dasha.fm/connect)
- [Live public MCP endpoint](https://dasha.fm/mcp)
- [Protected-resource discovery](https://dasha.fm/.well-known/oauth-protected-resource)
- [Authorization-server discovery](https://dasha.fm/.well-known/oauth-authorization-server)
- [OpenAI tool guidance](https://developers.openai.com/plugins/plan/tools)
- [OpenAI authentication guidance](https://developers.openai.com/plugins/build/auth)
- [OpenAI plugin guidelines](https://developers.openai.com/plugins/plugin-guidelines)

