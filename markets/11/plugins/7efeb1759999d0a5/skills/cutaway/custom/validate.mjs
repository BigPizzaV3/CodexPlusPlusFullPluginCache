import { existsSync, readFileSync, realpathSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { Script } from "node:vm";
import { validateConfig } from "./contract.mjs";

function check(condition, message) {
  if (!condition) throw new Error(message);
}

function attributes(tag) {
  return Object.fromEntries([...tag.matchAll(/([^\s=<>]+)\s*=\s*(?:"([^"]*)"|'([^']*)'|([^\s>]+))/g)]
    .map(([, key, double, single, bare]) => [key.toLowerCase(), double ?? single ?? bare]));
}

function checkMarkup(markup) {
  for (const match of markup.matchAll(/<([a-z][\w:-]*)\b[^>]*>/gi)) {
    const tag = match[1].toLowerCase();
    const attrs = attributes(match[0]);
    check(!["iframe", "object", "embed", "foreignobject", "base", "form"].includes(tag), `Unsupported embedded element: ${tag}`);
    check(!Object.keys(attrs).some(key => key.startsWith("on")), "Use the bundled runtime instead of inline event attributes");
    if (tag === "script") check(!("src" in attrs), "Scripts must be inline");
    if (tag === "link") check(!("href" in attrs), "Styles and fonts must be inline");
    if (["img", "image", "use", "video", "audio", "source"].includes(tag)) {
      for (const key of ["src", "href", "xlink:href", "srcset", "poster"]) {
        if (key in attrs) check(attrs[key].startsWith("#"), `External or embedded media dependency: ${tag} ${key}`);
      }
    }
    if (tag === "a" && "href" in attrs) check(/^(?:https:\/\/|#)/i.test(attrs.href), "Links must use HTTPS or a local anchor");
    for (const key of ["d", "points", "transform", "viewbox", "x", "y", "cx", "cy", "r", "width", "height"]) {
      if (key in attrs) check(!/(?:NaN|[+-]?Infinity)/i.test(attrs[key]), `Non-finite SVG geometry: ${key}`);
    }
  }
  check(!/@import\b/i.test(markup), "CSS imports prevent standalone use");
  for (const [, reference] of markup.matchAll(/url\(\s*["']?([^\s"')]+)["']?\s*\)/gi)) {
    check(reference.startsWith("#"), "CSS resources must be local SVG references");
  }
}

export function validateSvg(svg) {
  check(/^\s*<svg\b/i.test(svg) && /<\/svg>\s*$/i.test(svg), "Expected a standalone SVG");
  check(!/<script\b/i.test(svg), "A static SVG must not need scripts");
  check(/<metadata>/.test(svg) && /<desc>/.test(svg), "SVG must preserve research and license information");
  const bounds = attributes(svg.match(/<svg\b[^>]*>/i)[0]).viewbox?.split(/[ ,]+/).map(Number);
  check(bounds?.length === 4 && bounds.every(Number.isFinite) && bounds[2] > 0 && bounds[3] > 0, "Invalid SVG viewBox");
  checkMarkup(svg);
}

export function validateArtifact(html) {
  const scripts = [...html.matchAll(/<script\b([^>]*)>([\s\S]*?)<\/script\s*>/gi)];
  check(scripts.length === [...html.matchAll(/<script\b/gi)].length, "Unclosed inline script");
  let config;
  let executable = 0;
  for (const [, raw, source] of scripts) {
    const attrs = attributes(raw);
    check(!("src" in attrs), "Scripts must be inline");
    if (attrs.type === "application/json") {
      check(attrs.id === "cutaway-data" && !config, "Expected one cutaway-data record");
      config = JSON.parse(source);
    } else {
      check(!attrs.type || attrs.type === "text/javascript", "Bundle the runtime as a classic script");
      check(!/<!doctype\b|<\/?(?:html|head|body)(?:\s|>)/i.test(source), "Full-page markup inside the runtime can break inline previews");
      new Script(source, { filename: "cutaway-inline.js" });
      executable++;
    }
  }
  check(config && executable > 0, "Missing cutaway config or runtime");
  validateConfig(config);
  check(typeof config.license === "string" && config.license.trim(), "Preserve the drawing toolkit license");
  const markup = html.replace(/<script\b[^>]*>[\s\S]*?<\/script\s*>/gi, "");
  checkMarkup(markup);
  const elements = [...markup.matchAll(/<([a-z][\w:-]*)\b[^>]*>/gi)].map(match => ({ tag: match[1].toLowerCase(), ...attributes(match[0]) }));
  const required = {
    drawing: "div", progress: "input", play: "button", reset: "button", shell: "input",
    stage: "h2", "stage-description": "p", "part-title": "h3", "part-description": "p", "part-sources": "div", "export-status": "span", "cancel-video": "button", "save-video": "a",
  };
  for (const [id, tag] of Object.entries(required)) {
    const matches = elements.filter(element => element.id === id);
    check(matches.length === 1 && matches[0].tag === tag, `Missing or duplicate control: ${id}`);
  }
  const slider = elements.find(element => element.id === "progress");
  check(slider.type === "range" && slider.min === "0" && slider.max === "100", "Progress control must cover 0–100");
  for (const part of config.parts) {
    check(elements.some(element => element.tag === "button" && element["data-select"] === part.id), `Missing part button: ${part.id}`);
    check(elements.some(element => element["data-part"] === part.id), `Missing drawn part: ${part.id}`);
  }
  for (const format of ["html", "svg", "mp4"]) check(elements.some(element => element.tag === "button" && element["data-export"] === format), `Missing ${format} download control`);
  return { checks: ["Inline JavaScript syntax", "No full-page helpers in the runtime", "Research record and source references", "Required controls and drawn parts", "Static resource references and finite geometry"], remaining: ["Run the controls and downloads in a browser", "Inspect desktop and narrow layouts", "Verify the actual ChatGPT preview", "Check that the sources support the claims"] };
}

if (process.argv[1] && existsSync(process.argv[1]) && realpathSync(process.argv[1]) === fileURLToPath(import.meta.url)) {
  const [html, svg, extra] = process.argv.slice(2);
  if (!html || extra) throw new Error("Usage: bun validate.mjs <cutaway.html> [cutaway.svg]");
  const report = validateArtifact(readFileSync(html, "utf8"));
  if (svg) {
    validateSvg(readFileSync(svg, "utf8"));
    report.checks.push("Standalone SVG structure and metadata");
  }
  console.log(JSON.stringify(report, null, 2));
}
