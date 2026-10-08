# Preferences, bedtime schedules, and onboarding tool map

Treat every tool in this file as availability-sensitive. These tools exist in
the 61-tool source contract but may be absent from an active client. Check the
runtime tool catalog before calling or naming them.

## Profiles

| Tool | Choose it for | Resolve or verify |
|---|---|---|
| `cora_get_profile_options` | Valid stable IDs for training, rest, and food preference fields. | Use returned IDs rather than inventing enum values. |
| `cora_get_training_profile` | Current training goals, preferences, and constraints. | Read before setting list fields. |
| `cora_set_training_profile` | Save known training goals, preferences, and constraints. | Omitted fields stay; supplied lists replace. Re-read. |
| `cora_get_sleep_profile` | Current overnight routine preferences. | It may differ from the app's on-device screen. |
| `cora_set_sleep_profile` | Save overnight goals and preferences. | A profile is not a schedule or recorded session. Re-read. |
| `cora_get_nutrition_profile` | Current food preferences and restrictions. | Read before setting list fields. |
| `cora_set_nutrition_profile` | Save food preferences and restrictions. | Supplied lists replace rather than append. Re-read. |

Fetch profile options before setting fields whose valid identifiers are not
already established in the conversation. Explain replace-all list scope; do
not erase existing selections accidentally.

## Bedtime schedules

| Tool | Choose it for | Resolve or verify |
|---|---|---|
| `cora_get_sleep_schedules` | Active bedtime/wake schedules and current versioned IDs. | Read before update/delete. |
| `cora_set_sleep_schedule` | Create or update bedtime and wake targets by weekday. | An update returns a new ID; use that ID for later actions and re-read. |
| `cora_delete_sleep_schedule` | Soft-delete one exact schedule. | Resolve latest ID; confirm unless the exact deletion was requested. |

Do not treat a bedtime schedule as a recorded overnight session. The external
MCP does not write manual sessions or return raw device intervals.

## Onboarding intake

| Tool | Choose it for | Resolve or verify |
|---|---|---|
| `cora_get_onboarding_status` | Current intake stage, pillar, and state version for a new user. | Intake closes after native onboarding completion. |
| `cora_get_onboarding_options` | Stable field and option IDs for the current stage/pillar. | Request only the stage/pillar returned by status. |
| `cora_save_onboarding_step` | Validate and save one intake step. | Send the latest `state_version`; chain the returned version into the next step. |

Run onboarding as a state machine:

1. Read status.
2. Fetch options for exactly the returned stage and pillar.
3. Ask the user conversationally for the current step's missing values.
4. Save stable IDs with the latest `state_version`.
5. Repeat with the returned next state until `collection_status` is complete.

Do not jump stages, reuse a stale state version, invent an option ID, or keep
writing after intake reports completion.
