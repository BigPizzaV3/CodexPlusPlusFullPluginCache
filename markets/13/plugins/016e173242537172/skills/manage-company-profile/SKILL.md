---
name: manage-company-profile
description: Keep an employer's Himalayas company profile accurate and attractive to remote candidates, covering the about text and summary, size, founding year, locations, social links, perks and benefits, and tech stack. Use when the user wants to review, set up or update their company's profile, perks or tech stack on Himalayas.
---

# Manage the company profile

Follow [himalayas-basics](../himalayas-basics/SKILL.md) for the shared rules.
These tools need an employer account.

## 1. Review

Call `get_company_profile`, `get_company_perks` and, for comparison,
`get_company_details` with the company's slug (the public view candidates
see). Report what is missing or thin: about text, summary, size, founding
year, locations, social links, perks and tech stack.

## 2. Update the profile

`update_company_profile` changes only the fields you pass: `about`,
`summary`, `ceo`, `num_employees_range`, `year_founded`, `location_list` and
social links. Draft new text, show it, and write after the user confirms.
Read the profile back.

## 3. Perks

- `add_company_perk` adds a perk with a `title` and a `category` from the
  fixed list (healthcare, retirement, parental leave, equity, home office
  budget, learning budget and more; see the tool's enum).
- `remove_company_perk` removes one by id. Confirm first.

Remote candidates look for location-independent pay, home office budgets,
time off and learning budgets. Suggest only perks the user says the company
offers.

## 4. Tech stack

`update_company_tech_stack` takes technology names (such as `React` or
`Python`) and matches them to Himalayas' catalogue. Read the profile back to
see what matched.
