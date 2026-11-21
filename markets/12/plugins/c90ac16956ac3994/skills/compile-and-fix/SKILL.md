---
name: compile-and-fix
description: Compile LaTeX with letX and fix the errors it reports until the document builds. Use when the user wants a PDF of LaTeX from the conversation or of one of their letX projects, or asks why their LaTeX does not compile.
---

# Compile LaTeX with letX and fix its errors

The user's instructions come first. If they ask only for a compile, compile and report the result;
change their files only when they ask for a fix.

## What you need

- LaTeX in the conversation, or the name of one of the user's letX projects.
- For a project, find its id with `list_projects`. If several projects could be the one meant,
  ask which.

## Steps

1. Compile.
   - LaTeX from the conversation: call `compile_latex` with the whole main file as `main_tex` and
     any other text files (chapters, `refs.bib`, a custom `.sty`) in `files`. letX saves them in
     the user's "AI Scratchpad" project.
   - A letX project: call `compile_project` with its id.
2. Read the result.
   - "Compiled successfully" with a PDF link: give the user the PDF link, and the editor link if
     they want to keep editing in letX.
   - Errors: each one names the file and line TeX stopped at, for example
     `./main.tex:16: Undefined control sequence.`, and the source line follows after `l.16`.
3. Fix, when the user wants a fix.
   - In a project, read the file the error names with `read_project_file`, then write the
     corrected file with `update_project_file`. Send the whole file: it replaces the current
     text, and the previous version stays in the project's history.
   - For LaTeX from the conversation, correct it and call `compile_latex` again.
   - Change only what the error needs. Keep the author's words, structure and packages.
4. Compile again. Repeat while the errors change. If the same error survives three rounds, stop
   and tell the user what is still wrong and where.

## Engines

Documents that load `fontspec`, `unicode-math`, `polyglossia` or `xeCJK` need XeLaTeX or LuaLaTeX,
and documents that use `\directlua` or `luacode` need LuaLaTeX. When the errors show the document
needs another engine, set it with `set_project_compiler` for a project, or pass `compiler` to
`compile_latex`, then compile again.

## Never

- Never invent a PDF link, a page count or a result that a tool did not return.
- Never delete the user's content to make an error go away. If a fix would remove text, ask first.
- Images and other binary files cannot be sent this way. If a figure is missing, tell the user to
  upload it in the letX editor.
