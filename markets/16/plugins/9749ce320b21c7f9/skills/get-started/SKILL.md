---
name: get-started
description: Use when the user asks what Appo can do, or wants to start turning an existing website into iOS and Android apps with Appo.
---

# Get started with Appo

Appo turns an existing, publicly reachable website into iOS and Android apps and manages their publication on the App Store and Google Play, for the apps in the signed-in user's Appo account. Appo does not create websites.

The path of an app, with the Appo tools that cover each step:

1. Create the app from the website address: create_app. On every creation the user confirms that they own or are authorized to publish the website and accepts the Terms of Service. The site's maintainer adapts it to the app (prep_mode=self_managed, tried at once), or Appo's team does (prep_mode=appo_managed, typically 24-48 hours).
2. Adjust it: set_icon, set_permissions, and customize_appearance for a specific change the user asks for. An assistant that edits the website's code reads get_adaptation_brief.
3. Try it on a phone: preview_app returns one link that opens on the phone, or shows a QR code when opened in a computer's browser.
4. Publish it: publish_app. Publishing needs an active Appo plan for the app and, for the App Store, the user's own Apple Developer Program membership.
5. Follow store review: get_app_overview reports the state and the next available step. If Apple rejects the app, get_rejection and get_fix_recipe explain why and how to fix it, and trigger_resubmission sends it back for review.
6. Send push notifications to the people who installed the app: send_push.

customize_appearance, request_testflight_build, publish_app, trigger_resubmission, send_push and remove_app change nothing without confirm: true; without it they return a preview of the effect for the user to approve.
