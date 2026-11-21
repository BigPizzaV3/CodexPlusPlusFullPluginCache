---
name: build-candidate-profile
description: Build and improve the user's Himalayas candidate profile, which drives job matches, tailored documents and how employers find them, by importing from LinkedIn or a resume, editing experience, education, skills, work permits, salary expectations and search status, and setting a photo and email preferences. Use when the user wants to set up, import, review or update their Himalayas profile or account settings.
---

# Build the candidate profile

Follow [himalayas-basics](../himalayas-basics/SKILL.md) for the shared rules.
Profile tools need a Himalayas account.

## 1. Review what is there

Call `get_my_profile`. Report what is missing or weak for the user's goal:
primary role, location, work permits, salary expectations, search status,
experience with descriptions and skills, education, and tech stack.

## 2. Import (fastest for a new profile)

`import_profile` fills the profile from a LinkedIn profile URL or pasted resume
text. It runs in the background for a few minutes; call `get_my_profile`
afterwards to see the result.

- `append_only` adds what is missing and keeps what is there.
- `replace_all` overwrites the profile. Ask the user before using it.

## 3. Edit

- `update_profile`: name, bio, intro, location, `career_search_status`
  (`actively_searching`, `open_to_roles`, `closed_to_roles`), primary role,
  salary expectations, work permits and skills. Only the fields you pass
  change.
- `add_experience`, `update_experience`, `delete_experience` and the matching
  education tools take ids from `get_my_profile`. Deletes can't be undone.
- `update_tech_stack` replaces the list of tools and technologies. Names are
  matched to Himalayas' catalogue; unknown ones are requested for review.

Show the changes before writing them, then read the profile back.

## 4. Photo

- `update_profile_photo` sets the avatar or cover photo from an https image
  URL (JPEG, PNG, WebP or GIF, up to 5 MB).
- `list_headshots` lists headshots the user already made on Himalayas, and
  `use_headshot_as_profile_photo` sets one as the photo. `get_headshots_link`
  returns the page where they make new ones.
- Identity and work permit verification (the verified badge) isn't
  available through these tools. If the user asks, say it is done on
  himalayas.app. Never ask for or handle ID documents in the conversation.

## 5. Settings

- `update_email_preferences` turns Himalayas emails on or off; only the
  settings you pass change.
- `update_account` sets the account time zone used for email timing.
- Email address, password and account deletion can only be changed on
  himalayas.app.
