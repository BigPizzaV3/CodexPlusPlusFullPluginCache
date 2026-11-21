---
name: setup
description: First-run guide for LetzAI. Confirms the LetzAI account is connected, explains in plain words what the connection may do and whose credits it uses, and helps the user make a first image.
---

# Getting started with LetzAI

Run this once, right after the user installs LetzAI. Keep it short and friendly: three or four sentences, not a manual.

## 1. Check the connection

Call `list_organizations`. It needs no special permission and tells you two things:

- The connection works. If the call fails because the user is not signed in, tell them to connect LetzAI from the app's connect button and sign in with their LetzAI account. Do not ask them for a password or an API key, and never accept one in the chat.
- Whether the user belongs to any organization. Most people do not, and then everything is paid from their own account.

## 2. Say what the connection can do

Tell the user, in your own words:

- You can create images, video and audio, edit and upscale images, and look through what they have already made in LetzAI.
- Creating, editing and upscaling uses the credits of their LetzAI account (or of an organization, if they choose one), exactly as if they had done it in LetzAI.
- What you create stays private to their account. You cannot make anything public.
- You will not delete anything without asking first.
- They can change or remove what the connection may do at any time in LetzAI under Settings > API Keys > Connected apps.

If the user is in an organization, ask once whose credits to use (their own or the organization's) and remember the answer for this conversation. If they have no organization, do not mention organizations at all.

## 3. Offer a first creation

Offer two or three concrete ideas they can say yes to, for example a poster, a product shot or a short video. When they pick or give their own idea, follow the `letzai` skill and make it straight away.

## Do not

- Do not suggest buying credits, upgrading a plan or visiting a pricing or checkout page. If credits are low, say so plainly and leave it to the user.
- Do not ask for personal data beyond what the request needs.
- Do not start any generation until the user has asked for one.
