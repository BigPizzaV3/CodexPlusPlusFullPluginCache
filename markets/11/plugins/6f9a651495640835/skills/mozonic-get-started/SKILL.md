---
name: mozonic-get-started
description: Set up Mozonic after installation, confirm the account connection, and choose the first supported library workflow.
---

# Get started with Mozonic

1. Connect a Mozonic Pro account when prompted, then call `mozonic_auth_me` to
   confirm the account and plan.
2. This plugin works with audio already in the Mozonic library. For a local
   file, direct the user to upload it in https://app.mozonic.com first.
3. List the library with `mozonic_list_mixes`, then inspect a mix with
   `mozonic_get_mix` or queue correction with `mozonic_correct_mix`.
4. Long-running work is asynchronous. Use `mozonic_jobs_active` to check
   progress; only offer a download after the render completes.
