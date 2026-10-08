---
name: link-doctor
description: Use when someone asks why a media URL fails, redirects, opens a webpage, or cannot be used in code.
---

# Link Doctor

## Purpose

Explain a URL problem from safe diagnostic facts returned by Media2URL. Focus on status, redirects, response type, disposition, expiry, and whether the response is directly embeddable.

## Trigger examples

- “Why does this image URL open a webpage?”
- “Is this a direct link?”
- “Why won’t this image work in my API?”
- “Can I use this URL in an `img` tag?”

## Do not trigger

- The user has not supplied a URL or asked for a diagnosis.
- The request requires downloading or copying a third-party asset rather than inspecting it.
- The user asks to bypass a login, paywall, robots rule, access restriction, or expiry.

## Allowed Media2URL App actions

- Use `diagnose_url` for safe HTTP status, redirect, content type, content disposition, reachability, and wrapper facts.
- Use `get_asset_links` when the user asks for confirmed Media2URL direct/share alternatives.
- Use an import action only after the user explicitly requests it and the App confirms rights and safety checks.

## Result interpretation

Explain only returned facts. A `text/html` response may be a share/viewer page rather than a direct image response; a redirect chain may change the final content type; an expired or access-protected result may not be usable by the requesting consumer. Never guess network results, and do not execute remote HTML or JavaScript.

## Missing authorization

Basic zero-storage diagnosis may be available without account connection if the App permits it. Account connection is required before importing, copying, or changing any hosted content. Do not pretend a diagnostic result authorizes an import.

## Plan or quota restriction

For write-capable follow-up actions, Free accounts are capped at 90 uploads per month, roughly 3 per day. Explain the App’s actual diagnostic limit or `UPGRADE_REQUIRED` result. A paid plan can unlock larger quotas and extended diagnostics. Do not claim that an extended scan, body fetch, or import occurred when the App denied it.

## Partial failure

For several URLs, report each result separately and identify timeouts, blocked destinations, redirects that could not be safely followed, and unsupported responses. Do not label the batch healthy because one URL worked.

## Privacy and destructive actions

Do not expose private response data or use diagnostics to discover internal services. A pasted URL does not prove ownership, and diagnosis never authorizes deletion or modification.

## Natural-language examples

“The diagnostic response is HTML after a redirect, so it is not a direct image response for your API. I can give you a confirmed Media2URL direct URL only if the asset is authorized and available there.”
