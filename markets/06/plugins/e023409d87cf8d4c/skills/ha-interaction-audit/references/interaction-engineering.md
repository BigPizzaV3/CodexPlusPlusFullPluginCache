# Interaction engineering

## Input fidelity

Prefer permitted browser locators with actionability checks. For Puppeteer coordinates, resolve a unique target, scroll only if needed, wait for stable geometry, re-resolve, verify viewport visibility and hit testing through shadow roots, then tap. Record coordinates and identity. Do not force obstructed clicks, accept multiple matches, or act on detached/stale elements. Match virtualized records by stable ID.

Use actual keyboard input for typing. Observe the deepest active element through shadow roots, input value, app draft, selection start/end/direction. Programmatic caret placement is setup, not typing. `fill()` can establish data but cannot prove per-keystroke resilience.

Touch, mouse, keyboard and synthetic DOM events are separate modes. Browser automation touch is still emulated. Viewport/user-agent changes do not reproduce native iPhone keyboards, pickers, rubber-band scrolling, WKWebView lifecycle, VoiceOver or OS notifications.

## Timing

Use observable conditions and bounded polling. Two stable frames establish geometry, not completion of delayed restoration. Combine app signals with bounded stability windows. Record deadlines and observed times.

Run separately: normal pace; paced HA events during interaction; explicitly labeled synchronous bursts; repeated redraws with normal completion; and deliberate new interaction during pending restore/debounce/response. A corrected settling helper must retain the rapid-race case. Never hide it by putting a long sleep after every Back.

Use deterministic interleaving seeds. Start with targeted race pairs, not a random tap storm. Bound stress by useful coverage and runtime. No artificial elapsed-time target.

## Scroll and routes

Measure actual scrollers: document, HA panel, editor, modal and horizontal strips. Serialize each DOMRect field explicitly; spreading a DOMRect can lose its values.

Capture return scroll after any positioning needed to open the item. Verify content is sufficiently scrollable. Compare prompt and settled positions with explained tolerance, usually a few CSS pixels for stable layouts. Permit clamping only if content really shortened. When dynamic content invalidates pixel identity, verify the semantic visible anchor too.

Exercise app Back, browser Back/Forward, deep links, reload, filters, session restoration and rapid new navigation. New user intent should cancel stale restore callbacks when that is the product contract. Measure layout and visual viewports, transformed containing blocks, safe areas, content underlap, z-index and modal/nav overlap.

An intentional floating nav gap is not automatically a bug. Decide gesture behavior from the design. Do not blanket-disable pinch zoom or page scrolling to mask a nav issue.

## State, events and persistence

Count transitions and request intents for nested buttons, labels, rows, keyboard activation and repeated mount/unmount. Inspect bubbling/composed paths and duplicate listeners. A toggle that finishes unchanged may have toggled twice.

Exercise valid/invalid save, cancel, repeated save, late response after navigation, failed retry, partial batch failure and conflict. Keep draft separate from confirmed state. Service acknowledgment and a later HA event are different moments; acknowledgment does not prove a device acted.

For timers test absolute deadline where applicable, visible countdown, expiry/cancel exactly once, duplicate starts, navigation, full reload, corrupt/stale session and simulated background delay. A snapshot roundtrip is not a reload test. Local countdown does not prove an HA timer started.

## Profiles and usability

Use relevant profiles, for example 390x844 and 393x852 touch phones, 1180x820 landscape tablet and 1440x900 desktop. Report engines actually exercised; profile names are not hardware claims. Viewport shrink/orientation are simulations; native keyboard behavior needs separate evidence.

Check keyboard reachability, visible focus, tab order, accessible names, modal containment/return, Escape, labels, disabled/loading state and errors. Include clipping, reflow, long labels, empty states, contrast and reduced motion when relevant. A 44 CSS px target is a useful touch preference, not a blanket WCAG AA requirement. Geometry tests are not accessibility certification.

Measure latency/redraw counts under controlled conditions. Only report distributions when enough sampling exists. A slow shared browser run does not establish poor phone performance. Investigate runaway listeners, polling, timers and detached nodes before changing architecture.
