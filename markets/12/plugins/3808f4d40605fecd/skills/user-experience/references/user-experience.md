# User Experience

## Required Related Resources

- [Agent Instructions](../AGENTS.md) — `AGENTS.md`
- [UI Design](ui-design.md) — `skills/ui-design.md`

## Purpose

This skill owns user needs, task and content priorities, wording, interaction requirements, and recovery. [UI Design](ui-design.md) coordinates component selection, token use, visual composition, and rendered review; its linked skills own visual treatment.

## User-centricity

Design around researched user needs and goals while balancing business requirements.

- Identify users, their tasks, existing workflows, and barriers using available research, analytics, and feedback.
- Define the desired outcome before choosing the interface. “Compare options” describes a need; “add a dashboard” specifies a solution.
- Separate evidence from assumptions. Do not assume users share the agent’s knowledge or preferences, or invent research findings.
- Define content, navigation, interaction requirements, and task priorities from user needs. Delegate component selection to [UI Design](ui-design.md#component-selection), within the behavior supported by [canonical components](canonical/components.md), and visual emphasis to [Visual Hierarchy](ui-design/visual-hierarchy.md).

## Usability

Make tasks easy to learn, efficient to complete, and satisfying to use.

- Make starting points and expected outcomes understandable. Ensure actions do what their labels and explanations promise, within the supported behavior of [canonical components](canonical/components.md).
- Remove unnecessary steps and repeated entry. Offer supported shortcuts for frequent tasks.
- Explain unfamiliar actions where they occur.
- Test realistic tasks with representative first-time and returning users for completion, effort, errors, and satisfaction. Fix observed difficulties and recheck. Distinguish an agent walkthrough from actual user testing.

## Consistency

Use consistency when designing screens and flows so users can reuse what they have already learned.

- **Colors:** Preserve color meaning across screens and states. Follow [Color Discipline](ui-design/color-discipline.md) for semantic roles and [UI Design](ui-design.md) for token guidance.
- **Typography:** Keep equivalent text roles consistent across headings, body copy, labels, and data. Follow [Typography and Readability](ui-design/typography-readability.md) for their treatment.
- **Layout and spacing:** Keep recurring navigation and actions in predictable locations. Delegate their visual treatment to [Grid and Layout](ui-design/grid-layout.md), [Rhythm and Space](ui-design/rhythm-space.md), and [Alignment](ui-design/alignment.md).
- **Components:** Keep equivalent tasks recognizable through familiar interaction patterns. Delegate component and variant selection to [UI Design](ui-design.md#component-selection).
- **Content:** Use the same names for the same concepts across navigation, headings, controls, and messages. Maintain a consistent voice; do not use the same label for actions with different consequences.
- **Behavior:** Make equivalent actions behave consistently, including saving, cancellation, validation, feedback, and recovery. Follow familiar platform conventions unless a confirmed user need requires a departure.

## Context

Account for the circumstances in which people use the interface.

- Identify relevant devices, input methods, connectivity, surroundings, abilities, language, and privacy constraints.
- Match instructions, detail, and task sequence to users’ familiarity, attention, urgency, and current task stage. Do not infer these from screen size alone.
- Specify supported alternatives when conditions make sound, precise input, or sustained attention unreliable.
- Preserve drafts and task context through interruptions, connection loss, and session expiry where supported. On return, distinguish saved from unsaved work and show the current status and next step. Never claim progress was saved without confirmation.
- Pass these requirements to [Responsive Adaptation](responsive-adaptation.md) for interface changes and [Accessibility Audit](accessibility-audit.md) for verification.

## Hierarchy

Make content and action priorities immediately apparent.

- Define what users need to understand, decide, and do at each task stage. Distinguish essential information from supporting detail and optional actions.
- Sequence tasks around their dependencies. Provide prerequisites, costs, and consequences before the decision they affect.
- Identify the action that advances the current task and the meaningful alternatives. Do not invent a preferred choice when options deserve equal consideration.
- Reassess priorities when circumstances change. A blocking error may make recovery the immediate task.
- Pass these priorities to [Visual Hierarchy](ui-design/visual-hierarchy.md) for visual expression.

## Navigation and Orientation

Make location, destinations, and next steps clear.

- Identify the current page, section, or task step, including when users arrive through direct links.
- Use destination labels users understand and organize routes around their tasks.
- Make active filters and their effect on the results clear.
- Provide clear ways to continue, return, or exit. Preserve relevant state when returning; warn before navigation discards unsaved work.
- Delegate component selection and appearance to [UI Design](ui-design.md), and navigation accessibility checks to [Accessibility Audit](accessibility-audit.md).

## Simplicity

Remove unnecessary content, choices, and decoration while preserving what users need to complete the task.

- Include sections, controls, and messages only when they support understanding, decisions, actions, or recovery.
- Do not generate introductions, subtitles, helper text, summaries, or repeated calls to action by default. Add them only when they answer a real user need.
- Remove redundant choices and unnecessary decisions. Keep meaningful alternatives available.
- Preserve essential labels, instructions, consequences, feedback, and recovery. A sparse interface must not create more guessing or navigation.
- Flag decoration that distracts from the task. Resolve its treatment through [UI Design](ui-design.md), respecting the confirmed brand and style.

## Cognitive Load

Reduce mental effort; favor recognition over recall.

- Keep instructions, requirements, and relevant earlier answers available where needed. Do not require users to remember information from another screen.
- Offer recognizable options and supported suggestions instead of requiring exact names, codes, or commands from memory.
- Break complex tasks into meaningful groups or steps, retaining the context needed for each. Delegate their presentation to [UI Design](ui-design.md).
- Provide comparisons and summaries so users can review decisions without mentally reconstructing them.
- Let the system handle supported calculations and conversions. Show the inputs and results users need to verify them.

## User Control

Support deliberate choices, cancellation, and reversal.

- Explain commitments and data use before agreement. Do not use misleading defaults or make refusal unnecessarily difficult.
- Make clear when changes take effect: immediately, on Save, or on submission. Do not silently replace users’ choices.
- Before bulk actions, clarify which items are affected, including selections across pages.
- Provide a clear way to cancel unfinished tasks. Distinguish closing a view from stopping an operation or discarding edits.
- Offer undo or reversal where supported. Explain what it reverses, any time limit, and when an action cannot be undone.
- Let users revise choices and dismiss optional prompts. Keep automatic changes of context under user control.
- Delegate controls to [UI Design](ui-design.md). Never promise cancellation or undo that the product cannot perform.

## Feedback and Closure

Communicate actions, progress, outcomes, and completion.

- Acknowledge actions promptly. A clear state change is enough; avoid redundant confirmation messages.
- Explain waits and show reliable progress when available. Never invent percentages or completion times.
- Distinguish processing from completion, partial success from full success, and uncertain outcomes from confirmed results.
- Distinguish first-use emptiness, no matching results, and unavailable access. Explain the reason and offer a useful, supported next action.
- End flows with a clear result and any remaining action. Explain what happens next and when, where relevant.
- Match feedback to the action’s importance; keep essential results available to review. Delegate presentation to [UI Design](ui-design.md) and accessibility checks to [Accessibility Audit](accessibility-audit.md).

## Error Prevention and Recovery

Prevent predictable mistakes and help users recover without losing work.

- Explain requirements before entry. Validate when users have provided enough information; do not flag unfinished input as an error.
- Provide checking, review, or confirmation before costly, hard-to-reverse actions.
- Explain what failed and how to proceed. Distinguish input mistakes from permission or service problems.
- Preserve entered data and completed work. Let users correct affected parts without restarting.
- For partial failures, identify unsuccessful items and support retrying them without repeating completed actions. Offer recovery only when the product supports it.
- Delegate presentation to [UI Design](ui-design.md) and accessibility checks to [Accessibility Audit](accessibility-audit.md).

## Readability and Scannability

Design content so users can quickly locate what matters, then read enough to understand and act.

- Use plain, familiar language and short, direct sentences. Explain necessary specialist terms when first used.
- Put the main answer or takeaway before supporting explanation.
- Write descriptive headings, links, and control labels. Name the topic, destination, or action explicitly—for example, “Save changes” instead of “OK”—and put meaningful words early.
- Keep each paragraph focused on one point. Introduce that point immediately so readers can judge its relevance.
- Use lists for distinct items or steps and tables for structured comparisons. Keep connected explanations in prose.
- Identify the key words readers need to find. Delegate emphasis to [Visual Hierarchy](ui-design/visual-hierarchy.md) and text treatment and legibility to [Typography and Readability](ui-design/typography-readability.md).
- Cut redundant wording, filler, and exaggerated promotional claims without removing information needed for understanding or decisions.
- Support both scanning and sustained reading. Do not force every page into an F-pattern; reading patterns vary with task, motivation, and attention.

**Check:** Can someone scanning headings, opening sentences, and emphasized words locate the answer—and understand it when reading further?
