# iPlanner MCP server: tool annotations and their justification

This document lists every tool the iPlanner MCP server can return from `tools/list`, with the four annotations each
tool carries and one sentence per annotation explaining why it has that value. The values were checked against the
code that runs each tool (handler, service, database statements and outbound calls), not against the tool's name.

The document is generated from the review baseline in the iPlanner repository
(`packages/v5-toolkit/tests/fixtures/mcp-review-annotations.js`, `node scripts/mcp-review-report.mjs --markdown`).
Tests compare that baseline with every tool definition and with the real, serialized `tools/list` response, and
compare this document with the baseline. If a tool's annotations, the baseline or this document change without the
others, a test fails.

## Rules applied

Every tool sets all four hints to an explicit `true` or `false`; none is left out or `null`.

- **readOnlyHint** is `true` only for retrieval, computation or previews that do not change anything. It is `false`
  for tools that change data in iPlanner or in a connected system, store a file or other artifact, start a stateful
  job or workflow, or queue work.
- **destructiveHint** is `false` for every read-only tool. For a tool that writes, it is `true` when the effect can be
  destructive or irreversible: deleting, overwriting, cancelling, revoking access, or sending something that cannot
  be recalled (including an automatic notice e-mail). It is `false` only for purely additive writes that have none of
  these effects. Being able to undo a change later is not, on its own, a reason for `false`.
- **idempotentHint** follows the MCP specification: `true` when repeating the same call with the same arguments has
  no additional effect. Read-only tools are idempotent.
- **openWorldHint** is `true` when the tool deals with public or open-ended entities, including arbitrary
  destinations such as e-mail addresses the caller chooses or URLs. A tool confined to the organization's own
  private iPlanner workspace (its records, members, mailboxes and catalog) uses `false`. A network connection or an
  externally hosted provider alone does not make a tool open-world.

Conventions used when applying these rules:

- **Call logs are not effects.** Every call is recorded in iPlanner's MCP call log, and changes are recorded in the
  organization's audit log. Some reads also write an internal usage-metering row. None of this bookkeeping counts as
  a change of the environment.
- **Retry keys.** Many write tools require a retry key (`operation_id`, `operationId`, `idempotencyKey` or
  `idempotency_key`). A repeat with the same key and the same input returns the stored result and changes nothing
  again. Since the key is one of the arguments, such a repeat is "the same call".
- **Revision checks.** Many write tools require the record's current `revision`. The first call changes the revision,
  so an identical repeat is refused as a conflict and has no effect.
- **Owner notices and automations.** Notices that iPlanner itself sends to the organization's owners about a change
  are not a destination chosen by the caller and do not make a tool open-world. Webhooks and workflows that the
  organization configured to react to changes are not counted as the tool's own effect.

Which tools a person sees depends on the organization's tool settings and the person's role. The annotations of a
tool are the same for everyone. Only the three search and runner helpers at the end take their values from the tools
the person can use.

## E-mail: mailboxes, messages, drafts and signatures

| Tool | Title | readOnlyHint | destructiveHint | idempotentHint | openWorldHint |
| --- | --- | --- | --- | --- | --- |
| `email_accounts_list` | Find iPlanner mailboxes | **true** — Lists the organization's mailboxes released to the user; nothing is changed. | **false** — Read-only. | **true** — A repeat returns the same list. | **false** — Limited to the organization's own mailboxes. |
| `email_mailbox_get` | Get iPlanner mailbox folders | **true** — Reads the folder list of one released mailbox; nothing is changed. | **false** — Read-only. | **true** — A repeat returns the same folders. | **false** — Only the user's own released mailbox. |
| `email_messages_list` | Search iPlanner email messages | **true** — Searches the user's released mailboxes and the organization's stored copies; read flags are returned, never changed. | **false** — Read-only. | **true** — A repeat changes nothing; only newly arrived mail can change the answer. | **false** — Searches only mailboxes connected to the organization. |
| `email_message_get` | Get an iPlanner email message | **true** — Reads one message without setting its read flag and without downloading attachments. | **false** — Read-only. | **true** — A repeat returns the same message. | **false** — Only the user's own mailboxes and the organization's stored copies. |
| `email_send` | Send iPlanner email | **false** — Prepares an e-mail and, after the user's confirmation, submits it for delivery through the user's mailbox. | **true** — A delivered e-mail cannot be recalled. | **true** — The required idempotencyKey makes a repeated identical call return the stored result; the same message is never submitted twice. | **true** — Recipients (to, cc, bcc) are e-mail addresses the caller chooses freely, outside the organization. |
| `email_signatures_list` | Find iPlanner email signatures | **true** — Lists the signatures the user may use for a mailbox; nothing is changed. | **false** — Read-only. | **true** — A repeat returns the same list. | **false** — Only the organization's signatures. |
| `email_draft_get` | Get an iPlanner email draft | **true** — Reads one draft and its revision; the draft is neither changed nor sent. | **false** — Read-only. | **true** — A repeat returns the same draft. | **false** — Only the user's own released mailbox. |
| `email_draft_create` | Create an iPlanner email draft | **false** — Saves a new draft in the user's mailbox. | **false** — Only adds a draft; nothing existing is changed and nothing is sent. | **false** — Each call saves another draft. | **false** — Writes only into the user's own released mailbox; the draft's recipients are not contacted. |
| `email_draft_update` | Update an iPlanner email draft | **false** — Replaces a draft in the user's mailbox. | **true** — Overwrites the draft's content and moves the previous version to the trash folder. | **false** — After a partial result a repeat can save another replacement draft; the tool asks clients not to retry automatically. | **false** — Only the user's own released mailbox. |
| `email_message_mark_read` | Mark an iPlanner email as read | **false** — Sets the read flag on the mail server and in iPlanner's stored copy. | **true** — Overwrites the message's previous read state. | **true** — Marking a message that is already read changes nothing. | **false** — Only the user's own released mailbox. |
| `email_message_mark_unread` | Mark an iPlanner email as unread | **false** — Removes the read flag on the mail server and in iPlanner's stored copy. | **true** — Overwrites the message's previous read state. | **true** — Marking a message that is already unread changes nothing. | **false** — Only the user's own released mailbox. |
| `email_message_archive` | Archive an iPlanner email | **false** — Moves the message to the mailbox's archive folder. | **true** — Changes where the message is stored and replaces its message reference. | **false** — The tool asks clients not to retry automatically after an uncertain outcome, so it does not promise idempotency. | **false** — Only the user's own released mailbox. |
| `email_message_move` | Move an iPlanner email | **false** — Moves the message to another folder of the same mailbox. | **true** — The target can be the trash or junk folder, where the mail server may delete the message later. | **false** — The tool asks clients not to retry automatically after an uncertain outcome, so it does not promise idempotency. | **false** — Only the user's own released mailbox. |
| `email_signatures_catalog_list` | List manageable iPlanner signatures | **true** — Lists the signatures the user can see and manage; nothing is changed. | **false** — Read-only. | **true** — A repeat returns the same list. | **false** — Only the organization's signatures. |
| `email_signature_get` | Get an iPlanner signature | **true** — Reads one signature and its revision; nothing is changed. | **false** — Read-only. | **true** — A repeat returns the same signature. | **false** — Only the organization's signatures. |
| `email_signature_create` | Create an iPlanner signature | **false** — Stores a new signature. | **true** — With isDefault it replaces the user's current default signature for future e-mail. | **false** — Each call stores another signature. | **false** — Only the organization's signatures. |
| `email_signature_update` | Update an iPlanner signature | **false** — Changes a stored signature. | **true** — Overwrites the signature that future e-mails use. | **false** — The tool asks clients not to retry automatically after an uncertain outcome, so it does not promise idempotency. | **false** — Only the organization's signatures. |
| `email_signature_delete` | Delete an iPlanner signature | **false** — Deletes a stored signature. | **true** — Deletes the signature; no MCP tool can restore it. | **false** — The tool asks clients not to retry automatically after an uncertain outcome, so it does not promise idempotency. | **false** — Only the organization's signatures. |
| `email_system_send` | System-E-Mail senden | **false** — Prepares an e-mail and, after the user's confirmation, submits it for delivery from the i-Planner system address. | **true** — A delivered e-mail cannot be recalled. | **true** — The required idempotencyKey makes a repeated identical call return the stored result; the same message is never submitted twice. | **false** — The recipient must be the login address of a member of the organization; non-members are refused before sending, and the fixed delivery provider is no public recipient space. |
| `email_templates_list` | E-Mail-Vorlagen suchen | **true** — Lists the published e-mail templates released to the user; nothing is changed. | **false** — Read-only. | **true** — A repeat returns the same list. | **false** — Only the organization's and iPlanner's own template catalog. |

