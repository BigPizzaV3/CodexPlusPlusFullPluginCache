# Decisions retained in Doctilla

Draft recommendations freely, but do not use tools, alternate routes or narrative fields to simulate these protected human decisions:

- Close a CAR, set its closure date, or complete an 8D step.
- Record formal effectiveness results or an action's effectiveness.
- Approve management-review minutes or document revisions.
- Accept standard mappings or mark a product claim supported.
- Conclude a technical review; approve, reject or implement a product change.
- Set supplier status, evaluation outcomes or acknowledgements; accept/reject supplier CAR responses.
- Approve/reject concessions or management overrides; accept nonconforming output as-is or under concession.
- Close a complaint, activate a checklist, mark a programme deliverable done or decide quality-objective status.

Use the current server rules if stricter. Do not infer that a field enum granting a value authorises the decision. Report contradictions instead of exploiting REST/MCP drift. Return a trusted app link if actually available, otherwise direct the user to the named record in https://app.doctilla.co.uk.

Read locked records but do not edit the parent or bypass its lock through protected children/links. Do not unlock through tools, duplicate a record to evade a lock or quietly relocate the work. After a user reports an unlock, retrieve and verify the current editable state. Independently editable related actions require actual supported permission, not an assumption.

Proposed CARs are unagreed drafts, not open CARs. Observe the server's proposed-to-open transition rules. Closed, completed, approved and locked are different states; do not claim immutability from a label alone.

Evidence is currently metadata-only in the reviewed contract: no file upload/download through these domain tools. A file path is not a download URL. Generic links are not version-pinned evidence citations. Standards mappings are proposals; only human-accepted mappings count. Use authorised standards content and validate rights for the intended processing, not merely ownership of a purchased copy.
