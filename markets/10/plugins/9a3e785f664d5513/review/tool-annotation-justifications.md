# RankOrg MCP annotation review

Reviewed the server registrations and the actions they invoke. All 13 tools explicitly set boolean readOnlyHint, openWorldHint and destructiveHint. These declarations cover the most impactful supported mode, including indirect effects. Fixed AI/API providers serving a private account do not alone imply open-ended access. Public website fetching, public content changes and arbitrary outbound destinations do.

| Tool | Read-only | Open-world | Destructive | Justification |
| --- | --- | --- | --- | --- |
| `getSiteContext` | `true` | `false` | `false` | Reads only the authenticated account’s site, profile and plan; no account mutation or public-web access. |
| `listContent` | `true` | `false` | `false` | Lists only the authenticated account’s stored articles; no mutation or public-web access. |
| `getContent` | `true` | `false` | `false` | Reads one owned article from the database; no mutation or public-web access. |
| `getSearchPerformance` | `true` | `false` | `false` | Reads analytics from the configured private Search Console property. The fixed Google API is a bounded account service, not arbitrary web search; no content or settings are modified. |
| `getTopicalMap` | `true` | `false` | `false` | Reads stored account clusters and keyword coverage; no generation, mutation or public-web access. |
| `generateContentMap` | `false` | `true` | `false` | Fetches an arbitrary website and external keyword/domain data, then persists a new report and fills missing cached clusters/lead associations. Additive report creation/enrichment; no article overwrite, cancellation or publication. |
| `updateContent` | `false` | `true` | `true` | Overwrites existing title, HTML and metadata; editing a published article changes public content immediately. Ownership is checked and published titles cannot change. |
| `researchKeywords` | `false` | `false` | `true` | Uses the saved private business profile with a fixed AI provider, then overwrites rootKeyword and keywordSignals. No arbitrary web research; prior saved keyword values are replaced. |
| `generateArticle` | `false` | `true` | `false` | Creates a new scheduled article (or returns an existing one) without overwriting article content. May fetch a public website sitemap and validate generated external links; does not publish immediately. |
| `publishContent` | `false` | `true` | `true` | Overwrites publication status and makes an article public, notifies IndexNow and may send to configured WordPress/webhook destinations. External sends cannot be recalled; explicit user confirmation is required. |
| `rescheduleContent` | `false` | `false` | `true` | Overwrites dates or swaps planned posts; skip cancels a planned day and clears keywordId. Unskip does not restore that association. Account-scoped writes only; the combined tool must flag its destructive skip mode. |
| `mergeContent` | `false` | `true` | `true` | Overwrites article statuses and redirect targets, including flattening redirect chains; changes public URLs to permanent 308 redirects and notifies IndexNow. Confirm the survivor and redirected articles. |
| `unmergeContent` | `false` | `true` | `true` | Overwrites MERGED status and removes an existing redirect to restore public content; notifies IndexNow. This replaces live routing state, even though re-merging is possible; explicit confirmation is required. |

## Review resubmission

Deploy the server changes first. In the existing MCP app, refresh Scan Tools against https://rankorg.com/api/mcp and verify all 13 deployed descriptors match this table. Include these justifications in the review fields or appeal as requested by the rejection email. Keep reviewer credentials in secure dashboard fields. Run the authenticated review cases, then resubmit the existing app; publish that app before updating the dependent plugin ZIP if the portal requires it. A ZIP change alone cannot update remote tool annotations.

Source verification does not establish that production has been deployed or that authenticated review cases passed. No live writes were used to test annotations.

References: https://developers.openai.com/plugins/plugin-guidelines and https://developers.openai.com/plugins/deploy/app-review . Current guidelines say justifications are no longer required, but the received rejection requests them; this document supplies them for that review.

## Latest supplied scan

The creator supplied a scanned rescheduleContent definition with readOnlyHint=false, destructiveHint=true, openWorldHint=false and capability_labels=[destructive]. This confirms the corrected annotation is present in that scan. The portal reports: “This tool update needs further review before it can go live.” Approval and live availability remain pending. This evidence applies to rescheduleContent only; it does not verify every deployed tool or authenticated test case.
