---
name: heffl-sales
description: "Create or update Heffl deals, convert leads, move opportunities between pipeline stages, and prepare quotations or estimates for clients."
---

# Deals and quotations

Read ../heffl-crm/references/operating-rules.md before writes. Discover current write schemas with records_describe, surface:"write", mode:"create" or "update".

Deals use object:"deals". Creation requires title, clientId and stageId even when field metadata omits a required flag. Resolve clients with records_resolve. Read pipelines_list and pipelines_details to find stages. If the pipeline is unspecified and multiple plausible pipelines exist, clarify. Use a requested stage, otherwise the first ACTIVE stage in the chosen pipeline. Re-describe custom fields for the chosen pipeline when needed. Deal value is price; do not invent value, amount, probability or conversionRate fields. The pipeline is derived from stageId. Move, close or reopen through records_update with values.stageId; the shared handler derives ACTIVE/WON/LOST and checks destination requirements. Use leads_convert for lead conversion.

Quotations use object:"quotations". Describe creation to obtain fields, defaults and template candidates. Resolve clientId and supply at least one lineItem. Prefer the user-named template, a unique service match, or a generic template; when several templates remain and terms materially differ, clarify. Follow the described templateId/contentHtml rules and required custom fields for the selected template. Do not invent a deal linkage from a quotation title.

Lines use name, quantity and price, plus described discounts/taxes. For a free-text service explicitly set productId:null to suppress catalogue inference. Do not compute or send derived totals. Clarify how to allocate a fixed discount across multiple lines when unspecified. Preserve requested currency and tax-inclusive pricing. Creating a quotation does not send it; discover a supported send action before claiming delivery. Return the saved record and returned link only after a successful receipt.
