---
name: us-dockets
description: Find what parties and courts actually did in US federal and state litigation — real cases matching a fact pattern, a judge's or opposing counsel's record, what a named complaint pleaded or an order held, motion practice in a specific court, and filings read with OCR. Use exemplar filings as a template to draft from. United States only; non-US legal questions belong with clio-research.
---

# US court dockets

Vincent searches real US federal and state court dockets, retrieves filings (with OCR
on scanned documents), and profiles judges and lawyers. **United States only** — for a
non-US jurisdiction this is unavailable and vLex legal research is the right path, so
do not describe the absence as a gap in coverage of that jurisdiction.

There is no separate docket tool on this server. It is the same `start_research` /
`continue_conversation` conversation; what selects docket work is how the `question`
reads. Carry the user's own specifics into it.

## What reaches docket rather than legal research

Docket work is about what parties and courts *actually did*, not what the law says:

- finding real cases by fact pattern, party, judge, docket number, or filing type
- what a named case's complaint pleaded, what counts survived, what an order held
- motion practice in a named court — whether an argument has worked there
- a judge's or opposing counsel's record: ruling patterns, tendencies, track record

Pleading vocabulary **attached to a real named case** is docket work. The same words
with no case or party named are legal research. A question that pairs a doctrinal
standard with "have parties actually litigated this" is both — ask for both.

## Phrase the question so it lands

Name whatever the user named: the court (`D. Nev.`, `S.D.N.Y.`, PTAB, a state court),
the parties, the judge, the filing type, the date range. A bare "find cases about X"
with no US court or party is ambiguous and will be answered as legal research.

If the user's jurisdiction is unstated and the request only makes sense against US
courts, say which you assumed rather than silently picking.

## Exemplars as a drafting template

To draft from real filings, do it in one conversation and keep the
`conversation_id`: ask Vincent to find comparable filings in the relevant court,
read the ones that fit, and then draft from them — naming what should be modelled
(structure, causes of action, argument order) and what must change for these facts.

Two things to hold: attribute the draft to Vincent's own text rather than to the
exemplars, and never present language lifted from a filing as this matter's analysis.
Label the result a draft for review, and surface the exemplars it was built from so
the user can check them.

## When the tools are not there

Docket access is entitled per organization. Without it Vincent has no docket tools and
will answer from vLex legal research instead, which reads like a weak answer rather
than a missing entitlement. If the answer covers doctrine when real filings were asked
for, say the account may not have docket access and let the user confirm — do not
retry, and do not present the research fallback as the docket answer.

Judge that on the finished answer, never on the turn call. Searching dockets and OCRing
filings takes minutes, so a docket turn all but always returns `still_running` with no
answer at all — and reading "no filings" off that reports a billing problem to a user
whose search is running perfectly well.

Docket results are records of filings, not holdings that have been verified as good
law. A filing shows what a party argued, not that it succeeded.

## A missing link is the answer, not a gap to fill

Many docket citations come back with no link, or with one that resolves nowhere from
here. Both are correct, and neither means the lookup failed:

- A filing's real URL is often a session-protected permalink or a signed download.
  Vincent refuses to publish those as source links and returns the citation without
  one. The absence is a deliberate outcome.
- Where a link *is* returned, it is built for the deployment the account is on — a
  Clio Docket view for a Clio Work account. Those are for the user's own authenticated
  session; they are not expected to open anywhere else.

So do not web-search to find, repair, replace or confirm a docket link, and do not go
looking for the filing on a court portal or an aggregator. Vincent read the docket
record itself; a search result is a *different artifact* of unknown provenance, and
citing it beside Vincent's record silently mixes an unverified source into the answer.

Report the citation as Vincent returned it — party, court, docket number, date, filing
type — and say the filing is not linkable from here if the user reaches for a link.
That is more useful than a URL that goes somewhere else.
