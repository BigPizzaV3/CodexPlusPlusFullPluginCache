---
name: wordpress-seo-execution
description: Safely inspect, preview, apply, verify, and roll back SEO title and metadata changes on WordPress sites connected to RefreshAgent.
---

# WordPress SEO execution

Use RefreshAgent as the controlled execution layer between SEO evidence and WordPress. The host model supplies the reasoning. Never skip the preview/approval step.

## Safety contract

For any WordPress mutation:

1. Establish the evidence first. Use Search Console/GA4 tools when the requested change is based on SEO performance.
2. Call `list_wordpress_sites` if the target WordPress connection is ambiguous.
3. When SEO evidence identifies a URL rather than a WordPress ID, call `wordpress_resolve_url`.
4. Call `wordpress_get_content` when the page body materially affects the recommendation.
5. Call `wordpress_inspect_seo` before recommending an edit.
6. Call `wordpress_preview_seo_change` with the exact proposed fields.
7. Show the user the meaningful before/after diff and the reason for the change.
8. Do **not** call `wordpress_apply_seo_change` until the user explicitly approves that exact preview.
9. Pass the unchanged `expected_fingerprint` returned by preview when applying.
10. After apply, immediately call `wordpress_verify_seo_change` and report both database state and live-rendered verification.
11. Offer rollback when the user asks to undo the specific change. Use `wordpress_rollback_seo_change`; never manufacture a reverse edit manually.

If apply reports a stale-preview error, inspect and preview again. Do not reuse the old fingerprint.

If rollback reports a conflict, stop. That means the affected fields changed after RefreshAgent's edit and rollback would risk overwriting later work.

## Supported fields

The MVP execution surface supports:

- WordPress post/page title;
- SEO title;
- meta description.

SEO metadata is provider-aware:

- Yoast SEO;
- Rank Math;
- RefreshAgent fallback when neither is active.

If provider resolution is ambiguous, inspect first and explicitly select the intended provider rather than guessing.

## Evidence-led CTR workflow

For a request such as "fix my best CTR opportunity":

1. `find_ctr_opportunities`
2. choose the relevant page/query based on returned evidence;
3. `wordpress_resolve_url` using the returned page URL;
4. `wordpress_get_content` when page context is needed;
5. `wordpress_inspect_seo`;
6. reason about a proposed title/meta change;
7. `wordpress_preview_seo_change`;
8. show evidence + exact diff;
9. wait for explicit approval;
10. `wordpress_apply_seo_change`;
11. `wordpress_verify_seo_change`.

Do not claim that a title/meta change will improve rankings or CTR. Describe it as a hypothesis tied to observed evidence and measure the later outcome.

## Read vs write access

Inspection, preview, and verification use read access. Apply and rollback require RefreshAgent's separate `seo:write` OAuth scope. A client without write permission should still be able to diagnose and preview changes.
