---
name: plan-healthcare-payment
description: Build numerical healthcare payment and collection assumptions using official fee-schedule guidance, provenance, payer context, and user-supplied amounts. Use for feasibility reimbursement planning; this is not a code lookup, coding recommendation, or coverage determination.
---

# Plan payment assumptions

Read [working rules](../../references/working-rules.md) and [sources and fees](../../references/sources-and-fees.md), including the guided-lookup and rights boundaries.

Guide the user to the applicable official fee-schedule resource. The user or billing specialist performs code selection and any licensed lookup there; bring back numerical amounts and metadata using [payment assumptions](../../assets/payment-assumptions.csv). Do not bundle, retrieve in bulk, import, or reconstruct a CPT catalog, descriptors, or code crosswalk. This workflow remains useful when the amount is unknown: identify the missing lookup and compare explicitly hypothetical amounts.

For each original service label, record payer, year, location, setting, clinician, rate source, amount basis, adjustments already applied, and the coverage/billing dependencies. Separate fee-for-service, private payer contracts, capitation, and bundled payment. A per-visit model is inappropriate for capitation unless a separately explained allocation is merely an analytical scenario.

Build the collection waterfall using explicit assumptions. Do not automatically discount product payment by a clinician payment percentage. Do not confuse claim-payment probability with payer cost-sharing. Denials ultimately recovered belong in both the appropriate probability and timing, without double counting the same loss. If only net collected revenue per encounter is provided, model it as that basis and do not apply the payment waterfall again.

Deliver a sourced amount matrix, a collection/timing explanation, and unresolved eligibility or contract questions. A fee-schedule listing never establishes medical necessity, coverage, permissible same-day combinations, or profitability. Do not choose treatments or encounter frequency to achieve financial goals.
