---
name: portravo-prepare-takeoff
description: "Check trade availability and existing-credit cost, create an owned Portravo project, attach the actual plan PDF, and start an explicitly approved takeoff."
---

# Prepare a construction takeoff

Use the connected service at https://portravo.com/mcp through normal OAuth. If unavailable, preserve the selected plan and provide https://portravo.com/developers/mcp as the handoff. `get_profile` and `list_projects` identify the owned account and work.

Call `preflight_takeoff` without arguments for the live catalog, or with either proposed trades or a project_id, not both. Use `list_pricing_markets` for supported metro codes. Preserve automatic versus team-assisted scope, unresolved coverage and current cost; do not infer that every named trade runs automatically. Preflight neither reserves credits nor purchases anything.

Create a project only when requested, using `create_project` with an explicit selection returned by preflight and a stable idempotency_key. Keep that key after uncertainty. Attach only the user’s actual complete PDF with `attach_plan_pdf` and exactly one file source. Signed file transfer accepts up to 10 MiB; exact-byte inline base64 supports at most 32 KiB. Without an available transfer, use the returned owned project reviewUrl for browser upload up to 50 MiB. Never invent descriptors, truncate a plan or replace existing reviewed work.

Before `run_takeoff`, obtain any missing approval for the preflight selection and exact existing-credit ceiling. Pass confirmed_trades, max_credits and confirm_credit_use=true with a stable idempotency_key. Current maximum ceiling is three; the server rechecks actual cost. Do not infer one credit per trade or authorize billed overage. Changed cost/selection, insufficient balance or a credit guard needs resolution, not a larger ceiling or a new job.

Use `get_takeoff_status` after a running or uncertain response. Status reads never restart a run. Once ready, use `get_takeoff` to review actual source links, quantities, trade scope and unresolved work. Completion does not establish 95% whole-plan accuracy or a bid-ready estimate. Continue source and estimator review before pricing or export. Preserve errors and actual refund state instead of claiming a failed run succeeded.
