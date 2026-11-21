# Account entitlement questions

Read `get_profile` for the caller's current entitlement, status and period end. Never infer a plan from a permission or an old conversation. Do not guess a charge or renewal date: a period end alone does not prove a future payment. No offers, upgrades, checkout or billing links in the conversation; never request card details.

- Use `ownershipAllowance.remainingOwnedSlots` for workspace capacity. Legacy `list_workspaces.limit` means active-owned-workspace allowance, not pagination. `activeCount` includes joined workspaces; do not subtract it from that allowance. Joined and archived workspaces consume no owned slots. Null quota values mean no plan quota, not zero.
- Invitations use the workspace owner's entitlement. A Free invitee can join an eligible owner's workspace without subscribing. Roles still control permitted actions.
- Exchange retrieval uses the retrieving account's entitlement across its workspaces, not the workspace owner's. Distinct external analyses first delivered count; rereads, retries and corrections do not. When available, use `get_analysis_exchange` for participation and allowance. If absent, say Exchange is temporarily unavailable.
- Paid access does not enable Exchange participation, accept its terms or bypass validation, rights and moderation. Publication has no plan quota; this is not an exemption from safeguards.
- Explain cancellation or downgrade from the returned account context. Do not cancel, change plans or enable participation merely because the user asks how those actions work.

On older servers without explicit fields, report what is missing rather than inventing an allowance. Do not add account-specific values, prices or quota numbers to this skill.
