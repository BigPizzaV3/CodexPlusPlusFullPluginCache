import { escape } from "./contract.mjs";

export const materials = {
  black: { fill: "#232a28", top: "#424a45", edge: "#788077", shades: ["#202623", "#29312c", "#323b34", "#3c453d"] },
  steel: { fill: "#9caaa1", top: "#e1e7dd", edge: "#586e62", shades: ["#72867b", "#8c9f92", "#afbeb1", "#c5cec1"] },
  ceramic: { fill: "#e5dfd1", top: "#faf6e9", edge: "#a59e90", shades: ["#b9b5a7", "#cec9b9", "#ded9c9", "#eae6d8"] },
  brass: { fill: "#b78249", top: "#edc58a", edge: "#845d34", shades: ["#8f6237", "#ac7b45", "#c5965c", "#dcae76"] },
  coffee: { fill: "#584332", top: "#76543b", edge: "#3c3026", shades: ["#483728", "#574130", "#654c35", "#806142"] },
};

export function solid(shape, material = materials.steel) {
  const face = (d, color) => d ? `<path d="${escape(d)}" fill="${escape(color)}" stroke="${escape(color)}" stroke-width=".3"/>` : "";
  const edge = (d, width) => d ? `<path d="${escape(d)}" fill="none" stroke="${escape(material.edge)}" stroke-width="${width}" stroke-linejoin="round"/>` : "";
  return `<g>${face(shape.fill, material.fill)}${shape.shades.map((d, index) => face(d, material.shades[index])).join("")}${face(shape.top, material.top)}${edge(shape.crease, .55)}${edge(shape.outline, .8)}</g>`;
}
