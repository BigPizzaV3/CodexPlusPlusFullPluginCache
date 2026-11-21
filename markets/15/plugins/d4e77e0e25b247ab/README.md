# Simple Photo Gallery

Create photo galleries and albums, upload pictures, organize a photo story and share it from ChatGPT. The plugin works with photos uploaded to the connected Simple Photo Gallery account.

## Try these tasks

- Make a travel album from vacation photos.
- Create a family gallery or event recap.
- Build a wedding photo collection or photography portfolio.
- Add chat attachments or existing library photos to a gallery.
- Arrange a trip into days, places or moments.
- Rename sections and move pictures between them.
- Reorder selected photos without disturbing the rest.
- Write captions and choose a cover photo.
- Review duplicate candidates and hide unwanted occurrences.
- Review an organization proposal before applying it.
- Check the published version and share its existing viewer link.
- Publish a reviewed draft with the chosen access settings.

## Workflows

[Setup](skills/setup/SKILL.md) opens the account's galleries and helps choose one useful first task. [Create](skills/create-gallery/SKILL.md), [organize](skills/organize-gallery/SKILL.md) and [publish](skills/publish-gallery/SKILL.md) cover the main processes. [Gallery management](skills/gallery-management/SKILL.md) contains the shared context, versioning and media-handling rules.

Draft editing, publishing and viewer access are distinct. Uploads and optional analysis use the account's available features and allowances. The plugin does not retouch pixels, order printed books or continuously sync a phone.

## Package and review

The [ChatGPT walkthrough](https://youtu.be/Mko7nVoVBBk) uses the dedicated demo account and its two sample galleries. It shows photo previews, photo inspection, an organization proposal awaiting approval, and the connected photo library. The recording begins with the account connected and workspace loaded; idle pauses are shortened.

The portable source contains one production MCP endpoint, five skills, 30 discovery terms, 15 example prompts, five positive review cases and three negative cases. It preserves the existing `simple-photo-gallery` package identity. The public display name is Simple Photo Gallery, and the initial public release is 1.0.0. The installed private test build has its own version history.

Review cases use the dedicated account’s existing private Gallery 1 and Gallery 2 and at least two distinct sample image originals in its library. The section case uses Gallery 1 and may reuse existing Day One/Day Two sections. Library insertion uses an existing section in Gallery 2, so it does not depend on the section case running first. The proposal case also uses Gallery 2, which already contains photos. Keep these prerequisites available for independent runs. Creation uses a separate Review Album draft, and permits an available slug or reuse on repeat runs. No positive case needs paid analysis, publication or deletion.

Pass criteria check observable, tool-backed outcomes and correct scope, not exact prose, chosen photos or tool order. Saving a pending proposal is allowed in the review-only case; applying it is not. Failed or invented outcomes do not pass.

The owner selected Creafex Lab, all available countries and no purchases through this plugin. Public submission requires working reviewer access, a verified demo recording, publisher policy review and required portal checks. Packaging or a private test upload does not complete public submission.

## Live case verification

On 2026-10-31, the five positive and three negative cases passed their functional criteria in fresh ChatGPT Work conversations using the dedicated demo account and production MCP server. The section case exercised its allowed repeat-run behavior because Day One and Day Two already existed. Independent saved-state checks confirmed that originals remained in the library, the new draft stayed unpublished, and the organization proposal remained pending.

The initial visual workspace failed to open in all five positive cases; one Try again loaded each workspace. This is a remaining UI reliability issue, not a resolved defect or an unconditional visual pass. The setup workflow already explains this recovery. See the repository’s detailed submission-test results for the distinction between functional outcomes and visual startup.
