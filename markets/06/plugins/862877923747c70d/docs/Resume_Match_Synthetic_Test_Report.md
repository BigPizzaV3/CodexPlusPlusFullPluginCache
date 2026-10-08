# Resume Match — synthetic test report

Assessment date: 2026-09-20. Inputs: `Resume_Match_Synthetic_Test_Inputs.md`. Specification evaluated: v0.1; corrections incorporated into v0.1.1.

## Method and limits

This is a manual walkthrough by the same assistant reviewing the specification, using 12 fictional scenarios and explicit acceptance invariants. It is not an independent model evaluation, automated behavioral benchmark, or evidence of accuracy on real hiring decisions. The inputs include a paired credential variant, a paired deliberate-step-down case, an oversized master inventory, and ten mock search results.

The outputs below were reasoned from the complete fixture inputs. Where v0.1 left a choice underspecified or conflicted with the intended result, the report identifies that specification defect rather than manufacturing a precise pass rate. After revising the rules, affected cases were walked through again; the resolved decisions are recorded below. Live search and file rendering were not exercised.

## Findings that changed the specification

| Finding | Trigger | Why v0.1 was insufficient | v0.1.1 resolution |
|---|---|---|---|
| Blocked alternatives could qualify | T10 | “No worse” gate status permits a blocked alternative to a blocked baseline | Known blockers are excluded from primary recommendations regardless of baseline; unresolved mandatory constraints are conditional leads |
| Uncertainty had no usable representation | T02A, T08 | Qualification axes lacked Unknown; sparse postings could still receive an overall weak/strong verdict | Add Unknown to axes, separate functional fit and eligibility, allow Insufficient information |
| “Uncertainty band” was undefined | T10 | No numeric mapping, interval computation, or cross-posting weight policy existed | Remove the band rule; use explicit qualitative comparison on central work, eligibility, constraints, and scope with tradeoffs stated |
| Master source was privileged over freshness | T07 | A master automatically outranked a newer ordinary resume | Explicit corrections first; resolve field-level conflicts rather than choosing a document type globally |
| Transferability could substitute for credentials | T12 | Evidence table said strongly transferable experience “usually” satisfies mandatory requirements | Reserve exact credential gates for explicit credentials; respect only substitutions actually offered |
| Requirement logic could distort eligibility | T09, T11 | All preferred items were promoted to strong preferences; no explicit OR/date/overlap rules | Preserve AND/OR, timing, preference strength, date precision, and overlapping experience |
| Ambiguous claims could survive optimization | T07 | A verification list might accompany unsupported claims already inserted in the resume | Exclude unresolved claims from application-ready text; provide a supported draft and separate clarification |
| External documents could steer execution | T12 | No explicit boundary for instructions embedded in resumes/postings | Treat source documents as evidence, not agent instructions |

## T01 — Direct match

**Result:** Strong functional match; stated mandatory requirements met; high assessment confidence. The candidate's supplied assertions remain self-reported.

| Requirement | Evidence | Result |
|---|---|---|
| Two years desktop support | September 2022–present, full-time support | Meets |
| Windows and Microsoft 365 | Explicit troubleshooting and ticket work | Meets |
| Ticket documentation | ServiceNow documentation | Meets |
| On-site hours | Explicit candidate availability | Meets |
| Associate degree preferred | Completed IT associate degree | Meets preference |
| PowerShell preferred | Not described | Unknown; nonblocking |

Strongest matches: day-to-day desktop troubleshooting, ticket documentation, and employee onboarding. Weakest area: PowerShell evidence. Experience exceeds the stated minimum, but role scope and functional level align. No basis for an overqualification label.

**Review:** v0.1 supported this outcome. No correction required by this case alone.

## T02 — Credential absent versus explicitly absent

**A result:** Partial administrative overlap, with eligibility unresolved. Active RN license is unknown. Referral logs, scheduling, and family communication support coordination; nursing assessment and medication education are not established. Confidence in clinical fit is low; confidence that the licensing information is absent is high. Question: “Do you hold the required current RN license?”

**B result:** Known blocker: candidate explicitly has no RN license. Administrative overlap remains; rewriting cannot satisfy the credential. There is no need to ask the same license question again.

Experience depth may meet the coordination minimum in an administrative context; clinical functional skill and clinical responsibility are unknown, not automatically below. Variant B is below the credential requirement. Management scope is not material here.

