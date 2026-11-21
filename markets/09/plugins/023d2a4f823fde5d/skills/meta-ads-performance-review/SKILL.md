    ---
    name: meta-ads-performance-review
    description: Analyze stored Meta campaign, ad, and insight data in 33CRM, including impressions, clicks, provider leads, spend, account context, and data freshness. Use for Meta ads performance, campaign review, spend review, or ad-delivery analysis.
    ---

    Use this skill for Meta advertising performance stored in 33CRM.

Workflow:
1. Resolve the period and optional ad-account/campaign filters.
2. Call `get_marketing_report` for account-level stored totals.
3. Call `get_ad_insights` for daily rows or ad/campaign/account-level detail.
4. Call `list_meta_campaigns` and `get_meta_campaign` for campaign status/objective/schedule context.
5. Call `list_ads` to identify ads for insight filtering when needed.

Output:
- Spend and delivery summary
- Account-level performance
- Campaign/ad context
- Daily trend observations when enough data is available
- Data freshness
- Caveats and operational observations

Rules:
- Data is stored in 33CRM; these tools do not call or refresh Meta live.
- Provider-reported leads are not automatically CRM leads or conversions.
- Do not calculate or claim ROI, revenue attribution, CTR/CPC, or other derived metrics unless the user explicitly requests a mathematically valid derivation from compatible returned data.
- Never sum daily reach as unique reach.
- Never combine spend across different currencies.
- Reply in the user's language.
- Read-only only.
