---
name: security-review
description: Review a website's security from Relvato's monitors — known-vulnerable plugins, themes and core, signs of a hack (spam pages, injected redirects, a listing as unsafe), changed or unexpected files, new admin users and suspicious sign-ins, exposed backups and config files, new third-party scripts — and say what to do first. Use when the user asks whether their site is secure or hacked, or about vulnerabilities, malware, exposed files or a security alert.
---

# Review a site's security

Use the Relvato Security Monitoring tools (`list_sites`, `site_overview`, `list_checks`, `list_runs`, `get_run`, `get_fix_prompt`, `get_updates`, `get_activity_log`, `get_quarantine`, `get_safe_update`, `trigger_scan`). Call Relvato's checks **monitors** when talking to the user.

## 1. Which site

Use the site the user named, if any; otherwise call `list_sites` and ask if there are several. If the tools answer that the user isn't signed in, tell them to sign in to Relvato in ChatGPT, then try again.

## 2. Read the security monitors

Call `site_overview` for what needs attention. Call `list_checks` to see which security monitors the site has, then `list_runs` and `get_run` for each one whose latest run failed or warned. Relvato's Security group:

- `vuln-scan`: known vulnerabilities in the site's plugins, themes and WordPress core
- `hack-symptoms`: signs of a hack, such as spam pages, injected redirects or links, or a listing as unsafe
- `file-integrity` and `theme-integrity`: core, plugin and theme files that changed, or files that shouldn't be there
- `user-audit` and `admin-logins`: new or elevated admin users, and suspicious sign-ins
- `exposure-scan`: backups, debug logs, `.env` and config files anyone can download, and leaked keys
- `script-origins`: new third-party scripts on the pages, a card skimmer's usual way in
- `mixed-content`, `wp-health`, `backup-freshness` and `async-health`: hygiene

On WordPress, call `get_updates` for vulnerable plugins with an update and any rollbacks, `get_activity_log` for recent sign-ins and account changes, and `get_quarantine` for a recent cleanup watch.

## 3. Report

Order by urgency:

1. Signs of an active compromise: hack symptoms, unexpected file changes, unknown admins, new scripts.
2. Known vulnerabilities, and whether a fixed version exists.
3. Exposed files.
4. Hygiene.

A finding is a sign, not proof. Say what Relvato saw, where, and since when, and link each run. If nothing is wrong, say which monitors are watching, so "all clear" means something.

If the site has no security monitors, suggest adding them with `start_monitoring_for_goals` and the goal `security`, and only with the user's OK. Most of them need the site's ownership proven first; the `security-setup` skill walks through that.

## 4. What to do

- **File-integrity, script-origin and DNS changes** are approved by the owner in the Relvato dashboard, never from here. Say what to look at and link the site.
- **Vulnerable plugin on WordPress:** give the user the run's link (from `get_run`). From there an administrator updates the plugin to the fixed version (or deactivates it) in WordPress, and Relvato re-runs the monitors that were passing and says if anything broke; `get_safe_update` shows how it went. This app doesn't change the site itself.
- **Exposed files:** say which file, why it matters (a backup or `.env` file can hold database passwords and keys), and that it should be deleted from the server or blocked; any key it held should be changed. Call `get_fix_prompt` on the run for the exact steps.
- **What looks like an active hack:** follow the `after-a-hack` skill.
- **Cause in the site's code**, such as an injected script in a template: call `get_fix_prompt` on the failed run and explain the fix.
