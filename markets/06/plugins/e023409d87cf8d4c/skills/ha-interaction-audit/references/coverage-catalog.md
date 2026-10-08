# Coverage catalog

Select by product behavior and risk. These are scenario families, not claims that tests already exist or have run. Split composite rows into individually observable assertions. Use stable IDs such as `editor.focus.hass-updates.phone`. Record every included/excluded family and its rationale before execution. An irrelevant feature can be skipped with a reason; an unavailable required feature is blocked.

## Foundation and live-update behavior

| Family | Interaction or condition | Required observation |
| --- | --- | --- |
| BOOT-01 | Fresh fixture mount | Actual loader/component/version matches manifest |
| BOOT-02 | Cold load then owned warm reload | Required resources present; no stale code or duplicate definitions |
| BOOT-03 | Initial empty/loading/error state | Useful state shown; no accidental mutation |
| BOOT-04 | Missing or unavailable entity | Honest unavailable UI; controls follow intended availability |
| ISO-01 | Inert unmatched GET and POST probes | Rejected with recorded attempts; no upstream forwarding |
| ISO-02 | Raw WS/beacon/worker probes | Blocked before network or explicitly mocked |
| ISO-03 | Save/toggle in mock fixture | Exact target/payload and expected number of intents |
| ISO-04 | Unrecognized API route | Explicit rejection; no generic success fallback |
| STATE-01 | Unrelated paced HA updates | Draft, focus, expanded sections and route remain stable |
| STATE-02 | Relevant state/attribute update | Correct visible field updates without draft overwrite |
| STATE-03 | Burst + repeated redraw separately | User state survives; update counts recorded |
| STATE-04 | Disconnect/reconnect + fresh snapshot | Stale/loading indication, no replayed unwanted action |
| STATE-05 | Entity removed/reintroduced | Graceful absence and correct recovery |

## Forms and selection

| Family | Interaction or condition | Required observation |
| --- | --- | --- |
| FORM-01 | Type beginning/middle/end of text | Value, draft, deepest focus and caret/selection agree |
| FORM-02 | Type while updates/redraws occur | No lost/duplicated keystrokes or unexpected blur |
| FORM-03 | Select and replace text; delete; paste if supported | Selection and final value correct; input mode labeled |
| FORM-04 | Number empty/zero/min/max/out-of-range | Validity, clamping and error contract correct |
| FORM-05 | Unicode, apostrophes, long labels/multiline | Text preserved and safely displayed |
| FORM-06 | Toggle details repeatedly through redraw | Expanded state retained; visible content usable |
| FORM-07 | Native/custom dropdown, keyboard selection | Chosen option and focus retained; unavailable options handled |
| FORM-08 | Multi-select rapidly; clear all | Each stable ID selected exactly once; no lost taps |
| FORM-09 | Range drag preview, release, cancel, Apply | Draft versus committed values; no premature live-intent generation |
| FORM-10 | Save then inspect store/reopen | Exact payload, one logical save, persisted mock values |
| FORM-11 | Edit then cancel/back/dismiss | Correct draft policy; unchanged store where cancellation discards |
| FORM-12 | Invalid save; failed save; retry | No false success; error readable; recoverable draft retained |
| FORM-13 | Double-submit and slow response | Duplicate handling follows contract; no duplicated record |
| FORM-14 | Concurrent server edit/409 | Conflict handling visible; no silent overwrite |
| FORM-15 | IME/composition/native date picker | Test if supported; otherwise explicit device coverage gap |

## Navigation, scroll, touch and layout

