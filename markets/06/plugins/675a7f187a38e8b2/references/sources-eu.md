# Source registry — European Union

Verification labels below are original author notes, not results of the Codex compatibility
review. Recheck every endpoint and claim at run time. HTTP status alone does not verify
content. Runtime behavior is governed by `runtime-safety.md`.


Every URL here was fetched and confirmed live on **2026-09-09**. A source that fails at scan time is
a named coverage gap, never a silent omission.

---

## 1. Official Journal, L series (legislation) — `primary`

The OJ L series is where EU legal acts are published. **Publication in the OJ is the event** that
starts entry-into-force clocks, so this is the anchor source for EU.

- L series RSS: `https://eur-lex.europa.eu/EN/display-feed.rss?rssId=222` (verified 200)
  Feed title "Acts of the Official Journal L". Verified live content included Commission
  Implementing Regulation (EU) 2026/1975 (CELEX `32026R1975`), published 8 September 2026.
- C series RSS (information, notices, consultations):
  `https://eur-lex.europa.eu/EN/display-feed.rss?rssId=165` (verified 200)
- Daily view (human-readable): `https://eur-lex.europa.eu/oj/daily-view/L-series/default.html`

### Critical limitation — the feed is a short window

The RSS feed carries only the most recent editions. **It cannot satisfy a lookback longer than a few
days.** For any real scan window:

1. Use the feed for the most recent items.
2. Use EUR-Lex search or the SPARQL endpoint (§3) for the rest of the window.
3. If neither was used for part of the window, **say so as a coverage gap.** Do not present a
   feed-only result as a full-window EU scan — that is the most likely way this plugin produces a
   false "nothing new" for the EU.

## 2. CELEX resolution — `primary`

Every EU act has a CELEX number, which is the stable identifier and the `official_id`.

Deep link pattern (verified 200 for `32026R1975`):

```
https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:<CELEX>
```

CELEX shape, useful for triage: sector digit + year + descriptor + number. `3` = legislation;
`R` = regulation, `L` = directive, `D` = decision. So `32026R1975` is a 2026 regulation. A trailing
`R(01)` marks a corrigendum — verified in the live feed — and a corrigendum is an amendment to an
existing act, not a new obligation. Don't report it as new law.

Cite the CELEX deep link, not a EUR-Lex search URL.

## 3. EUR-Lex / Cellar SPARQL endpoint — `primary`, for real date-bounded queries

`https://publications.europa.eu/webapi/rdf/sparql` (verified 200)

The only reliable way to enumerate EU acts across an arbitrary date range. Use when the scan window
exceeds the RSS feed's reach. Returns CELEX identifiers, which then resolve via §2.

If a SPARQL query fails or times out, fall back to EUR-Lex search and **label the EU portion of the
scan as partial**.

## 4. Pipeline and consultations — `primary` / `regulator`

Acts in the OJ are already law. Horizon scanning needs what is *coming*.

| Source | URL | What it gives |
|---|---|---|
| Have Your Say | `https://ec.europa.eu/info/law/better-regulation/have-your-say_en` | Open consultations and feedback periods — the chance to influence a measure before it binds. Verified 200. |
| EP Legislative Observatory (OEIL) | `https://oeil.secure.europarl.europa.eu/oeil/home/home.do` | Procedure status for files in the ordinary legislative procedure. Verified 200. |

For anything from these, the lifecycle stage is `proposed` or `consultation` — **never** `adopted`.
A Commission proposal can change substantially or die. Describe it as a proposal, cite the proposal,
and do not carry its indicative dates forward as if settled.

## 5. Regulators and guidance — `regulator`

Guidance is not law, but it shapes enforcement, and supervisory expectations often move before
legislation does. Label the tier accordingly.

| Body | URL | Domain |
|---|---|---|
| EDPB | `https://www.edpb.europa.eu/edpb_en` | GDPR guidelines, opinions |
| EU AI Act / AI Office | `https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai` | AI Act implementation, codes of practice |
| EBA | `https://www.eba.europa.eu/publications-and-media/press-releases` | banking |
| ESMA | `https://www.esma.europa.eu/press-news/esma-news` | markets |

All verified 200 on 2026-09-09.

---

## 6. EU date traps — read before asserting any EU date

EU acts routinely carry three different dates, and conflating them is the most common way to give a
client a wrong deadline:

1. **Publication in the OJ** — the date on the act.
2. **Entry into force** — usually "the twentieth day following that of its publication," which you
   must compute from the publication date. Quote the provision, show the arithmetic, and **label the
   result as derived** rather than presenting it as a date the act states.
3. **Application / applies-from** — frequently much later than entry into force, and often staged by
   obligation or by entity class.

Cite each separately with its own quote. Where an act stages obligations across several dates, list
each milestone as its own calendar entry rather than collapsing them into one date.

## 7. Member State implementation — **out of v1 scope**

`EU-<country>` jurisdictions are recorded in the profile but **not searched** in v1. Directives
require national transposition, so Union-level coverage alone can miss the rule that actually binds
a local entity. Whenever a profile contains an `EU-<country>` token, state this limit explicitly in
the scan output.
