// Will the print stand on its own? The balance point of the solid model against the area that
// touches the bed, measured on the print as laid out (millimeters, standing on z = 0).
//
// The model faces -y (towards the viewer of the front view), so +y is its back.

const TOUCH = 0.3; // within this of the bed counts as touching, in millimeters

/** positions: flat xyz array; tris: flat index array. */
export function balance(positions, tris) {
  let minZ = Infinity;
  for (let i = 2; i < positions.length; i += 3) if (positions[i] < minZ) minZ = positions[i];
  // Centre of mass of the solid, from the signed volumes of tetrahedra to the origin.
  let V = 0, cx = 0, cy = 0, cz = 0;
  const at = (v, c) => positions[v * 3 + c];
  for (let f = 0; f < tris.length; f += 3) {
    const a = tris[f], b = tris[f + 1], q = tris[f + 2];
    const v = (at(a, 0) * (at(b, 1) * at(q, 2) - at(b, 2) * at(q, 1)) - at(a, 1) * (at(b, 0) * at(q, 2) - at(b, 2) * at(q, 0)) + at(a, 2) * (at(b, 0) * at(q, 1) - at(b, 1) * at(q, 0))) / 6;
    V += v;
    cx += v * (at(a, 0) + at(b, 0) + at(q, 0)) / 4; cy += v * (at(a, 1) + at(b, 1) + at(q, 1)) / 4; cz += v * (at(a, 2) + at(b, 2) + at(q, 2)) / 4;
  }
  if (!(Math.abs(V) > 1e-9)) return null;
  const com = [cx / V, cy / V, cz / V - minZ];
  // The footprint: the outline around every point touching the bed.
  const pts = [];
  for (let i = 0; i < positions.length; i += 3) if (positions[i + 2] - minZ < TOUCH) pts.push([positions[i], positions[i + 1]]);
  pts.sort((p, q) => p[0] - q[0] || p[1] - q[1]);
  const cross = (o, p, q) => (p[0] - o[0]) * (q[1] - o[1]) - (p[1] - o[1]) * (q[0] - o[0]);
  const lower = [], upper = [];
  for (const p of pts) { while (lower.length > 1 && cross(lower.at(-2), lower.at(-1), p) <= 0) lower.pop(); lower.push(p); }
  for (const p of pts.slice().reverse()) { while (upper.length > 1 && cross(upper.at(-2), upper.at(-1), p) <= 0) upper.pop(); upper.push(p); }
  const hull = lower.slice(0, -1).concat(upper.slice(0, -1));
  if (hull.length < 3) return { com, margin: -Infinity, tipDegrees: -90, towards: null, hanging: null };
  // Distance from the balance point to the nearest footprint edge (negative when outside),
  // and which way that edge faces.
  // Inside, the nearest edge is the one it would tip over; outside, the edge it is furthest
  // beyond is the one it has already tipped over.
  let margin = Infinity, normal = null;
  for (let k = 0; k < hull.length; k++) {
    const p = hull[k], q = hull[(k + 1) % hull.length], len = Math.hypot(q[0] - p[0], q[1] - p[1]);
    if (!len) continue;
    const d = cross(p, q, com) / len; // positive on the inner side
    if (d < margin) { margin = d; normal = [(q[1] - p[1]) / len, -(q[0] - p[0]) / len]; }
  }
  const towards = !normal ? null : Math.abs(normal[1]) >= Math.abs(normal[0]) ? (normal[1] > 0 ? 'back' : 'front') : (normal[0] > 0 ? 'right (seen from the front)' : 'left (seen from the front)');
  // A part hanging just above the bed, apart from what touches it (a tail, a cape's hem): it
  // needs support to print, and would steady the print if it touched. Everything below 6% of
  // the height is gathered into patches; a patch that never touches the bed is hanging. A
  // sole that is not quite flat stays joined to the part that touches, so it is not counted.
  let maxZ = -Infinity;
  for (let i = 2; i < positions.length; i += 3) if (positions[i] > maxZ) maxZ = positions[i];
  const H = maxZ - minZ, low = H * 0.06, cell = Math.max(0.2, H * 0.015);
  const cells = new Map();
  for (let i = 0; i < positions.length; i += 3) {
    const h = positions[i + 2] - minZ; if (h >= low) continue;
    const k = `${Math.floor(positions[i] / cell)},${Math.floor(positions[i + 1] / cell)}`;
    const c = cells.get(k) || cells.set(k, { lowest: Infinity, patch: -1 }).get(k);
    if (h < c.lowest) c.lowest = h;
  }
  let hanging = null, patch = 0;
  for (const [start, c0] of cells) {
    if (c0.patch >= 0) continue;
    const stack = [start], members = [];
    c0.patch = patch;
    while (stack.length) {
      const k = stack.pop(), c = cells.get(k); members.push(c);
      const [gx, gy] = k.split(',').map(Number);
      for (let i = -1; i <= 1; i++) for (let j = -1; j <= 1; j++) {
        const n = cells.get(`${gx + i},${gy + j}`);
        if (n && n.patch < 0) { n.patch = patch; stack.push(`${gx + i},${gy + j}`); }
      }
    }
    patch++;
    const lowest = Math.min(...members.map(c => c.lowest));
    if (lowest >= TOUCH && lowest >= 1 && (!hanging || lowest < hanging.height)) hanging = { height: lowest };
  }
  return { com, margin, tipDegrees: Math.atan2(margin, com[2]) * 180 / Math.PI, towards, hanging };
}
