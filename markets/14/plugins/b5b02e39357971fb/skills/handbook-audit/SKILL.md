---
name: handbook-audit
description: Audit an attached US employee handbook (PDF, DOCX or TXT) for missing or non-compliant federal and state employment-law policies with AirMason Handbook Audit. Use when the user asks to check, audit or review their handbook for compliance gaps, missing required policies or policies that need attention, or asks a follow-up about an audit run earlier in the conversation. Not for drafting or rewriting policies, general employment-law questions with no handbook, or rules outside the US.
---

# Handbook audit

Checks an employee handbook against the US federal and state employment-law policies that apply to the user's company, using the AirMason Handbook Audit tools. The user's explicit instructions take priority over this workflow.

## Inputs

- **Handbook:** the file the user attached in this conversation (PDF, DOCX or TXT, up to 30 MB). Pass it as `handbook`. Never build the file object yourself or ask the user for a link.
- **Pre-fill (optional):** any company facts the user has already stated: `total_headcount`, `regions` (`FEDERAL` plus two-letter state codes; map cities and counties to their state), `state_headcounts`, `industry`, `work_locations` and the yes/no answers. Don't guess; the form asks for the rest.

## Steps

1. If no handbook is attached, ask the user to attach it and stop. Don't call a tool.
2. Call `open_handbook_audit_form` with the handbook and whatever the user has already said. Don't ask the form's questions in chat: the form shows them, validates the answers, and starts the audit when the user presses **Run audit**. Then reply in one or two sentences asking the user to check the form and press **Run audit**. Don't review or comment on the handbook yourself: the audit checks it.
3. Never call `start_handbook_audit` yourself: it only accepts calls from the form, which passes its own key, and refuses everything else. If the user would rather answer in chat, explain that the audit runs from the form, and open it with what they've told you.
4. When the audit finishes, the form posts "Summarize the handbook audit results." in the chat. Call `get_handbook_audit` with the `auditId` the widget gave you (and `wait_seconds` 40 while `status` is `analyzing`).
5. When `status` is `complete`, reply in 3-4 lines with the most important missing required policies and the policies that need attention, taken only from the tool result. The widget shows the full report, so don't repeat every item, and don't add findings from your own reading of the handbook.
   - If `verifiedAgainstHandbook` is false, the handbook text couldn't be checked. Present the required policies as policies that apply to the company, not as confirmed gaps, and say the results are based on the user's answers only.
   - Say the results are a general compliance overview, not legal advice.

## Free audit limits

The free audit covers up to 5 states besides Federal (DC and PR count as states). If the user needs more, tell them it's part of AirMason's paid plans and share the pricing link from the tool result. Don't offer to split the states across several free audits. The same applies when the upload limit is reached.

## When something goes wrong

- **The document isn't a handbook:** say so, ask for the actual employee handbook, and don't present any findings.
- **Rate limit or busy service:** pass on the message and suggest trying again later.
- **Audit not found:** audits are kept for 1 hour. Offer to start a new one.
- **Any other error:** pass the tool's message to the user.

## Follow-up questions

For questions about an audit already run in this conversation, call `get_handbook_audit` with the same `auditId`. Don't start a new audit.

Answer the question itself, at whatever length it needs; the 3-4 line limit applies only to the first summary. Use the returned fields: for policies that need attention, their risk level, reasoning and the rules not met; for missing policies, their reason. The tool result doesn't include the handbook's own wording. The widget's fullscreen report shows the relevant passage for each policy, so point the user there instead of quoting or paraphrasing the handbook.

## Boundaries

- Report only what the tools return. Never invent, soften or add findings.
- Don't give legal advice or draft policies as part of this workflow.
- Results cover US federal and state rules only, not city or county ordinances.
