# Floyd by The F Suite — OpenAI review test cases

Five positive and three negative cases, per the OpenAI submission requirements. Each positive case
must be run end to end against the reviewer test account before submission.

Reviewer credentials go in the **dashboard**, never in the ZIP.

## Test account

| | |
|---|---|
| Login URL | https://braintrust.fsuite.co/ |
| Account | `test-floyd-mcp@fsuite.co` |
| Password | (entered in the dashboard, not here) |
| MFA | None — must remain off for review |
| Setup | Active F Suite membership on a non-guest CFO peer network, full access, not suspended |

## Positive cases

### P1 — Stage benchmark with a spread

- **Scenario:** A CFO wants to know whether their burn is in line with comparable companies.
- **Prompt:** `What's a normal burn multiple for a Series B SaaS company according to my peers?`
- **Expected tool:** `get_peer_insights`
- **Expected result:** A range of burn-multiple figures reported by F Suite members at Series B,
  with the cohort named, attributed to The F Suite CFO community, and inline citations resolving to
  F Suite discussion threads.

### P2 — Shortlist firms for a finance need

- **Scenario:** A finance lead at a venture-backed company needs to pick an audit firm.
- **Prompt:** `Which audit firms work well with venture-backed companies?`
- **Expected tool:** `find_vendors`
- **Expected result:** Named audit firms ordered by community discussion volume, separated from
  software vendors, with a synthesis of what practitioners reported and citations to the threads.

### P3 — Diligence on two named providers

- **Scenario:** A CFO is choosing between two spend-management platforms peers already use.
- **Prompt:** `What do CFOs say about Ramp vs Brex for spend management?`
- **Expected tool:** `find_vendors`
- **Expected result:** Peer commentary on both named providers with discussion counts and
  citations, presented as practitioner signal rather than a recommendation.

### P4 — Process and deliverable design

- **Scenario:** A newly hired CFO is building their first board reporting package.
- **Prompt:** `How do other CFOs structure their board reporting package?`
- **Expected tool:** `get_peer_insights`
- **Expected result:** Peer approaches to board package structure — sections, metrics, cadence —
  drawn from community threads and shared templates, with citations.

### P5 — Judgment under pressure

- **Scenario:** A finance team has tripped a debt covenant and wants to know how peers handled it.
- **Prompt:** `We had a covenant breach — how do peers usually handle the lender conversation?`
- **Expected tool:** `get_peer_insights`
- **Expected result:** Peer accounts of covenant breach handling — lender conversation, waiver,
  remediation — attributed to the community, with citations. Where signal is thin, the answer says
  so rather than inventing accounts.

## Negative cases

### N1 — Arithmetic on the user's own numbers

- **Prompt:** `Our revenue is $4.2M ARR and we burn $900K a month. What's our runway?`
- **Expected:** No tool call. This is computation on figures the user supplied; community
  intelligence adds nothing.

### N2 — Settled rule lookup

- **Prompt:** `What does ASC 606 say about the five-step revenue recognition model?`
- **Expected:** No tool call. A published accounting standard is a factual lookup with no
  "what's normal" dimension.

### N3 — Out of domain

- **Prompt:** `Write me a Python script to parse a CSV of invoices.`
- **Expected:** No tool call. Technical task outside the connector's scope.

## Out-of-scope access check

Not one of the eight required cases, but worth demonstrating in the walkthrough video: a request
for another community's content (for example `Show me what L Suite GCs are saying about outside
counsel rates`) should be answered by explaining that access is scoped to the member's own peer
networks — without claiming cross-network reach or surfacing out-of-scope identifiers.

## Video walkthrough

One recording covering P1 through P5 plus at least one negative case, at a URL reachable without
sign-in. Set in `extensions.com.openai.review.demo_recording_url` or entered in the dashboard.
