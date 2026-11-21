# Reviewer checklist

- [ ] Submitter has Apps Management write access in the publishing OpenAI organization.
- [ ] Singapore Department of Statistics, or an authorized representative, is the verified developer/business identity.
- [ ] Publisher can place the exact challenge token at the portal-specified `/.well-known/openai-apps-challenge` URL on the MCP host or an allowed parent host.
- [ ] Production endpoint `https://chatwithsandra.singstat.gov.sg/mcp` is stable and publicly reachable.
- [ ] **Scan Tools** discovers the three documented tools and the schemas match production behavior.
- [ ] Every live tool has accurate `readOnlyHint`, `openWorldHint`, and `destructiveHint` annotations. As of 21 September 2026, these annotations were absent from the production `tools/list` response.
- [ ] Tool responses exclude secrets, internal identifiers, debug payloads, and unnecessary personal data.
- [ ] The final skill bundle is uploaded or imported and scanned successfully.
- [ ] Listing text, support URL, privacy policy, terms, and publisher identity all match.
- [ ] At least five positive and three negative tests are entered and reproducible without authentication.
- [ ] Country/region availability matches the publisher's legal and support readiness.
- [ ] Release notes and policy attestations are accurate before submission.

Public submission cannot be completed by an unrelated third party because OpenAI requires verified publisher identity and control of the MCP domain. Do not submit this package under the Singapore Department of Statistics name without authorization.
