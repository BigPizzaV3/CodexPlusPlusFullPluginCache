---
name: dashboard-upload-and-remediation
description: Upload a package to the authenticated OpenAI plugin dashboard and resolve visible validation issues.
---

Open `https://platform.openai.com/plugins` in the user-authorized external browser and identify the existing published plugin record before acting. If the request is an update, use that record's version workflow; do not create a second public plugin. If a required browser or file permission is missing, request it once and resume from the last checkpoint after it is granted.

Run local validation and package preflight first. Upload the generated ZIP, inspect the visible result, and compare errors against the local package. Fix only verified issues, rebuild with a new version, and reupload. Typical issues include missing logo/composerIcon, invalid image dimensions, more than three default prompts, subtitle length over 30 characters, combined plugin/skill names that are too long, incomplete skill scans, missing links, and package structure errors.

Treat `Uploading` and `Scanning` as asynchronous jobs managed by a bounded recovery loop:

1. Save the package hash, plugin ID, submission ID if visible, current dashboard URL, and workflow stage.
2. Poll at 2, 4, 8, 15, 30, and 60 second intervals, refreshing or reopening the same submission when the UI is stale.
3. After each refresh, inspect the actual status and issue list. A disabled button or unchanged screen is not proof of failure.
4. If the timeout budget is reached, navigate back to the plugin list and check whether the draft already exists before uploading again.
5. Retry only when the prior attempt is confirmed failed or absent, and never create a second public listing for an update.

Use a bounded retry budget (default: three recovery attempts per stage), record every attempt in the issue ledger, and stop for user permission only when the browser session, file access, developer identity, or final compliance authorization is required. Do not claim success from an attempted click; verify the resulting version, status, plugin ID, and visible issue list.
