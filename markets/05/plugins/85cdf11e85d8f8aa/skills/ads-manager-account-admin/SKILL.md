---
name: ads-manager-account-admin
description: "Check what remains to finish an existing Ads Manager account's setup, launch billing setup, add or replace its logo, and manage users, pending invitations, roles, and removals. Use for existing-account setup/readiness questions, help setting up billing or a logo, and requested account-access changes. Setup checks are read-only; membership and logo writes require confirmation and verification. Do not use for new-account creation, ad creation, campaign/ad-group/ad changes, reporting, or delivery diagnosis."
allowed-tools:
  - list_ad_accounts
  - list_ad_account_users
  - add_or_update_ad_account_user
  - remove_ad_account_user
  - upload_account_logo_from_url
  - upload_account_logo_file
  - set_account_logo
  - get_onboarding_status
  - show_account_setup_widget
  - get_ads_manager_route_link
---

# Ads Manager Account Admin

Own existing-account setup questions, billing setup, membership changes, and logo setup or replacement. Keep simple account or membership reads connector-native: if the user asks only to see accounts, active users, or pending invitations, answer from the live read and do not manufacture a confirmation or write flow. New-account creation belongs to `$ads-manager-onboarding`; delivery diagnosis belongs to `$ads-manager-delivery-recovery`.

## Main Workflow

Separate read-only setup checks from confirmed account changes:

1. Identify whether the request is a setup/readiness question, billing setup, a membership read or change, or account-logo setup or replacement.
2. Resolve exactly one existing account from live results. Ask the user to choose by visible account name only when multiple plausible accounts remain; never ask them to transcribe an id.
3. Before advancing past the active branch, read and follow every linked reference whose condition matches that branch. When multiple conditions match, load all of them before acting; do not load unrelated references merely because they exist.
4. Read the current account-scoped state needed for the selected branch. For a setup question or billing request, follow the Setup Branch without entering the write sequence below. For an explicit logo request, go directly to the Existing-Account Logo Branch, not back through the launcher. Do not infer setup, membership, invitation, or logo state from a name, an earlier conversation, or a prior account.
5. For a requested membership or logo change, present the selected account and the exact user-visible change that would occur. Obtain explicit confirmation immediately before the first consequential write.
6. Execute only the approved write sequence, preserve successful returned ids privately, then verify or reconcile using the strongest live evidence the connector can provide.
7. Report only proven outcomes. If a result is failed or ambiguous, stop dependent work and follow the matching safety instructions before any corrected retry.

- Before any membership write, retry, or ambiguous-outcome reconciliation, read and follow [write-safety.md](references/_shared/write-safety.md).
- Before selecting, generating, validating, uploading, applying, retrying, or reconciling an existing-account logo, read and follow both the [shared image asset contract](references/_shared/image-asset-contract.md) for `account-logo` and [write-safety.md](references/_shared/write-safety.md).

## Setup Branch

For requests such as "what else needs to be done for account setup?" or "help me set up billing," call `get_onboarding_status` once for the resolved account. This read and displaying a widget do not require write confirmation or authorize a membership or logo change.

Use `billing_setup_status` and `billing_setup_flow` for billing questions, independently of the overall `recommended_next_step`. `complete` means no billing setup action is needed, regardless of flow; it does not establish campaign launch readiness or clear payment holds. Report confirmed setup completion without saying ads are ready to run. For `required`, offer the existing account setup widget only for `self_serve_card`; direct `postpaid_invoice` owners to their OpenAI account team. Otherwise explain that the billing arrangement needs verification; do not offer a card form.

Show `show_account_setup_widget` once when available for confirmed required self-serve card billing, or a missing logo (`has_account_logo=false` and `logo_in_review=false`) with no known submission awaiting review. Failed or inconclusive reads, pending review, completed setup, identity, and access issues alone do not qualify. If status conflicts with a known logo submission, skip the widget. The widget is the primary card setup flow. Its `billing_url` is reserved for its own external recovery; do not send it as a setup link. If the widget is unavailable or fails after confirmed required self-serve card billing, call `get_ads_manager_route_link` with `route_kind="billing_settings"` for the same account and offer its returned ordinary billing settings page link. If that read fails, explain the confirmed need and offer to retry here later. Never claim the widget displayed or construct a URL.

