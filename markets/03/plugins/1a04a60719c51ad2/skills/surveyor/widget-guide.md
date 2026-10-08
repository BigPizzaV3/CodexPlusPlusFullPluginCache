# Widget guide — render mechanics for the surveyor skill

When to read this: before your first render call in a session — not every response needs it, only the ones that render something. This file carries the HOW of building a rendered research log or answer visual — token layering, the fixed log template, hygiene, and the worked example. The WHEN and WHETHER (execution order, the fallback ladder, one-form rules, the finalization gate) live in `SKILL.md` and gate every response whether or not anything renders.

## The visualizer's own design system — re-derive it every session

Before your first widget call in a session, silently load that tool's own design-system reference (its `read_me`-style helper, if it has one — pick the module closest to "interactive" or "diagram") and use whatever CSS variables and conventions it documents. Do not hard-code variable names from this guide's example into a live response — token names belong to the visualizer, they can change independently of this skill, and copying stale names from an old example silently produces unstyled or invisible output. Treat the example below purely as a shape/structure reference (the step data, the two-color action/limit distinction, the provenance link), and re-derive the actual token names from that tool's current documentation each time you build one.

## Layer OpenLaws's brand tokens on top of the visualizer's structural tokens

Read `brand-tokens.css` (beside this file) and define its `--ol-*` custom properties at the top of every widget's style block. Map the timeline's action/limit nodes, the confidence bands, and citation links to these — `--ol-action`, `--ol-limit`, `--ol-high`, `--ol-flagged`, `--ol-cite` — instead of inventing ad hoc fallback hex values inline.

**Fills vs. text is load-bearing, not stylistic: use the base accents (`--ol-action`, `--ol-high`, …) only for fills, borders, and timeline nodes; any accent-colored TEXT or icon takes the matching `--ol-*-text` variant (`--ol-cite-text` for citation links, `--ol-high-text` for a "High" label, etc.), and card fills only ever use the `-soft` tokens.** The `-text` variants mix the brand hue with the host-following ink so they stay legible on a dark chat surface — the raw accents are dark colors and vanish as dark-on-dark text (the 2026-07-16 review screenshots).

This is a different animal from the visualizer's own tokens above, and doesn't relax that warning: the visualizer's structural tokens (surface, text, border) can drift out from under you and must be re-derived fresh each time, which is exactly why `--ol-ink`, `--ol-muted`, `--ol-surface`, and `--ol-border` are written to chain to those host tokens first, falling back to OpenLaws's own neutrals only when the host doesn't define them. The `--ol-*` accent tokens, by contrast, are skill-owned and brand-locked — fills and nodes render as OpenLaws's own colors regardless of host theme, and won't drift, because the skill (not the visualizer) is their source of truth. See `brand-tokens.css` itself for what's independently verified against openlaws.us's live stylesheet versus estimated.

**If `brand-tokens.css` can't be found or read, don't block the widget on it.** A packaging gap (the file didn't travel with the plugin) is different from the widget tool being unavailable, and it doesn't warrant the plain-text fallback — render the widget using the visualizer's own current tokens as if the brand layer simply weren't part of this skill. Silently proceeding without the brand colors is fine; silently reverting to inline ad hoc hex guesses is not — that's the same drift problem this guide exists to prevent, just triggered by a missing file instead of a missing instruction.

## The research-log render: ONE fixed layout, every time

The log is the same artifact on every answer; it gets no run-to-run creative variation. The template, top to bottom:

1. Visible title **Research log**.
2. A two-item legend distinguishing research actions from disclosed limits, colored `--ol-action` / `--ol-limit`.
3. The numbered vertical step timeline (connecting rail between entries), one entry per action or limit, citations as clickable links in `--ol-cite-text` using each cite's `openlaws_web_url`.
4. A section headed **Confidence** — one level card per claim group, fills in the `-soft` tokens, labels in the matching `--ol-*-text` variants. Distinguish levels visually (color or icon), consistent with the action/limit distinction in the timeline above. **`--ol-low` shares its hex with `--ol-action`/`--ol-cite`** — a low-confidence entry needs a distinct TREATMENT (e.g. a border + icon), not fill color alone, or it reads as an action step or citation link instead of a confidence level (see `brand-tokens.css`'s palette-constraint comment). The confidence section is the last thing in the render — timeline first (what was done), confidence second (what that supports and how strongly).

Same sections, same order, same token mapping, every render. Answer-content visuals (grids, trees, timelines) remain free-form — this template binds the log only.

## Widget hygiene

Keep the widget to the visual only: no prose, section headings, or explanation inside the widget markup beyond the template's own titles — narrative stays in your normal response text, and the rendered content stands on its own (the tool result already shows the user the rendered widget, so repeat nothing from it afterward). If a render needs correction, fix it without narrating the defect — no "fixing a styling bug now" between renders; the user sees finished artifacts, not the workshop. Give the widget a screen-reader-only heading summarizing it, if the visualizer's own rules call for one. Pass the whole log — timeline plus confidence — in a single render call; never split it across two calls or a call plus a text block.

## Worked example (shape/structure reference only — re-derive real token names first)

Step data to render, one entry per research action or disclosed limit:

```
steps = [
  {kind:"action", label:"Scoped the question", detail:"Fixed jurisdiction (California), law type (statute), and currency (in-force text) before any retrieval.", tag:"Scope"},
  {kind:"action", label:"Selected the authority", detail:"Confirmed the section sits in the Civil Code, Title 1.81 (Customer Records).", tag:"Source"},
  {kind:"action", label:"Retrieved by exact citation", detail:"Pulled the section by citation — an exact match, not a keyword hit.", tag:"Primary source", cite:"Cal. Civ. Code § 1798.82", cite_url:"<openlaws_web_url from the envelope>"},
  {kind:"limit", label:"Disclosed the temporal limit", detail:"Current in-force text only — no point-in-time version was retrieved; date-sensitive matters need independent version confirmation.", tag:"Temporal limit"},
  {kind:"limit", label:"Marked the coverage boundary", detail:"Case law, Attorney General opinions, and legislative history fall outside this corpus and were not consulted.", tag:"Coverage boundary"}
]
```

Render per the fixed layout above. Do not paste the markup into chat text, and do not split confidence into a second call.
