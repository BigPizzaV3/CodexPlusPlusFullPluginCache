# Web page for a signage player

Use a hosted page when content changes several times a week, shows live data, or is interactive (then
also read `references/kiosk.md`). Build it with the host's web-page tool (`references/host-tools.md`),
then publish with `optisigns_asset_create{url, name}`.

## What a player is

A small Android media player (about 1 GB RAM) with a modern WebView, running 24/7. It opens the page once
and never reloads it. Two rules matter more than anything else: **memory stays flat** and **the page never
needs a reload**. Keep the page ≤150 KB gzipped and load only what is shown.

## Fit the viewport you get

- Read `innerWidth` / `innerHeight`. The page may run in a zone of a split screen, smaller than the TV.
  A strip (height ≤100 px, or width/height ≥6) gets a one-line layout.
- Portrait: use `@media (max-aspect-ratio: 1/1)`. No orientation parameter is passed to the page.
- Size type in `vh` so it scales with the zone.
- Keep content 5% inside every edge. No scrolling, ever: the page fits one viewport.

## Memory and never-reload

- JS heap ≤25 MB steady, with no growth over hours. Any leak accumulates until the player struggles.
- No timers under 1 s. Release every listener, timer and observer you replace.
- No runtime CSS-in-JS; plain CSS. Don't keep growing arrays or DOM (replace nodes, don't append).

## Refresh

- Poll for new data with ETag / `If-None-Match`: ≥8 s for small config, 60 s for content.
- Up to 4 copies of the page can run on one player (zones). Add random jitter of up to 30 s to polls.
- Never call `location.reload()` except as a capped crash guard. No navigation away from the page.
- A clock ticks with a minute-aligned `setTimeout`, not `requestAnimationFrame`.

## Never a blank frame

- Paint from cache first (last good data in memory or `localStorage`), then refresh.
- On error: keep the last good content, or show a branded fallback panel (logo + message). Try one
  re-render; reload only as a last resort, capped.
- A failed fetch never clears the screen.

## Motion (the player's GPU is weak)

- CSS `@keyframes` on `transform` only, `will-change: transform`, no JavaScript per frame, no shadows
  or filters on moving layers. Pause animation when `document.hidden`.
- Measure text after `document.fonts.ready`, or layouts jump when the font arrives.

## No input

No hover, no scroll, no cursor, no keyboard. Nobody will click. (A kiosk is the exception:
`references/kiosk.md`.)

## Self-contained and public

- The player caches the page. First paint must need no runtime fetch: inline CSS, inline small images
  as data URIs, scripts only from a pinned CDN version if you need a library at all.
- Don't add a service worker; offline caching is the player's job.
- The URL must open in an anonymous browser (no sign-in, public). Check that before publishing.

## Skeleton

```html
<!doctype html><html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>Lobby board</title>
<style>html,body{margin:0;height:100%;overflow:hidden;background:#0B2545;color:#F4F1EA;font-family:system-ui,sans-serif}
main{box-sizing:border-box;height:100vh;padding:5vh 5vw;display:flex;flex-direction:column;justify-content:center}
h1{font-size:10vh;margin:0}p{font-size:5vh;margin:2vh 0 0}#fb{display:none}
@media (max-aspect-ratio:1/1){h1{font-size:7vh}}</style></head><body>
<main id="app"><h1>Welcome</h1><p id="msg">Loading…</p></main>
<main id="fb"><h1>Acme Co.</h1><p>Back shortly</p></main>
<script>let etag='',last=null;const show=t=>{document.getElementById('msg').textContent=t};
async function poll(){try{const r=await fetch('data.json',{headers:etag?{'If-None-Match':etag}:{}});
if(r.status===200){etag=r.headers.get('ETag')||'';last=(await r.json()).message;show(last);fb.style.display='none';app.style.display='flex'}}
catch(e){if(last===null){app.style.display='none';fb.style.display='flex'}}
setTimeout(poll,60000+Math.random()*30000)}poll();</script></body></html>
```
