# Schedule the runs

Use a native Codex automation in the project that contains the person's repository.
Each run uses this installed plugin and its Frontmost AI connector.
Do not create a workflow, install an action, or start an external program to run Autopilot.

The schedule wakes Autopilot. A run with no new scan and no other change ends without work.

## When to run

Read `run_config.cadence`, `next_scan`, and the person's timezone from the project and charter.

| `cadence` | Run |
|---|---|
| `daily` | Each day, two hours after the time of `next_scan` |
| `mwf` | 3 times a week, two hours after each scheduled scan |
| `weekly` | Two hours after the weekly scan, plus one run three days later to check changed pull requests |
| `off` | Do not schedule. See step 3 of Set-up |

For `mwf`, set the automation's weekdays to Monday, Wednesday, and Friday.
For `weekly`, use the weekday of `next_scan` and the weekday three days later.
If the next scan time or timezone is unavailable, ask for the missing value before scheduling.
Save the person's confirmed IANA timezone in `charter.md` before creating the automation.
If a scan is unfinished, skip the scan steps and read only changed pull requests. Read the scan on the next run.

## Create the automation

1. Confirm that the project folder and this plugin remain available to scheduled runs.
2. Confirm that the Frontmost AI connector works in that project.
3. Show the run times, timezone, project folder, and charter limits to the person. Ask before creating the automation.
4. Use the host's native automation tool to create the approved schedule with the prompt below.
5. Read back the saved schedule. Record its identifier, times, timezone, and project folder in `log.md`.

```text
Scheduled Autopilot run. In <absolute path of the repository>, follow the autopilot skill of the installed Frontmost AI plugin. Use its Frontmost AI connector. Nobody is here to answer questions. Stay inside frontmost-autopilot/charter.md. If the connector or required files are unavailable, report the blocker and stop. If nothing changed, print one line and end.
```

If the host cannot create a native automation, record that limitation. Do not claim that a schedule exists.
The person can still request individual runs in the same project.
Do not replace a failed automation with a shell command or an external scheduler.

## After scheduling

Report the saved run times and the automation's identifier. Explain how the person pauses or removes it through the host.
The charter's `paused` status stops work. It does not remove the schedule.
If the project cadence changes, propose the new run times in `log.md`. Change the automation only after approval.

The host controls whether a run can start while the computer is asleep or the app is closed.
Report the host's actual availability limits. Do not promise unattended execution without checking them.