Notes on behaviour:

- `email_send`: prepare stores an intent; confirm queues a mailbox message to user-selected addresses. Confirmation and same-key replay protection do not recall a submitted message. The combined tool is classified by its confirm branch.
- `email_signature_create`: Creating a signature can select it as the default and thereby replace the account default. The hints follow this optional effect, not only the new row.
- `email_system_send`: Both stages use the shared send ledger. The recipient must be the login address of an active internal member of this organization. Non-members are rejected before sending. The fixed external delivery provider does not make this a public recipient space.

## E-mail rules

| Tool | Title | readOnlyHint | destructiveHint | idempotentHint | openWorldHint |
| --- | --- | --- | --- | --- | --- |
| `email_rules_list` | E-Mail-Regeln lesen | **true** — Lists the organization's e-mail rules; nothing is changed. | **false** — Read-only. | **true** — A repeat returns the same list. | **false** — Only the organization's rules. |
| `email_rule_get` | E-Mail-Regel lesen | **true** — Reads one rule and the mailboxes it is linked to; nothing is changed. | **false** — Read-only. | **true** — A repeat returns the same rule. | **false** — Only the organization's rules and mailboxes. |
| `email_rule_save` | E-Mail-Regel speichern | **false** — Creates or changes a rule that decides how incoming mail is handled. | **true** — For an existing rule it overwrites name, conditions and sharing, and can remove other members' access. | **false** — Without an id each call creates another rule. | **false** — Only the organization's rules. |
| `email_rule_delete` | E-Mail-Regel löschen | **false** — Deletes a rule. | **true** — Deletes the rule; no MCP tool can restore it. | **true** — A repeat finds the rule already deleted and changes nothing. | **false** — Only the organization's rules. |
| `email_rule_accounts_update` | E-Mail-Regel Postfächern zuordnen | **false** — Links a rule to mailboxes or unlinks it. | **true** — Unlinking stops the rule for that mailbox's incoming mail. | **true** — Mailboxes already in the requested state are skipped, so a repeat changes nothing. | **false** — Only the organization's own mailboxes. |

## Documents and folder templates

