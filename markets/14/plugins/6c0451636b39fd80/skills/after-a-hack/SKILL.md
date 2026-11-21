---
name: after-a-hack
description: Guide the user through what to do when Relvato's monitors show signs that their website was hacked — contain it, clean it, check it again, then watch it closely with quarantine mode. Use when the user says their site was hacked or compromised, or Relvato found hack symptoms, unknown admins, unexpected file changes or injected scripts.
---

# After a hack

Use the Relvato Security Monitoring tools (`site_overview`, `list_runs`, `get_run`, `get_fix_prompt`, `get_activity_log`, `trigger_scan`, `get_quarantine`, `start_quarantine`, `extend_quarantine`). Call Relvato's checks **monitors** when talking to the user. Stay calm and practical: a finding is a sign, not proof, so say what Relvato saw and where.

## 1. What happened

Call `site_overview`, then `list_runs` and `get_run` for the failed security runs: hack symptoms, file integrity, admin users and sign-ins, script origins. On WordPress, `get_activity_log` shows recent sign-ins, new accounts and changed settings. Summarise what changed and since when, with each run's link.

## 2. Contain and clean

Tell the user, in this order:

1. Change the passwords of every administrator, the hosting account and the database, and remove admin accounts nobody recognises.
2. Restore a clean backup from before the first sign, or replace the changed core, plugin and theme files with fresh copies, and delete files that shouldn't be there. `get_fix_prompt` on a failed run gives the exact steps for what it found.
3. Update or remove the plugin or theme that let the attacker in, if a vulnerability monitor named one.
4. If the site was listed as unsafe, request a review in Google Search Console once it's clean.

File-integrity and script-origin changes the owner made on purpose are approved in the Relvato dashboard, never from here.

## 3. Check it again

With the user's OK, call `trigger_scan` with `group: "security"` and report each result. Runs count toward the monthly quota.

## 4. Watch it closely

On WordPress, suggest quarantine mode: `start_quarantine` runs the security monitors every hour for 48 hours, pauses plugin updates and alerts on every unexpected change. Call `get_quarantine` first: it says whether the account includes it and how many runs it uses. Ask before starting it. `extend_quarantine` keeps it on for longer; stopping it early is done in the Relvato dashboard.
