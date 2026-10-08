# HTML Report Workflow

Use for Standard and Deep reports when code execution is available. Rapid scans remain inline Markdown.

The renderer separates reasoning from presentation: research once, write compact JSON, and let
scripts/render_report.py produce the complete responsive HTML. Never spend tokens recreating CSS or
manually writing the page shell.

## Workflow

1. Finish research, scoring, and the 14-row evidence packet.
2. Build one compact JSON object using the schema below.
3. Include a final Sources section with public HTTPS URLs for decision-changing evidence.
4. Run:

~~~bash
python3 scripts/render_report.py --mode standard --input report.json --output CarSleuth-Report.html
~~~

5. Resolve any validation errors. Homepage-source warnings are non-fatal but should be replaced with
   claim-specific pages whenever possible.
6. Verify the output opens, contains the verdict, tables, score bars, seller questions, and sources.
7. Return the HTML report plus a short inline verdict. The chat summary should state verdict, score,
maximum price, dealer concern, and the next action without repeating the whole report.

If code execution is unavailable or rendering fails once, use the Markdown dashboard from
report-template.md. Do not keep retrying or withhold the vehicle decision.

## Compact schema

~~~json
{
  "page_title": "2021 Mercedes-Benz GLA 250 Investigation",
  "generated": "2026-09-01",
  "vehicle": {
    "title": "2021 Mercedes-Benz GLA 250 4MATIC",
    "meta": ["50,141 km", "North York, ON", "Independent dealer"]
  },
  "verdict": {
    "label": "NEGOTIATE",
    "confidence": "Medium",
    "score": 66,
    "metrics": [
      {"label": "Asking", "value": "$30,979"},
      {"label": "Fair value", "value": "$29.0–30.5k"},
      {"label": "Maximum", "value": "$29,750"},
      {"label": "Near-term", "value": "$700–2,600"}
    ],
    "summary": "One decisive paragraph."
  },
  "dealer": {
    "grade": "B",
    "name": "Dealer name and location",
    "risk": "Mixed",
    "note": "Written fees, PPI access, regulator status, and recurring review theme."
  },
  "sections": []
}
~~~

## Section types

Every section has type and title; optional fields include lede and note.

### Bullets, questions, or numbered actions

~~~json
{"type": "bullets", "title": "What Matters Most", "items": ["...", "..."]}
{"type": "questions", "title": "Ask the Seller", "items": ["...", "..."]}
{"type": "numbered", "title": "PPI Brief", "items": ["...", "..."]}
~~~

### Specifications with evidence status

~~~json
{
  "type": "specs",
  "title": "Vehicle Identified",
  "items": [
    {"label": "Engine", "value": "M260 2.0L turbo", "status": "Verified"},
    {"label": "History", "value": "One owner, no accident", "status": "Seller claim"}
  ]
}
~~~

Status labels containing Verified, Seller claim, Risk, or another value automatically receive
verified, claim, risk, or unknown styling.

### Risk cards

~~~json
{
  "type": "risks",
  "title": "Engine — M260 2.0T",
  "lede": "Short architecture context.",
  "items": [
    {
      "severity": 4,
      "title": "Exhaust valve seat and guide wear",
      "evidence": "A",
      "body": "Applicability, symptoms, cost exposure, and candidate evidence."
    }
  ],
  "score": "Engine score: 8/15 — concise reason."
}
~~~

### Tables

~~~json
{
  "type": "table",
  "title": "Maintenance at 50,141 km",
  "columns": ["Window", "Item", "Type", "Estimated cost"],
  "rows": [
    ["Now", "Brake fluid if undocumented", "Scheduled", "$150–220"]
  ]
}
~~~

Use tables for maintenance, history, market comps, dealership checks, ownership panel, and repeated
fields. Keep cells concise.

### Score bars

~~~json
{
  "type": "scorebars",
  "title": "Score Breakdown",
  "items": [
    {"label": "Engine", "score": 8, "max": 15},
    {"label": "Value", "score": 6, "max": 10}
  ],
  "subtotal": "59",
  "penalty": "−4 unresolved cylinder-head exposure",
  "final": "55/100"
}
~~~

### Tiles and callouts

~~~json
{
  "type": "tiles",
  "title": "Ownership Outlook",
  "items": [
    {"label": "12 months", "value": "$700–2,600"},
    {"label": "24 months", "value": "$1,800–4,300"},
    {"label": "36 months", "value": "$3,200–6,500"}
  ]
}
~~~

~~~json
{"type": "callout", "title": "Bottom Line", "style": "warn", "body": "Decision and next action."}
~~~

Callout styles are info, warn, and danger.

### Sources

~~~json
{
  "type": "sources",
  "title": "Sources",
  "items": [
    {"title": "Mercedes-Benz service schedule", "url": "https://...", "note": "Maintenance intervals"},
    {"title": "Local comparable listing", "url": "https://...", "note": "Asking-price evidence"}
  ]
}
~~~

Use real source URLs only. Internal citation reference IDs belong in the chat response, not the HTML.

## Content limits

- Standard: 8–12 sections, 3–5 risks, 3–5 comps, 5–8 PPI items, 5–10 sources.
- Deep: up to 16 sections, 6–8 risks, 5–8 comps, 8–12 PPI items, 10–18 sources.
- Avoid duplicate prose: every risk gets one detailed home.
- Keep cell text short and put interpretation in one note.
- Use Not credibly estimable before records/PPI instead of unsupported cost ranges.