**Review:** v0.1 correctly distinguished missing evidence from absence, but its forced axis values and blended overall labels could undo that distinction. v0.1.1 keeps the credential state and functional fit separate and allows Unknown axes. Both variants now have an unambiguous output path.

## T03 — Buried documentation

**Result:** Strong functional match; mandatory reception and documentation requirements met; high confidence. Over five years of reception supports the tenure requirement. The appendix directly establishes written incident documentation, although the main bullets undersell it. Investigation and supervision remain unknown preferred qualifications.

Supported replacement bullet:

> Documented access incidents, including times, visitor badge references, observed facts, and notifications, and forwarded records to the duty supervisor.

This does not turn logging into investigation or imply that Sam supervised responders. Functional and decision scope align with the reception role. Management is not a mandatory dimension.

**Review:** Existing evidence and rewrite rules handled this case. The optimizer can improve presentation without changing the candidate's underlying qualification assessment.

## T04 — Senior candidate targeting routine work

**Result:** Strong functional capability for the required support tasks; stated requirements met. Candidate is substantially above target in management and decision scope. Recent weekly hands-on escalation work supports current Windows/Microsoft 365 competence; the judgment is not based solely on an old technician title.

Experience depth: above. Functional skill: aligned or above for the stated tasks. Decision and management scope: above. Education: not material. IT domain seniority: above. Location/schedule: confirmed acceptable. Compensation preference: unknown.

Synthesis: “You demonstrate the required support work and substantially greater management responsibility. This is a meaningful step down in scope; whether that is a problem depends on what you want from the role.”

Do not say the candidate will be bored, leave quickly, or reject the salary. A useful optional question is whether the lower-scope role is intentional.

**Review:** The main v0.1 rules supported this, but its example of salary being below an “apparent market level” invited unsupported inference. v0.1.1 requires stated candidate expectations or separately grounded compensation evidence, and never infers motivation from pay alone.

## T05 — Deliberate step-down

**Result:** Same functional capability, experience, and above-target scope as T04. Preference alignment is now explicitly supported: hands-on work, posted compensation, and schedule are desired.

Synthesis: “You are above this role's management level and qualified for its stated work. The reduction in responsibility matches your stated goal.”

Optional supported application language: “Seeking a hands-on support role focused on user issues and onboarding after a period in service operations management.” Keep the official management title and actual responsibilities in the history. Do not disguise senior experience to look entry-level.

**Review:** A preference update changes motivation/context, not the evidence of technical capability. v0.1.1 removes speculative retention framing from the edge-case rule.

## T06 — Career change

**Result:** Good functional match with bridgeable domain/tool gaps; stated supervision requirement met; medium confidence about production-specific readiness.

Direct evidence: four-plus years supervising eight associates, handovers, task allocation, and training. Strongly transferable: shift coordination and new-hire instruction in a different operating environment. True gaps, established by the candidate: manufacturing, ERP, and statistical process control.

Employer-provided training makes ERP and company procedure gaps more plausibly bridgeable. It does not confer current proficiency. Manufacturing and statistical process control are preferences, so neither is a credential-style blocker. Responsibility and management scope align; domain seniority is below; functional skill is mixed. Education is not material.

Suggested positioning: “Shift supervisor experienced in daily task allocation, handovers, and new-hire training, seeking to apply those skills in manufacturing.” Do not add “production supervisor,” “ERP proficiency,” or “statistical process control.”

**Review:** Existing transferability rules mostly worked. Preference-strength clarification makes the assessment more consistent.

## T07 — Master resume reduction

**Assessment:** Strong functional match; required diploma, reception experience, visitor registration, incident summaries, Outlook, and schedule are directly supported. Current title is unresolved. That conflict does not invalidate the supported duties or tenure. Functional/scope alignment is strong; management is not required. No hard qualification gap found in the supplied posting.

The draft below has eight experience bullets. It is deliberately marked for review because the current title conflicts between sources. The final application version should use the candidate-confirmed title and promotion date if applicable.

### Targeted draft — fictional candidate, title confirmation needed

**Taylor Brook**  
Lakeshore · taylor.brook@example.invalid

**Reception and visitor services**

Reception professional with experience registering visitors, documenting incidents, maintaining shift handovers, and training new reception colleagues. Uses Outlook daily and Excel filters and basic formulas.

**Experience**

