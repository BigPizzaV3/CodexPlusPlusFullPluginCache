import { mountCutaway } from "./controls.mjs";
import { frame } from "./model.mjs";

mountCutaway({ frame, render({ diagram, state, view }) {
  diagram.querySelector("#plunger").setAttribute("transform", `translate(0 ${-state.lift * view.rise})`);
} });
