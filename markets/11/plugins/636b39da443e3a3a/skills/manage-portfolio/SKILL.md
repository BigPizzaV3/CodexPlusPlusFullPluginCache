---
name: manage-portfolio
description: Answer a landlord's questions about their rental properties through the PAM connector — rent and Direct Debits, compliance certificates (EICR, gas safety, EPC, alarms), open repairs, tenants, documents and PRS landlord-register readiness. Use whenever the user mentions their properties, tenants, rent, certificates, repairs or the landlord register.
---

Use the `pam` connector's tools. Everything is scoped to the signed-in landlord.

1. Call `list_properties` first and keep the ids. Other tools accept a property id or an address fragment ("12 High Street", "SS1 1EF"); if PAM says the reference is ambiguous, ask which property.
2. Pick the narrowest read tool for the question:
   - rent, due day, Direct Debit status, recent payments → `get_rent`
   - certificates and expiry dates → `get_compliance` (one property at a time; loop over `list_properties` for "across my portfolio")
   - repairs and what PAM is doing next → `get_maintenance`
   - who lives there and tenancy dates → `get_tenant`
   - landlord register / PRS database → `get_prs_readiness`
   - a copy of a document → `get_document_link` (a 24-hour link; say it expires)
   - a tradesperson near a property → `find_contractors` (read-only; it contacts nobody)
3. Reply in plain English with the figures that matter. Dates as "14 Mar 2027", money as "£1,250". Do not paste raw JSON or internal ids.
4. For "what needs my attention", combine `get_compliance` (anything expiring within 90 days or missing), `get_maintenance` (open jobs waiting on the landlord) and `get_rent` (missed or failed payments), and lead with the most urgent item.

Never guess a figure PAM did not return. If a tool says the connection lacks permission, tell the landlord to reconnect PAM from Settings → Integrations → Claude & ChatGPT.
