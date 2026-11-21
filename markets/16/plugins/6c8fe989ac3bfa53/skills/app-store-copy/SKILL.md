---
name: app-store-copy
description: Write or improve the App Store copy of an AppStorePack project, meaning the app name, subtitle, keywords, promotional text and description, checked against Apple's limits and rules. Use when the user asks for App Store text, keywords or other App Store search help for their app.
---

# Write App Store copy

The user's instructions come first: when they ask about one field, change only
that field.

1. Find the project with `list_projects`; ask if it isn't clear which one the
   user means. Then call `get_project` for its current copy, the app's details
   and any rule violations.
2. Call `get_store_copy_rules` and follow its limit and guidance for every
   field you write.
3. Write from what the user and the project say about the app. Don't invent
   features, awards, rankings or prices, and don't mention other apps.
4. When the user asks for a change, save it with `set_store_copy`, passing only
   the fields that change. When they ask for options, offer two or three and
   save the one they pick.
5. If the update is rejected, fix the fields it names and save again. Mention
   any warnings it returns, such as keywords that repeat words from the name.
6. Show the saved text with each field's character count.

If the user has the project open in the AppStorePack editor, ask them to
reload it afterwards, or their open tab may overwrite the change.
