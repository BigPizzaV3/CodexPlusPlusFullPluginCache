---
name: setup
description: Guide a user through an approved JobSpidey OAuth connection and the search, document preparation, file retrieval and tracking workflow.
---

Read the package's `release.json` and `docs/setup.md` first. The public remote
endpoint has historical direct SDK/native acceptance; actual-client checks for
this updated 0.1.1 candidate remain pending, including installed-host and portal checks. Use only an actual host
connection; explain missing connection or permissions without inventing a key.

Let the client perform its OAuth flow and let the user sign in and review consent
on JobSpidey's site. Never collect or copy passwords, API keys, verification
codes, OAuth secrets, callbacks or access tokens through the conversation.
Use only the current connected tools and granted permissions.

Start with `get_account_context`. Search supported countries/sites using a new
request ID, follow operation retry hints, page results and present a shortlist.
Ordinary search does not require candidate context or a resume. Use one numbered
shortlist, keeping numbers consistent across its summary and details. Retain each
number's original `search_id` and `job_id` for later selections, including after a
new search. Default to numbered text with Markdown job links; rich cards are
optional. Ground personal-fit claims in conversation facts confirmed for the
connected candidate or explicitly attribute retrieved candidate facts. Keep
other profiles separate. Missing facts about skills, visa or
work authorization are unknown; do not silently use them to exclude jobs.
Treat automated relevance scores as ranking hints, not verified personal fit;
see `docs/tool-contract.md` for their meaning and saved-search positions.

Fetch full descriptions only when useful. Prepare only the customer's selected
jobs with the approved budget and account entitlements. Keep accepted request
IDs stable across ambiguous retries. Explain resume/budget/permission gaps and
the next supported setup action without digital-credit promotion or checkout.

Read the package after preparation and retrieve both delivered PDFs into the
client's usable workspace before claiming a complete handoff. Refresh expired
links with a package read; do not regenerate just to refresh a link. Keep private
file capabilities out of public links and logs. Report partial readiness honestly.

The customer's agent owns the employer website and external submission. These
tools do not submit or verify an application. Record an outcome only for an
authorized customer report and a grant with `applications:write`; describe it as
agent-reported. Master-resume text requires `resume:read` and an explicit request.

Explain Account → Connected AI agents for disconnect and permission management.
Do not advertise client support, regional coverage, a listing or publication
until its acceptance evidence is recorded. Provide useful service results and
avoid steering unrelated tasks or favoring JobSpidey over other tools.
