---
name: box-legal-workflows-intake
description: "Run legal client intake and onboarding in Box: inventory submissions, check completeness, extract client and matter facts, surface cited risk indicators, route attorney review, and generate draft engagement documents. Use for client intake, onboarding, new matters, intake documents, or engagement letters."
---

# Legal intake in Box

Use the `box` skill for authentication and operations. For mechanics, use `box/references/content-workflows.md`, `box/references/ai-and-retrieval.md`, `box/references/mcp-search.md`, `box/references/mcp-doc-gen.md`, and `box/references/collaboration.md` as relevant.

## Workflow

1. Resolve the intake folder and record the relevant file IDs and versions. Cite the original files rather than an AI answer, and state when a result applies to an earlier version because a source changed. Identify the firm's required-document checklist; if it is not already supplied or identifiable, ask for it before assessing completeness.
2. Inventory the submission. In one cited multi-file pass when practical, check each required item for presence, readability, apparent completeness, and observable required fields or signatures, while extracting names, aliases, entities, jurisdictions, values, and other screening inputs.
3. Distinguish missing material from content that is present but unreadable, unsupported, truncated, or otherwise not assessed. Do not call the intake complete while a required item is unrepresented.
4. Use standard structured extraction by default and enhanced extraction only when the user explicitly requests it. Send the cited screening inputs to the firm's approved conflicts, sanctions, PEP, or similar systems; Box AI does not provide clearance.
5. Present the findings, then ask whether the user wants metadata written if the request did not already decide that. Use folder metadata for matter-level status and assignment, file metadata for document facts, or the firm's canonical intake file when that is its record model.
6. Route a summary comment or add access only when requested. Check the item's audience first; put privileged analysis, internal screening information, and other restricted reasoning in an internal artifact when the source has broader collaborators. Do not claim a plain comment targeted or notified a specific person.
7. When requested, generate an engagement-letter draft from the approved template and merge data. Record the template version, destination, output ID, and draft status; check an uncertain asynchronous batch before resubmitting.



## Intake output

Use one entry per checklist requirement. Label it **present and assessed**, **present but not assessed**, **missing**, or **not applicable**, then include the source citation, observed facts, limitation, and next action.

Example:

```text
Requirement: Beneficial ownership form
Status: Present but not assessed
Evidence: ownership-form.pdf, page 1
Limitation: pages 2–3 are unreadable
Next action: request a readable replacement before completeness approval
```

List screening inputs separately, for example: `Acme Holdings LLC — named in intake-form.pdf §2 — send to the firm's conflicts/sanctions system; no clearance conclusion made.`

Useful extracted fields include client and matter name, practice area, jurisdiction, value, and owner. Final risk, acceptance decision, assigned attorney, and decision date come from the authorized firm process and may be written only after approval.

When metadata was not requested, use a direct prompt such as: “I extracted the matter-level and document-level fields above. Do you want me to write them to the firm's existing Box metadata template?”

## Boundaries

- Completeness findings may be automated; authenticity, legal validity, sufficiency, client acceptance, risk rating, staffing, and clearance remain firm or attorney decisions.
- A model may apply documented criteria as preliminary analysis, but preliminary observations must not occupy final-decision metadata fields.
- Do not place preliminary screening hits or other restricted reasoning in broadly visible metadata or comments.
- A generated engagement letter remains a draft until authorized approval. Do not share it externally until approved, and use the audience and access specified by the user or clarify them when ambiguous.

