# Assign and conflicts

`optisigns_screen_assign_content(deviceIds[], contentId, contentType, assetName?, screenName?,
existingContent?, appendDurationSeconds?)` sets what screens show **now**.

- `contentType`: `asset` (default), `playlist`, `schedule`, `web`.
- Several screens: pass every id in one `deviceIds` call.
- The confirmation summary names the screen and content as OptiSigns has them; `assetName` and `screenName` are display hints only.
- There is no future time. For a later go-live, assign a schedule
  ([scheduling-rrule.md](scheduling-rrule.md)).
- Only assign ready content ([publish.md](publish.md)).

## Step 1: the confirmation request

The first call returns, instead of acting:

```
OPTISIGNS_CONFIRM_REQUIRED <summary> (team: <team>)
```

Where the tool shows an approval card instead, the user approves there: skip this step.

Nothing has been written. Ask the user in plain words, using the summary, e.g. "This will put 'Fall Menu'
on Lobby TV and Patio TV right away, in the Austin team. Go ahead?" Only after a clear yes, call again
with the **same arguments plus `confirmed: true`**. Never say it is live until that call succeeds.

## Step 2: a playlist is already playing

The (confirmed) call can return a normal result, not an error:

```
OPTISIGNS_SCREEN_CONFLICT 2 of 3 screen(s) are already playing a playlist.
- "Lobby TV" is playing playlist "Welcome Loop"
- "Patio TV" is playing playlist "Welcome Loop"
The other 1 screen(s) are not on a playlist and will simply receive Fall Menu.
Nothing has been written to OptiSigns. Ask the user which they want, then call this tool again with the SAME arguments plus ONE of:
  existingContent: "replace"  — ...
  existingContent: "append"   — ...
```

If OptiSigns didn't say which screens, the first line reads `OPTISIGNS_SCREEN_CONFLICT At least one of
N screen(s) is already playing a playlist (OptiSigns did not say which).`

How to respond:

1. Relay it in plain words, naming the screens and playlists: "Lobby TV and Patio TV are playing
   'Welcome Loop'. Should Fall Menu **replace** it there, or be **added to the end** of 'Welcome Loop'?"
2. Wait for the user's choice. Never pick for them.
3. Re-call with the same arguments plus one of:
   - `existingContent: "replace"`: the content takes over; the playlist stops playing on those screens
     (it is not deleted).
   - `existingContent: "append"`: the asset joins the end of that playlist, for
     `appendDurationSeconds` (4–86400, default 10). **Assets only**; not offered for a playlist or
     schedule. Note that append changes the playlist itself, so every screen and schedule using it gets
     the new item.
4. The re-call passes the confirmation gate again: expect `OPTISIGNS_CONFIRM_REQUIRED` once more, ask,
   then add `confirmed: true`.

Never:

- create a new playlist (with the old items plus the new one) and assign that,
- switch `contentType` to dodge the conflict,
- retry without `existingContent`.

An asset or schedule already on a screen is simply replaced; only a playing playlist needs this choice.

## Cancel scheduled or temporary content

`optisigns_screen_cancel_scheduled(screenId)` (confirm) cancels a scheduled go-live and any temporary
content on a screen, e.g. one set from the portal. Use it when the user says "stop the takeover" or "cancel
what's scheduled to go live".

## After assigning

Report per screen: what it shows now, and the team. If some screens failed or were skipped, name them.
Offer `optisigns_screen_diagnose` for any screen that is offline: it gets the content when it reconnects.
