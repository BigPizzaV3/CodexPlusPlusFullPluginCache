# Visual implementation field contract

Apply only fields relevant to declared scope; record N/A with evidence-based reason. An unknown is not N/A. Use existing registers/IDs by reference. Each material value or relationship carries its source revision and element/section, authority, requirement classification, owner, dependent build area and acceptance ID. Derived tables do not become competing source truth.

## Freeze and gap record

Record package/scope ID, version, approval evidence, design source IDs/revisions/frames, allowed source sections, CURRENT/SUPERSEDED relationship, precedence, repository baseline and recipient access. CURRENT describes active authority for that scope, not merely last modified. Keep sources governing copy, assets, geometry and behavior distinguishable. For conflict: both claims, evidence, scope, missing authority/decision, impacted tasks, owner and resolution requirement. An owner-approved unaffected task slice may be ready separately; never report the blocked parent scope ready.

## Visual system

- **Geometry:** coordinate reference and units, container constraints, aspect ratios, anchors, alignment, overflow, min/max sizes and intrinsic behavior. Describe relationships as well as reference-frame dimensions; do not flatten a responsive system into one screenshot's absolute coordinates.
- **Grid / spacing / radii:** columns, gutters, margins, nesting, alignment, token mapping and approved exceptions per breakpoint/state. Define interpolation/reflow only when approved, not by guessing industry-standard breakpoints.
- **Typography:** exact family/file/weight/style, license/access status, size, line height, tracking, wrapping, text measure and fallback behavior. Unsupported font substitution is a gap.
- **Colors:** roles, source color space where material, opacity and compositing context; approved contrast/accessibility constraints. Flag inaccessible approved designs for owner resolution; don't silently recolor them or waive the constraint.
- **States:** default, hover, focus, active, disabled, loading, empty, success and error only where applicable to actual behavior; data extremes, localization and overflow. Map content-dependent geometry explicitly.
- **Responsive / motion:** supported viewports, reflow order, hidden/replaced content, touch/keyboard behavior, transitions, duration/easing/triggers, reduced-motion behavior and scroll/sticky rules where relevant. A static source alone cannot establish these.

## Surface recipe per material surface

Stable ID and source region; silhouette; fill/material; gradient direction and stops; border/stroke; radius; shadow/highlight; blur/backdrop; texture and scale; blend/opacity; masks and clipping; internal padding; foreground/background relationships; states; approved representation and runtime limitations. Use exact values only from valid authority. For layered scenes include parent/stacking context, local layer order, overlaps, occluders, masks, hit-testing and focus/accessibility implications. A single arbitrary z-index list is insufficient when nesting or clipping changes the result.

Preserve approved anti-generic rules as testable, source-linked invariants: characteristic composition, typography, imagery, surface relationships and content presentation; list specifically forbidden substitutions only when supported by authority. Do not impose a universal ban on cards, gradients or a particular aesthetic. If a frozen premium design conflicts with its approved distinctiveness criteria, flag the conflict to its owner rather than decorate or redesign it.

## Asset truth and copy truth

Asset entry: ID, authoritative file/location/revision, intended role and component/state, observed availability, dimensions/format/alpha/color profile where relevant, permitted use/license evidence, export transformation, crop/focal point, scaling, runtime mapping and approved fallback. Hash only when integrity risk warrants it. Distinguish an unavailable file from an unchosen asset. A link without recipient access is not a usable handoff. Do not publish private assets or bundle secrets.

Copy entry: stable content ID, exact approved text including punctuation, locale, source/revision/approval, target element/state, link destinations, accessibility labels and dynamic-content rules. Mark illustrative mockup copy explicitly; it cannot be used as production truth. Truncation, line breaks and fallback text follow authority, not the builder's taste.

## Build and acceptance mapping

For each component/state: visual source and recipe IDs → asset/copy IDs → existing or approved new implementation target → functional interface → protected constraints → technical test → visual acceptance criterion. Respect an existing blueprint/file map; use one canonical owner per observable.

Technical acceptance covers applicable behavior, build, accessibility, responsive mechanics, performance and regressions using approved commands/thresholds. Unknown commands are not invented. Visual acceptance specifies approved reference, observable relationships, allowed deviations, capture state/viewport/DPR/browser/fonts/data/motion-time when measurement-relevant, comparison method and reviewer/owner. Missing material acceptance thresholds or authorities block readiness. Known-good authority remains separate from the candidate; baseline replacement requires approval.

## Minimal Claude contract view

Carry each applicable scoped `METHOD_LOCK` from the shared task contract into the build mapping and Claude brief. Preserve its essential mechanisms, prohibited substitutions and authorized calibration; require receiver access to the exact record. The existing decision-authority model owns this view and its failure/reopen rules. Missing material lock information blocks affected readiness rather than becoming a builder choice.

Use the shared task contract rather than inventing a second prompt schema. Provide first-read order, scoped active source manifest, exact source/asset access, protected invariants, decision-complete visual slice, allowed nonmaterial engineering choices, evidence requirements and next safe task. On any material design uncertainty the builder must identify the source/element and missing decision, emit `DESIGN SPEC CONFLICT`, and stop dependent work. No “make it premium,” invented values, placeholder acceptance, framework switches or out-of-scope cleanup. Handoff readiness never overrides existing owner or production gates.
