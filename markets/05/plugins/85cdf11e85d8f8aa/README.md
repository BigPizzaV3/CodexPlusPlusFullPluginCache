# Ads Manager

Use Ads Manager to discover and manage ad accounts, campaigns, ad groups, and ads; analyze performance, conversions, and change history; upload creative images; and, when available, complete self-serve account setup. When multiple campaigns need selection, call `list_campaigns` with `include_performance_metrics=true` so the gated picker can show recent performance.

## Try it

- Help me create a new Ad.
- Use $ads-manager-insights to compare performance across my campaigns.
- Use $ads-manager-insights to summarize common topics in my Business Agent conversations, when available.
- Based on those Business Agent sizing concerns, what sizing information should we add?
- Show the recorded changes to my campaign's budget and who made them.
- Use $ads-manager-start-agent to set up recommendation-only reviews for my campaigns.
- Compare campaign performance and highlight opportunities to improve.
- Use $ads-manager-review to run a read-only CMO review of my Ads Manager account.
- Use $ads-manager-actionable-review to review my account and prepare exact changes for my approval.
- Use $ads-manager:ads-manager-setup to help me get started with Ads Manager.
- Help me create an Ads Manager ad account for my business.
- Get help with Ads Manager or troubleshoot why my campaign, ad group, or ad is not delivering.
- Diagnose why an existing campaign is not scaling and give me a read-only recovery plan.

The plugin materializes the first-party `connector_openai_ads_manager` app. It remains explicitly installable and subject to workspace app-access policies: a NoAuth install creates a persisted Ads Manager connector link before its tools are exposed, while existing OAuth links retain their refresh and reauthentication support.

When enabled for both the user and selected account, `ask_business_agent_insights` answers aggregate Business Agent conversation questions and supports practical business recommendations grounded in those themes through this same app in ChatGPT and Codex. It takes the selected `ad_account_id`, a self-contained `question`, and optional paired UTC `start_time` and `end_time`. The window selects ingestion partitions; ingested snapshots may contain earlier conversation activity. Answers include snapshot coverage and limitations; unavailable or insufficient evidence does not produce an invented answer. Individual conversation summaries and raw transcripts are not exposed. Follow-ups retain the account and returned UTC ingestion window unless the user changes them.

## Shared references

Reporting instructions have the following owners:

| Location | Responsibility |
| --- | --- |
| App instructions | Route reporting, recommendations, and diagnosis |
| Insights skill | Resolve scope, select tools, collect evidence, and present reports |
| `shared-references/insights-contract.md` | Metric meaning, comparisons, aggregation, ranking, currency, and unavailable values |
| Tool descriptions and schemas | Argument meaning, defaults, dependencies, and supported response behavior |
| Tool errors | Rejection reasons, recovery actions, and corrective guidance |
| Review skills | Recommendation evidence requirements and thresholds |

When adding a reporting argument, update its schema, description, and pinned eval tool metadata/provenance together. Update the shared contract when interpretation changes and the insights workflow when tool selection or evidence collection changes. Sofa owns attribution calculations, account-specific event recognition, authorization, and data availability.

Canonical cross-skill references live in `shared-references/`. Edit those files directly; do not manually edit generated copies under `skills/*/references/_shared/`.

When a canonical shared reference or `shared-references/consumers.json` changes, run:

```bash
python chatgpt/oai-maintained-plugins/plugins/ads-manager/scripts/materialize_shared_references.py
```

Commit both the canonical changes and regenerated skill-local copies. Use `--check` to verify copies are synchronized.

It bundles eleven skills: `ads-manager-setup` welcomes users and routes their first task; `ads-manager-onboarding` guides progressive business-first self-serve account creation with optional attached, linked, or generated logos; `ads-manager-account-admin` coordinates confirmed existing-account user, invitation, role, removal, and logo workflows; `ads-manager-ad-creation` owns URL-driven website and image discovery, single- and multi-ad drafting, campaign-aware creative image handling, preview, upload, and save or publish; `ads-manager-entity-management` coordinates direct campaign and ad-group creation plus existing campaign, ad-group, and ad updates; `ads-manager-insights` reports performance, rankings, comparisons, trends, conversion data, and aggregate Business Agent conversation insights when available; `ads-manager-help` combines live connector evidence with specific Ads Manager Help Center articles; `ads-manager-delivery-recovery` identifies the first constrained delivery layer and produces a prioritized recovery plan; `ads-manager-start-agent` gathers a bounded recommendation goal, scope, and cadence before running once or preparing recurring read-only reviews; `ads-manager-review` performs scheduled or manual read-only shadow analysis and returns proposal-shaped performance recommendations without mutating Ads Manager state; and `ads-manager-actionable-review` is an explicit-invocation experiment that performs a manual read-only review, offers exact owner-supported changes for approval, and delegates accepted writes to their owning skills.
