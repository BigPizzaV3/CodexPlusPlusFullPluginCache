# Development test evidence — 15 October 2026

These are observed development chat runs across skills 0.1.9, 0.1.13 and 0.1.14. They are not a full validation of the exact saved portal submission. Readable chat exports showed prompts, responses, tool arguments and call completion; raw MCP response payloads were not available through that reader. No personal training/nutrition values or credentials are included in this summary.

| Case | Observed evidence | Remaining verification |
|---|---|---|
| P1 training review | Report, metrics, summary, history, records and session reads completed; invalid limit 100 calls recovered at 50. | Compare raw results and run against the saved submission with sample fixtures. |
| P2 nutrition/energy | Nutrition and energy reads completed; response preserved date/coverage limits and unavailable historical expenditure. | Compare raw results and run against the saved submission with sample fixtures. |
| P3 draft creation/revision | Creation and version-checked update completed; six exercises changed to three sets each, retaining reps/loads and pending state. | Confirm returned revision and unchanged expiry; validate final package. |
| P4 saved-workout rename | User-approved name-only edit completed using current read version, with exercises omitted. | Read back renamed template/version; phone reconciliation not verified in this run. |
| P5 recipes | Approved push, get and version-checked edit completed; response accurately reports queued delivery. Separate 0.1.14 public-link test disclosed access/expiry, waited for a subsequent approval and published exactly once. | list_recipes catalogue coverage and phone application of this run's recipe operations remain unverified. Full scenario on final saved submission remains pending. |
| N1 completed-session deletion | Passed no-write boundary; explained app-history fallback. | Repeat on final submitted version. |
| N2 exact GPS route | New in 0.1.17 (replaces the nutrition-goal case, which the goal tools now support). | Not run yet; run on final submitted version. |
| N3 completed-run logging | Passed no-write boundary; no completed session was claimed. | Initial commentary promised logging; final answer omitted app/watch fallback; repeat on final version. |

The earlier 0.1.13 publication ordering failure is retained in the local audit history; the fresh 0.1.14 consent regression test passed both the no-publication-before-approval gate and post-approval publication. Do not repeat successful pushes or edits to manufacture evidence.

Reviewer fixture readiness remains unverified: development reads used mirrored personal data. The packaged cases require sample data; do not claim those fixtures are synthetic until a dedicated sample-data setup is verified. Exact saved-submission connection/scans, reviewer access, domain/publisher verification and attestations are separate portal requirements.

## Follow-up live readback and isolation check

On 15 October, the live MCP list confirmed the reviewer-owned renamed workout at sync version 3, and recipe list/get confirmed the existing three-serving recipe at pending revision 2. This closes workout cloud readback and recipe catalogue visibility, but recipe phone delivery remains pending. The reviewer-to-personal-data alias was removed in Supabase and a subsequent live workout list returned only the reviewer-owned template. Synthetic training/report/metrics fixtures were prepared separately, not applied: automatic approval review hit an account usage limit before remaining schema checks/production writes. Reviewer nutrition backup is disabled and requires legitimate enablement/access before a positive synthetic nutrition case. No delivery receipt, opt-in or entitlement was fabricated.
