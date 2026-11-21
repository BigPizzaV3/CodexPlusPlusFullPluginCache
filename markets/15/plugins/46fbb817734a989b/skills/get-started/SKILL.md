---
name: get-started
description: Explains what GenerApp does and helps the user create their first shared web app with the GenerApp tools.
---

GenerApp hosts small web apps that the user can share by link with friends, family or flatmates. The data of each app syncs in real time between everyone who has the link, and the people who use an app need no account.

1. Briefly tell the user what GenerApp can make, for example a shared shopping list, a chore rota, a holiday budget or a small group game, and ask what they would like to create.
2. When the user has described their app, read the GenerApp guide with get_sdk_docs, then create the app with create_app.
3. Write app.json, index.html and icon.svg with write_file, check the app with validate_app and fix any reported error.
4. Publish it with deploy_app and give the user the public link, explaining that anyone with the link can open it in a phone browser and add it to their home screen.

If the user prefers to start from an existing app, use browse_library to show matching apps from the GenerApp library and copy_from_library to copy the one they choose.
