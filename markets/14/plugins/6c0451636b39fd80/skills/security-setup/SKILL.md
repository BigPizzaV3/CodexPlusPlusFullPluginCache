---
name: security-setup
description: Set up Relvato's security monitoring for a website — add the site, prove it's the user's (the Relvato WordPress plugin or a DNS record), add the security monitors and run them for the first time. Use when the user wants their site watched for hacks, vulnerabilities or exposed files, or asks how to start.
---

# Set up security monitoring for a site

Use the Relvato Security Monitoring tools (`list_sites`, `add_site`, `verify_site`, `start_monitoring_for_goals`, `list_checks`, `add_checks`, `trigger_scan`, `list_runs`, `get_run`). Call Relvato's checks **monitors** when talking to the user.

## 1. Add the site

Call `list_sites`; if the site is there, use it. Otherwise call `add_site` with the address and `platform` (`wordpress` or `other`). If the tools answer that the user isn't signed in, tell them to sign in to Relvato in ChatGPT, then try again.

## 2. Add the security monitors

Call `start_monitoring_for_goals` with the goal `security`. It adds the security monitors the account allows. To pick them one by one instead, use `list_checks` and `add_checks`.

## 3. Prove the site is the user's

Most security monitors need the site's ownership proven: they read the site from inside (vulnerabilities, file integrity, admin accounts and sign-ins need the Relvato WordPress plugin) or probe it the way an attacker would (the exposed-files scan and signs of a hack). `add_site` returns `setup.nextStep`, the quickest way:

- **WordPress:** install and connect the Relvato plugin from WordPress → Plugins → Add New (search "Relvato"). Connecting it is the proof.
- **Any other site:** add the DNS TXT record or the homepage meta tag from `setup.nextStep`.

Then call `verify_site`. Never tell the user the site is proven, monitored, watched or will alert them before `verify_site` says so: until then the monitors are added but don't run on their schedule (`scheduleStarts`).

## 4. First runs

Before proof, `trigger_scan` can run the public monitors by hand, 3 times a day per domain. These are real runs against the live site: never call them a test, a preview or a simulation. Once the site is proven, call `trigger_scan` with `group: "security"` to run them all. Ask first, because runs count toward the monthly quota. Tell the user how long to expect (`estimatedMinutes`, `tellUser`), read `progress.line` to them while runs are live, and report each result with `get_run` when they finish. For what the results mean, follow the `security-review` skill.
