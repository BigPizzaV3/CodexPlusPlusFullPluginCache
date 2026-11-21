"use strict";
var WandeoAnatomyRuntime = (() => {
  var __defProp = Object.defineProperty;
  var __getOwnPropDesc = Object.getOwnPropertyDescriptor;
  var __getOwnPropNames = Object.getOwnPropertyNames;
  var __hasOwnProp = Object.prototype.hasOwnProperty;
  var __export = (target, all) => {
    for (var name in all)
      __defProp(target, name, { get: all[name], enumerable: true });
  };
  var __copyProps = (to, from, except, desc) => {
    if (from && typeof from === "object" || typeof from === "function") {
      for (let key of __getOwnPropNames(from))
        if (!__hasOwnProp.call(to, key) && key !== except)
          __defProp(to, key, { get: () => from[key], enumerable: !(desc = __getOwnPropDesc(from, key)) || desc.enumerable });
    }
    return to;
  };
  var __toCommonJS = (mod) => __copyProps(__defProp({}, "__esModule", { value: true }), mod);

  // src/core/anatomy-runtime.ts
  var anatomy_runtime_exports = {};
  __export(anatomy_runtime_exports, {
    anatomyRuntime: () => api
  });

  // third_party/anatomy/kit/turn.mjs
  var T3_ROOT = Math.sqrt(1.6);
  var T3_TAU = Math.PI * 2;
  var T3_RAD = Math.PI / 180;
  var T3_LB = [0, 0.2, 0.42, 0.62];
  var T3_EB = [0.25, 0.5, 0.75];
  var T3_SOFT = 0.035;
  var T3_LEVELS = 32;
  var T3_Q = 64;
  var t3State = { detail: 1, exact: false };
  function t3Num(v) {
    if (t3State.exact) return String(Math.round(v * 1e6) / 1e6);
    let t = Math.round(v * 100);
    if (t === 0) return "0";
    let sign = "";
    if (t < 0) {
      sign = "-";
      t = -t;
    }
    const whole = Math.floor(t / 100);
    const part = t - whole * 100;
    if (part === 0) return sign + whole;
    if (part < 10) return sign + whole + ".0" + part;
    return sign + whole + "." + (part % 10 === 0 ? part / 10 : part);
  }
  function t3Fix(v, scale) {
    const t = Math.round(v * scale) / scale;
    return t === 0 ? "0" : String(t);
  }
  function t3Path(buf, count, closed) {
    if (count < 2) return "";
    let s = "M" + t3Num(buf[0]) + " " + t3Num(buf[1]);
    for (let i = 1; i < count; i++) s += "L" + t3Num(buf[2 * i]) + " " + t3Num(buf[2 * i + 1]);
    return closed ? s + "Z" : s;
  }
  var t3Step = (a, b, x) => {
    const t = Math.min(1, Math.max(0, (x - a) / (b - a)));
    return t * t * (3 - 2 * t);
  };
  function t3Level(score, bands) {
    let u = 0;
    for (let i = 0; i < bands.length; i++) u += t3Step(bands[i] - T3_SOFT, bands[i] + T3_SOFT, score);
    return Math.round(u * T3_Q);
  }
  function t3Grow(f, name, size, Kind) {
    if (!f[name] || f[name].length < size) f[name] = new Kind(Math.max(size, f[name] ? f[name].length * 2 : 16));
    return f[name];
  }
  function t3Box(buf, count, box) {
    let x0 = Infinity;
    let y0 = Infinity;
    let x1 = -Infinity;
    let y1 = -Infinity;
    for (let i = 0; i < count; i++) {
      const x = buf[2 * i];
      const y = buf[2 * i + 1];
      if (x < x0) x0 = x;
      if (x > x1) x1 = x;
      if (y < y0) y0 = y;
      if (y > y1) y1 = y;
    }
    box[0] = x0;
    box[1] = y0;
    box[2] = x1;
    box[3] = y1;
  }
  function t3Unit(v) {
    const l = Math.hypot(v[0], v[1], v[2]) || 1;
    return [v[0] / l, v[1] / l, v[2] / l];
  }
  function t3Rot(axis, degrees) {
    const [x, y, z] = t3Unit(axis);
    const c = Math.cos(degrees * T3_RAD);
    const s = Math.sin(degrees * T3_RAD);
    const C = 1 - c;
    return new Float64Array([c + x * x * C, x * y * C - z * s, x * z * C + y * s, y * x * C + z * s, c + y * y * C, y * z * C - x * s, z * x * C - y * s, z * y * C + x * s, c + z * z * C]);
  }
  function t3Mul(A, B) {
    const out = new Float64Array(9);
    for (let r = 0; r < 3; r++) for (let c = 0; c < 3; c++) out[r * 3 + c] = A[r * 3] * B[c] + A[r * 3 + 1] * B[3 + c] + A[r * 3 + 2] * B[6 + c];
    return out;
  }
  var t3Apply = (R, v) => [R[0] * v[0] + R[1] * v[1] + R[2] * v[2], R[3] * v[0] + R[4] * v[1] + R[5] * v[2], R[6] * v[0] + R[7] * v[1] + R[8] * v[2]];
  var T3_EYE = new Float64Array([1, 0, 0, 0, 1, 0, 0, 0, 1]);
  function t3Camera(P, pose) {
    const a = (P.azimuth ?? 45) * T3_RAD;
    const e = (P.elevation ?? 30) * T3_RAD;
    const k = P.scale * T3_ROOT;
    const sa = Math.sin(a);
    const ca = Math.cos(a);
    const se = Math.sin(e);
    const ce = Math.cos(e);
    const cam = { m: new Float64Array(6), ox: 0, oy: 0, V: [0, 0, 0], L: [0, 0, 0], k, turn: 0, R: T3_EYE, t: [0, 0, 0], lx: 0, ly: 1, sa, ca, se, ce, origin: P.origin };
    const lw = Math.hypot(sa, ca, 1.2);
    if (pose && pose.R && !(pose.turn !== void 0 && pose.root)) {
      const R = pose.R;
      const t = pose.t ?? [0, 0, 0];
      const r0 = [sa * k, -ca * k, 0];
      const r1 = [ca * se * k, sa * se * k, -ce * k];
      for (let c = 0; c < 3; c++) {
        cam.m[c] = r0[0] * R[c] + r0[1] * R[3 + c] + r0[2] * R[6 + c];
        cam.m[3 + c] = r1[0] * R[c] + r1[1] * R[3 + c] + r1[2] * R[6 + c];
      }
      cam.ox = P.origin[0] + r0[0] * t[0] + r0[1] * t[1] + r0[2] * t[2];
      cam.oy = P.origin[1] + r1[0] * t[0] + r1[1] * t[1] + r1[2] * t[2];
      const V = [ca * ce, sa * ce, se];
      const L = [-sa / lw, ca / lw, 1.2 / lw];
      for (let c = 0; c < 3; c++) {
        cam.V[c] = R[c] * V[0] + R[3 + c] * V[1] + R[6 + c] * V[2];
        cam.L[c] = R[c] * L[0] + R[3 + c] * L[1] + R[6 + c] * L[2];
      }
      cam.R = R;
      cam.t = t;
    } else {
      const turn = pose ? pose.turn ?? 0 : 0;
      const pivot = pose && pose.pivot ? pose.pivot : [0, 0];
      const b = a - turn * T3_RAD;
      const sb = Math.sin(b);
      const cb = Math.cos(b);
      cam.m[0] = sb * k;
      cam.m[1] = -cb * k;
      cam.m[2] = 0;
      cam.m[3] = cb * se * k;
      cam.m[4] = sb * se * k;
      cam.m[5] = -ce * k;
      cam.ox = P.origin[0] + (pivot[0] * sa - pivot[1] * ca) * k;
      cam.oy = P.origin[1] + (pivot[0] * ca + pivot[1] * sa) * se * k;
      cam.V = [cb * ce, sb * ce, se];
      cam.L = [-sb / lw, cb / lw, 1.2 / lw];
      cam.turn = turn;
      const c = Math.cos(turn * T3_RAD);
      const s = Math.sin(turn * T3_RAD);
      cam.R = new Float64Array([c, -s, 0, s, c, 0, 0, 0, 1]);
      cam.t = [pivot[0], pivot[1], 0];
    }
    const lh = Math.hypot(cam.L[0], cam.L[1]) || 1;
    cam.lx = cam.L[0] / lh;
    cam.ly = cam.L[1] / lh;
    return cam;
  }
  function t3Quat(q) {
    const l = Math.hypot(q[0], q[1], q[2], q[3]) || 1;
    const x = q[0] / l;
    const y = q[1] / l;
    const z = q[2] / l;
    const w = q[3] / l;
    return new Float64Array([1 - 2 * (y * y + z * z), 2 * (x * y - z * w), 2 * (x * z + y * w), 2 * (x * y + z * w), 1 - 2 * (x * x + z * z), 2 * (y * z - x * w), 2 * (x * z - y * w), 2 * (y * z + x * w), 1 - 2 * (x * x + y * y)]);
  }
  function t3FreeRot(v) {
    if (v.R) return v.R instanceof Float64Array ? v.R : Float64Array.from(v.R);
    if (v.q) return t3Quat(v.q);
    if (v.axis) return t3Rot(v.axis, v.angle ?? 0);
    return T3_EYE;
  }
  function t3Poses(groups, values) {
    const get = (name) => (values instanceof Map ? values.get(name) : values ? values[name] : void 0) ?? 0;
    const list = [];
    for (let index = 0; index < groups.length; index++) {
      const g = groups[index];
      const v = get(g.name);
      let parent = g.parent === void 0 || g.parent === null || g.parent < 0 ? null : list[g.parent];
      let po = parent ? groups[g.parent].origin : [0, 0, 0];
      let R = T3_EYE;
      let t = [g.origin[0] - po[0], g.origin[1] - po[1], g.origin[2] - po[2]];
      if (g.kind === "turn") R = t3Rot([0, 0, 1], v);
      else if (g.kind === "hinge") R = t3Rot(g.axis, v);
      else if (g.kind === "slide") {
        const d = t3Unit(g.direction);
        t[0] += d[0] * v;
        t[1] += d[1] * v;
        t[2] += d[2] * v;
      } else if (g.kind === "free" && v && typeof v === "object") {
        R = t3FreeRot(v);
        if (v.world) {
          parent = null;
          po = [0, 0, 0];
          t = [g.origin[0], g.origin[1], g.origin[2]];
        }
        if (v.t) {
          t[0] += v.t[0];
          t[1] += v.t[1];
          t[2] += v.t[2];
        }
      }
      if (!parent) {
        const pose = { R, t, value: v };
        if (g.kind === "turn") Object.assign(pose, { turn: v, pivot: [g.origin[0], g.origin[1]], root: true });
        list.push(pose);
        continue;
      }
      const tw = t3Apply(parent.R, t);
      list.push({ R: t3Mul(parent.R, R), t: [tw[0] + parent.t[0], tw[1] + parent.t[1], tw[2] + parent.t[2]], value: v });
    }
    return list;
  }
  function t3PosesMap(groups, values) {
    const list = t3Poses(groups, values);
    return new Map(groups.map((g, index) => [g.name, list[index]]));
  }
  function t3Roles(part) {
    const roles = [];
    const spec = part.spec;
    const details = part.details ?? {};
    const add = (name, type, extra = {}) => roles.push({ name, type, ...extra });
    const tone = part.tone ?? "hi";
    const crease = part.crease ?? "faint";
    const fadedSlots = (prefix, count, cls, lineTone) => {
      for (let j = 0; j < count; j++) add(`${prefix}${j}`, "slot", { cls, tone: lineTone });
    };
    const planes = () => (part.planes ?? []).forEach((_, j) => add(`plane${j}`, "plane"));
    const dots = () => (part.dots ?? []).forEach((dot, j) => add(`c${j}`, "dot", { tone: dot.tone ?? "mid", size: dot.size ?? 0.5 }));
    const sheets = (top) => {
      for (let t = 0; t < 4; t++) add(`s${t}`, "path", { cls: "iso-shade", shade: t });
      if (top) add("s4", "path", { cls: "iso-top" });
    };
    const inner = () => {
      if (details.seams && details.seams.length || details.ribs && details.ribs.seams) add("inner", "path", { cls: "iso-line", tone: "faint" });
    };
    const ribs = () => {
      if (details.ribs) fadedSlots("r", spec.slots?.ribs ?? 6, "iso-line", details.ribs.tone ?? "lo");
    };
    if (part.kind === "prism") {
      add("fill", "path", { cls: "iso-fill" });
      const faces = spec.ring.length / 2 + (spec.up ? 0 : 2);
      for (let j = 0; j < faces; j++) add(`f${j}`, "face");
      if (spec.up) add("top", "xform", { cls: "iso-top" });
      if (crease !== "none") add("crease", "path", { cls: "iso-line iso-crease", tone: crease });
      if (spec.bevel && crease !== "none") fadedSlots("v", spec.slots?.bevel ?? 6, "iso-line iso-bevel", crease);
      if (details.seams && details.seams.length) add("inner", "path", { cls: "iso-line", tone: "faint" });
      planes();
      add("edge", "path", { cls: "iso-line iso-edge", tone });
      dots();
    } else if (part.kind === "round" || part.kind === "lathe") {
      add("fill", "path", { cls: "iso-fill" });
      sheets(true);
      const ends = part.kind === "round" ? spec.ends : spec.caps.map((cap) => cap ? "flat" : "open");
      ends.forEach((end, j) => end === "flat" && add(`k${j}`, "face"));
      if (crease !== "none") add("crease", "path", { cls: "iso-line iso-crease", tone: crease });
      inner();
      ribs();
      planes();
      add("edge", "path", { cls: "iso-line iso-edge", tone });
      dots();
    } else if (part.kind === "ball") {
      add("fill", "path", { cls: "iso-fill" });
      sheets(false);
      spec.flats.forEach((_, j) => add(`f${j}`, "face"));
      if (crease !== "none") add("crease", "path", { cls: "iso-line iso-crease", tone: crease });
      planes();
      add("edge", "path", { cls: "iso-line iso-edge", tone });
      dots();
    } else if (part.kind === "tube") {
      add("body", "path", { cls: "tb-body" });
      if (spec.wide) {
        add("shine", "path", { cls: "tb-shine" });
        add("shade", "path", { cls: "tb-shade" });
      }
      if (spec.rings) fadedSlots("r", spec.slots?.ribs ?? 6, "tb-ring", spec.rings.tone ?? "lo");
      add("edges", "path", { cls: "iso-line tb-edge", tone });
    } else if (part.kind === "fixed") {
      add("move", "self");
      ribs();
      planes();
      dots();
    }
    return roles;
  }
  function t3Planes(list) {
    return (list ?? []).map((plane) => ({ o: plane.o, u: plane.u, v: plane.v, n: plane.n, fade: plane.fade ?? [0.04, 0.3], billboard: Boolean(plane.billboard) }));
  }
  function t3Dots(list) {
    return (list ?? []).map((dot) => ({ p: dot.p, n: dot.n ?? null, size: dot.size ?? 0.5, fade: dot.fade ?? [0.04, 0.42] }));
  }
  function t3PreparePrism(run, part) {
    const spec = part.spec;
    const n = spec.ring.length / 2;
    run.n = n;
    run.up = Boolean(spec.up);
    const ring = Float64Array.from(spec.ring);
    run.ring = ring;
    const nx = new Float64Array(n);
    const ny = new Float64Array(n);
    for (let i = 0; i < n; i++) {
      const j = (i + 1) % n;
      const dx = ring[2 * j] - ring[2 * i];
      const dy = ring[2 * j + 1] - ring[2 * i + 1];
      const l = Math.hypot(dx, dy) || 1;
      nx[i] = dy / l;
      ny[i] = -dx / l;
    }
    run.nx = nx;
    run.ny = ny;
    const F = spec.up ? { o: [0, 0, 0], a: [0, 0, 1], u: [1, 0, 0], v: [0, 1, 0] } : spec.F;
    run.F = F;
    run.s0 = spec.up ? spec.z0 : spec.s0;
    run.s1 = spec.up ? spec.z1 : spec.s1;
    const lo = new Float64Array(3 * n);
    const hi = new Float64Array(3 * n);
    const N3 = new Float64Array(3 * n);
    for (let i = 0; i < n; i++) {
      const x = ring[2 * i];
      const y = ring[2 * i + 1];
      for (let c = 0; c < 3; c++) {
        const base = F.o[c] + F.u[c] * x + F.v[c] * y;
        lo[3 * i + c] = base + F.a[c] * run.s0;
        hi[3 * i + c] = base + F.a[c] * run.s1;
        N3[3 * i + c] = F.u[c] * nx[i] + F.v[c] * ny[i];
      }
    }
    run.lo = lo;
    run.hi = hi;
    run.N3 = N3;
    run.sharp = new Uint8Array(n);
    for (let i = 0; i < n; i++) {
      const p = (i - 1 + n) % n;
      run.sharp[i] = nx[p] * nx[i] + ny[p] * ny[i] < Math.cos(0.35) ? 1 : 0;
    }
    if (spec.bevel) {
      const inset = new Float64Array(2 * n);
      for (let i = 0; i < n; i++) {
        const p = (i - 1 + n) % n;
        const mx = nx[p] + nx[i];
        const my = ny[p] + ny[i];
        const l = Math.hypot(mx, my) || 1;
        inset[2 * i] = ring[2 * i] - mx / l * spec.bevel;
        inset[2 * i + 1] = ring[2 * i + 1] - my / l * spec.bevel;
      }
      run.inset = inset;
    }
    run.seams = part.details && part.details.seams ? part.details.seams.slice() : null;
    run.cut = spec.cuts && spec.cuts.length ? spec.cuts : null;
  }
  function t3Axes(run, part) {
    if (run.kind === "ball") return run.flats.map((flat) => flat.n);
    if (run.kind === "tube") return run.tips.slice();
    if (run.kind === "prism") {
      const out = [run.F.a];
      for (let i = 0; i < run.n; i++) {
        const n = [run.N3[3 * i], run.N3[3 * i + 1], run.N3[3 * i + 2]];
        if (out.every((m) => Math.abs(m[0] * n[0] + m[1] * n[1] + m[2] * n[2]) < 0.9995)) out.push(n);
      }
      return out;
    }
    if (run.F) return [run.F.a];
    if (part.spec && part.spec.F) return [part.spec.F.a];
    return [];
  }
  function t3Cloud(run, part) {
    const out = [];
    const ring = (F, s, r, count) => {
      for (let j = 0; j < count; j++) {
        const c = Math.cos(j / count * T3_TAU);
        const n = Math.sin(j / count * T3_TAU);
        out.push(F.o[0] + F.a[0] * s + r * (c * F.u[0] + n * F.v[0]), F.o[1] + F.a[1] * s + r * (c * F.u[1] + n * F.v[1]), F.o[2] + F.a[2] * s + r * (c * F.u[2] + n * F.v[2]));
      }
    };
    if (run.kind === "prism") {
      for (let i = 0; i < 3 * run.n; i++) out.push(run.lo[i]);
      for (let i = 0; i < 3 * run.n; i++) out.push(run.hi[i]);
    } else if (run.kind === "round") {
      ring(run.F, run.s0, run.r0, 24);
      ring(run.F, run.s1, run.r1, 24);
      for (const [end, s, r] of [[0, run.s0, run.r0], [1, run.s1, run.r1]]) {
        if (run.ends[end] !== "dome") continue;
        const sign = end ? 1 : -1;
        for (const b of [0.5, 1, 1.35]) ring(run.F, s + sign * r * Math.sin(b), r * Math.cos(b), 6);
        out.push(run.F.o[0] + run.F.a[0] * (s + sign * r), run.F.o[1] + run.F.a[1] * (s + sign * r), run.F.o[2] + run.F.a[2] * (s + sign * r));
      }
    } else if (run.kind === "ball") {
      const golden = Math.PI * (3 - Math.sqrt(5));
      for (let i = 0; i < 64; i++) {
        const y = 1 - 2 * (i + 0.5) / 64;
        const rad = Math.sqrt(1 - y * y);
        const w = [Math.cos(golden * i) * rad, Math.sin(golden * i) * rad, y];
        const p = [run.c[0] + run.r * w[0], run.c[1] + run.r * w[1], run.c[2] + run.r * w[2]];
        let inside = true;
        for (const flat of run.flats) if ((p[0] - run.c[0]) * flat.n[0] + (p[1] - run.c[1]) * flat.n[1] + (p[2] - run.c[2]) * flat.n[2] > flat.d + 1e-9) inside = false;
        if (inside) out.push(p[0], p[1], p[2]);
      }
      for (const flat of run.flats)
        for (let j = 0; j < 12; j++) {
          const c = Math.cos(j / 12 * T3_TAU) * flat.rho;
          const n = Math.sin(j / 12 * T3_TAU) * flat.rho;
          out.push(run.c[0] + flat.n[0] * flat.d + c * flat.u[0] + n * flat.v[0], run.c[1] + flat.n[1] * flat.d + c * flat.u[1] + n * flat.v[1], run.c[2] + flat.n[2] * flat.d + c * flat.u[2] + n * flat.v[2]);
        }
    } else if (run.kind === "lathe") {
      const lv = run.levels;
      const step = Math.max(4, Math.floor(lv.length / 4 / 8)) * 4;
      for (let i = 0; i < lv.length; i += step) ring(run.F, lv[i], lv[i + 1], 8);
      ring(run.F, lv[lv.length - 4], lv[lv.length - 3], 8);
    } else if (run.kind === "tube") {
      const b = run.body;
      const stride = Math.max(1, Math.floor(b.count / 8));
      for (let i = 0; i < b.count; i += stride) {
        const T = t3Unit([b.D3[3 * i], b.D3[3 * i + 1], b.D3[3 * i + 2]]);
        const [u, v] = t3Basis(T);
        ring({ o: [b.P3[3 * i], b.P3[3 * i + 1], b.P3[3 * i + 2]], a: T, u, v }, 0, run.r, 8);
      }
    } else if (part.cloud) for (const v of part.cloud) out.push(v);
    return Float64Array.from(out);
  }
  function t3Unpack(value, grouped) {
    if (!value) return new Float64Array(0);
    if (typeof value !== "string") return Float64Array.from(value);
    const text = atob(value);
    const bytes = new Uint8Array(text.length);
    for (let i = 0; i < text.length; i++) bytes[i] = text.charCodeAt(i);
    const view = new DataView(bytes.buffer);
    const size = grouped ? 10 : 8;
    const stride = grouped ? 6 : 5;
    const count = bytes.length / size;
    const out = new Float64Array(count * stride);
    for (let e = 0; e < count; e++) {
      let o = e * size;
      const at = e * stride;
      out[at] = view.getUint16(o);
      out[at + 1] = view.getUint16(o + 2);
      o += 4;
      if (grouped) {
        out[at + 2] = view.getUint16(o) - 1;
        o += 2;
      }
      let x = view.getUint16(o) / 65535 * 2 - 1;
      let y = view.getUint16(o + 2) / 65535 * 2 - 1;
      const z = 1 - Math.abs(x) - Math.abs(y);
      if (z < 0) {
        const ox = (1 - Math.abs(y)) * (x >= 0 ? 1 : -1);
        const oy = (1 - Math.abs(x)) * (y >= 0 ? 1 : -1);
        x = ox;
        y = oy;
      }
      const l = Math.hypot(x, y, z) || 1;
      out[at + stride - 3] = x / l;
      out[at + stride - 2] = y / l;
      out[at + stride - 1] = z / l;
    }
    return out;
  }
  function t3Prepare(data, { unit = 1 } = {}) {
    const P = data.P;
    const runs = data.parts.map((part, index) => {
      const run = { index, name: part.name, kind: part.kind, group: part.group ?? -1, layer: part.layer, part, roles: t3Roles(part), planes: t3Planes(part.planes), dots: t3Dots(part.dots), unit };
      run.role = Object.fromEntries(run.roles.map((role, j) => [role.name, j]));
      if (part.kind === "prism") t3PreparePrism(run, part);
      else if (part.kind === "round") t3PrepareRound(run, part, P, unit);
      else if (part.kind === "ball") t3PrepareBall(run, part, P, unit);
      else if (part.kind === "lathe") t3PrepareLathe(run, part, P, unit);
      else if (part.kind === "tube") t3PrepareTube(run, part, data);
      else if (part.kind === "fixed") {
        run.anchor = part.spec.anchor;
        run.home = part.spec.home;
        run.box0 = part.spec.box;
        run.hull0 = Float64Array.from(part.spec.hull);
        run.F = part.spec.F ?? null;
        run.ribs = part.details && part.details.ribs ? part.details.ribs : null;
      }
      run.slots = part.spec.slots ?? {};
      run.cloud = t3Cloud(run, part);
      run.axes = t3Axes(run, part);
      const cn = run.cloud.length / 3;
      run.centroid = [0, 0, 0];
      for (let i = 0; i < cn; i++) for (let c = 0; c < 3; c++) run.centroid[c] += run.cloud[3 * i + c] / Math.max(1, cn);
      return run;
    });
    const layers = data.layers.map((layer, index) => {
      const parts = Int32Array.from(layer.parts);
      const local = /* @__PURE__ */ new Map();
      parts.forEach((global, at) => local.set(global, at));
      const planar = t3Unpack(data.planes && data.planes[layer.name], false);
      const dynamic = Int32Array.from((data.dynamic && data.dynamic[layer.name]) ?? []);
      const free2 = Int32Array.from((data.free && data.free[layer.name]) ?? []);
      const framed = t3Unpack(data.framed && data.framed[layer.name], true);
      const groupPairs = [];
      const raw = (data.groupPairs && data.groupPairs[layer.name]) ?? [];
      const members = /* @__PURE__ */ new Map();
      for (const global of parts) {
        const g = runs[global].group;
        if (!members.has(g)) members.set(g, []);
        members.get(g).push(global);
      }
      for (let p = 0; p < raw.length; p += 6) groupPairs.push({ a: Int32Array.from(members.get(raw[p]) ?? []), b: Int32Array.from(members.get(raw[p + 1]) ?? []), frame: raw[p + 2], n: [raw[p + 3], raw[p + 4], raw[p + 5]], boxA: new Float64Array(4), boxB: new Float64Array(4) });
      const looseAt = new Uint8Array(parts.length);
      for (const global of free2) looseAt[local.get(global)] = 1;
      return { index, name: layer.name, parts, local, rest: Int32Array.from(layer.rest ?? layer.parts), planar, framed, groupPairs, dynamic, free: free2, looseAt, warm: /* @__PURE__ */ new Map() };
    });
    return { P, data, unit, groups: data.groups, runs, layers };
  }
  function t3Frame(run) {
    const count = run.roles.length;
    return { d: new Array(count).fill(""), q: new Int32Array(count), w: new Float64Array(count).fill(-1), t: new Array(count).fill(""), o: new Float64Array(count).fill(1), box: new Float64Array(4), hull: new Float64Array(64), hullN: 0, cx: new Float64Array(count), cy: new Float64Array(count), quads: null, quadN: 0 };
  }
  var t3Buf = { a: new Float64Array(1024), b: new Float64Array(1024), c: new Float64Array(1024) };
  function t3Scratch(name, size) {
    if (t3Buf[name].length < size) t3Buf[name] = new Float64Array(size * 2);
    return t3Buf[name];
  }
  function t3SetHull(f, buf, count) {
    const hull = t3Grow(f, "hull", 2 * count, Float64Array);
    for (let i = 0; i < 2 * count; i++) hull[i] = buf[i];
    f.hullN = count;
  }
  function t3Faded(f, run, prefix, lines, count) {
    if (!f.fade) f.fade = {};
    const detail = t3State.detail;
    if (detail < 1) for (let i = 0; i < count; i++) lines.alpha[i] *= detail;
    if (detail < 0.01) count = 0;
    f.fade[prefix] = { key: lines.key.slice(0, count), alpha: lines.alpha.slice(0, count) };
    const slots = run.slots[prefix === "v" ? "bevel" : "ribs"] ?? 6;
    const levels = run._levels ?? (run._levels = new Array(T3_LEVELS + 1));
    for (let l = 0; l <= T3_LEVELS; l++) levels[l] = "";
    for (let i = 0; i < count; i++) {
      const alpha = lines.alpha[i];
      const level = Math.min(T3_LEVELS, Math.round(alpha * T3_LEVELS));
      if (level <= 0) continue;
      levels[level] += lines.d[i];
    }
    const present = [];
    for (let l = T3_LEVELS; l >= 1; l--) if (levels[l]) present.push([l, levels[l]]);
    while (present.length > slots) {
      let best = 1;
      let gap = Infinity;
      for (let i = 1; i < present.length; i++) {
        const g = present[i - 1][0] - present[i][0];
        if (g < gap) {
          gap = g;
          best = i;
        }
      }
      const [a, da] = present[best - 1];
      const [b, db] = present[best];
      present.splice(best - 1, 2, [(a + b) / 2, da + db]);
    }
    for (let j = 0; j < slots; j++) {
      const role = run.role[`${prefix}${j}`];
      if (role === void 0) continue;
      if (j < present.length) {
        f.d[role] = present[j][1];
        f.o[role] = present[j][0] / T3_LEVELS;
      } else {
        f.d[role] = "";
        f.o[role] = 0;
      }
    }
    return present.length;
  }
  var t3Lines = { d: [], alpha: [], key: [] };
  var t3None = { d: [], alpha: [], key: [] };
  function t3EmitPrism(run, cam, f) {
    const n = run.n;
    const m = cam.m;
    const ox = cam.ox;
    const oy = cam.oy;
    const V = cam.V;
    const L = cam.L;
    const lo = run.lo;
    const hi = run.hi;
    const N3 = run.N3;
    const bot = t3Scratch("a", 2 * n);
    const top = t3Scratch("b", 2 * n);
    for (let i = 0; i < n; i++) {
      const a = 3 * i;
      bot[2 * i] = ox + m[0] * lo[a] + m[1] * lo[a + 1] + m[2] * lo[a + 2];
      bot[2 * i + 1] = oy + m[3] * lo[a] + m[4] * lo[a + 1] + m[5] * lo[a + 2];
      top[2 * i] = ox + m[0] * hi[a] + m[1] * hi[a + 1] + m[2] * hi[a + 2];
      top[2 * i + 1] = oy + m[3] * hi[a] + m[4] * hi[a + 1] + m[5] * hi[a + 2];
    }
    const F = run.F;
    const aV = F.a[0] * V[0] + F.a[1] * V[1] + F.a[2] * V[2];
    const near = aV >= 0 ? top : bot;
    const far = aV >= 0 ? bot : top;
    const facing = run._facing ?? (run._facing = new Float64Array(n));
    for (let i = 0; i < n; i++) facing[i] = N3[3 * i] * V[0] + N3[3 * i + 1] * V[1] + N3[3 * i + 2] * V[2];
    const on = (i) => facing[(i % n + n) % n] > 1e-9;
    let i0 = -1;
    for (let i = 0; i < n; i++)
      if (on(i) && !on(i - 1)) {
        i0 = i;
        break;
      }
    const sil = t3Scratch("c", 4 * n + 8);
    const silAt = run._silAt ?? (run._silAt = new Int32Array(2 * n + 4));
    let count = 0;
    let i1 = i0;
    const nearSet = aV >= 0 ? hi : lo;
    const farSet = aV >= 0 ? lo : hi;
    if (i0 < 0) {
      for (let i = 0; i < n; i++) {
        sil[2 * count] = near[2 * i];
        sil[2 * count + 1] = near[2 * i + 1];
        silAt[count] = i;
        count++;
      }
    } else {
      while (on(i1)) i1++;
      for (let j = i0; j <= i1; j++) {
        const i = j % n;
        sil[2 * count] = far[2 * i];
        sil[2 * count + 1] = far[2 * i + 1];
        silAt[count] = -1 - i;
        count++;
      }
      for (let j = i1; j <= i0 + n; j++) {
        const i = j % n;
        sil[2 * count] = near[2 * i];
        sil[2 * count + 1] = near[2 * i + 1];
        silAt[count] = i;
        count++;
      }
      if (count > 2 && Math.abs(sil[0] - sil[2 * count - 2]) < 1e-9 && Math.abs(sil[1] - sil[2 * count - 1]) < 1e-9) count--;
    }
    const outline = t3Path(sil, count, true);
    f.d[run.role.fill] = outline;
    if (run.cut) {
      const inPlane = (index) => {
        const at = silAt[index];
        const set = at < 0 ? farSet : nearSet;
        const v = at < 0 ? -1 - at : at;
        return run.cut.some((cut2) => Math.abs(cut2.n[0] * set[3 * v] + cut2.n[1] * set[3 * v + 1] + cut2.n[2] * set[3 * v + 2] - cut2.d) < 1e-3);
      };
      const flags = new Uint8Array(count);
      const onSame = (i, j) => {
        const at = (index) => {
          const a = silAt[index];
          const set = a < 0 ? farSet : nearSet;
          const v = a < 0 ? -1 - a : a;
          return [set[3 * v], set[3 * v + 1], set[3 * v + 2]];
        };
        const p = at(i);
        const q = at(j);
        return run.cut.some((cut2) => Math.abs(cut2.n[0] * p[0] + cut2.n[1] * p[1] + cut2.n[2] * p[2] - cut2.d) < 1e-3 && Math.abs(cut2.n[0] * q[0] + cut2.n[1] * q[1] + cut2.n[2] * q[2] - cut2.d) < 1e-3);
      };
      for (let j = 0; j < count; j++) flags[j] = inPlane(j) && onSame(j, (j + 1) % count) ? 1 : 0;
      f.d[run.role.edge] = t3Broken(sil, count, flags);
    } else f.d[run.role.edge] = outline;
    t3Box(sil, count, f.box);
    t3SetHull(f, sil, count);
    const quad = new Float64Array(8);
    for (let i = 0; i < n; i++) {
      const role = run.role[`f${i}`];
      if (!(facing[i] > 1e-6)) {
        f.d[role] = "";
        continue;
      }
      const j = (i + 1) % n;
      quad[0] = top[2 * i];
      quad[1] = top[2 * i + 1];
      quad[2] = top[2 * j];
      quad[3] = top[2 * j + 1];
      quad[4] = bot[2 * j];
      quad[5] = bot[2 * j + 1];
      quad[6] = bot[2 * i];
      quad[7] = bot[2 * i + 1];
      f.d[role] = t3Path(quad, 4, true);
      let score;
      if (run.up) {
        score = (run.nx[i] * cam.lx + run.ny[i] * cam.ly + 1) / 2;
        f.q[role] = t3Level(score, T3_EB);
      } else {
        score = N3[3 * i] * L[0] + N3[3 * i + 1] * L[1] + N3[3 * i + 2] * L[2];
        f.q[role] = t3Level(score, T3_LB);
      }
      const e1 = Math.hypot(quad[2] - quad[0], quad[3] - quad[1]);
      const e2 = Math.hypot(quad[6] - quad[0], quad[7] - quad[1]);
      const area = Math.abs((quad[2] - quad[0]) * (quad[7] - quad[1]) - (quad[3] - quad[1]) * (quad[6] - quad[0]));
      const wide = area / (Math.max(e1, e2) || 1);
      f.w[role] = wide < 0.4 ? Math.round(wide * 100) / 100 : -1;
    }
    if (run.up) {
      const z = run.s1;
      f.t[run.role.top] = `matrix(${t3Fix(m[0], 1e5)} ${t3Fix(m[3], 1e5)} ${t3Fix(m[1], 1e5)} ${t3Fix(m[4], 1e5)} ${t3Fix(ox + m[2] * z, 100)} ${t3Fix(oy + m[5] * z, 100)})`;
    } else {
      for (let side = 0; side < 2; side++) {
        const role = run.role[`f${n + side}`];
        const sign = side ? 1 : -1;
        const face = sign * aV;
        if (!(face > 1e-6)) {
          f.d[role] = "";
          continue;
        }
        const ring = side ? top : bot;
        f.d[role] = t3Path(ring, n, true);
        f.q[role] = t3Level(sign * (F.a[0] * L[0] + F.a[1] * L[1] + F.a[2] * L[2]), T3_LB);
        let minor = Infinity;
        let x0 = Infinity;
        let x1 = -Infinity;
        for (let i = 0; i < n; i++) {
          const j = (i + 1) % n;
          const ex = ring[2 * j] - ring[2 * i];
          const ey = ring[2 * j + 1] - ring[2 * i + 1];
          const l = Math.hypot(ex, ey);
          if (l < 1e-9) continue;
          let lo2 = Infinity;
          let hi2 = -Infinity;
          for (let q = 0; q < n; q++) {
            const v = ((ring[2 * q] - ring[2 * i]) * ey - (ring[2 * q + 1] - ring[2 * i + 1]) * ex) / l;
            if (v < lo2) lo2 = v;
            if (v > hi2) hi2 = v;
          }
          minor = Math.min(minor, hi2 - lo2);
          x0 = Math.min(x0, lo2);
          x1 = Math.max(x1, hi2);
        }
        f.w[role] = minor < 0.4 ? Math.round(minor * 100) / 100 : -1;
      }
    }
    if (run.role.crease !== void 0) {
      let crease = "";
      if (run.up) {
        if (i0 >= 0) {
          const buf = t3Scratch("a", 0);
          let c = 0;
          const rim = t3Scratch("c", 2 * n + 4);
          for (let j = i0; j <= i1; j++) {
            const i = j % n;
            rim[2 * c] = top[2 * i];
            rim[2 * c + 1] = top[2 * i + 1];
            c++;
          }
          crease = t3Path(rim, c, false);
          void buf;
        }
      } else {
        const capOn = [-aV > 1e-6, aV > 1e-6];
        const seg = new Float64Array(4);
        for (let i = 0; i < n; i++) {
          const p = (i - 1 + n) % n;
          if (run.sharp[i] && facing[i] > 1e-6 && facing[p] > 1e-6) {
            seg[0] = bot[2 * i];
            seg[1] = bot[2 * i + 1];
            seg[2] = top[2 * i];
            seg[3] = top[2 * i + 1];
            crease += t3Path(seg, 2, false);
          }
        }
        for (let side = 0; side < 2; side++) {
          if (!capOn[side] || i0 < 0) continue;
          const ring = side ? top : bot;
          const rim = t3Scratch("c", 2 * n + 4);
          let c = 0;
          for (let j = i0; j <= i1; j++) {
            const i = j % n;
            rim[2 * c] = ring[2 * i];
            rim[2 * c + 1] = ring[2 * i + 1];
            c++;
          }
          crease += t3Path(rim, c, false);
        }
      }
      f.d[run.role.crease] = crease;
    }
    if (run.inset && run.role.v0 !== void 0 && t3State.detail < 0.01) f.levels = t3Faded(f, run, "v", t3None, 0);
    else if (run.inset && run.role.v0 !== void 0) {
      const lines = t3Lines;
      lines.d.length = 0;
      lines.alpha.length = 0;
      lines.key.length = 0;
      lines.key.length = 0;
      const capSide = aV >= 0 ? 1 : 0;
      const s = capSide ? run.s1 : run.s0;
      const capAlpha = run.up ? 1 : t3Step(0.02, 0.2, Math.abs(aV));
      const ins = t3Scratch("c", 2 * n);
      for (let i = 0; i < n; i++) {
        const x = run.inset[2 * i];
        const y = run.inset[2 * i + 1];
        const px = F.o[0] + F.a[0] * s + F.u[0] * x + F.v[0] * y;
        const py = F.o[1] + F.a[1] * s + F.u[1] * x + F.v[1] * y;
        const pz = F.o[2] + F.a[2] * s + F.u[2] * x + F.v[2] * y;
        ins[2 * i] = ox + m[0] * px + m[1] * py + m[2] * pz;
        ins[2 * i + 1] = oy + m[3] * px + m[4] * py + m[5] * pz;
      }
      const rim = capSide ? top : bot;
      const seg = new Float64Array(4);
      for (let i = 0; i < n; i++) {
        const p = (i - 1 + n) % n;
        const ai = capAlpha * t3Step(0, 0.14, facing[i]);
        const ap = capAlpha * t3Step(0, 0.14, facing[p]);
        if (ai > 0.01) {
          const j = (i + 1) % n;
          seg[0] = ins[2 * i];
          seg[1] = ins[2 * i + 1];
          seg[2] = ins[2 * j];
          seg[3] = ins[2 * j + 1];
          lines.d.push(t3Path(seg, 2, false));
          lines.alpha.push(ai);
          lines.key.push(2 * i);
        }
        const corner = ai * (1 - ap) + ap * (1 - ai);
        if (corner > 0.01) {
          seg[0] = ins[2 * i];
          seg[1] = ins[2 * i + 1];
          seg[2] = rim[2 * i];
          seg[3] = rim[2 * i + 1];
          lines.d.push(t3Path(seg, 2, false));
          lines.alpha.push(corner);
          lines.key.push(2 * i + 1);
        }
      }
      f.levels = t3Faded(f, run, "v", lines, lines.d.length);
    }
    if (run.seams && run.role.inner !== void 0) {
      let inner = "";
      if (i0 >= 0) {
        const rim = t3Scratch("c", 2 * n + 4);
        for (const s of run.seams) {
          let c = 0;
          for (let j = i0; j <= i1; j++) {
            const i = j % n;
            const x = run.ring[2 * i];
            const y = run.ring[2 * i + 1];
            const px = F.o[0] + F.a[0] * s + F.u[0] * x + F.v[0] * y;
            const py = F.o[1] + F.a[1] * s + F.u[1] * x + F.v[1] * y;
            const pz = F.o[2] + F.a[2] * s + F.u[2] * x + F.v[2] * y;
            rim[2 * c] = ox + m[0] * px + m[1] * py + m[2] * pz;
            rim[2 * c + 1] = oy + m[3] * px + m[4] * py + m[5] * pz;
            c++;
          }
          inner += t3Path(rim, c, false);
        }
      }
      f.d[run.role.inner] = inner;
    }
  }
  function t3Broken(buf, count, skip) {
    let start = -1;
    for (let j = 0; j < count; j++)
      if (skip[(j - 1 + count) % count] && !skip[j]) {
        start = j;
        break;
      }
    if (start < 0) return skip[0] ? "" : t3Path(buf, count, true);
    let out = "";
    let run = [];
    for (let step = 0; step < count; step++) {
      const j = (start + step) % count;
      if (skip[j]) {
        if (run.length) {
          run.push((j + 0) % count);
          out += t3PathOf(run.map((i) => [buf[2 * i], buf[2 * i + 1]]), false);
          run = [];
        }
        continue;
      }
      run.push(j);
    }
    if (run.length) {
      run.push((start + count) % count);
      out += t3PathOf(run.map((i) => [buf[2 * i], buf[2 * i + 1]]), false);
    }
    return out;
  }
  function t3EmitPlanes(run, cam, f, sx = 0, sy = 0) {
    const m = cam.m;
    const V = cam.V;
    for (let j = 0; j < run.planes.length; j++) {
      const plane = run.planes[j];
      const role = run.role[`plane${j}`];
      const o = plane.o;
      const X = cam.ox - sx + m[0] * o[0] + m[1] * o[1] + m[2] * o[2];
      const Y = cam.oy - sy + m[3] * o[0] + m[4] * o[1] + m[5] * o[2];
      const facing = plane.n[0] * V[0] + plane.n[1] * V[1] + plane.n[2] * V[2];
      const alpha = Math.round(t3Step(plane.fade[0], plane.fade[1], facing) * 100) / 100;
      f.o[role] = alpha;
      if (plane.billboard) {
        f.t[role] = `translate(${t3Num(X)} ${t3Num(Y)})`;
        continue;
      }
      const u = plane.u;
      const v = plane.v;
      const a = m[0] * u[0] + m[1] * u[1] + m[2] * u[2];
      const b = m[3] * u[0] + m[4] * u[1] + m[5] * u[2];
      const c = m[0] * v[0] + m[1] * v[1] + m[2] * v[2];
      const d = m[3] * v[0] + m[4] * v[1] + m[5] * v[2];
      f.t[role] = `matrix(${t3Fix(a, 1e5)} ${t3Fix(b, 1e5)} ${t3Fix(c, 1e5)} ${t3Fix(d, 1e5)} ${t3Fix(X, 100)} ${t3Fix(Y, 100)})`;
    }
  }
  function t3EmitDots(run, cam, f, sx = 0, sy = 0) {
    const m = cam.m;
    const V = cam.V;
    for (let j = 0; j < run.dots.length; j++) {
      const dot = run.dots[j];
      const role = run.role[`c${j}`];
      const p = dot.p;
      f.cx[role] = cam.ox - sx + m[0] * p[0] + m[1] * p[1] + m[2] * p[2];
      f.cy[role] = cam.oy - sy + m[3] * p[0] + m[4] * p[1] + m[5] * p[2];
      const alpha = (dot.n ? t3Step(dot.fade[0], dot.fade[1], dot.n[0] * V[0] + dot.n[1] * V[1] + dot.n[2] * V[2]) : 1) * t3State.detail;
      f.o[role] = alpha < 5e-3 ? 0 : Math.round(alpha * 100) / 100;
    }
  }
  function t3EmitFixed(run, cam, f) {
    const a = run.anchor;
    const m = cam.m;
    const X = cam.ox + m[0] * a[0] + m[1] * a[1] + m[2] * a[2];
    const Y = cam.oy + m[3] * a[0] + m[4] * a[1] + m[5] * a[2];
    const dx = X - run.home[0];
    const dy = Y - run.home[1];
    const rx = Math.round(dx * 100) / 100;
    const ry = Math.round(dy * 100) / 100;
    f.t[run.role.move] = rx || ry ? `translate(${t3Num(rx)} ${t3Num(ry)})` : "";
    f.shiftX = rx;
    f.shiftY = ry;
    const b = run.box0;
    f.box[0] = b[0] + rx;
    f.box[1] = b[1] + ry;
    f.box[2] = b[2] + rx;
    f.box[3] = b[3] + ry;
    const count = run.hull0.length / 2;
    const hull = t3Grow(f, "hull", 2 * count, Float64Array);
    for (let i = 0; i < count; i++) {
      hull[2 * i] = run.hull0[2 * i] + rx;
      hull[2 * i + 1] = run.hull0[2 * i + 1] + ry;
    }
    f.hullN = count;
    if (run.ribs && run.F) t3EmitRibs(run, cam, f, run.F, run.ribs, rx, ry);
    t3EmitPlanes(run, cam, f, rx, ry);
    t3EmitDots(run, cam, f, rx, ry);
  }
  function t3EmitRibs(run, cam, f, F, ribs, sx, sy) {
    if (t3State.detail < 0.01) {
      f.levels = t3Faded(f, run, "r", t3None, 0);
      return;
    }
    const m = cam.m;
    const V = cam.V;
    const lines = t3Lines;
    lines.d.length = 0;
    lines.alpha.length = 0;
    lines.key.length = 0;
    const { s0, s1, count, phase = 0, twist = 0, fade = [0.1, 0.55] } = ribs;
    const r0 = ribs.r0 ?? ribs.r;
    const r1 = ribs.r1 ?? r0;
    const slope = (r1 - r0) / (s1 - s0 || 1);
    const norm = Math.hypot(1, slope);
    const aV = F.a[0] * V[0] + F.a[1] * V[1] + F.a[2] * V[2];
    const uV = F.u[0] * V[0] + F.u[1] * V[1] + F.u[2] * V[2];
    const vV = F.v[0] * V[0] + F.v[1] * V[1] + F.v[2] * V[2];
    const seg = new Float64Array(4);
    const at = (s, r, t, out, index) => {
      const c = Math.cos(t);
      const n = Math.sin(t);
      const px = F.o[0] + F.a[0] * s + r * (c * F.u[0] + n * F.v[0]);
      const py = F.o[1] + F.a[1] * s + r * (c * F.u[1] + n * F.v[1]);
      const pz = F.o[2] + F.a[2] * s + r * (c * F.u[2] + n * F.v[2]);
      out[index] = cam.ox - sx + m[0] * px + m[1] * py + m[2] * pz;
      out[index + 1] = cam.oy - sy + m[3] * px + m[4] * py + m[5] * pz;
    };
    for (let i = 0; i < count; i++) {
      const t = phase + i / count * T3_TAU;
      const tm = t + twist / 2;
      const facing = (Math.cos(tm) * uV + Math.sin(tm) * vV - slope * aV) / norm;
      const alpha = t3Step(fade[0], fade[1], facing);
      if (alpha * T3_LEVELS < 0.5) continue;
      at(s0, r0, t, seg, 0);
      at(s1, r1, t + twist, seg, 2);
      lines.d.push(t3Path(seg, 2, false));
      lines.alpha.push(alpha);
      lines.key.push(i);
    }
    f.levels = t3Faded(f, run, "r", lines, lines.d.length);
  }
  function t3Geo(F, cam) {
    const m = cam.m;
    const V = cam.V;
    const L = cam.L;
    const dot = (a, b) => a[0] * b[0] + a[1] * b[1] + a[2] * b[2];
    const lin = (w) => [m[0] * w[0] + m[1] * w[1] + m[2] * w[2], m[3] * w[0] + m[4] * w[1] + m[5] * w[2]];
    const O = [cam.ox + m[0] * F.o[0] + m[1] * F.o[1] + m[2] * F.o[2], cam.oy + m[3] * F.o[0] + m[4] * F.o[1] + m[5] * F.o[2]];
    const aV = dot(F.a, V);
    const uV = dot(F.u, V);
    const vV = dot(F.v, V);
    const aL = dot(F.a, L);
    const uL = dot(F.u, L);
    const vL = dot(F.v, L);
    return { O, SA: lin(F.a), SU: lin(F.u), SV: lin(F.v), aV, aL, view: { a: aV, flat: Math.hypot(uV, vV), phi: Math.atan2(vV, uV) }, light: { a: aL, flat: Math.hypot(uL, vL), phi: Math.atan2(vL, uL) } };
  }
  function t3At(geo, s, r, t, buf, index) {
    const c = Math.cos(t);
    const n = Math.sin(t);
    buf[index] = geo.O[0] + s * geo.SA[0] + r * (c * geo.SU[0] + n * geo.SV[0]);
    buf[index + 1] = geo.O[1] + s * geo.SA[1] + r * (c * geo.SU[1] + n * geo.SV[1]);
  }
  function t3Arcs(nr, na, view, light) {
    const cuts = [];
    if (Math.abs(nr) > 1e-9) {
      const visibleCut = -(na * view.a) / (nr * view.flat);
      if (visibleCut > -1 && visibleCut < 1) {
        const d = Math.acos(visibleCut);
        cuts.push(view.phi - d, view.phi + d);
      }
      for (let b = 0; b < T3_LB.length; b++) {
        const c = (T3_LB[b] - na * light.a) / (nr * light.flat);
        if (c > -1 && c < 1) {
          const d = Math.acos(c);
          cuts.push(light.phi - d, light.phi + d);
        }
      }
    }
    for (let i = 0; i < cuts.length; i++) {
      const w = (cuts[i] % T3_TAU + T3_TAU) % T3_TAU;
      cuts[i] = Math.round(w * 1e9) / 1e9;
    }
    cuts.sort((a, b) => a - b);
    const sorted = [];
    for (let i = 0; i < cuts.length; i++) if (!sorted.length || cuts[i] !== sorted[sorted.length - 1]) sorted.push(cuts[i]);
    const label = (angle) => {
      const facing = nr * view.flat * Math.cos(angle - view.phi) + na * view.a;
      if (facing <= 1e-9) return -1;
      const score = nr * light.flat * Math.cos(angle - light.phi) + na * light.a;
      let tone = 0;
      while (tone < T3_LB.length && score >= T3_LB[tone]) tone++;
      return tone;
    };
    if (!sorted.length) {
      const tone = label(0);
      return tone < 0 ? [] : [{ tone, from: 0, to: T3_TAU, full: true }];
    }
    const merged = [];
    for (let index = 0; index < sorted.length; index++) {
      const from = sorted[index];
      const to = index + 1 < sorted.length ? sorted[index + 1] : sorted[0] + T3_TAU;
      const tone = label((from + to) / 2);
      const last = merged[merged.length - 1];
      if (last && last.tone === tone && Math.abs(last.to - from) < 1e-9) last.to = to;
      else merged.push({ tone, from, to });
    }
    if (merged.length > 1 && merged[0].tone === merged[merged.length - 1].tone && Math.abs(merged[merged.length - 1].to - T3_TAU - merged[0].from) < 1e-9) {
      const last = merged.pop();
      merged[0].from = last.from - T3_TAU;
    }
    const out = [];
    for (const arc of merged) if (arc.tone >= 0) out.push(arc);
    return out;
  }
  function t3Strip(geo, s0, r0, s1, r1, from, to, step) {
    const count = Math.max(1, Math.ceil((to - from) / step));
    const buf = t3Scratch("c", 4 * count + 8);
    for (let j = 0; j <= count; j++) {
      const t = from + (to - from) * j / count;
      t3At(geo, s0, r0, t, buf, 2 * j);
      t3At(geo, s1, r1, t, buf, 2 * (2 * count + 1 - j));
    }
    return t3Path(t3Oriented(buf, 2 * count + 2), 2 * count + 2, true);
  }
  function t3Oriented(buf, count) {
    let area = 0;
    for (let i = 0; i < count; i++) {
      const j = (i + 1) % count;
      area += buf[2 * i] * buf[2 * j + 1] - buf[2 * j] * buf[2 * i + 1];
    }
    if (area >= 0) return buf;
    for (let i = 0, j = count - 1; i < j; i++, j--) {
      const x = buf[2 * i];
      const y = buf[2 * i + 1];
      buf[2 * i] = buf[2 * j];
      buf[2 * i + 1] = buf[2 * j + 1];
      buf[2 * j] = x;
      buf[2 * j + 1] = y;
    }
    return buf;
  }
  function t3Hull(points) {
    const sorted = points.slice().sort((a, b) => a[0] - b[0] || a[1] - b[1]);
    if (sorted.length < 3) return sorted;
    const cross = (o, a, b) => (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0]);
    const lower = [];
    for (const p of sorted) {
      while (lower.length >= 2 && cross(lower[lower.length - 2], lower[lower.length - 1], p) <= 1e-12) lower.pop();
      lower.push(p);
    }
    const upper = [];
    for (let i = sorted.length - 1; i >= 0; i--) {
      const p = sorted[i];
      while (upper.length >= 2 && cross(upper[upper.length - 2], upper[upper.length - 1], p) <= 1e-12) upper.pop();
      upper.push(p);
    }
    return lower.slice(0, -1).concat(upper.slice(0, -1));
  }
  function t3PathOf(points, closed) {
    if (points.length < 2) return "";
    let s = "M" + t3Num(points[0][0]) + " " + t3Num(points[0][1]);
    for (let i = 1; i < points.length; i++) s += "L" + t3Num(points[i][0]) + " " + t3Num(points[i][1]);
    return closed ? s + "Z" : s;
  }
  function t3Basis(w) {
    const helper = Math.abs(w[2]) > 0.9 ? [1, 0, 0] : [0, 0, 1];
    const u = t3Unit([helper[1] * w[2] - helper[2] * w[1], helper[2] * w[0] - helper[0] * w[2], helper[0] * w[1] - helper[1] * w[0]]);
    return [u, [w[1] * u[2] - w[2] * u[1], w[2] * u[0] - w[0] * u[2], w[0] * u[1] - w[1] * u[0]]];
  }
  function t3Meet(A, a, B, b) {
    const ab = A[0] * B[0] + A[1] * B[1] + A[2] * B[2];
    const det = 1 - ab * ab;
    if (det < 1e-12) return [];
    const alpha = (a - b * ab) / det;
    const beta = (b - a * ab) / det;
    const base = [A[0] * alpha + B[0] * beta, A[1] * alpha + B[1] * beta, A[2] * alpha + B[2] * beta];
    const rest = 1 - (base[0] * base[0] + base[1] * base[1] + base[2] * base[2]);
    if (rest < 0) return [];
    const cr = [A[1] * B[2] - A[2] * B[1], A[2] * B[0] - A[0] * B[2], A[0] * B[1] - A[1] * B[0]];
    const k = Math.sqrt(rest / det);
    return [
      [base[0] + cr[0] * k, base[1] + cr[1] * k, base[2] + cr[2] * k],
      [base[0] - cr[0] * k, base[1] - cr[1] * k, base[2] - cr[2] * k]
    ];
  }
  var t3Tables = /* @__PURE__ */ new Map();
  function t3Table(count) {
    let table = t3Tables.get(count);
    if (!table) {
      table = new Float64Array(2 * count);
      for (let j = 0; j < count; j++) {
        table[2 * j] = Math.cos(j / count * T3_TAU);
        table[2 * j + 1] = Math.sin(j / count * T3_TAU);
      }
      t3Tables.set(count, table);
    }
    return table;
  }
  function t3Dome(cam, C, e, r, count, sheets) {
    const m = cam.m;
    const V = cam.V;
    const L = cam.L;
    const Sx = cam.ox + m[0] * C[0] + m[1] * C[1] + m[2] * C[2];
    const Sy = cam.oy + m[3] * C[0] + m[4] * C[1] + m[5] * C[2];
    const flat = (n) => [Sx + r * (m[0] * n[0] + m[1] * n[1] + m[2] * n[2]), Sy + r * (m[3] * n[0] + m[4] * n[1] + m[5] * n[2])];
    const dot = (a, b) => a[0] * b[0] + a[1] * b[1] + a[2] * b[2];
    const table = t3Table(count);
    const circle = (W, value, keep) => {
      const [U, Q] = t3Basis(W);
      const rad = Math.sqrt(Math.max(0, 1 - value * value));
      const out = [];
      for (let j = 0; j < count; j++) {
        const cs = table[2 * j] * rad;
        const sn = table[2 * j + 1] * rad;
        const n = [W[0] * value + U[0] * cs + Q[0] * sn, W[1] * value + U[1] * cs + Q[1] * sn, W[2] * value + U[2] * cs + Q[2] * sn];
        if (keep(n)) out.push(n);
      }
      return out;
    };
    const rim = circle(V, 0, (n) => dot(n, e) >= -1e-9).map((n) => [flat(n), dot(n, L)]);
    const base = circle(e, 0, (n) => dot(n, V) >= -1e-9).map((n) => [flat(n), dot(n, L)]);
    const corners = t3Meet(V, 0, e, 0).map((n) => [flat(n), dot(n, L)]);
    for (let tone = 0; tone < 5; tone++) {
      const tau = tone === 0 ? -Infinity : T3_LB[tone - 1];
      const candidates = [];
      for (const list of [rim, base, corners]) for (const [p, lit] of list) if (lit >= tau - 1e-9) candidates.push(p);
      if (tone > 0) {
        for (const n of circle(L, tau, (n2) => dot(n2, V) >= -1e-9 && dot(n2, e) >= -1e-9)) candidates.push(flat(n));
        for (const n of t3Meet(L, tau, V, 0)) if (dot(n, e) >= -1e-9) candidates.push(flat(n));
        for (const n of t3Meet(L, tau, e, 0)) if (dot(n, V) >= -1e-9) candidates.push(flat(n));
      }
      if (candidates.length < 3) continue;
      const region = t3Hull(candidates);
      if (region.length >= 3) sheets[tone] += t3PathOf(region, true);
    }
  }
  function t3BoxOf(pts, box) {
    let x0 = Infinity;
    let y0 = Infinity;
    let x1 = -Infinity;
    let y1 = -Infinity;
    for (const [x, y] of pts) {
      if (x < x0) x0 = x;
      if (x > x1) x1 = x;
      if (y < y0) y0 = y;
      if (y > y1) y1 = y;
    }
    box[0] = x0;
    box[1] = y0;
    box[2] = x1;
    box[3] = y1;
  }
  function t3Thin(points, most) {
    if (points.length <= most) return points;
    const n = points.length;
    const picks = [];
    for (let i = 0; i < most; i++) picks.push(Math.floor(i * n / most));
    const thin = picks.map((i) => points[i]);
    let err = 0;
    for (let j = 0; j < most; j++) {
      const a = thin[j];
      const b = thin[(j + 1) % most];
      const dx = b[0] - a[0];
      const dy = b[1] - a[1];
      const l = Math.hypot(dx, dy) || 1;
      const end = j + 1 < most ? picks[j + 1] : picks[0] + n;
      for (let i = picks[j] + 1; i < end; i++) {
        const p = points[i % n];
        const out = ((p[0] - a[0]) * dy - (p[1] - a[1]) * dx) / l;
        if (Math.abs(out) > err) err = Math.abs(out);
      }
    }
    return t3Grown(thin, err);
  }
  function t3Grown(poly, by) {
    if (!(by > 0)) return poly;
    let area = 0;
    for (let i = 0; i < poly.length; i++) {
      const a = poly[i];
      const b = poly[(i + 1) % poly.length];
      area += a[0] * b[1] - b[0] * a[1];
    }
    const sign = area >= 0 ? 1 : -1;
    const n = poly.length;
    const normals = poly.map((a, i) => {
      const b = poly[(i + 1) % n];
      const l = Math.hypot(b[0] - a[0], b[1] - a[1]) || 1;
      return [sign * (b[1] - a[1]) / l, -sign * (b[0] - a[0]) / l];
    });
    return poly.map((p, i) => {
      const na = normals[(i - 1 + n) % n];
      const nb = normals[i];
      const mx = na[0] + nb[0];
      const my = na[1] + nb[1];
      const dd = (mx * mx + my * my) / 2 || 1;
      return [p[0] + mx * by / dd, p[1] + my * by / dd];
    });
  }
  function t3HullOut(f, points, most = 32) {
    const thin = t3Thin(points, most);
    const hull = t3Grow(f, "hull", 2 * thin.length, Float64Array);
    for (let i = 0; i < thin.length; i++) {
      hull[2 * i] = thin[i][0];
      hull[2 * i + 1] = thin[i][1];
    }
    f.hullN = thin.length;
  }
  function t3ArcPoints(geo, s, r, from, to, k, out, cut2 = false) {
    const count = Math.max(2, Math.ceil(Math.abs(to - from) * 48 / T3_TAU), Math.ceil(Math.abs(to - from) * Math.max(r, 1e-6) * k / 1.5));
    for (let j = 0; j <= count; j++) {
      const t = from + (to - from) * j / count;
      const c = Math.cos(t);
      const n = Math.sin(t);
      const p = [geo.O[0] + s * geo.SA[0] + r * (c * geo.SU[0] + n * geo.SV[0]), geo.O[1] + s * geo.SA[1] + r * (c * geo.SU[1] + n * geo.SV[1])];
      if (cut2) p.cut = true;
      out.push(p);
    }
  }
  function t3RoundOutline(run, geo, cam) {
    const k = cam.k;
    const { s0, s1, r0, r1, ends } = run;
    const domes = (ends[0] === "dome" ? 1 : 0) + (ends[1] === "dome" ? 1 : 0);
    if (domes === 2) {
      const c0 = [geo.O[0] + s0 * geo.SA[0], geo.O[1] + s0 * geo.SA[1]];
      const c1 = [geo.O[0] + s1 * geo.SA[0], geo.O[1] + s1 * geo.SA[1]];
      const rk = r0 * k;
      const dx = c1[0] - c0[0];
      const dy = c1[1] - c0[1];
      const l = Math.hypot(dx, dy);
      const count = Math.max(24, Math.ceil(Math.PI * rk / 1.5));
      const out2 = [];
      if (l < 1e-6) {
        for (let j = 0; j < 2 * count; j++) {
          const t = j / (2 * count) * T3_TAU;
          out2.push([c1[0] + rk * Math.cos(t), c1[1] + rk * Math.sin(t)]);
        }
        return out2;
      }
      const beta = Math.atan2(dy, dx);
      for (let j = 0; j <= count; j++) {
        const t = beta - Math.PI / 2 + Math.PI * j / count;
        out2.push([c1[0] + rk * Math.cos(t), c1[1] + rk * Math.sin(t)]);
      }
      for (let j = 0; j <= count; j++) {
        const t = beta + Math.PI / 2 + Math.PI * j / count;
        out2.push([c0[0] + rk * Math.cos(t), c0[1] + rk * Math.sin(t)]);
      }
      return out2;
    }
    if (domes === 1) {
      const pts = [];
      for (const [end, s, r] of [[0, s0, r0], [1, s1, r1]]) {
        t3ArcPoints(geo, s, r, 0, T3_TAU, k, pts);
        if (ends[end] !== "dome") continue;
        const sign = end ? 1 : -1;
        const c2 = [geo.O[0] + s * geo.SA[0], geo.O[1] + s * geo.SA[1]];
        const rk = r * k;
        const beta = Math.atan2(sign * geo.SA[1], sign * geo.SA[0]);
        const count = Math.max(24, Math.ceil(Math.PI * rk / 1.5));
        for (let j = 0; j <= count; j++) {
          const t = beta - Math.PI / 2 + Math.PI * j / count;
          pts.push([c2[0] + rk * Math.cos(t), c2[1] + rk * Math.sin(t)]);
        }
      }
      return t3Hull(pts);
    }
    const view = geo.view;
    const out = [];
    let c;
    if (view.flat < 1e-9) c = run.na * view.a > 0 ? -2 : 2;
    else c = -(run.na * view.a) / (run.nr * view.flat);
    if (c <= -1 || c >= 1) {
      const side = c <= -1;
      const capFirst = -geo.aV > 0;
      const keepFirst = side ? !capFirst : capFirst;
      const s = keepFirst ? s0 : s1;
      const r = keepFirst ? r0 : r1;
      t3ArcPoints(geo, s, r, 0, T3_TAU, k, out, run.cutS !== null && Math.abs(run.cutS - s) < 1e-6);
      out.pop();
      return out;
    }
    const d = Math.acos(c);
    const lo = view.phi - d;
    const hi = view.phi + d;
    const cut0 = run.cutS !== null && Math.abs(run.cutS - s0) < 1e-6;
    const cut1 = run.cutS !== null && Math.abs(run.cutS - s1) < 1e-6;
    if (-geo.aV > 0) t3ArcPoints(geo, s0, r0, hi, lo + T3_TAU, k, out, cut0);
    else t3ArcPoints(geo, s0, r0, lo, hi, k, out, cut0);
    const tail = [];
    if (geo.aV > 0) t3ArcPoints(geo, s1, r1, hi, lo + T3_TAU, k, tail, cut1);
    else t3ArcPoints(geo, s1, r1, lo, hi, k, tail, cut1);
    const first = out[out.length - 1];
    const a = tail[0];
    const b = tail[tail.length - 1];
    if (Math.hypot(a[0] - first[0], a[1] - first[1]) > Math.hypot(b[0] - first[0], b[1] - first[1])) tail.reverse();
    for (const p of tail) out.push(p);
    return out;
  }
  function t3LatheMid(a, b) {
    const h = b.s - a.s;
    const ga = -a.na / a.nr;
    const gb = -b.na / b.nr;
    const nr = a.nr + b.nr;
    const na = a.na + b.na;
    const l = Math.hypot(nr, na) || 1;
    return { s: (a.s + b.s) / 2, r: (a.r + b.r) / 2 + h * (ga - gb) / 8, nr: nr / l, na: na / l };
  }
  function t3LatheOutline(run, geo, cam) {
    const k = cam.k;
    const view = geo.view;
    const lv = run.levels;
    const pts = [];
    const cut2 = (L) => view.flat < 1e-9 ? Infinity : -(L.na * view.a) / (L.nr * view.flat);
    const inside = (L) => L.r <= 1e-9 || Math.abs(cut2(L)) < 1;
    const sides = (L) => {
      if (L.r <= 1e-9) {
        const p = [geo.O[0] + L.s * geo.SA[0], geo.O[1] + L.s * geo.SA[1]];
        return [p, p];
      }
      const c = Math.max(-1, Math.min(1, cut2(L)));
      const d = Math.acos(c);
      return [view.phi - d, view.phi + d].map((t) => {
        const cs = Math.cos(t);
        const sn = Math.sin(t);
        return [geo.O[0] + L.s * geo.SA[0] + L.r * (cs * geo.SU[0] + sn * geo.SV[0]), geo.O[1] + L.s * geo.SA[1] + L.r * (cs * geo.SU[1] + sn * geo.SV[1])];
      });
    };
    const span = (a, b) => {
      const pa = sides(a);
      const pb = sides(b);
      return Math.max(Math.hypot(pa[0][0] - pb[0][0], pa[0][1] - pb[0][1]), Math.hypot(pa[1][0] - pb[1][0], pa[1][1] - pb[1][1]));
    };
    const refine = (a, b, depth) => {
      if (depth >= 10 || span(a, b) < 1.2) return;
      const mid = t3LatheMid(a, b);
      refine(a, mid, depth + 1);
      pts.push(...sides(mid));
      refine(mid, b, depth + 1);
    };
    let previous = null;
    for (let i = 0; i < lv.length; i += 4) {
      const L = { s: lv[i], r: lv[i + 1], nr: lv[i + 2], na: lv[i + 3] };
      if (inside(L)) pts.push(...sides(L));
      if (previous) {
        const pin = inside(previous);
        const lin = inside(L);
        if (pin && lin) refine(previous, L, 0);
        else if (pin !== lin) {
          let a = pin ? previous : L;
          let b = pin ? L : previous;
          const start = a;
          for (let it = 0; it < 14; it++) {
            const mid = t3LatheMid(a.s < b.s ? a : b, a.s < b.s ? b : a);
            if (inside(mid)) a = mid;
            else b = mid;
          }
          pts.push(...sides(a));
          refine(start.s < a.s ? start : a, start.s < a.s ? a : start, 0);
        }
      }
      previous = L;
    }
    for (const i of [0, lv.length - 4]) if (lv[i + 1] > 1e-9) t3ArcPoints(geo, lv[i], lv[i + 1], 0, T3_TAU, k, pts);
    return t3Hull(pts);
  }
  function t3SeamArc(geo, s, r, slope, k, trim = 0.3) {
    const view = geo.view;
    const norm = Math.hypot(1, slope);
    let lo;
    let hi;
    if (view.flat < 1e-9) {
      if (!(-slope * view.a / norm > 0)) return "";
      lo = view.phi;
      hi = view.phi + T3_TAU;
    } else {
      const cc = slope * view.a / view.flat;
      if (cc >= 1) return "";
      if (cc <= -1) {
        lo = view.phi;
        hi = view.phi + T3_TAU;
      } else {
        const d = Math.acos(cc);
        lo = view.phi - d;
        hi = view.phi + d;
      }
    }
    const full = hi - lo >= T3_TAU - 1e-9;
    const buf = t3Scratch("c", 2 * 520);
    if (!full) {
      const span = hi - lo;
      const cutAt = (from, sign) => {
        t3At(geo, s, r, from, buf, 0);
        const px = buf[0];
        const py = buf[1];
        let a = 0;
        let b = span * 0.25;
        t3At(geo, s, r, from + sign * b, buf, 0);
        if (Math.hypot(buf[0] - px, buf[1] - py) <= trim) return b;
        for (let it = 0; it < 18; it++) {
          const mid = (a + b) / 2;
          t3At(geo, s, r, from + sign * mid, buf, 0);
          if (Math.hypot(buf[0] - px, buf[1] - py) < trim) a = mid;
          else b = mid;
        }
        return (a + b) / 2;
      };
      const d0 = cutAt(lo, 1);
      const d1 = cutAt(hi, -1);
      lo += d0;
      hi -= d1;
    }
    const count = Math.min(512, Math.max(4, Math.ceil((hi - lo) * r * k / 1.5)));
    for (let j = 0; j <= count; j++) t3At(geo, s, r, lo + (hi - lo) * j / count, buf, 2 * j);
    return t3Path(buf, full ? count : count + 1, full);
  }
  function t3RibLines(geo, F, cam, ribs, sx, sy) {
    const lines = t3Lines;
    lines.d.length = 0;
    lines.alpha.length = 0;
    lines.key.length = 0;
    const { s0, s1, count, phase = 0, twist = 0, fade = [0.1, 0.55] } = ribs;
    const r0 = ribs.r0 ?? ribs.r;
    const r1 = ribs.r1 ?? r0;
    const slope = (r1 - r0) / (s1 - s0 || 1);
    const norm = Math.hypot(1, slope);
    const view = geo.view;
    const seg = new Float64Array(4);
    for (let i = 0; i < count; i++) {
      const t = phase + i / count * T3_TAU;
      const tm = t + twist / 2;
      const facing = (view.flat * Math.cos(tm - view.phi) - slope * view.a) / norm;
      const alpha = t3Step(fade[0], fade[1], facing);
      if (alpha * T3_LEVELS < 0.5) continue;
      t3At(geo, s0, r0, t, seg, 0);
      t3At(geo, s1, r1, t + twist, seg, 2);
      seg[0] -= sx;
      seg[1] -= sy;
      seg[2] -= sx;
      seg[3] -= sy;
      lines.d.push(t3Path(seg, 2, false));
      lines.alpha.push(alpha);
      lines.key.push(i);
    }
    return lines;
  }
  function t3PrepareRound(run, part, P, unit) {
    const spec = part.spec;
    const k = P.scale * T3_ROOT;
    run.F = spec.F;
    run.s0 = spec.s0;
    run.s1 = spec.s1;
    run.r0 = spec.r0;
    run.r1 = spec.r1;
    run.ends = spec.ends;
    const g = (spec.r1 - spec.r0) / (spec.s1 - spec.s0 || 1);
    const norm = Math.hypot(1, g);
    run.nr = 1 / norm;
    run.na = -g / norm;
    run.g = g;
    const rmax = Math.max(spec.r0, spec.r1);
    const around = T3_TAU * rmax * k * unit;
    run.fine = Math.max(around < 30 ? 16 : 24, Math.min(96, Math.ceil(around / 2.2)));
    run.dirs = Math.max(around < 30 ? 16 : 32, Math.min(256, Math.ceil(around / 1.5)));
    run.capCount = Math.max(around < 30 ? 16 : 24, Math.min(160, Math.ceil(around / 1.5)));
    run.domeCount = Math.max(around < 30 ? 12 : 16, Math.min(48, Math.round(run.fine * 0.75)));
    const comps = [];
    for (const [end, s, r] of [[0, spec.s0, spec.r0], [1, spec.s1, spec.r1]]) comps.push(spec.ends[end] === "dome" ? 1 : 0, s, r);
    run.components = comps;
    const details = part.details ?? {};
    run.seams = (details.seams ?? []).map((s) => ({ s, r: spec.r0 + g * (s - spec.s0), slope: g }));
    run.ribs = details.ribs ? { ...details.ribs, r0: details.ribs.r0 ?? spec.r0 + g * (details.ribs.s0 - spec.s0), r1: details.ribs.r1 ?? spec.r0 + g * (details.ribs.s1 - spec.s0) } : null;
    run.cutS = null;
    for (const cut2 of spec.cuts ?? []) {
      const along = cut2.n[0] * spec.F.a[0] + cut2.n[1] * spec.F.a[1] + cut2.n[2] * spec.F.a[2];
      const sCut = (cut2.d - (cut2.n[0] * spec.F.o[0] + cut2.n[1] * spec.F.o[1] + cut2.n[2] * spec.F.o[2])) / along;
      if (Math.abs(sCut - spec.s0) < 1e-6 || Math.abs(sCut - spec.s1) < 1e-6) run.cutS = sCut;
    }
  }
  function t3EmitRound(run, cam, f) {
    const geo = t3Geo(run.F, cam);
    const k = cam.k;
    const step = T3_TAU / run.fine;
    const sheets = ["", "", "", "", ""];
    const { s0, s1, r0, r1 } = run;
    for (const arc of t3Arcs(run.nr, run.na, geo.view, geo.light)) sheets[arc.tone] += t3Strip(geo, s0, r0, s1, r1, arc.from, arc.to, step);
    const F = run.F;
    for (let end = 0; end < 2; end++) {
      if (run.ends[end] !== "dome") continue;
      const s = end ? s1 : s0;
      const sign = end ? 1 : -1;
      const C = [F.o[0] + F.a[0] * s, F.o[1] + F.a[1] * s, F.o[2] + F.a[2] * s];
      t3Dome(cam, C, [F.a[0] * sign, F.a[1] * sign, F.a[2] * sign], end ? r1 : r0, run.domeCount, sheets);
    }
    for (let t = 0; t < 5; t++) f.d[run.role[`s${t}`]] = sheets[t];
    const pts = t3RoundOutline(run, geo, cam);
    const outline = t3PathOf(pts, true);
    f.d[run.role.fill] = outline;
    if (run.cutS !== null) {
      const buf = new Float64Array(2 * pts.length);
      const skip = new Uint8Array(pts.length);
      pts.forEach((p, j) => {
        buf[2 * j] = p[0];
        buf[2 * j + 1] = p[1];
      });
      for (let j = 0; j < pts.length; j++) skip[j] = pts[j].cut && pts[(j + 1) % pts.length].cut ? 1 : 0;
      f.d[run.role.edge] = t3Broken(buf, pts.length, skip);
    } else f.d[run.role.edge] = outline;
    t3BoxOf(pts, f.box);
    t3HullOut(f, pts);
    const view = geo.view;
    let crease = "";
    for (let end = 0; end < 2; end++) {
      if (run.ends[end] !== "flat") continue;
      const role = run.role[`k${end}`];
      const sign = end ? 1 : -1;
      const s = end ? s1 : s0;
      const r = end ? r1 : r0;
      const face = sign * geo.aV;
      if (!(face > 1e-9)) {
        f.d[role] = "";
        continue;
      }
      const n = run.capCount;
      const buf = t3Scratch("c", 2 * n);
      const table = t3Table(n);
      for (let j = 0; j < n; j++) {
        const c = table[2 * j];
        const q = table[2 * j + 1];
        buf[2 * j] = geo.O[0] + s * geo.SA[0] + r * (c * geo.SU[0] + q * geo.SV[0]);
        buf[2 * j + 1] = geo.O[1] + s * geo.SA[1] + r * (c * geo.SU[1] + q * geo.SV[1]);
      }
      f.d[role] = t3Path(buf, n, true);
      f.q[role] = t3Level(sign * geo.aL, T3_LB);
      const minor = 2 * r * k * Math.abs(face);
      f.w[role] = minor < 0.4 ? Math.round(minor * 100) / 100 : -1;
      if (run.role.crease === void 0) continue;
      let lo;
      let hi;
      if (view.flat < 1e-9) {
        if (!(run.na * view.a > 1e-9)) continue;
        lo = 0;
        hi = T3_TAU;
      } else {
        const cc = -(run.na * view.a) / (run.nr * view.flat);
        if (cc >= 1) continue;
        if (cc <= -1) {
          lo = view.phi;
          hi = view.phi + T3_TAU;
        } else {
          const d = Math.acos(cc);
          lo = view.phi - d;
          hi = view.phi + d;
        }
      }
      const count = Math.min(400, Math.max(4, Math.ceil((hi - lo) * r * k / 1.5)));
      const arc = t3Scratch("c", 2 * count + 2);
      for (let j = 0; j <= count; j++) t3At(geo, s, r, lo + (hi - lo) * j / count, arc, 2 * j);
      crease += t3Path(arc, count + 1, false);
    }
    if (run.role.crease !== void 0) f.d[run.role.crease] = crease;
    if (run.role.inner !== void 0) {
      let inner = "";
      for (const seam of run.seams) inner += t3SeamArc(geo, seam.s, seam.r, seam.slope, k);
      if (run.ribs && run.ribs.seams) {
        const rs = run.ribs;
        const slope = (rs.r1 - rs.r0) / (rs.s1 - rs.s0 || 1);
        if (rs.seams !== "last") inner += t3SeamArc(geo, rs.s0, rs.r0, slope, k);
        if (rs.seams !== "first") inner += t3SeamArc(geo, rs.s1, rs.r1, slope, k);
      }
      f.d[run.role.inner] = inner;
    }
    if (run.ribs) {
      const lines = t3State.detail < 0.01 ? t3None : t3RibLines(geo, run.F, cam, run.ribs, 0, 0);
      f.levels = t3Faded(f, run, "r", lines, lines.d.length);
    }
  }
  function t3PrepareBall(run, part, P, unit) {
    const spec = part.spec;
    const k = P.scale * T3_ROOT;
    run.c = spec.c;
    run.r = spec.r;
    run.flats = spec.flats.map((flat) => {
      const n = t3Unit(flat.n);
      const rho = Math.sqrt(Math.max(0, spec.r * spec.r - flat.d * flat.d));
      const [u, v] = t3Basis(n);
      return { n, d: flat.d, rho, u, v };
    });
    run.limb = Math.max(32, Math.min(160, Math.ceil(T3_TAU * spec.r * k * unit / 1.5)));
    run.rimCount = run.flats.map((flat) => Math.max(20, Math.min(120, Math.ceil(T3_TAU * flat.rho * k * unit / 1.5))));
  }
  function t3ClipConvex(subject, clip) {
    if (subject.length < 3 || clip.length < 3) return [];
    let area = 0;
    for (let i = 0; i < clip.length; i++) {
      const a = clip[i];
      const b = clip[(i + 1) % clip.length];
      area += a[0] * b[1] - b[0] * a[1];
    }
    const sign = area >= 0 ? 1 : -1;
    let out = subject;
    for (let i = 0; i < clip.length && out.length; i++) {
      const a = clip[i];
      const b = clip[(i + 1) % clip.length];
      const side = (p) => sign * ((b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0]));
      const input = out;
      out = [];
      for (let j = 0; j < input.length; j++) {
        const p = input[j];
        const q = input[(j + 1) % input.length];
        const sp = side(p);
        const sq = side(q);
        if (sp >= 0) out.push(p);
        if (sp >= 0 !== sq >= 0) {
          const t = sp / (sp - sq);
          out.push([p[0] + (q[0] - p[0]) * t, p[1] + (q[1] - p[1]) * t]);
        }
      }
    }
    return out;
  }
  function t3EmitBall(run, cam, f) {
    const m = cam.m;
    const V = cam.V;
    const L = cam.L;
    const { c, r, flats } = run;
    const Cx = cam.ox + m[0] * c[0] + m[1] * c[1] + m[2] * c[2];
    const Cy = cam.oy + m[3] * c[0] + m[4] * c[1] + m[5] * c[2];
    const dot = (a, b) => a[0] * b[0] + a[1] * b[1] + a[2] * b[2];
    const flat = (w) => [Cx + r * (m[0] * w[0] + m[1] * w[1] + m[2] * w[2]), Cy + r * (m[3] * w[0] + m[4] * w[1] + m[5] * w[2])];
    const inside = (w, skip = -1) => {
      for (let i = 0; i < flats.length; i++) if (i !== skip && dot(w, flats[i].n) * r > flats[i].d + 1e-7) return false;
      return true;
    };
    const [U, W] = t3Basis(V);
    const n = run.limb;
    const table = t3Table(n);
    const limb = [];
    for (let j = 0; j < n; j++) limb.push([U[0] * table[2 * j] + W[0] * table[2 * j + 1], U[1] * table[2 * j] + W[1] * table[2 * j + 1], U[2] * table[2 * j] + W[2] * table[2 * j + 1]]);
    const sil = [];
    for (const w of limb) if (inside(w)) sil.push(flat(w));
    const rims = flats.map((cut2, ci) => {
      const count = run.rimCount[ci];
      const t = t3Table(count);
      const list = [];
      for (let j = 0; j < count; j++) {
        const w = [(cut2.n[0] * cut2.d + cut2.rho * (cut2.u[0] * t[2 * j] + cut2.v[0] * t[2 * j + 1])) / r, (cut2.n[1] * cut2.d + cut2.rho * (cut2.u[1] * t[2 * j] + cut2.v[1] * t[2 * j + 1])) / r, (cut2.n[2] * cut2.d + cut2.rho * (cut2.u[2] * t[2 * j] + cut2.v[2] * t[2 * j + 1])) / r];
        list.push({ w, keep: inside(w, ci), p: flat(w) });
      }
      return list;
    });
    flats.forEach((cut2, ci) => {
      for (const w of t3Meet(V, 0, cut2.n, cut2.d / r)) if (inside(w, ci)) sil.push(flat(w));
      rims[ci].forEach(({ keep, p }) => keep && sil.push(p));
    });
    const hull = t3Hull(sil);
    const outline = t3PathOf(hull, true);
    f.d[run.role.fill] = outline;
    f.d[run.role.edge] = outline;
    f.d[run.role.s0] = outline;
    const capOf = (threshold) => {
      const points = [];
      for (const w of limb) if (dot(w, L) >= threshold && inside(w)) points.push(flat(w));
      const radius = Math.sqrt(Math.max(0, 1 - threshold * threshold));
      const [LU, LW] = t3Basis(L);
      for (let j = 0; j < n; j++) {
        const w = [L[0] * threshold + radius * (LU[0] * table[2 * j] + LW[0] * table[2 * j + 1]), L[1] * threshold + radius * (LU[1] * table[2 * j] + LW[1] * table[2 * j + 1]), L[2] * threshold + radius * (LU[2] * table[2 * j] + LW[2] * table[2 * j + 1])];
        if (dot(w, V) >= -1e-9) points.push(flat(w));
      }
      if (dot(L, V) > threshold) points.push(flat(V));
      for (const w of t3Meet(L, threshold, V, 0)) if (inside(w)) points.push(flat(w));
      flats.forEach((cut2, ci) => {
        for (const w of t3Meet(V, 0, cut2.n, cut2.d / r)) if (inside(w, ci) && dot(w, L) >= threshold) points.push(flat(w));
        for (const w of t3Meet(L, threshold, cut2.n, cut2.d / r)) if (inside(w, ci) && dot(w, V) >= -1e-9) points.push(flat(w));
        for (const { w, keep, p } of rims[ci]) if (keep && dot(w, L) >= threshold && dot(w, V) >= -1e-9) points.push(p);
      });
      if (points.length < 3) return "";
      const region = t3ClipConvex(t3Hull(points), hull);
      return region.length >= 3 ? t3PathOf(region, true) : "";
    };
    f.d[run.role.s1] = capOf(T3_LB[1]);
    f.d[run.role.s2] = capOf(T3_LB[2]);
    f.d[run.role.s3] = capOf(T3_LB[3]);
    let crease = "";
    flats.forEach((cut2, ci) => {
      const role = run.role[`f${ci}`];
      const face = dot(cut2.n, V);
      if (!(face > 1e-9)) {
        f.d[role] = "";
        return;
      }
      const pts = t3ClipConvex(rims[ci].map(({ p }) => p), hull);
      f.d[role] = t3PathOf(pts, true);
      f.q[role] = t3Level(dot(cut2.n, L), T3_LB);
      const minor = 2 * cut2.rho * cam.k * face;
      f.w[role] = minor < 0.4 ? Math.round(minor * 100) / 100 : -1;
      const list = rims[ci];
      const seen = list.map(({ w, keep }) => keep && dot(w, V) > 0);
      const start = seen.indexOf(false);
      if (start < 0) {
        crease += t3PathOf(list.map(({ p }) => p), true);
        return;
      }
      let cur = null;
      for (let s = 1; s <= list.length; s++) {
        const i = (start + s) % list.length;
        if (seen[i]) (cur ?? (cur = [])).push(list[i].p);
        else if (cur) {
          if (cur.length > 1) crease += t3PathOf(cur, false);
          cur = null;
        }
      }
      if (cur && cur.length > 1) crease += t3PathOf(cur, false);
    });
    if (run.role.crease !== void 0) f.d[run.role.crease] = crease;
    let x0 = Infinity;
    let y0 = Infinity;
    let x1 = -Infinity;
    let y1 = -Infinity;
    for (const [x, y] of hull) {
      if (x < x0) x0 = x;
      if (x > x1) x1 = x;
      if (y < y0) y0 = y;
      if (y > y1) y1 = y;
    }
    f.box[0] = x0;
    f.box[1] = y0;
    f.box[2] = x1;
    f.box[3] = y1;
    t3HullOut(f, hull);
  }
  function t3PrepareLathe(run, part, P, unit) {
    const spec = part.spec;
    const k = P.scale * T3_ROOT;
    run.F = spec.F;
    run.levels = spec.levels;
    run.caps = spec.caps;
    let rmax = 0;
    for (let i = 0; i < spec.levels.length; i += 4) rmax = Math.max(rmax, spec.levels[i + 1]);
    run.fine = Math.max(24, Math.min(96, Math.ceil(T3_TAU * rmax * k * unit / 2.2)));
    run.dirs = Math.max(32, Math.min(256, Math.ceil(T3_TAU * rmax * k * unit / 1.5)));
    run.capCount = Math.max(24, Math.min(160, Math.ceil(T3_TAU * rmax * k * unit / 1.5)));
    const comps = [];
    for (let i = 0; i < spec.levels.length; i += 4) comps.push(0, spec.levels[i], spec.levels[i + 1]);
    run.components = comps;
    const details = part.details ?? {};
    run.seams = (details.seams ?? []).map((seam) => typeof seam === "number" ? t3LatheSeam(spec.levels, seam) : seam);
    run.ribs = details.ribs ?? null;
  }
  function t3LatheSeam(levels, s) {
    for (let i = 0; i + 4 < levels.length; i += 4) {
      const sa = levels[i];
      const sb = levels[i + 4];
      if ((s - sa) * (s - sb) <= 0 && sa !== sb) {
        const t = (s - sa) / (sb - sa);
        const r = levels[i + 1] + (levels[i + 5] - levels[i + 1]) * t;
        const slope = (levels[i + 5] - levels[i + 1]) / (sb - sa);
        return { s, r, slope };
      }
    }
    return { s, r: levels[1], slope: 0 };
  }
  function t3LatheSheets(levels, geo, step, buckets) {
    const at = (L, t) => {
      const c = Math.cos(t);
      const n = Math.sin(t);
      return [geo.O[0] + L.s * geo.SA[0] + L.r * (c * geo.SU[0] + n * geo.SV[0]), geo.O[1] + L.s * geo.SA[1] + L.r * (c * geo.SU[1] + n * geo.SV[1])];
    };
    const arcPoints = (L, from, to) => {
      const count = Math.max(1, Math.ceil((to - from) / step));
      const out = new Array(count + 1);
      for (let index = 0; index <= count; index++) out[index] = at(L, from + (to - from) * index / count);
      return out;
    };
    const oriented = (points) => {
      let area = 0;
      for (let i = 0; i < points.length; i++) {
        const a = points[i];
        const b = points[(i + 1) % points.length];
        area += a[0] * b[1] - b[0] * a[1];
      }
      return area < 0 ? points.reverse() : points;
    };
    const centreOf = (arc, reference) => {
      let mid = (arc.from + arc.to) / 2 - reference;
      mid = (mid % T3_TAU + T3_TAU) % T3_TAU;
      return mid;
    };
    const present = [false, false, false, false, false];
    for (const L of levels) {
      const groups = [null, null, null, null, null];
      for (const arc of L.arcs) {
        if (!groups[arc.tone]) groups[arc.tone] = [];
        groups[arc.tone].push(arc);
        present[arc.tone] = true;
      }
      for (const list of groups) if (list && list.length > 1) list.sort((x, y) => centreOf(x, geo.light.phi) - centreOf(y, geo.light.phi));
      L.groups = groups;
    }
    const align = (reference, arc) => {
      const out = { ...arc };
      const centre = (reference.from + reference.to) / 2;
      while ((out.from + out.to) / 2 - centre > Math.PI) {
        out.from -= T3_TAU;
        out.to -= T3_TAU;
      }
      while (centre - (out.from + out.to) / 2 > Math.PI) {
        out.from += T3_TAU;
        out.to += T3_TAU;
      }
      return out;
    };
    const overlap = (x, y) => Math.min(x.to, y.to) - Math.max(x.from, y.from);
    const sheet = (tone, run) => {
      const chains = run[0].groups[tone].map((arc) => [arc]);
      for (let q = 1; q < run.length; q++) {
        const next = run[q].groups[tone];
        const used = new Uint8Array(next.length);
        for (const chain of chains) {
          const prev = chain[q - 1];
          let best = -1;
          let score = -Infinity;
          for (let j = 0; j < next.length; j++) {
            if (used[j]) continue;
            const value = overlap(prev, align(prev, next[j]));
            if (value > score) {
              score = value;
              best = j;
            }
          }
          used[best] = 1;
          chain.push(align(prev, next[best]));
        }
      }
      chains.forEach((chain) => {
        const last = run.length - 1;
        const points = arcPoints(run[0], chain[0].from, chain[0].to);
        for (let q = 1; q < last; q++) points.push(at(run[q], chain[q].to));
        points.push(...arcPoints(run[last], chain[last].from, chain[last].to).reverse());
        for (let q = last - 1; q >= 1; q--) points.push(at(run[q], chain[q].from));
        buckets[tone] += t3PathOf(oriented(points), true);
      });
    };
    const strip = (tone, a, b) => {
      const below = a.groups[tone] ?? [];
      const above = b.groups[tone] ?? [];
      const whole = (arc) => arc.to - arc.from >= T3_TAU - 1e-6;
      const seat = (ring, arc) => {
        const gap = T3_TAU - (arc.to - arc.from);
        return { from: arc.from - gap / 2, to: arc.to + gap / 2 };
      };
      const quad = (lo, hi) => {
        if (whole(hi) && !whole(lo)) hi = seat(hi, lo);
        else if (whole(lo) && !whole(hi)) lo = seat(lo, hi);
        const points = [...arcPoints(a, lo.from, lo.to), ...arcPoints(b, hi.from, hi.to).reverse()];
        buckets[tone] += t3PathOf(oriented(points), true);
      };
      const links = below.map(() => []);
      const back = above.map(() => []);
      below.forEach(
        (lo, i) => above.forEach((hi, j) => {
          if (overlap(lo, align(lo, hi)) > -0.05) {
            links[i].push(j);
            back[j].push(i);
          }
        })
      );
      const doneLo = new Uint8Array(below.length);
      const doneHi = new Uint8Array(above.length);
      const share = (span, parts, flip) => {
        if (whole(span)) {
          const base = parts[0].from;
          const sorted2 = parts.map((arc) => {
            const shift = T3_TAU * Math.floor((arc.from - base) / T3_TAU);
            return { from: arc.from - shift, to: arc.to - shift };
          }).sort((x, y) => x.from - y.from);
          const n = sorted2.length;
          const cuts2 = sorted2.map((arc, q) => {
            const next = q + 1 < n ? sorted2[q + 1].from : sorted2[0].from + T3_TAU;
            return (arc.to + next) / 2;
          });
          sorted2.forEach((arc, q) => {
            const piece = { from: q ? cuts2[q - 1] : cuts2[n - 1] - T3_TAU, to: cuts2[q] };
            if (flip) quad(arc, piece);
            else quad(piece, arc);
          });
          return;
        }
        const sorted = parts.map((arc) => align(span, arc)).sort((x, y) => x.from - y.from);
        const cuts = [span.from];
        for (let q = 1; q < sorted.length; q++) cuts.push(Math.min(span.to, Math.max(span.from, (sorted[q - 1].to + sorted[q].from) / 2)));
        cuts.push(span.to);
        sorted.forEach((arc, q) => {
          const piece = { from: cuts[q], to: cuts[q + 1] };
          if (flip) quad(arc, piece);
          else quad(piece, arc);
        });
      };
      for (let j = 0; j < above.length; j++) {
        if (back[j].length < 2 || back[j].some((i) => links[i].length !== 1)) continue;
        share(above[j], back[j].map((i) => below[i]), false);
        doneHi[j] = 1;
        for (const i of back[j]) doneLo[i] = 1;
      }
      for (let i = 0; i < below.length; i++) {
        if (doneLo[i] || links[i].length < 2 || links[i].some((j) => back[j].length !== 1)) continue;
        share(below[i], links[i].map((j) => above[j]), true);
        doneLo[i] = 1;
        for (const j of links[i]) doneHi[j] = 1;
      }
      for (let i = 0; i < below.length; i++) {
        if (doneLo[i]) continue;
        const lo = below[i];
        let best = -1;
        let score = -Infinity;
        for (const j of links[i]) {
          if (doneHi[j]) continue;
          const value = overlap(lo, align(lo, above[j]));
          if (value > score) {
            score = value;
            best = j;
          }
        }
        if (best >= 0) {
          doneHi[best] = 1;
          quad(lo, align(lo, above[best]));
        } else {
          const centre = (lo.from + lo.to) / 2;
          quad(lo, { from: centre, to: centre });
        }
      }
      for (let j = 0; j < above.length; j++) {
        if (doneHi[j]) continue;
        const centre = (above[j].from + above[j].to) / 2;
        quad({ from: centre, to: centre }, above[j]);
      }
    };
    for (let tone = 0; tone < 5; tone++) {
      if (!present[tone]) continue;
      for (let q = 1; q < levels.length; q++) strip(tone, levels[q - 1], levels[q]);
    }
    void sheet;
  }
  function t3EmitLathe(run, cam, f) {
    const geo = t3Geo(run.F, cam);
    const k = cam.k;
    const step = T3_TAU / run.fine;
    const sheets = ["", "", "", "", ""];
    const lv = run.levels;
    const levelAt = (s, r, nr, na) => ({ s, r, nr, na, arcs: t3Arcs(nr, na, geo.view, geo.light) });
    const same = (a, b) => {
      if (a.arcs.length !== b.arcs.length) return false;
      for (let i = 0; i < a.arcs.length; i++) if (a.arcs[i].tone !== b.arcs[i].tone || Boolean(a.arcs[i].full) !== Boolean(b.arcs[i].full)) return false;
      return true;
    };
    const reach = (a, b) => Math.hypot((b.s - a.s) * Math.hypot(geo.SA[0], geo.SA[1]), (b.r - a.r) * k) + Math.abs(b.r - a.r) * k;
    const levels = [];
    const wrap = (x, ref) => x + T3_TAU * Math.round((ref - x) / T3_TAU);
    const close = (a, mid, b) => {
      const r = Math.max(a.r, b.r) * k;
      for (let i = 0; i < mid.arcs.length; i++) {
        const m = mid.arcs[i];
        if (m.full) continue;
        for (const key of ["from", "to"]) {
          const x = m[key];
          const guess = (wrap(a.arcs[i][key], x) + wrap(b.arcs[i][key], x)) / 2;
          if (Math.abs(guess - x) * r > 0.25) return false;
        }
      }
      return true;
    };
    const refine = (a, b, depth) => {
      if (depth >= 8 || reach(a, b) < 0.1) {
        levels.push(b);
        return;
      }
      const m = t3LatheMid(a, b);
      const mid = levelAt(m.s, m.r, m.nr, m.na);
      if (same(a, b) && same(a, mid) && close(a, mid, b)) {
        levels.push(b);
        return;
      }
      refine(a, mid, depth + 1);
      refine(mid, b, depth + 1);
    };
    let previous = levelAt(lv[0], lv[1], lv[2], lv[3]);
    levels.push(previous);
    for (let i = 4; i < lv.length; i += 4) {
      const next = levelAt(lv[i], lv[i + 1], lv[i + 2], lv[i + 3]);
      refine(previous, next, 0);
      previous = next;
    }
    t3LatheSheets(levels, geo, step, sheets);
    for (let t = 0; t < 5; t++) f.d[run.role[`s${t}`]] = sheets[t];
    const pts = t3LatheOutline(run, geo, cam);
    const outline = t3PathOf(pts, true);
    f.d[run.role.fill] = outline;
    f.d[run.role.edge] = outline;
    t3BoxOf(pts, f.box);
    t3HullOut(f, pts);
    let crease = "";
    const view = geo.view;
    const ends = [[0, lv[0], lv[1], -1, 4], [1, lv[lv.length - 4], lv[lv.length - 3], 1, lv.length - 8]];
    for (const [end, s, r, sign, near] of ends) {
      const role = run.role[`k${end}`];
      if (role === void 0) continue;
      const face = sign * geo.aV;
      if (!(face > 1e-9) || r <= 1e-9) {
        f.d[role] = "";
        continue;
      }
      const n = run.capCount;
      const buf = t3Scratch("c", 2 * n);
      const table = t3Table(n);
      for (let j = 0; j < n; j++) {
        const c = table[2 * j];
        const q = table[2 * j + 1];
        buf[2 * j] = geo.O[0] + s * geo.SA[0] + r * (c * geo.SU[0] + q * geo.SV[0]);
        buf[2 * j + 1] = geo.O[1] + s * geo.SA[1] + r * (c * geo.SU[1] + q * geo.SV[1]);
      }
      f.d[role] = t3Path(buf, n, true);
      f.q[role] = t3Level(sign * geo.aL, T3_LB);
      const minor = 2 * r * k * Math.abs(face);
      f.w[role] = minor < 0.4 ? Math.round(minor * 100) / 100 : -1;
      if (run.role.crease === void 0) continue;
      const nr = lv[near + 2];
      const na = lv[near + 3];
      let lo;
      let hi;
      if (view.flat < 1e-9) {
        if (!(na * view.a > 1e-9)) continue;
        lo = 0;
        hi = T3_TAU;
      } else {
        const cc = -(na * view.a) / (nr * view.flat);
        if (cc >= 1) continue;
        if (cc <= -1) {
          lo = view.phi;
          hi = view.phi + T3_TAU;
        } else {
          const d = Math.acos(cc);
          lo = view.phi - d;
          hi = view.phi + d;
        }
      }
      const count = Math.min(400, Math.max(4, Math.ceil((hi - lo) * r * k / 1.5)));
      const arc = t3Scratch("c", 2 * count + 2);
      for (let j = 0; j <= count; j++) t3At(geo, s, r, lo + (hi - lo) * j / count, arc, 2 * j);
      crease += t3Path(arc, count + 1, false);
    }
    if (run.role.crease !== void 0) f.d[run.role.crease] = crease;
    if (run.role.inner !== void 0) {
      let inner = "";
      for (const seam of run.seams) inner += t3SeamArc(geo, seam.s, seam.r, seam.slope, k);
      f.d[run.role.inner] = inner;
    }
    if (run.ribs) {
      const lines = t3State.detail < 0.01 ? t3None : t3RibLines(geo, run.F, cam, run.ribs, 0, 0);
      f.levels = t3Faded(f, run, "r", lines, lines.d.length);
    }
  }
  var T3_SHINE = (() => {
    const l = Math.hypot(-0.55, -0.835);
    return [-0.55 / l, -0.835 / l];
  })();
  function t3RouteOf(flat) {
    const n = flat.length / 3;
    const along = new Float64Array(n);
    for (let i = 1; i < n; i++) along[i] = along[i - 1] + Math.hypot(flat[3 * i] - flat[3 * i - 3], flat[3 * i + 1] - flat[3 * i - 2], flat[3 * i + 2] - flat[3 * i - 1]);
    return { flat, n, along, total: along[n - 1] };
  }
  function t3PointAlong(route, at) {
    const { flat, n, along } = route;
    if (at <= 0) return [flat[0], flat[1], flat[2]];
    if (at >= along[n - 1]) return [flat[3 * n - 3], flat[3 * n - 2], flat[3 * n - 1]];
    let lo = 0;
    let hi = n - 1;
    while (hi - lo > 1) {
      const mid = lo + hi >> 1;
      if (along[mid] <= at) lo = mid;
      else hi = mid;
    }
    const span = along[hi] - along[lo] || 1;
    const t = (at - along[lo]) / span;
    return [flat[3 * lo] + (flat[3 * hi] - flat[3 * lo]) * t, flat[3 * lo + 1] + (flat[3 * hi + 1] - flat[3 * lo + 1]) * t, flat[3 * lo + 2] + (flat[3 * hi + 2] - flat[3 * lo + 2]) * t];
  }
  function t3Cut(route, from, to) {
    const { flat, n, along } = route;
    const out = [];
    for (let i = 1; i < n; i++) {
      const start = along[i - 1];
      const end = along[i];
      if (end >= from && start <= to) {
        const length = end - start || 1;
        const t0 = Math.max(0, (from - start) / length);
        const t1 = Math.min(1, (to - start) / length);
        const at = (t) => [flat[3 * i - 3] + (flat[3 * i] - flat[3 * i - 3]) * t, flat[3 * i - 2] + (flat[3 * i + 1] - flat[3 * i - 2]) * t, flat[3 * i - 1] + (flat[3 * i + 2] - flat[3 * i - 1]) * t];
        if (!out.length) out.push(at(t0));
        out.push(at(t1));
      }
    }
    return out;
  }
  function t3TangentAlong(route, at) {
    const a = t3PointAlong(route, Math.max(0, at - 0.6));
    const b = t3PointAlong(route, Math.min(route.total, at + 0.6));
    return t3Unit([b[0] - a[0], b[1] - a[1], b[2] - a[2]]);
  }
  var t3RouteCache = /* @__PURE__ */ new WeakMap();
  function t3PrepareTube(run, part, data) {
    const spec = part.spec;
    const source = data.routes[spec.route];
    let route = t3RouteCache.get(source);
    if (!route) {
      route = t3RouteOf(source.points);
      t3RouteCache.set(source, route);
    }
    const total = route.total;
    const r = source.r;
    const step = Math.max(0.05, Math.min(source.spacing, total / 4) * 0.5);
    const lead = 0.5;
    run.r = r;
    run.wide = Boolean(source.wide);
    run.hue = source.hue ?? null;
    const partOf = (start, end) => {
      const points = t3Cut(route, Math.max(0, start), Math.min(total, end));
      let walked = Math.max(0, start);
      const count = points.length;
      const P32 = new Float64Array(3 * count);
      const D3 = new Float64Array(3 * count);
      for (let i = 0; i < count; i++) {
        if (i > 0) walked += Math.hypot(points[i][0] - points[i - 1][0], points[i][1] - points[i - 1][1], points[i][2] - points[i - 1][2]);
        const a = t3PointAlong(route, Math.max(0, Math.min(total, walked - step)));
        const b = t3PointAlong(route, Math.max(0, Math.min(total, walked + step)));
        for (let c = 0; c < 3; c++) {
          P32[3 * i + c] = points[i][c];
          D3[3 * i + c] = b[c] - a[c];
        }
      }
      return { count, P3: P32, D3 };
    };
    const openStart = spec.open0 && spec.from > 0;
    const openEnd = spec.open1 && spec.to < total;
    run.body = partOf(openStart ? spec.from - lead : spec.from, openEnd ? spec.to + lead : spec.to);
    run.stripe = openStart || openEnd ? partOf(openStart ? spec.from - 2 * lead : spec.from, openEnd ? spec.to + 2 * lead : spec.to) : run.body;
    const ends = [!spec.open0 && (spec.from <= 1e-6 || spec.gap0), !spec.open1 && (spec.to >= total - 1e-6 || spec.gap1)];
    run.capped = [ends[0] && (spec.gap0 || spec.caps[0]), ends[1] && (spec.gap1 || spec.caps[1])];
    const P3 = run.body.P3;
    const last = run.body.count - 1;
    const vec = (i, j) => t3Unit([P3[3 * i] - P3[3 * j], P3[3 * i + 1] - P3[3 * j + 1], P3[3 * i + 2] - P3[3 * j + 2]]);
    run.tips = [vec(1, 0), vec(last, last - 1)];
    run.rings = null;
    if (source.rings) {
      const { pitch = 3, twist = 0, cross = false, fade = [0.1, 0.55], phase = 0, steps = 16 } = source.rings;
      const lo = openStart ? spec.from - 2 * lead : spec.from;
      const hi = openEnd ? spec.to + 2 * lead : spec.to;
      const margin = twist ? 0 : Math.min(pitch * 0.35, (hi - lo) / 2);
      const from = Math.max(lo, !openStart ? lo + margin : lo);
      const to = Math.min(hi, !openEnd ? hi - margin : hi);
      const segments = [];
      if (to > from) {
        const hands = twist ? cross ? [1, -1] : [1] : [0];
        const reach = Math.abs(twist) * r;
        const first = Math.ceil((from - reach - phase) / pitch);
        const lastIndex = Math.floor((to + reach - phase) / pitch);
        const surface = (t, theta) => {
          const at = Math.max(0, Math.min(total, t));
          return { c: t3PointAlong(route, at), T: t3TangentAlong(route, at), theta };
        };
        for (let index = first; index <= lastIndex; index++) {
          const station = phase + index * pitch;
          for (const hand of hands) {
            const samples = [];
            for (let k = 0; k <= steps; k++) {
              const theta = k / steps * Math.PI;
              const t = station + hand * twist * r * (k / steps - 0.5);
              samples.push({ t, theta });
            }
            for (let k = 0; k < steps; k++) {
              let a = samples[k];
              let b = samples[k + 1];
              if (a.t < from && b.t < from || a.t > to && b.t > to) continue;
              const clipTo = (x, y, edge) => ({ t: edge, theta: x.theta + (y.theta - x.theta) * (edge - x.t) / (y.t - x.t || 1e-9) });
              if (a.t < from) a = clipTo(a, b, from);
              if (b.t < from) b = clipTo(b, a, from);
              if (a.t > to) a = clipTo(a, b, to);
              if (b.t > to) b = clipTo(b, a, to);
              segments.push([surface(a.t, a.theta), surface(b.t, b.theta)]);
            }
          }
        }
      }
      run.rings = { segments, fade, tone: source.rings.tone ?? "lo" };
    }
  }
  function t3Sides(part, cam, r) {
    const m = cam.m;
    const k = cam.k;
    const n = part.count;
    const out = { n, flat: new Float64Array(2 * n), left: new Float64Array(2 * n), right: new Float64Array(2 * n), shineA: new Float64Array(2 * n), shineB: new Float64Array(2 * n), shadeA: new Float64Array(2 * n), shadeB: new Float64Array(2 * n), frames: [] };
    const half = r * k;
    for (let i = 0; i < n; i++) {
      const x = part.P3[3 * i];
      const y = part.P3[3 * i + 1];
      const z = part.P3[3 * i + 2];
      const px = cam.ox + m[0] * x + m[1] * y + m[2] * z;
      const py = cam.oy + m[3] * x + m[4] * y + m[5] * z;
      const dx = m[0] * part.D3[3 * i] + m[1] * part.D3[3 * i + 1] + m[2] * part.D3[3 * i + 2];
      const dy = m[3] * part.D3[3 * i] + m[4] * part.D3[3 * i + 1] + m[5] * part.D3[3 * i + 2];
      const l = Math.hypot(dx, dy) || 1;
      const nx = -dy / l;
      const ny = dx / l;
      out.flat[2 * i] = px;
      out.flat[2 * i + 1] = py;
      out.frames.push({ p: [px, py], nx, ny, half });
      out.left[2 * i] = px + nx * half;
      out.left[2 * i + 1] = py + ny * half;
      out.right[2 * i] = px - nx * half;
      out.right[2 * i + 1] = py - ny * half;
      const toward = nx * T3_SHINE[0] + ny * T3_SHINE[1];
      const shineAt = half * 0.44 * toward;
      const shineHalf = half * 0.24;
      out.shineA[2 * i] = px + nx * (shineAt + shineHalf);
      out.shineA[2 * i + 1] = py + ny * (shineAt + shineHalf);
      out.shineB[2 * i] = px + nx * (shineAt - shineHalf);
      out.shineB[2 * i + 1] = py + ny * (shineAt - shineHalf);
      const shadeAt = -half * 0.62 * toward;
      const shadeHalf = half * 0.2;
      out.shadeA[2 * i] = px + nx * (shadeAt + shadeHalf);
      out.shadeA[2 * i + 1] = py + ny * (shadeAt + shadeHalf);
      out.shadeB[2 * i] = px + nx * (shadeAt - shadeHalf);
      out.shadeB[2 * i + 1] = py + ny * (shadeAt - shadeHalf);
    }
    return out;
  }
  var t3Pts = (buf, n) => {
    const out = new Array(n);
    for (let i = 0; i < n; i++) out[i] = [buf[2 * i], buf[2 * i + 1]];
    return out;
  };
  function t3TubeCap(cam, centre, tangent, radius, inward) {
    const V = cam.V;
    const m = cam.m;
    let n1 = [tangent[1] * V[2] - tangent[2] * V[1], tangent[2] * V[0] - tangent[0] * V[2], tangent[0] * V[1] - tangent[1] * V[0]];
    if (Math.hypot(n1[0], n1[1], n1[2]) < 1e-6) {
      const helper = Math.abs(tangent[2]) > 0.9 ? [1, 0, 0] : [0, 0, 1];
      n1 = [helper[1] * tangent[2] - helper[2] * tangent[1], helper[2] * tangent[0] - helper[0] * tangent[2], helper[0] * tangent[1] - helper[1] * tangent[0]];
    }
    n1 = t3Unit(n1);
    const n2 = t3Unit([tangent[1] * n1[2] - tangent[2] * n1[1], tangent[2] * n1[0] - tangent[0] * n1[2], tangent[0] * n1[1] - tangent[1] * n1[0]]);
    const steps = 28;
    const proj = (p) => [cam.ox + m[0] * p[0] + m[1] * p[1] + m[2] * p[2], cam.oy + m[3] * p[0] + m[4] * p[1] + m[5] * p[2]];
    const ring = new Array(steps);
    for (let index = 0; index < steps; index++) {
      const angle = index / steps * T3_TAU;
      const cs = radius * Math.cos(angle);
      const sn = radius * Math.sin(angle);
      ring[index] = proj([centre[0] + n1[0] * cs + n2[0] * sn, centre[1] + n1[1] * cs + n2[1] * sn, centre[2] + n1[2] * cs + n2[2] * sn]);
    }
    const C = proj(centre);
    const probe = proj([centre[0] + n2[0], centre[1] + n2[1], centre[2] + n2[2]]);
    const along = (probe[0] - C[0]) * inward[0] + (probe[1] - C[1]) * inward[1];
    const from = along > 0 ? steps / 2 : 0;
    const half = (start) => Array.from({ length: steps / 2 + 1 }, (_, index) => ring[(start + index) % steps]);
    return { ring, arc: half(from), inner: half((from + steps / 2) % steps) };
  }
  function t3StripeEnd(half, centre, nx, ny, from, to) {
    const offset = (p) => (p[0] - centre[0]) * nx + (p[1] - centre[1]) * ny;
    const values = half.map(offset);
    const lo = Math.min(from, to);
    const hi = Math.max(from, to);
    const points = [];
    const cross = (k, level) => {
      const t = (level - values[k]) / (values[k + 1] - values[k] || 1e-9);
      return [half[k][0] + (half[k + 1][0] - half[k][0]) * t, half[k][1] + (half[k + 1][1] - half[k][1]) * t];
    };
    for (let k = 0; k < half.length; k++) {
      if (values[k] >= lo && values[k] <= hi) points.push(half[k]);
      if (k < half.length - 1) {
        for (const level of [lo, hi]) if ((values[k] - level) * (values[k + 1] - level) < 0) points.push(cross(k, level));
      }
    }
    return points.map((p) => [p, offset(p)]).sort((x, y) => from > to ? y[1] - x[1] : x[1] - y[1]).map(([p]) => p);
  }
  function t3EmitTube(run, cam, f) {
    const r = run.r;
    const sides = t3Sides(run.body, cam, r);
    const bands = run.stripe === run.body ? sides : t3Sides(run.stripe, cam, r);
    const n = sides.n;
    const left = t3Pts(sides.left, n);
    const right = t3Pts(sides.right, n);
    const loop = left.concat(right.slice().reverse());
    let area = 0;
    for (let i = 0; i < loop.length; i++) {
      const a = loop[i];
      const b = loop[(i + 1) % loop.length];
      area += a[0] * b[1] - b[0] * a[1];
    }
    const sign = Math.sign(area);
    let body = t3PathOf(loop, true);
    let edges = t3PathOf(left, false) + t3PathOf(right, false);
    const tips = [null, null];
    const last = n - 1;
    const quads = [];
    for (let i = 0; i < last; i++) quads.push([left[i], left[i + 1], right[i + 1], right[i]]);
    for (const side of [0, 1]) {
      if (!run.capped[side]) continue;
      const at = side ? last : 0;
      const other = side ? last - 1 : 1;
      const tangent = run.tips[side];
      const outward = side ? tangent : [-tangent[0], -tangent[1], -tangent[2]];
      const inward = [sides.flat[2 * other] - sides.flat[2 * at], sides.flat[2 * other + 1] - sides.flat[2 * at + 1]];
      const centre = [run.body.P3[3 * at], run.body.P3[3 * at + 1], run.body.P3[3 * at + 2]];
      const { ring, arc, inner } = t3TubeCap(cam, centre, tangent, r, inward);
      let ringArea = 0;
      for (let i = 0; i < ring.length; i++) {
        const a = ring[i];
        const b = ring[(i + 1) % ring.length];
        ringArea += a[0] * b[1] - b[0] * a[1];
      }
      body += t3PathOf(Math.sign(ringArea) === sign ? ring : ring.slice().reverse(), true);
      edges += t3PathOf(arc, false);
      const V = cam.V;
      const open = outward[0] * V[0] + outward[1] * V[1] + outward[2] * V[2] > 0;
      if (open) edges += t3PathOf(inner, false);
      tips[side] = { half: open ? inner : arc, frame: sides.frames[at] };
      quads.push(ring);
    }
    f.d[run.role.body] = body;
    f.d[run.role.edges] = edges;
    if (run.wide) {
      const toward = (frame) => frame.nx * T3_SHINE[0] + frame.ny * T3_SHINE[1];
      const shineOffsets = (frame) => [frame.half * 0.44 * toward(frame) + frame.half * 0.24, frame.half * 0.44 * toward(frame) - frame.half * 0.24];
      const shadeOffsets = (frame) => [-frame.half * 0.62 * toward(frame) + frame.half * 0.2, -frame.half * 0.62 * toward(frame) - frame.half * 0.2];
      const bn = bands.n;
      const band = (A, B, offsets) => {
        const head = tips[1] ? t3StripeEnd(tips[1].half, tips[1].frame.p, tips[1].frame.nx, tips[1].frame.ny, offsets(tips[1].frame)[0], offsets(tips[1].frame)[1]) : [];
        const tail = tips[0] ? t3StripeEnd(tips[0].half, tips[0].frame.p, tips[0].frame.nx, tips[0].frame.ny, offsets(tips[0].frame)[1], offsets(tips[0].frame)[0]) : [];
        return t3PathOf([...t3Pts(A, bn), ...head, ...t3Pts(B, bn).reverse(), ...tail], true);
      };
      f.d[run.role.shine] = band(bands.shineA, bands.shineB, shineOffsets);
      f.d[run.role.shade] = band(bands.shadeA, bands.shadeB, shadeOffsets);
    }
    if (run.rings) {
      const lines = t3Lines;
      lines.d.length = 0;
      lines.alpha.length = 0;
      lines.key.length = 0;
      lines.key.length = 0;
      const V = cam.V;
      const m = cam.m;
      const seg = new Float64Array(4);
      const surface = (sample, out, index2) => {
        const T = sample.T;
        let n1 = [T[1] * V[2] - T[2] * V[1], T[2] * V[0] - T[0] * V[2], T[0] * V[1] - T[1] * V[0]];
        const l1 = Math.hypot(n1[0], n1[1], n1[2]);
        if (l1 < 1e-6) return null;
        n1 = [n1[0] / l1, n1[1] / l1, n1[2] / l1];
        let n2 = t3Unit([T[1] * n1[2] - T[2] * n1[1], T[2] * n1[0] - T[0] * n1[2], T[0] * n1[1] - T[1] * n1[0]]);
        if (n2[0] * V[0] + n2[1] * V[1] + n2[2] * V[2] < 0) n2 = [-n2[0], -n2[1], -n2[2]];
        const cs = Math.cos(sample.theta);
        const sn = Math.sin(sample.theta);
        const normal = [n1[0] * cs + n2[0] * sn, n1[1] * cs + n2[1] * sn, n1[2] * cs + n2[2] * sn];
        const p = [sample.c[0] + normal[0] * r, sample.c[1] + normal[1] * r, sample.c[2] + normal[2] * r];
        out[index2] = cam.ox + m[0] * p[0] + m[1] * p[1] + m[2] * p[2];
        out[index2 + 1] = cam.oy + m[3] * p[0] + m[4] * p[1] + m[5] * p[2];
        return normal[0] * V[0] + normal[1] * V[1] + normal[2] * V[2];
      };
      const fade = run.rings.fade;
      let index = -1;
      for (const [a, b] of run.rings.segments) {
        index++;
        const fa = surface(a, seg, 0);
        const fb = surface(b, seg, 2);
        if (fa === null || fb === null) continue;
        const alpha = fade ? t3Step(fade[0], fade[1], (fa + fb) / 2) : 1;
        if (alpha * T3_LEVELS < 0.5) continue;
        lines.d.push(t3Path(seg, 2, false));
        lines.alpha.push(alpha);
        lines.key.push(index);
      }
      f.levels = t3Faded(f, run, "r", lines, lines.d.length);
    }
    const all = left.concat(right);
    t3BoxOf(all, f.box);
    for (const q of quads) for (const p of q) {
      if (p[0] < f.box[0]) f.box[0] = p[0];
      if (p[1] < f.box[1]) f.box[1] = p[1];
      if (p[0] > f.box[2]) f.box[2] = p[0];
      if (p[1] > f.box[3]) f.box[3] = p[1];
    }
    const list = f.quadList && f.quadList.length === quads.length ? f.quadList : f.quadList = quads.map(() => [new Float64Array(0), 0]);
    for (let qi = 0; qi < quads.length; qi++) {
      const q = quads[qi];
      let entry = list[qi];
      if (entry[0].length < 2 * q.length) entry[0] = new Float64Array(2 * q.length);
      const buf = entry[0];
      for (let i = 0; i < q.length; i++) {
        buf[2 * i] = q[i][0];
        buf[2 * i + 1] = q[i][1];
      }
      entry[1] = q.length;
    }
    f.quadN = quads.length;
    f.quads = f.quadList;
    f.hullN = 0;
  }
  function t3Emit(run, cam, out) {
    const f = out ?? t3Frame(run);
    if (run.kind === "prism") t3EmitPrism(run, cam, f);
    else if (run.kind === "round") t3EmitRound(run, cam, f);
    else if (run.kind === "ball") t3EmitBall(run, cam, f);
    else if (run.kind === "lathe") t3EmitLathe(run, cam, f);
    else if (run.kind === "tube") {
      t3EmitTube(run, cam, f);
      return f;
    } else if (run.kind === "fixed") {
      t3EmitFixed(run, cam, f);
      return f;
    }
    t3EmitPlanes(run, cam, f);
    t3EmitDots(run, cam, f);
    return f;
  }
  function t3Overlap(a, b, pad) {
    return a[0] < b[2] - pad && b[0] < a[2] - pad && a[1] < b[3] - pad && b[1] < a[3] - pad;
  }
  function t3Apart(A, an, B, bn, pad) {
    for (let pass = 0; pass < 2; pass++) {
      const P = pass ? B : A;
      const pn = pass ? bn : an;
      for (let i = 0; i < pn; i++) {
        const j = (i + 1) % pn;
        const nx = P[2 * j + 1] - P[2 * i + 1];
        const ny = P[2 * i] - P[2 * j];
        const l = Math.hypot(nx, ny);
        if (l < 1e-9) continue;
        let a0 = Infinity;
        let a1 = -Infinity;
        for (let q = 0; q < an; q++) {
          const v = (A[2 * q] * nx + A[2 * q + 1] * ny) / l;
          if (v < a0) a0 = v;
          if (v > a1) a1 = v;
        }
        let b0 = Infinity;
        let b1 = -Infinity;
        for (let q = 0; q < bn; q++) {
          const v = (B[2 * q] * nx + B[2 * q + 1] * ny) / l;
          if (v < b0) b0 = v;
          if (v > b1) b1 = v;
        }
        if (a1 < b0 + pad || b1 < a0 + pad) return true;
      }
    }
    return false;
  }
  function t3Disjoint(fa, fb, pad) {
    const qa = fa.quadN ? fa.quads : null;
    const qb = fb.quadN ? fb.quads : null;
    if (!qa && !qb) return t3Apart(fa.hull, fa.hullN, fb.hull, fb.hullN, pad);
    const listA = qa ? fa.quadList : [[fa.hull, fa.hullN]];
    const listB = qb ? fb.quadList : [[fb.hull, fb.hullN]];
    for (const [A, an] of listA) for (const [B, bn] of listB) if (!t3Apart(A, an, B, bn, pad)) return false;
    return true;
  }
  function t3Support(cloud, R, t, dir, world) {
    let best = -Infinity;
    let at = 0;
    const n = cloud.length / 3;
    const dx = R[0] * dir[0] + R[3] * dir[1] + R[6] * dir[2];
    const dy = R[1] * dir[0] + R[4] * dir[1] + R[7] * dir[2];
    const dz = R[2] * dir[0] + R[5] * dir[1] + R[8] * dir[2];
    for (let i = 0; i < n; i++) {
      const v = cloud[3 * i] * dx + cloud[3 * i + 1] * dy + cloud[3 * i + 2] * dz;
      if (v > best) {
        best = v;
        at = i;
      }
    }
    const x = cloud[3 * at];
    const y = cloud[3 * at + 1];
    const z = cloud[3 * at + 2];
    world[0] = R[0] * x + R[1] * y + R[2] * z + t[0];
    world[1] = R[3] * x + R[4] * y + R[5] * z + t[1];
    world[2] = R[6] * x + R[7] * y + R[8] * z + t[2];
    return best + dir[0] * t[0] + dir[1] * t[1] + dir[2] * t[2];
  }
  function t3Gjk(cloudA, camA, cloudB, camB, warm, rounds = 8, hints = null) {
    let w = warm && (warm[0] || warm[1] || warm[2]) ? [warm[0], warm[1], warm[2]] : null;
    const a = [0, 0, 0];
    const b = [0, 0, 0];
    if (!w) {
      t3Support(cloudA, camA.R, camA.t, [1, 0, 0], a);
      t3Support(cloudB, camB.R, camB.t, [-1, 0, 0], b);
      w = [b[0] - a[0], b[1] - a[1], b[2] - a[2]];
    }
    let margin = -Infinity;
    let best = w;
    const step = (limit) => {
      for (let it = 0; it < limit; it++) {
        const l2 = Math.hypot(w[0], w[1], w[2]);
        if (l2 < 1e-12) break;
        const n = [w[0] / l2, w[1] / l2, w[2] / l2];
        const hiA = t3Support(cloudA, camA.R, camA.t, n, a);
        const loB = -t3Support(cloudB, camB.R, camB.t, [-n[0], -n[1], -n[2]], b);
        const value = loB - hiA;
        if (value > margin) {
          margin = value;
          best = n;
        }
        const s = [b[0] - a[0], b[1] - a[1], b[2] - a[2]];
        const ds = [w[0] - s[0], w[1] - s[1], w[2] - s[2]];
        const dd = ds[0] * ds[0] + ds[1] * ds[1] + ds[2] * ds[2];
        if (dd < 1e-14) break;
        const tt = Math.max(0, Math.min(1, (w[0] * ds[0] + w[1] * ds[1] + w[2] * ds[2]) / dd));
        w = [w[0] - ds[0] * tt, w[1] - ds[1] * tt, w[2] - ds[2] * tt];
      }
    };
    step(rounds);
    if (margin < 0) step(24);
    if (margin < 0.05 && hints) {
      if (hints.centroids) {
        const [ca, cb] = hints.centroids;
        const wa = [camA.R[0] * ca[0] + camA.R[1] * ca[1] + camA.R[2] * ca[2] + camA.t[0], camA.R[3] * ca[0] + camA.R[4] * ca[1] + camA.R[5] * ca[2] + camA.t[1], camA.R[6] * ca[0] + camA.R[7] * ca[1] + camA.R[8] * ca[2] + camA.t[2]];
        const wb = [camB.R[0] * cb[0] + camB.R[1] * cb[1] + camB.R[2] * cb[2] + camB.t[0], camB.R[3] * cb[0] + camB.R[4] * cb[1] + camB.R[5] * cb[2] + camB.t[1], camB.R[6] * cb[0] + camB.R[7] * cb[1] + camB.R[8] * cb[2] + camB.t[2]];
        const n = t3Unit([wb[0] - wa[0], wb[1] - wa[1], wb[2] - wa[2]]);
        const hiA = t3Support(cloudA, camA.R, camA.t, n, a);
        const loB = -t3Support(cloudB, camB.R, camB.t, [-n[0], -n[1], -n[2]], b);
        if (loB - hiA > margin) {
          margin = loB - hiA;
          best = n;
        }
      }
      for (const [axis, cam] of hints) {
        const R = cam.R;
        const w0 = [R[0] * axis[0] + R[1] * axis[1] + R[2] * axis[2], R[3] * axis[0] + R[4] * axis[1] + R[5] * axis[2], R[6] * axis[0] + R[7] * axis[1] + R[8] * axis[2]];
        for (const sign of [1, -1]) {
          const n = [w0[0] * sign, w0[1] * sign, w0[2] * sign];
          const hiA = t3Support(cloudA, camA.R, camA.t, n, a);
          const loB = -t3Support(cloudB, camB.R, camB.t, [-n[0], -n[1], -n[2]], b);
          if (loB - hiA > margin) {
            margin = loB - hiA;
            best = n;
          }
        }
      }
    }
    const l = Math.hypot(best[0], best[1], best[2]) || 1;
    return { n: [best[0] / l, best[1] / l, best[2] / l], margin };
  }
  function t3Order(layer, frames, cams, previous, stats, scene) {
    const parts = layer.parts;
    const count = parts.length;
    const local = layer.local;
    const rank = layer._rank ?? (layer._rank = new Int32Array(count));
    if (previous) for (let at = 0; at < count; at++) rank[local.get(previous[at])] = at;
    else for (let at = 0; at < count; at++) rank[local.get(layer.rest[at])] = at;
    let groupEdges = 0;
    if (layer.groupPairs) for (const gp of layer.groupPairs) groupEdges += gp.a.length * gp.b.length;
    const maxEdges = layer.planar.length / 5 + (layer.framed ? layer.framed.length / 6 : 0) + groupEdges + layer.dynamic.length / 2 + (layer.free ? layer.free.length * count : 0) + 1;
    const head = layer._head ?? (layer._head = new Int32Array(count));
    const next = layer._next && layer._next.length >= maxEdges ? layer._next : layer._next = new Int32Array(maxEdges);
    const to = layer._to && layer._to.length >= maxEdges ? layer._to : layer._to = new Int32Array(maxEdges);
    const live = layer._live && layer._live.length >= maxEdges ? layer._live : layer._live = new Uint8Array(maxEdges);
    const indeg = layer._indeg ?? (layer._indeg = new Int32Array(count));
    head.fill(-1);
    indeg.fill(0);
    let edges = 0;
    const addEdge = (back, front) => {
      to[edges] = front;
      next[edges] = head[back];
      live[edges] = 1;
      head[back] = edges;
      indeg[front]++;
      edges++;
    };
    const runs = scene ? scene.runs : null;
    const groupOf = (global) => runs ? runs[global].group : -1;
    const planar = layer.planar;
    for (let p = 0; p < planar.length; p += 5) {
      const i = planar[p];
      const j = planar[p + 1];
      const fi = frames[i];
      const fj = frames[j];
      if (!t3Overlap(fi.box, fj.box, -0.05)) continue;
      const g = groupOf(i);
      const V = g >= 0 ? cams[g].V : cams.world.V;
      const s = planar[p + 2] * V[0] + planar[p + 3] * V[1] + planar[p + 4] * V[2];
      if (s < 1e-7 && s > -1e-7) continue;
      const li = local.get(i);
      const lj = local.get(j);
      if (s > 0) addEdge(li, lj);
      else addEdge(lj, li);
    }
    const framed = layer.framed;
    if (framed)
      for (let p = 0; p < framed.length; p += 6) {
        const i = framed[p];
        const j = framed[p + 1];
        if (!t3Overlap(frames[i].box, frames[j].box, -0.05)) continue;
        const g = framed[p + 2];
        const V = g >= 0 ? cams[g].V : cams.world.V;
        const s = framed[p + 3] * V[0] + framed[p + 4] * V[1] + framed[p + 5] * V[2];
        if (s < 1e-7 && s > -1e-7) continue;
        const li = local.get(i);
        const lj = local.get(j);
        if (s > 0) addEdge(li, lj);
        else addEdge(lj, li);
      }
    if (layer.groupPairs)
      for (const gp of layer.groupPairs) {
        const union = (list, box) => {
          box[0] = Infinity;
          box[1] = Infinity;
          box[2] = -Infinity;
          box[3] = -Infinity;
          for (let q = 0; q < list.length; q++) {
            const b = frames[list[q]].box;
            if (b[0] < box[0]) box[0] = b[0];
            if (b[1] < box[1]) box[1] = b[1];
            if (b[2] > box[2]) box[2] = b[2];
            if (b[3] > box[3]) box[3] = b[3];
          }
        };
        union(gp.a, gp.boxA);
        union(gp.b, gp.boxB);
        if (!t3Overlap(gp.boxA, gp.boxB, -0.05)) continue;
        const V = gp.frame >= 0 ? cams[gp.frame].V : cams.world.V;
        const s = gp.n[0] * V[0] + gp.n[1] * V[1] + gp.n[2] * V[2];
        if (s < 1e-7 && s > -1e-7) continue;
        for (let x = 0; x < gp.a.length; x++) {
          const i = gp.a[x];
          const bi = frames[i].box;
          if (!t3Overlap(bi, gp.boxB, -0.05)) continue;
          for (let y = 0; y < gp.b.length; y++) {
            const j = gp.b[y];
            if (!t3Overlap(bi, frames[j].box, -0.05)) continue;
            if (s > 0) addEdge(local.get(i), local.get(j));
            else addEdge(local.get(j), local.get(i));
          }
        }
      }
    const dynamic = layer.dynamic;
    let unseparated = 0;
    let solved = 0;
    const rel = layer.rel ?? (layer.rel = /* @__PURE__ */ new Map());
    const cross = (i, j) => {
      const ri = runs[i];
      const rj = runs[j];
      const ci = ri.group >= 0 ? cams[ri.group] : cams.world;
      const cj = rj.group >= 0 ? cams[rj.group] : cams.world;
      const A = ci.R;
      const B = cj.R;
      const dx = cj.t[0] - ci.t[0];
      const dy = cj.t[1] - ci.t[1];
      const dz = cj.t[2] - ci.t[2];
      const key = i * 65536 + j;
      let memo = rel.get(key);
      if (!memo) {
        memo = { pose: new Float64Array(12), n: [0, 0, 0], margin: -Infinity, fresh: false };
        rel.set(key, memo);
      }
      const pose = memo.pose;
      let same = memo.fresh;
      let at = 0;
      for (let c = 0; c < 3; c++)
        for (let r = 0; r < 3; r++) {
          const v = A[c] * B[r] + A[3 + c] * B[3 + r] + A[6 + c] * B[6 + r];
          if (same && Math.abs(pose[at] - v) > 1e-12) same = false;
          pose[at++] = v;
        }
      for (let c = 0; c < 3; c++) {
        const v = A[c] * dx + A[3 + c] * dy + A[6 + c] * dz;
        if (same && Math.abs(pose[at] - v) > 1e-9) same = false;
        pose[at++] = v;
      }
      let nx;
      let ny;
      let nz;
      if (same) {
        const n = memo.n;
        nx = A[0] * n[0] + A[1] * n[1] + A[2] * n[2];
        ny = A[3] * n[0] + A[4] * n[1] + A[5] * n[2];
        nz = A[6] * n[0] + A[7] * n[1] + A[8] * n[2];
      } else {
        const n = memo.n;
        const warm = memo.fresh ? [A[0] * n[0] + A[1] * n[1] + A[2] * n[2], A[3] * n[0] + A[4] * n[1] + A[5] * n[2], A[6] * n[0] + A[7] * n[1] + A[8] * n[2]] : null;
        const hints = [...ri.axes.map((axis) => [axis, ci]), ...rj.axes.map((axis) => [axis, cj]), [[0, 0, 1], cams.world]];
        hints.centroids = [ri.centroid, rj.centroid];
        const hit = t3Gjk(ri.cloud, ci, rj.cloud, cj, warm, 8, hints);
        solved++;
        nx = hit.n[0];
        ny = hit.n[1];
        nz = hit.n[2];
        n[0] = A[0] * nx + A[3] * ny + A[6] * nz;
        n[1] = A[1] * nx + A[4] * ny + A[7] * nz;
        n[2] = A[2] * nx + A[5] * ny + A[8] * nz;
        memo.margin = hit.margin;
        memo.fresh = true;
      }
      if (memo.margin < -0.08) unseparated++;
      const V = cams.world.V;
      return nx * V[0] + ny * V[1] + nz * V[2];
    };
    for (let p = 0; p < dynamic.length; p += 2) {
      const i = dynamic[p];
      const j = dynamic[p + 1];
      if (!t3Overlap(frames[i].box, frames[j].box, -0.05)) continue;
      const s = cross(i, j);
      if (s < 1e-7 && s > -1e-7) continue;
      const li = local.get(i);
      const lj = local.get(j);
      if (s > 0) addEdge(li, lj);
      else addEdge(lj, li);
    }
    const loose = layer.free;
    if (loose && loose.length) {
      const isLoose = layer.looseAt;
      for (let a = 0; a < loose.length; a++) {
        const i = loose[a];
        const gi = runs[i].group;
        const bi = frames[i].box;
        for (let b = 0; b < count; b++) {
          const j = parts[b];
          if (j === i || runs[j].group === gi) continue;
          if (isLoose[b] && j < i) continue;
          if (!t3Overlap(bi, frames[j].box, -0.05)) continue;
          const s = cross(i, j);
          if (s < 1e-7 && s > -1e-7) continue;
          const li = local.get(i);
          if (s > 0) addEdge(li, b);
          else addEdge(b, li);
        }
      }
    }
    const heap = layer._heap ?? (layer._heap = new Int32Array(count));
    const done = layer._done ?? (layer._done = new Uint8Array(count));
    done.fill(0);
    let size = 0;
    const less = (a, b) => rank[a] < rank[b];
    const push = (v) => {
      let i = size++;
      heap[i] = v;
      while (i > 0) {
        const p = i - 1 >> 1;
        if (!less(heap[i], heap[p])) break;
        const tmp = heap[i];
        heap[i] = heap[p];
        heap[p] = tmp;
        i = p;
      }
    };
    const pop = () => {
      const top = heap[0];
      heap[0] = heap[--size];
      let i = 0;
      for (; ; ) {
        const l = 2 * i + 1;
        const r = l + 1;
        let s = i;
        if (l < size && less(heap[l], heap[s])) s = l;
        if (r < size && less(heap[r], heap[s])) s = r;
        if (s === i) break;
        const tmp = heap[i];
        heap[i] = heap[s];
        heap[s] = tmp;
        i = s;
      }
      return top;
    };
    for (let v = 0; v < count; v++) if (indeg[v] === 0) push(v);
    const out = new Int32Array(count);
    let placed = 0;
    let forced = 0;
    let refined = 0;
    let tested = false;
    const mark = layer._mark && layer._mark.length >= count ? layer._mark : layer._mark = new Uint8Array(count);
    const via = layer._via && layer._via.length >= count ? layer._via : layer._via = new Int32Array(count);
    const iter = layer._iter && layer._iter.length >= count ? layer._iter : layer._iter = new Int32Array(count);
    const stack = layer._stack && layer._stack.length >= count ? layer._stack : layer._stack = new Int32Array(count);
    const checked = layer._checked && layer._checked.length >= maxEdges ? layer._checked : layer._checked = new Uint8Array(maxEdges);
    checked.fill(0, 0, edges);
    const breakCycle = () => {
      mark.fill(0, 0, count);
      for (let root = 0; root < count; root++) {
        if (done[root] || mark[root]) continue;
        let top = 0;
        stack[top++] = root;
        mark[root] = 1;
        iter[root] = head[root];
        while (top) {
          const v = stack[top - 1];
          let e = iter[v];
          while (e >= 0 && (!live[e] || done[to[e]] || mark[to[e]] === 2)) e = next[e];
          if (e < 0) {
            mark[v] = 2;
            top--;
            continue;
          }
          iter[v] = next[e];
          const w = to[e];
          if (mark[w] === 1) {
            let dropped = false;
            let x = v;
            let edge = e;
            for (; ; ) {
              if (!checked[edge]) {
                checked[edge] = 1;
                const a = x;
                const b = to[edge];
                if (t3Disjoint(frames[parts[a]], frames[parts[b]], 0.1)) {
                  live[edge] = 0;
                  indeg[b]--;
                  refined++;
                  dropped = true;
                  if (indeg[b] === 0) push(b);
                }
              }
              if (x === w) break;
              edge = via[x];
              let from = -1;
              for (let s = 0; s < top; s++) if (stack[s] === x) from = s > 0 ? stack[s - 1] : -1;
              if (from < 0) break;
              x = from;
            }
            return dropped ? 1 : 0;
          }
          via[w] = e;
          mark[w] = 1;
          iter[w] = head[w];
          stack[top++] = w;
        }
      }
      return -1;
    };
    while (placed < count) {
      if (size === 0) {
        let broken = 0;
        for (let tries = 0; tries < 64 && size === 0; tries++) {
          const result = breakCycle();
          if (result <= 0) break;
          broken++;
        }
        if (size) continue;
        void broken;
        void tested;
        let pick = -1;
        for (let v2 = 0; v2 < count; v2++) if (!done[v2] && (pick < 0 || indeg[v2] < indeg[pick] || indeg[v2] === indeg[pick] && rank[v2] < rank[pick])) pick = v2;
        forced++;
        indeg[pick] = 0;
        push(pick);
      }
      const v = pop();
      if (done[v]) continue;
      done[v] = 1;
      out[placed++] = parts[v];
      for (let e = head[v]; e >= 0; e = next[e]) {
        if (!live[e]) continue;
        const w = to[e];
        if (done[w]) continue;
        if (--indeg[w] === 0) push(w);
      }
    }
    if (stats) {
      stats.edges = (stats.edges ?? 0) + edges;
      stats.forced = (stats.forced ?? 0) + forced;
      stats.refined = (stats.refined ?? 0) + refined;
      stats.unseparated = (stats.unseparated ?? 0) + unseparated;
      stats.solved = (stats.solved ?? 0) + solved;
    }
    return out;
  }
  function t3Keep(values) {
    const n = values.length;
    const tails = [];
    const tailAt = [];
    const back = new Int32Array(n).fill(-1);
    for (let i = 0; i < n; i++) {
      let lo = 0;
      let hi = tails.length;
      while (lo < hi) {
        const mid = lo + hi >> 1;
        if (tails[mid] < values[i]) lo = mid + 1;
        else hi = mid;
      }
      tails[lo] = values[i];
      tailAt[lo] = i;
      back[i] = lo > 0 ? tailAt[lo - 1] : -1;
    }
    const keep = new Uint8Array(n);
    let k = tails.length ? tailAt[tails.length - 1] : -1;
    while (k >= 0) {
      keep[k] = 1;
      k = back[k];
    }
    return keep;
  }
  function t3Cams(scene, values) {
    const poses = t3Poses(scene.groups, values);
    const cams = poses.map((pose) => t3Camera(scene.P, pose));
    cams.world = t3Camera(scene.P, null);
    cams.poses = poses;
    return cams;
  }
  function t3Mount(stage, data, { onHold = null, onFrame = null, follow = null, painter = "svg" } = {}) {
    void painter;
    const layerEls = new Map([...stage.querySelectorAll("svg[data-live]")].map((svg) => [svg.dataset.live, svg]));
    const first = layerEls.values().next().value;
    const viewWidth = first && first.viewBox && first.viewBox.baseVal ? first.viewBox.baseVal.width : 0;
    const unitOf = () => {
      const width = first ? first.getBoundingClientRect().width : 0;
      return viewWidth && width ? Math.round(width / viewWidth * 100) / 100 : 1;
    };
    let unit = unitOf();
    let scene = t3Prepare(data, { unit });
    const runs = () => scene.runs;
    const count = data.parts.length;
    const nodes = new Array(count);
    const bound = new Array(count);
    const cache = new Array(count);
    const containers = /* @__PURE__ */ new Map();
    for (const [name, svg] of layerEls) containers.set(name, svg.querySelector(".iso-parts") ?? svg);
    for (const run of scene.runs) {
      const layer = data.layers[run.layer];
      const container = containers.get(layer.name);
      const node = container ? container.querySelector(`[data-p="${run.index}"]`) : null;
      nodes[run.index] = node;
      const map = {};
      if (node) {
        map.move = node;
        node.querySelectorAll("[data-r]").forEach((el) => map[el.getAttribute("data-r")] = el);
      }
      bound[run.index] = run.roles.map((role) => map[role.name] ?? null);
      cache[run.index] = run.roles.map(() => ({ d: null, q: null, b: null, f: null, w: null, t: null, o: null, cx: null, cy: null }));
    }
    const frames = scene.runs.map((run) => t3Frame(run));
    const values = Object.fromEntries(data.groups.map((g) => [g.name, data.values ? data.values[g.name] ?? 0 : 0]));
    let lastPoses = null;
    let cams = null;
    const orders = scene.layers.map((layer) => Int32Array.from(layer.rest));
    const changes = [];
    const stats = { ms: 0, writes: 0, moved: 0, forced: 0, refined: 0, unseparated: 0, emitted: 0 };
    let writes = 0;
    const write = (index) => {
      const run = scene.runs[index];
      const f = frames[index];
      const els = bound[index];
      const memo = cache[index];
      for (let r = 0; r < run.roles.length; r++) {
        const el = els[r];
        if (!el) continue;
        const role = run.roles[r];
        const c = memo[r];
        const type = role.type;
        if (type === "path" || type === "face" || type === "slot") {
          const d = f.d[r];
          if (c.d !== d) {
            el.setAttribute("d", d);
            c.d = d;
            writes++;
          }
          if (type === "face") {
            const q = f.q[r];
            if (c.q !== q) {
              const band = Math.min(3, Math.floor(q / T3_Q));
              const mix = (q - T3_Q * band) / T3_Q;
              if (c.b !== band) {
                el.setAttribute("data-b", String(band));
                c.b = band;
                writes++;
              }
              if (c.f !== mix) {
                if (mix) el.style.setProperty("--f", String(mix));
                else el.style.removeProperty("--f");
                c.f = mix;
                writes++;
              }
              c.q = q;
            }
            const w = f.w[r];
            if (c.w !== w) {
              if (w < 0) el.style.removeProperty("stroke-width");
              else el.style.strokeWidth = String(w);
              c.w = w;
              writes++;
            }
          } else if (type === "slot") {
            const o = f.o[r];
            if (c.o !== o) {
              el.setAttribute("opacity", String(Math.round(o * 1e3) / 1e3));
              c.o = o;
              writes++;
            }
          }
        } else if (type === "xform" || type === "self" || type === "plane") {
          const t = f.t[r];
          if (c.t !== t) {
            if (t) el.setAttribute("transform", t);
            else el.removeAttribute("transform");
            c.t = t;
            writes++;
          }
          if (type === "plane") {
            const o = f.o[r];
            if (c.o !== o) {
              el.setAttribute("opacity", String(o));
              c.o = o;
              writes++;
            }
          }
        } else if (type === "dot") {
          const x = Math.round(f.cx[r] * 100) / 100;
          const y = Math.round(f.cy[r] * 100) / 100;
          const o = f.o[r];
          if (c.cx !== x) {
            el.setAttribute("cx", String(x));
            c.cx = x;
            writes++;
          }
          if (c.cy !== y) {
            el.setAttribute("cy", String(y));
            c.cy = y;
            writes++;
          }
          if (c.o !== o) {
            el.setAttribute("fill-opacity", String(o));
            c.o = o;
            writes++;
          }
        }
      }
    };
    const samePose = (a, b) => {
      if (!a || !b) return false;
      for (let i = 0; i < 9; i++) if (a.R[i] !== b.R[i]) return false;
      return a.t[0] === b.t[0] && a.t[1] === b.t[1] && a.t[2] === b.t[2];
    };
    let lastUnit = unit;
    let moved = 0;
    const render = () => {
      const t0 = performance.now();
      writes = 0;
      moved = 0;
      cams = t3Cams(scene, values);
      t3State.detail = detail;
      const poses = cams.poses;
      const fresh = lastUnit !== unit || !lastPoses;
      let emitted = 0;
      for (const run of scene.runs) {
        const g = run.group;
        const changed = fresh || (g >= 0 ? !samePose(poses[g], lastPoses[g]) : false);
        if (!changed) continue;
        t3Emit(run, g >= 0 ? cams[g] : cams.world, frames[run.index]);
        write(run.index);
        emitted++;
      }
      lastPoses = poses;
      lastUnit = unit;
      const orderStats = { forced: 0, refined: 0, unseparated: 0, edges: 0 };
      scene.layers.forEach((layer, index) => {
        const previous = orders[index];
        const order = t3Order(layer, frames, cams, previous, orderStats, scene);
        let same = true;
        for (let j = 0; j < order.length; j++)
          if (order[j] !== previous[j]) {
            same = false;
            break;
          }
        if (same) return;
        const container = containers.get(layer.name);
        const position = /* @__PURE__ */ new Map();
        previous.forEach((global, at) => position.set(global, at));
        const keep = t3Keep(Array.from(order, (global) => position.get(global)));
        let after = null;
        const shifted = [];
        for (let j = order.length - 1; j >= 0; j--) {
          const node = nodes[order[j]];
          if (!keep[j] && node && container) {
            container.insertBefore(node, after);
            moved++;
            shifted.push(scene.runs[order[j]].name);
          }
          if (node) after = node;
        }
        orders[index] = order;
        if (shifted.length) changes.push({ layer: layer.name, moved: shifted });
      });
      stats.ms = performance.now() - t0;
      stats.writes = writes;
      stats.moved = moved;
      stats.forced = orderStats.forced;
      stats.refined = orderStats.refined;
      stats.unseparated = orderStats.unseparated;
      stats.emitted = emitted;
      t3State.detail = 1;
      if (onFrame) onFrame(controller);
      return { ...stats };
    };
    let detail = 1;
    const set = (next, options) => {
      if (options && options.detail !== void 0) {
        const value = Math.max(0, Math.min(1, options.detail));
        if (value !== detail) {
          detail = value;
          lastPoses = null;
        }
      }
      if (typeof next === "number") {
        const g = data.groups.find((group) => group.kind === "turn");
        if (g) values[g.name] = next;
      } else if (next) for (const [name, value] of Object.entries(next)) values[name] = value;
      if (follow) Object.assign(values, follow({ ...values }));
      return render();
    };
    let unwrap = /* @__PURE__ */ new Map();
    const angleAt = (clientX, clientY, z = 0, groupName) => {
      const svg = first;
      const box = svg.getBoundingClientRect();
      const vb = svg.viewBox.baseVal;
      const x = vb.x + (clientX - box.left) / box.width * vb.width;
      const y = vb.y + (clientY - box.top) / box.height * vb.height;
      const c = t3Camera(scene.P, null);
      const p = (x - c.ox) / c.k;
      const q = (y - c.oy + z * c.ce * c.k) / (c.se * c.k);
      const wx = p * c.sa + q * c.ca;
      const wy = -p * c.ca + q * c.sa;
      const group = data.groups.find((g) => g.name === groupName) ?? data.groups.find((g) => g.kind === "turn");
      const pivot = group ? group.origin : [0, 0, 0];
      const raw = Math.atan2(wy - pivot[1], wx - pivot[0]) * 180 / Math.PI;
      const key = group ? group.name : "";
      const last = unwrap.get(key);
      let angle = raw;
      if (last !== void 0) angle = last + ((raw - last) % 360 + 540) % 360 - 180;
      unwrap.set(key, angle);
      return angle;
    };
    const observer = typeof ResizeObserver === "function" && first ? new ResizeObserver(() => {
      const next = unitOf();
      if (Math.abs(next - unit) < 0.05) return;
      unit = next;
      scene = t3Prepare(data, { unit });
      render();
    }) : null;
    if (observer) observer.observe(first);
    if (follow) Object.assign(values, follow({ ...values }));
    const controller = {
      set,
      render,
      angleAt,
      get values() {
        return { ...values };
      },
      cover: (names, options) => t3Cover(controller, names, options),
      order: (name) => {
        const index = name === void 0 ? 0 : scene.layers.findIndex((layer) => layer.name === name);
        return index < 0 ? [] : Array.from(orders[index], (global) => scene.runs[global].name);
      },
      orderIndex: (name) => {
        const index = name === void 0 ? 0 : scene.layers.findIndex((layer) => layer.name === name);
        return index < 0 ? null : orders[index];
      },
      events: () => changes.splice(0, changes.length),
      stats: () => ({ ...stats }),
      frames: () => frames,
      cams: () => cams,
      scene: () => scene,
      pose: (name) => t3PoseOf(scene, cams, name),
      detach: (name) => {
        const index = scene.groups.findIndex((g) => g.name === name);
        const pose = t3PoseOf(scene, cams, name);
        const o = scene.groups[index].origin;
        return { world: true, R: pose.R, t: [pose.t[0] - o[0], pose.t[1] - o[1], pose.t[2] - o[2]] };
      },
      anchor: (name, point, direction) => t3Anchor(scene, cams, name, point, direction),
      destroy: () => {
        if (observer) observer.disconnect();
        if (typeof window !== "undefined" && window.__isoTurn && window.__isoTurn.controller === controller) delete window.__isoTurn;
      }
    };
    const hold = () => {
      if (onHold) onHold();
    };
    if (typeof window !== "undefined") {
      window.__isoTurn = {
        controller,
        set(next) {
          hold();
          return set(next);
        },
        get() {
          hold();
          return { ...values };
        },
        order(name) {
          hold();
          return controller.order(name);
        },
        events() {
          hold();
          return controller.events();
        },
        stats() {
          hold();
          return controller.stats();
        },
        layers() {
          hold();
          return scene.layers.map((layer) => layer.name);
        }
      };
    }
    render();
    return controller;
  }
  function t3Enclose(points, edges) {
    const hull = t3Hull(points);
    const n = hull.length;
    if (n < 3) return [];
    let area = 0;
    for (let i = 0; i < n; i++) area += hull[i][0] * hull[(i + 1) % n][1] - hull[(i + 1) % n][0] * hull[i][1];
    const sign = area >= 0 ? 1 : -1;
    let lines = [];
    for (let i = 0; i < n; i++) {
      const p = hull[i];
      const q = hull[(i + 1) % n];
      const dx = q[0] - p[0];
      const dy = q[1] - p[1];
      const l = Math.hypot(dx, dy);
      if (l < 1e-9) continue;
      const nx = sign * dy / l;
      const ny = -sign * dx / l;
      lines.push([nx, ny, -(nx * p[0] + ny * p[1])]);
    }
    const meet = (A, B) => {
      const det = A[0] * B[1] - A[1] * B[0];
      if (Math.abs(det) < 1e-12) return null;
      return [(-A[2] * B[1] + B[2] * A[1]) / det, (-A[0] * B[2] + B[0] * A[2]) / det];
    };
    while (lines.length > edges) {
      let best = -1;
      let cost = Infinity;
      const m = lines.length;
      for (let i = 0; i < m; i++) {
        const prev = lines[(i - 1 + m) % m];
        const self = lines[i];
        const next = lines[(i + 1) % m];
        const turn = prev[0] * next[1] - prev[1] * next[0];
        if (sign * turn <= 1e-9) continue;
        const apex = meet(prev, next);
        const a = meet(prev, self);
        const b = meet(self, next);
        if (!apex || !a || !b) continue;
        const added = Math.abs((a[0] - apex[0]) * (b[1] - apex[1]) - (a[1] - apex[1]) * (b[0] - apex[0])) / 2;
        if (added < cost) {
          cost = added;
          best = i;
        }
      }
      if (best < 0) break;
      lines.splice(best, 1);
    }
    return lines;
  }
  function t3Cover(controller, names, { polygons = 6, edges = 10, pad = 0.3, layers = null } = {}) {
    const uCoverEdge = new Float32Array(polygons * edges * 3);
    const uCoverCount = new Float32Array(polygons);
    const scene = controller.scene();
    const frames = controller.frames();
    const sets = Array.isArray(names) ? names.length && Array.isArray(names[0]) ? names : [names] : [[names]];
    const candidates = [];
    const taken = /* @__PURE__ */ new Set();
    for (const list of sets) {
      const targets = scene.runs.filter((run) => list.includes(run.name));
      if (!targets.length) continue;
      const box = [Infinity, Infinity, -Infinity, -Infinity];
      for (const run of targets) {
        const b = frames[run.index].box;
        box[0] = Math.min(box[0], b[0]);
        box[1] = Math.min(box[1], b[1]);
        box[2] = Math.max(box[2], b[2]);
        box[3] = Math.max(box[3], b[3]);
      }
      const home = targets[0].layer;
      scene.layers.forEach((layer, index) => {
        const order = controller.orderIndex(layer.name);
        if (!order) return;
        let from = 0;
        if (index === home) {
          for (let at = 0; at < order.length; at++) if (targets.some((run) => run.index === order[at])) from = at + 1;
        } else if (!(layers && layers.includes(layer.name)) || index < home) return;
        for (let at = from; at < order.length; at++) {
          const run = scene.runs[order[at]];
          if (list.includes(run.name) || taken.has(run.index)) continue;
          const f = frames[run.index];
          const b = f.box;
          if (!(b[0] < box[2] + pad && box[0] < b[2] + pad && b[1] < box[3] + pad && box[1] < b[3] + pad)) continue;
          if (!targets.some((target) => !t3Disjoint(frames[target.index], f, -pad))) continue;
          taken.add(run.index);
          const share = (Math.min(b[2], box[2]) - Math.max(b[0], box[0])) * (Math.min(b[3], box[3]) - Math.max(b[1], box[1]));
          candidates.push({ run, f, share });
        }
      });
    }
    candidates.sort((a, b) => b.share - a.share);
    const parts = [];
    let slot = 0;
    for (const { run, f } of candidates) {
      if (slot >= polygons) break;
      const points = [];
      if (f.quadN) for (const [buf, count] of f.quadList) for (let i = 0; i < count; i++) points.push([buf[2 * i], buf[2 * i + 1]]);
      else for (let i = 0; i < f.hullN; i++) points.push([f.hull[2 * i], f.hull[2 * i + 1]]);
      const lines = t3Enclose(points, edges);
      if (!lines.length) continue;
      lines.forEach((line, e) => {
        const at = (slot * edges + e) * 3;
        uCoverEdge[at] = line[0];
        uCoverEdge[at + 1] = line[1];
        uCoverEdge[at + 2] = line[2] - pad;
      });
      uCoverCount[slot] = lines.length;
      parts.push(run.name);
      slot++;
    }
    return { uCoverEdge, uCoverCount, dropped: Math.max(0, candidates.length - slot), parts };
  }
  function t3PoseOf(scene, cams, name) {
    const index = scene.groups.findIndex((g) => g.name === name);
    const cam = index >= 0 && cams ? cams[index] : null;
    return { R: cam ? Array.from(cam.R) : Array.from(T3_EYE), t: cam ? [cam.t[0], cam.t[1], cam.t[2]] : [0, 0, 0] };
  }
  function t3Anchor(scene, cams, name, point, direction) {
    const index = name === null || name === void 0 ? -1 : scene.groups.findIndex((g) => g.name === name);
    const cam = index >= 0 ? cams[index] : cams.world;
    const o = index >= 0 ? scene.groups[index].origin : [0, 0, 0];
    const R = cam.R;
    const q = [point[0] - o[0], point[1] - o[1], point[2] - o[2]];
    const world = [R[0] * q[0] + R[1] * q[1] + R[2] * q[2] + cam.t[0], R[3] * q[0] + R[4] * q[1] + R[5] * q[2] + cam.t[1], R[6] * q[0] + R[7] * q[1] + R[8] * q[2] + cam.t[2]];
    const w = cams.world;
    const screen = [w.ox + w.m[0] * world[0] + w.m[1] * world[1] + w.m[2] * world[2], w.oy + w.m[3] * world[0] + w.m[4] * world[1] + w.m[5] * world[2]];
    const out = { world, screen };
    if (direction) out.direction = [R[0] * direction[0] + R[1] * direction[1] + R[2] * direction[2], R[3] * direction[0] + R[4] * direction[1] + R[5] * direction[2], R[6] * direction[0] + R[7] * direction[1] + R[8] * direction[2]];
    return out;
  }
  function t3FloorOf(scene, name, R = T3_EYE) {
    const index = scene.groups.findIndex((g) => g.name === name);
    let low = Infinity;
    for (const run of scene.runs) {
      if (run.group !== index) continue;
      const c = run.cloud;
      for (let i = 0; i < c.length; i += 3) {
        const z = R[6] * c[i] + R[7] * c[i + 1] + R[8] * c[i + 2];
        if (z < low) low = z;
      }
    }
    return low;
  }
  function t3Compose(A, B) {
    return Array.from(t3Mul(A, B));
  }
  function t3PoseUniforms(controller, group, prefix = "uGroup") {
    const scene = controller.scene();
    const index = scene.groups.findIndex((g) => g.name === group);
    const cams = controller.cams();
    const cam = index >= 0 && cams ? cams[index] : null;
    const R = cam ? cam.R : T3_EYE;
    const t = cam ? cam.t : [0, 0, 0];
    const o = index >= 0 ? scene.groups[index].origin : [0, 0, 0];
    const T = [t[0] - (R[0] * o[0] + R[1] * o[1] + R[2] * o[2]), t[1] - (R[3] * o[0] + R[4] * o[1] + R[5] * o[2]), t[2] - (R[6] * o[0] + R[7] * o[1] + R[8] * o[2])];
    return { [`${prefix}X`]: [R[0], R[3], R[6]], [`${prefix}Y`]: [R[1], R[4], R[7]], [`${prefix}Z`]: [R[2], R[5], R[8]], [`${prefix}T`]: T };
  }
  var T3_MAT_KEYS = ["paper", "face", "top", "shade-0", "shade-1", "shade-2", "shade-3", "lit-top", "lit-shade", "hi", "mid", "lo", "faint", "dot", "lit"];
  var T3_MAT_TUBE = ["body", "shine", "shade", "edge"];
  var T3_MATERIALS = {
    gold: {
      light: ["#d3bb88", "#e4d2a8", "#f1e5c6", "#a1844f", "#bc9f69", "#d3bb88", "#e4d2a8", "#f8efd8", "#dfcb9c", "#4b3920", "#86693f", "#a98c5b", "#c1a676", "#4a381f", "#2a1d0c", "#cdb07a", "#f3e8cc", "#8e7044", "#4b3920"],
      dark: ["#3f3521", "#4b3f28", "#5a4c31", "#2b2416", "#352c1b", "#3f3521", "#4b3f28", "#6a5a3b", "#4f4329", "#e6d2a3", "#8a7550", "#5e4e33", "#463a26", "#e6d2a3", "#fff3d6", "#4a3e27", "#8c7853", "#251f13", "#e6d2a3"]
    },
    chrome: {
      light: ["#8e959c", "#c3c8cd", "#f7f8f9", "#a2a9b0", "#6f767d", "#454b52", "#cacfd4", "#ffffff", "#bcc2c8", "#202428", "#585e65", "#878d94", "#a9afb5", "#2a2e33", "#000000", "#8b9299", "#fbfcfd", "#3c4248", "#202428"],
      dark: ["#2a2e32", "#4a5056", "#6e757c", "#2e3236", "#24272b", "#1a1d20", "#4a5056", "#848b92", "#3a3f44", "#dfe3e7", "#7c838a", "#4d5359", "#363b40", "#e4e7ea", "#ffffff", "#34393e", "#9aa1a8", "#16191b", "#dfe3e7"]
    },
    steel: {
      light: ["#b8bdc1", "#cdd1d4", "#e5e8ea", "#8f959b", "#a4aaaf", "#b8bdc1", "#cdd1d4", "#f1f3f4", "#c6cacd", "#2b2f33", "#6b7177", "#959ba1", "#aeb3b8", "#33373b", "#000000", "#b3b8bd", "#eef0f2", "#7d8389", "#2b2f33"],
      dark: ["#2c3034", "#34393d", "#3e4348", "#1f2225", "#25292c", "#2c3034", "#34393d", "#4a5056", "#33383c", "#d0d4d8", "#727980", "#4a5056", "#33383d", "#d8dce0", "#ffffff", "#30353a", "#5c6369", "#1a1d20", "#d0d4d8"]
    },
    gunmetal: {
      light: ["#444a51", "#50575e", "#5f666e", "#2f3439", "#393f45", "#444a51", "#50575e", "#6d757d", "#4b5258", "#0f1113", "#1d2125", "#272b30", "#30353a", "#b0b5ba", "#000000", "#3d4349", "#6e757c", "#24282c", "#0f1113"],
      dark: ["#1d2125", "#22272b", "#2a2f34", "#15181b", "#191c20", "#1d2125", "#22272b", "#323840", "#20252a", "#a9b0b7", "#5c636a", "#3a4046", "#2a2f34", "#b8bec4", "#ffffff", "#1f2327", "#3a4046", "#111316", "#a9b0b7"]
    },
    rubber: {
      light: ["#2a2b2e", "#34363a", "#46484d", "#1b1c1e", "#222326", "#2a2b2e", "#34363a", "#55575c", "#2f3134", "#070708", "#111214", "#18191b", "#1f2023", "#6a6c70", "#000000", "#27282b", "#5b5d62", "#121314", "#050506"],
      dark: ["#121213", "#161618", "#1c1c1f", "#0c0c0d", "#0f0f10", "#121213", "#161618", "#232327", "#141416", "#8c8e92", "#4a4c50", "#2c2d30", "#1f2023", "#9a9ca0", "#ffffff", "#131315", "#2b2c30", "#0a0a0b", "#8c8e92"]
    },
    brass: {
      light: ["#bd9646", "#d2ad5b", "#e6c87e", "#8a6a2c", "#a47f38", "#bd9646", "#d2ad5b", "#f0d796", "#c8a252", "#3f2e0e", "#765a24", "#9a7a3c", "#b08c46", "#3a2a0c", "#1f1606", "#b8913f", "#efd795", "#7d5f26", "#3f2e0e"],
      dark: ["#3d3017", "#49391c", "#574523", "#2a210f", "#332813", "#3d3017", "#49391c", "#66522b", "#45371b", "#e9cf8a", "#8e7438", "#5e4c25", "#44371c", "#e9cf8a", "#fff0c8", "#433419", "#8a6f36", "#21190b", "#e9cf8a"]
    },
    copper: {
      light: ["#b3633e", "#c9784f", "#df9670", "#7c4128", "#9a5132", "#b3633e", "#c9784f", "#eaa985", "#be6d46", "#3a1a0c", "#6e3820", "#925037", "#a65d3f", "#3a1a0c", "#1c0b04", "#ad5f3b", "#f0b896", "#6e3720", "#3a1a0c"],
      dark: ["#3d1f13", "#492617", "#582e1c", "#2a160d", "#331a10", "#3d1f13", "#492617", "#673722", "#432215", "#eaa985", "#8f5236", "#5f3624", "#45271a", "#eaa985", "#ffe0cc", "#42221a", "#8a4c31", "#1f0f08", "#eaa985"]
    }
  };
  function t3MaterialCss() {
    const rules = [];
    const block = (values) => T3_MAT_KEYS.map((key, i) => `--anatomy-${key}:${values[i]}`).concat(T3_MAT_TUBE.map((key, i) => `--mat-${key}:${values[T3_MAT_KEYS.length + i]}`)).join(";");
    for (const [name, { light, dark }] of Object.entries(T3_MATERIALS)) {
      rules.push(`[data-mat="${name}"]{${block(dark)}}`);
      rules.push(`.iso[data-theme="light"] [data-mat="${name}"]{${block(light)}}`);
      rules.push(`.iso[data-theme="dark"] [data-mat="${name}"]{${block(dark)}}`);
    }
    rules.push("[data-mat] .tb-body{fill:var(--mat-body)}");
    rules.push("[data-mat] .tb-shine{fill:var(--mat-shine)}");
    rules.push("[data-mat] .tb-shade{fill:var(--mat-shade)}");
    rules.push("[data-mat] .tb-edge{stroke:var(--mat-edge)}");
    return rules.join("\n");
  }
  function t3Css() {
    const rules = [];
    const ramp = "--tn-0:var(--anatomy-shade-0);--tn-1:var(--anatomy-shade-1);--tn-2:var(--anatomy-shade-2);--tn-3:var(--anatomy-shade-3);--tn-4:var(--anatomy-top)";
    rules.push(`.iso-live{${ramp}}`);
    rules.push(`.iso-live [data-mat]{${ramp}}`);
    rules.push(".iso-live [data-lit]{--tn-0:var(--anatomy-lit-shade);--tn-1:var(--anatomy-lit-shade);--tn-2:var(--anatomy-lit-shade);--tn-3:var(--anatomy-lit-shade);--tn-4:var(--anatomy-lit-top)}");
    const colour = "color-mix(in srgb,var(--ta) calc(100% - var(--f,0) * 100%),var(--tb))";
    rules.push(`.iso-tn{stroke-width:.4;stroke-linejoin:round;--ta:var(--tn-0);--tb:var(--tn-1);fill:${colour};stroke:${colour}}`);
    for (let i = 1; i < 4; i++) rules.push(`.iso-tn[data-b="${i}"]{--ta:var(--tn-${i});--tb:var(--tn-${i + 1})}`);
    rules.push(t3MaterialCss());
    for (const hue of ["red", "green", "blue"]) rules.push(`.tb[data-hue="${hue}"]{--tb-ink:var(--anatomy-${hue})}`);
    rules.push(".tb[data-hue] .tb-body{fill:color-mix(in srgb,var(--tb-ink) 54%,var(--anatomy-shade-2))}");
    rules.push(".tb[data-hue] .tb-shine{fill:color-mix(in srgb,var(--tb-ink) 16%,var(--anatomy-top))}");
    rules.push(".tb[data-hue] .tb-shade{fill:color-mix(in srgb,var(--tb-ink) 30%,var(--anatomy-hi))}");
    rules.push(".tb[data-hue] .tb-edge{stroke:color-mix(in srgb,var(--tb-ink) 38%,var(--anatomy-hi))}");
    rules.push(".tb[data-hue][data-mat] .tb-body{fill:color-mix(in srgb,var(--tb-ink) 62%,var(--mat-body))}");
    rules.push(".tb[data-hue][data-mat] .tb-shine{fill:color-mix(in srgb,var(--tb-ink) 22%,var(--mat-shine))}");
    rules.push(".tb[data-hue][data-mat] .tb-shade{fill:color-mix(in srgb,var(--tb-ink) 46%,var(--mat-shade))}");
    rules.push(".tb[data-hue][data-mat] .tb-edge{stroke:color-mix(in srgb,var(--tb-ink) 30%,var(--mat-edge))}");
    rules.push(".iso-turn{position:relative}");
    rules.push(".iso-turn>.iso-layer{position:absolute;inset:0;width:100%;height:100%;pointer-events:none}");
    return rules.join("\n");
  }
  var TURN = { materials: Object.keys(T3_MATERIALS), materialCss: t3MaterialCss, rotation: (axis, degrees) => Array.from(t3Rot(axis, degrees)), quat: (q) => Array.from(t3Quat(q)), compose: t3Compose, floorOf: t3FloorOf, anchor: t3Anchor, camera: t3Camera, poses: t3PosesMap, prepare: t3Prepare, emit: t3Emit, order: t3Order, mount: t3Mount, cover: t3Cover, poseUniforms: t3PoseUniforms, css: t3Css, frame: t3Frame, cams: t3Cams, gjk: t3Gjk, hintsOf: (ri, ci, rj, cj, world) => Object.assign([...ri.axes.map((axis) => [axis, ci]), ...rj.axes.map((axis) => [axis, cj]), [[0, 0, 1], world]], { centroids: [ri.centroid, rj.centroid] }), disjoint: t3Disjoint, levels: T3_LEVELS, q: T3_Q, exact: (on) => {
    t3State.exact = Boolean(on);
  } };
  var TURN_CSS = t3Css();

  // third_party/anatomy/kit/iso-kit.mjs
  var AZIMUTH = 45;
  var ELEVATION = 30;
  var RADIANS = Math.PI / 180;
  var UNIT = Math.sqrt(1.6);
  function cameraOf({ scale, azimuth = AZIMUTH, elevation = ELEVATION }) {
    const a = azimuth * RADIANS;
    const e = elevation * RADIANS;
    return { sinA: Math.sin(a), cosA: Math.cos(a), sinE: Math.sin(e), cosE: Math.cos(e), k: scale * UNIT };
  }
  function iso([x, y, z], projection) {
    const { origin } = projection;
    const { sinA, cosA, sinE, cosE, k } = cameraOf(projection);
    return [origin[0] + (x * sinA - y * cosA) * k, origin[1] + ((x * cosA + y * sinA) * sinE - z * cosE) * k];
  }

  // third_party/anatomy/kit/gl.mjs
  var GLSL_ISO = `precision highp float;
uniform vec2 uCanvas;
uniform vec2 uView;
uniform vec2 uOrigin;
uniform float uK;
uniform vec4 uCam;
uniform float uTime;
vec2 viewOf(vec2 frag){return vec2(frag.x,uCanvas.y-frag.y)*(uView.x/uCanvas.x);}
vec2 project(vec3 p){return uOrigin+uK*vec2(p.x*uCam.x-p.y*uCam.y,(p.x*uCam.y+p.y*uCam.x)*uCam.z-p.z*uCam.w);}
vec3 towardViewer(){return vec3(uCam.y*uCam.w,uCam.x*uCam.w,uCam.z);}
vec3 rayOf(vec2 vb){vec2 q=(vb-uOrigin)/uK;return vec3(q.x*uCam.x,-q.x*uCam.y,-q.y/uCam.w);}
float pixelOf(){return (uView.x/uCanvas.x)/uK;}
vec3 lightDir(){return normalize(vec3(-uCam.x,uCam.y,1.2));}
vec3 onFloor(vec2 vb,float h){vec2 q=(vb-uOrigin)/uK;float b=(q.y+h*uCam.w)/uCam.z;return vec3(q.x*uCam.x+b*uCam.y,-q.x*uCam.y+b*uCam.x,h);}
vec3 onWallY(vec2 vb,float y){vec2 q=(vb-uOrigin)/uK;float x=(q.x+y*uCam.y)/uCam.x;return vec3(x,y,((x*uCam.y+y*uCam.x)*uCam.z-q.y)/uCam.w);}
vec3 onWallX(vec2 vb,float x){vec2 q=(vb-uOrigin)/uK;float y=(x*uCam.x-q.x)/uCam.y;return vec3(x,y,((x*uCam.y+y*uCam.x)*uCam.z-q.y)/uCam.w);}
float hash12(vec2 p){vec3 q=fract(vec3(p.xyx)*.1031);q+=dot(q,q.yzx+33.33);return fract((q.x+q.y)*q.z);}
float hash13(vec3 p){p=fract(p*.1031);p+=dot(p,p.zyx+31.32);return fract((p.x+p.y)*p.z);}
float noise2(vec2 p){vec2 i=floor(p);vec2 f=fract(p);f=f*f*(3.-2.*f);return mix(mix(hash12(i),hash12(i+vec2(1.,0.)),f.x),mix(hash12(i+vec2(0.,1.)),hash12(i+vec2(1.,1.)),f.x),f.y);}
float noise3(vec3 p){vec3 i=floor(p);vec3 f=fract(p);f=f*f*(3.-2.*f);
  float a=mix(mix(hash13(i),hash13(i+vec3(1.,0.,0.)),f.x),mix(hash13(i+vec3(0.,1.,0.)),hash13(i+vec3(1.,1.,0.)),f.x),f.y);
  float b=mix(mix(hash13(i+vec3(0.,0.,1.)),hash13(i+vec3(1.,0.,1.)),f.x),mix(hash13(i+vec3(0.,1.,1.)),hash13(i+vec3(1.,1.,1.)),f.x),f.y);
  return mix(a,b,f.z);}
float fbm2(vec2 p){float s=0.;float a=.5;for(int i=0;i<4;i++){s+=a*noise2(p);p=p*2.07+vec2(17.1,9.2);a*=.5;}return s/.9375;}
float fbm3(vec3 p){float s=0.;float a=.5;for(int i=0;i<4;i++){s+=a*noise3(p);p=p*2.07+vec3(17.1,9.2,4.7);a*=.5;}return s/.9375;}
float window(float x,float a,float b,float soft){return smoothstep(a-soft,a+soft,x)*(1.-smoothstep(b-soft,b+soft,x));}
vec3 tonemap(vec3 c,float exposure){return 1.-exp(-c*exposure);}
`;
  function glCamera(projection) {
    const a = (projection.azimuth ?? 45) * Math.PI / 180;
    const e = (projection.elevation ?? 30) * Math.PI / 180;
    return {
      origin: [projection.origin[0], projection.origin[1]],
      k: projection.scale * Math.sqrt(1.6),
      cam: [Math.sin(a), Math.cos(a), Math.sin(e), Math.cos(e)]
    };
  }
  var VERTEX = "attribute vec2 p;void main(){gl_Position=vec4(p,0.,1.);}";
  function glLayer({ canvas, fragment, view, camera, uniforms = [], fixed = {}, extensions = [], maxRatio = 1.5, onError = (message) => console.error(message) }) {
    const gl = canvas.getContext("webgl", { premultipliedAlpha: true, alpha: true, antialias: false, preserveDrawingBuffer: false });
    if (!gl) return null;
    const compile = (type, source) => {
      const shader = gl.createShader(type);
      gl.shaderSource(shader, source);
      gl.compileShader(shader);
      if (gl.getShaderParameter(shader, gl.COMPILE_STATUS)) return shader;
      onError(gl.getShaderInfoLog(shader));
      return null;
    };
    const vs = compile(gl.VERTEX_SHADER, VERTEX);
    const enabled = extensions.filter((name) => gl.getExtension(name.replace(/^GL_/, "")));
    const fs = compile(gl.FRAGMENT_SHADER, enabled.map((name) => `#extension ${name} : enable
`).join("") + GLSL_ISO + fragment);
    if (!vs || !fs) return null;
    const program = gl.createProgram();
    gl.attachShader(program, vs);
    gl.attachShader(program, fs);
    gl.linkProgram(program);
    if (!gl.getProgramParameter(program, gl.LINK_STATUS)) {
      onError(gl.getProgramInfoLog(program));
      return null;
    }
    gl.useProgram(program);
    const buffer = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, buffer);
    gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, 3, -1, -1, 3]), gl.STATIC_DRAW);
    const position = gl.getAttribLocation(program, "p");
    gl.enableVertexAttribArray(position);
    gl.vertexAttribPointer(position, 2, gl.FLOAT, false, 0, 0);
    const where = {};
    for (const name of ["uCanvas", "uView", "uOrigin", "uK", "uCam", "uTime", ...uniforms, ...Object.keys(fixed)]) where[name] = gl.getUniformLocation(program, name);
    const types = {};
    const active = gl.getProgramParameter(program, gl.ACTIVE_UNIFORMS);
    for (let index = 0; index < active; index++) {
      const info = gl.getActiveUniform(program, index);
      if (info) types[info.name.replace(/\[0\]$/, "")] = info.type;
    }
    let painted = false;
    const fit = () => {
      const box = canvas.getBoundingClientRect();
      const ratio = Math.min(maxRatio, window.devicePixelRatio || 1);
      const width = Math.max(1, Math.round(box.width * ratio));
      const height = Math.max(1, Math.round(box.height * ratio));
      if (canvas.width !== width || canvas.height !== height) {
        canvas.width = width;
        canvas.height = height;
      }
    };
    const set = (name, value) => {
      const at = where[name];
      if (at === void 0 || at === null) return;
      if (typeof value === "number") gl.uniform1f(at, value);
      else if (value.length > 4) {
        const data = value instanceof Float32Array ? value : new Float32Array(value);
        const type = types[name];
        if (type === gl.FLOAT_VEC2) gl.uniform2fv(at, data);
        else if (type === gl.FLOAT_VEC3) gl.uniform3fv(at, data);
        else if (type === gl.FLOAT_VEC4) gl.uniform4fv(at, data);
        else gl.uniform1fv(at, data);
      } else if (value.length === 1) gl.uniform1f(at, value[0]);
      else if (value.length === 2) gl.uniform2f(at, value[0], value[1]);
      else if (value.length === 3) gl.uniform3f(at, value[0], value[1], value[2]);
      else if (value.length === 4) gl.uniform4f(at, value[0], value[1], value[2], value[3]);
    };
    for (const [name, value] of Object.entries(fixed)) set(name, value);
    return {
      gl,
      extensions: enabled,
      set(values = {}) {
        for (const [name, value] of Object.entries(values)) set(name, value);
      },
      draw(values = {}, time = 0) {
        fit();
        gl.viewport(0, 0, canvas.width, canvas.height);
        set("uCanvas", [canvas.width, canvas.height]);
        set("uView", view);
        set("uOrigin", camera.origin);
        set("uK", camera.k);
        set("uCam", camera.cam);
        set("uTime", time);
        for (const [name, value] of Object.entries(values)) set(name, value);
        gl.drawArrays(gl.TRIANGLES, 0, 3);
        painted = true;
      },
      clear() {
        if (!painted) return;
        gl.clearColor(0, 0, 0, 0);
        gl.clear(gl.COLOR_BUFFER_BIT);
        painted = false;
      }
    };
  }

  // third_party/anatomy/kit/lathe.mjs
  var TAU = Math.PI * 2;

  // third_party/anatomy/kit/tube.mjs
  var LIGHT = (() => {
    const length = Math.hypot(-0.55, -0.835);
    return [-0.55 / length, -0.835 / length];
  })();

  // third_party/anatomy/kit/turn-build.mjs
  var TAU2 = Math.PI * 2;

  // third_party/anatomy/kit/turn-audit.mjs
  var TAU3 = Math.PI * 2;

  // src/core/anatomy-adapter.ts
  var add32 = (a, b) => [
    a[0] + b[0],
    a[1] + b[1],
    a[2] + b[2]
  ];
  var zero = [0, 0, 0];
  var esc = (s) => s.replace(
    /[&<>"']/g,
    (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[c]
  );
  function anatomyEase(name, t) {
    t = Math.max(0, Math.min(1, t));
    if (name === "sine.inOut") return (1 - Math.cos(Math.PI * t)) / 2;
    const power = name?.startsWith("power2") ? 3 : 2;
    if (name?.endsWith(".inOut"))
      return t < 0.5 ? Math.pow(2 * t, power) / 2 : 1 - Math.pow(2 * (1 - t), power) / 2;
    if (name?.endsWith(".out")) return 1 - Math.pow(1 - t, power);
    if (name?.endsWith(".in")) return Math.pow(t, power);
    return t;
  }
  function lerp(a, b, t) {
    if (typeof a === "number" && typeof b === "number") return a + (b - a) * t;
    if (Array.isArray(a) && Array.isArray(b))
      return a.map((x, i) => lerp(x, b[i], t));
    if (a && b && typeof a === "object" && typeof b === "object")
      return Object.fromEntries(
        [.../* @__PURE__ */ new Set([...Object.keys(a), ...Object.keys(b)])].map((k) => [
          k,
          lerp(a[k] ?? b[k], b[k] ?? a[k], t)
        ])
      );
    return t < 1 ? a : b;
  }
  var free = (v) => Array.isArray(v) ? { translation: v, rotation: zero } : typeof v === "object" ? { translation: v.translation ?? zero, rotation: v.rotation ?? zero } : { translation: zero, rotation: zero };
  function anatomyValues(scene, time) {
    const frames = [...scene.keyframes ?? []].sort(
      (a, b) => a.atSeconds - b.atSeconds
    );
    const values = Object.fromEntries(
      (scene.groups ?? []).map((g) => {
        const normalize = (v) => g.type === "free" ? free(v) : v;
        let before = {
          atSeconds: 0,
          value: normalize(g.type === "free" ? zero : 0)
        }, value = before.value;
        for (const f of frames) {
          if (f.values[g.id] === void 0) continue;
          const next = normalize(f.values[g.id]);
          if (time < f.atSeconds) {
            value = lerp(
              before.value,
              next,
              anatomyEase(
                f.easing,
                (time - before.atSeconds) / Math.max(1e-9, f.atSeconds - before.atSeconds)
              )
            );
            break;
          }
          before = { atSeconds: f.atSeconds, value: next };
          value = next;
        }
        if (g.type === "free") {
          const v = value;
          const rx = TURN.rotation([1, 0, 0], v.rotation[0]), ry = TURN.rotation([0, 1, 0], v.rotation[1]), rz = TURN.rotation([0, 0, 1], v.rotation[2]);
          const mul = (a, b) => Array.from(
            { length: 9 },
            (_, i) => [0, 1, 2].reduce(
              (s, k) => s + a[Math.floor(i / 3) * 3 + k] * b[k * 3 + i % 3],
              0
            )
          );
          return [g.id, { t: v.translation, R: mul(rz, mul(ry, rx)) }];
        }
        return [g.id, value];
      })
    );
    if (scene.nativeExample) {
      const nativeIds = new Set(frames.flatMap((frame) => Object.keys(frame.values)));
      for (const id of nativeIds) {
        let before = { atSeconds: 0, value: 0 }, value = before.value;
        for (const frame of frames) {
          const raw = frame.values[id];
          if (typeof raw !== "number" || !Number.isFinite(raw)) continue;
          if (time < frame.atSeconds) {
            value = lerp(before.value, raw, anatomyEase(frame.easing, (time - before.atSeconds) / Math.max(1e-9, frame.atSeconds - before.atSeconds)));
            break;
          }
          before = { atSeconds: frame.atSeconds, value: raw };
          value = raw;
        }
        values[id] = value;
      }
    }
    return values;
  }
  function anatomyPartState(scene, part, time) {
    const section = part.section ?? scene.section;
    let before = {
      atSeconds: 0,
      value: {
        opacity: part.opacity ?? 1,
        visible: part.visible !== false,
        removedOpacity: section?.mode === "clip" ? 0 : section?.opacity ?? 0.12
      }
    }, value = before.value;
    for (const f of [...scene.keyframes ?? []].sort(
      (a, b) => a.atSeconds - b.atSeconds
    )) {
      const state = f.parts?.[part.id];
      if (!state) continue;
      const next = { ...before.value, ...state };
      if (time < f.atSeconds) {
        value = lerp(
          before.value,
          next,
          anatomyEase(
            f.easing,
            (time - before.atSeconds) / Math.max(1e-9, f.atSeconds - before.atSeconds)
          )
        );
        break;
      }
      before = { atSeconds: f.atSeconds, value: next };
      value = next;
    }
    return value;
  }
  function anatomyMarkup(geometry, width, height) {
    const className = geometry.nativeExample ? "iso iso-turn native-upstream-figure" : "iso iso-turn";
    return `<style>${geometry.css}</style><div class="${className}" data-theme="light" style="position:absolute;inset:0;width:${width}px;height:${height}px">${geometry.markup}</div>`;
  }

  // src/core/authored-anatomy-runtime.ts
  var fullFrame = { x: 0, y: 0, width: 1, height: 1 };
  function anatomyViewAt(view, sceneTime) {
    let before = { atSeconds: 0, frame: fullFrame, focusPartIds: [], dimOpacity: 0.18 };
    for (const key of [...view?.keyframes ?? []].sort((a, b) => a.atSeconds - b.atSeconds)) {
      const next = { ...before, ...key, frame: key.frame ?? before.frame, focusPartIds: key.focusPartIds ?? before.focusPartIds };
      if (sceneTime < key.atSeconds) {
        const linear = Math.max(0, Math.min(1, (sceneTime - before.atSeconds) / Math.max(1e-9, key.atSeconds - before.atSeconds)));
        const t = linear * linear * (3 - 2 * linear);
        const frame = Object.fromEntries(Object.keys(fullFrame).map((k) => [k, before.frame[k] + (next.frame[k] - before.frame[k]) * t]));
        return { frame, focusPartIds: before.focusPartIds, dimOpacity: before.dimOpacity + (next.dimOpacity - before.dimOpacity) * t };
      }
      before = next;
    }
    return { frame: before.frame, focusPartIds: before.focusPartIds, dimOpacity: before.dimOpacity };
  }
  function authoredModelTime(view, sceneTime) {
    return (view?.timeOffsetSeconds ?? 0) + Math.max(0, sceneTime) * (view?.timeScale ?? 1);
  }
  function authoredViewTransforms(figure, output, frame, contentCamera) {
    const fit = (rect) => {
      const scale = Math.min(output.width / (figure.width * rect.width), output.height / (figure.height * rect.height));
      return {
        scale,
        x: (output.width - rect.width * figure.width * scale) / 2 - rect.x * figure.width * scale,
        y: (output.height - rect.height * figure.height * scale) / 2 - rect.y * figure.height * scale
      };
    };
    const viewed = fit(frame);
    if (!contentCamera) return { iframe: viewed };
    const full = fit(fullFrame);
    return { iframe: full, camera: { x: (viewed.x - full.x) / full.scale, y: (viewed.y - full.y) / full.scale, scale: viewed.scale / full.scale } };
  }
  var transformCss = ({ x, y, scale }) => `translate(${x}px,${y}px) scale(${scale})`;
  var json = (value) => JSON.stringify(value).replace(/</g, "\\u003c").replace(/\u2028/g, "\\u2028").replace(/\u2029/g, "\\u2029");
  function authoredFigureDocument(figure) {
    const payload = json(figure);
    return `<!doctype html><html><head><meta charset="utf-8"><meta http-equiv="Content-Security-Policy" content="default-src 'none'; script-src 'unsafe-inline' 'unsafe-eval'; style-src 'unsafe-inline'; img-src data: blob:; font-src data:; connect-src 'none'; media-src data: blob:; worker-src 'none'; frame-src 'none'; object-src 'none'; base-uri 'none'; form-action 'none'"><style>html,body{margin:0;padding:0;overflow:hidden;width:100%;height:100%;background:transparent}#figure-root{position:relative;overflow:hidden}[data-anatomy-camera]{position:absolute;inset:0;width:100%;height:100%;transform-origin:0 0}*{box-sizing:border-box;cursor:none!important}</style></head><body><div id="figure-root"></div><script>
    const figure=${payload};
    window.__dpFigureDiagnostics=[];
    window.__dpFigureGlContexts=[];
    const getContext=HTMLCanvasElement.prototype.getContext;
    HTMLCanvasElement.prototype.getContext=function(kind,options){
      const webgl=kind==='webgl'||kind==='webgl2'||kind==='experimental-webgl';
      const context=getContext.call(this,kind,webgl?{...options,preserveDrawingBuffer:true}:options);
      if(webgl&&context&&!window.__dpFigureGlContexts.includes(context))window.__dpFigureGlContexts.push(context);
      return context;
    };
    for(const name of ['requestAnimationFrame','setInterval'])window[name]=function(){
      const message='ANATOMY_AUTHORED_WALL_CLOCK: '+name+' is disabled; update the figure through renderAt(time).';
      window.__dpFigureDiagnostics.push({severity:'error',code:'ANATOMY_AUTHORED_WALL_CLOCK',message});throw new Error(message);
    };
    document.addEventListener('securitypolicyviolation',event=>window.__dpFigureDiagnostics.push({severity:'error',code:'ANATOMY_AUTHORED_RESOURCE_BLOCKED',message:event.violatedDirective+': '+event.blockedURI}));
    window.addEventListener('error',event=>window.__dpFigureDiagnostics.push({severity:'error',code:'ANATOMY_AUTHORED_SCRIPT_ERROR',message:event.message}));
    window.addEventListener('unhandledrejection',event=>window.__dpFigureDiagnostics.push({severity:'error',code:'ANATOMY_AUTHORED_SCRIPT_ERROR',message:String(event.reason)}));
    window.__dpFigureReady=(async()=>{
      const root=document.getElementById('figure-root');root.style.width=figure.width+'px';root.style.height=figure.height+'px';root.innerHTML=figure.markup;
      const style=document.createElement('style');style.textContent=figure.css;document.head.appendChild(style);
      const create=new Function('"use strict"; return ('+figure.script+'\\n);')();
      if(typeof create!=='function')throw new Error('ANATOMY_AUTHORED_FACTORY_INVALID: script must be a function expression.');
      const api=await create(root);
      if(!api||typeof api.renderAt!=='function')throw new Error('ANATOMY_AUTHORED_RENDER_MISSING: factory must return renderAt(time, context).');
      await api.ready; await document.fonts.ready;
      await Promise.all(Array.from(root.querySelectorAll('img')).map(image=>image.decode()));
      window.__dpFigureApi=api;return api;
    })();window.__dpFigureReady.catch(()=>{});
  <\/script></body></html>`;
  }
  function mountAuthoredAnatomy(canvas, config) {
    const scene = config.scene.anatomy, figure = scene.authoredFigure;
    if (!figure) throw new Error(`ANATOMY_FIGURE_UNBOUND: ${scene.figureId ?? "unknown"}; import the figure and compile the project first.`);
    const stage = document.createElement("div");
    stage.className = "anatomy-authored-stage";
    stage.style.cssText = `position:absolute;inset:0;overflow:hidden;background:${scene.background ?? config.scene.background ?? "transparent"}`;
    const iframe = document.createElement("iframe");
    iframe.setAttribute("sandbox", "allow-scripts allow-same-origin");
    iframe.setAttribute("title", `Anatomy figure ${scene.figureId}`);
    iframe.style.cssText = `position:absolute;left:0;top:0;border:0;width:${figure.width}px;height:${figure.height}px;transform-origin:0 0;pointer-events:none`;
    stage.appendChild(iframe);
    const canvasDisplay = canvas.style.display;
    canvas.style.display = "none";
    canvas.parentElement.appendChild(stage);
    const diagnostics = [], seen = /* @__PURE__ */ new Set();
    const report = (item) => {
      const key = `${item.code}:${item.message}`;
      if (!seen.has(key)) {
        diagnostics.push(item);
        seen.add(key);
      }
    };
    const collectDiagnostics = () => {
      for (const item of [...iframe.contentWindow?.__dpFigureDiagnostics ?? [], ...api2?.diagnostics ?? []]) {
        if (item && ["error", "warning"].includes(item.severity)) report({ code: String(item.code ?? "ANATOMY_AUTHORED_DIAGNOSTIC"), message: String(item.message ?? ""), severity: item.severity });
      }
    };
    const fail = (error) => {
      report({ code: "ANATOMY_AUTHORED_FAILED", severity: "error", message: String(error) });
      throw error;
    };
    const metadata = {
      backend: "anatomy-authored",
      engine: "project-authored anatomy",
      sourceCommit: figure.provenance?.sourceCommit,
      provenance: figure.provenance,
      figureId: scene.figureId,
      runtime: config.version,
      webgl: "not-observed",
      namedParts: figure.parts.length,
      network: "blocked-by-csp",
      cameraMode: "whole-figure"
    };
    let api2, disposed = false, frameCount = 0, lastTime = config.sceneRange.start, lastModelTime = 0;
    let queue = Promise.resolve();
    const opacityRestore = /* @__PURE__ */ new Map();
    let cameraRestore;
    const paintAt = async (filmTime) => {
      if (disposed || !api2) return;
      if (!Number.isFinite(filmTime)) throw new Error("ANATOMY_AUTHORED_TIME_INVALID: renderAt needs finite seconds.");
      const sceneTime = Math.max(0, Math.min(config.sceneRange.end - config.sceneRange.start, filmTime - config.sceneRange.start));
      const modelTime = authoredModelTime(scene.view, sceneTime), view = anatomyViewAt(scene.view, sceneTime);
      for (const [node, original] of opacityRestore) {
        if (original.value) node.style.setProperty("opacity", original.value, original.priority);
        else node.style.removeProperty("opacity");
      }
      opacityRestore.clear();
      if (cameraRestore) {
        if (cameraRestore.value) cameraRestore.node.style.setProperty("transform", cameraRestore.value, cameraRestore.priority);
        else cameraRestore.node.style.removeProperty("transform");
        cameraRestore = void 0;
      }
      let paintTimeout;
      try {
        await Promise.race([api2.renderAt(modelTime, { sceneTime, modelTime, filmTime, focusPartIds: view.focusPartIds }), new Promise((_, reject) => {
          paintTimeout = window.setTimeout(() => reject(new Error(`ANATOMY_AUTHORED_PAINT_TIMEOUT: renderAt(${modelTime}) did not settle within 10s.`)), 1e4);
        })]);
      } finally {
        window.clearTimeout(paintTimeout);
      }
      const doc = iframe.contentDocument;
      const nodes = [...doc.querySelectorAll("[data-anatomy-part]")];
      const available = new Set(nodes.map((node) => node.dataset.anatomyPart));
      for (const part of figure.parts) if (!available.has(part.id)) throw new Error(`ANATOMY_AUTHORED_PART_MISSING: ${part.id} has no data-anatomy-part element.`);
      const focused = nodes.filter((node) => view.focusPartIds.includes(node.dataset.anatomyPart));
      const highlighted = new Set(nodes.filter((node) => focused.some((target) => node === target || node.contains(target) || target.contains(node))));
      if (focused.length) for (const node of nodes) {
        if (highlighted.has(node)) continue;
        if (nodes.some((parent) => parent !== node && parent.contains(node) && !highlighted.has(parent))) continue;
        opacityRestore.set(node, { value: node.style.getPropertyValue("opacity"), priority: node.style.getPropertyPriority("opacity") });
        const base = Number(iframe.contentWindow.getComputedStyle(node).opacity);
        node.style.setProperty("opacity", String((Number.isFinite(base) ? base : 1) * view.dimOpacity), "important");
      }
      const cameraNodes = [...doc.querySelectorAll("[data-anatomy-camera]")];
      if (cameraNodes.length > 1) throw new Error("ANATOMY_AUTHORED_CAMERA_AMBIGUOUS: use one data-anatomy-camera wrapper for the figure content.");
      const camera = cameraNodes[0];
      if (camera && (camera.namespaceURI !== "http://www.w3.org/1999/xhtml" || camera === doc.getElementById("figure-root"))) throw new Error("ANATOMY_AUTHORED_CAMERA_INVALID: camera must be an HTML wrapper inside figure-root.");
      const transforms = authoredViewTransforms(figure, config, view.frame, Boolean(camera));
      iframe.style.transform = transformCss(transforms.iframe);
      metadata.cameraMode = camera ? "content-only" : "whole-figure";
      if (camera) {
        if (iframe.contentWindow.getComputedStyle(camera).transform !== "none") throw new Error("ANATOMY_AUTHORED_CAMERA_TRANSFORM_CONFLICT: animate content inside data-anatomy-camera; its transform belongs to the shot camera.");
        cameraRestore = { node: camera, value: camera.style.getPropertyValue("transform"), priority: camera.style.getPropertyPriority("transform") };
        camera.style.position = "absolute";
        camera.style.inset = "0";
        camera.style.width = `${figure.width}px`;
        camera.style.height = `${figure.height}px`;
        camera.style.transformOrigin = "0 0";
        camera.style.setProperty("transform", transformCss(transforms.camera), "important");
      }
      await doc.fonts.ready;
      await Promise.all([...doc.querySelectorAll("img")].map((image) => image.decode()));
      for (const gl of iframe.contentWindow.__dpFigureGlContexts ?? []) {
        gl.finish();
        metadata.webgl = "available";
      }
      doc.documentElement.getBoundingClientRect();
      stage.getBoundingClientRect();
      collectDiagnostics();
      const errors = diagnostics.filter((item) => item.severity === "error");
      if (errors.length) throw new Error(errors.map((item) => `${item.code}: ${item.message}`).join("; "));
      lastTime = filmTime;
      lastModelTime = modelTime;
      frameCount++;
    };
    const loaded = new Promise((resolve, reject) => {
      const timeout = window.setTimeout(() => reject(new Error("ANATOMY_AUTHORED_READY_TIMEOUT: figure did not load within 30s.")), 3e4);
      iframe.addEventListener("load", () => {
        if (!iframe.contentWindow?.__dpFigureReady) return;
        window.clearTimeout(timeout);
        resolve();
      });
      iframe.addEventListener("error", () => {
        window.clearTimeout(timeout);
        reject(new Error("ANATOMY_AUTHORED_FRAME_FAILED"));
      }, { once: true });
    });
    iframe.srcdoc = authoredFigureDocument(figure);
    const ready = loaded.then(async () => {
      const source = iframe.contentWindow;
      if (!source?.__dpFigureReady) throw new Error("ANATOMY_AUTHORED_BOOTSTRAP_FAILED");
      let timer;
      try {
        api2 = await Promise.race([source.__dpFigureReady, new Promise((_, reject) => {
          timer = window.setTimeout(() => reject(new Error("ANATOMY_AUTHORED_READY_TIMEOUT: factory resources did not settle within 30s.")), 3e4);
        })]);
      } finally {
        window.clearTimeout(timer);
      }
      await Promise.all([...document.fonts].map(async (font) => {
        const loadedFont = await font.load();
        iframe.contentDocument.fonts.add(loadedFont);
      }));
      await paintAt(config.sceneRange.start);
    }).catch(fail);
    ready.catch(() => {
    });
    const renderAt = (time) => {
      queue = queue.then(() => ready).then(() => paintAt(time)).catch(fail);
      queue.catch(() => {
      });
    };
    return {
      ready,
      renderAt,
      paintReady: () => queue,
      diagnostics,
      metadata,
      evidence: () => ({ ...metadata, frameCount, lastTime, modelTime: lastModelTime, diagnostics }),
      dispose: () => {
        disposed = true;
        api2?.dispose?.();
        stage.remove();
        canvas.style.display = canvasDisplay;
      }
    };
  }

  // src/core/anatomy-runtime.ts
  function mount(canvas, config) {
    if (config.scene.anatomy?.figureId) return mountAuthoredAnatomy(canvas, config);
    const scene = config.scene.anatomy, geometry = config.anatomyGeometry;
    if (!scene || !geometry)
      throw new Error(
        "ANATOMY_COMPILED_DATA_MISSING: compile the project with Wandeo 0.6.0."
      );
    const diagnostics = [], seen = /* @__PURE__ */ new Set();
    const warn = (code, message, partId) => {
      const key = code + partId;
      if (!seen.has(key)) {
        seen.add(key);
        diagnostics.push({ code, message, partId, severity: "warning" });
      }
    };
    const stage = document.createElement("div");
    stage.className = "anatomy-stage";
    stage.dataset.engine = "anatomy-turn";
    stage.style.cssText = `position:absolute;inset:0;overflow:hidden;isolation:isolate;background:${scene.background ?? config.scene.background ?? "#f1f5f9"}`;
    stage.innerHTML = anatomyMarkup(geometry, config.width, config.height);
    const host = stage.querySelector(".iso");
    host.dataset.theme = scene.theme ?? "light";
    host.style.zIndex = "2";
    canvas.parentElement.appendChild(stage);
    const canvasDisplay = canvas.style.display;
    canvas.style.display = "none";
    const controller = TURN.mount(host, geometry.data);
    const partMap = new Map(geometry.parts.map((p) => [p.id, p]));
    const bindings = geometry.bindings.map((b) => ({
      ...b,
      node: host.querySelector(`[data-p="${b.index}"]`)
    }));
    for (const b of bindings) {
      const part = partMap.get(b.partId);
      b.node.dataset.anatomyPart = part.id;
      b.node.dataset.section = b.removed ? "removed" : "kept";
      if (part.color && !part.material) {
        const c = part.color, secondary = part.secondaryColor ?? c;
        b.node.style.cssText = `--anatomy-paper:${c};--anatomy-top:color-mix(in srgb,${c} 70%,white);--anatomy-shade-0:color-mix(in srgb,${secondary} 60%,black);--anatomy-shade-1:${secondary};--anatomy-shade-2:${c};--anatomy-shade-3:color-mix(in srgb,${c} 85%,white);--anatomy-hi:color-mix(in srgb,${c} 40%,black);--mat-body:${c};--mat-shine:color-mix(in srgb,${c} 70%,white);--mat-shade:${secondary};--mat-edge:${secondary}`;
      }
    }
    const annotationSvg = document.createElementNS(
      "http://www.w3.org/2000/svg",
      "svg"
    );
    annotationSvg.setAttribute("viewBox", `0 0 ${config.width} ${config.height}`);
    annotationSvg.style.cssText = "position:absolute;inset:0;width:100%;height:100%;pointer-events:none;z-index:110";
    stage.appendChild(annotationSvg);
    const readoutHost = document.createElement("div");
    readoutHost.dataset.anatomyReadouts = "true";
    readoutHost.style.cssText = "position:absolute;inset:0;pointer-events:none;z-index:110;font-family:ui-monospace,SFMono-Regular,Menlo,monospace";
    if (scene.presentation?.showReadout === false) readoutHost.style.display = "none";
    stage.appendChild(readoutHost);
    if (scene.presentation?.card !== false && (scene.presentation?.title || scene.presentation?.subtitle || scene.presentation?.hint)) {
      const card = document.createElement("div");
      card.dataset.anatomyCard = "true";
      card.style.cssText = "position:absolute;left:24px;top:20px;z-index:120;pointer-events:none;color:var(--anatomy-text,#18212b);text-shadow:0 1px 4px rgba(255,255,255,.7)";
      card.innerHTML = `${scene.presentation.title ? `<strong style="display:block;font-size:28px;line-height:1.15">${esc(scene.presentation.title)}</strong>` : ""}${scene.presentation.subtitle ? `<span style="display:block;margin-top:4px;font-size:16px">${esc(scene.presentation.subtitle)}</span>` : ""}${scene.presentation.hint ? `<span style="display:block;margin-top:10px;font-size:13px;opacity:.75">${esc(scene.presentation.hint)}</span>` : ""}`;
      stage.appendChild(card);
    }
    const controlValues = {};
    for (const control of scene.controls ?? []) if (control.initial !== void 0) controlValues[control.groupId] = control.initial;
    const controlsHost = document.createElement("div");
    controlsHost.dataset.anatomyControls = "true";
    controlsHost.style.cssText = "position:absolute;right:20px;bottom:20px;z-index:140;display:flex;gap:8px;pointer-events:auto;font-family:ui-sans-serif,system-ui,sans-serif";
    stage.appendChild(controlsHost);
    const clampControl = (control, value) => {
      const min = control.min ?? -360, max = control.max ?? 360, step = control.step ?? 1;
      return Math.max(min, Math.min(max, Math.round(value / step) * step));
    };
    const setControl = (control, value) => {
      controlValues[control.groupId] = clampControl(control, value);
      renderFrame(lastTime, controlValues);
    };
    for (const control of scene.controls ?? []) {
      if (control.type === "pointer") {
        let active = false;
        stage.addEventListener("pointerdown", (event) => {
          active = true;
          event.target.setPointerCapture?.(event.pointerId);
        });
        stage.addEventListener("pointerup", () => {
          active = false;
        });
        stage.addEventListener("pointermove", (event) => {
          if (!active) return;
          const box = stage.getBoundingClientRect();
          const p = (event.clientX - box.left) / Math.max(1, box.width);
          setControl(control, (control.min ?? -360) + p * ((control.max ?? 360) - (control.min ?? -360)));
        });
      } else if (control.type === "keyboard") {
        window.addEventListener("keydown", (event) => {
          if (event.key === control.keys?.increase) setControl(control, (controlValues[control.groupId] ?? control.initial ?? 0) + (control.step ?? 1));
          if (event.key === control.keys?.decrease) setControl(control, (controlValues[control.groupId] ?? control.initial ?? 0) - (control.step ?? 1));
          if (event.key === control.keys?.reset) setControl(control, control.initial ?? 0);
        });
      } else if (control.type === "button") {
        const button = document.createElement("button");
        button.type = "button";
        button.dataset.anatomyControl = control.id;
        button.textContent = control.id;
        button.style.cssText = "border:1px solid rgba(15,23,42,.25);border-radius:6px;background:rgba(255,255,255,.9);padding:6px 10px;color:#18212b;cursor:pointer";
        button.addEventListener("click", () => setControl(control, control.initial ?? control.min ?? 0));
        controlsHost.appendChild(button);
      }
    }
    let paint = Promise.resolve(), disposed = false, frameCount = 0, lastTime = config.sceneRange.start, paintRevision = 0;
    const canvasMode = Boolean(window.__wandeoForceAnatomyCanvas);
    const rasterCanvas = canvasMode ? document.createElement("canvas") : void 0;
    if (rasterCanvas) {
      rasterCanvas.width = config.width;
      rasterCanvas.height = config.height;
      rasterCanvas.style.cssText = "position:absolute;inset:0;width:100%;height:100%;z-index:2;pointer-events:none";
      stage.appendChild(rasterCanvas);
      host.style.visibility = "hidden";
    }
    const metadata = {
      backend: canvasMode ? "anatomy-canvas2d" : "anatomy-svg",
      engine: "upstream TURN.mount/turning",
      sourceCommit: "1482e8469b0a9e0d8cc18ea2740a01423d29ae80",
      runtime: config.version,
      webgl: "not-required",
      geometryParts: geometry.data.parts.length
    };
    const configuredEffects = [
      ...scene.effects ?? [],
      ...scene.effect ? [{ id: "legacy-effect", fragment: scene.effect.fragment, order: "front", uniforms: scene.effect.uniforms, required: scene.effect.required }] : []
    ];
    const effects = [];
    for (const layer of configuredEffects) {
      const effectCanvas = document.createElement("canvas");
      effectCanvas.style.cssText = `position:absolute;inset:0;width:100%;height:100%;pointer-events:none;z-index:${layer.order === "back" ? 1 : 100};opacity:${layer.opacity ?? 1}`;
      stage.appendChild(effectCanvas);
      effectCanvas.getContext("webgl", { premultipliedAlpha: true, alpha: true, antialias: false, preserveDrawingBuffer: true });
      const shader = glLayer({
        canvas: effectCanvas,
        fragment: layer.fragment,
        view: [config.width, config.height],
        camera: glCamera(geometry.projection),
        uniforms: Object.keys(layer.uniforms ?? {}),
        maxRatio: 1,
        onError: (message) => diagnostics.push({ code: "ANATOMY_EFFECT_SHADER_FAILED", message, severity: layer.required ? "error" : "warning" })
      });
      if (!shader) {
        if (layer.required) throw new Error(`ANATOMY_EFFECT_WEBGL_REQUIRED: ${layer.id}`);
        warn("ANATOMY_EFFECT_FALLBACK", `WebGL effect ${layer.id} unavailable; geometry remains visible.`);
        continue;
      }
      effects.push({ layer, shader, canvas: effectCanvas });
    }
    metadata.webgl = effects.length ? "available" : configuredEffects.length ? "unavailable" : "not-required";
    const project = (group, point) => group ? controller.anchor(group, point).screen : iso(point, geometry.projection);
    const renderFrame = (filmTime, previewValues) => {
      if (disposed) return;
      const time = Math.max(0, filmTime - config.sceneRange.start);
      lastTime = filmTime;
      for (const layer of geometry.data.layers) {
        const order = controller.orderIndex(layer.name);
        order?.set(layer.rest);
        const svg = [
          ...host.querySelectorAll("svg[data-live]")
        ].find((svg2) => svg2.dataset.live === layer.name);
        const container = svg?.querySelector(".iso-parts");
        for (const index of layer.rest) {
          const node = bindings[index]?.node;
          if (node && container) container.appendChild(node);
        }
      }
      let values = { ...geometry.nativeDefaults ?? {}, ...anatomyValues(scene, time), ...previewValues };
      if (geometry.nativeFollow === "turning-dial") {
        const dial = Number(values.dial ?? 0);
        values = { ...values, wheel: -(dial ?? 0) / 4, pawl: 4 * Math.sin(dial * Math.PI / 18) };
      }
      controller.set(values);
      for (const b of bindings) {
        const p = partMap.get(b.partId), s = anatomyPartState(scene, p, time);
        b.node.style.opacity = String(
          s.opacity * (b.removed ? s.removedOpacity : 1)
        );
        b.node.style.display = s.visible ? "" : "none";
      }
      const annotationMarkup = [];
      const annotations = [
        ...scene.annotations ?? [],
        ...(config.scene.annotations ?? []).map((a) => ({
          ...a,
          range: {
            start: a.range.start - config.sceneRange.start,
            end: a.range.end - config.sceneRange.start
          },
          anchor: Array.isArray(a.anchor) ? a.anchor : { partId: a.anchor.modelId, offset: a.anchor.offset },
          fontSize: 20,
          labelOffset: [100, -50]
        }))
      ];
      for (const a of annotations) {
        if (a.range && (time < a.range.start || time >= a.range.end)) continue;
        const part = Array.isArray(a.anchor) ? void 0 : partMap.get(a.anchor.partId);
        if (part && !anatomyPartState(scene, part, time).visible) continue;
        const at = Array.isArray(a.anchor) ? a.anchor : add32(part?.position ?? [0, 0, 0], a.anchor.offset ?? [0, 0, 0]);
        const [x, y] = project(part?.groupId, at), [dx, dy] = a.labelOffset ?? [100, -50], font = a.fontSize ?? Math.max(16, config.height / 36);
        const tx = Math.max(12, Math.min(config.width - 12, x + dx)), ty = Math.max(font, Math.min(config.height - font, y + dy));
        const align = tx > config.width * 0.65 ? "end" : "start";
        annotationMarkup.push(
          `<g data-anatomy-annotation="${esc(a.id)}"><path d="M${x} ${y}L${tx} ${ty}" fill="none" stroke="${a.lineColor ?? "#475569"}" stroke-width="1.5"/><circle cx="${x}" cy="${y}" r="3" fill="${a.lineColor ?? "#475569"}"/><text x="${tx}" y="${ty - 8}" text-anchor="${align}" fill="${a.color ?? "#0f172a"}" font-size="${font}" font-weight="600" font-family="inherit">${esc(a.text)}</text></g>`
        );
        if (x < 0 || x > config.width || y < 0 || y > config.height)
          warn(
            "ANATOMY_ANNOTATION_ANCHOR_OFFSCREEN",
            `Annotation ${a.id} points outside the frame.`,
            part?.id
          );
      }
      for (const p of geometry.parts.filter((p2) => p2.kind === "label")) {
        const s = anatomyPartState(scene, p, time);
        if (!s.visible) continue;
        const [x, y] = project(p.groupId, p.position ?? [0, 0, 0]);
        annotationMarkup.push(
          `<text x="${x}" y="${y}" fill="${p.color ?? "#0f172a"}" opacity="${s.opacity}" font-size="${p.fontSize ?? 24}" font-family="inherit">${esc(p.text ?? p.id)}</text>`
        );
      }
      annotationSvg.innerHTML = annotationMarkup.join("");
      readoutHost.innerHTML = (scene.readouts ?? []).map((readout) => {
        const raw = readout.groupId ? values[readout.groupId] : readout.value;
        const numeric = typeof raw === "number" ? raw : raw && typeof raw === "object" && typeof raw.value === "number" ? raw.value : void 0;
        const value = numeric !== void 0 ? readout.format ? readout.format.replace(/\{value\}/g, numeric.toFixed(2)) : numeric.toFixed(2) : raw && typeof raw === "object" ? JSON.stringify(raw) : raw ?? "";
        const [x, y] = readout.position ?? [config.width - 240, 32];
        return `<span data-anatomy-readout="${esc(readout.id)}" style="position:absolute;left:${x}px;top:${y}px;color:${readout.color ?? "#18212b"};font-size:${readout.fontSize ?? 16}px">${esc(readout.text ?? readout.id)} ${esc(String(value))}${readout.unit ? ` ${esc(readout.unit)}` : ""}</span>`;
      }).join("");
      const active = filmTime >= config.sceneRange.start && filmTime < config.sceneRange.end;
      if (active) {
        const viewport = stage.getBoundingClientRect();
        if (viewport.width && viewport.height) {
          for (const b of bindings) {
            const p = partMap.get(b.partId), state = anatomyPartState(scene, p, time);
            if (!state.visible || state.opacity * (b.removed ? state.removedOpacity : 1) < 0.1)
              continue;
            const r = b.node.getBoundingClientRect();
            if (r.width > 1 && r.height > 1 && (r.left < viewport.left - 1 || r.top < viewport.top - 1 || r.right > viewport.right + 1 || r.bottom > viewport.bottom + 1))
              warn(
                "ANATOMY_PART_CLIPPED",
                `Part ${p.id} crosses the viewport at ${time.toFixed(3)}s.`,
                p.id
              );
          }
          const labels = Array.from(annotationSvg.querySelectorAll("text"));
          for (let i = 0; i < labels.length; i++)
            for (let j = i + 1; j < labels.length; j++) {
              const a = labels[i].getBoundingClientRect(), b = labels[j].getBoundingClientRect();
              if (a.left < b.right && a.right > b.left && a.top < b.bottom && a.bottom > b.top)
                warn(
                  "ANATOMY_LABEL_OVERLAP",
                  `Labels overlap at ${time.toFixed(3)}s.`,
                  labels[i].textContent ?? "label"
                );
            }
        }
      }
      for (const effect of effects) {
        effect.shader.draw(effect.layer.uniforms ?? {}, time);
        effect.shader.gl.finish();
      }
      if (rasterCanvas) {
        const revision = ++paintRevision;
        const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="${config.width}" height="${config.height}" class="iso" data-theme="${scene.theme ?? "light"}"><style>${geometry.css}</style>${Array.from(
          host.querySelectorAll("svg")
        ).map((s) => s.outerHTML).join("")}</svg>`;
        const image = new Image();
        image.src = "data:image/svg+xml;charset=utf-8," + encodeURIComponent(svg);
        paint = image.decode().then(() => {
          if (disposed || revision !== paintRevision) return;
          const ctx = rasterCanvas.getContext("2d");
          ctx.clearRect(0, 0, config.width, config.height);
          ctx.drawImage(image, 0, 0);
        });
      }
      frameCount++;
    };
    const renderAt = (filmTime) => renderFrame(filmTime);
    const ready = document.fonts.ready.then(() => {
      renderAt(config.sceneRange.start);
      return paint;
    });
    return {
      ready,
      renderAt,
      paintReady: () => paint,
      diagnostics,
      metadata,
      geometryAudit: geometry.audits,
      evidence: () => ({
        ...metadata,
        frameCount,
        lastTime,
        diagnostics,
        geometryAudit: geometry.audits
      }),
      dispose: () => {
        disposed = true;
        controller.destroy();
        for (const effect of effects) effect.shader.gl.getExtension("WEBGL_lose_context")?.loseContext();
        stage.remove();
        canvas.style.display = canvasDisplay;
      }
    };
  }
  var api = { version: "0.6.0-anatomy", mount };
  if (typeof window !== "undefined") window.__wandeoAnatomy = api;
  return __toCommonJS(anatomy_runtime_exports);
})();
