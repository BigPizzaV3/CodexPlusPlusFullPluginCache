# Board Patterns Reference

Common patterns for structuring Cartographer boards across different use cases.

## Pattern 1: New Product Story Map

For mapping a new product or major feature from scratch.

**Structure:**

- 4-6 journeys covering the end-to-end user experience
- 2-4 steps per journey breaking down each activity
- Mix of card types: objectives at the top of each step, stories in the middle, risks and questions at the bottom
- 2-3 milestones: "MVP", "V1.1", "Future"

**Process:**

1. Start by identifying the user persona
2. Walk through their experience left to right: what do they do first, second, third?
3. Each major activity becomes a journey
4. Break each journey into the steps the user takes
5. Under each step, add story cards for what needs to be built
6. Surface risks, questions, and knowledge gaps as you go
7. Draw milestone lines to separate releases

## Pattern 2: Feature Discovery Board

For exploring a specific feature or epic before committing to build it.

**Structure:**

- 3-4 journeys representing different user paths or scenarios
- 2-3 steps per journey
- Heavy use of `question`, `knowledge_gap`, and `risk` card types
- Objectives framing desired outcomes per step
- May not need milestones initially

**Process:**

1. Frame the feature as a user activity
2. Identify the different ways users might approach it
3. Each approach or scenario becomes a journey
4. Map out what happens at each step
5. Focus on surfacing unknowns: what questions need answering? What don't we know?
6. Add learnings as research results come in

## Pattern 3: Research Synthesis Board

For organizing insights from user research into actionable themes.

**Structure:**

- Journeys represent themes or user goals discovered in research
- Steps represent sub-themes or moments in the user's experience
- Story cards are primarily `learn` type (validated insights)
- `question` cards for follow-up research needs
- `risk` cards for concerns raised by the research
- Milestones might represent research phases or priority tiers

**Process:**

1. Parse research notes, transcripts, or summaries
2. Extract individual insights and categorize them
3. Group insights into themes (journeys)
4. Organize within themes into sub-themes (steps)
5. Create `learn` cards for each validated insight
6. Add `question` cards for things that need more investigation
7. Surface `risk` cards for concerns discovered in research

## Pattern 4: Release Planning Board

For an existing product planning its next releases.

**Structure:**

- Journeys represent the major user flows that are changing
- Steps represent the phases within each flow
- Story cards are primarily `none` type (actionable stories)
- Milestones represent releases or sprints
- Statuses track progress

**Process:**

1. Read the existing board state first
2. Identify which journeys and steps are affected
3. Add new story cards to existing steps
4. Create new steps or journeys only if the change introduces new user activities
5. Assign milestones to prioritize across releases
6. Set statuses as work progresses

## Structural Guidelines

### Journey Naming

- Use verb phrases: "Discover Product", "Complete Purchase", "Manage Account"
- Name from the user's perspective, not the system's
- Read left-to-right as a narrative: "First they X, then they Y, then they Z"

### Step Naming

- Use specific action phrases: "Browse Catalog", "Add to Cart", "Enter Payment"
- Should be concrete enough that a team member can imagine the screen or interaction
- Ordered within the journey as the user would experience them

### Story Card Titles

- Short and descriptive: prefer "Display search results" over "As a user I want to see search results so that I can find what I need"
- Use the description field for details, acceptance criteria, and context
- Title should fit in a card on the board without truncation

### When to Add Milestones

- The user mentions releases, sprints, phases, or timelines
- The board is being used for planning rather than discovery
- There's a need to distinguish "must have now" from "nice to have later"
- Don't add milestones to every board — discovery boards often don't need them

### When to Use Colors

- Multiple personas interact with the same journey steps
- Multiple teams own cards across the same board
- A cross-cutting concern (e.g., "needs design review") spans multiple journeys
- Limit to 2-4 colors and always explain what each color means
