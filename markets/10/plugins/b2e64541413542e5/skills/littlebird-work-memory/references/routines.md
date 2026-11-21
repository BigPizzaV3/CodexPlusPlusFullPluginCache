# Littlebird routines

Use the server's current schemas and descriptions as the source of truth.

## Create a routine

Use a short title and a self-contained prompt addressed to the assistant that
will run unattended. Specify which meetings, integrations, or context to read,
what to produce, and the output format. Do not end with questions that would
require an absent user to answer them.

Use the user's schedule and timezone. Resolve meaningful ambiguity before
creating the routine. A weekly schedule needs its weekdays and local time; a
monthly schedule needs its day and time. Follow the tool's actual allowed values.
Do not add notification destinations or change the requested reasoning mode
without a basis in the user's request and the tool's requirements.

When exposed by the server, use a digest for reports on every run, a watcher for
conditional notifications, and a reminder for one message at a specific moment.
For a watcher, state the notification condition explicitly and follow the tool's
behavior for failed checks. A watcher about a single occurrence must stop after
notifying once. Follow the tool's auto-pause guidance for mostly silent watchers.
For a reminder, use the message itself as the prompt and the required date/time.

Creation may produce an immediate first report for a recurring routine; explain
that behavior when relevant. A tool response about a plan limit is not a
successful creation. State the saved title and schedule after success.

## Update a routine

Read the current configuration first. Submit only fields the user wants changed.
If a prompt or schedule is a full replacement, preserve its unrelated contents
and send the complete replacement rather than a fragment.

Honor an exact change already requested by the user. If the intended edit is
unclear, show the proposed change and resolve it before writing. Do not create a
second routine when the user asks to change an existing one.

Follow the tool's restrictions on read-only routines, protected fields,
confirmation for permanent retirement, and calls from inside a running routine.
Updates apply from the next run when that is what the server states; do not claim
that updating a routine reran it. Report the returned outcome precisely.
