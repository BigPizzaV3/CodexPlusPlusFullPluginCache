---
name: ga4-connect
description: Connect, reconnect, or add Google Analytics 4 (GA4) properties to Windsor.ai and resolve which connected property a request means. Use when the user wants to connect a property, asks what is connected, or hits a permission error. Do not use for analysis or exports.
---

# Connect GA4 properties

Help the user connect, reconnect, or add a Google Analytics 4 property to Windsor.ai (connector id `googleanalytics4`), and resolve which connected property a request refers to.

## Stay in scope
- Use this skill when the user wants to connect a property, add another one, reconnect after a permission error, or asks which properties are connected.
- For analysis use $ga4-insights; for recurring exports use $ga4-export.

## Workflow
1. Call get_connectors with include_not_yet_connected=True to see whether `googleanalytics4` has connected properties.
2. For a connection, call get_connector_authorization_url for a ready-to-open setup link (Google sign-in), or get_connector_connect_info for the auth details. Hand the user the link and tell them to authorize with the Google account that has access to the property.
3. Never ask the user to paste tokens or passwords into the chat, and never describe manual dashboard navigation instead of giving the link.
4. After they finish, call get_connectors again and confirm the new property by name.

## Property resolution
- If a request names a property or site, match it to a connected account id. If several properties could match, ask which one before any read.
- A permission error on a read usually means the Google account lacks access to that property; reconnect through the same setup link with the right account.

## Support
- get_windsor_login_url gives an auto-login link into the Windsor.ai dashboard; get_current_user shows who is signed in; contact_windsor files a support or feature request. Never discuss plans or pricing.

## Answer with evidence
State which properties are connected, which are not, and the exact next step with its link.
