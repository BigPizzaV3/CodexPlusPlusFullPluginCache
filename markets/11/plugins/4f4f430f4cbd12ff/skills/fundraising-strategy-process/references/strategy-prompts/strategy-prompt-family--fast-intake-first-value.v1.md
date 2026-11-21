Adapted from the Azimuth Strategy Framework prompt library.

## Host/MCP adaptation

Use the method below with this connection's actual catalog and the user's available conversation and document context. Placeholders, schemas, stored state, job steps, interface actions and revision receipts mentioned in the text belong to the strategy application, not to this connection; do not invent their presence or require their setup. Use the host assistant's native research for current primary sources. Return useful prose unless the user requests a schema. Separate copy-ready strategy from supporting analysis, evidence gaps and provisional candidates, keeping both visible to the user. Preserve accepted decisions and propose bounded changes for user review. Prompts for inactive features supply drafting methods only. Connection boundaries and evidence rules remain authoritative, including no saving on a read-only connection.

# Fast Intake — Initial Strategy Draft

You are creating the first useful version of a fundraising strategy.

The shared strategy context supplied with this prompt is authoritative.

This is an initial draft for feedback. It will improve as information is
curated and validated.

Your job is to turn the supplied intake and available organization context
into:

1. A coherent, copy-ready six-chapter strategy.
2. Three to five useful peer suggestions.
3. Five to ten plausible funder suggestions.
4. A private validation ledger for later research and Consultant View.

The visible strategy is the best current strategic answer—not a research
report, diagnostic memo, or list of caveats.

## Inputs

### Owner intake

{{OWNER_INTAKE}}

### Resolved organization

{{ORGANIZATION_IDENTITY}}

### Available organization context

{{ORGANIZATION_CONTEXT}}

The context may contain website and mission information, programs,
populations, geography, IRS and financial information, known funding
relationships, graph relationships, owner-provided sources, and peer or funder
seeds.

Use the context that is present. Missing context must not prevent a useful
initial draft.

## Depth and length

Produce a substantive working document, not six short answers written to
satisfy a schema.

Target approximately 1,450–2,100 words:

- Define Ask: 150–225 words.
- Org Frame: 225–325 words.
- Peer Benchmarking: 250–350 words.
- Evidence Base: 225–325 words.
- Case Design: 300–450 words.
- Opportunities: 300–450 words.

Each chapter should normally contain two to four developed paragraphs. Case
Design and Opportunities may use more.

Every paragraph must advance the strategy. Do not pad the document by
repeating the mission, intake, disclaimer, or earlier conclusions.

When context is thin, use sound strategic reasoning to develop the strongest
plausible direction. Do not replace substance with caveats, disclaimers, or
statements that more information is needed.

## Progressive chapter contract

The chapters form one argument, not six independent responses.

1. Define Ask establishes the initial fundraising objective and strategic
   direction.
2. Org Frame explains why this organization is positioned to pursue that
   objective.
3. Peer Benchmarking selects peers based on the objective, organizational
   role, operating model, and geography established in Chapters 1 and 2.
4. Evidence Base interprets the available organization and peer evidence in
   support of the emerging strategy.
5. Case Design turns Chapters 1–4 into a persuasive argument for support.
6. Opportunities selects funding routes and plausible funders based on the
   case, intended uses, peer patterns, geography, and known relationships
   established in Chapters 1–5.

Do not introduce a major new strategy in a later chapter that contradicts or
ignores the earlier chapters.

## Internal working process

Complete these stages in order.

### 1. Establish the position

Determine:

- What the organization does.
- Whom and where it serves.
- What it appears to be trying to fund.
- The most useful initial fundraising direction.
- The organizational distinction that can anchor its case.

If the owner has not supplied a precise fundraising target, choose a reasonable
starting direction. Do not replace the strategy with a request for more
information.

Use this conclusion as the foundation for every later stage.

### 2. Identify useful peers

Suggest three to five organizations that help the owner think about
positioning, fundraising posture, or organizational strategy.

Use a useful mix of:

- Direct operating-model peers.
- Adjacent organizations with a relevant role or funding model.
- Contextual reference organizations.

Peers do not need to be perfect matches. Select organizations that create
useful comparisons and briefly explain why each belongs.

For each peer, determine:

- Its comparison role.
- The aspect of the focal organization it helps illuminate.
- The strategic or funding lane it may help identify.
- Any funders or funding patterns connected to that peer in the supplied
  context.

Preserve this peer-to-funder information for the funder stage. Do not wait
until after producing the funder list to compare it with the peers.

### 3. Build the evidence reading

Interpret the strongest available facts about the organization and peers.

Use the evidence to clarify:

- The organization’s starting position.
- The opportunity or constraint the strategy addresses.
- Relevant patterns visible across peers.
- The funding routes that appear most credible.
- The uses of funding the organization can most persuasively advance.

Do not turn this chapter into a source inventory or limitations memo.

### 4. Build the case

Use the fundraising objective, organization frame, peer perspective, and
evidence reading to develop a simple, persuasive case.

The case should answer:

- What matters?
- Why is this organization positioned to act?
- What does funding make possible?
- Why is this a credible direction?
- Which aspects of the case are most likely to connect with institutional
  funders?

Make the strongest reasonable strategic interpretation of the available
information. Do not invent numerical outcomes, deadlines, grants, or owner
commitments.

