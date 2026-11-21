import { clamp } from "./contract.mjs";

export const model = {
  title: "A plunger in motion",
  description: "Move through the cycle and select a part to see its role.",
  note: "Illustrative geometry and timing.",
  cycleSeconds: 8,
  steps: [0, .25, .5, .75, 1],
  state: { progress: 0, part: "plunger", exterior: false },
  parts: [
    { id: "plunger", title: "Plunger", description: "The plunger slides vertically through the guide. Its motion is prescribed for this illustration; no driving mechanism is shown.", sources: [] },
    { id: "guide", title: "Guide", description: "The guide keeps the plunger aligned. The surfaces are simplified to make the motion visible.", sources: [] },
  ],
};

export function frame(progress) {
  const p = clamp(progress);
  return {
    progress: p,
    lift: (1 - Math.cos(p * Math.PI * 2)) / 2,
    title: p === 0 ? "Ready" : p === 1 ? "Complete" : p < .5 ? "Rising" : "Returning",
    description: "The plunger travels up, then returns to its starting position.",
  };
}
