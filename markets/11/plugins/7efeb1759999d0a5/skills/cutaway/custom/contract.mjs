export const escape = value => String(value).replace(/[&<>"']/g, char => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[char]);
export const json = value => JSON.stringify(value).replaceAll("<", "\\u003c");
export const clamp = value => Number.isFinite(value) ? Math.max(0, Math.min(1, value)) : 0;

function requireValue(condition, message) {
  if (!condition) throw new Error(message);
}
function text(value, name) {
  requireValue(typeof value === "string" && value.trim().length > 0, `${name} needs text`);
}
function texts(value, name) {
  requireValue(Array.isArray(value), `${name} must be an array`);
  value.forEach(item => text(item, name));
}

export function validateConfig(config) {
  const { research, parts, steps, cycleSeconds, title, description, note } = config;
  for (const [name, value] of Object.entries({ title, description, note })) text(value, name);
  requireValue(research && typeof research === "object", "Missing research record");
  text(research.identification?.name, "Identification");
  text(research.identification?.detail, "Identification detail");
  requireValue(["confirmed", "likely", "unknown", "generic"].includes(research.identification.status), "Invalid identification status");
  requireValue(research.sources && typeof research.sources === "object" && !Array.isArray(research.sources), "Sources must be keyed by ID");
  for (const [id, source] of Object.entries(research.sources)) {
    requireValue(/^[a-z][a-z0-9-]*$/.test(id), "Invalid source ID");
    text(source.label, `Source ${id}`);
    text(source.note, `Scope of source ${id}`);
    const url = new URL(source.url);
    requireValue(url.protocol === "https:" && !url.username && !url.password, `Source ${id} needs a public HTTPS URL`);
  }
  const references = ids => {
    texts(ids, "Source references");
    for (const id of ids) requireValue(Object.hasOwn(research.sources, id), `Unknown source: ${id}`);
  };
  requireValue(Array.isArray(research.claims), "Claims must be an array");
  for (const claim of research.claims) {
    text(claim.text, "Claim");
    references(claim.sources);
    requireValue(claim.sources.length > 0, "Documented claims need a source");
  }
  texts(research.assumptions, "Assumptions");
  texts(research.unknowns, "Unknowns");
  requireValue(Array.isArray(parts) && parts.length > 0, "Provide selectable parts");
  const ids = new Set();
  for (const part of parts) {
    requireValue(/^[a-z][a-z0-9-]*$/.test(part.id) && !ids.has(part.id), "Part IDs must be unique lowercase names");
    ids.add(part.id);
    text(part.title, "Part title");
    text(part.description, "Part description");
    references(part.sources);
  }
  requireValue(Number.isFinite(cycleSeconds) && cycleSeconds > 0, "Cycle duration must be positive");
  requireValue(Array.isArray(steps) && steps.length >= 2 && steps[0] === 0 && steps.at(-1) === 1
    && steps.every((step, index) => Number.isFinite(step) && step >= 0 && step <= 1 && (!index || step > steps[index - 1])), "Steps must increase from 0 to 1");
  const state = config.state;
  requireValue(state && Number.isFinite(state.progress) && clamp(state.progress) === state.progress
    && ids.has(state.part) && typeof state.exterior === "boolean", "Invalid initial view state");
}

export function researchSummary(research) {
  const { identification, claims, assumptions, unknowns, sources } = research;
  return [
    `${identification.status}: ${identification.name}. ${identification.detail}`,
    ...claims.map(claim => `${claim.text} Sources: ${claim.sources.map(id => sources[id].url).join(", ")}`),
    ...assumptions.map(item => `Illustrative: ${item}`),
    ...unknowns.map(item => `Unknown: ${item}`),
  ].join("\n");
}

export function standaloneSvg(diagram, config) {
  const match = diagram.match(/\bviewBox="([^"]+)"/);
  const bounds = match?.[1].split(/[ ,]+/).map(Number);
  requireValue(bounds?.length === 4 && bounds.every(Number.isFinite) && bounds[2] > 0 && bounds[3] > 0, "Drawing needs a finite viewBox");
  const [x, y, width, height] = bounds;
  const { title, note, research, license, state } = config;
  const detail = researchSummary(research);
  const inner = diagram.replace(/^\s*<svg\b[^>]*>/, "").replace(/<\/svg>\s*$/, "");
  const lines = `${research.identification.status}: ${research.identification.name}. ${note}`.match(/.{1,76}(?:\s|$)|\S{1,76}/g) ?? [];
  const footerHeight = 38 + lines.length * 18;
  return `<svg xmlns="http://www.w3.org/2000/svg" width="${width}" height="${height + footerHeight}" viewBox="${x} ${y} ${width} ${height + footerHeight}" role="img" aria-label="${escape(title)}">
<title>${escape(title)}</title><desc>${escape(detail)}</desc><metadata>${escape(JSON.stringify({ research, state, license }))}</metadata>
<rect x="${x}" y="${y}" width="${width}" height="${height + footerHeight}" fill="#f6f3ec"/>
${inner}
<text x="${x + 20}" y="${y + height + 22}" font-family="sans-serif" font-size="12" fill="#344434">${lines.map((line, index) => `<tspan x="${x + 20}" dy="${index ? 18 : 0}">${escape(line.trim())}</tspan>`).join("")}</text></svg>`;
}
