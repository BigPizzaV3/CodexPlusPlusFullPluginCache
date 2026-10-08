---
name: genealogydirect
description: Use GenealogyDirect to find archive repositories, search visible genealogy requests, find recent requests, submit confirmed offers to help, or prepare and publish document-copy requests and research questions for a verified GenealogyDirect user. Trigger for genealogy archive discovery, document retrieval requests, family-history research questions, research offers, and GenealogyDirect marketplace work.
---

# GenealogyDirect

Use the authenticated `genealogydirect` MCP server for GenealogyDirect work. The connection uses the user's existing GenealogyDirect account through OAuth. If authentication is required, let the product open the GenealogyDirect sign-in flow; never ask the user for their password or token in chat.

## Available workflows

- Find archive repositories in a country with `retrieve_repositories`.
- Search visible document-copy requests and research questions with `search_requests`.
- Find recently created requests with `get_new_requests`.
- Retrieve the authenticated user's submitted and involved work with `get_my_requests`.
- Find visible open research questions with `find_open_research_questions`.
- Preview and submit an offer to help with `submit_offer`.
- Prepare and publish a document-copy request with `post_document_copy_request`.
- Prepare and publish a research question with `post_research_question`.

Country inputs use ISO 3166-1 alpha-3 codes such as `FRA`, `USA`, `GBR`, `CAN`, or `DEU`. Convert an unambiguous country name to its code. Ask a short clarifying question when the country is ambiguous.

## Read-only requests

Call repository and request searches directly once the country or filters are clear. Topic filters must be GenealogyDirect topic slugs. If the user gives an ordinary topic name and the corresponding slug is not known with confidence, omit the optional topic filter or explain that a recognized topic is needed; never invent a taxonomy value.

A document-copy request asks a researcher to obtain a specific record from a named archive repository. A research question asks the community to investigate or answer a broader genealogy problem; it may be free or open to paid offers.

Use `get_my_requests` whenever the user asks for "my requests", requests they submitted or posted, work they are helping with, or requests they are involved in. It requires no user identifier because the MCP uses the authenticated GenealogyDirect account. The `submitted` section contains the user's document-copy requests and research questions. The `involved` section contains assigned document-copy requests, assigned paid research questions, and free research questions where the user has written an answer or saved an answer draft. Preserve the returned active, completed, draft, and closed group labels when summarizing. Never ask for or display an internal user or request ID.

Use `search_requests` for general discovery such as "open requests", "available requests", "paid requests", or "requests where I can offer help". It has no creation-date cutoff and searches both document-copy requests and research questions by default. The phrase "open paid requests" means `open_only: true`, `paid_only: true`, and `request_type: all`. Never substitute `find_open_research_questions` when the user asks for all requests because that tool searches only research questions. Search filters include open status, paid status, request type, country, topic, repository, proximity, and result limit.

Use `get_new_requests` only when the user explicitly asks for new or recent requests, or requests created during the past X days. `past_days` defaults to 7, `request_type` defaults to `all`, and `paid_only` defaults to false, which includes both paid and unpaid requests.

A repository filter applies only to document-copy requests. Retrieve the repository ID with `retrieve_repositories`, then pass it internally to `search_requests` or `get_new_requests`; do not ask the user to find or type an ID. Supplying a repository ID automatically limits the request type to `doc_copy`.

Both request tools accept an optional `near` object containing `latitude` and `longitude`. It returns document-copy requests whose archive repository is within 100 km, matching GenealogyDirect's web-app behavior. Supplying `near` automatically limits the request type to `doc_copy`; never combine it with `research_question`. Do not claim that research questions have physical proximity. Coordinates are used for the search and are not a request ID or repository ID.

The MCP cannot determine the user's current coordinates, but the user should never be asked to provide latitude or longitude. For "near me" or another proximity request, use a city or postcode already present in the conversation and resolve its central coordinates before calling the request tool. If no location is known, ask the user only for their city or postcode. If the place is ambiguous, ask for the country or region needed to disambiguate it. Use a reliable non-interactive geocoding or knowledge source when available; ordinary city-center coordinates are sufficient for the 100 km search.

Stay within the GenealogyDirect MCP workflow: never open, inspect, or control Chrome, the GenealogyDirect web app, or any other application to obtain or infer the user's location. Do not use a saved application location or imply that GenealogyDirect has provided one.

Summarize results in plain language. Render every returned GenealogyDirect URL as a descriptive Markdown link, such as `[Archives de Paris](URL)` or `[Read the research question](URL)`. Do not display standalone record IDs, label a URL segment as an ID, or print bare URLs unless the user specifically asks for them. Do not expose private implementation fields or infer facts missing from the results.

When presenting requests or research-question search results, always state the returned currency for paid work. Treat it as authoritative for that request.

## Offer safety

`submit_offer` has a non-writing preview mode and a confirmed submission mode. Always follow this sequence:

