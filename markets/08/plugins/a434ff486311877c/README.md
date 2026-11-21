# DomainKits plugin for ChatGPT and Codex

DomainKits connects ChatGPT and Codex to domain data: newly registered, expired, deleted, aged, and active domains, with WHOIS (RDAP), DNS, reverse nameserver, registrar, EPP status, IP, availability, TLD price, typosquat, and keyword and TLD registration trend lookups. The model does the analysis.

## Who it's for

- **Brand protection:** new registrations and lookalike domains that contain a brand name, and where the name is registered across TLDs.
- **Security teams:** pivot from a suspicious domain to its registrar, nameservers, and other domains on the same nameservers.
- **Naming and acquisition research:** availability, recently deleted names that may be registrable again, and TLD prices.
- **Market research:** keywords and TLDs gaining new registrations.

## Package contents

```
domainkits/
├── plugin.json      → package manifest and listing metadata (Agent Plugins format)
├── mcp.json         → remote MCP server: https://api.domainkits.com/v1/mcp (Streamable HTTP)
├── skills/          → getting-started skill and nine workflow skills
└── assets/icon.png  → listing and composer icon
```

| Skill | What it does |
|---|---|
| get-started | First-run orientation: what DomainKits does, four starting points, routing to the right workflow |
| domainkits | Tool guide: which tool fits each lifecycle stage, how to combine and report results |
| brand-protection | Typosquat and lookalike scan around a brand, with a per-domain assessment |
| domain-analyze | Evidence-based picture of one domain: registration, DNS, backlinks, cross-TLD footprint, market and legal context |
| domain-cma-valuation | Comparative market analysis against current for-sale substitutes in the same keyword market |
| domain-generator | Brandable names from a keyword, concept, or taken domain, checked for availability |
| domain-name-advisor | Naming consultation across registration, drop, backorder, and aftermarket paths |
| keyword-intel | Evidence map for one keyword, with search, advertiser, registration, supply, and transaction layers kept separate |
| keyword-trend-hunter | Registration keyword spikes, validated against new-registration cohort signals |
| domain-market-beat | Time-bounded domain-market briefing with source tiers |

The package ships no executable code and reads no local files.

## Data and privacy

Queries (domain names, keywords, search filters) are sent to `api.domainkits.com` to fetch results. Search and lookup tools are stateless. Three tools store data on the user's DomainKits account, and only after the user enables memory:

| Tool | What it stores |
|---|---|
| `monitor` | The domains the user watches and the results of each check |
| `preferences` | Saved preferences and the memory switch |
| `strategy` | Strategy text the user wrote, run timestamps, and the most recent result |

Stored data is encrypted with AES-256-GCM and kept separately for each user. The user can delete all of it at any time (GDPR Article 17). WHOIS results carry registrar, dates, status codes, and nameservers only, not registrant personal data.

Privacy policy: https://domainkits.com/privacy · Terms: https://domainkits.com/terms · Plans and limits: https://domainkits.com/mcp

## License

Code: MIT (see [LICENSE](LICENSE)). Domain data is provided by [DomainKits](https://domainkits.com) under its own terms.
