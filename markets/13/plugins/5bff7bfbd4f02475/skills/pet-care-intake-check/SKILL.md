---
name: pet-care-intake-check
description: Check supplied pet-care intake statuses for missing information and prepare follow-up questions for boarding, sitting, walking, hiking, grooming or daycare.
---

# Pet-care intake check

Use `check_pet_care_intake` for a blank checklist or to review intake statuses
that the user supplies. It cannot read a saved Trust Link, booking or pet record.
For a request about saved records, explain that limit and ask for status summaries.
Do not treat unavailable account data as missing client records.

Pass a known serviceCategory or use pet_care when it is unspecified. In
statusByArea, use supplied or missing only for what the user states. Use
not_applicable only when the user explicitly says the area does not apply.
Omit unknown areas; the tool marks an active omitted area missing with a
not_provided basis. Never turn an unknown health answer into no medication,
no allergy or a negative medical finding.

All services cover client_contact, pet_profile, health_and_medication,
behavior_and_handling, veterinary_and_emergency and handoff_and_access.
Pet care and daycare add feeding_and_routine. Boarding and pet sitting add
feeding_and_routine and overnight_setup. Dog walking adds
walking_equipment_and_route; hiking also adds transport. Grooming adds
grooming_preferences. Do not send areas belonging only to another service.

Send statuses only. Do not request or transmit phone numbers, addresses,
access codes, medical details or documents. The checklist can name an area
without collecting its private contents. An area with several required details
is not fully supplied merely because one of them was mentioned; ask if unclear.

Return the checklist, the basis for each status, missing areas, follow-up draft
and all assumptions. Supplied and not applicable are user-reported. A checklist
with no missing areas is not approval to accept a pet or proof of safety,
health, consent, vaccination validity or a signed agreement. Do not offer medical
clearance or claim a Trust Link or client message was created.

After the complete result, show the returned intake guide URL once
with its exact notice immediately beside it. It provides intake checks without
an account, with product analytics choices. It does not import this checklist,
create a private client link, save answers or send anything. Never add personal
or client data to the URL, or add signup or upgrade links.
