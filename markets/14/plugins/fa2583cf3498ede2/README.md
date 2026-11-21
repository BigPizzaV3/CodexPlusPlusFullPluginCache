# Praxis

![Praxis](./assets/praxis.svg)

**Preview package.** The insights endpoint and directory listings are awaiting activation.

Read aggregate CMA Order compliance counts, held billing totals and open Praxis task counts from your authorized workspace. Praxis works on top of the veterinary practice management system your practice already runs. Summaries retain their observation times, incomplete-data evidence and stated currencies. This connection does not expose personal records, clinical advice or controls that change practice records.

Package identifier: `praxis-veterinary-insights`.

Connect the remote Praxis server through your host's OAuth connection flow at https://praxisvets.com/mcp/insights. Select your authorized workspace and grant only `insights:read`. Do not paste account credentials or tokens into chat. Run the practice-insights skill to request one of the aggregate summaries. A Praxis account and authorized workspace are required.

The package contains workflow instructions and public connection metadata. The service runs remotely; the public plugin repository does not contain the Praxis backend or practice records.

Aggregate tool outputs exclude personal record fields. Praxis sign-in and authorization process account/session identity. Praxis retains the workspace credential name, authorizing account reference, hash/prefix and usage/revocation metadata; these records can persist beyond 30 days until workspace erasure. Revocation stops access without deleting that metadata. The bundled workflow sends no data to services other than its declared Praxis connector.

Privacy: https://praxisvets.com/privacy

Support: https://praxisvets.com/support

Terms: https://praxisvets.com/terms

Version 0.1.0. Proprietary; all rights reserved.