### 5. Build the funder map from the strategy

Identify five to ten plausible funders or funding institutions.

Search conceptually in this order:

1. Known current or previous funders of the focal organization.
2. Funders connected to the selected peers in the supplied context.
3. Funders associated with the same program, population, geography, or
   strategic lane.
4. Additional model-suggested funders that plausibly fit the completed case.

For every funder, determine how it entered the list:

- existing_relationship
- peer_funder_pattern
- strategy_fit

When the context documents that a funder supports a selected peer, preserve
that connection.

When a funder merely fits the same strategic lane as a peer, describe it as a
shared strategy fit. Do not falsely claim that the funder supports the peer.

Known current funders must be identified as existing or stewardship
relationships, not presented as new cold prospects.

A suggested funder may be included without verified current eligibility or an
open program. Record that validation need privately rather than turning it
into visible caveat prose.

The funder list must follow from the completed case. Do not produce a generic
list that could apply to any nonprofit in the same city.

### 6. Edit the complete artifact

Read the entire draft as one document.

Confirm that:

- Each chapter builds on the preceding chapters.
- The peer set follows from the ask and organization frame.
- The evidence reading uses the peer context rather than merely listing facts.
- The case follows from the peer and evidence reading.
- The funder list follows from the case and peer patterns.
- The recommendations are consistent.
- The strategy is specific to this organization.
- The prose is direct and ready to copy into another document.
- Internal uncertainty and validation work stay outside the strategy.

## Visible strategy requirements

Write in direct organizational language.

Prefer formulations such as:

- “Our strategy centers on…”
- “The organization’s strongest fundraising position is…”
- “This strategy connects…”
- “The initial peer set includes…”
- “The leading funding opportunities are…”

Do not write:

- “The organization should…”
- “We recommend that…”
- “The evidence is not enough to claim…”
- “Peer evidence does not determine…”
- “More research is required before proceeding.”
- Internal status or confidence labels.
- A research plan, readiness assessment, or Consultant View analysis.

Do not invent:

- Financial figures.
- Relationships.
- Eligibility.
- Open grant programs.
- Deadlines.
- Warm access.
- Owner decisions.
- Outcomes or commitments not supported by the intake.

When evidence is limited, make a reasonable strategic recommendation and
record the limitation in the private ledger.

## Required structured output

Return exactly this structure:

{
"artifact": {
"disclaimer": "This is an initial draft for feedback. It will improve as information is curated and validated.",
"chapters": [
{
"chapterNumber": 1,
"title": "Define Ask",
"prose": "150–225 words of copy-ready strategy prose."
},
{
"chapterNumber": 2,
"title": "Org Frame",
"prose": "225–325 words that build on Chapter 1."
},
{
"chapterNumber": 3,
"title": "Peer Benchmarking",
"prose": "250–350 words connecting the peer set to Chapters 1 and 2."
},
{
"chapterNumber": 4,
"title": "Evidence Base",
"prose": "225–325 words interpreting organization and peer evidence."
},
{
"chapterNumber": 5,
"title": "Case Design",
"prose": "300–450 words building the case from Chapters 1–4."
},
{
"chapterNumber": 6,
"title": "Opportunities",
"prose": "300–450 words connecting funding routes to the case and peer patterns."
}
]
},
"peerSuggestions": [
{
"organizationName": "Organization name",
"comparisonRole": "direct_peer | adjacent_peer | contextual_reference",
"whyRelevant": "A concise, organization-specific explanation.",
"strategicLane": "The strategy or funding lane this peer helps illuminate.",
"basis": "context_backed | model_suggested"
}
],
"funderSuggestions": [
{
"funderName": "Funder name",
"relationshipType": "existing_relationship | plausible_prospect",
"discoveryPath": "existing_relationship | peer_funder_pattern | strategy_fit",
"whyFit": "A concise explanation connecting this funder to the completed strategy.",
"likelyUse": "The program, capacity, operating, or strategic use that appears most relevant.",
"peerConnections": [
{
"peerName": "Selected peer name",
"connectionType": "documented_funder_of_peer | shared_strategy_fit",
"basis": "context_backed | model_suggested"
}
],
"basis": "context_backed | model_suggested"
}
],
"privateValidationLedger": [
{
"subjectType": "strategy_claim | peer | funder | peer_funder_connection",
"subjectName": "Claim or organization",
"confidence": "high | medium | low",
"validationStatus": "supported | plausible | needs_validation",
"reason": "Why this status applies.",
"recommendedCheck": "The next bounded research or owner-validation action."
}
]
}

## Final checks

Before returning:

- Confirm the complete strategy is approximately 1,450–2,100 words.
- Confirm all six chapters contain developed, substantive prose.
- Confirm each chapter uses conclusions established by preceding chapters.
- Confirm there are three to five peer suggestions.
- Confirm there are five to ten funder suggestions.
- Confirm funders were derived from existing relationships, peer patterns, or
  the completed strategic case.
- Confirm every claimed peer-funder relationship is supported by context;
  otherwise use shared_strategy_fit.
- Confirm the funder list is not a generic post hoc list.
- Confirm the strategy contains no internal labels or consultant scaffolding.
- Confirm the visible artifact does not expose the private validation ledger.
- Confirm incomplete evidence did not erase the strongest reasonable
  recommendation.
- Confirm replacing the organization’s name with another organization would
  make the strategy incorrect.
