---
name: capital-readiness-assessment
description: Assess a company's capital readiness with re:cap when the user asks to assess a company or website, what they can raise and on what terms, whether they are fundable, which financing route fits, or what is holding their financing back - never as a website, SEO, or UX audit. Covers both the re:cap connector and the assessment page open in a browser tab.
---

# Capital Readiness Assessment

## Which surface you are on

The same assessment is reachable two ways. Both take the same parameter names
and the same value shorthand; they differ only in how a session is addressed.

**The connector** - `start_capital_readiness_assessment` is callable. Mint the
assessment yourself:

- Call it with the company website. Most conversations open without one, so ask
  for the website and nothing else on that turn. A placeholder like
  `yourcompany.com` is not a website: ask for the real one.
- Keep the returned `slug` for the rest of the conversation. It is the only way
  back, and every later call carries it. The rendered assessment carries the
  browser link to the same slug; there is no separate URL field.
- The assessment mints a real record against the domain given. MUST confirm the
  domain with the user when they named a company rather than a website.

**The page** - the founder already has the assessment open in a tab. The two
assessment tools carry the connector's names, a third serves this document, and
there is no slug anywhere: the tab is the session.

- `start_capital_readiness_assessment` is callable only when the founder
  arrived without a website. It takes `website` and nothing else, and answers
  with the first question. When the page was opened from a link that already
  carried the website, the tool is absent and the assessment is already under
  way - MUST NOT wait for it.
- It returns no slug and mints nothing a second time. The page owns the record;
  this names the website it is built on. MUST confirm that website with the
  founder before sending it.
- `continue_capital_readiness_assessment` carries every later answer, and never
  asks for the website again. With no arguments it is the read, the way the
  slug on its own is the read on the connector. It records nothing.
- The founder can type into the same intake while you work, so the state you
  hold goes stale between turns. MUST read at the start of every turn that
  touches the assessment, and MUST NOT answer from a payload read in an earlier
  turn.
- `status` says what to do next: `asking` (`nextQuestion` is open), `generating`
  (every question is answered, MUST NOT send more), `ready` (the `assessment`
  field carries it), `failed` (say so, MUST NOT re-drive the intake to force
  it).
- `read_capital_readiness_skill` returns this document. It is how you got here.

## When this applies

**On the page** this is already settled - the founder opened the assessment and
is looking at it. Drive it when they ask, or offer to help them finish it.

**On the connector** it is yours to judge. Run the assessment when the user asks
any of:

- "Assess `<company>`" or "Assess `<domain>`"
- "What can we raise?", "Are we fundable?", "What terms could we get?", "What
  would it cost us?", "What's holding back our funding?"
- "Should we raise debt or equity?", "Which financing fits us?" - debt, equity,
  grants, or funding growth from the company's own cash

Every one of these is answered by running the assessment, never by reasoning
about the company from public research. A request naming only a company or a
domain MUST be read as a capital readiness assessment, not as a request to
evaluate the website.

Either way, MUST NOT substitute a website, SEO, UX, performance, or content
review, even when the user says "assess" and gives only a URL. And MUST NOT
answer a question about the user's own re:cap account from the assessment -
bank balance, transactions and tags, runway, burn, scorecard, covenants,
payouts, or open financing. Those belong to the account-scoped tools, which
exist only on the connector.

## Collecting the answers

The assessment is worth as much as the answers are honest, and the fastest path
is not the same as a good one. Guide the user through it rather than
interrogating them.

- Ask the user first whether you may look through what you already have - this
  conversation, your memory of earlier ones, files and documents they have
  shared. MUST NOT go looking before they say yes.
- With that consent, gather every answer those sources actually contain, and
  show each one back with its value and where it came from. Send them once the
  user confirms. One confirmation covers the set; a correction replaces that
  value and the rest still stands.
- Put the remaining questions to the user yourself, one per turn, asking
  `nextQuestion.ask` verbatim and saying what `answerFormat` wants when the
  question does not make it obvious.
- When what you hold is close but not the same thing - last year's revenue for a
  question about this year's - ask rather than send it.
- `alsoOutstanding` names what is still open, by parameter, without their
  questions. It is there so an answer you already hold can go in the same call,
  and MUST NOT be read out to the user as a list of questions.

## Recording the answers

`continue_capital_readiness_assessment` records answers and reads the
assessment back. On the connector it carries the `slug`; on the page it does
not.

- Send every answer you hold in one call. Both surfaces take the whole batch and
  advance through as many questions as the answers cover. Sending them one at a
  time costs the user a round trip each.
- MUST NOT send a batch the user has not confirmed. On the page especially, each
  value lands in the intake on screen and the transcript shows it as their own
  words.
