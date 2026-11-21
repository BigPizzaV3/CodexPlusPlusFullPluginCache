# GovBot Organization Records

An OpenAI plugin from Ideation Lab, Corp. for sourced U.S. federal organization profiles, federal contracting histories, and qualified supplier background briefs. It connects to the independent read-only MCP service at https://records-api.govbot.ai/mcp.

## Included skills

- **organization-federal-record** resolves an organization and presents SEC, federal award, enforcement, complaint, and recall records by source.
- **federal-contracting-history** examines a selected UEI's obligations by federal fiscal year and largest prime awards, with agency and award category context.
- **supplier-record-screening** prepares a qualified background brief using available EPA, CFPB, FDA, and NHTSA records.

Start with an organization name, ticker, or known identifier. The assistant may ask which legal entity you mean when results are ambiguous. Example: “Use organization-federal-record to prepare a sourced federal-record profile of Lockheed Martin (LMT).”

## Sources and limitations

The service reads SEC EDGAR, USAspending.gov, EPA ECHO, the CFPB Consumer Complaint Database, openFDA recall enforcement reports, and NHTSA recalls. Availability and record dates differ. Identity resolution is source-specific: a CIK, UEI, or name match does not automatically link records across sources. Subsidiaries and parents with separate UEIs remain separate.

Obligations are not payments. Annual obligations and life-of-award amounts cover different periods. Returned largest-award samples do not establish complete agency totals. Name-matched enforcement or recall records can concern other entities. Complaints and recalls alone do not prove wrongdoing. Empty, unavailable, timed-out and unsearched sources are distinct; none establishes compliance. The plugin provides no risk score, legal opinion, eligibility decision, or medical advice.

Only send public organization queries; do not provide credentials or confidential supplier material. Queries go to the independent service and relevant public data providers. See the [service privacy notice](https://records-api.govbot.ai/privacy), [publisher website](https://govbot.ai), and [service support information](https://records-api.govbot.ai/).

## Local development and validation

Using Python 3.10 or later, from this independent project directory:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python scripts/package.py --build
python3 scripts/probe_mcp.py
```

The default probe validates saved contract evidence offline. Live verification is explicitly opt-in; see `docs/MCP_VALIDATION.md` for its bounded invocation and observations. The ZIP is built deterministically from seven allowlisted files. No archived server source, private configuration, test evidence, or deployment commands are included.

## Installation and release status

`dist/govbot-organization-records-openai.zip` is a local candidate package, not a directory listing. For current supported installation and review procedures, see [OpenAI plugin documentation](https://developers.openai.com/plugins/). In the development workspace, `docs/OPENAI_SUBMISSION.md` records the verified specification, local test route and outstanding owner steps. Local schema validation does not prove successful installation in an OpenAI client or directory approval.

Publisher: Ideation Lab, Corp. The independent server source is in `server/`; deployment belongs to the Claude session. Version 1.0.1 targets records-api.govbot.ai and awaits deployment/live verification. No public submission is included in this milestone.
