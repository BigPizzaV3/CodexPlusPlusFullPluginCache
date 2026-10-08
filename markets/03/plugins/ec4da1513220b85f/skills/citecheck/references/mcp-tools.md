# MCP tool reference

Server: `https://objectionacademy.com/mcp`

`search` and `fetch` implement the compatibility contract used by ChatGPT
Company Knowledge and deep-research citation flows. Prefer the branded tools
below when jurisdiction filters or passage-level results are needed.

| Tool                        | Use                                                    | Important boundary                                  |
| --------------------------- | ------------------------------------------------------ | --------------------------------------------------- |
| `search_authorities`        | Search cases, citations, evidence topics, and passages | Covered corpus only                                 |
| `get_authority`             | Retrieve one document and stored passages              | Later-citing authorities are not a complete citator |
| `check_citations`           | Extract and deterministically look up citations        | Does not evaluate proposition support               |
| `explain_objection`         | Find authority relevant to an objection                | Educational explanation, not legal advice           |
| `create_objection_drill`    | Generate a short practice scenario                     | Answer before requesting the explanation            |
| `open_full_authority_check` | Open the hosted independent-review workflow            | Public, nonconfidential text only                   |

When the server is unavailable, disclose the outage and provide a manual research checklist. Never replace source verification with model memory.
