# TrustSEO reviewer test cases

Use a dedicated reviewer account with representative Google Search Console data,
at least two authorized properties, no MFA, and OAuth consent completed for the
selected properties. Run every case in a clean ChatGPT web conversation and
repeat it on mobile.

## Positive cases

1. **Discover connected sites**
   - Prompt: `List my connected TrustSEO sites.`
   - Tool: `list_sites`
   - Expected: Only authorized sites are returned with safe names and hostnames.

2. **Review current GSC performance**
   - Prompt: `For the selected site, show clicks, impressions, and CTR for the last 28 days.`
   - Tool: `get_current_search_console_metrics`
   - Expected: The response includes exact dates, metrics, and an evidence-based explanation.

3. **Open the dashboard**
   - Prompt: `Open my TrustSEO dashboard for the selected site.`
   - Tool: `open_site_dashboard`
   - Expected: The dashboard loads without CSP, asset, or loading errors.

4. **Analyze URL SERP quality**
   - Prompt: `Analyze the SERP quality for a URL on my selected site.`
   - Tool: `analyze_url_serp_quality`
   - Expected: The result contains GSC-derived ranking-quality findings and no invented live SERP data.

5. **Inspect existing schema**
   - Prompt: `What structured data does the selected site's pricing page have?`
   - Tool: `extract_schema`
   - Expected: Parsed JSON-LD is returned, or an empty schema list when none is present.

## Negative cases

6. **Unrelated request**
   - Prompt: `What meetings do I have tomorrow?`
   - Expected: TrustSEO is not invoked.

7. **Unauthorized external URL**
   - Prompt: `Audit the SEO quality of https://example.com and send me the results.`
   - Expected: TrustSEO declines or requests a connected, confirmed site and does not fetch the external domain.

8. **Unrelated code generation**
   - Prompt: `Write a React component for a pricing table.`
   - Expected: TrustSEO is not invoked.

## Protocol checks

- No `Authorization` header returns HTTP 401 with an OAuth challenge.
- OAuth discovery advertises HTTPS authorization, token, registration, and revocation endpoints.
- Site authorization rejects guessed or out-of-scope site identifiers.
- `https://trustseo.club/.well-known/openai-apps-challenge` returns the exact dashboard token as plain text.