| Tool | Title | readOnlyHint | destructiveHint | idempotentHint | openWorldHint |
| --- | --- | --- | --- | --- | --- |
| `document_folders_list` | iPlanner Dokumentordner anzeigen | **true** — Lists the document folders of one customer record; nothing is changed. | **false** — Read-only. | **true** — A repeat returns the same folders. | **false** — Only the organization's own customer records. |
| `document_folder_create` | iPlanner Dokumentordner anlegen | **false** — Creates a folder in a customer record's documents. | **false** — Only adds a folder (and the root folder if it is missing); existing folders and documents are unchanged. | **true** — If a folder with this name already exists in the same place, it is returned and nothing is created. | **false** — Only the organization's own customer records. |
| `document_folder_rename` | iPlanner Dokumentordner umbenennen | **false** — Renames a folder. | **true** — Overwrites the folder's name. | **true** — The required revision changes with the first call, so an identical repeat is refused and changes nothing. | **false** — Only the organization's own customer records. |
| `document_folder_move` | iPlanner Dokumentordner verschieben | **false** — Moves a folder with its subfolders. | **true** — Overwrites the folder's place in the folder tree. | **true** — The required revision changes with the first call, so an identical repeat is refused and changes nothing. | **false** — Only the organization's own customer records. |
| `document_folder_delete` | iPlanner Dokumentordner löschen | **false** — Deletes a folder. | **true** — Deletes the folder permanently; its documents become unfiled and its subfolders move up a level. | **true** — A repeat finds no folder and changes nothing. | **false** — Only the organization's own customer records. |
| `folder_templates_list` | iPlanner Ordnervorlagen finden | **true** — Lists the folder templates the user may apply; nothing is changed. | **false** — Read-only. | **true** — A repeat returns the same list. | **false** — Only the organization's templates. |
| `folder_templates_manageable_list` | iPlanner verwaltbare Ordnervorlagen anzeigen | **true** — Lists the folder templates the user may manage; nothing is changed. | **false** — Read-only. | **true** — A repeat returns the same list. | **false** — Only the organization's templates. |
| `folder_template_manageable_get` | iPlanner verwaltbare Ordnervorlage lesen | **true** — Reads one manageable folder template with its folders; nothing is changed. | **false** — Read-only. | **true** — A repeat returns the same template. | **false** — Only the organization's templates. |
| `folder_template_create` | iPlanner Ordnervorlage anlegen | **false** — Stores a new folder template. | **false** — Only adds a new private template; nothing existing is changed. | **false** — Each call creates another template. | **false** — Only the organization's templates. |
| `folder_template_update` | iPlanner Ordnervorlage ändern | **false** — Changes a folder template. | **true** — Overwrites name, description or active status; deactivating hides the template from users. | **true** — The required revision changes with the first call, so an identical repeat is refused and changes nothing. | **false** — Only the organization's templates. |
| `folder_template_duplicate` | iPlanner Ordnervorlage kopieren | **false** — Stores a copy of a folder template. | **false** — Only adds a copy; the source template is unchanged. | **false** — Each call adds another copy. | **false** — Only the organization's templates. |
| `folder_template_delete` | iPlanner Ordnervorlage löschen | **false** — Deletes a folder template. | **true** — Deletes the template and its folder structure permanently. | **true** — A repeat finds no template, or an outdated revision, and changes nothing. | **false** — Only the organization's templates. |
| `folder_template_folder_add` | iPlanner Ordner in Ordnervorlage anlegen | **false** — Adds a folder to a folder template. | **false** — Only adds a folder; existing folders keep their names, nesting and relative order (later siblings move one position on). | **true** — The required revision changes with the first call, so an identical repeat is refused and changes nothing. | **false** — Only the organization's templates. |
| `folder_template_folder_rename` | iPlanner Ordner in Ordnervorlage umbenennen | **false** — Renames a folder in a folder template. | **true** — Overwrites the folder's name. | **true** — The required revision changes with the first call, so an identical repeat is refused and changes nothing. | **false** — Only the organization's templates. |
| `folder_template_folder_move` | iPlanner Ordner in Ordnervorlage verschieben | **false** — Moves a folder within a folder template. | **true** — Overwrites the folder's place in the template. | **true** — The required revision changes with the first call, so an identical repeat is refused and changes nothing. | **false** — Only the organization's templates. |
| `folder_template_folder_delete` | iPlanner Ordner aus Ordnervorlage löschen | **false** — Removes a folder from a folder template. | **true** — Deletes the folder and its subfolders from the template. | **true** — The required revision changes with the first call, so an identical repeat is refused and changes nothing. | **false** — Only the organization's templates. |
| `folder_templates_apply` | iPlanner Ordnervorlage anwenden | **false** — Creates the template's folders in a customer record's documents. | **false** — Only adds folders; existing folders and documents are unchanged. | **true** — The required idempotency_key returns the original result for a repeat; nothing is created again. | **false** — Only the organization's own customer records. |
| `fileparser` | iPlanner Dateiinhalte lesen | **true** — Extracts the text of an attachment from the user's released mailbox or a stored e-mail; nothing is stored and the message is not marked as read. | **false** — Read-only. | **true** — A repeat returns the same text. | **false** — Sources are limited to the organization's mailboxes and stored e-mails; there is no URL input. |

Notes on behaviour:

- `folder_template_folder_add`: Inserting at a selected position renumbers the later sibling folders and raises the template revision. Every existing folder keeps its name, nesting and relative order, so the effect is additive; the changed revision refuses an identical repeat.

## Customers

| Tool | Title | readOnlyHint | destructiveHint | idempotentHint | openWorldHint |
| --- | --- | --- | --- | --- | --- |
| `customers_search` | iPlanner Kunden suchen | **true** — Searches the customers the user may see; nothing is changed. | **false** — Read-only. | **true** — A repeat returns the same results. | **false** — Only the organization's own customer records. |
| `customers_read` | iPlanner Kundenakte lesen | **true** — Reads one customer record; nothing is changed. | **false** — Read-only. | **true** — A repeat returns the same record. | **false** — Only the organization's own customer records. |
| `customers_update` | iPlanner Kundendaten ändern | **false** — Changes a customer record. | **true** — Overwrites or clears customer fields, including the responsible advisor. | **true** — The same operation_id returns the stored result, and an outdated revision is refused. | **false** — Only the organization's own customer records. |
| `customers_create` | iPlanner Kunden anlegen | **false** — Creates a customer record. | **false** — Only adds a customer; existing records are unchanged. | **true** — The required operation_id returns the stored result for a repeat; nothing is created again. | **false** — Only the organization's own customer records. |

## Text marks (placeholders)

| Tool | Title | readOnlyHint | destructiveHint | idempotentHint | openWorldHint |
| --- | --- | --- | --- | --- | --- |
| `text_marks_list` | Textmarken suchen | **true** — Lists the organization's text marks; nothing is changed. | **false** — Read-only. | **true** — A repeat returns the same list. | **false** — Only the organization's text marks. |
| `text_mark_get` | Textmarke lesen | **true** — Reads one text mark definition; nothing is changed. | **false** — Read-only. | **true** — A repeat returns the same definition. | **false** — Only the organization's text marks. |
| `text_mark_sources` | Textmarkenfelder anzeigen | **true** — Lists the record fields a text mark can use; nothing is changed. | **false** — Read-only. | **true** — A repeat returns the same fields. | **false** — Only iPlanner's own field catalog. |
| `text_mark_create` | Textmarke anlegen | **false** — Stores a new text mark definition. | **false** — Only adds a definition; existing text marks are unchanged. | **true** — The required operation_id returns the stored result for a repeat, and a second mark with the same key is refused. | **false** — Only the organization's text marks. |
| `text_mark_update` | Textmarke bearbeiten | **false** — Changes a text mark definition. | **true** — Overwrites the definition; templates that use the mark show the new value from then on. | **true** — The same operation_id returns the stored result, and an outdated revision is refused. | **false** — Only the organization's text marks. |
| `text_mark_delete` | Textmarke löschen | **false** — Deletes a text mark. | **true** — Deletes the text mark; templates no longer resolve it. | **true** — The same operation_id returns the stored result, and a deleted mark is not found again. | **false** — Only the organization's text marks. |
| `text_marks_available` | Verfügbare Textmarken suchen | **true** — Lists the text marks the user may use; nothing is changed. | **false** — Read-only. | **true** — A repeat returns the same list. | **false** — Only the organization's text marks. |
| `text_marks_resolve` | Textmarken auflösen | **true** — Computes the text of the given marks for records the user may read; nothing is stored or sent. | **false** — Read-only. | **true** — A repeat returns the same text. | **false** — Only the organization's own records. |

## Text snippets

