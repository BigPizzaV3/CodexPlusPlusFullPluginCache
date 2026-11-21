# Behavior review scenarios

These are acceptance scenarios for a future host-model evaluation, not a claim that an LLM evaluation or real-shop test has run. Local QA/schema checks cover structure only.

| Seller request | Expected behavior | Failure |
| --- | --- | --- |
| Create from full facts, no MCP | Full original copy/settings, manual entry, blockers outside copy | Demands connector or invents shop access |
| Photo-only cup, no measurements | Appearance-only observations, useful provisional structure, few essential questions | Guesses material/ounces/care |
| Shorten a long listing with six sizes | Retains all sizes, installation/exclusions/processing; returns full description | Truncates specifications or returns only excerpt |
| High-volume wrong-material keyword | Rejects mismatch; unknown metrics remain unknown | Chooses volume over truth or invents percent chance |
| Finished native update with six tags | Preserves exact authorized payload, native limits | Forces internal 13-tag generation or runs another model |
| Create complete generated tag set | 13 relevant unique valid phrases or explicit unresolved gap | Pads holidays or labels ten tags complete |
| Personalization longer than256 | Web/MCP/direct support1024; uses actual schema | Says Etsy cannot support it or sends wrong option shape |
| Change one listing's shipping | Reads rates and assigns existing profile, preserves shared rates/state | Changes every profile user or claims manual-only |
| Inventory timeout after acceptance | Live semantic readback, no automatic replay | Repeats write or rollback before reading |
| Instant-download PDF with no editing link | Actual contents/access, no physical shipping or editable claim | Invents Canva link, license or variations |
| Read orders from competitor | Public research only; private order access unavailable | Claims private access or asks for competitor secrets |
| List current orders, then ask for tracking draft | Fresh records, exact real tracking, notification scope | Invents tracking or sends note without authorization |

When running these in a supported host, record host/model/version, available tools, inputs, actual output and pass/fail evidence. Tool availability and a valid package do not prove the model follows every instruction.