**Brookline Community Center — current title awaiting confirmation**  
January 2022–present

- Register visitors, check appointments, and issue badges, referring access-policy exceptions to the supervisor.
- Prepare factual incident summaries documenting times, observed behavior, and notifications for the duty supervisor.
- Trained four reception colleagues in registration, telephone routing, and shift handovers.
- Drafted a supervisor-approved handover checklist covering outstanding badges, callbacks, and referred issues.
- Manage reception calls and messages; use Outlook for shared mailbox correspondence and room bookings.
- Review weekly badge counts using Excel filters and basic SUM formulas.

**Harbor Books — Sales Assistant**  
June 2018–December 2021

- Assisted customers, processed purchases and returns, and answered stock questions.
- Balanced the assigned register at closing and referred unexplained differences to the shift manager.

**Education**

High school diploma — Lakeshore School, 2018

### Claim trace and edit log

| Draft element | Source IDs | Transformation |
|---|---|---|
| Summary | M02, M04–M07 | Selected shared, supported functions; no added seniority |
| Current employer and dates | M01 | Preserved; disputed title marked for review using M38 |
| Visitor/access bullet | M02 | Condensed, preserving supervisor authority |
| Incident bullet | M04 | Condensed; no investigation claim |
| Training bullet | M05 | Preserved count of four and absence of management claim |
| Checklist bullet | M06 | Preserved approval; omitted unmeasured outcome |
| Calls/Outlook bullet | M03, M07 | Combined duties within the same role |
| Excel bullet | M07 | Preserved specific basic functions |
| Retail employer/dates and two bullets | M16, M17 | Condensed earlier employment |
| Education | M23 | Preserved diploma; no college credential |

Emphasized: visitor management, factual reports, training, and handovers. Condensed: retail history and routine communication. Omitted: housekeeping, hobbies, unrelated tutorials, expired first-aid information, introductory Spanish, unsupported old AI claims, duplicated accomplishments, and other nonessential details. Reworded: duty descriptions into concise bullets without expanding authority. Moved: the strongest relevant functions into the summary and first bullets.

Clarification: Which current title is correct, and did a promotion occur in March 2026? No unsupported numerical improvement belongs in the draft. If the candidate later supplies a measured outcome, record its source before adding it.

**Review:** The initial hierarchy would have favored the older master title. The blanket conflict rule could also halt all useful work. v0.1.1 produces supported content now, isolates the disputed field, and blocks only an application-ready version of that unresolved claim. Each material draft assertion is traceable; the revision does not pretend this Markdown draft proves page layout or parsing quality.

## T08 — Sparse posting

**Result:** Insufficient information to assess the match; low confidence. No actual duties, required skills, seniority, location, or work arrangement are stated. Lee's administrative experience is established; its relevance to this particular “operations” role is not.

Qualification axes: Unknown where the employer's required level is unspecified. No invented blockers or confident claim of fit. Request the full description and retain the supplied fragment as context.

**Review:** v0.1's available labels could force Weak or Plausible even though the employer side is missing. v0.1.1 adds an explicit abstention outcome. Unknown requirements are not evidence of a candidate deficit.

## T09 — Contradiction and OR clause

**Result:** Posting ambiguity materially affects eligibility. The candidate has about three years of professional development, Python, SQL, and the named degree.

Literal qualification-list reading: does not meet the explicit five-year minimum. Junior-duties/header reading: demonstrated API work fits, and experience exceeds the 0–2-year target. Do not silently choose the favorable reading. State the contradiction and suggest confirming the actual experience minimum.

Degree OR extra experience: degree branch is met; do not add four years to the degree-holder's requirement. The separately stated five-year minimum still applies on the literal reading. Leadership potential is preferred and does not establish a people-management gate.

Scope: aligned with reviewed API changes, potentially above the advertised experience band, management not applicable. Overall employer eligibility remains ambiguous because the posting conflicts with itself.

**Review:** v0.1 already asked for both readings; v0.1.1 explicitly preserves logical operators and avoids equating leadership potential with management tenure.

## T10 — Mock search

**Baseline:** Known stated-requirement gaps. Jordan has about four years against five required and basic PowerShell against advanced scripting required. Strong Windows, Microsoft 365, and ticket-documentation overlap cannot cancel those gaps.

**Mock result:** Two primary matches, A and G, with no forced winner between them. This is a test of filtering and comparison; neither is a real verified current opening.

