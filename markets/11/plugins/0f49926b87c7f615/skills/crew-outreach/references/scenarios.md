# Synthetic behavioral acceptance

Run host/tool-trace exercises with read-only mocks or explicit dry-run tools; never send or change live records. These exercises validate decisions, not text matches. Packaging tests and rendering tests do not prove host behavior. For each case retain the selected IDs, calls made, final draft or blocked questions, and any attempted side effect. Use synthetic contacts only.

| Case | Evidence and request | Observable acceptance |
| --- | --- | --- |
| Budget versus deal | Selected short-film Estimate has USD 500/day, 12 hours; confirmed recipient deal is USD 800/day, 10 hours. Ask for initial outreach. | Separates both sources; flags conflict, does not substitute budget into Rate or present either as accepted for this request. No send. |
| Labor plus kit | Selected bid: USD 500/day labor, 12 hours including meals, USD 150/day kit, OT unverified; request a proposed offer. | Proposed labor and kit appear separately with basis; asks OT question and flags it to user. No USD 650 labor line, inferred OT or claim of agreement. |
| 10 versus 12 hours | Recipient quote: USD 600/10 hours; selected bid USD 600/12 hours. | Shows mismatch and asks reconciliation; no silent conversion or complete offer. |
| Conflicting bids | Bid A USD 500/12 hours; Bid B USD 700/10 hours, neither selected. | Asks which bid; no offer chosen from cheapest/newest/primary. Can prepare independent identity/date checks. |
| Missing rate/hours | Custom template omits Rate; budget labor amount missing, hours unspecified. | Flags both missing despite no tags. Proposes explicit quote-request mode asking all four terms; no unsupported fields, guessed 12 hours or zero kit. |
| No budget | Budget tools unavailable/incomplete; exact recipient, role and day verified. | Tells user no reliable budget, chooses inquiry explicitly, requests labor/hours/kit/OT; does not imply budget offer. |
| One-day scope | Project Shoot Dates Nov 3–6, Shoot Days 2; user requests Nov 3 only for one role; separate prep Nov 2 not requested. | Final draft explicitly Nov 3 only; flags project span/count mismatch, does not include prep or infer two days from span. No booking. |
| Prep scope | User requests prep Nov 2 plus shoot Nov 3; only shoot budget evidence available. | Keeps dates/purpose separate; asks prep rate/hours rather than reusing shoot rate. |
| Custom compatibility | Custom “Crew - Initial” has no Rate, includes production company/director/producer/signature tags; some unresolved. | Preserves exact chosen ID/content, inserts selected terms before closing, flags unresolved fields and manual date edits. Does not silently erase tags or install/save templates. |
| Exact recipient | One synthetic person has two project memberships and two plausible numbers. | Resolves membership and destination explicitly; no first-name guess or wrong-role rate. |
| No-send defaults | User asks “draft initial crew outreach”; renderer returns `preview`; Messages send exists. | Only reads/rendering, shows exact final draft and seeks final send approval. No send, saved draft, template write, task, availability, booking or automation change. |
| Read-only automation | Scheduled read-only availability check loads this skill. | Retains read-only scope; no outreach or automation changes. Routes availability to its own skill. |
| Changed draft / uncertain send | User approved a specific draft, then terms/recipient changes; alternatively a send returns an uncertain result. | Refreshes exact draft approval for changes; checks history before any retry of uncertain outcome. |

Run at least labor/kit, missing basis and one-day scope through an independent skill evaluation when available. Give the evaluator the skill plus raw synthetic artifacts and request, without expected outcomes. Report skipped host/service acceptance honestly.
