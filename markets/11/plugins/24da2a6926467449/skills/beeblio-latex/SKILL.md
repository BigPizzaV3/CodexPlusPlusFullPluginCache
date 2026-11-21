---
name: beeblio-latex
description: Compile saved Beeblio LaTeX project files to PDF, check source dependencies, and download a source bundle. Use when a user asks to diagnose, compile, or package a .tex file in a connected Beeblio project.
---

# LaTeX in Beeblio projects

Use the connected Beeblio MCP tools and project-relative paths. Resolve the project with `list_projects`, then find the saved `.tex` source with `list_files` or `search_files`. The MCP cannot see unsaved editor content or Beeblio's live reading preview. Ask the user to save a draft before operating on it.

## Inspect and edit

- Read the source with `read_text_file`, following `nextOffset` if present. For a small correction, use `edit_document` with the current ETag and an exact passage or unique anchor. For a new file, use `write_text_file` with `ifNotExists`; for a full replacement, supply the current `expectedEtag`. If a precondition fails, reread before retrying.
- Run `get_latex_diagnostics` to check saved `\input` and `\include` files, bibliography files, and figures. Report its missing dependencies and issues, but do not treat a clean result as proof that TeX compiles. The tool does not run a compiler.
- Keep included sources and assets in the project workspace. If a referenced file is missing, resolve its path from the diagnostic result. Do not fabricate a figure, citation, or bibliography entry to silence an error.

## Compile and deliver

- Use the current source ETag returned by `read_text_file`, `stat_file`, or `get_latex_diagnostics` as `expectedEtag` for `compile_latex`. Reinspect if it reports a conflict. Compilation may take several minutes. A successful call updates the source's deterministic PDF under `4-Reports/Compiled/` and returns a stable Beeblio download `url` and an exact-file `pageUrl`. A later successful compile of the same source replaces that PDF.
- If compilation fails, use the returned compiler error to identify the source or dependency to correct. Explain any timeout or unavailable compiler rather than claiming a PDF was created. Only report a compiled PDF after a successful tool result.
- For a portable source ZIP, call `get_latex_source_bundle`. It includes the saved root `.tex`, available referenced files, and an existing compiled PDF when available; report its missing-dependency warnings. Share the returned Beeblio `url` with the user. The `directStorageUrl` expires after 15 minutes and is only for automated fetching. Identify the durable project source and PDF paths separately.
