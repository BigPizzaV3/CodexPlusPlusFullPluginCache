# Card Types Reference

Story cards (tier 3) in Cartographer have a `type` field that communicates the card's purpose at a glance. Choosing the right type makes the board scannable and helps teams prioritize.

## Type Details

### `none` — Generic Story Card

The default type. Use for standard user stories, tasks, or work items that don't fit a more specific type.

**Examples:**

- "Display search results with pagination"
- "Send welcome email after signup"
- "Add dark mode toggle to settings"

**When to use:** When the card describes a feature, task, or user story without a specific analytical angle.

### `objective` — Goal or Outcome

Represents a desired outcome, success metric, or goal the team wants to achieve within a step.

**Examples:**

- "User can complete checkout in under 60 seconds"
- "Reduce support tickets by 30% for this flow"
- "All critical paths have error recovery"

**When to use:** To anchor a step around what success looks like. Objectives help teams stay outcome-focused rather than output-focused. Place objectives near the top of a step to frame the work below.

### `risk` — Threat or Concern

Captures something that could go wrong, a technical constraint, a regulatory issue, or any source of uncertainty that threatens success.

**Examples:**

- "Payment provider API may have downtime during peak"
- "GDPR requires explicit consent before data processing"
- "Legacy system has no documented API"
- "User drop-off likely high at this step"

**When to use:** Whenever you identify something that could block or degrade the user experience. Surface risks early — they often become the most important items to address first.

### `question` — Open Question

An explicit question the team needs to answer before proceeding. Questions acknowledge what's unknown and prevent assumptions from silently entering the design.

**Examples:**

- "Do users need to invite teammates during onboarding or after?"
- "Should we support offline mode in v1?"
- "What happens if the user has multiple organizations?"

**When to use:** When there's a decision to be made or information to gather. Convert questions to `learn` cards once they're answered.

### `knowledge_gap` — Something to Learn

Identifies an area where the team lacks knowledge needed to make good decisions. More structural than a question — it points to a domain or topic requiring research.

**Examples:**

- "How do competitors handle bulk import?"
- "What are the accessibility requirements for drag-and-drop?"
- "Need to understand payment provider webhook reliability"

**When to use:** When the gap is about a domain or topic rather than a specific yes/no decision. Knowledge gaps often trigger research spikes or user interviews.

### `learn` — Insight or Learning

Captures validated knowledge — something the team has learned from research, user testing, analytics, or experience. Learnings are the resolved form of questions and knowledge gaps.

**Examples:**

- "Users prefer email notifications over in-app (validated in 12 interviews)"
- "Average session length is 4 minutes — flows must be completable in that window"
- "Competitor X requires 7 steps for this task — we can do it in 3"

**When to use:** To record insights that should inform design decisions. Learnings are especially valuable when imported from research. They provide evidence for why certain story cards exist.

### `pain_point` — User Frustration

A problem, frustration, or workaround users experience today at this step. Pain points describe the current reality, not the solution.

**Examples:**

- "Admins rebuild the weekly report by hand every Monday"
- "Users lose their draft when the session times out"
- "Finance can't get numbers out without asking an engineer"

**When to use:** When mapping research, support tickets, customer feedback, or a prospect's current workflow. Put the evidence (a quote, how many users mentioned it) in the description. Pain points are often the best input for deciding what goes in the next release.

### `opportunity` — Potential Value

A chance to create value that the team hasn't committed to building. Opportunities sit between a pain point and a story: they describe the need or the value, not yet the solution.

**Examples:**

- "Send the weekly report to finance automatically"
- "Pre-fill the form from last month's order"
- "Offer a template gallery on the empty dashboard"

**When to use:** For customer needs, feature requests reframed as needs, and ideas worth exploring. Promote an opportunity to a `none` story card once the team decides to build it.

## Type Distribution Guidelines

A well-balanced step typically has a mix of types:

- **1-2 objectives** framing what success looks like
- **Several `none` cards** describing the work
- **1-3 risks or questions** surfacing uncertainty
- **Learnings** grounding decisions in evidence
- **Pain points and opportunities** when the map is built from research or customer feedback

A step with only `none`-typed cards suggests the team hasn't yet thought critically about the user experience at that point. Prompt for risks, questions, and objectives.

## Type Transitions

Cards can change type as work progresses:

- `question` → `learn` (when answered through research)
- `knowledge_gap` → `learn` (when the team has learned what they needed)
- `risk` → `none` (when the risk is mitigated and becomes a standard task)
- `none` → `objective` (when a task is reframed as an outcome)
- `pain_point` → `opportunity` (when the team frames a need worth addressing)
- `opportunity` → `none` (when the team commits to building it)
