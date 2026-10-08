---
name: create-japanese-document
description: Create Japanese student study notes, exam summaries, exercise sheets, or simple academic reports as polished PDFs. Use when the user asks to turn material into a Japanese PDF, study guide, シケプリ, 講義ノート, 問題集, or report.
---

# Create a TeX64 document

Keep interaction plain and concise. The user never needs to know that TeX is
used internally.

Whenever a choice is needed, prefer the client's structured question UI (Codex `request_user_input`, Claude `AskUserQuestion`, or an equivalent) over a plain-text question. Ask one question at a time. Fall back to plain text only when the client does not expose a structured question tool.

1. Infer the document kind from the request. If it is genuinely unclear, ask only whether they want a visually structured study handout or a restrained report.
2. Do not ask about fonts, TeX commands, packages, engines, margins in millimetres, or other production details. Unless the user already specified a page size, use B5 for study handouts and A4 for reports. Translate visual wishes such as “soft,” “formal,” “compact,” or “easy to read” into internal settings yourself.
3. Call `doc_types` to choose the closest structure.
4. Call `scaffold_document` and adapt its structure to the user's material. Keep production comments in the internal source; do not ask the user to confirm production settings unless they explicitly care about them.
5. Call `check_document` on the finished source before typesetting.
6. Then take whichever route the environment actually supports:
   - **You can write files and run `latexmk` locally:** call `get_style_files` (start with `list=true`), write the files into the user's project, read `compile_guide`, compile, render pages to images, and inspect them.
   - **You cannot (ChatGPT, or the user has no TeX):** call `compile_document` with the source and the same `preset` / `paper` / `prefix` / `theme` you would have used. The server generates the styles, typesets, and returns a temporary PDF link plus page images. Do not ask the user to install TeX, and do not call `get_style_files` first — the server builds the styles itself.
7. Inspect the returned page images yourself: cover, Japanese glyphs, headings, boxes, margins, page breaks. Fix the source and compile again rather than shipping something you have not looked at.
8. Show the user the PDF link and the preview images. Tell them the server link expires within the hour so they save it. Describe adjustable parts by what they look like on the page, and ask at most one short visual question at a time.
9. Do not show raw TeX logs, package names, or error text to the user. Fix errors first, then return the result.

## Server-side limits

`compile_document` automatically uses a compatible server font, refuses paths outside the document, and cannot add server dependencies. If a build keeps failing because an internal dependency is unavailable, rewrite the source using what is available instead of asking the user to change their machine.
