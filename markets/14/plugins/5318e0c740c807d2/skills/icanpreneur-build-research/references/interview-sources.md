# Adding evidence: routes in detail

## A. Interviews with specific people

Use when the user names respondents to interview.

1. **Contacts.** For each person: `list_contacts(ideaId, search: <name>)` to check they do not exist. If not, `create_contact(firstName, lastName, emailAddress?, jobTitle?, customerSegmentIds: [<segment id>])`. `ideaId`, first name and last name are required. Use only details the user gave. Search matches names, not email. Inspect saved email/profile fields to distinguish namesakes. Contact creation does not deduplicate automatically. Segment links are optional and do not determine research membership; preserve existing links when changing them.
2. **Interviews.** `create_interview(ideaId, contactId, researchId, languageTag, aiLed?, hostId?)`.
    - `aiLed` defaults to true: Icanpreneur's interviewer runs it through a link. `aiLed: false` is for an interview a person hosts; only human-led interviews default `hostId` to the authenticated user.
    - With `researchId`, the interview uses the research's script. A compatible `scriptId` overrides it for this interview only. Without `researchId`, `scriptId` is required and the interview is standalone.
    - The result includes `aiLedInterviewUrl`, specific to that contact, for AI-led interviews. `languageTag` is required and must support interviewing. Do not supply a host for an AI-led interview.
3. **Give the user the links.** A table works: name, interview ID, link. Say clearly that nothing has been sent. They share the link themselves.
4. The research also has one general link: `get_research` → `aiLedInterviewUrl`. It is returned even when AI-led interviews are switched off, so check `aiLedInterviewsEnabled` before giving it out.
5. Interviews move `NotStarted` → `InProgress` → `Completed`. Analysis starts after they complete. Only nonsynthetic `NotStarted` interviews can be edited (`update_interview`: delivery mode, host, meeting code, script, language). Imports created here are already `Completed`.

Create only the interviews the user asked for. Creating one can trigger processing.

## B. Existing transcripts or recordings

Use when the user has done interviews already and has the transcript files.

1. Each transcript must be an uploaded file: `upload_file(usage: "InterviewTranscript", name, mimeType, contentBase64)`. Accepted: pdf, docx, doc, rtf, txt, up to 10 MiB.
    - You need the file's real bytes from your client. Never rebuild or retype a transcript as base64. If your client cannot pass the file's bytes, say so, and ask the user to import it in the Icanpreneur app or to try a client that can attach files. Do not paste the transcript into a tool as text; no tool accepts that.
    - An optional original script can be uploaded with `usage: "ImportedInterviewScriptAttachment"` and passed as `scriptFileKey`. Without it, the interview has no script coverage.
2. Single-file `import_interview` requires a real contact. Use the person's name from the file or the user; ask if unknown and do not invent it. Reuse or create the contact (route A step 1); segment links are optional. Bulk `import_interviews` does not require a contact and does not link one automatically.
3. `import_interview(ideaId, type, contactId, fileKey, researchId?, hostId?, scriptFileKey?)`. `type` is the interview type, usually the research type. Passing `researchId` adds it straight to that research.
    - Import one file at a time by default. Use `import_interviews` for an authorized bulk import. It cannot take a contact for each file: contacts remain unlinked, and respondent names are detected asynchronously. Successful results preserve input order. Compare the returned IDs and saved interviews with the files. A failure may have saved/charged some imports and returns no per-file partial-results envelope; reconcile before retrying only missing work, never the whole batch. Saved successes from a failed batch may need platform help if their processing never started.
    - An imported interview is saved at stage `Completed`, has no AI-led link, may lack speaker roles and timestamps, and starts analysis automatically. Importing uses credits.
    - The importer is not recorded as the interviewer. Set `hostId` only if the user tells you who ran it.
4. Wait for analysis (`get_interview_analysis`, then `get_research_analysis`).

## C. Interviews already in the workspace

Use for "turn my existing interviews into a persona" when they are already saved.

1. Create BuyerPersona research for the segment (needs a script of type `BuyerPersona`; reuse or generate one).
2. `list_interviews(notInResearchId: <research id>, customerSegmentId: <segment id>)`. Interviews of other types can be added, for example problem-validation interviews. The `customerSegmentId` filter only narrows the list; it is not a rule about which interviews can join. When reorganizing evidence into a new segment's research, do not filter by the new segment's ID, or you will hide the interviews you are looking for.
3. Show the candidates (title, interviewee, type, `synthetic`, `imported`, stage). Add the ones the user picks with `update_research_interviews(idsToAdd: [...])`. Removing (`idsToRemove`) only unlinks; it does not delete the interview.
4. Adding interviews starts a refresh of the analysis and the persona. Wait as usual.

## D. Synthetic interviews and contacts

Use only when the user authorizes synthetic exploration. Having no respondents alone is not authorization to generate simulations.

- `generate_synthetic_interviews(ideaId, researchId, numberOfInterviews?)`: adds simulated interviews (default 5) to existing research. The number is additional, not a total.
- `generate_synthetic_contacts(ideaId, customerSegmentId, amount)`: creates synthetic respondent profiles. `amount` is required and counts new contacts. Ask how many. If the user tells you to decide, use 5 and say so.
- Both are billable. Synthetic interviews use a positive integer `numberOfInterviews` (default 5); synthetic contacts require a positive integer `amount`. Neither has a declared maximum; agree a bounded batch rather than promising unlimited capacity. Pending contact profiles are returned before full generation and have no ready/error flag; reread their details before presenting them as complete.
- Every result keeps its synthetic mark. Report the split whenever you describe findings.
- A synthetic persona is useful for sharpening hypotheses and questions. It is not a reason to skip real interviews. Say that once.

## Mixing routes

Real, imported and synthetic interviews can sit in one research. The persona and the analysis then blend them. Always report the split (`icanpreneur` → `references/evidence.md`). If the user wants a persona from real evidence only, create the research without synthetic interviews and do not add any.
