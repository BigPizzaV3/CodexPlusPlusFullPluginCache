---
name: get-started-with-aperture
description: Help users get started with Aperture Read, choose something useful to read, or set up a recurring brief. For requests to save an existing answer, use the saving workflow.
---

# Get started with Aperture Read

Use two stages: try saving and reading, then create something useful to keep.
Use the user's existing topic, answer or report request. Do not require a
practice guide before saving their own content.

## Choose the entry

- General onboarding: call `get_onboarding_guidance` with `stage="start"`.
  Save its complete canonical welcome guide through `save_document`, using
  the installed save skill and live tool schema. Return the real reader link
  and receipt warnings. Invite the user to open it and check its ending.
- Useful reading ideas or continuing onboarding: request `stage="useful"`.
  Use the returned question, examples and editable templates. Ask only for
  missing details. Create one preview, offer shorter/deeper/different-focus
  changes, then save the chosen complete version when authorized.
  If the user chooses a recurring recipe, fetch the recurring guidance before
  setting up the schedule.
- Recurring reports: request `stage="recurring"`. Start with a useful preview
  as the first save. Review the schedule and timezone before using supported
  ChatGPT scheduling controls. Include the returned complete saving and
  recovery instructions directly in the reviewed task prompt.

Do not create a schedule unless the user requests one. If scheduling is
unavailable, give the full prompt for manual setup. Treat a created schedule,
a completed run, and a confirmed saved receipt as separate outcomes.
Verify one actual scheduled save; an interactive save is not that evidence.

## Connection and recovery

If tools need authorization, help the user select Aperture Read with `@`
and connect it. Pasting literal `@` text does not select the integration.
Saving requires an Aperture Read account. New users should follow signup in
the selected integration's account setup flow, including any invitation or
registration limits. Existing users should sign in with their Aperture Read
account. Check the destination account before approving access, then resume
the chosen stage.

If guidance is unavailable, use the returned `help_url` when available.
Otherwise, share the [public setup guide](https://apertureread.com/help/chatgpt).
Keep the user's topic or answer and selected integration. Do not fabricate a
canonical guide, receipt, reader URL, or schedule. Keep saving outcome separate
from onboarding advice.

For every save, preserve the full text, ending and references. Follow the
installed save workflow and tool recovery contract. Generate a fresh UUID
for a new read. Retry only the original capture ID with its exact arguments,
at most twice. Never reconstruct missing arguments or repeat a confirmed save
to obtain a card. Keep the original content when saving cannot be confirmed.

Stage two is optional. Do not require a third practice save, a minimum report
length, or multiple tasks before the user can read normally.
