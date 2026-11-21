import { escape, json } from "./contract.mjs";

export function pageHtml(options) {
  return `<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>${escape(options.config.title)} · Cutaway</title></head>
<body style="margin:0">${pageFragment(options)}</body></html>`;
}

export function pageFragment({ config, diagram, css, runtime, initial }) {
  const { research, parts, title, description, note, license } = config;
  const { identification, claims, assumptions, unknowns, sources } = research;
  const sourceLinks = ids => ids.map(id => `<a href="${escape(sources[id].url)}" target="_blank" rel="noreferrer">${escape(sources[id].label)}</a>`).join(" · ");
  const list = items => `<ul>${items.map(item => `<li>${escape(item)}</li>`).join("")}</ul>`;
  const status = { confirmed: "Identified", likely: "Likely match", unknown: "Unconfirmed", generic: "Illustrative model" }[identification.status];
  return `<div class="cutaway-root" lang="en"><style>${css}</style>
<main><header><h1>${escape(title)}</h1><p><strong>${status}: ${escape(identification.name)}.</strong> ${escape(identification.detail)}</p><p>${escape(description)}</p></header>
<noscript>Enable JavaScript to use the controls. The drawing shows the initial view.</noscript>
<section class="demo" aria-label="Interactive cutaway"><div class="stage-wrap"><div class="view-control"><label><input id="shell" type="checkbox">Show exterior</label></div><div id="drawing">${diagram}</div><p class="diagram-note">${escape(note)}</p></div>
<aside class="panel"><div class="status-copy"><h2 id="stage">${escape(initial.title)}</h2><p id="stage-description">${escape(initial.description)}</p></div>
<div class="control-row"><button id="play" type="button" aria-pressed="false">Play cycle</button><button id="reset" type="button">Reset</button></div>
<div class="scrub"><label for="progress">Step through the cycle</label><input id="progress" type="range" min="0" max="100" step="0.01" value="${config.state.progress * 100}"></div>
<div class="parts" aria-label="Explore parts">${parts.map(part => `<button type="button" data-select="${part.id}" aria-pressed="false">${escape(part.title)}</button>`).join("")}</div>
<div class="part-info" aria-live="polite"><h3 id="part-title"></h3><p id="part-description"></p><div id="part-sources"></div></div></aside></section>
<div class="downloads"><button type="button" data-export="html">Download HTML</button><button type="button" data-export="svg">Download SVG</button><button type="button" data-export="mp4">Download video</button><button id="cancel-video" type="button" hidden>Cancel</button><a id="save-video" download="cutaway.mp4" hidden>Save MP4</a><span id="export-status" role="status"></span></div>
<section class="evidence"><h2>About this drawing</h2><div class="evidence-grid">
${claims.length ? `<div><h3>Documented</h3><ul>${claims.map(claim => `<li>${escape(claim.text)}<div>${sourceLinks(claim.sources)}</div></li>`).join("")}</ul></div>` : ""}
${assumptions.length ? `<div><h3>Illustrative details</h3>${list(assumptions)}</div>` : ""}
${unknowns.length ? `<div><h3>Unknowns</h3>${list(unknowns)}</div>` : ""}</div></section>
${Object.keys(sources).length ? `<details class="sources"><summary>Sources and scope</summary><ul>${Object.values(sources).map(source => `<li><a href="${escape(source.url)}" target="_blank" rel="noreferrer">${escape(source.label)}</a><p>${escape(source.note)}</p></li>`).join("")}</ul></details>` : ""}
<details class="license"><summary>Drawing toolkit license</summary><pre>${escape(license)}</pre></details>
</main><script id="cutaway-data" type="application/json">${json(config)}</script><script>${runtime.replace(/<\/script/gi, "<\\/script")}</script></div>`;
}
