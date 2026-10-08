---
# SPDX-License-Identifier: LicenseRef-Regit-Proprietary
# Copyright (c) 2026 Regit
name: regit-priips-calculation
description: Calculate and review PRIIPs KID risk, scenario, and cost figures from supplied facts; compare published and fresh figures for numeric review triggers.
---

Use this skill when the user wants to prepare or review numeric PRIIPs KID
figures from product facts, including a discrepancy check against an existing
KID. Keep the job focused on the requested figures and their evidence.

First establish that the request concerns PRIIPs, the exact product/share
class and figure sought, and the relevant valuation or review date, holding
period, and currency context needed for that figure. For another regulation,
state this plugin's PRIIPs scope instead of forcing a PRIIPs operation.

1. Use only the approved `https://ai.regit.io/mcp/priips` connection with its
   exact resource and `priips:compute` scope. If linking or permission is missing,
   explain the access step and stop before calculation.
2. For an existing KID, use readable content available to the chat host to
   extract the published SRI, relevant MRM/CRM classes, and moderate-scenario
   returns by displayed holding period. Record the exact product/share class,
   document date, units, horizons, and page or section for each figure. The MCP
   connection does not ingest the document. Ask only when an extracted value or
   its product context is ambiguous; if content is unreadable, request the
   published figures and their source instead.
3. Discover the connection's current tools and advertised input schemas. Read
   `regit://priips/version` and `regit://priips/schemas` when available for
   provenance and detail; the advertised tool input schema governs calls and
   may differ structurally from the raw engine registry. Compute fresh risk,
   cost, or scenario figures only from current supplied product data and a
   supported tool. For SRI, obtain the MRM/CRM classes and each applicable
   liquidity criterion rather than inferring them from a generic liquidity
   label. For scenario presentation, use already-selected outcomes; do not
   treat presentation arithmetic as scenario selection. Chain cost operations
   only when their required inputs and prior Regit results exist. Never reuse
   old KID figures as fresh recomputations. Ask for missing, ambiguous, or
   invalid inputs, including numeric/range constraints, before calling; keep
   decimal values as strings where the live schema requires them.
4. If the user asks for a KID discrepancy check, compare the published and
   freshly recomputed SRI classes and moderate-scenario returns with the
   current numeric KID-review tool. Normalize published percentages and any
   Regit scenario fractions to one explicitly declared return unit only with
   deterministic exact-decimal arithmetic available to the host, never a
   binary-float or model-estimated conversion. If that is unavailable or the
   representation is ambiguous, request old/new values in the same stated
   units. Align displayed holding periods; include
   old/new MRM or CRM only as complete
   pairs when known, and supply the benchmark/proxy applicability fact. If a
   fresh figure cannot be computed from available current inputs, request the
   missing data or an externally recomputed figure with its provenance.
   Interpret shifts strictly greater than five percentage points and any
   unmatched horizons separately. A negative numeric trigger does not settle
   the review calendar, qualitative changes, whole-KID compliance, or revision.
5. Present published versus fresh figures with their sources, the Regit
   `result`, relevant `trace` steps, actual `coverage` or warnings, and engine
   version/provenance returned. For a discrepancy, prepare candidate corrected
   numeric figures and evidence for the manufacturer's review; do not claim to
   generate, validate, or publish a complete KID. If a tool reports an error or
   incomplete evidence, state that limit instead of giving an authoritative
   number.
