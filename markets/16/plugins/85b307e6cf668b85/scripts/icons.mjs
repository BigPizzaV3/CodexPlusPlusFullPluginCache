// Deterministic opaque device icon, with the mark inside the maskable safe zone.
import png from 'pngjs';
export function makeIcon(size, color = '#2155CD') {
  const image = new png.PNG({ width: size, height: size });
  const rgb = [1, 3, 5].map(start => parseInt(color.slice(start, start + 2), 16));
  for (let y = 0; y < size; y++) for (let x = 0; x < size; x++) {
    const px = x / size, py = y / size;
    const edge = px >= .35 && px <= .65 && py >= .24 && py <= .76;
    const screen = px > .38 && px < .62 && py > .29 && py < .68;
    const dot = Math.hypot(px - .5, py - .72) < .015;
    const ink = edge && !screen && !dot;
    const at = (y * size + x) * 4;
    image.data.set(ink ? [255, 255, 255, 255] : [...rgb, 255], at);
  }
  return png.PNG.sync.write(image);
}
