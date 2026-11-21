# Aggregate marking and checked generic schemes

Privacy boundary: this public plugin is for adult educators and creators. Never
transmit personal information about children under 13 to OpenAI. Use anonymous
or synthetic inputs only; do not request, send or retrieve pupil names, pupil
ids, rosters, photographs, scripts, individual answers or individual results.
Apply this boundary whenever ages or identifiability are uncertain. Do not
open, screenshot, upload or read back private pupil records through a browser
or another connector. Give the exact native link and hand the sensitive step
to the adult user to complete independently. Do not read a record first merely
to decide whether it contains personal information.

Use only current public operations. Reads need `marking:read`; permitted
scheme/preferences/session-settings writes need `marking:write`. Request the
relevant explicit OAuth consent without requesting credentials in chat.
Ownership or teacher consent does not permit a pupil-record read through this
public integration.

## Safe summaries and analysis

`get_marking_overview`, `list_marking_sessions` and `get_marking_session`
provide owned session-level metadata, progress/counts and native links only.
They do not expose pupil identities, scripts, page images, raw answers,
individual marks/results, overrides or notes. Use actual returned session ids;
do not guess them or expand to pupil records.

`get_marking_analysis` provides numeric aggregates only, with generated
`questionNumber` ordinals rather than stored question ids or question text.
Session scores are suppressed below five assessed pupils; each question's
scores are suppressed below five answered pupils. Explain suppression and
complete versus marked-so-far averages using the actual response, without
inferring missing scores. Never request raw answers, named clusters, individual
results, stored identifiers or reteach prose, or reconstruct them from the
aggregate. Session responses omit labels and expose page-status counts only,
not page ids, images or errors. The overview preserves native
`freePages.remaining`/`limit`, but its
credit-derived `month.pagesLeft` is null rather than issuing/refreshing credits
for a read. Do not invent an allowance from that null value.

For individual inspection, transcription, corrections, notes, scan/crop
inspection, capture/uploads, closing and reports/exports, give the exact
private native marking link and hand the work to the adult independently.
Do not open or screenshot it and do not read the private outcome back. There
are no pupil-specific mark-override or answer-note operations in the public
surface, and no saved-tool/resource/browser workaround.

## Checked generic schemes

`list_marking_papers` and `get_marking_paper` identify owned schemes using safe
metadata without saved paper titles. Use only anonymous or synthetic generic
paper content. Do not read an uncertain saved paper merely to decide whether
it contains personal pupil data. A scheme known to be `learned_from_script`
returns metadata and `nativeEditorRequired` rather than its structure or
checked question ids. Hand it to the adult in the native editor without a
browser readback; never recreate that blocked read through another operation.

The adult must explicitly check proposed questions, accepted/rejected generic
answers, marks and rules before `create_structured_marking_paper` receives its
exact disclosed `structure` and `teacher_checked:true`. AI confidence is not
approval. Native totals are recomputed; this operation uploads/marks no scripts
and makes no model/prefill call. `rename_marking_paper` changes the requested
generic title. `confirm_marking_paper` records only an actual adult check of
that ready generic scheme. Uploaded-paper extraction is an independent native
handoff, not an agent browser readback workflow.

## Session settings and retention

`create_marking_session` and `update_marking_session_settings` use only their
closed fields: requested anonymous title, owned paper/class references, modes
and retention settings. Responses stay session-level summaries. They do not
capture, upload or mark scripts. Keep the actual id/link rather than creating
a duplicate after a timeout. Native state rules restrict paper changes after
marking and retention changes once a page arrives.

For `save_results:false`, explain automatic 48-hour expiry and deletion of
scripts/results on native close. Obtain explicit discard agreement before
`discard_results_confirmed:true`; a request to start a session alone is
insufficient. Session closing itself is an independent adult native action.
Poll only existing aggregate processing state every 15–30 seconds, at most
eight times, then return the current state and exact native link.

`get_marking_preferences` and `update_marking_preferences` read/change only the
requested `show_tips` setting. They do not change schemes or pupil marks.
On permission/state/ownership errors, explain the actual refusal, without
upsells, purchases, retries that risk duplicates or any pupil-data bypass.
