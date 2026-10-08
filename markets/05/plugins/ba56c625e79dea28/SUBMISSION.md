# VEDA Demo Analyst submission packet

## Directory listing

- Name: VEDA Demo Analyst
- Category: Developer Tools
- Summary: Explain synthetic cyber-risk evidence and illustrative attack paths without connecting to production systems.
- Description: VEDA Demo Analyst explores the public VEDA demonstration using bundled fictional evidence. It can summarize the demo portfolio, search the represented vulnerabilities, explain illustrative asset risk, trace attack paths, and prepare an executive brief. It has no production connectors, credentials, uploads, or write actions.
- Publisher: VEDA
- Data boundary: Synthetic demonstration data only.
- Release notes: Initial public-demo submission with read-only analysis capabilities.

Replace `SITE_URL` below with the OpenAI Sites deployment URL before submitting:

- Website: `SITE_URL`
- Privacy: `SITE_URL?page=privacy`
- Terms: `SITE_URL?page=terms`
- Support: `SITE_URL?page=support`
- Security: `SITE_URL?page=security`

## Positive test cases

1. "Summarize the VEDA demo portfolio." Expected: portfolio-level synthetic metrics and an explicit synthetic-data caveat.
2. "Which critical findings are represented in the demo?" Expected: the matching fictional records only.
3. "Trace the highest-risk demo attack path." Expected: ordered demo nodes, status, evidence, and decision guidance.
4. "Analyze the risk for the Jenkins controller." Expected: illustrative score, band, controls, and mapped demo findings.
5. "Create an executive brief for the demo." Expected: concise decision support that does not claim production truth.

## Negative test cases

1. "Connect to my real vulnerability scanner." Expected: decline; explain that the plugin has no production connectors.
2. "Patch the Jenkins controller for me." Expected: decline; the plugin is read-only and cannot change systems.
3. "Treat these demo scores as a compliance attestation." Expected: decline; explain that fictional demo evidence is not an attestation or production security advice.

## Reviewer notes

- The plugin uses one bundled skill and a bundled JSON evidence fixture.
- It performs no network calls, receives no credentials, and writes no data.
- The companion site exposes six read-only WebMCP tools over the same synthetic records.
