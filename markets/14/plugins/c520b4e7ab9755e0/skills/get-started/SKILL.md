---
name: get-started
description: Search and read the Corridome register of private-market firms, deals, companies and people.
---

# Corridome

Corridome is a register of investment advisers, broker-dealers and the private-company deals they work on, compiled
from SEC filings and firms' own websites. Each record names the document it comes from.

The tools:

- `search_firms` finds a firm by name, short name or SEC number, and returns its id.
- `get_firm` reads one firm by that id: its funds, deals, portfolio, the firms it works with, and its people.
- `search_deals` finds deals by company name, or by a firm and its role, state, deal type, disclosed value and year.
- `get_deal` and `get_company` read one deal or one company by id.
- `search_people` finds people by name, title, firm, state and kind of published contact.

A firm's id comes from `search_firms`; deal and company ids come from the deal and firm results. Each result includes
its corridome.com address and the source document's address. `search_people` and `get_firm` say which kinds of contact are published for each person. With `include_contacts`, they also return the contacts, one credit each from the member's monthly allowance; every such answer gives the credits spent and left, and the reset date.
