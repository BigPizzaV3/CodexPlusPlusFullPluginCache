# UX Flow and State Patterns

## Purpose

Use this file to design how the product works before polishing visual style.

Good UX supports the user's task, keeps them informed, preserves context, supports recovery, and includes accessibility from the start.

# 1. Primary-flow template

For each important task define:
1. Entry point
2. User intent
3. Required information
4. Main action
5. System feedback
6. Result
7. Recovery/undo
8. Next logical action

Avoid unnecessary steps.

# 2. Screen/state matrix

For important screens consider:

| State | Question |
|---|---|
| First use | Does the user know what to do? |
| Empty | What can they do next? |
| Loading | Is progress understandable? |
| Success | Is completion clear? |
| Error | What failed and how can they recover? |
| Partial | Can useful work continue? |
| Permission denied | Why and what can they do? |
| Offline/degraded | What remains available? |
| Destructive action | Is consequence clear and reversible where possible? |

Do not add every state mechanically; include only reachable states.

# 3. Onboarding

Use onboarding only when the user cannot reasonably start without it.

Prefer:
- direct entry into value;
- progressive disclosure;
- contextual explanation.

Avoid long tutorials before the user sees the product.

Ask for permissions only when the need is understandable in context.

# 4. Navigation

Navigation should reflect stable user mental models and primary tasks.

Choose patterns based on product structure:
- top-level tabs for a small number of peer sections;
- sidebar for larger desktop information architectures;
- hierarchical navigation for drill-down content;
- search when retrieval is central;
- command/action surfaces for expert workflows.

Do not turn actions into navigation or navigation into hidden gestures.

# 5. Forms and input

Prefer:
- only necessary fields;
- useful defaults;
- clear labels;
- inline validation;
- preserved input after errors;
- correct keyboard/input type;
- explicit optional fields.

Do not request data before it is needed.

# 6. Errors and recovery

Error messages should answer:
1. What happened?
2. Was my work preserved?
3. What can I do now?

For destructive or consequential actions:
- preview effect when practical;
- confirm intent;
- offer undo/restore when feasible;
- distinguish reversible from irreversible actions.

# 7. Responsive/adaptive behavior

Do not merely shrink desktop layouts.

Define:
- what remains primary;
- what can move/collapse;
- navigation change;
- touch vs pointer behavior;
- content priority;
- table/list adaptation;
- modal/sheet behavior;
- keyboard support where relevant.

For native apps, follow platform conventions.

# 8. Accessibility baseline

Design accessibility into flows, not as a final pass.

Consider:
- keyboard navigation;
- visible focus;
- semantic labels;
- screen-reader order;
- sufficient contrast;
- text scaling;
- target size;
- alternatives to drag-only interaction;
- alternatives to color-only meaning;
- reduced motion;
- accessible authentication;
- understandable errors.

For web-specific conformance details, verify current WCAG guidance.

# 9. UX writing

Use clear action-oriented labels, consistent terminology, concise instructions, specific error messages, and user language rather than internal system terms.

Avoid clever labels that hide meaning.

# 10. Flow review

Before approving a flow ask:
- Can the user reach value quickly?
- Is the next action obvious?
- Is system status visible?
- Are important failures represented?
- Can users recover?
- Are permissions understandable?
- Does the flow work without relying on hover/color/gesture only?
- Is important context preserved?
- Does mobile/native behavior feel appropriate rather than copied from desktop?
