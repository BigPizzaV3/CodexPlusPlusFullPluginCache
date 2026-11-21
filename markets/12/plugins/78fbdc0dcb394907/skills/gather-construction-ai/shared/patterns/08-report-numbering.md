# Pattern 8: Report Numbering

All skills and agents that produce structured report output include a reference number in the header block. This enables cross-referencing between reports in the same conversation.

### Format

```
Ref: [PREFIX]-[NNN]
```

Where:
- `[PREFIX]` is a 2-letter code identifying the report type (see table below)
- `[NNN]` is a zero-padded 3-digit sequential number, starting at `001`

### Prefix Table

| Prefix | Report Type | Skill / Agent |
|---|---|---|
| PR | Progress Report | `$progress-report` |
| CR | Commercial Report | `$commercial-report` |
| PL | Plant & Equipment Report | `$plant-report` |
| DQ | Data Quality Report | `$data-quality` |
| LA | Labour Analysis | `$labour` |
| RA | Resource Analysis | `$resource-analysis` |
| PG | Progress Analysis | `$progress` |
| AB | As-Built Programme | `$asbuilt-programme` |
| DA | Delay Analysis | `$delay-analysis` |
| WI | Weather Impact | `$weather-impact` |
| AC | Access Analysis | `$access` |
| MM | Measured Mile | `$measured-mile` |
| BM | Benchmark | `$benchmark` |
| PM | Programme Analysis | `$programme` |
| ES | Estimator Rate Card | `$estimator` |
| CC | Cost to Complete | `$cost-to-complete` |
| EV | Event Register | `$events` |
| CE | Claim/CE Submission | `$ce-builder` |
| QT | CE Quotation | `$ce-quotation` |
| TB | NEC Deadline Clock | `$nec-deadlines` |
| EP | CE Evidence Pack | CE Evidence agent |
| AP | Application for Payment / Valuation | `$valuation` |
| SV | Subcontractor Application Verification | `$subcontractor-check` |
| TS | Timesheet Verification | `$timesheet-check` |
| PI | Programme Import | `$programme-import` |
| DW | Daywork Sheet | `$dayworks` |
| OH | Plant Off-Hire Review | `$plant-offhire` |
| MR | Material Reconciliation | `$material-reconciliation` |
| PS | Prelims & Staff Monitor | `$prelims-monitor` |
| WQ | Weekly QS Pack | Weekly QS agent |
| TC | Time & Claims Package | Time & Claims Advisor agent |
| WP | Workforce & Performance Review | Workforce & Performance Advisor agent |
| CF | Commercial Forecast | Commercial Forecast agent |
| RD | Data Readiness Report | Data Assurance agent |
| CT | Contract Guidance Note | Contract Advisor agent |
| CD | Portfolio Review | Commercial Director agent |
| PA | Programme Advisor Review | Programme Advisor agent |
| CL | Cost Ledger Import | `$cost-import` |
| CV | Cost Value Reconciliation | `$cvr` |
| FA | Final Account Position | `$final-account` |
| AJ | Adjudication Readiness Pack | `$adjudication-pack` |
| CS | Project Cash Forecast | `$cashflow` |
| RL | Rate Library Sweep | `$rate-library` |
| RT | Red Team Review | Red Team agent |
| CO | Correspondence Import | `$correspondence-import` |
| IA | Indicative Impact Assessment | `$programme-impact` |
| RV | Programme Revision Comparison | `$programme-compare` |
| DP | Draft Programme | `$programme-create` |
| BQ | BoQ Import | `$boq-import` |
| TP | Tender Pricing Build-Up | `$tender-pricing` |
| QL | Quote Levelling | `$quote-levelling` |
| BA | Bid Advisor Review | Bid Advisor agent |
| OF | CE Opportunity Radar | `$ce-radar` |

### Sequencing Rules

1. If a previous report **of the same type** exists in the conversation, increment the number by 1
2. If no previous report of that type exists, use `001`
3. The number is **session-local** — it resets each conversation and does not replace the project's own report numbering
4. Always include a caveat line: "Ref: [PREFIX]-[NNN] is a session-local sequence number for cross-referencing."

### Cross-Referencing

When one report references findings from another report in the same conversation, use the ref number:

> "As identified in DA-001 (Delay Analysis), [X] hours were lost to access restrictions."

---

## Cross-Skill Suggestions

After presenting results, suggest related skills that could provide deeper analysis:

- Labour analysis → suggest `estimator` (derive unit rates)
- Progress tracking → suggest `programme` (milestone forecasting), `estimator` (actual rates)
- Delay analysis → suggest `weather-impact` (if weather is a factor), `measured-mile` (quantify disruption)
- Access analysis → suggest `delay-analysis` (broader delay register), `programme` (programme impact)

Keep suggestions brief — one line per related skill, only suggest skills genuinely relevant to the data just presented.
