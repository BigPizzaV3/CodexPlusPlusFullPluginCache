---
name: lead-follow-up
description: Review Zylu customer enquiries and record a follow-up outcome or task. Use when a user asks to find leads, review follow-ups, log contact activity, or assign a follow-up task.
---

Help users manage a lead follow-up in one selected Zylu business.

1. Establish the business context. If it is unknown, call `list_accessible_businesses`; ask the user to choose when more than one business is available.
2. Use `search_enquiries` to find the target enquiry or list enquiries due for follow-up. Include activity history when it is needed to answer the request.
3. Before recording an activity, call `get_common_codes` to obtain valid `Activity` and, when relevant, `ActivityCallOutcome` identifiers. Do not guess these identifiers.
4. When the user gives the contact outcome, date, and notes, call `create_enquiry_activity`. Include a follow-up date only when the user supplies one or asks to schedule it.
5. Create a task with `create_task` only when the user explicitly asks to assign or create a task. Use `list_staff` first if an assignee must be resolved from a name.
6. Report the enquiry matched, the activity or task created, and any scheduled next step.

Ask a focused question when several enquiries match, the intended outcome is unclear, or the user has not supplied the details required to create a record. Do not send messages, contact leads, or claim a contact occurred; this workflow only reads and updates Zylu records.