Avoid repeating an unchanged active widget the user has already seen or deferred. Self-serve card billing is completed through the widget's secure form, not chat: never collect payment details or invoke its private billing helpers from the model. Saving or closing billing updates that same widget; do not render another on save. A setup-complete result does not establish campaign launch readiness or clear independent identity, access, or account-review blockers.

## Membership Branch

For a requested access change, use the exact email the user supplied and read both active users and pending invitations for the selected account before every write. Use the email search when available, and follow pagination before concluding that the email is absent. Never use membership data from one account to act on another.

Classify the live state before proposing a write:

| Live state | Requested change | Behavior |
| --- | --- | --- |
| Active with the requested role | Grant or role change | Report that the requested state already exists; do not write. |
| Active with a different role | Role change | Propose the exact new role, confirm, then use the live add-or-update action. |
| Active | Removal | Propose removal of that exact email from that exact account, confirm, then use the live removal action. |
| Pending invitation | Removal | Stop and explain that this workflow cannot cancel a pending invitation; do not call the active-user removal action. |
| Pending invitation | Grant or role change | Show that the email is already pending. Do not silently describe the operation as a new grant or re-invite; proceed only with behavior supported by the live add-or-update action and report its actual result. |
| Absent from both lists | Grant or invite | Propose the exact email and requested role, confirm, then use the live add-or-update action. |

- The proposal must show the selected account name, exact email, detected active/pending/absent state, requested role when applicable, and the plain-language change that will occur. Do not expose raw tool names or request fields in that proposal.
- If the live action requires approval to invite an email into the workspace, set its workspace-invite confirmation field only after the user explicitly approves inviting that exact email. Do not treat approval for a different account, email, role, or earlier payload as sufficient.
- For multiple explicitly named emails, build one bounded proposal table and never extend its scope. Each email still needs its own active-and-pending classification, exact approved change, independent write result, and read-back verification.
- After a successful membership write, read the relevant active or pending state again and report only what that read confirms. If the write response is missing or ambiguous, reconcile with fresh reads before considering any retry; never claim access changed from an ambiguous result.

## Existing-Account Logo Branch

Resolve exactly one existing account before logo work. Accept only a user-supplied or explicitly approved logo candidate: a provided attachment, a direct public image URL, or a generated logo after the user explicitly chooses generation. Never inspect a website or its assets to discover a logo, and never treat a webpage URL, local filesystem path, selected image, generated image, or approval alone as an uploaded logo.

1. Read and follow the linked image and write-safety references before accepting, generating, validating, uploading, applying, retrying, or reconciling the logo.
2. Propose the exact candidate logo and selected account. Ask for explicit approval of the exact sequence: upload that candidate for that account, then submit the returned upload as the account logo.
3. Use the matching account-scoped logo upload action once for that approved candidate. Continue only when it succeeds and returns a non-empty opaque `file_id`; retain that token privately and never treat upload alone as an applied logo.
4. Call `set_account_logo` for the same selected account with that returned token and a short user-visible description grounded only in the exact approved candidate.
5. Treat a successful apply result as submission for brand review. If a public logo already exists, it remains active until approval; do not claim the public logo changed immediately.
6. After a successful submission, call `get_onboarding_status` once for the same account and apply the Setup Branch's widget criteria. The earlier widget remains retired; any qualifying checklist must be a fresh instance. Otherwise report confirmed status in text, preserving `In review` until approval is confirmed.
7. A fresh account read may provide current account context, but it cannot prove that a submitted replacement is already public. If upload or apply is failed or ambiguous, do not continue or blindly repeat it; follow the shared write-safety recovery path.

## Scope And Tool-Owned Rules

Use only fields, enum values, validation, permissions, response fields, and backend errors exposed by the live actions. Do not restate or override email validation, role enums, permission rules, tool schemas, logo file requirements, or backend error behavior in this skill. Never create a new account, change ads or hierarchy, perform reporting, diagnose delivery, or turn a read-only request into a write while using this workflow.
