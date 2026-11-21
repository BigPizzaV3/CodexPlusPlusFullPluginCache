# Radar cards

Use a Radar card only when the client exposes a Particle render tool backed by an MCP Apps UI resource and the visual adds value.

## Preferred flow

1. Call the normal Particle data tool first.
2. Request `output_format: "json"` for chaining only when the data tool exposes that parameter; otherwise use its returned structured content or Markdown evidence.
3. Read the exposed schema for `particle_radar_render_cards` in the client's MCP `tools/list`. It is one of the fixed tools on the bundled `/plugins` connection.
4. Call the renderer directly with a `title` and a `cards` array of up to six selected results. Each card has `kind` (`episode`, `podcast`, `company`, or `person`), `title`, and a canonical HTTPS `source_url` returned by Particle. Optional `subtitle`, `summary`, and up to four `facts` (`label`/`value`) provide context. Keep summaries grounded in the retrieved results and preserve dates, units, and organic-versus-paid distinctions.
5. Let the renderer own its `ui://particle/radar-cards-v1.html` resource. It returns structured cards and the same evidence in Markdown. Rendering does not fetch data again or store the selection. The account's existing metered research usage and previously enabled overage still apply. An empty `cards` array produces a no-results state.

The heading and card titles are 1–160 characters, subtitles up to 160, summaries up to 800, and source URLs up to 2048. Each of up to four facts has a 1–60 character label and 1–120 character value. Use the exposed schema for current constraints. An empty-state payload is `{"title":"No matching results","cards":[]}`. Do not supply HTML, full transcripts, credentials, or URLs with query parameters or fragments. If a result has no suitable source URL, show that result as text rather than inventing a link. The direct renderer returns both UI metadata and a Markdown fallback; use that fallback when the client cannot display cards.

Do not assume a renderer exists, invent a renderer tool name, or send credentials to a widget. When the client or server has no UI capability, return a compact Markdown summary with source links. The same workflow must remain useful in Codex and other non-UI MCP clients.

Avoid card spam: render one focused card or a small comparison set, not every intermediate tool result.
