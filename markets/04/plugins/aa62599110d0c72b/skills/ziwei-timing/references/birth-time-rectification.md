# Birth-time interview

Enter only when the user explicitly wants to estimate an unknown or disputed birth time. Work toward a useful best-fitting birth window through actual candidate-chart comparisons. This is an interpretive estimate, not historical verification; explain that briefly once, then conduct the interview. A corrected known time uses ordinary setup.

## Collect everything except time

Check that `get_birth_time_candidates`, `preview_profile_change` and `commit_profile_change` are actually available before collecting birth details. Read their exposed schemas. If unavailable, explain the observed connection limitation; do not simulate candidates by overwriting the saved chart. Apply the main Skill's website-link rule.

Whether a saved chart exists or not, ask in one compact group for the missing birth date/calendar, birth city/country or authoritative birth timezone, calculation sex input, and current residence city/timezone. Reuse details the user already supplied for this person in this conversation. Do not infer them from language or an unrelated saved chart. Time is deliberately the missing field: do not ask for a clock time or require family recollection before starting. Current residence is collected for a later complete profile preview; it is not a candidate-tool input.

Prefer an ordinary Gregorian date. Use [profile-setup.md](profile-setup.md) only for an actual calendar/place ambiguity, lunar input or DST issue. Give a short data-path notice once: supplied birth details go through this conversation and Ziweave. Do not add age reminders, repeated consent questions or an explanation of every later step. Interview answers stay in the conversation; do not send them as birth inputs or profile fields.

## Obtain and understand all 13 charts

Call `get_birth_time_candidates` once with the supplied `birth`, `detail:"full"` and a fresh opaque `operationId`. For this interview, start with all 13 windows and omit `hardTimeBound`; a vague recollection can inform later comparison without removing candidates. Proceed naturally without a pricing announcement or extra permission prompt.

`birth` includes calendar/date, birth timezone and calculation sex; include required leap-month fields for lunar input. Do not send a guessed time, residence, scores, interview answers or account/profile selectors. These alternatives change birth time, unlike hourly forecasts for a saved chart. Ordinary natal/timing calls cannot substitute for them, and a preview is not chart evidence.

Read the complete response before deriving questions. Require `kind:"birth-time-candidates-context"`, complete coverage, matching counts/indexes, consistent resolved inputs and engine policy, unique candidate IDs, explicit windows and twelve indexed natal palaces per candidate. A normal unrestricted date has indexes 0–12: early Zi 00:00–01:00, the two-hour windows from 01:00–03:00 through 21:00–23:00, and late Zi 23:00–24:00. Preserve server-supplied DST intervals and any proven unavailable window; do not invent missing evidence or shift civil dates.

Build a compact internal comparison covering **every candidate**:

`candidate/window → actual 命宮 (life palace) stars → actual 身宮 (body palace) stars → observable tendencies and counterexamples → current support, contradictions and priority`

Identify 命宮 by its semantic palace label and 身宮 by `isBodyPalace`; the chart's 身主 is not its body palace. Read both main and auxiliary stars and relevant brightness/mutagens from that candidate. If 命宮 is empty of main stars, retain its own evidence; any borrowed opposite-palace interpretation must identify that source. If 命宮 and 身宮 coincide, do not count the same feature twice. Keep a short chart trace for each question using exact returned star labels/keys, not ambiguous abbreviations, and check it against the response before using the distinction.

Translate combinations into concrete behavior contrasts, such as how someone first responds to an unstructured task, handles disagreement, or balances autonomy and stability. Do not assume 13 charts necessarily yield 13 distinguishable personalities. Group equivalent features for questioning while retaining each birth window; especially keep early/late Zi tied when the available distinguishing evidence is identical.

## Stage 1: narrow through life and body palaces

