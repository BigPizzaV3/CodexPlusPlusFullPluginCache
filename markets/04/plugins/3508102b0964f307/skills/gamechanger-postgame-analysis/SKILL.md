---
name: gamechanger-postgame-analysis
description: >-
  Use after games when the user pastes GameChanger CSV exports, uploads or
  pastes screenshots of GC stats/box scores, or pastes boxscore text. Enhance
  analysis while they keep scoring in GC. No private GC API — CSV/export or
  screenshots only. Screenshot path is primary for many coaches without Staff
  export access.
---

# GameChanger Postgame Analysis (Buddy Model)

Jordan Heckler voice: what mattered, what to practice Tuesday, what to tell parents without drama. Original analysis frameworks only.

## Hard rules

- **GameChanger buddy model:** they keep scoring in GC; we enhance insight.
- **No invented private GameChanger API.** As of 2026 research, GC has **no documented public coach API**. Supported paths: **Staff CSV export** when available, or **screenshots / pasted images** of GC stats and box scores (primary path for many coaches without export access).
- Do not instruct users to scrape GC, steal session tokens, or use unofficial reverse-engineered clients as the product path.
- **Ask age tier** and whether this was rec / select / HS.
- No scholarship guarantees from a box score.
- **Never invent stats.** If a number is not visible or readable in the upload, say so — do not guess, fill, or “complete” the box score.

## Teaching / Canvas default

When the user wants to **show** players or staff (projector, classroom, “show the guys,” whiteboard replacement), invoke the `teach-board-visuals` pattern or **ChatGPT Canvas** (Apps SDK widget when available) **first** — diagram on the board, short chat companion — instead of long prose. One board at a time unless they ask for a mini slide pack.

## Input modes (both required)

### A) Staff / admin CSV export (when available)

- Staff accounts: GameChanger app or web.gc.com → team → **Stats** → **Export Stats** → CSV.
- Follower accounts typically **cannot** export — do not pretend they can; fall back to screenshots.
- Accept pasted CSV rows or uploaded export text.

### B) Screenshots of GC stats / box scores (primary for many coaches)

- Many volunteer coaches and parents only have Follower / limited access — **screenshots are the expected mobile path**.
- Accept ChatGPT image uploads or pasted screenshots of: team stats, game box score, batting/pitching tabs, play-by-play summary screens.
- This is the **default phone workflow**: open GC → screenshot the relevant screen → upload into ChatGPT → run this skill.

## Teaching ChatGPT how to read GC screenshots

When the user uploads or pastes an image:

1. **Ask which screen** they shared if unclear (e.g. season batting, single-game box, pitching tab, defensive summary, lineup card). Confirm before deep analysis.
2. **Read carefully** — GC UI densifies numbers; check headers, player rows, and column labels. Prefer what is clearly labeled over inference.
3. **List what you can see** — name the readable fields (e.g. AB, H, RBI, IP, BB, K, ERA if shown).
4. **List what you cannot see** — blurry digits, cropped columns, off-screen tabs, or stats not on that screen. Explicitly say “not visible in this screenshot.”
5. **Never invent** missing plate appearances, pitch counts, or batting averages. Offer to analyze another crop/tab if needed.
6. If both CSV and screenshots are provided, prefer CSV for precision and use screenshots for context the CSV lacks (e.g. inning-by-inning story).

## Preferred inputs (in order)

1. Staff CSV export (most precise when available)
2. Screenshots / pasted images of GC stats or box scores (**primary path for many coaches; default on mobile**)
3. Pasted boxscore / play summary text
4. Coach’s rough notes (“we walked 8, stranded 9”)

## Steps

1. Confirm input mode (CSV vs screenshot vs paste vs notes) and what screen/game/season it covers.
2. For screenshots: ask which screen if needed; list visible vs not-visible numbers before analyzing.
3. Summarize **game story in 5 bullets** (not a data dump) — only from confirmed numbers + coach notes.
4. Separate **signal vs noise**:
   - Signal examples: free bases, 2-strike approach, soft contact with RISP, pitch count spike, errors on routine balls
   - Noise examples: one bloop average spike, tiny sample overreaction
5. **Practice implications** (max 3): drills or segments for next practice.
6. **Player touches**: who needs encouragement vs a technical cue (respectful, private-toned).
7. **Pitching / catching notes** if data exists; else ask for pitch counts from coach notes or another screenshot.
8. **Parent-safe summary** (optional short paragraph): factual, calm, no blame.
9. Offer one **question** for the next pregame meeting.

## Output template

```markdown
## Inputs used (CSV / screenshot / paste / notes)
## Screenshot literacy (if image): screen type · visible stats · not visible
## Game story (5 bullets)
## Signal vs noise
## Next practice (3 priorities)
## Individual touches (coach eyes only)
## Parent-safe blurb
## Pregame question for next time
```

## How to get data (coach reminder)

- **Staff:** GameChanger app or web.gc.com → team → **Stats** → **Export Stats** → CSV.
- **No export access / on phone:** open the game or season stats screen in GC → screenshot the tabs you care about → upload into ChatGPT. Prefer one clear crop per screen (batting, pitching, box) over a single tiny full-page shot.
- Follower accounts: use screenshots; ask a Staff coach only if you specifically need CSV.

## Explicit non-goals

- Replacing GC scoring UX
- Live scrape / unofficial token bots
- Claiming access to a private GC API that does not exist for coaches
- Inventing stats from incomplete or blurry screenshots
