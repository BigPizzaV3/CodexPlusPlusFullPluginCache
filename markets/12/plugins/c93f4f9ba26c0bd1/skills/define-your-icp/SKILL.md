---
name: define-your-icp
description: Define who a team sells to, as an ideal customer profile (ICP). Use when someone says who their ideal customer is, wants to describe their target market, or wants to decide who counts as a good lead.
---

# Define an ideal customer profile (ICP)

An ICP says who is worth contacting: the companies, and the people inside them. It has two
parts, and they do different jobs.

- **Filters** carve out a broad group to search: places, job titles, industry, company size.
- **Checks** are the real test. Each check is one yes/no question about one public fact.

## Rules

- **One ICP at a time.** If the person describes several buyers, help them pick the sharpest one
  first. The others can come later.
- **A check asks ONE thing, in at most 250 characters.** If it has an "and", a list of
  exceptions, or two ideas, make it two checks. Most good checks are under 100 characters.
- **A check must be answerable from public information.** "Is a B2B software company" works.
  "Owns the tooling budget" does not: nobody publishes it. If a person with only public pages
  could not answer it, do not write it.
- **Translate a pain, never restate it.** If the person says "they have no CRM", ask: what is
  publicly true of a company that has this pain? Write that.
- **Write it so "yes" is good:** "is an architecture studio, not a staffing firm".
- **Places, job titles, industry and size go in the filters, not in a check.** The same for lists
  of companies to avoid.
- **Do not use dates or sums in a check.** Ask about the fact itself.

## Steps

1. Ask what they sell and who bought best. Look up what you can before you ask, starting with
   `workspace_profile_get`, which holds what the workspace has already said about its offer. Ask
   only what you cannot find. Save a better answer with `workspace_profile_update` once the
   person agrees; it replaces that whole section.
2. Propose a place first, then ask them to confirm it. Set only what they confirm, and say it
   back in plain words.
3. Create the ICP with `icp_create`. It is a **draft**: nothing can use it yet. Show the person
   the filters and each check in plain words.
4. Change it with `icp_update`. Send only the fields that change. Rewrite or split the ONE check
   that decided a case. Never add an exception to an existing check; a new rule is a new check.
5. Look at `icp_get` to see what publishing would change.
6. **Ask before `icp_publish`.** Publishing makes this ICP decide who counts as a fit, and it can
   use the workspace balance for re-checks. Say that, then wait for a yes.
7. After it is live, go to the `qualify-a-list` skill to test it on a few people.

## How to know it is good

A good ICP, tested on ten people who should fit, passes about six in ten. If most people come
back "not sure", a check asks for something nobody publishes: rewrite it. If the list is full of
the wrong kind of company, the search is too wide, not the ICP.

Say what you changed and why, so the person can disagree with the reasoning.
