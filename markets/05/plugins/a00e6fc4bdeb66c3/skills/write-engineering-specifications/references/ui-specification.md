# UI and Interaction Specification

Specify visual behavior only from approved designs, verified existing tokens, or clearly labeled proposals.

## Finality and controlled production decisions

Classify implementation-relevant requirements as `FIXED`, `TARGET`, `BOUND`, `PROFESSIONAL_DISCRETION`, `ENGINEERING_DISCRETION`, `OWNER_DECISION_REQUIRED`, `CALIBRATION_REQUIRED`, `VERIFY_AT_RUNTIME`, or `PERCEPTUAL_ACCEPTANCE`. Use exact production values when they are supported by an owner decision, authoritative standard, approved-artifact measurement, real calibration, or mathematical necessity. Do not manufacture exactness for professional microdecisions.

Before a visual specification becomes `FINAL`, every Class-1 decision must be approved; every Class-2 zone must identify lead role, target, bounds, invariants, evidence, reversibility, checkpoint, reviewer, and stop condition; Class-3 space must be bounded by the approved outcome. Record `ENTSCHEIDUNGSLÜCKE` only when those controls are missing, not merely because a professional judgment remains.

## Required surfaces

- viewport and breakpoint strategy;
- grid, container, alignment, spacing, and density;
- component anatomy and content hierarchy;
- typography roles, sizes, weights, line heights, and wrapping;
- color tokens, contrast, surfaces, borders, elevation, and icons;
- asset source, crop, aspect ratio, loading, fallback, and rights status;
- interaction states: default, hover, focus, active, selected, disabled, loading, empty, success, warning, and error;
- keyboard sequence, focus management, semantics, labels, announcements, targets, zoom, and reduced motion;
- animation trigger, affected element, property, duration range, easing, sequence, interruption, and reduced-motion fallback;
- responsive rearrangement, hiding rules, overflow, touch behavior, orientation, and safe areas;
- content constraints, truncation, localization expansion, and validation messages.
- relationship specifications such as surface roles, visual hierarchy, relative weight, spacing rhythm, shadow grammar, and component relationships;
- representation strategy and proof for important visible components whose production method is not already proven;
- primary source ownership for each material observable;
- local preview checkpoints and perceptual acceptance where objective tests are insufficient.

## Component record

| Field | Required detail |
|---|---|
| Component ID/name | Stable identifier |
| Purpose | User need and placement |
| Anatomy | Child elements and hierarchy |
| Content | Exact copy or bounded content rules |
| Inputs/properties | Type, allowed values, defaults |
| States | Visual and behavioral states |
| Interactions | Trigger, action, feedback, side effect |
| Responsive behavior | Changes by available space |
| Accessibility | Semantics, keyboard, focus, announcements |
| Tokens and requirement class | Approved values, targets, bounds, calibration, or discretion contract |
| Analytics | Event and permitted properties, if required |
| Acceptance | Visual and functional evidence |

When measurements are unavailable, do not invent pixel values and present them as approved. Classify the requirement according to evidence and authority. A target or controlled professional-discretion zone may be final when its acceptance, reviewer, and verification are explicit.