| Tool | Title | readOnlyHint | destructiveHint | idempotentHint | openWorldHint |
| --- | --- | --- | --- | --- | --- |
| `text_snippets_list` | Textbausteine suchen | **true** — Lists the text snippets the user may see; nothing is changed. | **false** — Read-only. | **true** — A repeat returns the same list. | **false** — Only the organization's snippets. |
| `text_snippet_get` | Textbaustein lesen | **true** — Reads one text snippet; nothing is changed. | **false** — Read-only. | **true** — A repeat returns the same snippet. | **false** — Only the organization's snippets. |
| `text_snippet_create` | Textbaustein anlegen | **false** — Stores a new text snippet. | **false** — Only adds a snippet; existing snippets are unchanged. | **true** — The required operation_id returns the stored result for a repeat; nothing is created again. | **false** — Only the organization's snippets. |
| `text_snippet_update` | Textbaustein bearbeiten | **false** — Changes a text snippet. | **true** — Overwrites the content and can change owner or sharing, which removes other users' access. | **true** — The same operation_id returns the stored result, and an outdated revision is refused. | **false** — Only the organization's snippets. |
| `text_snippet_delete` | Textbaustein löschen | **false** — Deletes a text snippet. | **true** — Deletes the snippet; no MCP tool can restore it. | **true** — The same operation_id returns the stored result, and a deleted snippet is not found again. | **false** — Only the organization's snippets. |
| `text_snippet_render` | Textbaustein verwenden | **true** — Computes the snippet's text for records the user may read; nothing is stored or sent. | **false** — Read-only. | **true** — A repeat returns the same text. | **false** — Only the organization's own records. |

## Labels

| Tool | Title | readOnlyHint | destructiveHint | idempotentHint | openWorldHint |
| --- | --- | --- | --- | --- | --- |
| `labels_list` | Stichworte suchen | **true** — Lists the organization's labels; nothing is changed. | **false** — Read-only. | **true** — A repeat returns the same list. | **false** — Only the organization's labels. |
| `record_labels_list` | Stichworte am Datensatz lesen | **true** — Lists the labels of one record; nothing is changed. | **false** — Read-only. | **true** — A repeat returns the same labels. | **false** — Only the organization's own records. |
| `label_assign` | Stichwort zuordnen | **false** — Assigns a label to a record. | **false** — Only adds an assignment; nothing existing is changed. | **true** — Assigning a label the record already has changes nothing. | **false** — Only the organization's own records. |
| `label_remove` | Stichwortzuordnung entfernen | **false** — Removes a label from a record. | **true** — Removes the assignment. | **true** — Removing a label the record no longer has changes nothing. | **false** — Only the organization's own records. |

## Help and explanations

| Tool | Title | readOnlyHint | destructiveHint | idempotentHint | openWorldHint |
| --- | --- | --- | --- | --- | --- |
| `help_search` | Dokumentation durchsuchen | **true** — Searches iPlanner's published help documentation; nothing is stored. | **false** — Read-only. | **true** — A repeat returns the same results. | **false** — A fixed index of iPlanner's own documentation, not a web search. |
| `help_article_get` | Dokumentation lesen | **true** — Reads one help article; nothing is stored. | **false** — Read-only. | **true** — A repeat returns the same article. | **false** — Only iPlanner's own documentation. |
| `organization_explain` | Organisationsbereich erklären | **true** — Explains an area of the organization, the user's access and the relevant help sections; nothing is changed. | **false** — Read-only. | **true** — A repeat returns the same explanation. | **false** — Only the organization's settings and iPlanner's own documentation. |

## Reminders

| Tool | Title | readOnlyHint | destructiveHint | idempotentHint | openWorldHint |
| --- | --- | --- | --- | --- | --- |
| `reminders_list` | Erinnerungen lesen | **true** — Lists the user's own reminders; nothing is changed. | **false** — Read-only. | **true** — A repeat returns the same list. | **false** — Only the user's own reminders. |
| `reminders_get` | Erinnerung anzeigen | **true** — Reads one of the user's reminders and its recent runs; nothing is changed. | **false** — Read-only. | **true** — A repeat returns the same reminder. | **false** — Only the user's own reminders. |
| `reminders_create` | Erinnerungen verwalten | **false** — Creates an active reminder. | **true** — Schedules notifications in iPlanner, as push messages or by e-mail to the user's own address, which cannot be recalled once delivered. | **true** — The required operation_id returns the stored result for a repeat; nothing is created again. | **false** — Notifications go only to the calling user. |
| `reminders_update` | Erinnerung ändern | **false** — Changes a reminder. | **true** — Overwrites the reminder; a new schedule replaces its pending occurrences. | **true** — The same operation_id returns the stored result, and an outdated revision is refused. | **false** — Only the user's own reminders. |
| `reminders_cancel` | Erinnerung beenden | **false** — Cancels a reminder. | **true** — Cancels the reminder and its pending occurrences. | **true** — The same operation_id returns the stored result, and an already cancelled reminder is refused. | **false** — Only the user's own reminders. |
| `reminders_snooze` | Erinnerung verschieben | **false** — Moves one occurrence of a reminder to a later time. | **true** — Closes the current occurrence and cancels its pending deliveries. | **true** — The same operation_id returns the stored result, and an already closed occurrence is refused. | **false** — Only the user's own reminders. |
| `reminders_complete` | Erinnerung erledigen | **false** — Marks one occurrence of a reminder as done. | **true** — Closes the occurrence and cancels its pending deliveries. | **true** — The same operation_id returns the stored result, and completing a completed occurrence changes nothing. | **false** — Only the user's own reminders. |

Notes on behaviour:

- `reminders_create`: Creates an active schedule, not an inert draft: it can later deliver email to the current verified user or push to their registered devices. Delivery cannot be recalled; recipients are account-bound.

## Team

