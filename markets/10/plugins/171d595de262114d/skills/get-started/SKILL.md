---
name: get-started
description: Connect RefreshAgent and run the first useful live SEO workflow after installation.
---

# Get started with RefreshAgent

Use this skill for a new installation or when the user asks what RefreshAgent can do with their connected data.

## First run

1. Call `get_account_status` to check whether Search Console, Analytics, and optional WordPress access are available.
2. If the target site is ambiguous, call `list_connected_sites`.
3. If Search Console is connected, call `compare_search_performance` for the last 30 days as the default first-value workflow.
4. Use the direction of the evidence to choose one focused follow-up:
   - meaningful growth -> `find_biggest_gainers`;
   - meaningful decline -> `find_biggest_losers` or `diagnose_search_change`;
   - stable traffic with meaningful impressions -> `find_ctr_opportunities`;
   - refresh prioritization -> `find_content_decay`.
5. Explain the result using the exact returned metrics and comparison window.

## Missing access

Search Console and GA4 are independent. Do not block Search Console workflows because GA4 is unavailable.

If the required data source is not connected, explain which connection is missing and direct the user to RefreshAgent's connection flow. Do not claim access that the authenticated account does not have.

## Safety

Read-only evidence and diagnostics are the default. Never make a WordPress change during onboarding. WordPress edits require the dedicated inspect -> preview -> explicit approval -> apply -> verify workflow in the `wordpress-seo-execution` skill.
