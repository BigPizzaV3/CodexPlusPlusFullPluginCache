---
name: horizonx
description: Find and add HorizonX animated UI components, image textures, WebGL shaders, landing page templates, UI kits and design systems to the user's project through the HorizonX MCP server. Use when the user asks for a visual effect, an animated section, a shader or texture background, a ready-made landing page or template, or mentions HorizonX.
---

# HorizonX

HorizonX is a catalogue of production-ready front-end work. The `horizonx` MCP server gives you two catalogues:

- **Components**: animated UI components, image textures and WebGL shaders. They are generated as code you can paste: a self-contained HTML document, or one Svelte or React component with no runtime dependencies.
- **Library**: ready-made products delivered as files: landing pages and site templates, UI kits, design systems, and image and video assets.

Pick the catalogue by what the user needs. Something to drop into an existing page ("a tilt-on-hover card", "an ASCII effect on the hero photo") is a component. A whole page, kit or asset pack is a Library product.

## Before you start

- If the `horizonx` tools are missing or every call fails with an authentication error, the server is not connected or not signed in. Tell the user to sign in when their tool asks (in Claude Code, run `/mcp` and pick `horizonx`; in Codex, run `codex mcp login horizonx`). Setup for every tool is at https://horizonx.so/mcp.
- The server needs an active HorizonX membership. If a call says a membership is required, say so plainly and stop. Do not try other tools to work around it.
- Do not mention plans or prices unless the user asks.

## Components

1. **Search.** Call `search_components` with a plain-language description of what the element should do, not what it is called: "text that follows a curve", "cards that tilt on hover", "grainy gradient background". Use `kind` (`component`, `texture` or `shader`) only when the user was specific. Calling it with no query lists what exists.
2. **Choose.** Pick the closest match by its description. If two or three are close and the choice is a matter of taste, show the user the options with their `editorUrl` so they can preview them in the browser, and let them choose. If the user only asked to find, search or compare, list the best matches (title, one line each, `editorUrl`) and stop there: an export uses their allowance, so export only once they want it in their code.
3. **Inspect.** Call `get_component` on the slug. It lists every parameter with its current value and allowed range. Only call it once per component.
4. **Export.** Call `export_component` with:
   - `framework`: match the project. Use `react` for React and Next.js, `svelte` for Svelte and SvelteKit, `html` for anything else, including Vue, Astro and plain sites.
   - `parameters`: only keys that `get_component` listed, and only when the user asked for something different from the default (colours, speed, text, sizes). Unknown keys and out-of-range values are dropped silently, so check the names.
5. **Place it.** The first text block is the file name and a usage hint; the second is the code. Write the code into the project where similar components live (look for `components/`, `src/lib/components/` or similar), keep the file name unless the project has its own convention, and import it where the user asked for it. The code has no dependencies: do not install packages for it.

### Textures

A texture applies a look to one image. Pass the user's image through the `images` parameter as a root-relative path or an absolute URL. The image must be served from the same origin as the page or with CORS headers, because the effect reads its pixels. Without it, the sample image is used, which is rarely what the user wants.

### Export limits

Each new component exported counts against the member's daily export allowance and a 30-day limit on different components. Exporting a component that was already exported in that window again is free, so re-export with new parameters instead of searching for a different component. If an export is refused because a limit was reached, tell the user the message the server returned, including when it resets. Do not retry.

## Library

1. **Search.** Call `search_library` with what the user wants ("SaaS landing page", "finance dashboard UI kit"). `category` is optional, for example `Code`, `UI/UX`, `Assets` or `Landing Pages`.
2. **Check.** Call `get_library_item` on the slug. It shows the format (code, Figma or media), what is included and the file list, and it does not use a download. Confirm the format fits: a Figma file cannot be dropped into a codebase.
3. **Download.** Call `download_library_item` only when the user wants the files. It spends one download from the member's plan limit, unless the same product was already downloaded that day. The links expire in about five minutes, so fetch them immediately, for example with `curl -L -o <file> "<url>"`, then unpack them where the user asked.

## Good habits

- Ask one short question only when the request is truly ambiguous. When the user asks for the element itself ("add an animated background to the hero"), search, choose and build. When they ask to find or see options, show the options first.
- Say which HorizonX component or product you used, with its `editorUrl` when there is one, so the user can tweak it in the visual editor later.
- Keep the generated code as exported. Adapt the surrounding page, imports and props, not the effect itself, unless the user asks.