| Family | Interaction or condition | Required observation |
| --- | --- | --- |
| NAV-01 | Every primary route and active tab | Correct route, selected tab and meaningful content |
| NAV-02 | Filter/search/scroll, open item, app Back | Filter values, route and prompt/settled return position |
| NAV-03 | Back then immediate new item/search/scroll | New intent wins; stale restoration cannot change route |
| NAV-04 | Browser Back/Forward and deep link | Correct history state and target, if supported |
| NAV-05 | Navigate with pending response/debounce | Late work cannot resurrect old route or draft |
| NAV-06 | Reload and malformed/old saved session | Intended persistence; safe fallback, no crash |
| SCROLL-01 | Document top/middle/bottom + updates | No unexplained jump; content remains reachable |
| SCROLL-02 | Editor/modal scroll + redraw | Correct container restored without page displacement |
| SCROLL-03 | Horizontal week/tag strip touch swipe | Expected horizontal motion; bounded unintended vertical drift |
| SCROLL-04 | Gesture begins on bottom nav | Nav and page behavior match intended contract |
| SCROLL-05 | Resize, orientation, viewport shrink | Nav bounds, visual viewport, scroll and input visibility |
| TOUCH-01 | Nested row/button tap | Exactly one intended transition/request |
| TOUCH-02 | Short tap versus long press/drag | Tap not misclassified; drag only after intended threshold |
| TOUCH-03 | Reorder then cancel/save/reload | Stable IDs/order; no lost or duplicate items |
| TOUCH-04 | Drag while list updates | Correct target and recoverable cancellation |
| LAYOUT-01 | Phone widths, tablet and desktop | No document overflow/clipping or obscured controls |
| LAYOUT-02 | Modal/nav/safe-area boundaries | Correct stacking, bottom clearance and content padding |
| LAYOUT-03 | Long lists, delayed images and empty results | Stable readable layout and reachable controls |
| A11Y-01 | Tab/Shift-Tab/Enter/Space/Escape | Logical focus, no trap, correct activation/dismissal |
| A11Y-02 | Open/close modal | Focus enters, stays appropriately contained, returns |
| A11Y-03 | Labels, names, focus, errors, target geometry | Evidence of usability; no unsupported compliance claim |
| A11Y-04 | Zoom/reflow, contrast, reduced motion | Applicable checks identified with tool/device limits |

## HA control, automation and persistence contracts

| Family | Interaction or condition | Required observation |
| --- | --- | --- |
| HA-01 | Switch/button action | Exact domain/service/entity/target and one intent |
| HA-02 | Acknowledgment then delayed state event | Pending versus confirmed UI correctly distinguished |
| HA-03 | Failed action then state refresh | Revert or error contract, no false device success |
| HA-04 | Disabled, hold, unavailable, busy state | UI gating and backend contract agree in simulation |
| HA-05 | Schedule crossing midnight/DST/timezone | Model boundary correctness with explicit test clock |
| HA-06 | Queue/running/cancel/retry flow | Valid state transitions and no duplicate dispatch in model |
| HA-07 | Long-running action + navigation | Progress remains consistent, no accidental resubmit |
| TIMER-01 | Start once and inspect visible countdown | Immediate intended start and elapsed-time change |
| TIMER-02 | Pause/resume/cancel/expire when supported | Correct deadline and exactly-once completion |
| TIMER-03 | Navigate, redraw, full reload, resume | Same deadline where persistence is promised |
| TIMER-04 | Stale/corrupt saved timer or clock change | Explicit fallback; no repeated stale alarm |
| LIFE-01 | Repeated mount/unmount and route cycles | No escalating listeners, intervals or duplicate writes |
| LIFE-02 | Logout/session loss/user permissions | Honest failure; no privileged bypass or hidden data |

These model/fixture tests do not prove real valves, locks, heating, schedules or notification delivery operated. Read-only trace/log verification can support an integration conclusion separately. Real actuation tests require actual authorization and safeguards appropriate to the action.

## Add-on and data-heavy workflows

| Family | Interaction or condition | Required observation |
| --- | --- | --- |
| DATA-01 | Search, combined filters, clear, favorites | UI selection and actual result identities agree |
| DATA-02 | Create/edit/delete with confirm/cancel | Mock store and intent count reflect the contract |
| DATA-03 | Grocery/todo add/check/delete/undo | Stable IDs and correct service arguments |
| DATA-04 | Meal planning/calendar synchronization | Correct dates/timezone/records; all writes mocked |
| DATA-05 | Generate/replace/apply a suggested plan | Enough alternatives; expected no-alternative path tested separately |
| DATA-06 | Ingredient/quantity/serving scaling | Correct underlying values and no unintended scroll jump |
| DATA-07 | Import/file/URL/Discover/source filters | Valid and invalid inputs; external requests explicitly mocked |
| DATA-08 | Batch partial failure/cancel | Per-item result and recovery; no silent data loss |
| DATA-09 | Ingress/session expiry/offline | Recoverable error; no unauthorized endpoint fallback |
| PERF-01 | Large realistic synthetic dataset | Measured response/DOM cost, not arbitrary benchmark claims |
| PERF-02 | Repeated refresh/navigation/redraw | No obvious runaway work; resource observations recorded |

## Advanced behavior and evidence challenges

Apply these families to relevant high-consequence journeys. They specify distinct proof obligations; do not inflate executed assertion counts simply by attaching several family IDs to one result.

