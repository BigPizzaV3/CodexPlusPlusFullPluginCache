import { arrowRotateCounterclockwiseLight16 } from "@oai/icons/arrow-rotate-counterclockwise-light-16";
import { chevronDownSmLight16 } from "@oai/icons/chevron-down-sm-light-16";
import { playLight20 } from "@oai/icons/play-light-20";

const icons = {
  refresh: arrowRotateCounterclockwiseLight16,
  chevronDown: chevronDownSmLight16,
  play: playLight20,
};

/** Decorative controls keep the same artwork without the host's icon renderer. */
export function WorkbenchIcon({ name }: { name: keyof typeof icons }) {
  const icon = icons[name];
  return (
    <svg
      aria-hidden="true"
      focusable="false"
      width={icon.canvas.width}
      height={icon.canvas.height}
      viewBox={icon.canvas.viewBox}
      fill="currentColor"
      style={{
        width: icon.canvas.width,
        height: icon.canvas.height,
        flexShrink: 0,
      }}
      // Only these static, monochrome @oai/icons presets supply SVG markup.
      dangerouslySetInnerHTML={{ __html: icon.body }}
    />
  );
}
