---
name: get-started
description: Set up HaulForza after installing the plugin. Confirm the HaulForza sign-in works, pick the company to work with, and show what the user can ask for.
---

# Get started with HaulForza

Run this right after the user installs the HaulForza plugin.

1. Call `list_companies`. If it fails because the user is not signed in, ask them to connect their HaulForza account and approve access, then try again. If they don't have an account, point them to https://www.haulforza.com.
2. If one company is returned, confirm it by name. If several are returned, list them by name and ask which one to use by default in this conversation.
3. Call `company_summary` for the chosen company for the current month and give a short overview: loads by status, revenue, driver pay and expenses. Quote the numbers exactly as returned.
4. Tell the user what they can ask next, for example:
   - "Which loads are in transit right now?"
   - "Show me the broker, stops and rate for load <load number>."
   - "List my active drivers."
   - "Create a load from Dallas, TX to Houston, TX for $1,800 picking up tomorrow."
5. Explain that HaulForza will always show the details and ask for a clear yes before creating a load or changing a load's status, and that invoiced, factoring and paid statuses are handled in the HaulForza app, not here.

Do not create or change anything during setup.
