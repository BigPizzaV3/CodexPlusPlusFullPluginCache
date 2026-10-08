---
name: onboarding-wins
description: Build a complete, evidence-backed Zendesk onboarding journey import from Gmail plus the user's local Chrome session for Gong, Salesforce and View 360. Use when a coworker asks to import, refresh, reimport or investigate an onboarding account for the Onboarding Wins app.
---

# Onboarding Wins import workflow

Use this skill to produce one canonical JSON object for the Onboarding Wins Google Apps Script app. The app is the system of record for the dashboard; this workflow is the research and normalization layer.

## Required operating context

- Run in ChatGPT Work with `Local` computer access when browser work is needed.
- Use the Gmail connector for the coworker's connected mailbox.
- Use the local Chrome/browser session for Gong, Salesforce and View 360, because those systems may only be reachable through the coworker's logged-in browser session.
- Do not claim that a source was reviewed if the connector or browser session could not access it.
- Ask only for missing scope: exact account name, onboarding CSM, CSM email, customer contacts/domain, and the journey start/end month. If an account-specific Gong, Salesforce or View 360 link is provided, use it as the entry point.

## Scope and evidence rules

1. Interpret the journey window as the first day of the start month through the last day of the end month, inclusive.
2. Gmail is used to find and count relevant individual messages between the CSM and the customer's contacts/domain. Count messages, not threads. Record the query used and exclude internal messages without direct onboarding evidence.
3. Gong is used to find and count relevant calls in the window. Review every result that loads. If results are unavailable, distinguish `found`, `reviewed`, and `notLoaded` in `sourceStatus` and notes.
4. Salesforce is the primary source for ARR, subscription, agents, products, add-ons, account status and opportunities. View 360 is a secondary verification source. Count the admin in agents when the source defines agents that way.
5. If Salesforce and View 360 disagree, do not guess. Use the value that is explicitly current only when the source says so; otherwise set the field to null and record the discrepancy.
6. Never estimate ARR, agents, subscription or add-ons. Missing values are acceptable and should be represented as `null` plus a source explanation.
7. Keep source links in `client.links.gong` and `client.links.gmail` only when useful for the app. Do not include private Salesforce/View 360 links in the output unless the app's configured schema explicitly requests them.

## Win and CSQL classification

Allowed win types are `Retention`, `Implementation`, `Adoption` and `Expansion`.

- Retention: a real cancellation, churn or ARR-loss risk existed and the customer continued.
- Implementation: Zendesk was configured or technically ready to operate.
- Adoption: the customer used, expanded or operationalized Zendesk in a measurable way.
- Expansion: seats, products or add-ons were explicitly purchased, contracted or otherwise confirmed.

Only mark `csql: true` when the evidence shows an explicit commercial signal such as a request for additional seats/add-ons, a sales handoff, proposal, DocuSign or confirmed purchase. A demo, trial, discussion or recommendation alone is not a CSQL. When the process is not confirmed closed, record `state: "Pending validation"` and do not represent it as booked revenue.

## ARR normalization

Return ARR as a JSON number in USD, never as a currency string. Normalize values such as `$46,632 USD`, `ARR: $46,632`, `46.6K` and `46.6k` to `46632`, `46632`, `46600` and `46600`. If the source is blank, says not found, or cannot be reconciled, return `null` and explain it in `arrSource` and `notes`.

Agents must be an integer or `null`. Subscription must be a concise string or `"No encontrado en Salesforce o View 360"`. Do not convert unknown values into zero.

## Output contract

Return only one JSON object in a fenced block only if the user explicitly asks for a fence; otherwise return only the raw JSON object with no introduction, markdown, or trailing explanation. It must follow this shape:

```json
{
  "client": {
    "clientId": "stable-slug-or-existing-client-id",
    "accountName": "Exact account name",
    "owner": "Adrián Trejo",
    "status": "En progreso",
    "startDate": "Febrero 2026",
    "endDate": "Julio 2026",
    "quarters": ["Q1 2026", "Q2 2026"],
    "arr": 46632,
    "arrSource": "Salesforce",
    "subscription": "Suite Professional",
    "agents": 5,
    "agentsSource": "Salesforce / View 360",
    "goal": "What the onboarding was intended to achieve",
    "calls": 7,
    "emails": 66,
    "impact": "Business impact in one sentence",
    "winType": ["Implementation", "Adoption"],
    "winImpact": "Why the completed journey mattered",
    "winEvidence": "Specific evidence from calls and emails",
    "win": "Final win statement",
    "summary": "Long executive summary of the full journey",
    "brief": "Longer brief combining calls, email evidence and the final win",
    "links": {"gong": "https://...", "gmail": "https://..."},
    "gmailQuery": "query used",
    "expansion": {
      "additionalAgents": 0,
      "addons": [],
      "summary": "",
      "evidence": ""
    },
    "notes": "Source availability, limitations and pending validations"
  },
  "sessions": [],
  "milestones": [],
  "steps": [],
  "timeline": []
}
```

Each session row should contain `dateEs`, `titleEs`, `descriptionEs`, `source`, `dateEn`, `titleEn`, `descriptionEn`. Each milestone/timeline row should contain the same fields. Use month-level start/end dates in the client, while evidence rows may contain exact dates.

## Final quality check

Before returning the object:

- Verify `accountName`, `owner`, date range, calls and emails are present.
- Verify ARR is a number or null, never `$`, comma-delimited text or `"No encontrado"` in the ARR field.
- Verify agents is an integer or null, never zero merely because it was unavailable.
- Verify all four arrays exist, even when empty.
- Verify every win has evidence and that CSQL is false unless a commercial signal is explicit.
- Preserve limitations in `notes`, including source access, unloaded Gong results, unresolved Salesforce/View 360 discrepancies and unconfirmed expansion.
- If the app is performing a reimport, preserve the selected client's `clientId` and account name.

If the app rejects the JSON, run the bundled validator on the exact object and repair only the reported schema or normalization issues. Do not add prose around the JSON.