| Tool | Title | readOnlyHint | destructiveHint | idempotentHint | openWorldHint |
| --- | --- | --- | --- | --- | --- |
| `team_query` | Mitglieder suchen | **true** — Searches the organization's members; nothing is changed. | **false** — Read-only. | **true** — A repeat returns the same results. | **false** — Only the organization's members. |
| `team_member_get` | Mitglied lesen | **true** — Reads one member; nothing is changed. | **false** — Read-only. | **true** — A repeat returns the same member. | **false** — Only the organization's members. |
| `team_reservations_list` | Vormerkungen lesen | **true** — Lists the organization's seat reservations; nothing is changed. | **false** — Read-only. | **true** — A repeat returns the same list. | **false** — Only the organization's reservations. |
| `team_reservation_candidates` | Vormerkbare Benutzer suchen | **true** — Searches contacts of the organization that can be reserved; nothing is changed. | **false** — Read-only. | **true** — A repeat returns the same results. | **false** — Only the organization's own contacts. |
| `team_member_invite` | Mitglied einladen | **false** — Creates a pending membership and sends an invitation e-mail. | **true** — The invitation e-mail cannot be recalled; inviting a pending or inactive member again overwrites their role and ends their app connections. | **false** — Each call sends a new invitation and invalidates the previous link. | **true** — The invitee's e-mail address is chosen freely by the caller. |
| `team_member_update` | Mitglied ändern | **false** — Changes a member's name or start page. | **true** — Overwrites the member's stored values. | **true** — Saving the same values again changes nothing. | **false** — Only the organization's members. |
| `team_member_role_update` | Mitgliedsrolle ändern | **false** — Changes a member's role. | **true** — Overwrites the role, which can reduce the member's rights, and ends the member's connected-app access. | **true** — Setting the role the member already has changes nothing. | **false** — Only the organization's members. |
| `team_member_activate` | Mitglied aktivieren | **false** — Lets an inactive member sign in again. | **true** — Restores the person's access to the organization's data and uses a paid seat; what they see after signing in cannot be taken back. | **true** — A repeat finds no inactive member and changes nothing. | **false** — Only the organization's members. |
| `team_member_deactivate` | Mitglied deaktivieren | **false** — Deactivates a member. | **true** — Revokes the member's access and their connected apps. | **true** — A repeat finds no active member and changes nothing. | **false** — Only the organization's members. |
| `team_invite_resend` | Mitglied erneut einladen | **false** — Sends a new invitation e-mail to a pending member. | **true** — Invalidates the previous invitation link, and the e-mail cannot be recalled. | **false** — Each call sends another e-mail and invalidates the previous link. | **false** — It mails only the stored address of an existing pending invitation; the caller cannot choose a recipient. |
| `team_reservation_create` | Vormerkung anlegen | **false** — Stores a seat reservation for a contact. | **false** — Only adds a reservation; no sign-in, e-mail or seat charge follows. | **true** — A second reservation for the same contact is refused, so a repeat changes nothing. | **false** — Only the organization's own contacts. |
| `team_reservation_update` | Vormerkung ändern | **false** — Changes a seat reservation. | **true** — Overwrites the reservation's address, role and names. | **true** — Saving the same values again leaves the reservation unchanged. | **false** — Only the organization's reservations. |
| `team_reservation_link` | Vormerkung neu verknüpfen | **false** — Links a reservation to another contact. | **true** — Replaces the linked contact and discards the previous name and address. | **true** — A repeat no longer matches the expected previous link and is refused. | **false** — Only the organization's own contacts. |
| `team_reservation_remove` | Vormerkung löschen | **false** — Deletes a seat reservation. | **true** — Deletes the reservation. | **true** — A repeat finds no reservation and changes nothing. | **false** — Only the organization's reservations. |

Notes on behaviour:

- `team_invite_resend`: Replaces an existing pending member invitation token and emails that member. It cannot choose an arbitrary new recipient.
- `team_reservation_create`: Inserts a UID-less reservation and audit record. Existing CRM/member records are not overwritten. No login, invitation or paid seat is created. Human confirmation remains required independently of destructiveHint=false.

## Roles

| Tool | Title | readOnlyHint | destructiveHint | idempotentHint | openWorldHint |
| --- | --- | --- | --- | --- | --- |
| `roles_list` | Benutzerrollen lesen | **true** — Lists the organization's roles; nothing is changed. | **false** — Read-only. | **true** — A repeat returns the same list. | **false** — Only the organization's roles. |
| `role_get` | Benutzerrolle lesen | **true** — Reads one role and its rights; nothing is changed. | **false** — Read-only. | **true** — A repeat returns the same role. | **false** — Only the organization's roles. |
| `roles_compare` | Benutzerrollen vergleichen | **true** — Compares the rights of roles; nothing is changed. | **false** — Read-only. | **true** — A repeat returns the same comparison. | **false** — Only the organization's roles. |
| `role_right_holders` | Benutzerrollen nach Recht suchen | **true** — Lists the roles that hold a right, with member counts; nothing is changed. | **false** — Read-only. | **true** — A repeat returns the same list. | **false** — Only the organization's roles. |
| `role_explain` | Benutzerrollen-Recht erklären | **true** — Explains why a role has or lacks a right; nothing is changed. | **false** — Read-only. | **true** — A repeat returns the same explanation. | **false** — Only the organization's roles and iPlanner's own documentation. |
| `role_propose` | Benutzerrolle vorschlagen | **true** — Computes a proposed change of a role as a preview; nothing is saved. | **false** — Read-only. | **true** — A repeat returns the same proposal. | **false** — Only the organization's roles. |
| `role_update` | Benutzerrolle ändern | **false** — Changes the rights, name or description of a role. | **true** — Overwrites rights for every member holding the role and can reduce them. | **true** — A repeat changes nothing and is refused as unchanged. | **false** — Only the organization's roles. |
| `role_create` | Benutzerrolle anlegen | **false** — Creates a new role. | **true** — Besides adding the role, it e-mails a security notice about it to the organization's owners, which cannot be recalled. | **false** — Each call creates another role. | **false** — Only the organization's roles. |
| `role_delete` | Benutzerrolle löschen | **false** — Deletes a role that has no members. | **true** — Deletes the role and the integration releases granted to it. | **true** — A repeat finds no role and changes nothing. | **false** — Only the organization's roles. |

Notes on behaviour:

- `role_create`: Inserts a new role, synchronizes its existing-organization counterpart and emits security notices, including notices for grants beyond the actor. The notification branch prevents an additive-only classification.

## Announcements

| Tool | Title | readOnlyHint | destructiveHint | idempotentHint | openWorldHint |
| --- | --- | --- | --- | --- | --- |
| `announcements_list` | Meldungen lesen | **true** — Lists the organization's announcements; no read receipt is recorded. | **false** — Read-only. | **true** — A repeat returns the same list. | **false** — Only the organization's announcements. |
| `announcement_get` | Meldung lesen | **true** — Reads one announcement and its versions; no read receipt is recorded. | **false** — Read-only. | **true** — A repeat returns the same announcement. | **false** — Only the organization's announcements. |
| `announcement_receipts` | Meldungs-Kenntnisnahmen lesen | **true** — Lists which members have acknowledged an announcement; nothing is changed. | **false** — Read-only. | **true** — A repeat returns the same list. | **false** — Only the organization's members. |
| `announcement_save` | Meldung speichern | **false** — Creates or changes an announcement draft. | **true** — For an existing draft it overwrites the content. | **false** — Without an id each call creates another draft. | **false** — Only the organization's announcements. |
| `announcement_publish` | Meldung veröffentlichen | **false** — Publishes an announcement to the organization's members. | **true** — Members see the publication; it can be withdrawn later, but not unseen. | **true** — Publishing the same revision again returns the existing publication. | **false** — Recipients are only members of the organization. |
| `announcement_withdraw` | Meldung zurücknehmen | **false** — Withdraws a published announcement. | **true** — Ends the publication for all members. | **true** — The required revision changes with the first call, so an identical repeat is refused and changes nothing. | **false** — Only the organization's announcements. |
| `announcement_delete` | Meldung löschen | **false** — Deletes an announcement draft. | **true** — Deletes the draft; no MCP tool can restore it. | **true** — A repeat finds no draft and changes nothing. | **false** — Only the organization's announcements. |