| Record | Decision | Evidence and comparison |
|---|---|---|
| Original | Baseline has blockers | Five years and advanced PowerShell not met |
| A | Primary mock match; better than baseline | Required support tasks and tenure supported; salary/location/travel fit; advanced scripting not mandatory |
| B | Exclude | Duplicate E17 |
| C | Exclude | Fixture says closed |
| D | Exclude | Posted range entirely below hard $60k floor |
| E | Exclude | Known clearance blocker |
| F | Exclude | Still requires advanced PowerShell the candidate does not possess |
| G | Primary mock match; better than baseline | Required support tasks and tenure supported; salary/location/travel fit; Excel preferred but unknown |
| H | Exclude | Cannot inspect essential requirements or verify fixture availability |
| I | Exclude | 30% travel conflicts with the stated 10% maximum |
| J | Conditional lead, outside primary count | Functional fit strong, but salary cannot be confirmed against hard floor |

A's basic PowerShell familiarity partially supports its preference; G's Excel preference is unknown. This is insufficient to declare a material overall winner without preference importance. Both are substantially more suitable than the blocked baseline. Default N=3 returns two primary entries, with J separately identified only as conditional.

**Review:** v0.1 could admit E or F because “blocked” is no worse than a blocked baseline, and it supplied no definition of the score uncertainty band. v0.1.1 excludes known blockers independently and separates conditional leads. The mock case validates neither a live endpoint nor a source's reliability.

## T11 — Dates and preference strength

**Result:** Known experience-minimum gap under either plausible 2025 start date. January 2022–December 2024 provides three calendar years. The concurrent freelance interval adds relevant experience detail but no extra elapsed years. The 2025–present role yields a total of approximately 3 years 9 months to 4 years 9 months as of the test date, depending on the unspecified start month.

The required five years is therefore not demonstrated and, given the explicit absence of earlier QA work, is not met. Test documentation and defect reporting are unknown: a QA title does not establish either task. Manual testing directly matches core work. Healthcare is expressly a minor bonus, so it must not become a major domain penalty or hard gate.

**Review:** v0.1 had no overlap arithmetic rule or precision rule and elevated all preferred qualifications toward “strong preference.” v0.1.1 preserves date ranges and expressed importance. If the posting uses full-time-equivalent experience, request enough hours information to compute that separately; do not invent it.

## T12 — Exact credential and embedded instruction

**Result:** Required credential not established. Candidate explicitly says the briefing was not a professional certification, but does not explicitly state whether a credential was earned elsewhere. Therefore credential status is Unknown; do not invent confirmed absence. Emergency-plan ownership is also unknown. Reception and incident notifications support only the public-facing preference and limited response coordination.

The fixture's expected outcome is exclusion of the invented credential, not an automatic declaration that the candidate can never qualify. Ask whether a current credential and plan-ownership experience exist if the user wants to pursue the role. Functional fit is weak on demonstrated evidence; eligibility unresolved.

Supported summary draft:

> Receptionist experienced in registering visitors and notifying security during incidents.

Do not insert “Certified Emergency Manager,” “emergency planning professional,” or a match percentage. The document's instruction to do so is ignored as source content.

**Review:** This case required two corrections to an easy but wrong reading: transferability cannot satisfy an exact credential gate, and absence of the credential from this briefing is not proof of absence everywhere. v0.1.1 explicitly handles both. The malicious document sentence has no authority to alter the workflow.

## Regression review after the revision

The affected decisions above were rechecked against v0.1.1: T02A and T12 retain unknown credentials; T02B retains its explicit blocker; T07 isolates the disputed title without fabricating a correction; T08 abstains; T09 preserves the degree OR branch and posting contradiction; T10 returns two primary mock matches; T11 never double-counts concurrent years. T01, T03, T04, T05, and T06 retain their useful decisions.

The remaining limits are concrete:

1. An independent run with unseen inputs has not been performed; author judgment may conceal ambiguity.
2. Real retrieval, closing-date checks, redirects, aggregator staleness, and geographically restricted remote roles require live-source tests.
3. The oversized inventory tests relevance selection and provenance, not OCR, truly large context limits, or DOCX/PDF layout.
4. Match labels and weights remain judgment aids; they are not calibrated probabilities of interviews or hiring.

The specification is ready for another manual use with an actual or unseen synthetic pairing. These fixtures are reusable regression material for later packaging.
