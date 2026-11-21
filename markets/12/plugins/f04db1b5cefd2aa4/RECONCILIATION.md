# AdNeuron Ads Agent v1.1.0 — platform-neutral update review

**Public target listing:** `plugin_asdk_app_6ad30793384c81919c4ff090fbeae35d` (user-supplied). Verify dashboard ownership and update association before uploading.

**Existing package baseline:** AdNeuron Ads Manager 0.3.1, `name: adneuron-meta-ads`. Keep the internal identifier unchanged for this update pending confirmation that renaming it will not create a new listing. This is a compatibility identifier, not the customer-facing product name.

**Customer-facing branding:** `AdNeuron Ads Agent` / `Your AI agent to create, manage, and optimize ads.` No Meta-only wording in general product positioning. Current supported workflow descriptions cover Google Ads and Meta Ads; Amazon Ads is future-only.

**Preserved:** original v0.3.1 MCP configuration and endpoint, logo PNG, reporting skill, developer identity, category, and existing review cases. Added five workflow skills and references. The package does not change the live MCP service, OAuth scopes, or ad-account permissions.

**Known discrepancy:** v0.3.1 listing describes read-only operation, while the user reports successful campaign creation through an AdNeuron integration. Verify which public plugin, MCP tool set, OAuth permissions, and review-approved write capabilities apply before claiming production campaign creation. Refresh review test cases to cover verified writes and approval gating; existing test cases are preserved as baseline only.

**Submission blockers:** Validate `publication.countries: []` semantics and schema; confirm packaging accepts `skills/` and `references/`; verify public listing update linkage and OAuth/write access; refresh test cases and demo if required. This is a review candidate, not a submission-ready release. No deployment or publication performed.
