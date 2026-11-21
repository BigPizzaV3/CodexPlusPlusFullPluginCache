---
name: helptester
description: Test the user's hardware (keyboard, mouse, gamepad, microphone, MIDI, touchscreen, speakers), check their network (public IP, ISP, latency, internet speed) or use HelpTester developer tools (JSON formatter, Base64, QR code generator, DNS checker, AI Unicode remover) directly in the chat. Use when the user wants to check whether a device works or asks for one of these utilities.
---

# HelpTester

HelpTester (https://helptester.com) provides browser-based hardware tests and
developer tools. All tests run client-side with standard browser APIs. No AI is used
for the tests, nothing is recorded or uploaded unless the user saves a result.

## Which tool to call

Interactive widgets (render inside ChatGPT):

| User intent | Tool | Notes |
|---|---|---|
| Keys not working, ghosting, keyboard check | `keyboard_test` | The widget switches to fullscreen; user presses keys. Some ChatGPT shortcuts (Tab, Esc) may be intercepted. |
| Mouse polling rate / Hz, mouse lag | `mouse_test` | User moves the mouse over the test area for 5 seconds. |
| Controller / gamepad buttons, sticks, vibration | `gamepad_test` | User must press a button on the controller first. Experimental inside ChatGPT; if nothing is detected, give the website link. |
| Microphone check, "can you hear me", mic level | `mic_test` | Browser asks for microphone permission. |
| MIDI keyboard / controller not recognised | `midi_test` | Chrome/Edge only; Safari has no Web MIDI. |
| Touchscreen dead zones, multitouch, latency | `touchscreen_test` | Best on phone/tablet; the widget opens fullscreen. |
| Speaker left/right, no sound, frequency test | `speaker_test` | User must click to start sound (autoplay policy). |
| Format / validate / minify JSON | `json_formatter` | Pass the JSON in `json` to pre-fill. |
| Base64 encode or decode | `base64_tool` | Pass `text` and `mode` (`encode`/`decode`). |
| QR code for a URL, text, Wi-Fi, contact | `qr_generator` | Pass `text` to pre-fill; the code renders immediately. |
| DNS records, MX, nameservers, SPF of a domain | `dns_checker` | Pass `domain`. Lookup runs in the browser via DNS-over-HTTPS. |
| "What is my IP", ISP, location, is my connection working, latency | `ip_test` | Runs from the user's browser, so it shows the user's own IP, not the server's. Has ping, DNS-resolution and connectivity checks. |
| Internet speed, download/upload, ping, jitter | `speed_test` | User clicks start; transfers up to ~25 MB. Suggest closing other downloads first. |
| Remove hidden/invisible Unicode from AI text | `unicode_remover` | Pass `text`. |

Tools that open on helptester.com (call `open_helptester_tool` with the `tool` id and
give the user the returned link):

| User intent | `tool` value |
|---|---|
| Webcam / camera test | `webcam_test` (ChatGPT does not grant camera access to apps) |
| Dead or stuck pixels | `deadpixel_test` (needs true fullscreen) |
| CPU / GPU stress test, thermal throttling | `stress_test` |
| Favicon check / favicon generation | `favicon_checker`, `favicon_generator` |
| Which analytics / ad tags does a site use | `tag_checker` |
| Musical key / BPM of a song file | `key_finder` |

`list_helptester_tools` returns the full catalogue if the user asks what HelpTester can do.

## How to respond

- Call the tool first, then explain in one or two sentences what the user should do
  in the widget (press keys, allow the microphone, move the mouse, etc.).
- When a permission is needed, say so before or while the widget appears.
- If a test is not possible in ChatGPT (webcam, dead pixel, stress test, tag checker, favicon tools),
  do not try to simulate it. Use `open_helptester_tool` and give the link.
- Do not claim to diagnose hardware faults yourself. Help the user interpret what the
  widget shows (e.g. a key that never lights up is likely defective; try another port
  or Bluetooth re-pairing for controllers).
- These tools do not write poems, fix drivers, or upload recordings. Decline such
  requests politely and offer the matching test instead.