| Family | Interaction or condition | Required observation |
| --- | --- | --- |
| MODEL-01 | Independent route/draft/commit state model | Observable UI and mock store match each legal transition |
| MODEL-02 | Seeded legal action sequences | Guard validity, seed, concrete actions and per-step checks recorded |
| MODEL-03 | Invalid transition attempt | User-visible rejection and no forbidden state or write |
| MODEL-04 | Inverse action and roundtrip | Select/deselect or edit/cancel returns to the promised state |
| MODEL-05 | Irrelevant data reorder or unrelated update | Stable record identity and unchanged relevant outcome |
| MODEL-06 | Failure reduction and replay | Same oracle signature from fresh state, not an unrelated failure |
| RACE-01 | Read A then B; deliver B then A | Latest intent remains authoritative after both deliveries |
| RACE-02 | Save acknowledgment versus later HA state | Pending, accepted and confirmed states distinguished |
| RACE-03 | Commit succeeds but response is lost | No false rollback claim or duplicated blind retry |
| RACE-04 | Cancel/unmount before response | Late completion cannot revive discarded UI or new session |
| RACE-05 | Action at debounce/restore boundary | Test before, at, and after boundary with measured timing |
| RACE-06 | Chosen three-way interaction | New input plus redraw plus pending response preserves contract |
| TIME-01 | Running control after immediate feedback | Status remains usable throughout a sampled real-time window |
| TIME-02 | Timer expiry at t-1, t, t+1 | Boundary result and exactly-once completion consistent |
| TIME-03 | Clock advances while callbacks suspended | Absolute deadline, catch-up and stale-notification policy |
| TIME-04 | Cancel races with expiry | No unwanted completion after successful cancellation |
| TIME-05 | Wall clock jump and timezone change | Wall and monotonic semantics explicitly distinguished |
| TIME-06 | Long-duration staged soak | Actual observed duration, gaps, resource slope and checkpoints |
| RECOVER-01 | Two tabs edit same stable record | Conflict/version policy and no silent cross-tab corruption |
| RECOVER-02 | Reload with write pending | Honest ambiguity, recoverable draft and no duplicate actuation |
| RECOVER-03 | Storage unavailable/full/corrupt | Clear fallback and no false persistence claim |
| RECOVER-04 | Session schema upgrade/downgrade | Compatible restoration or safe explicit discard |
| RECOVER-05 | Reconnect with duplicate/stale events | Correct ordering/deduplication and no unwanted dispatch |
| RECOVER-06 | Role change or entity removal mid-edit | No stale enabled control or claimed successful unauthorized save |
| ORACLE-01 | Deliberate duplicate listener in fixture | Exact transition/write-count assertion fails for that cause |
| ORACLE-02 | Deliberately hidden/clipped timer | Visibility oracle detects it despite valid countdown state |
| ORACLE-03 | Deliberate stale response overwrite | Latest-intent oracle fails with response order evidence |
| ORACLE-04 | Clean reference and broken variant | Baseline passes, mutant reaches action then same intended oracle fails |
| ORACLE-05 | Missing control or unvisited branch | Missing evidence stays blocked/not-run, never inferred pass |
| ORACLE-06 | Repeat runs and intermittent outcomes | First failures and all attempts retained; no retry-to-green |
| OBSERVE-01 | Stop/cancel behind sheet or nav | Actual reachable recovery action, not mere DOM presence |
| OBSERVE-02 | Native viewport and CSS occlusion | Bounds, ancestor visibility, sampled hits and screenshot agree |
| OBSERVE-03 | Eventual success after transient failure | Separate always-held invariant from eventual success |
| OBSERVE-04 | Long gaps in evidence sampling | Inconclusive sustained-behavior claim, even if endpoints pass |
| OBSERVE-05 | Repeated mount/listener/timer cycles | Stable resource ownership and no accumulating actions |
| OBSERVE-06 | User intent to usable feedback latency | Defined start/end, cold/warm split, budget and measurements |

## Choosing rigorous passes

Keep isolation, active-source identity, core navigation and the user-reported defect in the fast suite. Deep pass boundaries should follow independent journeys, for example editor/control state; data workflows; navigation/device geometry; and error/race/lifecycle scenarios. Each starts from a fresh seed. Choose a pass budget below the observed provider deadline with room for cleanup, often tens of seconds. Do not encode “30 seconds” or “25 minutes” as a platform guarantee.
