# Irish Legal Assistant

A source-first research tool for the law of the Republic of Ireland, for education and research.

## How it works

The plugin works on its own using official Irish sources. It includes a reference map (`skills/irish-legal-research/references/official-irish-sources.md`) of the responsible public body, official website and starting statutes for each legal area.

Uploading your own legal sources (for example current Revised Acts in a Project or Space) is optional. If you do, the plugin checks them first.

## MCP tools

The plugin connects to a read-only MCP server at https://mcp.cemkoyluoglu.tech/mcp. It needs no sign-in and collects no personal data.

- `list_legal_areas`, `find_official_sources`: responsible bodies, official websites and starting statutes by legal area
- `search_acts`: find an Act of the Oireachtas by title (every enacted Act since 1922)
- `get_act`: look up an Act by year and number (live, Oireachtas open data API)
- `get_act_section`: the text of a section as enacted (live, Irish Statute Book)

## Coverage

Employment • Housing/RTB • Consumer • Revenue/Tax • Immigration • Traffic/Garda • Criminal procedure • Family • Courts • Data protection • Health • Business • Debt/insolvency • Property/succession • Human rights/FOI

## Research model

Uploaded sources, if any → current Revised Acts → current official Irish guidance → reliable secondary sources when necessary.

Answers explain the general rule, the legal basis, common exceptions and the official body that deals with the matter. They do not decide how the law applies to your own case.

Time-sensitive legal points should be checked against current official sources when available.

## Source refresh

The plugin does not run scheduled or background jobs. When you ask for a source refresh, it reviews new and amended Irish legislation, commencement, Statutory Instruments and updated official guidance, then produces a change log and a recommended source list. It cannot replace files in your Project/Space; you replace them yourself.

## Important limitation

This plugin provides general legal information and research support. It does not give legal advice or legal representation. It is not a solicitor or barrister and does not guarantee a legal outcome.

## Developer

Cem Koyluoglu. Website: https://cemkoyluoglu.tech (personal website, not a law firm). Privacy policy: https://cemkoyluoglu.tech/privacy