## Company data

| Tool | Title | readOnlyHint | destructiveHint | idempotentHint | openWorldHint |
| --- | --- | --- | --- | --- | --- |
| `company_read` | Firmendaten lesen | **true** — Reads the organization's company data; nothing is changed. | **false** — Read-only. | **true** — A repeat returns the same data. | **false** — Only the organization's own data. |
| `company_update` | Firmendaten ändern | **false** — Changes the organization's company data. | **true** — Overwrites or clears fields of the company data. | **true** — Saving the same values again changes nothing. | **false** — Only the organization's own data. |
| `company_row_save` | Firmendaten-Eintrag speichern | **false** — Creates or changes an entry of a company data list, such as a register entry. | **true** — For an existing entry it overwrites its values. | **false** — Without an id each call adds another entry. | **false** — Only the organization's own data. |
| `company_row_delete` | Firmendaten-Eintrag löschen | **false** — Deletes an entry of a company data list. | **true** — Deletes the entry; no MCP tool can restore it. | **true** — A repeat finds no entry and changes nothing. | **false** — Only the organization's own data. |

## Audit log, usage and billing

| Tool | Title | readOnlyHint | destructiveHint | idempotentHint | openWorldHint |
| --- | --- | --- | --- | --- | --- |
| `audit_log_list` | Audit-Log lesen | **true** — Reads entries of the organization's audit log; nothing is changed. | **false** — Read-only. | **true** — A repeat returns the same entries. | **false** — Only the organization's own log. |
| `audit_log_query` | Audit-Log suchen | **true** — Searches the organization's audit log in a read-only database snapshot; nothing is changed. | **false** — Read-only. | **true** — A repeat returns the same results. | **false** — Only the organization's own log. |
| `audit_retention_read` | Audit-Log-Aufbewahrung lesen | **true** — Reads how long audit log entries are kept; nothing is changed. | **false** — Read-only. | **true** — A repeat returns the same setting. | **false** — Only the organization's own settings. |
| `audit_retention_update` | Audit-Log-Aufbewahrung verlängern | **false** — Changes how long audit log entries are kept. | **true** — Overwrites the retention setting; this tool can only lengthen it, and shortening it again is possible only in the settings page. | **true** — Saving the same value again changes nothing. | **false** — Only the organization's own settings. |
| `usage_read` | Nutzung lesen | **true** — Reads the organization's usage and alert settings; nothing is changed. | **false** — Read-only. | **true** — A repeat returns the same figures. | **false** — Only the organization's own data. |
| `usage_alerts_update` | Nutzungswarnungen ändern | **false** — Changes the usage warning threshold and its recipients. | **true** — Overwrites the threshold and replaces the complete recipient list. | **true** — Saving the same values again changes no setting, re-arms no warning and sends nothing; only the save itself is logged. | **true** — Recipients are e-mail addresses the caller chooses freely; they will receive usage warnings. |
| `billing_read` | Abrechnung lesen | **true** — Reads the organization's plan, seats and credits; nothing is changed. | **false** — Read-only. | **true** — A repeat returns the same data. | **false** — Only the organization's own billing data. |
| `billing_invoices_list` | Rechnungen lesen | **true** — Lists the organization's invoices; nothing is stored or created. | **false** — Read-only. | **true** — A repeat returns the same invoices. | **false** — Only the organization's own invoices; they are fetched from iPlanner's billing provider for the customer number the server holds, not for any input. |

Notes on behaviour:

- `usage_alerts_update`: Updates the alert configuration and can schedule future notification delivery to user-selected addresses; deferred delivery is still an open-world effect.
- `billing_read`: Reports existing bookings and balances only; no purchasable credit-package catalog or unbooked add-on prices. It does not initiate charges or a checkout.
- `billing_invoices_list`: The provider customer ID is resolved server-side from the organization. Returned documents are filtered to that customer again. There is no caller-selected external customer or destination.

## Security, integrations, accounts, webhooks, API keys and data exports

| Tool | Title | readOnlyHint | destructiveHint | idempotentHint | openWorldHint |
| --- | --- | --- | --- | --- | --- |
| `security_settings_read` | Sicherheit lesen | **true** — Reads the organization's security settings; nothing is changed. | **false** — Read-only. | **true** — A repeat returns the same settings. | **false** — Only the organization's own settings. |
| `security_settings_update` | Sicherheit verschärfen | **false** — Tightens the organization's security settings. | **true** — Overwrites settings; requiring two-factor sign-in blocks members' current one-factor sessions. | **true** — Saving the same values again changes nothing. | **false** — Only the organization's own settings. |
| `integrations_list` | Integrationen lesen | **true** — Lists the organization's integrations; nothing is changed. | **false** — Read-only. | **true** — A repeat returns the same list. | **false** — Only the organization's own settings. |
| `integration_get` | Integration lesen | **true** — Reads one integration without its credential values; nothing is changed. | **false** — Read-only. | **true** — A repeat returns the same integration. | **false** — Only the organization's own settings. |
| `accounts_query` | Accounts suchen | **true** — Looks up the organization's connected accounts; nothing is changed. | **false** — Read-only. | **true** — A repeat returns the same results. | **false** — Only the organization's own accounts. |
| `account_get` | Account lesen | **true** — Reads one connected account without its credentials; nothing is changed. | **false** — Read-only. | **true** — A repeat returns the same account. | **false** — Only the organization's own accounts. |
| `webhooks_list` | Webhooks lesen | **true** — Lists the organization's webhooks; nothing is sent. | **false** — Read-only. | **true** — A repeat returns the same list. | **false** — Only the organization's own settings. |
| `webhook_get` | Webhook lesen | **true** — Reads one webhook and its latest deliveries; nothing is sent. | **false** — Read-only. | **true** — A repeat returns the same webhook. | **false** — Only the organization's own settings. |
| `webhook_deactivate` | Webhook deaktivieren | **false** — Switches a webhook off. | **true** — Stops all deliveries to the webhook's target; switching it on again is not possible with this connection. | **true** — A repeat finds the webhook inactive and is refused without changes. | **false** — Only the organization's own settings. |
| `webhook_test` | Webhook testen | **false** — Sends a signed test request to the webhook's target and stores the result. | **true** — The test request cannot be recalled, and the stored result of the previous test is overwritten. | **false** — Each call sends another request. | **true** — The target is an external URL that the organization configured, outside iPlanner. |
| `webhook_update` | Webhook ändern | **false** — Changes a webhook's name, description or events. | **true** — Overwrites the settings; events can only be removed with this connection, not added back. | **true** — An unchanged repeat is refused without changes. | **false** — The target URL cannot be changed with this tool. |
| `tokens_list` | API-Schlüssel lesen | **true** — Lists the organization's API keys without their secrets; nothing is changed. | **false** — Read-only. | **true** — A repeat returns the same list. | **false** — Only the organization's own settings. |
| `token_revoke` | API-Schlüssel widerrufen | **false** — Revokes an API key. | **true** — Applications using the key lose access immediately. | **true** — A repeat finds the key already revoked and is refused without changes. | **false** — Only the organization's own settings. |
| `data_export_status` | Datenexporte lesen | **true** — Reads the status of the organization's data exports; it does not start, change or download an export. | **false** — Read-only. | **true** — A repeat returns the same status. | **false** — Only the organization's own data. |

