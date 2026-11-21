import { readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { model, frame } from "./model.mjs";
import { drawing } from "./drawing.mjs";
import { pageHtml, pageFragment } from "./page.mjs";
import { standaloneSvg, validateConfig } from "./contract.mjs";
import { validateArtifact, validateSvg } from "./validate.mjs";

const here = dirname(fileURLToPath(import.meta.url));

export async function buildCutaway(output) {
  const research = JSON.parse(readFileSync(join(here, "research.json"), "utf8"));
  const initial = frame(model.state.progress);
  const { diagram, view } = drawing(initial);
  const config = { ...model, view, research, license: readFileSync(join(here, "../LICENSE"), "utf8") };
  validateConfig(config);
  const compiled = await Bun.build({ entrypoints: [join(here, "runtime.mjs")], target: "browser", format: "iife", minify: true });
  if (!compiled.success) throw new AggregateError(compiled.logs, "Couldn't bundle the cutaway controls");
  const options = { config, diagram, initial, css: readFileSync(join(here, "style.css"), "utf8"), runtime: await compiled.outputs[0].text() };
  const html = pageHtml(options);
  const fragment = pageFragment(options);
  const svg = standaloneSvg(diagram, config);
  validateArtifact(html);
  validateArtifact(fragment);
  validateSvg(svg);
  writeFileSync(join(output, "cutaway.html"), html);
  writeFileSync(join(output, "cutaway.fragment.html"), fragment);
  writeFileSync(join(output, "cutaway.svg"), svg);
  console.log(`Built ${join(output, "cutaway.html")}, cutaway.fragment.html, and cutaway.svg`);
}
