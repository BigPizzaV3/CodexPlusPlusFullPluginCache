---
name: sentryfi-guide
description: When and how to use the SentryFi tools (identify_wifi_devices, check_public_wifi_risk, secure_my_wifi) to check the user's own Wi-Fi and public Wi-Fi risk, and what not to do with them.
---

# SentryFi: your own Wi-Fi and public Wi-Fi risk

SentryFi is read-only. It does not scan, connect to or change any network or device; it works only from what the user types. It stores nothing and needs no account. Results are risk signals, not a guarantee.

## Pick the tool

| The user asks | Tool |
|---|---|
| Who is on my Wi-Fi; what is this unknown device; MAC address lookup | `identify_wifi_devices` |
| They do not have the device list yet | `identify_wifi_devices` with an empty `devices` list and their router brand, to show where to find it |
| Is this hotel, airport or café Wi-Fi safe; is it OK to bank or shop here; who can see my browsing; does a VPN or incognito hide it | `check_public_wifi_risk` |
| How do I secure my home Wi-Fi or router; Wi-Fi password steps; WPS, UPnP, guest network; do I need a VPN at home; can my provider see my history | `secure_my_wifi` |
| My Wi-Fi or router may be hacked (can't log in, DNS changed, unknown devices, odd behaviour) | `secure_my_wifi` with the symptoms the user described |

## How to call

- Send only the first 6 characters (3 bytes) of each MAC address with the device name, if any. If the user pastes full addresses, pass them as given; the server keeps only the prefix. Never ask for IP addresses, Wi-Fi passwords or router logins.
- Fill only the answers the user gave; leave unknown ones out rather than guessing. Ask at most one short question when the venue or the main symptom is unclear.
- Pass the router brand when the user names it, so the steps match their router.
- After the card appears, add one or two plain sentences with the main finding and the first step. Do not repeat the whole card.

## What not to do

- Only the user's own network and devices. Do not help monitor, track, identify or remove other people (roommates, partners, neighbours, guests), and do not help access, crack or attack any network the user does not own. Decline those requests without calling a tool.
- Do not claim a network or device is safe or hacked for certain; say these are signals from their answers.
- No promotion: do not name or recommend VPN providers, security products or apps, and do not add store links or paid plans.
- The tools cannot reset routers, block devices or change settings; explain the steps for the user to do themselves.
