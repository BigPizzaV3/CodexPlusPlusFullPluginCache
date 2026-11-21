---
name: foreign-associate
description: Use when a user needs a trademark, patent or design attorney in another country (a foreign associate or local agent) - checking that country's rules, shortlisting attorneys on IPRwise and writing the instruction letter. Uses the IPRwise connector.
---

# Choosing and instructing a foreign associate

This skill gives the method for helping an IP professional or a business find and instruct an attorney in another country. The IPRwise connector supplies the data; this skill says how to use it.

## If the connector is not connected

If the IPRwise tools (`country_ip_facts`, `find_attorneys`, `filing_routes`) are not available, ask the user to connect IPRwise in the app's settings and sign in with an IPRwise account (Google, LinkedIn, Microsoft or e-mail). Without the connector, do not present a country's rules as facts: say they are unverified.

## Workflow

1. **Pin down the matter.** Right (trademark, patent, design), country, action (new filing, response to an office action or a Madrid provisional refusal, opposition, renewal, recordal of an assignment, enforcement), the deadline and the client. Ask only for what is missing.
2. **Check the country's rules first.** Call `country_ip_facts`. Note whether foreign applicants need a local agent, the power of attorney formalities (simple signature, notarisation, legalisation or apostille, and any deadline to file it), the filing language, the opposition period and the terms. Cite the source link the tool returns. Put in quotation marks only the text given in its "Quote" lines. If the tool has no data for the country, say so and treat the rules as points to confirm with the local attorney.
3. **Check the route.** If the matter could run through Madrid, Hague, PCT or a regional office, call `filing_routes` with the country and the client's home country.
4. **Shortlist attorneys.** Call `find_attorneys` with the country, adding `practice` and `city` when they matter.
   - Present verified IPRwise members first and say what "verified" means: IPRwise checked their identity and professional registration.
   - Present the other entries as "from public sources" and name the source the tool gives.
   - Suggest two or three candidates with their iprwise.com profile links.
   - Never invent e-mail addresses, phone numbers or fees.
   - If the list is thin, give the directory page from the tool's answer: the user can ask IPRwise for an introduction there.
5. **Questions for the candidate before instructing:** a fee estimate split into official and professional fees, with currency and payment terms; the timeline; the documents needed and their formalities (original power of attorney, legalisation, translations); a conflict check; the attorney who will handle the file; the reporting language and channel.
6. **Draft the instruction letter** using the template below, in the language the associate works in (English unless the user says otherwise).

## Instruction letter

- **Subject:** client reference, country, right, action and the deadline.
- **Opening:** one sentence saying who is instructing and on which matter; ask for an acknowledgment within two working days.
- **Matter data, as a list:** applicant or holder (name, address, nationality), the mark, title or design, application or registration numbers, classes and specification, priority claim (country, number, date), enclosed documents.
- **Instructions:** what to do and by when. Set an internal deadline one to two weeks before the official one and state both.
- **Costs:** ask for a fee estimate to approve before work starts, unless the deadline does not allow it.
- **Reporting and billing:** who receives reports; invoice details.
- **Closing:** confidentiality and the contact person.

## Rules

- Do not calculate a statutory deadline from memory. Use the period `country_ip_facts` returns, show the calculation, and tell the user to confirm it with the local attorney.
- One instruction per paragraph. Data goes in lists, not inside sentences.
- This is reference information, not legal advice; say so when the user is about to act on it.
