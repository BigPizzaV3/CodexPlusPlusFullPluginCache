---
name: get-started
description: Connect Lighthouse Hiring and run a first pipeline check. Use when someone has just installed Lighthouse Hiring or asks how to start using it.
---

# Get started with Lighthouse Hiring

Lighthouse Hiring is an applicant tracking system. The Lighthouse tools act as the signed-in
user, in the companies that user belongs to. Tools start in their active company; pass a
company's name or id as `company` to work in another one (`list_my_companies` shows them).

1. Call `whoami` and tell the user which company you are working in.
2. Call `posting_list` and show the open roles.
3. Offer three next steps, in the user's words:
   - "What needs attention in the pipeline?" (`report_pipeline_snapshot`)
   - "How long has each role been open, and has anyone reached interview yet?"
     (`report_time_to_stage`)
   - "Help me open a new role." (`posting_draft_start`)

If the connection is refused with "This account is not a member of any company", tell the user
to ask an admin at their company to invite them to Lighthouse, then reconnect.