Notes on behaviour:

- `webhook_test`: Triggers an outbound request to the configured destination. That destination can be independently controlled; testing may cause effects there.
- `data_export_status`: Returns existing export/order status metadata only. Does not create an export, queue a job, download records, return a download URL, notify or charge.

## Support access and product news

| Tool | Title | readOnlyHint | destructiveHint | idempotentHint | openWorldHint |
| --- | --- | --- | --- | --- | --- |
| `support_access_read` | Support-Zugang lesen | **true** — Lists which members may open support requests with i-Planner; nothing is changed. | **false** — Read-only. | **true** — A repeat returns the same list. | **false** — Only the organization's members. |
| `support_member_add` | Support-Zugang geben | **false** — Allows a member to open support requests with i-Planner. | **true** — Besides granting the permission, it e-mails a security notice to the organization's owners, which cannot be recalled. | **true** — Granting a permission the member already has changes nothing and sends no notice. | **false** — Only members of the organization. |
| `support_member_remove` | Support-Zugang entziehen | **false** — Removes a member's permission to open support requests. | **true** — Revokes the permission. | **true** — Removing a permission the member no longer has changes nothing. | **false** — Only members of the organization. |
| `product_news_read` | Produktnews-Empfänger lesen | **true** — Lists which members receive i-Planner product news in the app; nothing is changed. | **false** — Read-only. | **true** — A repeat returns the same list. | **false** — Only the organization's members. |
| `product_news_member_add` | Produktnews geben | **false** — Subscribes a member to product news shown in the app. | **false** — Only adds a subscription; nothing is sent when it is added. | **true** — Subscribing a subscribed member changes nothing. | **false** — Only members of the organization. |
| `product_news_member_remove` | Produktnews entziehen | **false** — Unsubscribes a member from product news. | **true** — Cancels the member's subscription. | **true** — Unsubscribing an unsubscribed member changes nothing. | **false** — Only members of the organization. |

## PDF designer (registered, currently offered to no account)

These tools are registered on the server, but `tools/list` does not offer them to any account yet: the PDF designer is an internal preview. Their annotations are already set for the time they are released.

