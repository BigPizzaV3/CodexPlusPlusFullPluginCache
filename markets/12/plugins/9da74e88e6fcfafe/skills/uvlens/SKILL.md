---
name: uvlens
description: Answer UV index, sunburn and sun protection questions with UVLens forecasts. Use when the user asks about UV now or on a day, when to go outside with less UV, how long until they burn, or UV during planned outdoor activities, and for scheduled briefings that mention outdoor plans.
---

# UVLens

UVLens provides NOAA UV index forecasts for any place, lower-UV time windows and burn-time estimates. Forecast values include forecast cloud cover. They do not include rain, heat or other hazards.

## Get the place first

- Use a place the user named or one they gave earlier in the conversation. Do not guess a location, and do not use device location.
- Resolve the name with `search_places`, then pass the returned coordinates and label to the other tools. Reuse them for follow-up questions.
- If several results could match, such as two places with the same name, ask the user which one they mean. State which place you used in the answer.

## Choose the tool

| User need                                                         | Tool                                                                                                                            |
| ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| UV now, or how UV changes on a day                                | `get_uv_forecast`                                                                                                               |
| When to go out with less UV, or morning versus afternoon          | `find_lower_uv_windows` with the activity length and the hours available                                                        |
| UV and burn time for a planned activity, such as a calendar event | `find_lower_uv_windows` with `earliest` and `latest` set to the event's start and end, and `duration_minutes` set to its length |

To compare morning and afternoon, call `find_lower_uv_windows` twice with the same duration: once with `latest` set to 12:00 and once with `earliest` set to 12:00.

Pass dates in the place's local time. For "tomorrow", use the day after today at the place. Keep the place and date the user chose for follow-up questions, unless they change them.

## Burn time

- Burn time needs a Fitzpatrick skin type from 1 to 6. Pass `skin_type` only when the user has given it in this conversation or you already know it.
- If the user asks about burning and has not given a skin type, give the UV information and ask for their skin type. Do not assume one, and do not call a tool with several skin types to cover the possibilities.
- UVLens does not determine skin type. If the user is unsure of theirs, say burn time needs it and give the UV information without burn times.
- Present burn time as an estimate for unprotected skin. It is not a safe exposure time. It does not account for sunscreen, shade, reflection or photosensitivity.
- When the burn-time status is `coverage_limited`, say the forecast does not cover the full period. Do not say the user will not burn.

## Use only returned values

- Quote UV values, times and burn times only from tool results.
- If the forecast does not cover the date, say so and give the dates it covers. Do not estimate UV from general knowledge or the season.
- If the forecast is stale or unavailable, say so and do not give values.
- Do not provide tanning schedules or guarantee burn-free exposure.

## Sun protection advice

- UV 3 or higher is when sun protection is recommended: sunscreen, a hat, sunglasses, protective clothing and shade.
- For when to reapply sunscreen, refer the user to the product label. Do not give a reapplication schedule.
- When the user asks about UV, answer it whatever the level. Only suggest a lower-UV time without being asked when UV reaches 3 during the activity.

## Scheduled and background use

These rules apply when the assistant checks UV without the user asking.

- For a daily briefing, call `get_uv_forecast` for the user's place. Mention UV only when the peak is 3 or higher.
- For calendar events that are likely outdoors, check each event with `find_lower_uv_windows`. Events entirely between sunset and sunrise have no UV and need no check. For an event that crosses midnight, check the part before midnight with `latest` set to 23:59, and the part after on the next date with `earliest` set to 00:00. Check an event longer than 12 hours in parts of up to 12 hours. Recommend protection or a lower-UV time only when UV is 3 or higher during the event, or the event is longer than the burn time.
- Do not notify when UV stays low or nothing has changed. Keep the tone factual.
- Check again after the forecast's `next_update_at`, not on every run.
- UVLens does not send reminders. If the user wants one, use the assistant's own reminder features.
