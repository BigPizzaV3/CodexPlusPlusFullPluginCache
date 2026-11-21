# Moda basics — connection, account, conventions

## Connecting

There is nothing to install and nothing to update on this surface: Moda is connected by your host,
and its tools and skill guides are served by Moda, always current. A succeeding `moda_bootstrap`
IS the health check — call it once, before the first canvas operation.

`moda_bootstrap` names the signed-in identity and the teams you can work in. Team = whose
workspace and billing the work lands in: pass `team` on the tools that take it, and never switch
on your own initiative. Nothing here handles or prints a credential.

## Credits and spend

`moda_bootstrap` reports the plan, the remaining credits, and the entitlements this account has —
it is the answer to "how many credits do we have left?". Deterministic tools report zero metered
credits; believe them, because authoring, editing, screenshots and exports really are free. Each
metered call returns a usage receipt on its result; report it as information, never as a warning.

## Self-description and troubleshooting

- Each tool's own description and schema is ground truth, including whether it mutates or meters.
  Trust it over memory, and over this file.
- The skill guides load by name, free. A failed call carries its whole typed error — code,
  message and hint — on the result you already hold.
- Typed errors carry actionable hints. Follow the hint; on the same code twice, stop and call
  `ask_expert(question=…, context="<the error>")`.

## Result conventions

- Decide from the result's own fields, not the prose summary — the summary omits caveats.
- Big canvases: read the summary first, then scope reads to the pages you need, so a large result
  cannot blow your context.
- **A list result is a PAGE, not the universe.** Check `total` / `has_more` before telling the user
  how many things they have, and follow the cursor or offset the result names. Where the server
  reports no total, say "at least N" — never "N total".
- Ids and URLs are copied verbatim, never retyped or reconstructed.

## Defaults across calls

Chat sessions hold no per-project configuration: there is no pinned team, brand kit or canvas on
this surface. Carry the refs yourself and pass them on every call — the brand kit especially, since
binding it at create time is what makes the artifact on-brand.

## Working through Moda's terminal client instead

The same capabilities ship as a terminal client, which additionally has a local filesystem, web
research, PowerPoint import, and per-repository defaults. If the user asks for any of those, that
client is the honest answer — moda.app documents the install. Everything you do here is portable
to it: same canvases, same kits, same files, same team.