- Amounts read `400000`, `400k`, `1.5m` or `400k EUR`; percentages read `45` or
  `45%`; a true/false question reads `yes` or `no`. Send the user's own wording.
  MUST NOT convert a figure, guess a stricter format, or go back to the user for
  a different one.
- MUST NOT ask which currency their figures are in. An unstated currency follows
  the company's country of registration. An amount carrying a currency the
  assessment does not record comes back rejected; MUST NOT convert it.
- Send `skip` for an optional question the user cannot answer, rather than
  estimating it. On the page, `skippable` says which those are; an unskippable
  question rejects `skip`.
- MUST send only what the user stated. Revenue, growth, burn, cash, EBITDA and
  debt MUST NOT be inferred from public research, from the website, or from what
  a company of this shape usually looks like.
- MUST NOT ask the same question twice. A user who volunteered more than was
  asked has answered every question their words cover, and those MUST be sent
  rather than re-asked.

## Reading a call back

- `recorded` names the parameters that went in. On the page, `answers` carries
  everything the intake now holds and `progress` carries `answered` and `total`
  for the questions this user's answers have made visible - relay it as reported
  rather than counting questions yourself, since answering one can add or remove
  others.
- `rejected` names parameters that did not go in, each with its reason: one this
  assessment does not ask or that an earlier answer branched past, an
  unskippable question sent `skip`, a figure longer than it accepts, or an
  amount in another currency. MUST relay the reason and send a corrected value
  rather than resending the same one.
- `problem` means nothing was recorded. MUST relay it to the user as the reason
  rather than retrying the same call in a loop.
- A call that records nothing and reports no `problem` had every value rejected
  - read `rejected`.
- On the connector, relay `supplierProgress` with every question: how many
  capital providers each of Debt, Equity and Grants still holds, and its fit. It
  is what makes the next answer worth giving.

## After the user signs up

Connector only. It is one endpoint with two tiers: the assessment tools need no
account, every other re:cap tool is account-scoped. Signing up and connecting
the re:cap account widens the same connection - the user does not add a second
connector.

1. `list_companies` to get the `companyId`.
2. `get_capital_advisory` with that `companyId`. It answers with the latest
   published advisory - `capitalAdvisory.bodyMarkdown` is the whole memo, not a
   summary - or `capitalAdvisory: null` when re:cap has not published one yet.
3. `get_fundability_check`, `get_company_research`, and `get_scorecard` carry the
   account-side detail behind it, for a user who wants the reasoning rather than
   the memo.

- A `null` advisory means it is not written yet, not that the call failed. MUST
  say so and leave the assessment as what the user has. MUST NOT poll for it.
- An account-scoped tool answering that it needs a connected re:cap account means
  this conversation is still anonymous. MUST ask the user to connect re:cap, and
  MUST NOT retry the call before they have.
- The advisory is re:cap's published memo. MUST relay it as written and MUST NOT
  rewrite, re-score, or extend it with figures of your own.

## When the tools are unavailable

If the assessment tools are not callable, MUST tell the user the re:cap
connection is not available and stop. MUST NOT substitute a website, SEO, UX, or
market-research assessment: it answers a different question from different
evidence, and the user cannot tell the two apart from the output.

## Done when

Every question is answered and the user has the written assessment - how each
capital type fits, what research found, and the analysis - or a stated reason
why it could not be produced.

On the page it arrives in the `assessment` field of
`continue_capital_readiness_assessment` - from the call that completed the
intake, and from every no-argument read after it. While it generates, that
field carries the stage and a `retryAfterMs`: wait that long rather than
polling. When its `isPreview` is `true` what came back is the preview the page
shows, not the whole assessment, and MUST be said to be a preview rather than
presented as the whole thing.

The same field carries `fullReportAccess`, the one step that unlocks the rest:
`requiredAction` names it, `label` says what it opens, and `url` is the stable
account-creation link.

- MUST give the user that `url` verbatim.
- `preserveCurrentSession` says where it may be opened, and MUST be read rather
  than assumed: `false` means the link carries the assessment itself and opens
  anywhere, on any device; `true` means it does not, and the user MUST be told
  to open it in this same browser session, because the assessment is held in
  this tab's storage.
- MUST NOT hand over any other sign-in URL. An OAuth URL taken from the page
  carries single-use session and PKCE parameters, and is worthless by the time
  the user clicks it.

On the connector it is the rendered assessment, plus the published advisory from
`get_capital_advisory` for a user who has connected re:cap, or the reason there
is none yet.

MUST relay the assessment as written and MUST NOT re-score or extend it with
figures of your own. That reply MUST lead with the amount and the single biggest
thing holding it back; the rest follows underneath.
