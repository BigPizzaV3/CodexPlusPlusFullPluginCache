---
name: company-researcher
description: Builds a structured profile of one German company — master data, business model, management, financials and recent register changes — from the Implisense tools. Use when the user asks about a single German company by name, website, VAT ID, LEI or register number.
---

# Company Researcher

Turn a question about one German company ("Tell me about TRUMPF", "Research the company behind check24.de") into a structured, sourced profile. Answer in the user's language.

## Workflow

1. Call `company_profile` with the identifier the user gave (name, website, VAT ID, LEI or register court + type + number). Pass `include=people,financials,announcements` for a complete picture.
2. If the result is ambiguous, `meta.candidates` lists the matches. Ask the user which one they mean (city or register number), then call again. Never pick one yourself.
3. If `meta.confidence` is `low`, say that the name matched only fuzzily.
4. If the user asks what changed recently, call `recent_changes` with the company `id` and a `since` date.
5. If the user asks for competitors or comparable firms, call `similar_companies` with `seed_id`.
6. If the user asks whom to contact in a specific function (sales, purchasing, IT, …), follow the `contact-finder` skill.

## Profile structure

- **Master data**: name, legal form, registered seat (city, state), founding date, size class, industries, register number, VAT ID.
- **Business model**: two or three sentences from `summary` — what the company does, for whom, what stands out.
- **Management**: managing directors, board members and authorized signatories with their roles.
- **Financials**: latest available year with its year stated — revenue or balance-sheet total, net income, equity and equity ratio. If several years are available, a short trend. A brief qualitative reading: profitable? solidly capitalised?
- **Recent changes**: relevant register announcements, if requested.
- **Assessment and open questions**: one or two sentences on what to check next.

## Rules

- Use only what the tools return. If a figure is missing, say so — never estimate or invent numbers.
- Always state the financial year next to a figure.
- No forecasts; interpret historical data only.
- For several companies at once use the `portfolio-analyst` skill; for prospect lists use `lead-qualifier`; for contact persons use `contact-finder`.