Ask one interview question per turn and wait for the user's actual answer. Select the next question from the largest meaningful differences among the current leading candidates, using a new dimension or a counterexample to the current favorite. Offer two to four balanced, plausible responses, allowing mixed answers, none, uncertainty or skipping. A concrete everyday situation is usually easier than chart terminology. Do not administer a fixed generic personality quiz or ask flattering traits that fit almost anyone.

After each answer, update relative support for **all returned candidates (normally 13)** using the actual palace combinations. Consistent behavior across different situations strengthens a match; a substantial counterexample lowers it. Distinguish longstanding patterns from temporary roles or moods. Mixed answers support their respective components; skipped/unknown answers are neutral. Rephrasing the same trait does not supply independent support. If the user corrects an answer, revise affected priorities instead of forcing the old favorite to fit or resetting all candidates to equal standing.

Actively rank relative fit. An answer can lower a candidate's priority without proving its historical impossibility; lower-ranked candidates remain available for reconsideration. **Do not require a birth record or hard clock bound before lowering priorities or proposing a shortlist.** Use comparative reasons rather than invented percentages, numerical scores or claims of calibrated accuracy.

After roughly **3–5 meaningful, discriminating answers**, present the primary, secondary and, when useful, third candidate with one short reason each. This is a working shortlist, not a declaration that the other windows are impossible. If one candidate is already clearly stronger across independent dimensions, say so; if actual evidence is tied, show the tie rather than arbitrarily selecting three. Nonanswers need not force a premature ranking.

The shortlist is the entry to Stage 2, not the final answer or a reason to offer saving. Even an initially strong favorite needs the broader comparison and the user's whole-chart fit check below. Keep progress visible in a sentence: what moved up or down and why.

## Stage 2: distinguish the shortlist through other palaces

Inspect the two or three leading candidates' **complete twelve-palace evidence already returned**. No new natal/timing/candidate call is needed to read another palace. Compare the same semantic palace in each candidate using its own indexes, actual stars and mutagens, rather than treating one candidate's slots as universal. Integrate its relation to the life/body pattern, including contrary evidence.

Choose two or three meaningful differences outside the features already used, then ask one new everyday situation question at a time. Relevant palaces might illuminate comfort in unfamiliar settings, how someone rests alone, boundaries in groups, home preferences, work roles or close-relationship communication. Choose from actual contrasts, not a fixed palace checklist; personal or sensitive topics are optional, and detailed medical, financial or traumatic history is unnecessary. Do not invent dated events from natal evidence.

Maintain a compact internal trace: `question → compared candidates → semantic palace and exact stars → distinguishing interpretation → answer and counterevidence`. A different palace or setting does not make the same autonomy, analysis or responsibility trait independent evidence. Avoid choosing a winner from a tenuous auxiliary-star distinction or generic descriptions shared by the leaders. Ask one or two genuinely new questions where supported, update the order, and retain ties when no meaningful distinction is available. Do not keep asking merely to force a larger apparent gap.

## Stage 3: check the strongest whole-chart portrait

When a candidate leads, synthesize its most distinctive two or three features from the whole chart and the interview. Include a concrete tendency and its possible difficulty or tradeoff, not an entirely flattering description or a replay of the user's own answers. Keep each feature traceable to the chart and retain major counterexamples. Use a short natural paragraph in the user's language, without a star catalogue; identify the proposed birth window and birth timezone without inventing minutes.

Ask how well this **overall description** fits: mostly fits, partly fits or does not fit, with room to say which part differs. Stop for the real answer. This is a fit check before the save offer, not evidence that the historical birth time is proven. Do not combine the first portrait and a request to save into the same question.

- **Mostly fits, with no major unresolved conflict:** state the preferred estimate and briefly retain any material alternative. Then proactively ask whether to use it in the saved chart. Agreement that the portrait fits is not agreement to preview or save.
- **Partly fits or unclear:** clarify the specific mismatch with one focused question before deciding whether it is a minor qualification or a reason to lower this candidate. Do not rewrite every contradiction into agreement or use a fit percentage as a calibrated likelihood.
- **Does not fit:** retain the concrete counterevidence and lower the candidate. Describe the next still-supported candidate's own strongest whole-chart features, ordinarily the second and then third, one portrait per turn with a real answer between them. Do not copy the first description with different times. If the new counterevidence also undermines the next candidate, acknowledge and revise the order; rejecting the first never counts as positive evidence for the second. Do not offer to save a rejected candidate.

