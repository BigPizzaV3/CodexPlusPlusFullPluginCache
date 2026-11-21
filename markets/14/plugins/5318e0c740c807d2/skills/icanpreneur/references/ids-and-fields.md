# IDs, enums and field rules

## Where each ID comes from

| Thing                | Get it from                                                                                | Pass it as                                                                                         |
| -------------------- | ------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------- |
| Workspace (idea)     | `list_ideas`, `get_idea`, `create_idea`: `uniqueId`                                        | `ideaId` (string)                                                                                  |
| Canvas item          | `get_canvas`: item `id`                                                                    | `itemId` together with `box`                                                                       |
| Customer segment     | `get_canvas`, box `CustomerSegments`: item `id`                                            | `customerSegmentId`; also inside `relatedItemIds` of other items; `customerSegmentIds` on contacts |
| Interview script     | `list_interview_scripts`, `generate_interview_script`: `id`                                | `scriptId` (interviews, script tools); `interviewScriptId` (research tools)                        |
| Research             | `list_research`, `create_research`: `id`                                                   | `researchId`                                                                                       |
| Buyer Persona        | `list_buyer_personas`: `id`; also `buyerPersonaId` on BuyerPersona research once available | `buyerPersonaId`                                                                                   |
| Persona conversation | `ask_buyer_persona`: `conversationId`                                                      | `conversationId` for follow-ups                                                                    |
| Interview            | `list_interviews`, `create_interview`, `import_interview`: `id`                            | `interviewId`                                                                                      |
| Contact              | `list_contacts`, `create_contact`: `id`                                                    | `contactId`                                                                                        |
| Research insight     | `list_research_insights`: category/insight `id` and full supporting evidence               | Identify the saved finding in your answer; there is no per-insight read tool.                      |
| Persona document     | `list_buyer_persona_documents`, `generate_*`: `id`                                         | `buyerPersonaDocumentId`; for a `PositioningAndMessaging` document also `positioningDocumentId`    |
| Note                 | `list_notes`, `create_note`: `id`                                                          | `noteId`                                                                                           |
| Idea member          | `list_idea_members`: `members[].user.userId` (string)                                     | `userId`                                                                                           |
| Idea invitation      | `list_idea_invites`: `id`                                                                  | `inviteId`                                                                                         |
| Host                 | `members[].user.userId` from `list_idea_members`                                           | `hostId` (string)                                                                                  |
| Uploaded file        | `upload_file`: `fileKey` (string)                                                          | `fileKey`, `fileKeys`, `scriptFileKey`, `logoFileKey`                                              |

`relatedDocuments` on a document lists the documents it was generated **from**, not documents generated from it.

Interview details come in two shapes. Standard interviews have `scriptId` and `transcriptId`. Imported interviews (`imported: true`) have `transcriptFileId` and nullable `scriptFileId` instead. Upload keys are inputs only; do not treat those saved numeric IDs as reusable upload keys. The same read tools work for both.

## Enums

- Canvas `box`: `Problem`, `Solution`, `KeyMetrics`, `UniqueValueProposition`, `UnfairAdvantage`, `Channel`, `CustomerSegments`, `CostStructure`, `RevenueStreams`. Customer segments have their own create and update tools. Other boxes use `create_canvas_item` and `update_canvas_item`.
- Research type and interview type: `ProblemDiscoveryAndValidation`, `WinLoss`, `BuyerPersona`, `Other`.
- Interview stage: `NotStarted`, `InProgress`, `Completed`. Only `NotStarted` interviews can be updated.
- Analysis status: `NotStarted`, `Pending`, `Complete`, `Error`.
- Persona status: `Pending`, `Complete`, `Error`.
- Document type: `PositioningAndMessaging`, `LandingPage`, `CustomerPitchDeck` (the sales deck).
- Preview type: `WebPage`, `GoogleSlidesPresentation`.
- Idea role: `Viewer`, `Editor`, `Administrator`. Invitations can offer only `Viewer` or `Editor`.

## Paging

`take` defaults to 20 (1 to 100) and `skip` to 0 on paged tools. For a full traversal, omit `afterId`, hold filters/order fixed and advance `skip` to `totalCount`. `afterId` is a tool-specific numeric ID filter applied before skip, not a cursor in sorted order. Some services compute totalCount before that ID filter, so it is not a reliable traversal target with afterId. Research insights/quality, members, invitations and catalogs are unpaged.

## File usage by consumer

| Tool field                                                          | `usage` to upload with              |
| ------------------------------------------------------------------- | ----------------------------------- |
| `create_idea.fileKeys`                                             | `IdeaCreationDocument`              |
| `ask_buyer_persona.fileKeys`                                       | `ChatFile`                          |
| `create_idea.logoFileKey`, `update_idea.logoFileKey`                | `IdeaLogo`                          |
| `import_interview.fileKey`, `import_interviews.fileKeys`            | `InterviewTranscript`               |
| `import_interview.scriptFileKey`, `import_interviews.scriptFileKey` | `ImportedInterviewScriptAttachment` |
| `update_buyer_persona.fileKey`                                      | `BuyerPersonaImage`                 |

Use the upload usage matching the intended consumer above; uploading a file does not create the resource that uses it.

## Update semantics

- Omitted fields are unchanged. Use `null` only for fields marked nullable in the tool schema.
- Profile/content arrays such as `sections`, `relatedItemIds` and `customerSegmentIds` replace the stored value. `[]` clears them. Membership `idsToAdd`/`idsToRemove` are deltas, not replacements.
- Updates need at least one field besides the identifying IDs.
- Updating a research script or language does not change interviews that already exist. They keep their own script and language. Interviews snapshot their script's latest content when they start.

## Research membership and segments

Research membership decides which interviews contribute to a research's analysis. A research has a default interview script, and its interviews may have used other scripts. A contact's customer segments are optional and do not decide whether the contact's interviews can join a research. A script belongs to one segment and `duplicate_interview_script` cannot change that. Creating research or changing its default script requires the same segment and the same research/interview type. Adding existing interviews only requires the same workspace. Script duration is any positive finite number of minutes, with no declared maximum; ask for a sensible duration when needed.
