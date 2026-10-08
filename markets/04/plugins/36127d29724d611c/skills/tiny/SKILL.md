---
name: tiny
description: >-
  Build and deploy apps to Tiniest Cloud, which gives every app sign-in, per-user storage,
  realtime, push notifications, scheduled jobs and an LLM with no keys and no backend. Use when
  building or changing an app hosted on Tiniest Cloud, or when you see tiny.db, tiny.ai, or
  tiny.rules.json.
---

# Building for Tiniest Cloud

Tiniest Cloud hosts static frontends. Each one gets sign-in, per-user storage, realtime rooms,
push notifications, scheduled jobs and a language model, with no keys anywhere and no backend
to write.

## Call `tiny_guide` first

**Before writing or changing any app that will be deployed here, call the `tiny_guide` tool.**
It returns the current SDK reference: every call, its exact signature, the limits, and the
patterns that matter. This file deliberately does not repeat it. The platform gains features,
and a copy pasted into a plugin listing would keep teaching an old API long after the real one
moved on, producing apps that deploy cleanly and then fail in the browser.

So: `tiny_guide`, then build, then `deploy`.

## What never changes

These four hold regardless of which version of the SDK is current, and they are the ones an
agent gets wrong when it treats this like ordinary static hosting:

- **Build a plain static site.** HTML, CSS and JavaScript. No build step is required and no
  server code runs. Include `index.html` at the top level.
- **Do not write a login flow.** Sign-in belongs to the platform. The SDK tells you who the
  visitor is; there are no passwords, sessions or tokens for the app to handle.
- **Do not use `localStorage` for anything that matters.** It is per-browser and per-device,
  so the same person loses their data on their phone. Storage in the SDK follows the account.
- **Do not add a backend or call your own API.** There is no origin to call. Anything that
  needs a secret goes through a connection the app's owner declares, so the key never reaches
  the page.

## Deploying

The server cannot read your disk. Read the files yourself and pass their contents to `deploy`.
Every deploy is a new immutable version, and earlier versions stay restorable with `rollback`.

If a deploy reports that an app uses `localStorage` or calls its own backend, `modernize_app`
converts it to the platform's own storage and sign-in.
