# Shared Ads Manager Handoff State

```yaml
ad_creation_state:
  originating_skill:
  brief:
  approved_image:
  destination:
  selected_account:
  hierarchy:
  pending_checkpoint:
  generation:
  writes:
```

Before onboarding, set `originating_skill` to `ads-manager-ad-creation` or `ads-manager-starter-campaign`. Return to that owner with the capsule preserved; legacy capsules without an owner return to ad creation.

For Carpet Lite, `generation` retains the generation inputs and original result: draft ID, expiry, original proposal, generation metadata, asset references and optional unconfirmed logo candidate. Keep user edits and approved settings in the existing brief, image, destination and hierarchy fields. Keep the selected image separate from the original draft; onboarding must not overwrite these edits. Continue from this capsule without a draft-retrieval step. `writes` retains successful upload/entity IDs and each pending create's exact body and idempotency key. Keep this continuation state in the conversation; do not create another store or expose private IDs to the user.

```yaml
review_brief:
  account:
  scope:
  objective:
  review_focus:
  windows:
  evidence_thresholds:
  max_recommendations:
  max_hypothetical_budget_change:
  cadence:
```