If leaders are indistinguishable even across the relevant whole-chart evidence, show that tie rather than inventing different portraits or an arbitrary favorite. A preference to use one tied estimate can be a user choice, not a claim that the interview distinguished it. Stop whenever the user wants to stop.

## When all shortlisted portraits fail

Say plainly that none of the current descriptions fits well enough and withdraw the shortlist as a recommendation. Do not treat this as a user error, automatically restart, or cycle through all remaining portraits looking for assent. If the user has not already identified a clear mismatch, ask **one focused question** about the most unlike feature and, optionally, an ordinary counterexample. If they have already supplied it, use it instead of asking again.

Review which earlier answer or interpretation caused the wrong grouping. Reuse the full candidate set and all prior answers; distinguish uncertain answers, misleading descriptions and genuinely conflicting evidence. Re-rank the other windows against the actual mismatch while retaining rejected candidates' reasons. Ask a new discriminating question or offer one revised small set only if different chart evidence supports it. This is a bounded reconsideration, not an endless quiz; do not just polish the same rejected portraits until one sounds agreeable.

Clarify birth date/calendar, place/timezone or calculation input only when there is a concrete ambiguity or the user reports an error. Only an actual relevant input change needs a fresh candidate set. A failed personality fit does not itself justify re-fetching charts or repeatedly requesting the same birth details.

If there is no useful new distinction, or the revised comparison still produces no fitting candidate, finish as **unresolved** with the specific missing or conflicting evidence. Leave the saved chart unchanged and do not proactively propose saving. The user can pause, return with a concrete longstanding example, or optionally look for a birth record or family recollection; none is a mandatory hurdle to the interview, and no exact time should be manufactured.

## Adopt an estimate through the ordinary preview

The user must first agree to using a candidate after the fit check (or explicitly choose a tied estimate). A fit response, interview participation or rejection of alternatives does not initiate a profile preview by itself.

If they accept, call a fresh `preview_profile_change` with the collected profile details and the selected `timePrecision:"shichen"` / `timeIndex`. Do not invent a representative clock time. Show the exact normalized birth date/calendar, estimated shichen, calculation sex and birth/residence/display timezones, explaining that this creates or replaces the account's one saved chart. Keep the estimate visible in the explanation; do not invent a persisted certainty field. Stop and wait for a **later explicit confirmation of this preview** before `commit_profile_change`. The user's agreement to the interview, answer favoring a candidate or request to preview is not that final confirmation. A declined save ends without a write.

## Reuse and recovery

Keep complete candidate evidence in this conversation for all answers, rankings, explanations and language switches. A different leading candidate or corrected personality answer needs no new fetch. Changed birth date/calendar, birth timezone, calculation sex or policy requires a fresh complete set. A candidate-set ID is not a lookup or confirmation token.

Retry an interrupted identical operation with the same `operationId`. Only an explicit `USAGE_OPERATION_RESTART_REQUIRED` allows replacing an obsolete unfinished operation with a fresh ID; do not treat a generic conflict as permission to retry a different request. For `BIRTH_TIME_RATE_LIMITED`, explain briefly that another calculation can be tried shortly, then pause instead of looping or switching tools. If `USAGE_REPLAY_UNAVAILABLE` occurs and the complete evidence is actually missing from the conversation, a fresh operation may obtain it again. Candidate setup does not consume chart allowance, including input corrections and existing-profile reassessment; do not announce this unless asked or require a positive balance. Incomplete/failed evidence blocks chart-derived ranking until resolved. Candidate generation and interviewing never modify the saved chart; preview/commit use the ordinary two-stage contract.
