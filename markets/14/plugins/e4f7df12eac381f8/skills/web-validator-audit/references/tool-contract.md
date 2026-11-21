# Hosted Web Validator tool contract

Use this reference when selecting and parameterizing the **hosted MCP** at `https://web-validator-mcp.digestseo.com/mcp`. These are not local MCP tool names. Verify against the live tool schema if it changes; the server contract is authoritative.

| Exact hosted tool | Required input | Optional inputs | Actual behavior |
| --- | --- | --- | --- |
| `validate_html` | `html` | none | Sends provided HTML to Nu HTML Checker; returns validation messages, totals, truncation and overview |
| `validate_css` | `css` | none | Local CSS syntax parsing; reports first syntax failure where applicable; no external CSS service |
| `audit_seo_metadata` | `html` | none | On-page SEO and accessibility **signals**, not WCAG compliance or ranking measurement |
| `validate_schema_markup` | `html` | none | Parses JSON-LD blocks for JSON syntax only; `blocks_checked` may be zero |
| `check_broken_links` | `html` | `base_url`, `max_links` | Resolves eligible public HTTP(S) links; does not fetch `base_url`; reports but never follows redirects or retains response bodies |
| `generate_validation_report` | `html` | `css`, `check_links`, `base_url`, `max_links` | Combines supplied HTML validation, optional supplied CSS syntax, SEO/accessibility signals and JSON-LD syntax; optional bounded link check |
| `audit_public_webpage` | `url` | `check_links`, `max_links` | Fetches a single bounded static public HTML response and runs the combined audit; optional bounded public-link check; no crawl |
| `audit_public_site` | `site_url` | `max_pages`, `page_offset` | Same-origin sitemap-first robots-aware public HTML sampling; no HTML-link recursion or site-wide link check |

## Server-confirmed limits and defaults

- HTML and CSS input lengths: at most 200,000 characters each, subject to tool validation.
- `max_links`: integer 1-20, server default 15. Start with 10 when checking links unless the user asks for more.
- `audit_public_site.max_pages`: integer 1-8, server default 5. Choose 2 as the skill's conservative initial sample unless the user explicitly chooses a broader bounded scope.
- `audit_public_site.page_offset`: zero-based integer; start at 0. Continue using the returned `next_page_offset` only, when appropriate.
- Sitemap URL discovery is capped; account for `truncated`, `issue_groups_truncated`, `pages_partial`, and `pages_failed` when present.
- Server-enforced rate limiting, public-address restrictions, redirect limits, and input size checks take precedence over any suggested workflow.

## What tool outputs can support

- A valid JSON-LD block means parseable JSON, not recognized Schema.org types, Google eligibility, or structured-data correctness.
- CSS validation here is syntax analysis, not a W3C Jigsaw CSS conformance run. Do not suggest it contacted W3C CSS validation.
- A public webpage audit fetches static HTML and may follow only its bounded HTTP redirects. It does not run a browser, execute page JavaScript, log in, fetch linked CSS or images, or test rendered accessibility.
- `audit_public_site` reports discovery, selected/audited/partial/failed page counts, grouped issues and optional `next_page_offset`. It is a bounded sample, not proof of entire-site coverage.
- Link check redirects are not followed, and 403/429/network errors may be anti-bot restrictions or transient conditions; don't claim they are definitively broken.
- `overview.status` can mean passed, needs attention, not applicable, partial, or failed; use the actual returned label and explanation, never convert partial to passed.

## Common calling mistakes

- Do not pass a website URL as `html` hoping the server will fetch it. Use `audit_public_webpage` for one URL.
- Do not use `generate_validation_report` to crawl; `base_url` is only a relative-link base when link checking is enabled.
- Do not call `audit_public_site` to obtain exhaustive links; it doesn't run site-wide link checks.
- Do not fabricate unexposed tool flags such as `deep_crawl`, `render_js`, `fix_errors`, `export_pdf`, `follow_redirects`, `use_credentials`, or `automatic_repair`.
- Do not change a website, issue network requests to unapproved domains, or use other browsing tools to bypass limits because the audit tool declined a request.
