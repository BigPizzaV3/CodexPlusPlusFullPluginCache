# TMC rendered verification matrix

Use the current handoff's exact matrix when it defines one. The values below are the standing TMC baseline and should be updated when later authority replaces them.

## Targets and claims

Resolve the official browser, device, accessibility, and privacy targets from current authority before making a support or conformance claim. Record exact browser names and versions tested, real device or emulation, operating system when material, and the accessibility standard and method used.

If official targets do not exist, propose a provisional matrix for approval. Until it is accepted, describe completed checks as sampled coverage rather than official support. A result may still identify observed defects, but it must not claim full browser support or accessibility conformance.

For consequential shared UI changes, sample more than one browser engine when tools and authority permit. Do not treat two Chromium-branded browsers as independent engine coverage. Use real devices when emulation cannot establish virtual-keyboard, safe-area, touch, viewport, font, or platform-control behavior.

## Widths

Cover the composition changes, not merely device labels:

- wide desktop around 1920 or 1800 pixels;
- 1600 pixels around the full and compact context threshold;
- 1440 pixels for common desktop;
- 1366 by 768 for the known laptop pressure case;
- 1280 by 800 for constrained desktop;
- 1024 by 768 for narrow workspace and drawer pressure;
- 820 or 768 pixels around tablet and navigation transitions;
- phone widths from 390 to 430 pixels.

Record the viewport and usable application or component width. Sidebars, browser zoom, split panes, drawers, and devtools can make a wide viewport a narrow workspace.

Test 200 percent zoom or increased text size on required journeys where the environment permits.

## Data pressure

Use product-valid combinations:

- Purchase, Sale, and Combined;
- one, two, and four applicants;
- long two-person names;
- zero, two, and eight or more factors;
- long lender, Provider, brokerage, client, and property names;
- long addresses and reference values;
- one available Provider and many Providers;
- selected and unselected Provider;
- no available Provider;
- current, stale, draft, saved, unsaved, and recovery states when supported;
- live, loading, retry, timeout, empty, validation, error, success, disabled, and destructive states;
- role and permission differences that change actions;
- populated and zero-data accounts.

Do not create a broker-visible state that current product authority forbids merely to fill the matrix.

## Responsive continuity

Across layout changes confirm:

- reading and focus order remain logical;
- primary actions and consequential information remain reachable;
- labels, totals, units, freshness, warnings, and selected state remain visible;
- entered data, selection, expansion, and relevant scroll context survive;
- cockpit, compact cockpit, ribbon, drawer, and mobile treatment follow current authority;
- navigation and Quote context do not collapse into an ambiguous control;
- no page-wide horizontal scroll, clipped popover, covered content, off-screen action, or inaccessible sticky element appears;
- dialogs, sheets, tables, cards, charts, and drawers fit their usable container;
- touch and pointer targets do not overlap.

## Interaction and accessibility

Where relevant, inspect:

- keyboard traversal and activation;
- visible focus and sensible focus return;
- accessible names for icon-only controls;
- selected, expanded, busy, invalid, and live-status semantics;
- contrast and non-color cues;
- error summary and field-level association;
- target size;
- screen-reader announcements when the available tools can establish them;
- reduced-motion behavior;
- Escape, outside-click, scroll lock, and focus trapping for dialogs, drawers, and sheets.

Do not claim screen-reader compatibility from appearance or DOM shape alone.

## Asynchronous, session, and recovery sequences

Apply this section when the lane changes asynchronous data, saving, repricing, selection, submission, authentication, permissions, or recovery. Use a safe local, preview, or test environment. Do not trigger real Provider communication, production Case creation, or production-data mutation.

Where relevant, check:

- rapid consecutive input changes and responses arriving out of order, confirming that only the latest valid result controls the UI;
- loading and pending controls, repeated clicks, retry, timeout, cancellation, and reconnection without duplicate or contradictory outcomes;
- immediate referral-fee repricing and the authorised Provider-selection clearing behavior under rapid changes;
- repeated Instruction submission or retry without implying that a disabled button replaces backend idempotency or exactly-one Case protection;
- refresh, browser back and forward, route changes, and accidental navigation with saved and unsaved work;
- session expiry before save, during a request, and before a consequential submit, including reauthentication and safe preservation or recovery of entered data;
- permission or role changes during an open session;
- a second tab when the affected state can realistically be edited in more than one tab.

Record the request sequence, visible state, authoritative final response, and resulting persisted state. If the environment cannot force timing or failure conditions reliably, label the result unverified rather than simulating a success path and claiming resilience.

## Runtime and frontend privacy inspection

For the affected journey, inspect the browser console and network activity for new unhandled exceptions, rejected promises, hydration mismatches, repeated or failed requests, sensitive query parameters, and requests caused by stale or duplicate effects. Establish whether visible noise predates the lane before assigning it to the change.

Use synthetic or explicitly approved test data. Check that client names, addresses, references, quotes, Case details, tokens, and other sensitive values do not appear unnecessarily in:

- URLs, query strings, page titles, referrers, or browser history;
- console output, client-visible stack traces, analytics, telemetry, or error payloads;
- local storage, session storage, caches, persisted state, or screenshots;
- third-party requests or services not covered by current authority.

Inspect only what the UI sends or stores as part of the affected behavior. This is a frontend privacy check, not proof of backend security, tenant isolation, penetration resistance, legal compliance, or the absence of all data leakage. Escalate evidence of a wider issue without expanding the UI lane into an unauthorised security exercise.

Record the request type, destination, field category, storage location, or error class needed to prove the finding. Redact tokens, cookies, credentials, personal data, and raw client payloads from screenshots, logs, reports, prompts, and handoffs.

## Visual and motion checks

Confirm:

- the visual hierarchy follows the decision sequence;
- the action hierarchy remains consistent;
- financial values align and do not jump misleadingly;
- loading skeletons match the real geometry;
- transitions preserve causality and do not block input;
- real server state appears without fake intermediate values;
- success and failure feedback attaches to the action that caused it;
- decorative effects do not reduce contrast, performance, or readability;
- reduced motion removes nonessential animation without hiding state change.

## Completion evidence

For each material repair retain:

- before and after evidence at the same state and width;
- route, role, data, viewport, usable container, zoom, and browser;
- browser version, operating system or device when material, accessibility method, and whether the target was official or provisional;
- expected behavior and observed result;
- relevant DOM or accessibility evidence;
- relevant asynchronous sequence plus console, network, session, and privacy evidence;
- tests run and result;
- representative broker acceptance when required, including the acceptance owner and unresolved observations;
- any unavailable coverage.

A screenshot gallery without state labels is not a verification record. Name or index each capture with its route, state, viewport, usable container, role, data fixture, browser, and before or after status. Compare like with like. Use automated visual diffs when the repository already supports them, but inspect the diff because fonts, animation, timestamps, and dynamic data can create noise. Do not approve a changed baseline solely because the new image was generated by the current code. Record where evidence is retained, and do not commit generated captures unless repository convention or the accepted lane requires it.
