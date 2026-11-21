---
name: get-started
description: How to build and publish a web app on Pilely from this chat — find or create the app, change its files, then build and publish it.
---

# Build and publish a Pilely app

1. Find the app with `list_my_apps`, or make a new one with `create_app` (it starts as a Vite starter project).
2. Look at the files with `list_files` and `read_file`.
3. Change them with `write_files` (whole files) or `edit_file` (one exact replacement). Use `delete_files` only when the user asks to remove files.
4. When the user wants it live, call `build_publish`, then call `get_build` until the state is `live` or `failed`.
   - `live`: give the user the URL.
   - `failed`: read `failed_step`, `error` and `log_tail`, fix the files, and publish again. The previous live version stays up.
5. If the app needs a database, groups, rate limits or email, read that service's manual with `read_service_api_doc` first, then call its routes: `read_service_data` for a route that only reads (its last path segment is `list`, `get`, `info`, `search`, `resolve`, `lookup` or `download`), `write_service_data` for every other route.

Publishing replaces the live version at `https://<app>.pilely.app`. Confirm with the user before publishing or deleting files.

Pilely's full step-by-step guide to building, publishing and moving an app with these tools — talking the app through, the app's note, setting up its services, writing the code — is available from `get_app_workflow_instruction`.
