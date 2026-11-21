# 1.0.11

- Four new read-only tools for AI connector v2 Release A: `get_sleep_history` (up to 30 days of
  nightly detail), `get_tonight_target`, `get_account_status` and `explain_lezonder`. Six tools in all.
- New permission `lezonder:mcp:details:read`; users approve it once. The draw tool and draw
  permission are not listed until Release B.
- Description, capabilities, prompts, three positive review cases and one negative case updated.
- Plan: `docs/ai-connector-v2-plan.md`.

# 1.0.10

- Description adds: "Scores calculated from a direct Oura connection can't be shared,
  because Oura's developer rules don't allow it. Oura data synced through Apple Health works."
- Keeps everything from 1.0.9. Tools, data, sign-in and review cases unchanged.

# 1.0.9

- New subtitle: "See if your sleep is improving" (was "Your Lezonder Sleep Scores").
- Keeps everything from 1.0.8: every country, any existing Lezonder account.
  Tools, data, sign-in and review cases unchanged.

# 1.0.8

- Available in every country ChatGPT supports (1.0.7 was US only).
- Listing text: works with any existing Lezonder account; membership and
  sharing-permission wording removed. Tools, data, sign-in and review cases unchanged.

# 1.0.7

- Candidate only: rename the single MCP configuration key to lezonder-sleep,
  retaining the canonical endpoint, two sleep tools and existing OAuth policy.
- Test whether fresh discovery stops requesting the retired draw permission;
  the outcome is unverified. No scope expansion, new server or new account.
- Update package status. Upload and final submission remain owner-approved steps.

# 1.0.5

- Replace the Directory scope with two sleep tools: latest date/Lezonder Sleep
  Score and dated scores for 1–7 local days. No tickets, reasons, draw or odds.
- Replace the draw review case with a one-day trend; keep exactly five positive
  and three negative cases, one canonical remote server and existing brand assets.
- Explain the source-sharing restriction, the distinct OAuth identity/refresh
  permissions and recipient retention/deletion boundaries in prepared disclosures.
- Bundle a labelled local two-tool rehearsal; clear the old three-tool recording
  URL for replacement after the approved live release. No new live scan is claimed.
- Prepared candidate only. Production/publication, final review recording,
  broader access and submission remain subject to their existing gates.

# 1.0.4

- Describe sleep-score review as the main purpose and use the supported Healthcare category.
- Remove payment-related wording from public descriptions; retain the existing-membership requirement and truthful paid-access/draw disclosures for reviewers.
- Record completed primary MCP authorization and owner-confirmed password-only reviewer sign-in. The three tools, scopes and five positive/three negative cases are unchanged.
- Draft only; final submission and policy attestations remain with the owner.

# 1.0.3

- Replace the local mocked-authentication demo with actual ChatGPT test screenshots against the live MCP server, using invented review examples.
- All five positive and three negative reviewer scenarios passed their live UI checks.
- Refresh package status for the existing owner-selected test account; credentials stay outside the ZIP.
- Publish and verify the owner-approved public walkthrough URL. Fresh-browser login and final submission remain pending their required verification/approval.

# 1.0.2

- Use the documented Productivity category after the portal rejected Lifestyle.
- Simplify the listing description to state existing-member access and read-only behavior without references to subscription upgrades.

# 1.0.1

- Align listing with the approved scope: existing current paying Lezonder members, exactly three read-only tools and no signup or purchase flow.
- Use the owner's verified individual publisher identity, EVGENIY ANTOSHKIN.
- Correct the service-age disclosure and preserve existing draw eligibility rules.
- Keep exactly five positive and three negative review cases, one canonical remote server, and credentials outside the package.
- Draft only: paid-entitlement enforcement, dedicated reviewer access, privacy publication and remaining release checks are pending. Final submission and further production changes require owner approval.

# 1.0.0

- Three strict, authenticated read-only tools with structured JSON and text results.
- Scoped, instance-bound Clerk opaque OAuth verification; exact OpenAI client allowlist and canonical resource audience.
- HTTP discovery and tool-level reauthorization challenges; RFC 9728 metadata.
- Reuse of Muse account ownership, visibility, local-day/month and immutable draw-snapshot behavior, deadline and operational rate limits.
- Private/no-store website routing, dashboard-token domain challenge route, supplemental sharing privacy and support pages.
- Synthetic-only by default: exact reviewer-subject allowlist and verified test flag; real data requires provider clearance and explicit release setting.
- No MCP engagement events. Muse's existing authorization policy remains separate.

Private candidate only. Live refresh/revocation, provider-data permissions and public Directory eligibility remain open gates. No further production deployment or configuration change is authorized by this package.
