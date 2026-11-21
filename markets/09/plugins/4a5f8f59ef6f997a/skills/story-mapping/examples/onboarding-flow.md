# Example: SaaS Onboarding Flow

A story map for a SaaS product's user onboarding experience, from initial discovery through becoming an active user.

## Board Structure

**Board name:** "User Onboarding Story Map"
**Board description:** "Mapping the end-to-end onboarding experience for new users of our project management tool"

### Journeys (left to right)

1. **Discover Product** — How users first learn about the tool
2. **Sign Up** — The registration and initial setup experience
3. **First Value** — Getting the user to their first meaningful outcome
4. **Invite Team** — Expanding from solo use to team collaboration

### Milestones

- **MVP Launch** — Minimum viable onboarding
- **V1.1** — Improvements based on initial feedback
- **Future** — Nice-to-have enhancements

---

## Detailed Structure

### Journey: Discover Product

#### Step: Land on Marketing Site

- (objective) "User understands value proposition in 5 seconds"
- (none) "Hero section with clear headline and CTA"
- (none) "Social proof section with customer logos"
- (question) "Do we show pricing on the landing page or gate it?"

#### Step: View Demo

- (objective) "User sees the product solving their problem"
- (none) "Interactive product tour"
- (risk) "Demo may not match user's specific use case"
- (knowledge_gap) "What demo scenarios resonate most with our ICP?"

### Journey: Sign Up

#### Step: Create Account

- (objective) "Account creation under 30 seconds"
- (none) "Email + password form"
- (none) "OAuth with Google and GitHub"
- (risk) "Email verification friction may cause drop-off"
- (learn) "SSO conversion rate 3x higher than email (from competitor analysis)"

#### Step: Initial Setup

- (objective) "User has a configured workspace in under 2 minutes"
- (none) "Workspace name and URL slug"
- (none) "Template selection for first project"
- (question) "Should we ask about team size during setup?"
- (knowledge_gap) "What information do we actually need vs. what can be inferred?"

### Journey: First Value

#### Step: Create First Project

- (objective) "User creates a project and adds first items within 5 minutes"
- (none) "Project creation wizard from template"
- (none) "Pre-populated sample data that's editable"
- (risk) "Blank slate problem — empty project feels overwhelming"
- (learn) "Users who create their first project within 10 minutes have 60% higher retention"

#### Step: Complete First Task

- (objective) "User experiences the core workflow loop"
- (none) "Guided walkthrough of task creation"
- (none) "Contextual tooltips for key features"
- (none) "Achievement celebration on first task completion"
- (question) "Should the walkthrough be skippable?"

### Journey: Invite Team

#### Step: Send Invitations

- (objective) "At least one teammate joins within first session"
- (none) "Email invitation flow"
- (none) "Shareable invite link"
- (risk) "User may not have team email addresses handy"
- (learn) "Teams that add a second member in day 1 retain at 4x the rate of solo users"

#### Step: Collaborative Onboarding

- (objective) "Invited user has a productive first session"
- (none) "Teammate landing page with context about the workspace"
- (none) "Suggested first actions based on existing project state"
- (question) "Should new team members see the same onboarding or an abbreviated version?"

---

## Card Count Summary

| Journey          | Steps | Story Cards | Objectives | Risks | Questions | Knowledge Gaps | Learnings |
| ---------------- | ----- | ----------- | ---------- | ----- | --------- | -------------- | --------- |
| Discover Product | 2     | 8           | 2          | 1     | 1         | 1              | 0         |
| Sign Up          | 2     | 9           | 2          | 1     | 1         | 1              | 1         |
| First Value      | 2     | 9           | 2          | 1     | 1         | 0              | 1         |
| Invite Team      | 2     | 8           | 2          | 1     | 1         | 0              | 1         |
| **Total**        | **8** | **34**      | **8**      | **4** | **4**     | **2**          | **3**     |

## Notes

- Objectives are placed at the top of each step to frame the work
- Risks and questions are distributed across steps rather than clustered
- Learnings provide evidence-based grounding for design decisions
- No colors used — a single-persona flow doesn't benefit from cross-cutting color groupings
- Milestones would slice horizontally: MVP items near the top, future items lower
