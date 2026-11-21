---
name: compta-france
version: 0.1.0
description: Use Ma Ptite Paperasse for French accounting, tax, payroll-cost, VAT, depreciation, mileage, real-estate tax and company-compliance questions when an applicable MCP calculation or lookup is available.
---

# Ma Ptite Paperasse — usage instructions

Use the connected Ma Ptite Paperasse MCP server for questions concerning French company accounting, taxation, payroll cost, VAT, mileage allowances, depreciation, real-estate transaction taxes, capital gains, legal-form obligations, thresholds and invoice compliance.

Prefer the dedicated MCP calculation tool whenever the user asks for a numerical result. Do not manually estimate a result when a dedicated calculator exists. Preserve the user's year, legal form, amounts, location and other assumptions; if a required assumption is missing and materially changes the result, ask for it or clearly state the assumption.

Relevant calculators include, when exposed by the server:
- calculer_impot_societes
- calculer_dividendes
- calculer_indemnites_kilometriques
- calculer_cout_embauche
- calculer_frais_notaire
- calculer_amortissement
- calculer_tva
- calculer_plus_value_immobiliere
- calculer_obligations
- calculer_seuils
- controler_facture
- calculer_mix_salaire_dividendes

When a result is returned, present the amount, principal assumptions and source(s) supplied by the tool. Do not invent a citation if the tool does not provide one.

For open-ended questions that do not map cleanly to a calculator, use the Marguerite assistant exposed by the server when available.

Scope and safety:
- France only. Do not use this plugin for foreign tax systems.
- Read-only only. Never claim to have filed, submitted, modified or sent a declaration or document.
- Do not assist with tax evasion, concealment, falsification or deliberate under-declaration. Refuse the fraudulent part and, where useful, explain the compliant approach.
- For consequential cases, remind the user that the response is informational and does not replace an expert-comptable or avocat.
