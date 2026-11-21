---
name: requstory-setup
description: How to start with Requstory in ChatGPT, with or without signing in.
---

# Getting started with Requstory

Requstory maps how a company works from its public website: teams, processes, customer journey, and an ease-of-business score with the gaps behind it.

## Without signing in
- Look up a company: "What is the ease score of monzo.com?" (search_companies, get_company_score)
- See who owns each team where the company published it: get_company_owners
- Check whether AI agents can read and use a website: check_ai_readiness
- Try the order-to-cash agents on a made-up store: start_o2c_demo

## With a free Requstory account
The first account tool asks the person to sign in (Google or an email link). Then:
- map_website maps a website into their account, then get_map and ask_map read and question it
- list_maps lists their saved maps; get_account shows what their account includes
- start_o2c_run runs the order-to-cash agents on their own data

The order-to-cash agents stop for the person's decision on credit limits, short stock, packing, reminders, unclear payments and returns; list_o2c_exceptions shows those questions and resolve_o2c_exception records the person's choice.
