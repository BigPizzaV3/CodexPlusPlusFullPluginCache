---
name: ando-tune-notifications
description: Tune a person's Ando notification preferences to preserve useful attention and reduce noise. Use for first notification setup, excessive alerts, or choosing delivery devices and events.
---

# Tune notifications

Read [Ando basics](../../references/ando-basics.md) for identity, current-schema discovery, access, and write authorization. Establish whose preferences should change, which events need attention, and which devices should deliver them. Preserve explicit notification choices already supplied.

## Inspect both delivery controls

Follow the current [Notifications guide](https://docs.ando.so/docs/notifications). Delivery depends on both Ando preferences and browser/device permission. The desktop event setting covers desktop-app and browser push; mobile delivery has its own setting. Sounds, focus modes, and operating-system controls may affect what the person notices.

Read permitted current preferences before editing. If delivery is missing, use [Troubleshoot your setup](../ando-troubleshoot-setup/SKILL.md) to distinguish disabled events, device permission, and a delivery failure. Muting everything is not a diagnosis.

## Choose what deserves attention

Use the person's work pattern to choose events and destinations. Direct requests, mentions, and followed work may deserve attention; reactions or sounds may be less useful. Treat those as choices, not universal defaults. Make the requested change without changing unrelated notification or conversation settings.

Operate only on the authenticated person's permitted preferences. Inspect the actual notification tool's identity and credential requirements: an agent credential or ordinary OAuth access may not support personal preferences. Do not switch principals silently or treat another member's settings as accessible. If the operation is unavailable, prepare the proposed settings and guide the person through the current app surface; keep credentials in secure settings.

Human notifications and agent receiving/subscription settings are different controls. Do not change agent proactivity, inbox receiving, automation schedules, or provider alert feeds to satisfy a person's notification preference request.

## Verify and explain recovery

Read back saved preferences, separating what changed from a proposal or app handoff. For a requested delivery check, use an authorized representative event and confirm the notification on the intended device with the person. A saved setting alone does not prove push delivery.

Report the selected events/devices, any system permission still needed, and how to restore the previous preference. Avoid promising that notifications will arrive while the relevant device, browser, or runtime is unavailable.
