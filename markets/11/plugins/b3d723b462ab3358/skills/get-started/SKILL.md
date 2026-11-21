---
name: get-started
description: How a Five Dots session begins, where the client keeps their work, and the information exchanged with the methodology service.
---

# Getting started with Five Dots

Five Dots is connected as the `five-dots` MCP server. It supplies RevOps and go-to-market
methodology: the GTM Audit, a knowledge base and a skills library.

1. The session guide explains the capabilities, operational help and workflow for work the
   client chooses. `get_playbook` returns it.
2. The client chooses where their assistant keeps their work, using a separately authorised
   workspace connection or the conversation itself. Five Dots does not directly read their CRM
   or workspace. Access or changes through other tools require the client's authorisation.
3. Five Dots tool inputs are narrow selectors: the audit scope or module ids, which CRM the
   audit can read (hubspot, salesforce, other or none), an optional target date, run or content
   identifiers, and short generic search/help terms. No tool takes the names of other connected
   tools, the workspace or its status, the company name, or the conversation. Keep business
   records, personal names, findings, figures, credentials and conversation transcripts out of
   those inputs.
4. The connection identifies a Five Dots account and, where applicable, its member. Five Dots
   retains account information, run records and service-usage events. Responses return methodology
   and audit module lists to the assistant and may repeat supplied selectors or search terms. Do not describe
   this as anonymous use or claim that Five Dots holds no data or history.
5. For data uses, recipients, retention and controls, refer to https://fivedots.ai/privacy.
   Disconnecting the plugin stops future calls from that connection; deletion of the account,
   assistant conversation and workspace copies are separate controls.
