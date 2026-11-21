---
name: intakra-workspace-setup
description: "Set an Intakra offering, add explicitly chosen company domains, or request and review account suggestions for the user’s workspace."
---

# Set up an account watch list

Use https://intakra.com/mcp through normal workspace OAuth. Reads need `accounts:read`; `add_accounts` and `request_accounts` need `accounts:write`, and `set_offering` needs `offering:write` plus the appropriate workspace role. Missing permissions use the normal consent flow. An existing base-only client registration may require reconnecting with the requested supported scopes. Documentation: https://intakra.com/mcp-guide.

Read `list_accounts` to recognize existing companies and avoid guessing that a workspace is empty. Collect the user’s actual offering and intended companies. `set_offering` replaces the saved description: use the exact agreed wording. `add_accounts` takes company website domains, skips existing entries and respects plan limits; it schedules public-record checking for a later daily pass, not an immediate completed result. A user instruction specifying these changes is authorization; clarify only missing or conflicting choices.

For discovery, `request_accounts` accepts the desired business description and supported industry, country, region, employee range or up to five lookalike customer domains. Run it only when the user requests or agrees to that background account-finding work. Retain the user’s criteria, respect rate limits and report that suggestions arrive later. Use `list_suggestions` to review actual returned candidates and reasons.

The discovery tools do not accept an exact-count target, so do not promise exactly 100 or invent unsupported filters. Reading a suggestion does not approve its record. There is no suggestion-state approval tool in this connection: use the app for that action. If the user authorizes adding particular returned domains, or selection under concrete agreed criteria, add those actual domains through add_accounts and report the resulting account changes; do not describe that as approving the suggestion records. Clarify missing selection criteria and respect the returned plan limits. After an uncertain write, inspect current accounts or returned state before resubmitting. Never replace the offering, populate guessed companies, bypass role limits or send outreach to make an empty result look successful.
