# Accessibility Web Quality Checklist

## Purpose

Use this file for practical accessibility QA. Automated tools provide evidence but do not prove conformance.

Verify current WCAG guidance when exact criteria/conformance details matter.

# 1. Semantics

Check:
- landmarks;
- heading hierarchy;
- buttons vs links;
- list/table semantics;
- meaningful accessible names.

Avoid replacing semantic controls with generic clickable containers without equivalent accessibility.

# 2. Keyboard

Test:
- all interactive controls reachable;
- logical order;
- visible focus;
- no keyboard traps;
- custom widgets operable.

# 3. Focus management

For dialogs, drawers, route changes, and dynamic UI:
- move focus intentionally when needed;
- keep focus inside modal interaction when appropriate;
- restore focus after close;
- avoid lost focus after updates.

# 4. Forms

Check:
- programmatic labels;
- instructions;
- required state;
- validation;
- error association;
- preserved input;
- accessible input purpose when relevant.

# 5. Dynamic updates

Important asynchronous changes may need programmatic announcements:
- success;
- errors;
- loading completion;
- live results;
- status changes.

# 6. Color and contrast

Check text, non-text contrast where relevant, focus indicators, status, and charts.

Do not use color alone for required meaning.

# 7. Text resizing and zoom

Verify zoom, larger text, reflow, clipping, and content loss.

# 8. Motion

Respect reduced-motion preferences when animation is nonessential or potentially problematic.

# 9. Touch targets

Critical controls should be large/spaced enough for reliable activation.

Verify current WCAG/platform guidance when exact minimums matter.

# 10. Screen reader

Manual verification should cover critical journeys when accessibility is important.

Check:
- page title/landmarks;
- headings;
- control names/states;
- form errors;
- dialogs;
- dynamic status;
- table relationships.

# 11. Automated vs manual

Automated tools are useful for missing labels, contrast, ARIA misuse, and structural issues.

Manual testing remains necessary for keyboard flow, focus order, understandable names, screen-reader experience, error recovery, and actual task completion.
