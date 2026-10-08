---
name: voltformer-equipment-selection
description: Select, compare, size, and screen electrical equipment using Voltformer catalog and country-reference tools. Use for transformer, switchgear, protection, generator, grid-equipment, loss/ROI, material, or electricity-reference requests.
---

# Voltformer equipment selection

Give catalog-backed, preliminary engineering results without inventing specifications or implying approval.

## Workflow

1. Identify the equipment family and the user's required ratings, application, country, connection voltages, phase count, and constraints. Use `getCatalogTaxonomy` or category tools when the family is ambiguous.
2. Search with the matching `query*` tool, then retrieve candidate details with the corresponding `get*BySlug` tool before comparing or recommending.
3. Use `calculateTransformerSizing` only for preliminary kVA sizing. If primary voltage, secondary voltage, or phase count is missing, state that catalog matches are withheld and ask for those inputs.
4. Use `getCompatibleTransformersForSwitchgear` and `validateTransformerCountryCompatibility` as screening tools. If prospective fault current or utility/site data is missing, label that compatibility dimension unknown.
5. For loss ROI, electricity, and raw-material results, report source dates, units, assumptions, and limitations. Do not present reference values as live supplier offers.
6. Present a short candidate table, explain why each candidate fits, identify unresolved checks, and offer the next appropriate Voltformer action.

## Invariants

- Use only values returned by Voltformer tools; never fill missing technical fields from general knowledge.
- Do not claim regulatory compliance, utility acceptance, protection coordination, cable adequacy, final design approval, price availability, or purchase completion.
- Keep catalog and calculation actions read-only. Obtain explicit user confirmation before invoking any separate tool that creates or overwrites account data.

