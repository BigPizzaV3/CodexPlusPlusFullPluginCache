# Updater and installer problems
Use the exact updater status shown in `Cài đặt`. Current application logic distinguishes optional updates, mandatory updates, up-to-date state, check failures, download failures, and install failures.
Customer-safe checks:
1. Confirm the current VeTayStudio version and the target version shown by the updater.
2. Finish active production/render/device tasks before starting an update when the UI says the update is paused.
3. Check internet access and retry once after a transient check/download error.
4. Close VeTayStudio only when the updater instructs the user to do so.
5. Do not delete application data, projects, models, updater state, or Windows folders as a generic fix.
6. Do not use a downgrade installer unless the owner explicitly supports that path.
If the updater repeatedly fails, capture the exact message and escalate through Zalo for an owner-approved installer or recovery procedure.
