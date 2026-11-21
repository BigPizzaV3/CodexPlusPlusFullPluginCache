---
name: account-and-access
description: Explain MockMentor and its supported exams, show the approved connected profile, validate onboarding and feature access, and handle referral progress, unlocks, and personal referral links.
---

# Account and access

Use this skill for general MockMentor product questions and for any action that depends on the signed-in student's onboarding, exam context, feature access, or referral state.

## Product overview

For “What is MockMentor?”, supported-exam, pricing, creator, or general capability questions, read [references/product-overview.md](references/product-overview.md) and answer without running account or referral tools. Do not imply that every described or planned capability is currently operational. Use [templates/overview-responses.md](templates/overview-responses.md) when a standard response shape is useful.

When availability for this student matters, perform the account check below and use only fresh server-returned feature state. Never guarantee scores, ranks, admissions, exam results, or alignment with the latest official syllabus.

## Internal account check

At the start of each new user-requested MockMentor workflow, silently call `who_am_i` once and wait for it to succeed. This includes referral workflows. Reuse that routing context for subsequent calls and pagination within the same workflow; the server independently enforces fresh access on every tool call. Do not announce the check or ask permission for it.

Exceptions are `who_am_i` itself, OAuth setup, and protocol or skill discovery. Never recurse or run the initial dependent call in parallel with preflight. Refresh preflight for a new user request, after reconnecting or changing account/exam, or when a tool reports changed access or onboarding.

`who_am_i` is both the approved connected-profile tool and an internal routing and authorization preflight. Call it when a student asks “who am I?”, “show my profile”, “what is my email?”, or which MockMentor account is connected. For those explicit identity requests, return only the name and email fields that are present. Never expose a user/account ID, raw profile, full feature payload, or other internal fields. For silent preflight calls, do not volunteer or use name or email as conversational personalization.

Read [references/account-context.md](references/account-context.md) whenever onboarding, access, identity, or failure handling affects the request.

## Onboarding gate

After preflight, inspect `onboardingComplete` before taking any dependent action.

- When `false`, stop. Do not call the requested study or referral tool. Tell the student to complete signup at [mockmentor.ai](https://mockmentor.ai), then retry.
- When `true`, use the returned exam and feature state only to route the request. Do not volunteer the underlying profile.

## Feature routing

- A feature is usable only when its key appears in `accessibleFeatureKeys`.
- If a requested feature key is absent, do not call its study tool. Call `get_referral_status` to determine whether it requires referrals, is disabled, or has not launched, then explain only the relevant status. Never suggest that referrals can enable a feature whose `lockReason` is `disabled`.
- Take a Mock requires zero referrals. Never gate it behind a referral.
- Use only live status and thresholds returned by the server. Never infer access from a link, a token, or the student's claimed count.

## Referral workflows

- Referral progress: `who_am_i` → `get_referral_status`.
- Personal link or invite request: `who_am_i` → `get_or_create_referral_link`.
- Locked feature: `who_am_i` → `get_referral_status` → `get_or_create_referral_link`. Use the latest tool-returned access state and stop the detour if access changes.

For a progress-only request, do not create a link. For a locked feature, provide the server-created link without waiting for a second request. A link lookup may create one durable record, but it does not send an invitation or qualify a referral.

Report only the student's aggregate qualified and pending counts, the relevant remaining qualified referrals, and the exact server-provided link when needed. Never reveal another student's identity or activity, promise qualification, or construct, shorten, or alter a referral URL.

Use [templates/referral-responses.md](templates/referral-responses.md) for concise response shapes. Substitute only live values and omit fields that are not returned.

## Authentication and failures

Let the host run OAuth. Never request a password, authorization code, bearer token, session cookie, Google credential, user ID, or referral code in chat.

If preflight fails, stop dependent calls and offer one retry or reconnection. If a later tool fails, report that failure without inventing profile, access, counts, or links. Avoid retry loops.
