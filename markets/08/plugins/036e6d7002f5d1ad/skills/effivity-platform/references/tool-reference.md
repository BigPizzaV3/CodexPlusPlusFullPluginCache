# Effivity MCP Tool Reference

## list_form_data

Retrieves existing form data from platform-managed data sources.

### Behavior
- Reads existing form data.
- Does not create records.
- Does not update records.
- Does not delete records.
- Does not modify form data.
- Returns information without side effects.

### Scope
Access is limited to application-managed data sources. The tool cannot access arbitrary internet resources or unrelated external systems.

## get_workflow_master

Retrieves workflow master information.

### Behavior
- Performs retrieval only.
- Reads existing workflow metadata.
- Does not create, update, or delete workflow master records.

### Scope
Limited to workflow metadata stored within the platform. No external web access.

## list_workflow_masters

Lists existing workflow master records.

### Behavior
- Provides read-only access to existing workflow configuration.
- Does not create, update, or delete records.
- Produces no side effects.

### Scope
Restricted to platform-controlled repositories. Cannot interact with arbitrary external systems.

## ask_faq

Processes a user question and returns an answer using internal FAQ knowledge.

### Behavior
- Processes the user's question.
- May perform internal FAQ lookups and application-level conversational processing.
- Does not delete, overwrite, or modify operational data.
- Returns an answer rather than performing a destructive operation.

### Scope
Restricted to internal FAQ knowledge sources. It is not a general-purpose internet search tool.

## get_workflow_forms

Retrieves forms associated with workflows.

### Behavior
- Reads existing workflow-related form definitions or records.
- Does not create, update, or delete forms.
- Produces no modification side effects.

### Scope
Data comes only from internal application repositories. No arbitrary internet access.

## create_support_ticket

Creates a new support ticket in the application's support ticketing system.

### Behavior
- Creates a new persistent record.
- Is therefore not read-only.
- Does not delete or overwrite existing records.
- Adding a new record is non-destructive unless the underlying implementation also modifies or deletes existing data.

### Scope
Restricted to the application's support ticketing system. It cannot be used to act on arbitrary external resources or unrelated systems.
