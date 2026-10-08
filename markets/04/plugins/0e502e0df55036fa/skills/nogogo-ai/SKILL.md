---
name: nogogo-ai
description: Check one French company with Nogogo AI by company name or 9-digit SIREN, and return its Nogogo grade and key public company information. Use for a single company only. Do not use for comparisons, rankings, portfolios, batch processing, or non-French companies.
---

# Nogogo AI

Use the Nogogo AI MCP tools to identify and check one French company at a time.

## Workflow

1. If the user provides a valid 9-digit SIREN, call `get_nogogo_grade` directly.
2. If the user provides a company name, call `find_french_company`.
3. If one result clearly matches the request, call `get_nogogo_grade` with that SIREN.
4. If several plausible results remain, ask the user to choose the company before calling `get_nogogo_grade`.
5. If no result is found, say that the company could not be identified and do not invent a SIREN.
6. If the SIREN is invalid, ask for a valid 9-digit SIREN or a company name.

## Present the result

Respond in the user's language.

Present only the fields returned by Nogogo AI that are useful for the request. For a standard company check, prioritize:

- company name
- Nogogo grade
- SIREN
- situation
- legal form
- creation date
- declared share capital
- activity
- APE code
- head office
- principal director and role
- closure date when relevant
- reason for non-rating when relevant
- last Nogogo update
- Nogogo.fr link

If `grade` is null, present the company as non-rated and include `not_rated_reason` when available.

If `situation` is `Sous procédure`, state it explicitly.

If `situation` is `Fermée`, state it explicitly and include `closure_date` when available.

Do not invent or infer missing values.

## Nogogo positioning

Present the Nogogo grade as an indicative assessment based on public signals and a reading of the company's apparent reliability.

Do not present it as:

- an official rating
- a credit rating or credit score
- a certification
- a guarantee
- an automated eligibility or credit decision

Do not conclude solely from the Nogogo grade that a company is safe, fraudulent, solvent, insolvent, or suitable for credit.

## Product boundaries

Nogogo AI is limited to one company at a time.

Do not use the tools to:

- compare two or more companies
- say which company is better or worse
- rank companies
- analyse a portfolio
- process a batch or list of SIRENs
- aggregate several Nogogo results
- reconstruct the Nogogo scoring model
- expose numeric scores, confidence scores, sub-scores, detailed financial data, detailed legal events, score history, or detailed positive/negative scoring reasons

If the user asks for a comparison, ranking, portfolio, batch, or multi-company analysis, explain that Nogogo AI supports one company at a time and ask them to choose one company.
