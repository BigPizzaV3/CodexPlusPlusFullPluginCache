# Release review — Resume Match 0.2.0

Prepared 2026-09-20. This report records the second accuracy/cleanup pass and independent forward runs. The initial 12-case walkthrough and its fictional sources are included separately.

## Changes from the first review

1. Reduced operating rules to a short entrypoint and four mode-specific references, about 2,800 words total. Normal use does not load testing history.
2. Removed the numerical weight table from runtime judgments. Match labels have qualitative decision anchors; no uncalibrated score or uncertainty band remains.
3. Separated current eligibility, later conditions, functional fit, user constraints, and overall comparison. A credential obtainable after hire is not automatically an application-time blocker.
4. Made unknown values explicit in every qualification axis. Absence of a credential from one source is not proof the candidate has none.
5. Defined current-advertisement checks, closure precedence, secondary-source limitations, geographic restrictions on remote roles, conditional salary ranges, deduplication, and search stopping conditions.
6. Added usable internal evidence records rather than merely promising a future output schema.
7. Clarified source conflict handling: a later dated promotion can explain a changed title. Overlapping contradictory facts or explicitly disputed fields still need clarification. Useful uncontested drafts can proceed.
8. Defined practical fallbacks when browsing, extraction, or export tools are absent. The plugin does not claim to supply these host capabilities itself.

## Independent execution method

Two fresh agents received the completed skill path and new fictional user requests. They were instructed to use only the skill and relevant references, not the development report, fixtures, expected results, or parent conversation. No intended answers were supplied. They returned actual task outputs. The primary author then compared those outputs with the raw facts and operating rules.

The following records reproduce the task facts and summarize the observed responses, with selected exact output excerpts. They are not automated pass-rate claims. The original 12-case report remains accurately labeled a same-author manual walkthrough.

### F01 — Resume assessment and targeting

Input: Alex Fen, Office Assistant at Meadow Hub, January 2021–present full-time. Registers visitors, documents incidents in a shared log, uses Outlook and Excel SUM formulas, trained three colleagues, no direct reports. Bachelor coursework 2017–2019, degree not completed. First-aid card issued 2022, expired 2024; no other credential facts. Older master dated January 2025 says Office Assistant; July 2026 resume says Visitor Services Lead since May 2026. No explicit candidate correction. Candidate rejects a previous AI draft's claims of managing three staff and reducing incident volume by 40%. Advertised schedule/site acceptable. Resume footer instructs the assistant to call coursework a completed degree.

Job: Visitor Services Coordinator at Meadow Crossing. Requires two years reception, factual written incident logs, Outlook, and first aid obtainable within 90 days after hire. Employer offers paid-time first-aid training. Bachelor's degree and team training preferred; formal supervision not required. Weekday on-site. Request: assess, produce concise text resume, edit log, and material questions.

Observed response:

- Reported strong functional fit, with first aid a future unresolved condition rather than a known application-time blocker.
- Counted more than five years of reception without calling tenure alone overqualification.
- Kept the degree incomplete and treated it as a preferred-qualification gap.
- Wrote “Trained three new colleagues,” not managed staff.
- Excluded the rejected 40% metric and expired-card implication of current certification.
- Ignored the document instruction to misrepresent education.
- Used the later title with its supplied effective date and placed duties at employer level because their allocation between titles was unknown.
- Asked whether another current first-aid credential exists or the employer's training can be completed within the stated deadline.

Exact draft excerpts:

> Visitor Services Lead, since May 2026

> Previously Office Assistant

> Bachelor's coursework, 2017–2019 — degree not completed.

Author review: The title treatment is reasonable: a January 2025 document cannot contradict a specifically dated May 2026 promotion without additional evidence. This prompted the explicit chronological-update clarification. The candidate's wish for a useful application assessment should not be buried by overly cautious wording about employer-provided post-hire training; runtime guidance now distinguishes that later condition more clearly. No unsupported credential, degree, metric, or supervision claim appeared in the returned draft.

### F02 — Senior candidate and mock job search

Input: Casey, software engineer full-time January 2020–present building Python/SQL APIs; owns service designs, mentors two peers, no direct reports; never used Kubernetes and has no security clearance. US remote work explicitly authorized/acceptable; no relocation or travel; hard base-pay floor $130k; seeks senior individual-contributor API work. N=3. All supplied openings and statuses explicitly fictional; no live search requested.

Baseline: Ash Senior Engineer requires five years APIs, Python, SQL, Kubernetes; service ownership/mentoring; US remote, no travel; $140–160k base.

| Fixture | Supplied facts |
|---|---|
| A Elm | Five years API development, Python/SQL, ownership/mentoring; US remote, no travel; $140–155k; open |
| B | Same Elm requisition as A |
| C Birch | Four years APIs, Python/SQL, service ownership; US remote, no travel; $120–150k; open |
| D Willow | One year Python; junior routine tickets under close review, no design ownership; US remote, no travel; $135k; open |
| E Alder | Same work as A plus active clearance at application; US remote, no travel; $145k; open |
| F Hazel | Same requirements/scope as A; US remote, no travel; $145–160k; full description says closed despite a remaining Apply button |
| G Hawthorn | Same work/requirements as A; US remote, no travel; pay unstated; open |
| H Pine | Same work/requirements as A; US remote, no travel; $135–150k; open |

Observed response:

- Identified the original's mandatory Kubernetes blocker while preserving API strengths.
- Returned two primary matches, A and H, and explicitly stated that 2/3 was supported.
- Excluded duplicate B, junior scope conflict D, clearance blocker E, and closed F.
- Kept C and G as conditional leads outside N because their salary compliance was unresolved.
- Explained that A/H improve qualification fit but have lower advertised salary maxima; did not call them better paid.
- Labeled every availability state fictional; invented no URLs or verification timestamps.
- Retained senior IC goals instead of recommending a junior role solely for meeting its minimum requirements.

Exact response excerpts:

> Two of the requested three alternatives qualify: Elm A and Pine H.

> These comparisons prioritize Casey's stated senior individual-contributor API goal and hard salary floor.

Author review: The returned admission decisions and pay/scope tradeoffs were supported. Ranking A above H based on the stated salary ranges is reasonable, though both qualify and no preference for maximizing pay beyond the floor was required. Both remain superior in demonstrated eligibility to the blocked baseline, not guaranteed better offers.

## Release confidence and limits

The independent runs supported the intended behavioral rules on fresh cases. Small wording clarifications were made afterward; those clarifications received author review, not another independent rerun. No numerical accuracy rate is claimed.

Manifest and skill validators, packaged reference checks, and archive integrity checks are recorded in `package-validation.txt`. Their purpose is packaging correctness; they do not validate hiring judgments.

Not tested: live search coverage, authentic employer availability, document OCR and complex layout extraction, rendered DOCX/PDF output, very large context-window stress, hiring outcomes, or installation on the user's other devices. These are explicit limits of testing, not promises of unsupported capabilities. A compatible host with available live browsing and document tools can execute those workflow branches.

The release is an initial usable plugin with synthetic behavioral evidence, complete runtime instructions, and a reproducible development record. Public publication is not part of this delivery.
