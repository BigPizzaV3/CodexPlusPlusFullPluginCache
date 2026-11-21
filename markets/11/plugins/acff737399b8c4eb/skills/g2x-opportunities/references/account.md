# Account, usage and settings

Keep three different profiles apart:

- The claimed company profile is the company's public page in the GovCon Directory. Calibration reads it. Its owner can edit six public fields.
- A G2X AI profile is private context for Lumen and Bid Hub (Settings, then AI profiles, in G2X). A user can keep several, such as one per legal entity or market. It is not the public company page.
- Registered SAM.gov data (legal name, CAGE code, address) is edited at SAM.gov, never here.

### `g2x_calibrate_session`

Call once at the start of a session, before searching. It matches the session to the user's company so searches fit them.

- Inputs: `uei` (only when the account claimed several companies: the UEI of the one to use; omit to use the first); `list_profiles` (true lists every claimed profile without calibrating; then call again with the UEI to use).
- Output: with a profile, the company name, UEI, CAGE and location, primary NAICS, business types and SBA certifications, the agencies that award it the most, its G2X profile link, and the filters to pass on every search, including a one-query override. It says when the profile UEI is not in SAM registration data. With no profile, it lists the questions to ask and links the page where the user claims their company. It reads only the user's own claimed profiles and changes nothing.
- Plan: all plans. Read only. On the research endpoint: yes.
- Example: `{}` and, with several profiles, `{"list_profiles": true}` then `{"uei": "<UEI from the list>"}`

Confirm the profile in one sentence before searching: "I'll look for work that fits {company}: NAICS {codes}, agencies {agencies}, {certifications}. Anything to change for today?" With no profile, ask for the UEI or company name, main NAICS codes, target agencies, set-asides or certifications, places of performance and kinds of work, and share the claim link so the next session calibrates by itself.

### `g2x_usage`

Check how much G2X usage the account has used. Use it when the user asks what remains; never guess a balance from call counts.

- Inputs: none: `{}`.
- Output: how much of the Lumen usage is used this session and this week, as a percent and state, and when each resets, plus pool and extra usage where they apply. Lumen and this connection share the same allowance. Report the scope, period and remaining amount or percent as returned. A missing balance is unknown, not zero.
- Plan: all plans, when the connection offers the usage read. Read only. Checking usage does not spend the daily allowance. On the research endpoint: yes, when offered.
- Example: `{}`

If this tool is not in the connected tool list, say that this connection cannot check usage yet and point to the usage screen in the account. Do not invent a tool or a balance.

### `g2x_list_ai_profiles`

List the user's G2X AI profiles. Use it whenever the user mentions their AI profile, or asks to review, compare or pick one.

- Inputs: none: `{}`.
- Output: each profile's id, name, company, UEI and CAGE when linked, bidding name when set, whether it is the default, whether it is shared with the team, which of the five Bid/No-Bid readiness sections are complete and which are missing, and its page in G2X.
- Plan: when the connection offers it. Read only. On the research endpoint: no.
- Example: `{}`

### `g2x_get_ai_profile`

Read one G2X AI profile in full. Read it before suggesting or making changes.

- Inputs: `profile_id` (required, from the profile list).
- Output: every field the update tool can change, by the same names, which fields are empty, Bid/No-Bid readiness, and whether the user can edit it. Company, CAGE code, readiness, default, shared and access are read only here. Another account's profile, or one the user cannot see, is not found.
- Plan: when the connection offers it. Read only. On the research endpoint: no.
- Example: `{"profile_id": "<id from the profile list>"}`

### `g2x_create_ai_profile`

Create a new G2X AI profile, for example one per legal entity or market. Each call creates a new profile and nothing deduplicates by name, so list profiles first. It never changes which profile is the default, except that a user's first own-company profile becomes their default.

- Inputs: `name` (required, as Settings shows it); any profile fields, such as `relationship`, `uei`, `bidding_name`, `naics_codes`, `psc_codes`, `agency_codes`, `geographic_focus`, `interest_tags`, `target_contract_value`, `facility_clearance`, `capabilities`, `certifications`, `past_performance_themes`, `teaming_notes`, `response_depth`, `citation_style` and `tone`. `bidding_name` sets the name to bid under, such as a DBA. Read an existing profile to see every field name.
- Output: the new profile with its id and page in G2X.
- Plan: when the connection offers it. Write. On the research endpoint: no.
- Example: `{"name": "Health IT", "relationship": "own", "naics_codes": ["541512"], "agency_codes": ["VA"]}`

Confirm the fields with the user before creating. Do not invent capabilities, certifications or past performance.

### `g2x_update_ai_profile`

Change the named fields of one G2X AI profile. Fields not named keep their values. A list replaces the whole list. Null clears a field.

- Inputs: `profile_id` (required); `name`; any profile fields by the names the read tool returns; `message` (a short note shown to the profile's owner when the change needs their review). `bidding_name` sets or clears the name to bid under; without one, the registered legal name is used.
- Output: the saved profile. An owner's change applies at once. An editor's change waits for an owner's review in G2X; say it is pending, not applied. A profile the user can only view is refused.
- Plan: when the connection offers it. Write. On the research endpoint: no.
- Example: `{"profile_id": "<profile id>", "certifications": "ISO 27001; SDVOSB"}`

Read the profile back after an update and report what changed.

### `g2x_list_my_company_profiles`

List the claimed company profiles on the user's account: the public GovCon Directory pages this account owns.

- Inputs: none: `{}`.
- Output: each company's UEI and name, its public page, the current value of each owner-editable field (`description`, `employee_count`, `website`, `careers_url`, `jobs_publication_opt_out`, `dba_name`), which are empty, and whether the account's plan lets the owner edit them. With none, it points to the Directory page where the owner claims the profile.
- Plan: when the connection offers it. Read only. On the research endpoint: no.
- Example: `{}`

### `g2x_update_my_company_profile`

Change the named owner-editable fields of a claimed company profile this account owns. Fields not named keep their values. Null clears a field other than `description`. The change shows on the company's public Directory page. A profile another account claimed, or one nobody has claimed, is refused.

- Inputs: `uei` (required, from the claimed profiles list); `description`, `employee_count` (`0-10`, `11-50`, `51-100`, `101-300`, `300+`), `website`, `careers_url`, `jobs_publication_opt_out` (true hides web-found job openings from public job browsing; jobs posted by the company stay visible), `dba_name` (the name G2X shows; empty restores the SAM.gov registration name). Name at least one field to change.
- Output: the saved profile. If G2X saved the change but could not read it back, it says so; check the Directory page before changing it again.
- Plan: Starter and up for editing, when the connection offers it. Write. On the research endpoint: no.
- Example: `{"uei": "<UEI from the list>", "website": "https://www.example.com"}`

Confirm public-facing text with the user before saving. This tool never edits SAM.gov registration fields.
