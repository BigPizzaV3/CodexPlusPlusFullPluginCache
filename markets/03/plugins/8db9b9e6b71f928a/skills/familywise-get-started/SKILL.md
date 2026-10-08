---
name: familywise-get-started
description: Guide a FamilyWise Plus or Premium customer from current source-backed setup status to a useful first week. Use when the user asks to set up FamilyWise, continue onboarding, connect a Home, or learn the next setup step. Do not use for a one-off read or for protected member, invitation, health, custody, or account setup.
---

# Get Started

Build a useful first FamilyWise week without creating parallel onboarding state.

1. Call `familywise_get_setup_status`. If the result says a shared Home is required, route the customer to FamilyWise Account & Sharing and stop. Never collect member or invitation data in chat.
2. Explain only the returned `nextSafeStep` and incomplete sections. Do not infer completeness from conversation history.
3. For an ordinary planning step, call the matching read tool, show one exact proposed change, and wait for explicit confirmation before calling the granular write tool.
4. Re-read the affected record and setup status after each confirmed change.
5. Stop on wrong Home, insufficient role, stale version, missing confirmation, unknown result, or a request for protected profile data.

There is no batch setup write. Home creation, invitations, birthdates, exact ages, allergies, health information, medications, custody details, and private notes stay in FamilyWise HQ.
