---
name: set-up-autorouter
description: Set up AutoRouter after the plugin is installed, or when someone asks to install, set up, or get started with AutoRouter. Checks for a Mac, installs the AutoRouter Mac app, and opens it so its onboarding can connect Codex.
---

# Set up AutoRouter

AutoRouter picks the model for each Codex and Claude Code turn, using the
person's ChatGPT or Claude plan first and AutoRouter credits otherwise. It
runs through a Mac app. This skill installs that app and opens it; the app's
own onboarding signs the person in and connects Codex. Your part ends once
the app is open.

The script is `../../scripts/autorouter-app.mjs`, relative to this file. Run
it with `node`. It prints progress on stderr and one JSON object last.

1. In one sentence, say what AutoRouter does and that you'll install its Mac
   app.
2. Run `status`.
   - If `supported` is false, say politely that AutoRouter only runs on
     macOS for now, and stop. Don't attempt an install.
   - If `routing` is true, AutoRouter already routes this Codex: say so and
     stop.
   - If you can't run commands here, give the download link
     `[Download AutoRouter](https://autorouter.com/AutoRouter.dmg)` and say
     to open it and drag AutoRouter into Applications. Then stop.
3. Run `install`. It downloads the signed disk image from autorouter.com,
   checks its signature, copies the app into `/Applications`, and opens it.
   It needs network access and write access to `/Applications`; if the
   sandbox blocks either, request those permissions and run it again. Don't
   ask to run outside the sandbox.
4. Finish with one short message, based on the result:
   - `opened` is true: AutoRouter's window is open. Tell them to follow it
     to sign in and turn on Codex.
   - `action` is `open-link`: the app is installed but the sandbox couldn't
     open it. Show `[Open AutoRouter](<link>)` and say that clicking it
     opens AutoRouter, where they sign in and turn on Codex.
     In both cases, add that new Codex chats use AutoRouter once that's done,
     and that in a new chat they can ask you to add, change or remove
     routing rules, such as "Use the strongest model for architecture work".
     They can also ask which models AutoRouter offers, or which one fits a
     task, at any time.

The AutoRouter window is the person's to work through. Never click, type or
sign in for them, even if a computer-use tool is available. Don't wait for
the onboarding to finish or check on it afterwards. Don't quote prices or
plans, and don't read or edit the Codex config.
