# Pre-submission checklist

- [x] Supported compatibility manifest and root .mcp.json included.
- [x] Original canonical logo downloaded without alteration (512 x 512 PNG).
- [x] Public OAuth discovery advertises DCR and PKCE S256.
- [x] Privacy and terms URLs return HTTP 200.
- [ ] Complete domain verification in the OpenAI submission portal.
- [ ] Connect the HTTPS endpoint using OAuth DCR in a fresh OpenAI session.
- [ ] Verify DCR registration, actual S256 exchange, callback, token exchange, resource/audience binding and bearer validation. Metadata alone does not prove these work.
- [ ] Execute all five tools through that OAuth session and retain results.
- [ ] Run the five positive and three negative review scenarios.
- [x] Add the supplied demo URL to extensions.com.openai.review.demo_recording_url.
- [ ] Confirm the demo plays in a signed-out browser and Drive sharing allows reviewers to view it.
- [ ] Enter reviewer account credentials privately in the portal; never package secrets.
- [ ] Confirm publisher identity, category, country availability and commerce settings.
- [ ] Upload ZIP, connect MCP under With MCP, finish scans and resolve findings.
- [ ] Submit for review after completing the required attestations.
