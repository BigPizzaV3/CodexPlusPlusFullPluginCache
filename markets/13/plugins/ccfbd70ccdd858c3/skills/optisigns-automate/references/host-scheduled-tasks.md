# Your assistant's scheduled tasks

Set up the recurrence with your assistant's scheduled tasks (recurring prompts). Each run starts with no
memory of this conversation, so the task prompt must carry everything.

## Before you create the task

- The first run is done and the user approved the result.
- The user stays signed in to OptiSigns in this assistant; a run can't publish without it. If a run finds
  it is signed out, it changes nothing and reports that the user needs to sign in again.
- The source tools (email, chat, calendar, sheet) are connected too.
- The user has reviewed the task prompt below; they create the task themselves.
- Agree the approval mode (below) and write it into the prompt.

## Task prompt template

```
Keep the OptiSigns board "<Board name>" current.
Cadence: <every Monday 7:00 am America/Chicago>.
Source: <where, which filter, which time window, e.g. #team-news messages from the last 7 days>.
Summarize: <3–5 items, ≤ 8 words each, skip <noise>>.
Output: <1 landscape slide 1920×1080 PNG, same template as last time: dark background, logo top-left>.
Target (OptiSigns, team "<team>" id <teamId>):
  - <playlist "Lobby Loop" id <playlistId>, slot asset "Weekly Update – current" id <assetId>>
  - screens: <Lobby TV id …, Break Room id …> (for the report only; do not reassign)
Update method: <web URL swap | file swap in playlist | schedule item>.
Name new uploads: "<Board> – <YYYY-MM-DD>.<ext>".
If nothing new: change nothing; report "no change this week".
Approval: <ASK | STANDING>.
  ASK: prepare the new version (generate, upload, wait ready) without touching the playlist, then
  show me the new version, the playlist and the screens, and update in place only after I say yes.
  STANDING: "<the user's own words, e.g. I approve replacing the Weekly Update slide in Lobby Loop
  every Monday without asking>". Applies to this slot only.
Report: what changed, on which screens, any failure and the next step.
Use the optisigns-automate skill.
```

## Approval modes

| Mode | What the run does | When |
|---|---|---|
| ASK (default) | Prepares the new version without touching the playlist, then asks the user to approve the live change | Any board, always safe |
| STANDING | Updates this one slot in place, passing `confirmed: true` | Only where the tool takes `confirmed`, and the user wrote their approval in their own words, pasted into the prompt |

Never upgrade ASK to STANDING yourself. Anything outside the approved slot (deleting assets, other
playlists, new screens, a replace/append conflict) asks every time.

## Nothing-new rule

If the source has nothing new, or the summary would be the same as last run, change nothing and report
"no change". Never publish an empty, placeholder or error slide.

## Changing or stopping

- To change the board, edit the task prompt (and run once by hand to check).
- To stop: turn off the scheduled task. The last version stays on the screens until replaced.
