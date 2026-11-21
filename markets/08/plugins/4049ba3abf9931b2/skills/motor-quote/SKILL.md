---
name: motor-quote
description: "Obtain or continue an esure motor insurance quote. Use when a user asks for a car or motor insurance quote, provides quote details, wants to continue a quote journey, or asks for a premium using the esure motor quote tools."
---

# Motor quote journey

At the very start of the user quote journey, before asking any quote questions, state the following to the user verbatim:

**To find out how esure processes your personal data, please see our [privacy notice | esure](https://www.esure.com/privacy). The data controllers are esure Insurance Limited and esure Services Limited. We use automated decision-making processes. To check your eligibility for payments, we’ll carry out a credit check. This won’t affect your credit score unless you choose to pay monthly. The credit reference agency we use is Experian.**

Guide the user through one quote journey at a time. Collect the five groups below in order and use the MCP tools exactly where instructed.

Before submitting, read [references/quote-schema.md](references/quote-schema.md) and map the user's answers to the exact tool schema. The reference contains accepted literals and field names; do not ask users to provide internal literals.

## Conversation state

- Extract and retain every usable answer the user has already supplied.
- Never ask the user to repeat a valid answer.
- Do not invent, assume, or silently default customer information.
- Complete the current group, including required tool calls and confirmations, before mentioning or asking about a later group.
- Ask all independent outstanding questions in the current group together, in listed order. Ask separately only when the next question depends on a tool result or conditional answer.
- Accept answers in any reasonable format or order. Clarify only missing, ambiguous, unsupported, or invalid answers.
- Do not reveal internal field names, enum literals, schemas, or implementation details unless the user asks.

## Group 1: Find the car

1. Ask only for the UK vehicle registration.
2. Call `lookup_car_by_registration` as soon as a registration is supplied.
3. Show the returned make, model, and registration date. Do not convert the registration date to a claimed model year.
4. Ask the user to confirm the vehicle.
5. After confirmation, ask when they bought or started to lease this car. The date must be on or after the returned registration date and cannot be in the future.

If the lookup fails or returns nothing, tell the user it did not work this time and ask them to try the registration again. If it fails a second time, stop retrying and direct them to esure.com, where they can look up their vehicle by make, model, and other details instead. If the user rejects the returned vehicle, ask for a corrected registration and repeat the lookup under the same two-attempt rule. Retain the returned `abi_code` and `registration_date` for submission but do not expose the ABI code unless asked.

Do not begin Group 2 until the vehicle is confirmed and the purchase or lease start date is known.

## Group 2: Personal details

Ask together for:

1. Title.
2. First name.
3. Surname.
4. Email address.
5. Date of birth. The customer must be at least 17 years old.
6. UK postcode.
7. House number or house name, which is optional.

After receiving the postcode, call `lookup_address_by_postcode`, including the house number or name when supplied. Present the matching address or a concise numbered list if several addresses are returned. Ask the user to select and confirm the correct address. Preserve the selected result exactly for submission.

If no correct address is returned, ask the user to correct the postcode or house identifier and repeat the lookup. Do not begin Group 3 until every personal field is valid and an address is confirmed.

## Group 3: Driving history

Ask together for:

1. Driving licence type. Offer these choices:
   - Full UK licence.
   - Full UK automatic-only licence.
   - Provisional UK licence.
   - Full EC or EEA licence.
   - Provisional EC or EEA licence.
   - Licence issued outside the UK, EC or EEA.
   - Other.

   If the customer's answer does not match one of these, apologise and explain that a quote cannot be produced.
2. Number of years and months they have held the licence.
3. Years of No Claims Discount (NCD).

The customer must be at least 17 years old, and their stated licence duration must not imply that they held a licence before their 17th birthday.

Do not begin Group 4 until Group 3 is complete.

## Group 4: A bit more about you

Ask together for:

1. Relationship status. Offer these choices: married, single, living with partner, widowed, divorced, or separated.
2. What they do for a living (occupation).
3. Whether they use any other vehicles. Offer these choices:
   - No, they do not use any other vehicles.
   - Yes, they have access to another vehicle they do not own.
   - Yes, they own another vehicle.
   - Yes, they are a named driver on another vehicle.

Do not begin Group 5 until Group 4 is complete.

## Group 5: Cover needs

Ask together for:

1. Estimated annual mileage.
2. Cover start date.

The cover start date cannot be in the past and must be no more than 30 days from today. Ask all outstanding or invalid Group 5 questions together.

## Submission

Before calling `submit_insurance_quote_request`, verify all of the following:

- Every required field in all five groups is present and valid.
- The user confirmed the vehicle returned by the lookup.
- The user selected and confirmed an address returned by the lookup.
- Human answers have been mapped to the exact object fields, types, date formats, and literals in [references/quote-schema.md](references/quote-schema.md).
- No value was inferred merely from another answer.

Then summarise every collected and interpreted answer back to the user in plain English, grouped by section, and ask them to confirm before you continue. Use the human-friendly wording, not internal literals (for example "Full UK licence", not `FullUK`). Include the confirmed vehicle, purchase or lease date, personal details, chosen address, licence type and duration, NCD years, relationship status, occupation, other-vehicle use, annual mileage, and cover start date. If the user asks to change anything, update those fields and re-summarise before proceeding.

After the user confirms the summary, say verbatim:
"Thanks — I’ll submit these details now to retrieve your quote."

After each explicit confirmation of the complete summary, call
`submit_insurance_quote_request`. Never make duplicate calls for the same confirmation. Do not call it to discover missing fields or test a partial request.

Display the returned quote result and checkout action. Do not invent, recalculate, round, or modify the premium. The result includes `selected_occupation`. If it differs from the occupation supplied by the user, tell them which occupation was selected and ask them to provide a different or more specific job title if they are not happy with it. If the user provides a new job title, update only the occupation, re-summarise the answers, obtain confirmation, and make one new quote request. If they are still unhappy with the selected occupation after that request, direct them to the [esure car insurance quote journey](https://www.esure.com/car-insurance), where they can enter their details directly and complete their quote. If an explicit error says that the occupation could not be found, ask the user to provide a different or more specific job title, then update only the occupation, re-summarise the answers, obtain confirmation, and make one new quote request. If an error says that a quote could not be generated, do not imply a system fault or apologise for a technical problem. Tell the user that, based on the details provided, esure isn't able to offer them a quote at this time. Do not speculate about which detail caused this. Allow no more than two submission attempts in total. If the second submission fails, or the user asks to try again, explain that the outcome is unlikely to change and direct them to the [esure car insurance quote journey](https://www.esure.com/car-insurance), where they can enter their details directly and explore other options.

Submission-attempt limits are internal safeguards. Do not mention or emphasize the number of tool calls or submission attempts to the user.