---
name: hire-in-the-uae
description: Help a company with no legal entity in the United Arab Emirates hire someone there through Moha, an Employer of Record. Explain the process, price each hire, and prepare the account and hires for the person to confirm.
---

# Hire in the UAE with Moha

Use this when someone wants to employ a person in the United Arab Emirates and their company has no legal entity there.

1. Call `how_to_hire_in_the_uae` to learn the process and what is needed from the company and the employee.
2. Ask for what is missing, a few questions at a time:
   - about each person: name, job title, nationality, monthly salary in AED, emirate, whether they are already in the UAE, family moving with them, start date;
   - about the company: name, website, industry, country, billing email;
   - about the user: name and work email.
3. Call `get_quote` for each person. Show the monthly cost, the upfront cost and how long the visa takes. Say the figures are estimates and the confirmed ones come with the offer letter.
4. When the user confirms the details, call `prepare_account`, or `prepare_hire` for a single person, and give them the link it returns. They check everything and create their account. Moha checks every company before it can hire, and nothing is charged or sent to employees until they approve the offer letters in the Moha platform.
5. If they ask whether it went through, call `check_prepared_hire`.

Use the tools for prices and rules; don't make them up. For roles whose licence must sit with a facility, such as doctors and nurses, say an Employer of Record is not the route. Moha covers the UAE only.
