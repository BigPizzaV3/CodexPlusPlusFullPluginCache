---
name: release-check
description: >-
  Check whether an iOS version is ready for App Review, explain what blocks
  it, fix what MetaRun can stage, and submit when the person approves. Also
  explains an App Review rejection. Use for "is my app ready to submit", "why
  is Submit greyed out", "ship 2.4", "attach the new build", "Apple rejected
  my app, why".
---

# Release check: from "is it ready?" to submitted

## 1. Find the version and the build

- `apple_list_apps`, then `apple_list_versions`: the editable version is the
  one being prepared (or a rejected one, which stays editable).
- No editable version: `apple_preview_create_version` stages one (Apple allows
  only one at a time).
- `apple_list_builds` lists uploaded builds; `apple_preview_set_version_build`
  attaches one. Builds come from Xcode or CI; MetaRun does not upload them.

## 2. Run the readiness sweep

`apple_preview_submit_for_review` is the sweep. Its card lists every blocker:
version state, missing build, export compliance, App Privacy, empty required
fields per language, and what App Review already holds. Explain blockers in
plain words and stage the fixes MetaRun can make (listing fields through the
localize-listing flow, the build through `apple_preview_set_version_build`).
App Privacy answers are published in App Store Connect itself; say so.

## 3. Submit only on the person's click

When nothing blocks, the card offers Submit for review with a confirmation
checkbox. Only the person can tick it and press Submit. Do not describe the
version as submitted until the card says so.

## After a rejection

`apple_list_review_submissions` shows App Review history newest first,
including the guideline Apple cited. Explain the verdict, help fix the cause,
then run the sweep again: a rejected version is resubmitted through the same
card, never by creating a new version.
