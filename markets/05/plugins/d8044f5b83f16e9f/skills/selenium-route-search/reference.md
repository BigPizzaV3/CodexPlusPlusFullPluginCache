# REST reference (for agents not using the MCP server)

Base URL: `$SELENIUM_API_URL`. Auth: `Authorization: Bearer $B12_API_KEY` on
every call. All `/v1/` responses set `Cache-Control: no-store`. Every response
carries `X-Request-ID`; send your own to correlate support reports.

## Quote (no charge)

```
POST /v1/route-searches/quote
{ "smiles": "CC(=O)Oc1ccccc1C(=O)O", "tier": "standard",
  "instructions": "Avoid protecting groups; prioritize convergent routes." }
→ { "credits_required": 100, "version": "v1.3.31", "params": {...} }
```

## Submit (debits credits, returns 202)

```
POST /v1/route-searches
Idempotency-Key: aspirin-standard-2026-07-09     # stable! reuse = same job
{ "smiles": "...", "name": "aspirin", "tier": "standard",
  "instructions": "Avoid protecting groups; prioritize convergent routes." }
→ 202 { "id": "<job_id>", "status": "queued", "credits_charged": 100,
        "links": { "self": ..., "routes": ..., "cancel": ... } }
```

Tier presets:
- scout: `10 credits`; fixed bounds of `researcher_runs=1, max_route_families=1, target_ready_routes=1, timeout_minutes=15`; no follow-up research
- basic: `50 credits`; `researcher_runs=1, max_route_families=3, target_ready_routes=1, timeout_minutes=30`
- standard: `100 credits`; `researcher_runs=5, max_route_families=8, target_ready_routes=3, timeout_minutes=90`
- exhaustive: `300 credits`; `researcher_runs=12, max_route_families=24, target_ready_routes=6, timeout_minutes=360`

Scout is a bounded feasibility screen and does not accept numeric overrides or
guarantee latency, evidence, or a solved route. Other tier prices are minimums;
numeric overrides can increase a quote when they request more compute than the
selected tier includes.

## Poll

```
GET /v1/route-searches/{job_id}
→ { "status": "running",
    "progress": { "families_found": 5, "families_solved": 2, "elapsed_minutes": 12 },
    "retry_after_seconds": 60 }          # use as your poll interval
```
Statuses: `queued`, `running`, `completed`, `partial`, `failed`, `cancelled`.

## Fetch routes (valid mid-run)

```
GET /v1/route-searches/{job_id}/routes
→ { "status": "partial", "target": {"smiles": ..., "name": ...},
    "families": [
      { "id": "f_1a2b3c4d", "name": "...", "status": "solved",
        "best_route": {
          "molecules": [{ "smiles": ..., "role": "starting_material",
                          "commercially_available": true }, ...],
          "reactions": [{ "label": "Fischer esterification",
                          "reaction_smiles": "...",
                          "assessment": { "band": "likely_feasible" } }, ...],
          "scores": { "judge_combined_score": 92.0, "feasibility_band": "likely_feasible" },
          "stats": { "reaction_count": 1, "commercially_solved": true } } },
      { "id": "f_...", "name": "...", "status": "incomplete" }   # stub
    ] }
```

## Other

```
GET  /v1/route-searches?status=completed&limit=50   # list; paginate via next_cursor
POST /v1/route-searches/{job_id}/cancel             # refund only if not started
GET  /v1/credits                                    # balance + ledger
GET  /v1/usage                                      # balance + jobs incl. by_source split
GET  /v1/capabilities                               # versions, param bounds, pricing inputs
```

## Error shape

```
4xx { "detail": { "code": "insufficient_credits", "message": "...",
                  "request_id": "..." } }
```
Key codes: `insufficient_credits` (402), `outstanding_job_limit_exceeded` /
`submission_rate_limit_exceeded` (429), `invalid_smiles` /
`unsupported_molecule` / `molecule_too_large` (422), `idempotency_key_conflict`
(409, key reused with different params), `route_search_not_found` (404).
