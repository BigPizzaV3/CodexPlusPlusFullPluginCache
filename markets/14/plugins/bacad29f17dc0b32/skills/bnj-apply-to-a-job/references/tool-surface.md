# BNJ tool surface

The 20 tools exposed by the Brave New Jobs MCP server for ChatGPT, grouped by
what they are for. Read-only tools are safe to call freely. A tool marked
"destructive" overwrites or discards something (see Notes); of those, only
`submit_application` reaches the employer. Every tool requires the candidate to be
signed in to BNJ through the connector.

There is no tool that stores, quotes or summarises the conversation, and no tool
that rates, scores or profiles the candidate. If you are looking for one, it does
not exist and its absence is deliberate.

## Finding work

| Tool | Read-only | What it does |
|---|---|---|
| `search_jobs` | yes | Filtered search over published jobs: keywords, location, minimum salary, employment type, workplace type, department. |
| `get_job_details` | yes | Full profile for one job: description, application requirements, screening questions, employer info, legal documents. |
| `save_job` | no | Bookmarks a job. Idempotent, and there is no unsave. |
| `saved_jobs` | yes | Lists bookmarked jobs. |

## Session

| Tool | Read-only | What it does |
|---|---|---|
| `check_login_status` | yes | Reports who is signed in. Selects no CV: use `list_my_files` and `select_file_for_application`. |
| `logout` | no, destructive | Clears the session and any open draft. Stored data is untouched. |

## Files

| Tool | Read-only | What it does |
|---|---|---|
| `list_my_files` | yes | Lists the candidate's CVs or cover letters. Takes `kind: "cv" \| "cover_letter"`. |
| `get_upload_link` | yes | Returns the browser page where the candidate uploads a file. Starts no upload itself. |
| `select_file_for_application` | no, destructive | Pins an existing file to the draft, replacing any earlier choice of that kind. Checks ownership, kind and upload confirmation. |
| `get_cv_text` | yes | Plain text of a stored CV. |
| `get_cv_json_schema` | yes | The CV shape BNJ expects. |
| `upload_cv_data` | no, destructive | Attaches the parsed CV to an uploaded CV file (replacing any parsed data already on it), or to the draft on jobs that accept the CV without the file. |

Accepted uploads: pdf, doc, docx. Max 5 MB, max 5 files per kind per candidate.

## Building the application

| Tool | Read-only | What it does |
|---|---|---|
| `start_application` | no | Opens a draft. Refuses if a draft for a different job is open, or if the candidate already applied to this job, unless that application was withdrawn, rejected or disqualified. |
| `answer_screening` | no | Records one screening answer on the draft. |
| `prefill_answers` | no | Records several answers at once, drawn from the CV. Skips already-answered questions and invalid values. Get the candidate's agreement first. |
| `process_cv` | yes | Renders the CV alongside the still-unanswered questions. Records nothing. |
| `update_application` | no, destructive | Sets expected salary, inline cover letter text, or whether the CV may be used for inference. Replaces the previous value. |
| `acknowledge_legal_documents` | no | Records which mandatory documents were accepted. Additive: earlier acceptances are kept. |
| `submit_application` | no, destructive | Files the application. Requires `confirmed: true`. |
| `my_applications` | yes | Lists the candidate's own applications and their status. |

## Notes

- Nothing reaches the employer before `submit_application`. Draft state lives in
  the session until then. Some writes replace earlier values
  (`update_application`, `select_file_for_application`, and `upload_cv_data` on
  the stored CV), and `logout` discards an open draft; none of them touch a
  submitted application.
- All ids are UUIDs returned by a previous tool. Never construct one.
- No tool reaches outside BNJ's own database, file storage and sign-in service.
- The application is built from the candidate's CV, their screening answers and
  their cover letter. Nothing else about them is collected through this channel.
