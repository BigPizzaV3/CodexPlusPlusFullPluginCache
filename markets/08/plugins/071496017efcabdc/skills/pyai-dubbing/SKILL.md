---
name: pyai-dubbing
description: "Translate and dub supplied audio recordings into a supported target language with PyAI Dubbing."
---

# Dubbing

Use the connected PyAI tool schemas as the source of truth; clients may prefix tool IDs with the server name. If PyAI is disconnected, direct the user to the host's browser sign-in. Keep credentials out of chat. Respect the selected project and the user's authorized task.

Tools: `whoami`, `get_dub_capabilities`, `create_dub`, `get_dub_job`, `get_dub_audio`

Check `get_dub_capabilities` for current supported input/output languages before submitting. Use the user's authorized HTTPS source audio URL and selected languages with `create_dub`. Do not upload a local file to an unrelated hosting service without authorization.

Submit once and retain the returned `job_id`. Poll `get_dub_job` (displayed as “Dubbing”) until done or an error. Pending/processing states do not justify a second submission. If a timeout leaves submission uncertain, report that rather than creating a duplicate job.

When done, call `get_dub_audio` and present the actual playable audio or download link. If waiting must stop, provide the job ID and status so the user can resume. Only claim languages and media handling the live capabilities support.
