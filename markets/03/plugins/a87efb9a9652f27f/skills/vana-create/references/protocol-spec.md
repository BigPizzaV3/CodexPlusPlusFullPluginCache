# Protocol spec v0.4

A protocol is a reusable plan for making progress toward a goal over time.

The protocol is one content-only Markdown file, saved at `protocols/<slug>/protocol.md` in the user's Data. It contains no YAML frontmatter, document title, summary, category, tags, sources, risk classification, or other application metadata.

## Scope

A protocol can cover any goal or repeatable activity the user chooses. The user's request defines the subject. This spec defines how to turn that request into a clear system of actions, adjustments, and progress checks.

## Style

- Write practical instructions that fit the user's goal and constraints.
- Keep the draft bounded to the user's request.
- Match the example's density. Use short bullets under each H1. Use `##` subsections only when a section has natural groups. Use `- **Label:** detail` for compact sets of related details.
- Use `Not applicable` only when a section truly does not apply, and explain why.
- Use the user's facts and linked sources. Mark assumptions as assumptions.

## Required Sections

Every protocol contains these top-level H1 headings exactly once and in this order.

### `# Purpose`

The goal, the intended user, the starting point, the time horizon, and what completion means.

### `# Boundaries`

The scope, constraints, exclusions, and conditions that should change or end the protocol.

### `# Requirements`

The time, information, tools, materials, environment, or access needed to follow the protocol.

### `# Protocol`

The steps, sequence, schedule, duration, and smallest useful version. The user must be able to follow this section without inventing missing steps. Use numbered steps for ordered work.

### `# Adaptation`

How to change the protocol when the user's time, resources, pace, or results change. State how to resume after an interruption. Use labels that match the protocol.

### `# Tracking & Review`

The smallest set of facts needed to show progress and choose the next action. Define when to record them, when to review them, and how the review changes the protocol.

### `# Rationale`

Why this structure fits the goal. State the important assumptions, tradeoffs, and source basis. Keep this section short.

## Example

This example shows the section shape and the density to match:

```md
# Purpose

- Publish six useful newsletter issues in six weeks.
- For a first-time newsletter writer with one topic and three hours each week.
- Complete when all six issues are sent and archived.

# Boundaries

- Cover one topic for the full six weeks.
- Keep each issue under 1,000 words.
- Change the schedule before adding more work when two issues miss their planned date.

# Requirements

- One three-hour writing block each week
- A list of six issue ideas before week one
- Access to the publishing tool

# Protocol

1. Monday: choose one idea and write a one-sentence promise for the reader.
2. Tuesday: outline the issue in five bullets.
3. Wednesday: write the first draft.
4. Thursday: edit the draft and check every link.
5. Friday: send the issue and add it to the archive.

# Adaptation

- **Short week:** publish a 300-word issue that answers one question.
- **Missed issue:** move it to the end of the six-week run. Keep the next planned topic on schedule.
- **Idea does not work:** replace it with the first unused idea from the list.

# Tracking & Review

- Record the planned date, sent date, topic, word count, and writing time for each issue.
- Review after issue three. If two issues missed their date, shorten the next issue before changing the weekly schedule.
- Review after issue six and keep the steps that matched the available three hours.

# Rationale

- A fixed weekly sequence makes the next action clear.
- The short-week version preserves the publishing schedule when time is limited.
- The three-issue review gives enough work to test the schedule before changing it.
```
