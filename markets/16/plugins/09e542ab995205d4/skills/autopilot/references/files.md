# The Autopilot files

All three files are in `frontmost-autopilot/` at the root of the repository. The examples use an invented business.

## charter.md

The person owns this file. Autopilot writes it at set-up and changes it only when the person says so.

```markdown
# Autopilot charter

status: running
mode: assist
project: 123 (Northwind Invoices)
timezone: America/New_York
set up: 2026-11-16

## The business

- Sells: invoicing software for freelancers.
- Buyers: freelance designers and developers in the United States.
- Facts a page can state: $12 a month. 14-day free trial. Founded 2023.
- Never claim: "the cheapest", customer counts, awards.

## The site

- Live site: https://northwind.example. This repository publishes it.
- Pages: `site/pages/`. Framework: Astro. A page goes live when its pull request merges to `main`.
- Records: commit `plan.md` and `log.md` to `main`.
- Do not touch: `site/pages/legal/`, `src/billing/`.

## Limits

- open_limit: 3 pull requests that wait for me
- publish_limit: 1 new page in one run (Full-send only)
- read_after: 3 scans

## Outreach

- Mailbox: none. Write pitches to draft files.

## Full-send

- Off.
```

When the person turns Full-send on, replace the last section:

```markdown
## Full-send

- On since 2026-12-02. In my words: "Go full-send on fixes and pages."
```

## plan.md

Autopilot owns this file.

```markdown
# Autopilot plan

last_scan: 4411 (2026-11-18)
last_brief: 208 (week of 2026-11-16)
plugin version: 0.3.0
last review: none

## Scoreboard

| Scan | Scope | AI Visibility | Win Rate | Position | Sentiment |
|---|---|---|---|---|---|
| 4398 (2026-11-16) | total | 31% · 28 of 90 | 12% · 11 of 90 | 3.4 · 28 answers | 80% · 12 of 15 |
| 4398 (2026-11-16) | unbranded | 9% · 6 of 66 | 3% · 2 of 66 | 3.8 · 6 answers | 75% · 3 of 4 |
| 4411 (2026-11-18) | total | 32% · 29 of 90 | 13% · 12 of 90 | 3.3 · 29 answers | 80% · 12 of 15 |
| 4411 (2026-11-18) | unbranded | 11% · 7 of 66 | 5% · 3 of 66 | 3.6 · 7 answers | 80% · 4 of 5 |

## Open jobs

| Job | Target | Evidence | State |
|---|---|---|---|
| Answer page | Question 812, "best invoicing tool for freelancers" | Scans 4398 and 4411: 0 answers mentioned us. In scan 4411, 5 of 6 AI apps named another business first | `waits for review`, pull request #41 |
| Listing pitch | example.com/best-invoicing-tools | Cited in 9 answers, 2026-10-21 to 2026-11-18. Lists 3 rivals, not us | `waits for review`, draft in `frontmost-autopilot/drafts/pitch-example-com.md` |
| Search-term coverage | "invoice app with time tracking" | Scan 4411 only: 4 answers used it, 0 mentioned us | `watching` |

## Shipped jobs

| Job | Target | Shipped at scan | Link | Read |
|---|---|---|---|---|
| Fix | robots.txt blocked OAI-SearchBot | 4398 | #39 | `passed` in scan 4411 |

## Practice notes

- 2026-11-16. Google spam policies, scaled content abuse: many pages made for ranking and not for readers are spam. https://developers.google.com/search/docs/essentials/spam-policies
```

## log.md

Newest entry first. One entry for each run that did work or found a change.

```markdown
## 2026-11-18, scan 4411

**Waits for you**
- Pull request #41: a page for "best invoicing tool for freelancers".
- A fact: do you support recurring invoices? A page needs it.

**What changed**
- AI Visibility, unbranded: 11% · 7 of 66. It was 9% · 6 of 66. One answer is not a trend.
- The robots.txt fix is live. The check passed in this scan.

**What I did**
- Opened #41.
- Drafted one pitch. No mailbox is set, so nothing was sent.

**Next**
- The next scan is on 2026-11-20. Question 812 gets its read three scans after #41 is live.
```
