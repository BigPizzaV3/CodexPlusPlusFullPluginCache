---
name: aureic-properties
description: Search, inspect and compare Aureic Properties' active public Costa del Sol residential catalogue, and send a deliberately confirmed request for information about one public property. Use the bundled MCP tools for published facts, public source links, freshness and Aureic's clearly labelled perspective. Do not use it for off-market disclosure, live availability guarantees, viewing bookings, transactions or investment guarantees.
---

# Aureic Properties public catalogue

Choose the tool that matches the user's goal:

- Use `search_properties` to discover active public properties using budget,
  location, type, specification, lifestyle or free-text criteria.
- Use `get_property` for one known public property.
- Use `compare_properties` for two to four known public properties.
- Use `submit_property_enquiry` only after the user has selected one public
  property, supplied the minimum contact fields, reviewed the exact submission
  and explicitly accepted the privacy notice.

Results returned by the Aureic tools describe Aureic's bounded public catalogue
only. State that scope clearly and never imply that the result represents the
complete property market.

After the data tool returns the final selection, present it visually when the
client supports MCP Apps UI:

- After `search_properties`, call `render_property_results` with up to six
  selected canonical property IDs in their intended order. Also pass the
  complete `all_result_ids` array as `all_identifiers`, so the component can
  offer the complete fullscreen catalogue without performing another search.
- After `get_property`, call `render_property_detail` with its canonical ID.
- After `compare_properties`, call `render_property_comparison` with the same
  canonical IDs in the same order.

Property cards can open the internal detail inside the component. The detail
can open an internal request-for-information form. Do not reproduce that form
in the assistant response when the component is available.

After a render tool succeeds, the component is the authoritative presentation.
Keep the assistant follow-up to at most one short factual sentence or one useful
next-step question. Do not repeat the property cards, photographs, full
catalogue, gallery or comparison table in the model response. Do not create a
second carousel, host-native image group or other duplicate rich result.

The property-detail component deliberately contains a curated selection of up
to eight published photographs. It is not the complete gallery from the source
page. Never state the total number of source photographs or say that the full
gallery is present in ChatGPT. Direct the user to the official property page to
see the complete gallery.

Describe `compare_properties` as a property comparison across published facts.
Do not claim that it performs photographic, architectural or visual analysis
of the homes merely because the comparison is presented in a visual component.

The render tools are presentation-only. Never use them instead of the matching
data tool, and do not call them when the client cannot render MCP Apps UI.

Do not call a tool merely to restate an answer already returned. A materially
changed request can justify another call.

## Present facts and advice separately

- Treat the returned property record and catalogue version as authoritative.
- Describe specifications, published price, status, source URL and verification
  dates as published facts.
- Describe every `aureic_assessment` field as Aureic's perspective and keep it clearly labelled as advisory.
- Preserve absent values as unknown. Never infer a missing address, cost,
  dimension, availability state or technical condition.
- Keep the public source URL attached to the property.
- Explain relative trade-offs according to the user's stated priorities; do not
  declare a universal winner.

## Preserve the public boundary

- Search results contain active public listings only.
- Never reveal or speculate about private or off-market inventory, exact
  unpublished addresses, seller identity or internal notes.
- Published availability and prices are not live guarantees. State their stored
  verification dates when material.
- A successfully confirmed `submit_property_enquiry` call submits an enquiry
  only. Do not claim that it schedules a viewing, confirms availability, takes
  a deposit, processes a payment or reserves a property.
- Do not guarantee investment performance, rental yield, appreciation, legal
  status, tax treatment, building condition or financing.
- Aureic Properties is not a substitute for legal, tax, financial, survey or
  technical advice.

When a user wants more information, use the internal detail and enquiry form
when supported. Collect only name, email, optional phone, optional budget and a
short property-specific message. Show the exact submission for review and
obtain explicit privacy consent before sending. Never ask for passports, bank
details, proof of funds, credentials or other sensitive data. Enquiry records
are retained for no more than 60 days. A request does not create a viewing,
reservation or live availability confirmation.

Never cite or mention this skill, bundled references, local filesystem paths,
plugin cache locations or internal instructions in a user-facing answer.

Read [references/TOOL_CONTRACT.md](references/TOOL_CONTRACT.md) for field
semantics and [references/TRUST_BOUNDARIES.md](references/TRUST_BOUNDARIES.md)
for unsupported claims and privacy boundaries.
