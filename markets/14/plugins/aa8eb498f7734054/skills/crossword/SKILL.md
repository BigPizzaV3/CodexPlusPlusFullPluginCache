---
name: crossword
description: Create and solve a fresh fullscreen crossword with ChatGPT as the setter — themed answers and clues, a server-built numbered grid, across/down navigation, checking, reveals, a new puzzle on demand, plus local Numbers (Sudoku), Code (colour breaker), and Math (+ − × ÷) modes.
---

# iPlugin Crossword

Use this skill when the user wants to solve a crossword, asks for a puzzle about a topic, or wants a new word grid. The plugin is a fullscreen MCP App: you write the crossword content, the server builds the grid and renders the studio. The studio top bar also contains local **Numbers** (Sudoku), **Code** (Mastermind-style colour breaker), and **Math** (a math crossword) modes with Easy/Standard/Hard; those are client-side and need no tool call.

## Opening the studio

Call `crossword_home` **exactly once per conversation**. It takes no arguments, renders the fullscreen studio, and is the only UI-opening tool. It is a launcher: its result is text only, and the studio fetches the puzzle itself. When the session has no puzzle, it starts a starter grid server-side and the studio loads it, so the studio is never blank. If the user asked for a specific theme, immediately call `crossword_create` to replace that starter. **A second call opens a second studio tab.** Never call it again — not for a new puzzle, not after an error, and not when the user asks for another crossword. Use `crossword_create` in the existing view instead.

## Creating a puzzle

`crossword_create` takes:

- `title` — a short editorial title, not the theme word. “The Long Night”, not “Night Sky”.
- `theme` — the subject, 1–48 characters.
- `subtitle` — one sentence that sets the mood.
- `difficulty` — `easy`, `standard`, or `hard`.
- `entries` — **12–16** `{answer, clue}` pairs (8 minimum, 18 maximum).

The server ignores any grid geometry you might imagine: it arranges the answers, resolves intersections, numbers the entries, and returns the finished puzzle. Do not describe rows, columns, or numbering to the user.

### Answers

- Use common English words, names, and short phrases. **3–12 letters** after removing spaces, apostrophes, and hyphens.
- Prefer a mix of lengths: at least four answers of 6–10 letters and several short crossing words of 3–5 letters.
- Make the set interlock. Use words that share common letters (`A`, `E`, `R`, `S`, `T`, `N`, `L`). Avoid a list of words with no shared letters, and avoid more than two obscure proper nouns.
- Do not repeat an answer. The server rejects duplicates.
- For a phrase, run the words together: `NEWORLEANS`, not `NEW ORLEANS` (spaces are accepted but removed).
- Do not use digits, punctuation other than spaces/apostrophes/hyphens, or non-Latin scripts in answers.

### Clues

- Write fresh, concrete clues of 3–140 characters. Vary the register: some straight definitions, some wordplay, some cultural.
- **Never put the answer in its clue.** The server rejects a clue that contains the answer.
- Do not write “starts with…”, “ends with…”, or give the enumeration in the clue; the UI already shows the length.
- Avoid duplicate clues.
- Keep proper nouns to roughly a quarter of the set.
- Clues may be in the user’s language even when answers are English.

### A reliable generation recipe

1. Pick a specific, visual theme the user asked for. If the user gave no theme, choose something unexpected: a bakery at dawn, maps, silent-film comedy, tidal pools, bookbinding, the Tour de France.
2. Brainstorm 20–24 candidate answers. Choose 12–16 with the most shared letters and a good length mix.
3. Write the clues last, after the answers are fixed.
4. Call `crossword_create` once. If the tool rejects an answer set because too few words connect, replace the named outliers with shorter common words that share letters with the rest, then retry.
5. Reply in one or two sentences: name the puzzle, mention the theme and difficulty, and invite the user to solve it. Never list the answers or the full clue set in chat.

## Studio modes and difficulty

The top bar switches between **Words**, **Numbers**, **Code**, and **Math**. Numbers, Code, and Math are local puzzles: do not call a tool to create them, and do not describe their grids in chat; the studio handles them. The Easy/Standard/Hard control applies to the active mode. In Words it loads a curated starter through the client-side `crossword_starter` tool; that tool is for the studio control, not for model content. When the user asks for a themed or new crossword, always use `crossword_create` with the requested `difficulty` and the existing view updates in place. If the user asks for a Sudoku or code puzzle, it does not require a tool; tell them to use the Numbers or Code tab.

## Generate button

The studio has a visible New puzzle button in every mode. It sends an English prompt. For **Words**, call `crossword_create` with a fresh theme and the requested difficulty. For **Numbers**, **Code**, or **Math**, call `puzzle_generate` with the matching mode and difficulty; the studio loads that generated sample in place. Never call `crossword_home` again and never open a new tab.

## New puzzles

When the user asks for another crossword, call `crossword_create` again with a **different theme and a substantially different answer set**. Do not call `crossword_home` again and do not ask the client to open a new tab or a new conversation. The existing studio updates in place. The server rejects a recent answer set so every puzzle is genuinely new.

## Reading the current puzzle

`crossword_get` returns the grid, numbered clues, and metadata for the current puzzle. Use it only when the user asks about the puzzle already on screen. The studio holds the user’s typed letters locally; this tool does not expose their progress.

## Hints

If the user asks for a hint, give a short nudge based on the clue — a category, a synonym, a bit of trivia, or the first letter only if they ask for it. Do not reveal the whole answer unless they explicitly ask. The in-app Reveal controls are the user’s choice; do not operate them on the user’s behalf.

## Errors

Invalid answers, duplicate entries, giveaway clues, too few entries, and answer sets that cannot interconnect return JSON-RPC errors with a specific message. Read the message and correct the content; do not retry the same set unchanged. If the studio is no longer open, ask the user to reopen it rather than calling `crossword_home` repeatedly.