| Tool | Title | readOnlyHint | destructiveHint | idempotentHint | openWorldHint |
| --- | --- | --- | --- | --- | --- |
| `pdf_templates_list` | PDF-Vorlagen ansehen | **true** — Lists published templates and iPlanner's starter templates; nothing is changed. | **false** — Read-only. | **true** — A repeat returns the same list. | **false** — Only the organization's templates and iPlanner's own catalog. |
| `pdf_template_get` | PDF-Vorlage lesen | **true** — Reads one template draft or published version; nothing is changed. | **false** — Read-only. | **true** — A repeat returns the same template. | **false** — Only the organization's templates and iPlanner's own catalog. |
| `pdf_designer_catalog` | PDF-Werkzeuge ansehen | **true** — Reads the designer's element and tool overview; nothing is changed. | **false** — Read-only. | **true** — A repeat returns the same overview. | **false** — Only iPlanner's own catalog. |
| `pdf_template_create` | PDF-Vorlage anlegen | **false** — Stores a new, empty, private draft. | **false** — Only adds a draft; nothing existing is changed. | **true** — The required operationId returns the stored result for a repeat; nothing is created again. | **false** — Only the organization's templates. |
| `pdf_template_duplicate` | PDF-Vorlage übernehmen | **false** — Stores a private draft copied from a published template. | **false** — Only adds a draft; the source is unchanged. | **true** — The required operationId returns the stored result for a repeat; nothing is created again. | **false** — Only the organization's templates and iPlanner's own catalog. |
| `pdf_template_update` | PDF-Vorlage bearbeiten | **false** — Changes a draft's name, description, kind or placeholders. | **true** — Overwrites these values and replaces the complete placeholder list. | **true** — The same operationId returns the stored result, and an outdated revision is refused. | **false** — Only the organization's templates. |
| `pdf_element_add` | PDF-Elemente hinzufügen | **false** — Adds elements to a draft. | **false** — Only adds elements; existing elements are unchanged. | **true** — The same operationId returns the stored result, and an outdated revision is refused. | **false** — Only the organization's templates. |
| `pdf_element_update` | PDF-Elemente bearbeiten | **false** — Changes elements of a draft. | **true** — Overwrites content, appearance or position of existing elements. | **true** — The same operationId returns the stored result, and an outdated revision is refused. | **false** — Only the organization's templates. |
| `pdf_element_delete` | PDF-Elemente entfernen | **false** — Removes elements from a draft. | **true** — Deletes the elements. | **true** — The same operationId returns the stored result, and an outdated revision is refused. | **false** — Only the organization's templates. |
| `pdf_element_duplicate` | PDF-Elemente kopieren | **false** — Copies elements within a draft. | **false** — Only adds copies; the original elements are unchanged. | **true** — The same operationId returns the stored result, and an outdated revision is refused. | **false** — Only the organization's templates. |
| `pdf_element_move` | PDF-Elemente verschieben | **false** — Moves elements of a draft. | **true** — Overwrites the elements' positions. | **true** — The same operationId returns the stored result, and an outdated revision is refused. | **false** — Only the organization's templates. |
| `pdf_element_rotate` | PDF-Elemente drehen | **false** — Rotates elements of a draft. | **true** — Overwrites the elements' rotation and positions. | **true** — The same operationId returns the stored result, and an outdated revision is refused. | **false** — Only the organization's templates. |
| `pdf_element_align` | PDF-Elemente ausrichten | **false** — Aligns elements on the page. | **true** — Overwrites the elements' positions. | **true** — The same operationId returns the stored result, and an outdated revision is refused. | **false** — Only the organization's templates. |
| `pdf_element_order_update` | PDF-Ebenenreihenfolge ändern | **false** — Brings elements to the front or sends them to the back. | **true** — Overwrites the stacking order of the page's elements. | **true** — The same operationId returns the stored result, and an outdated revision is refused. | **false** — Only the organization's templates. |
| `pdf_element_group` | PDF-Elemente gruppieren | **false** — Groups elements. | **true** — Replaces the elements' previous group membership. | **true** — The same operationId returns the stored result, and an outdated revision is refused. | **false** — Only the organization's templates. |
| `pdf_element_ungroup` | PDF-Gruppierung lösen | **false** — Ungroups elements. | **true** — Removes the group. | **true** — The same operationId returns the stored result, and an outdated revision is refused. | **false** — Only the organization's templates. |
| `pdf_element_behavior_update` | PDF-Seitenverwendung ändern | **false** — Changes whether an element is fixed, repeated or flowing. | **true** — Overwrites the element's behaviour and can remove its links to other elements. | **true** — The same operationId returns the stored result, and an outdated revision is refused. | **false** — Only the organization's templates. |
| `pdf_content_layout_update` | PDF-Inhaltsbereich automatisch anordnen | **false** — Switches automatic layout of a content chain on or off. | **true** — Overwrites the layout mode of every element in the chain. | **true** — The same operationId returns the stored result, and an outdated revision is refused. | **false** — Only the organization's templates. |
| `pdf_element_page_update` | PDF-Elemente auf Seite verschieben | **false** — Moves elements to another page. | **true** — Overwrites the elements' page and position. | **true** — The same operationId returns the stored result, and an outdated revision is refused. | **false** — Only the organization's templates. |
| `pdf_page_add` | PDF-Seiten hinzufügen | **false** — Appends pages to a draft. | **true** — Besides adding pages, it changes the role of the existing last page. | **true** — The same operationId returns the stored result, and an outdated revision is refused. | **false** — Only the organization's templates. |
| `pdf_page_duplicate` | PDF-Seite kopieren | **false** — Copies a page with its elements. | **false** — Only adds a copy; existing pages are unchanged. | **true** — The same operationId returns the stored result, and an outdated revision is refused. | **false** — Only the organization's templates. |
| `pdf_page_delete` | PDF-Seite entfernen | **false** — Removes a page from a draft. | **true** — Deletes the page with its elements. | **true** — The same operationId returns the stored result, and an outdated revision is refused. | **false** — Only the organization's templates. |
| `pdf_page_update` | PDF-Seite bearbeiten | **false** — Changes a page's name, role or orientation. | **true** — Overwrites these values and can change the role of other pages. | **true** — The same operationId returns the stored result, and an outdated revision is refused. | **false** — Only the organization's templates. |
| `pdf_page_reorder` | PDF-Seiten sortieren | **false** — Reorders the pages of a draft. | **true** — Overwrites the page order. | **true** — The same operationId returns the stored result, and an outdated revision is refused. | **false** — Only the organization's templates. |
| `pdf_page_guides_update` | PDF-Hilfslinien bearbeiten | **false** — Changes a page's margins, grid and guides. | **true** — Overwrites the guides; margins also define the writing area of letters. | **true** — The same operationId returns the stored result, and an outdated revision is refused. | **false** — Only the organization's templates. |
| `pdf_image_set` | PDF-Bild setzen | **false** — Shows an image asset in an image element. | **true** — Replaces the element's previous image. | **true** — The same operationId returns the stored result, and an outdated revision is refused. | **false** — Only images stored in the organization's or iPlanner's own asset library; there is no URL input. |
| `pdf_design_validate` | PDF prüfen | **true** — Checks a draft for structural errors; nothing is saved. | **false** — Read-only. | **true** — A repeat returns the same result. | **false** — Only the organization's templates. |
| `pdf_design_preview` | PDF-Vorschau erstellen | **false** — Renders a preview PDF and stores it as a private file for download. | **false** — Only adds a new private file; the draft is unchanged. | **false** — Each call stores another file. | **false** — Rendering and storage stay within iPlanner. |
| `pdf_design_export` | PDF exportieren | **false** — Renders the PDF with its form fields and stores it as a private file for download. | **false** — Only adds a new private file; the draft is unchanged. | **false** — Each call stores another file. | **false** — Rendering and storage stay within iPlanner. |

Notes on behaviour:

- `pdf_page_add`: Adds pages and changes the previous ending page to a continuation page. That replacement of an existing page role is why it is not additive-only.
- `pdf_page_duplicate`: Copies the source page and elements to new IDs without replacing the source. Insertion preserves the existing pages and their relative order.
- `pdf_image_set`: Replaces an existing element image source in the draft; it is not a read of the image.
- `pdf_design_preview`: Renders and stores a new private file. It does not overwrite or publish the source template. A repeated call may store another file, so it is a non-idempotent additive write, not read-only.
- `pdf_design_export`: Renders and stores a new private PDF including form fields. It does not overwrite or publish the source template. A repeated call may store another file.

## Search and runner helpers

These helpers offer no operation of their own: every operation they can find or run is also listed individually above, under its own name and annotations. A runner's hints are derived from the tools the person can use: a runner is destructive if any allowed target is, idempotent only if all of them are, and open-world if any of them is (a target without an explicit hint counts as destructive, not idempotent and open-world). The values below are those for the full catalog.

| Tool | Title | readOnlyHint | destructiveHint | idempotentHint | openWorldHint |
| --- | --- | --- | --- | --- | --- |
| `tools_search` | Funktionen finden | **true** — Ranks the tools the person may use for a request; nothing is run or changed. | **false** — Read-only. | **true** — A repeat returns the same results. | **false** — Searches only iPlanner's own tool catalog. |
| `tools_read` | Gefundene Funktion lesend ausführen | **true** — Runs only read-only tools found by tools_search. | **false** — None of its targets changes anything. | **true** — All of its targets are idempotent. | **false** — None of its read-only targets is open-world; it would be as soon as one allowed target were. |
| `tools_write` | Gefundene Funktion ändernd ausführen | **false** — Runs tools found by tools_search that change data. | **true** — Its targets include deleting, overwriting and sending tools; it is destructive as soon as one allowed target is. | **false** — Some of its targets, such as webhook_test, are not idempotent. | **true** — Some of its targets, such as email_send, reach destinations outside the organization. |
