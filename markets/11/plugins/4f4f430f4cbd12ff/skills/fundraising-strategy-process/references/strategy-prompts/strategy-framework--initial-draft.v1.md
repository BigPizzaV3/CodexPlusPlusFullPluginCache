Adapted from the Azimuth Strategy Framework prompt library.

## Host/MCP adaptation

Use the method below with this connection's actual catalog and the user's available conversation and document context. Placeholders, schemas, stored state, job steps, interface actions and revision receipts mentioned in the text belong to the strategy application, not to this connection; do not invent their presence or require their setup. Use the host assistant's native research for current primary sources. Return useful prose unless the user requests a schema. Separate copy-ready strategy from supporting analysis, evidence gaps and provisional candidates, keeping both visible to the user. Preserve accepted decisions and propose bounded changes for user review. Prompts for inactive features supply drafting methods only. Connection boundaries and evidence rules remain authoritative, including no saving on a read-only connection.

# Intake-draft construction

Create a useful, complete-shaped `intake_draft` from the approved entry brief,
verified focal identity, user statements, and framework methodology. If the
intended decision or organization/program/project scope is still materially
ambiguous, return the permitted focused question instead of guessing.

Before writing, inspect the current revision, accepted decisions, protected
sections, and open gaps. Prefer durable accepted strategy state, owned or
private engagement sources, warehouse evidence, and graph receipts already in
context before asking the user for facts that can be retrieved. Ask only for
private facts, judgment calls, relationship access, material decisions, or
unresolved contradictions. If a compatible intake draft already exists, patch
only materially affected sections or return `no_change`; do not regenerate it.

The document must contain the strategy itself in the organization's voice: its
honest current or starting position, why that direction fits, and which funding
routes lead, follow, or remain separate. Write copy-ready organizational
strategy primarily in present tense. Future-tense commitments may appear only
when they closely preserve an explicit owner-stated or already durably accepted
commitment. Never convert an aspiration, inference, or recommendation into
“will,” including owner language such as “we hope to,” “we are considering,” or
“we want to.” Do not write
“we recommend,” “the organization should position,” “based on what we know,”
claim-kind labels, confidence labels, receipt language, or questions to the
user. Those belong in consultant analysis, readiness metadata, evidence needs,
the tool rail, or `first_actions` — never as a replacement for chapter prose.
Sparse context still requires a present strategic judgment.

Produce distinct work for the eight intake sections:

1. `executive_recommendation` (projects to Chapter 1): one provisional
   direction that ends with an explicit direct-voice conclusion, why it is useful now,
   the lead funding route, and the decision it is meant to support. Do not leave
   this section as an unranked menu, identity summary, or research request;
2. `define_ask` (projects to Org Frame / `current_organizational_position`):
   establish the fundraising-relevant organizational frame and end with an
   explicit positioning conclusion. Answer what kind of organization this is
   for fundraising purposes; which capabilities, program model, geography, or
   constituency define its credible position; what leads its fundraising
   posture; and which interpretation does not lead because the evidence does
   not support it. Facts, mission summaries, NTEE labels, and program lists are
   insufficient without that resulting strategic frame. Do not turn this
   section into a research request or action plan. Use the direct sentence
   frame “Our fundraising position is … . … leads our fundraising posture;
   … does not lead it”;
3. `strategic_angle`: a working case hypothesis and the organization role that
   still needs validation;
4. `use_of_funds`: provisional workstreams or cost categories, with unknown
   budget, timing, or implementation details marked as gaps that condition the
   case rather than erase it;
5. `funding_routes`: two or three meaningfully different route hypotheses with
   explicit lead / follow / separate roles, including separation of
   philanthropy from project-linked support and structured capital when
   relevant;
6. `peer_benchmark`: a comparative conclusion that ends in an explicit direct-voice
   decision about how peers affect the strategy. Benchmark facts,
   bands, rankings, and caveats alone are insufficient. With useful peer
   evidence, state which peer posture or band guides the strategy and
   why (for example: treat the pure-developer band as the credibility floor,
   adopt a staged platform between bands as the current choice, and keep a
   higher services-band stretch conditional on readiness). With insufficient
   evidence, explicitly state that peers should not determine the target and
   define their limited strategic use (posture or role choice only). Keep role
   bands explicit and do not blend unlike organizations into one median. Do
   not replace this section with a research assignment, benchmark plan, or
   action plan;
7. `evidence_gaps`: material gaps, each tied to the decision it could change,
   plus direct-voice conclusion prose stating “Our current evidence is enough
   to choose …” and “It is not enough to claim …”; and
8. `first_actions`: prioritized actions for the next 90 days, separating
   decisions, retrieval, readiness work, and relationship work. These actions
   support the margin and tooling; they are not chapter substitutes.

Every section that projects into the six-chapter document must include at least
one conclusion or recommendation. Missing evidence may limit a target, keep a
claim provisional, prevent a peer-derived conclusion, make one route
conditional, or identify the next material owner decision. It must not cause a
chapter to become “research this later.”

Use claim kinds explicitly. Verified organization identity (name and EIN) is
`fact`. Owner-provided goals and judgments are `user_stated`. Use `inference`,
`recommendation`, and `gap` for derived conclusions, choices, and missing
material. Do not add named peers, prospects, funders, relationships, award
amounts, outcomes, or access paths merely to make the draft look complete.
Treat filing contributions with discipline: report total contributions,
government grants, and private non-government support distinctly when supplied;
never overload total contributions with private support alone. Exclude
related-organization transfers and one-time campaign spikes when the supplied
evidence marks them.

Make a recommendation rather than presenting an unranked menu. Explain what
would confirm or change it in analysis fields, not as a substitute for chapter
prose. Keep later-stage requirements visible as next-level blockers, not
current-stage accomplishments. Write chapter prose as copy-paste-ready
organizational language. Return only the caller's closed structured output.
