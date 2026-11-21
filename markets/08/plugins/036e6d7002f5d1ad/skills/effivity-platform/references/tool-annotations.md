# MCP Tool Annotation Justifications

## list_form_data

### Read Only: True
The tool only retrieves existing form data. It does not create, update, delete, overwrite, or otherwise modify records. Execution returns information without changing application state.

### Open World: False
The tool accesses only platform-managed data sources. It has no general-purpose internet browsing or arbitrary external-system access.

### Destructive: False
The tool performs no deletion, irreversible modification, or destructive state change.

### Summary
The annotations accurately describe a read-only, internally scoped data retrieval operation with no destructive side effects.

## get_workflow_master

### Read Only: True
The tool fetches existing workflow master information and performs no creation, update, or deletion.

### Open World: False
The tool is limited to workflow metadata stored within the application platform and has no external web access.

### Destructive: False
Retrieval does not modify or delete workflow metadata and produces no destructive side effects.

### Summary
The annotations accurately describe an internal read-only workflow metadata retrieval operation.

## list_workflow_masters

### Read Only: True
The tool lists existing workflow master records and does not modify, create, or delete configuration.

### Open World: False
The tool is restricted to platform-controlled repositories and cannot interact with arbitrary external systems.

### Destructive: False
Listing records has no destructive effect and does not alter application state.

### Summary
The annotations accurately describe a read-only internal configuration listing operation.

## ask_faq

### Read Only: False
The tool processes user questions and may perform internal lookup, matching, reasoning, and conversational service logic. It is therefore not represented as a purely read-only record retrieval operation. This annotation does not mean the tool writes operational data.

### Open World: False
The tool is restricted to internal FAQ knowledge sources and does not provide arbitrary internet or external-system access.

### Destructive: False
The tool does not delete, overwrite, or otherwise destroy operational data. Its processing produces an answer without destructive state changes.

### Summary
The annotations accurately distinguish application-level question processing from simple retrieval while confirming that the tool remains internally scoped and non-destructive.

## get_workflow_forms

### Read Only: True
The tool retrieves existing workflow-related forms and does not create, update, or delete them.

### Open World: False
The data comes only from internal application repositories. The tool cannot access arbitrary internet resources.

### Destructive: False
Retrieval does not modify, delete, overwrite, or irreversibly alter form data.

### Summary
The annotations accurately describe an internal read-only form retrieval operation with no destructive side effects.

## create_support_ticket

### Read Only: False
The tool creates a new support ticket record, which changes application state. It therefore cannot be classified as read-only.

### Open World: False
The tool is restricted to the application's support ticketing system and cannot access or act upon arbitrary external resources.

### Destructive: False
Creating a new ticket adds information rather than deleting or irreversibly altering existing records. It is non-destructive provided the implementation does not additionally modify or delete existing records.

### Summary
The annotations accurately describe a scoped write operation that creates a new record without destructive deletion or alteration.
