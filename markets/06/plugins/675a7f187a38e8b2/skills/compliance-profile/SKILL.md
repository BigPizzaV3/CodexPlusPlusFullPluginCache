---
name: compliance-profile
description: Build or update the compliance profile that scopes every horizon scan — the business's legal entities, operating jurisdictions, sector, headcount, data and AI exposure, supply chain, and materiality thresholds. Use when the user is setting up for the first time, has no profile yet, or needs to change one after a business change such as a new jurisdiction, product line, or headcount shift. Emits a portable YAML block the user saves and supplies to later scans.
---

Read `../../references/runtime-safety.md` before using this workflow. Resolve relative paths from this skill directory. To use a sibling skill, read its `../<skill-name>/SKILL.md`; no special invocation tool is required.


The profile is the plugin's only memory. It scopes the scan to one business and carries the scan
state that makes later runs incremental. Getting it right is what separates a relevant scan from a
generic one.

Read `../../references/profile-schema.md` for the full field reference and vocabulary.

---

## 1. Establish whether this is new or an update

Ask for an existing profile block first. If there is one, go to §5.

## 2. Interview — ask only what you cannot infer

Work through the schema, but do not read it out as a form. Ask in the order below, group related
questions, and infer what you reasonably can from what the user has already said — then state your
inference so they can correct it.

**Identity and footprint** (needed)
- Legal entities and where each is incorporated
- Where the business actually operates — use the `operating_jurisdictions` vocabulary
- For US coverage, offer federal-only (default) or federal plus selected states. Ask which
  states matter, accept names or postal codes, and save them in `coverage.us_states` using
  the schema. Explain state research is bounded by reachable official sources. Ask only
  if the preference is not already clear; never enable every state automatically.
- Sector, in the user's own words; add NAICS/SIC if they know them
- Headcount per jurisdiction, roughly
- Public company? If so, listing venues
- Revenue band, roughly

**Exposure** (this is what makes the scan specific — worth the time)
- What personal data: customer, employee, health, biometric, children, financial, location
- AI anywhere: in the product, in hiring, in credit decisions, internal only
- Consumer-facing? Payments?
- Regulated products
- Export-controlled items; any touchpoints with sanctioned jurisdictions
- Physical sites, and how far the supply chain is mapped
- Unionised workforce

**Thresholds**
- Report at `medium` and above (default), or a different cut
- Anything to always surface regardless of score — default is criminal liability, personal
  liability for directors and officers, and licence conditions

### How to ask well

**Don't ask what you can infer, but do confirm it.** If they say "we're a UK SaaS business selling
to consumers in Europe," set `consumer_facing: true`, `sector` to software, and propose `UK` and
`EU` — then say what you assumed and let them correct it.

**Headcount matters more than it looks.** Several employment and reporting obligations turn on
thresholds, so an approximate number per jurisdiction is worth pressing for gently. "Roughly how
many people in the UK — under 50, under 250, or more?" gets there without an interrogation.

**Push a little on the exposure flags, and only there.** These are where a wrong value produces
confidently irrelevant results. `biometric` and `children` in particular pull in materially
different regimes, and users often don't volunteer them — face unlock, age-gated sign-up, or a
photo feature all count. Ask directly.

**Don't guess an exposure flag to be safe.** Setting `biometric: true` on a hunch floods every
later scan with irrelevant high-impact findings and trains the user to ignore the output. If you
don't know, ask; if the user doesn't know, record it as unknown and say the next scan may miss or
over-report in that area.

## 3. Set the scan-state fields

- `last_scan_date` → **90 days before today**, and say so
- `reported_ledger` → empty
- `profile_version: 1`, and a `profile_name` the user will recognise

## 4. Emit the block and explain what to do with it

Output the complete YAML block, then, in two or three sentences:

- **Save it** — in a project file or notes. Supply it at the start of each scan.
- **Each scan returns an updated block. Save that one too.** This is how "what's new since last
  time" works; skip it and every scan re-reports the same items.
- Echo selected states (or “state coverage off”). Name unselected profile states, local law,
  and EU member-state implementation as exclusions. Use the pending baseline rules when
  adding or removing states; preserve the existing global scan date and ledger.

Then offer to run the first scan, noting it will be a 90-day baseline rather than a delta.

## 5. Updating an existing profile

Accept a partial change without re-interviewing. Keep `last_scan_date` and `reported_ledger`
exactly as they are — an update is not a reset, and clearing the ledger would re-report everything.

Change only what the user asked for, then re-emit the whole block so they have one current artifact
to save.

For scope-expanding changes, also create `coverage.pending_scope_baselines` entries under the
schema rules. Explain that the next scan checks earlier developments and standing obligations
relevant to the change, not only publications since the last scan. Preserve pending work and all
saved rule snapshots. Do not promise coverage of unsupported countries or silently select states.

**Say when a change alters what will be in scope.** Adding `biometric` to `personal_data`, crossing
a headcount threshold, or adding a jurisdiction changes what the next scan surfaces, and the user
should hear that from you rather than be surprised by a scan that suddenly looks different:

> Added `biometric`. That engages special-category data rules and, with `in_product` AI, high-risk
> AI classification — your next scan will likely surface materially more in `privacy_ai`.

**Never silently correct a field the user set.** If something looks wrong — headcount inconsistent
with revenue band, a jurisdiction with no entity or staff — raise it as a question. The profile is
their artifact and counsel may have set a value deliberately.
