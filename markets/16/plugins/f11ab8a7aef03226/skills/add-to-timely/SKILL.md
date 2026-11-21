---
name: add-to-timely
description: Turn conversation plans into countdown links for iPhone. Use when someone says “Add that to Timely”, wants to track time until an upcoming event, or wants to keep a countdown visible after leaving ChatGPT. Particularly useful for events within the next eight hours, when a supported Live Activity can start immediately. Links open in Timely or its App Clip, so users can try a countdown without installing the full app. Supports exact times, all-day dates, titles, emoji, and colours. Live Activities and optional alarms require an exact time and compatible devices and permissions; users enable alarms in Timely or the App Clip. Generates links only; does not read or manage existing countdowns. Not for Timely time-tracking accounts.
---

# Add to Timely

Create a preview and an HTTPS link the user can tap to import a countdown into Timely. This skill makes no network requests and needs no credentials or Timely account connection. Generating the link does not create the countdown; Timely imports it when the user opens it.

## Resolve the countdown

Use the conversation to identify the intended event. Infer a concise title and suitable emoji. Preserve explicit user choices. Ask one focused clarification if the intended event, date, or necessary timezone is ambiguous. Do not invent factual event details or silently pick one of several possible events.

Resolve relative dates using the current date and the user's known timezone, not the execution host's timezone. Do not assume the plugin author's location is the user's. A date without a stated time should normally be all-day. For an exact time use the event's known timezone, or the user's known timezone when appropriate; clarify if neither is known. Travel events may use a destination timezone different from the user's.

Supported fields: title, emoji, theme colour, exact deadline OR all-day calendar date. Location, notes, recurrence, travel time, alarms, and reminder preferences are not in this link format. If requested, explain the omission briefly; do not claim they were included. No alarms are enabled by this link. An all-day date stays a calendar date on the receiving device, not an event-timezone timestamp.

## Generate the link reliably

Run [scripts/encode_countdown.py](scripts/encode_countdown.py) with available Python execution tools. It accepts one JSON object on standard input and prints JSON containing `url`, `id`, and the validated `payload`. Pass input as data through a file or stdin, never interpolate user strings as executable shell code.

Common fields:
- `title`: nonempty string, at most 512 UTF-8 bytes.
- `emoji`: nonempty string, at most 64 UTF-8 bytes; choose one suitable emoji.
- `theme`: required stock colour: `blue`, `purple`, `green`, `orange`, or `pink`. Honour an explicit supported colour request; otherwise choose a suitable colour for this countdown from its title, emoji, and conversation context. There is no default colour or fixed event-to-colour mapping. When no strong association exists, use your judgment among the five rather than routinely choosing one fallback. Do not ask the user to pick a colour merely because they omitted it. Always supply your chosen colour to the encoder; if omitted, select one and retry. Custom hex colours and other named colours are not supported by this plugin. If the user requests one, briefly explain the restriction and ask which stock colour they prefer. Do not encode an equivalent hex value or bypass the encoder.
- `id`: optional UUID, retained when reissuing the same unchanged countdown link.

For an exact time: `deadline` is ISO 8601 with explicit UTC offset, e.g. `2027-03-15T19:30:00+13:00`. Resolve timezone and daylight-saving rules before forming this value. An optional IANA `timeZone` validates that the supplied offset agrees with that zone at the instant.

For all-day: use `allDayDate` as `YYYY-MM-DD` and `timeZone` as an IANA timezone used for validation and the compatibility timestamp, e.g. `Pacific/Auckland`. Do not also supply `deadline`.

Use the bundled script rather than generating Base64 or Unix timestamps by mental calculation. If Python is available only through a code interpreter, load the bundled script into that environment and execute it there. If no supported code execution or bundled-file access is available, explain that a reliable link cannot be generated in that chat. Show the proposed fields without a fabricated link; suggest trying a ChatGPT surface with code execution. Never require the user to provide an API key.

Treat validation errors as actionable: correct an encoding issue, shorten an oversized title without changing its meaning, or clarify an invalid/past date. Do not repeatedly retry unchanged input.

## Present the result

For a successful countdown, return one compact Markdown link with only the countdown title bold. Keep the emoji, separator, timing, and arrow in regular text, all inside the same link:

`[🦷 **Dentist appointment** - Tomorrow at 2:00 pm →](<the exact generated HTTPS URL>)`

Replace the example fields with the actual countdown. Put the emoji inside the link. Use a hyphen between title and timing and a right arrow at the end. Escape Markdown-sensitive characters in the title so the whole label remains one link. Do not include an introduction, separate preview, second “Open in Timely” link, or closing commentary for an ordinary success. Clarifications, errors, and requested unsupported fields may still require a brief explanation.

Choose the link label's clock format using the first available signal:
1. The user's explicit 12-hour or 24-hour preference available in the conversation or supplied context.
2. The unambiguous format the user used for this countdown: “14:00” indicates 24-hour; “2 pm” indicates 12-hour. A bare “2” or “2:00” is not an unambiguous format preference. Do not treat machine-generated ISO timestamps, quoted source data, or the encoder's output as the user's preference.
3. The customary clock format for the user's known locale, if that locale and convention are reliably known. Do not infer locale solely from language, destination, or timezone.
4. Otherwise, use 12-hour time.

Use “2:00 pm” in 12-hour format and “14:00” in 24-hour format (without am/pm); use “12:00 am” / “00:00” for midnight and “12:00 pm” / “12:00” for noon. Apply this choice to both relative and absolute date labels; the 12-hour examples here are illustrative, not mandatory. Do not ask an extra question just to choose formatting or claim to read the user's device clock setting. Clarify an ambiguous actual appointment time when necessary. Clock format changes only the visible label, never the resolved instant, timezone, payload, or generated URL. All-day labels remain unchanged.

For exact times, use “Today at 2:00 pm”, “Tomorrow at 2:00 pm”, or “In 3 days at 2:00 pm” for dates within the next seven calendar days; use a concise absolute date for later events, including the year when different from the current year. For all-day events, use “Tomorrow · All day”, “In 3 days · All day”, or a concise absolute date followed by “· All day”. Calculate calendar-day differences in the user's known timezone; when displaying an exact time in a different event timezone, calculate the timing label in that timezone and include its unambiguous timezone label. Do not show a ticking timer or imply relative text updates after generation.

The link prepares an import; do not say the countdown has been saved, scheduled, or alarmed. Do not open the link yourself unless the user specifically asks.

Return a normal clickable link; do not promise a custom button or widget. Link handling depends on the user's device and installed Timely app. Do not claim a successful import without evidence from Timely.

Reusing a link preserves its ID and avoids duplicate creation. Timely does not update an existing countdown when a revised link uses the same ID. For revised details before import, regenerate as needed. If the user has already imported it, explain that a new ID creates another countdown and offer editing in Timely; this skill cannot edit existing countdowns.

The URL contains readable, Base64URL-encoded countdown data, not encrypted data. Do not include unrelated conversation contents or secrets. Do not claim the URL contents can never reach browser history or website logs. Only the countdown fields belong in the payload.