1. Pass the selected request page link to `submit_offer` with `confirmed: false`. This submits nothing and returns the authoritative pricing mode, amount when fixed, currency, and exact default dates.
2. If pricing is `fixed_price`, do not ask the user to choose a price; clearly state the request's fixed price and currency and ask them to accept it. If pricing is `open_to_offers`, ask the user for their price in the request's returned currency.
3. For a research-question offer, also ask how many research hours are included.
4. Unless the user requests changes, use 7 days for offer validity and the returned default completion date, which follows the web app's 14-day default.
5. Present the complete offer summary: linked request, price and currency, validity date, expected completion date, research hours when applicable, and any message.
6. Ask: "Submit this offer on GenealogyDirect now?"
7. Only after explicit agreement, call `submit_offer` again with the reviewed values and `confirmed: true`.

Never infer confirmation from a request to preview, prepare, revise, or explain an offer. If any material value changes after confirmation, show the revised summary and ask again. The tool uses the user's connected payout account automatically; if none is available, explain that payout setup must be completed in GenealogyDirect account settings. Do not claim an offer was submitted when the tool returns `needs_input` or `confirmation_required`.

The offer currency is fixed by the request. Never ask the user to choose or change currencies, never perform currency conversion, and never describe an offer as being in a currency other than the one returned by the request or offer preview.

## Publishing safety

The two request-publishing tools create real, visible GenealogyDirect records. Always use this sequence:

1. Classify and refine the work using the intake rules below.
2. Gather the required information.
3. Present a concise final draft, including pricing choices and all supplied dates, people, locations, taxonomy values, and notes.
4. Ask: "Publish this on GenealogyDirect now?"
5. Call the relevant tool with `confirmed: true` only after the user explicitly agrees to that final draft.

Do not treat a request to draft, prepare, revise, preview, or explain as publication approval. If the user changes any material field after confirming, show the revised draft and confirm again.

### Mandatory intake classification

Classify the assignment before choosing a publishing tool. Explain the classification briefly when it is not obvious. Do not choose a document-copy request merely because the user mentions a type of record.

Use a document-copy request only for targeted retrieval of a document that is reasonably known to exist and can plausibly be found by requesting or consulting no more than one or two registers, volumes, files, or equivalent items. It must have:

- a selected repository that plausibly holds the document
- a specific document or record type
- identifiable party or parties
- a precise locality or jurisdiction
- an exact date or a date range no longer than five years

An exact call number, shelfmark, volume, or register reference is helpful but not required when the other details make the retrieval targeted.

Use a research question when the assignment requires discovering whether or where a record exists, searching broadly across registers or sources, correlating evidence, identifying a person or event, resolving conflicting information, or reaching a genealogical conclusion. An approximately dated baptism with an uncertain place is a research question, not a document-copy request. A request that is likely to require more than one or two registers or equivalent items is also a research question.

If the boundary is unclear, ask one short question about the single detail that would decide the classification. Never invent precision or silently narrow the user's facts. If a proposed document-copy request remains too broad, explain why and offer to turn it into a research question.

### Document-copy requests

First retrieve repositories for the country so the user can select a repository by name and page link. Pass the selected repository URL back to the publishing tool without asking the user for an internal identifier. Collect:

- repository
- document type
- location
- one or two people, each with first and last name
- either an exact date or a year range no longer than five years
- fixed price and currency, or open bidding
- optional title, call number, and notes

Before presenting the final draft, verify again that the repository, parties, place, and date identify a retrieval likely limited to one or two registers or equivalent items. If the type is `DTOTHER`, a document title is required.

If GenealogyDirect returns `needs_clarification`, no request was created. Present the assessment analysis and recommendation. Do not override a warning when the request is actually broad research; offer to reframe it as a research question. Retry with the returned assessment ID only when the user explicitly accepts the warning and the request still satisfies the targeted-retrieval rules above without altering the assessed request.

### Research questions

Collect a title, full question body, country, active GenealogyDirect period, active GenealogyDirect topic, source language, and whether paid offers are allowed. Period and topic values must be recognized GenealogyDirect IDs or slugs; do not guess them. Attachments are not supported in this initial plugin.

Every research question must be actionable before it is shown for publication confirmation. Assess and refine free and paid questions alike using the same standard as GenealogyDirect's web-app scope assistant:

- make the requested outcome explicit
- identify the main person, family line, or event
- give the useful place and approximate time frame
- preserve relevant known facts, uncertainty, prior searches, and constraints
- keep one bounded primary objective; suggest splitting unrelated objectives

If the draft is not yet actionable, ask one focused scope-defining question at a time, choosing only a question whose answer materially improves the assignment. Do not conduct the research, recommend sources, or demand unnecessary precision during refinement. Stop asking once a researcher could reasonably begin the assignment.

Then propose a polished title and a conservative full body in the user's language and first-person voice. Preserve every supplied fact and meaningful uncertainty, incorporate the user's answers beside the related information, and never invent, omit, or generalize details. If the original is already actionable, retain it with only useful clarity edits. Show this refined version as the final draft and obtain the normal explicit publication confirmation before calling `post_research_question`.

## Results

After a successful publication, state that it was created and render the returned URL as a descriptive link such as `[Open the document-copy request](URL)` or `[Open the research question](URL)`. After a successful offer, state that it was submitted and link the request rather than exposing an offer or request ID. If a tool returns a validation or authentication error, explain the specific correction needed without claiming that anything was published or submitted.
