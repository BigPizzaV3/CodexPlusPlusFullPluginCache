---
name: app-store-listing
description: Make a complete App Store listing for an iOS app with AppStorePack, from picking a screenshot template to exporting the finished bundle. Use when the user wants App Store screenshots, a whole App Store listing, or help getting an app ready for the App Store, and when they first set up AppStorePack.
---

# Make an App Store listing

Use this workflow when the user wants their App Store listing made or improved
with AppStorePack. The user's own instructions come first: skip, reorder or
stop steps when they ask, and don't redo work they say is finished.

## 1. Find or create the project

1. Call `list_projects`. If a project matches the app the user means, use it
   and say which one. If more than one could match, ask which.
2. Otherwise create one with `create_project`. It needs the app's name; also
   pass a one- or two-sentence `pitch` on what the app does and who it's for,
   and the `category` when it's clear. Ask the user for anything you don't
   know. Don't invent features they haven't described.
3. Call `get_account` before the user puts in much work. If their plan doesn't
   include export, tell them once, plainly, and share the `plansUrl` it
   returns. Don't quote prices or encourage upgrading. Everything before the
   export step works on every plan.

## 2. Pick a screenshot template

1. Call `browse_templates` and suggest two or three templates that suit the
   app's category and look, with one line on why each fits.
2. When the user wants a closer look at one, show it with `preview_template`.
3. Apply the template the user picks with `apply_template`. Applying a
   template resets the captions to its placeholders.

## 3. Add the screenshots and logo

1. Call `request_screenshots`. It shows an upload panel where the user drops
   an app screenshot onto each panel and their logo onto the icon tile. Files
   go straight to AppStorePack, so never ask the user to paste images into
   the chat.
2. Wait until the user says they're done, then call `get_design` to see which
   panels have screenshots. Mention any panel that is still empty.

## 4. Write the captions

1. Read the caption slots from `get_design`.
2. Write one short, benefit-led headline per panel that matches what that
   panel's screenshot shows: at most 32 characters, and subtitles at most 48.
   If you can't tell what a screenshot shows, ask.
3. Save them with `set_captions`. If a line is rejected, fix it and try again.
4. Show the set with `preview_design` and offer changes: `adjust_panel` for
   layout, `add_panel` or `remove_panel` for the number of panels. Ask before
   removing a panel that has the user's screenshot.

## 5. Make the icon

If the user uploaded a logo, call `preview_icon` and offer `set_icon_style`
changes, such as a background that contrasts with the logo. If there's no logo
yet, call `request_icon`.

## 6. Write the App Store copy

Call `get_store_copy_rules`, then write the name, subtitle, keywords,
promotional text and description from what the user and the project say about
the app. Save them with `set_store_copy`. If a field breaks a rule, the whole
update is rejected with the reasons: fix those fields and save again. Show the
user what was saved.

## 7. Finish

- **Export:** call `export_bundle` and share the download link, which works for
  one hour. If it returns `exported: false`, pass on what it says and its link;
  nothing is lost.
- **App Store Connect:** to fill in the listing in App Store Connect instead,
  call `asc_status`, then link the app with `asc_list_apps` and
  `asc_link_project` if it isn't linked yet. Call `asc_plan_push` and show the
  user exactly what will change. Call `asc_push` with `confirm: true` only after
  the user explicitly agrees to that plan. A push replaces the version's
  screenshots, and it never submits the app for review.

## Notes

- If the user has the project open in the AppStorePack editor, ask them to
  reload it after you change something, or their open tab may overwrite the
  change.
- When a tool returns an error, say what went wrong in plain words and what
  you'll try next.
