import { fitProjection, boxCorners, cylinder, slabOf, screenRise, figureSvg } from "../upstream/kit/iso-kit.mjs";
import { materials, solid } from "./materials.mjs";

const plan = { x: -44, y: -38, w: 88, d: 76, r: 8 };
const projection = fitProjection(boxCorners(plan, 0, 165), 720, 600, { pad: 65 });

export function drawing(initial) {
  const body = [
    solid(slabOf(plan, 0, 10, projection), materials.black),
    `<g data-part="guide">${solid(cylinder(0, 0, 30, 10, 77, projection))}</g>`,
    `<g id="plunger" data-part="plunger" transform="translate(0 ${-initial.lift * screenRise(45, projection)})">${solid(cylinder(0, 0, 15, 30, 70, projection), materials.brass)}${solid(cylinder(0, 0, 24, 100, 8, projection), materials.brass)}</g>`,
  ];
  return {
    diagram: figureSvg({ width: 720, height: 600, label: "An illustrative plunger slides vertically through its guide.", body }),
    view: { rise: screenRise(45, projection) },
  };
}
