#!/usr/bin/env node
var __defProp = Object.defineProperty;
var __getOwnPropNames = Object.getOwnPropertyNames;
var __esm = (fn, res) => function __init() {
  return fn && (res = (0, fn[__getOwnPropNames(fn)[0]])(fn = 0)), res;
};
var __export = (target, all) => {
  for (var name in all)
    __defProp(target, name, { get: all[name], enumerable: true });
};

// node_modules/fflate/esm/index.mjs
import { createRequire as createRequire2 } from "module";
function inflateSync(data, opts) {
  return inflt(data, { i: 2 }, opts && opts.out, opts && opts.dictionary);
}
function strFromU8(dat, latin1) {
  if (latin1) {
    var r = "";
    for (var i = 0; i < dat.length; i += 16384)
      r += String.fromCharCode.apply(null, dat.subarray(i, i + 16384));
    return r;
  } else if (td) {
    return td.decode(dat);
  } else {
    var _a2 = dutf8(dat), s = _a2.s, r = _a2.r;
    if (r.length)
      err(8);
    return s;
  }
}
function unzipSync(data, opts) {
  var files = {};
  var e = data.length - 22;
  for (; b4(data, e) != 101010256; --e) {
    if (!e || data.length - e > 65558)
      err(13);
  }
  ;
  var c = b2(data, e + 8);
  if (!c)
    return {};
  var o = b4(data, e + 16);
  var z = b4(data, e - 20) == 117853008;
  if (z) {
    var ze = b4(data, e - 12);
    z = b4(data, ze) == 101075792;
    if (z) {
      c = b4(data, ze + 32);
      o = b4(data, ze + 48);
    }
  }
  var fltr = opts && opts.filter;
  for (var i = 0; i < c; ++i) {
    var _a2 = zh(data, o, z), c_2 = _a2[0], sc = _a2[1], su = _a2[2], fn = _a2[3], no = _a2[4], off = _a2[5], b = slzh(data, off);
    o = no;
    if (!fltr || fltr({
      name: fn,
      size: sc,
      originalSize: su,
      compression: c_2
    })) {
      if (!c_2)
        files[fn] = slc(data, b, b + sc);
      else if (c_2 == 8)
        files[fn] = inflateSync(data.subarray(b, b + sc), { out: new u8(su) });
      else
        err(14, "unknown compression type " + c_2);
    }
  }
  return files;
}
var require2, _a, Worker, isMarkedAsUntransferable, u8, u16, i32, fleb, fdeb, clim, freb, _a, fl, revfl, _b, fd, revfd, rev, x, i, hMap, flt, i, i, i, i, fdt, i, flrm, fdrm, max, bits, bits16, shft, slc, ec, err, inflt, et, b2, b4, b8, td, tds, dutf8, slzh, zh, z64hs;
var init_esm = __esm({
  "node_modules/fflate/esm/index.mjs"() {
    require2 = createRequire2("/");
    try {
      _a = require2("worker_threads"), Worker = _a.Worker, isMarkedAsUntransferable = _a.isMarkedAsUntransferable;
    } catch (e) {
    }
    u8 = Uint8Array;
    u16 = Uint16Array;
    i32 = Int32Array;
    fleb = new u8([
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      1,
      1,
      1,
      1,
      2,
      2,
      2,
      2,
      3,
      3,
      3,
      3,
      4,
      4,
      4,
      4,
      5,
      5,
      5,
      5,
      0,
      /* unused */
      0,
      0,
      /* impossible */
      0
    ]);
    fdeb = new u8([
      0,
      0,
      0,
      0,
      1,
      1,
      2,
      2,
      3,
      3,
      4,
      4,
      5,
      5,
      6,
      6,
      7,
      7,
      8,
      8,
      9,
      9,
      10,
      10,
      11,
      11,
      12,
      12,
      13,
      13,
      /* unused */
      0,
      0
    ]);
    clim = new u8([16, 17, 18, 0, 8, 7, 9, 6, 10, 5, 11, 4, 12, 3, 13, 2, 14, 1, 15]);
    freb = function(eb, start) {
      var b = new u16(31);
      for (var i = 0; i < 31; ++i) {
        b[i] = start += 1 << eb[i - 1];
      }
      var r = new i32(b[30]);
      for (var i = 1; i < 30; ++i) {
        for (var j = b[i]; j < b[i + 1]; ++j) {
          r[j] = j - b[i] << 5 | i;
        }
      }
      return { b, r };
    };
    _a = freb(fleb, 2);
    fl = _a.b;
    revfl = _a.r;
    fl[28] = 258, revfl[258] = 28;
    _b = freb(fdeb, 0);
    fd = _b.b;
    revfd = _b.r;
    rev = new u16(32768);
    for (i = 0; i < 32768; ++i) {
      x = (i & 43690) >> 1 | (i & 21845) << 1;
      x = (x & 52428) >> 2 | (x & 13107) << 2;
      x = (x & 61680) >> 4 | (x & 3855) << 4;
      rev[i] = ((x & 65280) >> 8 | (x & 255) << 8) >> 1;
    }
    hMap = (function(cd, mb, r) {
      var s = cd.length;
      var i = 0;
      var l = new u16(mb);
      for (; i < s; ++i) {
        if (cd[i])
          ++l[cd[i] - 1];
      }
      var le = new u16(mb);
      for (i = 1; i < mb; ++i) {
        le[i] = le[i - 1] + l[i - 1] << 1;
      }
      var co;
      if (r) {
        co = new u16(1 << mb);
        var rvb = 15 - mb;
        for (i = 0; i < s; ++i) {
          if (cd[i]) {
            var sv = i << 4 | cd[i];
            var r_1 = mb - cd[i];
            var v = le[cd[i] - 1]++ << r_1;
            for (var m = v | (1 << r_1) - 1; v <= m; ++v) {
              co[rev[v] >> rvb] = sv;
            }
          }
        }
      } else {
        co = new u16(s);
        for (i = 0; i < s; ++i) {
          if (cd[i]) {
            co[i] = rev[le[cd[i] - 1]++] >> 15 - cd[i];
          }
        }
      }
      return co;
    });
    flt = new u8(288);
    for (i = 0; i < 144; ++i)
      flt[i] = 8;
    for (i = 144; i < 256; ++i)
      flt[i] = 9;
    for (i = 256; i < 280; ++i)
      flt[i] = 7;
    for (i = 280; i < 288; ++i)
      flt[i] = 8;
    fdt = new u8(32);
    for (i = 0; i < 32; ++i)
      fdt[i] = 5;
    flrm = /* @__PURE__ */ hMap(flt, 9, 1);
    fdrm = /* @__PURE__ */ hMap(fdt, 5, 1);
    max = function(a) {
      var m = a[0];
      for (var i = 1; i < a.length; ++i) {
        if (a[i] > m)
          m = a[i];
      }
      return m;
    };
    bits = function(d, p, m) {
      var o = p / 8 | 0;
      return (d[o] | d[o + 1] << 8) >> (p & 7) & m;
    };
    bits16 = function(d, p) {
      var o = p / 8 | 0;
      return (d[o] | d[o + 1] << 8 | d[o + 2] << 16) >> (p & 7);
    };
    shft = function(p) {
      return (p + 7) / 8 | 0;
    };
    slc = function(v, s, e) {
      if (s == null || s < 0)
        s = 0;
      if (e == null || e > v.length)
        e = v.length;
      return new u8(v.subarray(s, e));
    };
    ec = [
      "unexpected EOF",
      "invalid block type",
      "invalid length/literal",
      "invalid distance",
      "stream finished",
      "no stream handler",
      ,
      // determined by compression function
      "no callback",
      "invalid UTF-8 data",
      "extra field too long",
      "date not in range 1980-2099",
      "filename too long",
      "stream finishing",
      "invalid zip data"
      // determined by unknown compression method
    ];
    err = function(ind, msg, nt) {
      var e = new Error(msg || ec[ind]);
      e.code = ind;
      if (Error.captureStackTrace)
        Error.captureStackTrace(e, err);
      if (!nt)
        throw e;
      return e;
    };
    inflt = function(dat, st, buf, dict) {
      var sl = dat.length, dl = dict ? dict.length : 0;
      if (!sl || st.f && !st.l)
        return buf || new u8(0);
      var noBuf = !buf;
      var resize = noBuf || st.i != 2;
      var noSt = st.i;
      if (noBuf)
        buf = new u8(sl * 3);
      var cbuf = function(l2) {
        var bl = buf.length;
        if (l2 > bl) {
          var nbuf = new u8(Math.max(bl * 2, l2));
          nbuf.set(buf);
          buf = nbuf;
        }
      };
      var final = st.f || 0, pos = st.p || 0, bt = st.b || 0, lm = st.l, dm = st.d, lbt = st.m, dbt = st.n;
      var tbts = sl * 8;
      do {
        if (!lm) {
          final = bits(dat, pos, 1);
          var type = bits(dat, pos + 1, 3);
          pos += 3;
          if (!type) {
            var s = shft(pos) + 4, l = dat[s - 4] | dat[s - 3] << 8, t = s + l;
            if (t > sl) {
              if (noSt)
                err(0);
              break;
            }
            if (resize)
              cbuf(bt + l);
            buf.set(dat.subarray(s, t), bt);
            st.b = bt += l, st.p = pos = t * 8, st.f = final;
            continue;
          } else if (type == 1)
            lm = flrm, dm = fdrm, lbt = 9, dbt = 5;
          else if (type == 2) {
            var hLit = bits(dat, pos, 31) + 257, hcLen = bits(dat, pos + 10, 15) + 4;
            var tl = hLit + bits(dat, pos + 5, 31) + 1;
            pos += 14;
            var ldt = new u8(tl);
            var clt = new u8(19);
            for (var i = 0; i < hcLen; ++i) {
              clt[clim[i]] = bits(dat, pos + i * 3, 7);
            }
            pos += hcLen * 3;
            var clb = max(clt), clbmsk = (1 << clb) - 1;
            var clm = hMap(clt, clb, 1);
            for (var i = 0; i < tl; ) {
              var r = clm[bits(dat, pos, clbmsk)];
              pos += r & 15;
              var s = r >> 4;
              if (s < 16) {
                ldt[i++] = s;
              } else {
                var c = 0, n = 0;
                if (s == 16)
                  n = 3 + bits(dat, pos, 3), pos += 2, c = ldt[i - 1];
                else if (s == 17)
                  n = 3 + bits(dat, pos, 7), pos += 3;
                else if (s == 18)
                  n = 11 + bits(dat, pos, 127), pos += 7;
                while (n--)
                  ldt[i++] = c;
              }
            }
            var lt = ldt.subarray(0, hLit), dt = ldt.subarray(hLit);
            lbt = max(lt);
            dbt = max(dt);
            lm = hMap(lt, lbt, 1);
            dm = hMap(dt, dbt, 1);
          } else
            err(1);
          if (pos > tbts) {
            if (noSt)
              err(0);
            break;
          }
        }
        if (resize)
          cbuf(bt + 131072);
        var lms = (1 << lbt) - 1, dms = (1 << dbt) - 1;
        var lpos = pos;
        for (; ; lpos = pos) {
          var c = lm[bits16(dat, pos) & lms], sym = c >> 4;
          pos += c & 15;
          if (pos > tbts) {
            if (noSt)
              err(0);
            break;
          }
          if (!c)
            err(2);
          if (sym < 256)
            buf[bt++] = sym;
          else if (sym == 256) {
            lpos = pos, lm = null;
            break;
          } else {
            var add = sym - 254;
            if (sym > 264) {
              var i = sym - 257, b = fleb[i];
              add = bits(dat, pos, (1 << b) - 1) + fl[i];
              pos += b;
            }
            var d = dm[bits16(dat, pos) & dms], dsym = d >> 4;
            if (!d)
              err(3);
            pos += d & 15;
            var dt = fd[dsym];
            if (dsym > 3) {
              var b = fdeb[dsym];
              dt += bits16(dat, pos) & (1 << b) - 1, pos += b;
            }
            if (pos > tbts) {
              if (noSt)
                err(0);
              break;
            }
            if (resize)
              cbuf(bt + 131072);
            var end = bt + add;
            if (bt < dt) {
              var shift = dl - dt, dend = Math.min(dt, end);
              if (shift + bt < 0)
                err(3);
              for (; bt < dend; ++bt)
                buf[bt] = dict[shift + bt];
            }
            for (; bt < end; ++bt)
              buf[bt] = buf[bt - dt];
          }
        }
        st.l = lm, st.p = lpos, st.b = bt, st.f = final;
        if (lm)
          final = 1, st.m = lbt, st.d = dm, st.n = dbt;
      } while (!final);
      return bt != buf.length && noBuf ? slc(buf, 0, bt) : buf.subarray(0, bt);
    };
    et = /* @__PURE__ */ new u8(0);
    b2 = function(d, b) {
      return d[b] | d[b + 1] << 8;
    };
    b4 = function(d, b) {
      return (d[b] | d[b + 1] << 8 | d[b + 2] << 16 | d[b + 3] << 24) >>> 0;
    };
    b8 = function(d, b) {
      return b4(d, b) + b4(d, b + 4) * 4294967296;
    };
    td = typeof TextDecoder != "undefined" && /* @__PURE__ */ new TextDecoder();
    tds = 0;
    try {
      td.decode(et, { stream: true });
      tds = 1;
    } catch (e) {
    }
    dutf8 = function(d) {
      for (var r = "", i = 0; ; ) {
        var c = d[i++];
        var eb = (c > 127) + (c > 223) + (c > 239);
        if (i + eb > d.length)
          return { s: r, r: slc(d, i - 1) };
        if (!eb)
          r += String.fromCharCode(c);
        else if (eb == 3) {
          c = ((c & 15) << 18 | (d[i++] & 63) << 12 | (d[i++] & 63) << 6 | d[i++] & 63) - 65536, r += String.fromCharCode(55296 | c >> 10, 56320 | c & 1023);
        } else if (eb & 1)
          r += String.fromCharCode((c & 31) << 6 | d[i++] & 63);
        else
          r += String.fromCharCode((c & 15) << 12 | (d[i++] & 63) << 6 | d[i++] & 63);
      }
    };
    slzh = function(d, b) {
      return b + 30 + b2(d, b + 26) + b2(d, b + 28);
    };
    zh = function(d, b, z) {
      var fnl = b2(d, b + 28), efl = b2(d, b + 30), fn = strFromU8(d.subarray(b + 46, b + 46 + fnl), !(b2(d, b + 8) & 2048)), es = b + 46 + fnl;
      var _a2 = z64hs(d, es, efl, z, b4(d, b + 20), b4(d, b + 24), b4(d, b + 42)), sc = _a2[0], su = _a2[1], off = _a2[2];
      return [b2(d, b + 10), sc, su, fn, es + efl + b2(d, b + 32), off];
    };
    z64hs = function(d, b, l, z, sc, su, off) {
      var nsc = sc == 4294967295, nsu = su == 4294967295, noff = off == 4294967295, e = b + l;
      var nf = nsc + nsu + noff;
      if (z && nf) {
        for (; b + 4 < e; b += 4 + b2(d, b + 2)) {
          if (b2(d, b) == 1) {
            return [
              nsc ? b8(d, b + 4 + 8 * nsu) : sc,
              nsu ? b8(d, b + 4) : su,
              noff ? b8(d, b + 4 + 8 * (nsu + nsc)) : off,
              1
            ];
          }
        }
        if (z < 2)
          err(13);
      }
      return [sc, su, off, 0];
    };
  }
});

// src/privacy.ts
import path2 from "node:path";
import os2 from "node:os";
function projectRelativePath(root, file) {
  if (file.startsWith("file:")) {
    try {
      const url = new URL(file);
      file = decodeURIComponent(url.pathname);
      if (url.hostname) file = `\\\\${url.hostname}${file.replaceAll("/", "\\")}`;
      else if (/^\/[a-z]:\//i.test(file)) file = file.slice(1);
    } catch {
      return "[local file]";
    }
  }
  const paths = /^[a-z]:[\\/]|^\\\\/i.test(file) ? path2.win32 : path2.posix;
  if (!paths.isAbsolute(file)) return file.replaceAll("\\", "/").split("/").includes("..") ? "[external file]" : file;
  if (!root) return "[local file]";
  const relative = paths.relative(paths.resolve(root), file);
  if (relative === ".." || relative.startsWith(`..${paths.sep}`) || paths.isAbsolute(relative)) return "[external file]";
  return relative.replaceAll("\\", "/") || ".";
}
function redactDiagnostic(value) {
  return value.replace(/https?:\/\/[^\s"<>]+/gi, (url) => publicUrl(url)).replaceAll(os2.homedir(), "[home]").replace(/(?:file:\/\/)?\/(?:Users|home)\/[^/\\\r\n]+/g, "[home]").replace(/[A-Za-z]:[\\/]Users[\\/][^\\/\r\n]+/gi, "[home]").replace(/(?:\/private)?\/var\/folders\/[^/\s]+\/[^/\s]+/g, "[temp]").replace(/[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}/gi, "[email]").replace(/(Bearer\s+)\S+/gi, "$1[redacted]").replace(/((?:token|password|secret|api[_-]?key)\s*[:=]\s*)\S+/gi, "$1[redacted]");
}
function publicErrorMessage(error, root) {
  if (!(error instanceof Error)) return "Command failed.";
  if ("stderr" in error || "stdout" in error) {
    return "A local processing command failed. Check the input format and runtime availability.";
  }
  let message = error.message;
  for (const key of ["path", "dest"]) {
    const file = error[key];
    if (file) message = message.replaceAll(file, projectRelativePath(root, file));
  }
  if (root) message = message.replaceAll(path2.resolve(root), "[project]");
  return redactDiagnostic(message);
}
function publicUrl(value) {
  try {
    const url = new URL(value);
    if (!["http:", "https:"].includes(url.protocol)) return value === "about:blank" ? value : "[local file]";
    url.username = "";
    url.password = "";
    url.hash = "";
    for (const key of [...url.searchParams.keys()]) {
      if (/token|auth|secret|password|signature|credential|session|email|user.?id|api.?key/i.test(key)) url.searchParams.delete(key);
    }
    return url.href;
  } catch {
    return value;
  }
}
function publicMediaMetadata(value = {}) {
  if (!value || typeof value !== "object") return {};
  const result = Object.fromEntries(Object.entries(pick(value, ["durationSeconds", "width", "height", "fps", "hasAudio", "videoCodec", "pixelFormat", "audioCodec", "sampleRate", "schemaVersion", "partCount", "selfContained"])).filter(([, item]) => ["string", "number", "boolean"].includes(typeof item)));
  if (Array.isArray(value.parts)) result.parts = value.parts.map((part) => stringFields(part, ["id", "label", "group"]));
  const model = value.model ?? (typeof value.format === "string" && ["glb", "gltf"].includes(value.format) ? value : void 0);
  if (model) {
    const summary = pick(model, ["format", "version", "scenes", "meshes", "materials", "textures", "images", "buffers", "externalDependencies", "bounds", "hasDraco", "hasKtx2", "unitScale", "coordinateSystem", "supportsCompression", "supportsSkeletalAnimation", "supportsNodeAnimation", "sha256"]);
    summary.nodes = (model.nodes ?? []).map((node) => pick(node, ["name", "mesh", "children"]));
    summary.animations = (model.animations ?? []).map((animation) => pick(animation, ["name", "channels", "durationSeconds"]));
    if (value.model) Object.assign(result, { kind: "model3d", format: summary.format, model: summary });
    else Object.assign(result, summary);
  }
  return result;
}
function stringFields(value, keys) {
  return Object.fromEntries(Object.entries(pick(value, keys)).filter(([, item]) => typeof item === "string"));
}
function publicProvenance(value) {
  return stringFields(value, ["kind", "type", "license", "author", "source", "url", "version", "sourceId", "sourceVersion", "sourceCommit", "buildSource"]);
}
function clean(value, root, field = "") {
  if (typeof value === "string") {
    if (fileFields.has(field)) return projectRelativePath(root, value);
    if (["message", "error"].includes(field)) return redactDiagnostic(value);
    if (["url", "recordedUrl", "locator", "source"].includes(field)) return /^https?:/i.test(value) ? publicUrl(value) : projectRelativePath(root, value);
    return value;
  }
  if (!value || typeof value !== "object") return value;
  if (Array.isArray(value)) return value.map((item) => clean(item, root, field));
  let selected = value;
  if (value.id && value.kind && value.relativePath && "sha256" in value) {
    selected = { ...pick(value, ["id", "kind", "relativePath", "sha256", "transcript", "interactions", "provenance"]), metadata: publicMediaMetadata(value.metadata) };
  } else if (value.locator && value.relativePath && value.version) {
    selected = pick(value, ["id", "kind", "version", "relativePath", "files", "assetIds"]);
    if (/^https?:/i.test(value.locator)) selected.locator = publicUrl(value.locator);
  } else if (field === "provenance") selected = publicProvenance(value);
  else if (field === "metadata") selected = publicMediaMetadata(value);
  else if (field === "diagnostics") selected = pick(value, ["code", "message", "severity", "sceneId", "partId", "modelId", "atSeconds"]);
  else if (field === "webgl") return { available: value.available !== false };
  return Object.fromEntries(Object.entries(selected).filter(([key, child]) => !internalFields.has(key) && !(key === "format" && typeof child === "object")).map(([key, child]) => [key, clean(child, root, key)]));
}
function publicCommandResult(value, group2, operation2, root) {
  let selected = value;
  if (group2 === "setup" || group2 === "doctor") selected = pick(value, ["status", "target", "versions", "attribution"]);
  else if (group2 === "runtime") selected = { id: value.id, status: "ready" };
  else if (group2 === "exec") {
    selected = operation2 === "logs" ? { ...pick(value, ["id", "offset", "nextOffset"]), text: redactDiagnostic(value.text ?? "") } : { ...pick(value, ["id", "sourceId", "status", "workspace", "exitCode", "signal"]), ...value.error ? { error: redactDiagnostic(value.error) } : {} };
  } else if (group2 === "project" && operation2 === "compile") {
    selected = pick(value, ["revision", "composition", "directory", "range", "scale", "fps", "spatialRuntime", "sourceUsage", "quality"]);
  } else if (group2 === "review") {
    selected = pick(value, ["schemaVersion", "input", "revision", "metadata", "frames", "smallScreenFrames", "renderRange", "contextWarning", "sourceUsage", "spatialRuntime", "reviewPlan", "quality", "measurements", "mediaFindings", "visualReview", "instruction", "reportFile"]);
  } else if (group2 === "media" && operation2 === "probe") selected = publicMediaMetadata(value);
  return clean(selected, root);
}
var pick, fileFields, internalFields;
var init_privacy = __esm({
  "src/privacy.ts"() {
    "use strict";
    pick = (value, keys) => Object.fromEntries(keys.filter((key) => value?.[key] !== void 0).map((key) => [key, value[key]]));
    fileFields = /* @__PURE__ */ new Set(["root", "path", "relativePath", "input", "output", "composition", "directory", "workspace", "screenshot", "subtitles", "transcript", "interactions", "evidence", "reportFile", "renderContext", "baselineRenderContext", "buildSource"]);
    internalFields = /* @__PURE__ */ new Set(["pid", "workerPid", "env", "binDirectories", "cache", "fingerprint", "assetPath", "debug", "raw", "streams", "filename", "tags", "stopTimings"]);
  }
});

// src/util.ts
var util_exports = {};
__export(util_exports, {
  checkedRelative: () => checkedRelative,
  digest: () => digest,
  download: () => download,
  exists: () => exists,
  extractTar: () => extractTar,
  extractZip: () => extractZip,
  inside: () => inside,
  listFiles: () => listFiles,
  log: () => log,
  readJson: () => readJson,
  run: () => run,
  sha256: () => sha256,
  withLock: () => withLock,
  writeJson: () => writeJson
});
import fs from "node:fs/promises";
import { createReadStream } from "node:fs";
import { createHash, randomUUID } from "node:crypto";
import { spawn } from "node:child_process";
import path3 from "node:path";
async function readJson(file) {
  return JSON.parse(await fs.readFile(file, "utf8"));
}
async function writeJson(file, data) {
  await fs.mkdir(path3.dirname(file), { recursive: true });
  const temp = `${file}.${randomUUID()}.tmp`;
  try {
    await fs.writeFile(temp, JSON.stringify(data, null, 2) + "\n");
    await fs.rename(temp, file);
  } finally {
    await fs.rm(temp, { force: true });
  }
}
async function exists(file) {
  return fs.stat(file).then(() => true, () => false);
}
function inside(root, relative) {
  const target = path3.resolve(root, relative);
  const rel = path3.relative(path3.resolve(root), target);
  if (rel === ".." || rel.startsWith(`..${path3.sep}`) || path3.isAbsolute(rel)) throw new Error("Path escapes its project directory.");
  return target;
}
function checkedRelative(relative) {
  if (!relative || relative.includes("\0") || /^(?:[a-z]:|[\\/])/i.test(relative) || relative.replaceAll("\\", "/").split("/").includes("..")) throw new Error("Unsafe archive path.");
  return relative.replaceAll("\\", "/");
}
async function sha256(file) {
  const hash2 = createHash("sha256");
  for await (const chunk of createReadStream(file)) hash2.update(chunk);
  return hash2.digest("hex");
}
function digest(value) {
  return createHash("sha256").update(value).digest("hex");
}
function log(message) {
  process.stderr.write(`[wandeo] ${redactDiagnostic(message)}
`);
}
async function withLock(file, callback) {
  await fs.mkdir(path3.dirname(file), { recursive: true });
  const start = Date.now();
  while (true) {
    try {
      const handle = await fs.open(file, "wx");
      await handle.writeFile(JSON.stringify({ pid: process.pid, createdAt: Date.now() }));
      await handle.close();
      break;
    } catch (error) {
      if (error.code !== "EEXIST") throw error;
      const lock = await readJson(file).catch(() => null);
      if (lock?.pid) {
        try {
          process.kill(lock.pid, 0);
        } catch {
          await fs.rm(file, { force: true });
          continue;
        }
      }
      if (Date.now() - start > 20 * 6e4) throw new Error(`Timed out waiting for ${file}`);
      await new Promise((resolve2) => setTimeout(resolve2, 200));
    }
  }
  try {
    return await callback();
  } finally {
    await fs.rm(file, { force: true });
  }
}
async function run(command, args, options2 = {}) {
  return new Promise((resolve2, reject) => {
    const child = spawn(command, args, { cwd: options2.cwd, env: options2.env, windowsHide: true, stdio: ["ignore", "pipe", "pipe"] });
    let stdout = "", stderr = "";
    if (options2.stream) log(`Running ${path3.basename(command)}`);
    child.stdout.on("data", (data) => {
      stdout = (stdout + data.toString()).slice(-4 * 1024 * 1024);
    });
    child.stderr.on("data", (data) => {
      stderr = (stderr + data.toString()).slice(-4 * 1024 * 1024);
    });
    const timer = setTimeout(() => {
      child.kill();
      reject(new Error(`${path3.basename(command)} timed out.`));
    }, options2.timeout ?? 12e4);
    child.once("error", (error) => {
      clearTimeout(timer);
      reject(error);
    });
    child.once("exit", (code) => {
      clearTimeout(timer);
      code === 0 ? resolve2({ stdout, stderr }) : reject(new Error(`${path3.basename(command)} exited ${code}. Check the input format and runtime availability.`));
    });
  });
}
async function download(url, file, expected, maxBytes = 1024 * 1024 * 1024) {
  const parsed = new URL(url);
  if (parsed.protocol !== "https:" && !(process.env.WANDEO_TEST_HTTP === "1" && parsed.hostname === "127.0.0.1")) throw new Error("Downloads require HTTPS.");
  if (await exists(file) && expected?.sha256 && await sha256(file) === expected.sha256) return file;
  if (process.env.WANDEO_OFFLINE === "1") throw new Error(`Offline cache miss: ${path3.basename(file)}. Run setup or transcription online first.`);
  await fs.mkdir(path3.dirname(file), { recursive: true });
  const temporary = `${file}.download-${randomUUID()}`;
  for (let attempt = 1; attempt <= 3; attempt++) {
    try {
      log(`Downloading ${path3.basename(file)} (attempt ${attempt})`);
      const response = await fetch(url, { signal: AbortSignal.timeout(6e5), headers: { "User-Agent": "Wandeo/0.1" } });
      if (!response.ok || !response.body) throw new Error(`Download HTTP ${response.status}: ${url}`);
      if (Number(response.headers.get("content-length")) > maxBytes) throw new Error("Download exceeds size limit.");
      const handle = await fs.open(temporary, "wx");
      let size = 0;
      try {
        for await (const part of response.body) {
          size += part.length;
          if (size > maxBytes) throw new Error("Download exceeds size limit.");
          let offset = 0;
          while (offset < part.length) offset += (await handle.write(part, offset)).bytesWritten;
        }
      } finally {
        await handle.close();
      }
      if (expected?.size !== void 0 && size !== expected.size) throw new Error("Download size mismatch.");
      if (expected?.sha256 && await sha256(temporary) !== expected.sha256) throw new Error("Download checksum mismatch.");
      await fs.rename(temporary, file);
      return file;
    } catch (error) {
      await fs.rm(temporary, { force: true });
      if (attempt === 3) throw error;
    }
  }
  throw new Error("Download failed.");
}
async function extractZip(file, destination, stripRoot = false, filter) {
  let total = 0, count = 0;
  const entries = unzipSync(await fs.readFile(file), { filter: (entry) => {
    checkedRelative(entry.name);
    if (++count > 5e4 || (total += entry.originalSize) > 2 * 1024 ** 3 || entry.originalSize > 1024 ** 3) throw new Error("Archive exceeds extraction limits.");
    return !entry.name.endsWith("/") && (!filter || filter(entry.name));
  } });
  for (const [name, bytes] of Object.entries(entries)) {
    const relative = stripRoot ? name.split("/").slice(1).join("/") : name;
    if (!relative) continue;
    const output = inside(destination, relative);
    await fs.mkdir(path3.dirname(output), { recursive: true });
    await fs.writeFile(output, bytes);
  }
}
async function extractTar(file, destination) {
  const entries = await run("tar", ["-tzf", file]);
  for (const name of entries.stdout.split("\n").filter(Boolean)) checkedRelative(name);
  await fs.mkdir(destination, { recursive: true });
  await run("tar", ["-xzf", file, "-C", destination]);
}
async function listFiles(root, excluded = () => false, limit = 2e4) {
  const files = [];
  const walk = async (directory) => {
    for (const entry of await fs.readdir(directory, { withFileTypes: true })) {
      const file = path3.join(directory, entry.name), relative = path3.relative(root, file).replaceAll("\\", "/");
      if (excluded(relative) || entry.isSymbolicLink()) continue;
      if (entry.isDirectory()) await walk(file);
      else if (entry.isFile()) {
        if (files.length >= limit) throw new Error("Source contains too many files.");
        files.push(relative);
      }
    }
  };
  await walk(root);
  return files.sort();
}
var init_util = __esm({
  "src/util.ts"() {
    "use strict";
    init_esm();
    init_privacy();
  }
});

// src/cli.ts
import path17 from "node:path";
import { parseArgs } from "node:util";

// src/runtime.ts
import fs2 from "node:fs/promises";
import path4 from "node:path";
import { createReadStream as createReadStream2, createWriteStream } from "node:fs";
import { createGunzip } from "node:zlib";
import { pipeline } from "node:stream/promises";
import { randomUUID as randomUUID2 } from "node:crypto";

// src/environment.ts
import path from "node:path";
import os from "node:os";
import { fileURLToPath } from "node:url";
import { createRequire } from "node:module";
var PLUGIN_ROOT = process.env.WANDEO_PLUGIN_ROOT || path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
var configured;
function cacheRoot() {
  return path.resolve(process.env.WANDEO_CACHE_DIR || (process.platform === "win32" ? path.join(process.env.LOCALAPPDATA || os.homedir(), "Wandeo", "Cache") : path.join(os.homedir(), "Library", "Caches", "Wandeo")));
}
function targetKey(platform = process.platform, arch = process.arch) {
  const target = `${platform}-${arch}`;
  if (!["darwin-arm64", "darwin-x64", "win32-x64"].includes(target)) throw new Error(`Unsupported local target: ${target}. Supported: macOS arm64/x64 and Windows x64.`);
  return target;
}
function configureRuntime(config) {
  configured = config;
}
function runtimeConfig() {
  if (!configured) throw new Error("Runtime is not configured. Run wandeo setup.");
  return configured;
}
function getFfmpegBinaryPath() {
  return runtimeConfig().ffmpeg;
}
function getFfprobeBinaryPath() {
  return runtimeConfig().ffprobe;
}
function browserPath() {
  return runtimeConfig().browser;
}
function runtimeRequire(root) {
  return createRequire(path.join(root || runtimeConfig().depsRoot, "package.json"));
}

// src/runtime.ts
init_util();
function binaryArchitecture(buffer) {
  if (buffer.length >= 8 && buffer.readUInt32LE(0) === 4277009103) return { 16777223: "x64", 16777228: "arm64" }[buffer.readUInt32LE(4)] || "unknown";
  if (buffer.subarray(0, 2).toString() === "MZ" && buffer.length >= 64) {
    const pe = buffer.readUInt32LE(60);
    if (pe + 6 <= buffer.length && buffer.subarray(pe, pe + 4).toString() === "PE\0\0") return { 34404: "x64", 43620: "arm64" }[buffer.readUInt16LE(pe + 4)] || "unknown";
  }
  return "unknown";
}
async function packagesHealthy(root, kind) {
  try {
    const wanted = await readJson(path4.join(PLUGIN_ROOT, "runtime", kind, "package.json"));
    for (const [name, version] of Object.entries(wanted.dependencies)) {
      const installed = await readJson(path4.join(root, "node_modules", name, "package.json"));
      if (installed.version !== version) return false;
    }
    const files = kind === "base" ? ["hyperframes/bin/hyperframes.mjs", "gsap/dist/gsap.min.js", "@fontsource-variable/noto-sans-sc/wght.css", "@fontsource-variable/noto-serif-sc/wght.css"] : ["@huggingface/transformers/dist/transformers.node.cjs"];
    for (const file of files) if (!await exists(path4.join(root, "node_modules", file))) return false;
    if (kind === "base") {
      runtimeRequire(root).resolve("puppeteer-core");
      runtimeRequire(root)("sharp");
    }
    return await exists(path4.join(root, ".complete"));
  } catch {
    return false;
  }
}
async function assertArchitecture(file, target) {
  const handle = await fs2.open(file, "r");
  const buffer = Buffer.alloc(8192);
  try {
    await handle.read(buffer);
  } finally {
    await handle.close();
  }
  const actual = binaryArchitecture(buffer);
  if (actual !== target.split("-")[1]) throw new Error(`Wrong binary architecture for ${target}: ${actual} (${path4.basename(file)})`);
}
async function ensurePackages(kind) {
  const source = path4.join(PLUGIN_ROOT, "runtime", kind);
  const lock = await fs2.readFile(path4.join(source, "package-lock.json"));
  const root = path4.join(cacheRoot(), "packages", `${kind}-${targetKey()}-${digest(lock).slice(0, 16)}`);
  await withLock(`${root}.lock`, async () => {
    if (await packagesHealthy(root, kind)) return;
    if (process.env.WANDEO_OFFLINE === "1") throw new Error(`Offline cache miss for ${kind} runtime packages.`);
    const temporary = `${root}.tmp-${randomUUID2()}`;
    await fs2.mkdir(temporary, { recursive: true });
    try {
      await fs2.copyFile(path4.join(source, "package.json"), path4.join(temporary, "package.json"));
      await fs2.writeFile(path4.join(temporary, "package-lock.json"), lock);
      let npmCli = process.env.WANDEO_NPM_CLI || path4.resolve(path4.dirname(process.execPath), process.platform === "win32" ? "node_modules/npm/bin/npm-cli.js" : "../lib/node_modules/npm/bin/npm-cli.js");
      if (!await exists(npmCli)) {
        const portable = await prepareRuntime({ name: "node", version: "24.21.0" });
        npmCli = path4.resolve(portable.binDirectories[0], process.platform === "win32" ? "node_modules/npm/bin/npm-cli.js" : "../lib/node_modules/npm/bin/npm-cli.js");
      }
      log(`Installing pinned ${kind} packages in cache`);
      await run(process.execPath, [npmCli, "ci", "--omit=dev", "--no-audit", "--no-fund"], { cwd: temporary, timeout: 20 * 6e4, stream: true, env: { ...process.env, PUPPETEER_SKIP_DOWNLOAD: "true", npm_config_cache: path4.join(cacheRoot(), "npm") } });
      await fs2.writeFile(path4.join(temporary, ".complete"), digest(lock));
      await fs2.rm(root, { recursive: true, force: true });
      await fs2.rename(temporary, root);
    } finally {
      await fs2.rm(temporary, { recursive: true, force: true });
    }
  });
  return root;
}
async function manifestAndRoot() {
  const manifest = await readJson(path4.join(PLUGIN_ROOT, "runtime", "manifest.json"));
  const key = digest(JSON.stringify(manifest)).slice(0, 12);
  const target = targetKey();
  return { manifest, target, root: path4.join(cacheRoot(), "media", `${target}-${key}`) };
}
async function valid(config, manifest) {
  try {
    for (const key of ["ffmpeg", "ffprobe"]) {
      if (await sha256(config[key]) !== manifest.media.targets[config.target][key].binarySha256) return false;
      await assertArchitecture(config[key], config.target);
    }
    if (await sha256(config.browser) !== manifest.browser.artifacts[config.target].executableSha256) return false;
    await assertArchitecture(config.browser, config.target);
    return packagesHealthy(config.depsRoot, "base");
  } catch {
    return false;
  }
}
async function loadRuntime() {
  const { root, manifest } = await manifestAndRoot();
  const config = await readJson(path4.join(root, "ready.json")).catch(() => null);
  if (!config || config.root !== root || !await valid(config, manifest)) throw new Error("Runtime is missing or damaged. Run wandeo setup.");
  configureRuntime(config);
  return config;
}
async function setup() {
  const { manifest, target, root } = await manifestAndRoot();
  const depsRoot = await ensurePackages("base");
  await withLock(`${root}.lock`, async () => {
    const previous = await readJson(path4.join(root, "ready.json")).catch(() => null);
    if (previous && previous.depsRoot === depsRoot && await valid(previous, manifest)) return;
    const temporary = `${root}.tmp-${randomUUID2()}`;
    await fs2.mkdir(temporary, { recursive: true });
    const archives = path4.join(cacheRoot(), "downloads");
    const extension = target.startsWith("win32") ? ".exe" : "";
    try {
      for (const name of ["ffmpeg", "ffprobe"]) {
        const spec2 = manifest.media.targets[target][name];
        const archive2 = await download(`${manifest.media.baseUrl}/${spec2.asset}`, path4.join(archives, spec2.sha256 + ".gz"), spec2);
        const output = path4.join(temporary, `${name}${extension}`);
        await pipeline(createReadStream2(archive2), createGunzip(), createWriteStream(output));
        await fs2.chmod(output, 493);
      }
      for (const name of ["LICENSE", "README"]) {
        const spec2 = manifest.media.targets[target][name];
        const file = await download(`${manifest.media.baseUrl}/${spec2.asset}`, path4.join(archives, spec2.sha256 + ".txt"), spec2);
        await fs2.copyFile(file, path4.join(temporary, `FFmpeg-${name}.txt`));
      }
      const spec = manifest.browser.artifacts[target];
      const archive = await download(spec.url, path4.join(archives, spec.sha256 + ".zip"), spec);
      await extractZip(archive, path4.join(temporary, "browser"));
      const browserDirectory = `chrome-headless-shell-${target === "darwin-arm64" ? "mac-arm64" : target === "darwin-x64" ? "mac-x64" : "win64"}`;
      const relativeBrowser = path4.join("browser", browserDirectory, `chrome-headless-shell${extension}`);
      await fs2.chmod(path4.join(temporary, relativeBrowser), 493);
      const staged = { root: temporary, target, depsRoot, browser: path4.join(temporary, relativeBrowser), ffmpeg: path4.join(temporary, `ffmpeg${extension}`), ffprobe: path4.join(temporary, `ffprobe${extension}`) };
      if (!await valid(staged, manifest)) throw new Error("Prepared runtime failed integrity or architecture validation.");
      await fs2.rm(root, { force: true, recursive: true });
      await fs2.rename(temporary, root);
      await writeJson(path4.join(root, "ready.json"), { ...staged, root, browser: path4.join(root, relativeBrowser), ffmpeg: path4.join(root, `ffmpeg${extension}`), ffprobe: path4.join(root, `ffprobe${extension}`) });
    } finally {
      await fs2.rm(temporary, { recursive: true, force: true });
    }
  });
  return doctor();
}
async function doctor() {
  const config = await loadRuntime();
  const versions = {};
  for (const key of ["ffmpeg", "ffprobe", "browser"]) {
    const result = await run(config[key], [key === "browser" ? "--version" : "-version"]);
    versions[key] = (result.stdout || result.stderr).split("\n")[0];
  }
  const page = await run(config.browser, ["--headless", "--disable-gpu", "--dump-dom", "about:blank"], { timeout: 3e4 });
  if (!page.stdout.includes("<html")) throw new Error("Browser blank-page preflight failed.");
  return { status: "ready", target: config.target, cache: cacheRoot(), versions, attribution: "Includes code derived from Recordly (AGPLv3)." };
}
async function prepareRuntime(request) {
  if (request.name === "node" && !request.packageUrl) {
    const version = String(request.version || "24.21.0").replace(/^v/, "");
    if (!/^\d+\.\d+\.\d+$/.test(version)) throw new Error("Choose an exact Node version.");
    const platform = process.platform === "win32" ? "win" : "darwin";
    const archive = platform === "win" ? "zip" : "tar.gz";
    const directory = `node-v${version}-${platform}-${process.arch}`, filename = `${directory}.${archive}`;
    const checksumUrl = `https://nodejs.org/dist/v${version}/SHASUMS256.txt`;
    const response = await fetch(checksumUrl);
    if (!response.ok) throw new Error(`Node checksum HTTP ${response.status}`);
    const hash2 = (await response.text()).split("\n").find((line) => line.trim().split(/\s+/)[1] === filename)?.split(/\s+/)[0];
    request = { name: "node", version, archive, packageUrl: `https://nodejs.org/dist/v${version}/${filename}`, checksumUrl, sha256: hash2, binDirectories: [platform === "win" ? directory : `${directory}/bin`] };
  }
  if (!/^[a-z0-9-]+$/.test(request.name) || !/^[a-f\d]{64}$/i.test(request.sha256 || "") || !["zip", "tar.gz"].includes(request.archive) || !Array.isArray(request.binDirectories)) throw new Error("Runtime descriptor needs name, exact version, HTTPS packageUrl, sha256, archive and binDirectories.");
  const id = `${request.name}-${digest(JSON.stringify(request)).slice(0, 20)}`, root = path4.join(cacheRoot(), "portable", id);
  await withLock(`${root}.lock`, async () => {
    if (await exists(path4.join(root, "runtime.json"))) return;
    const archive = await download(request.packageUrl, path4.join(cacheRoot(), "downloads", `${request.sha256}.${request.archive}`), { sha256: request.sha256 });
    const temporary = `${root}.tmp-${randomUUID2()}`;
    await fs2.mkdir(temporary, { recursive: true });
    try {
      if (request.archive === "zip") await extractZip(archive, temporary);
      else await extractTar(archive, temporary);
      const { inside: inside2 } = await Promise.resolve().then(() => (init_util(), util_exports));
      for (const directory of request.binDirectories) inside2(temporary, directory);
      await writeJson(path4.join(temporary, "runtime.json"), { id, ...request });
      await fs2.rename(temporary, root);
    } finally {
      await fs2.rm(temporary, { force: true, recursive: true });
    }
  });
  return { id, root, binDirectories: request.binDirectories.map((relative) => path4.join(root, relative)) };
}

// src/project.ts
init_util();
import fs3 from "node:fs/promises";
import path5 from "node:path";
import { randomUUID as randomUUID3 } from "node:crypto";
function projectRoot(root) {
  if (!root) throw new Error("--project is required.");
  return path5.resolve(root);
}
function manifestFile(root) {
  return path5.join(projectRoot(root), "manifest.json");
}
async function getProject(root) {
  const value = await readJson(manifestFile(root));
  if (value.schemaVersion !== 1 || !Array.isArray(value.assets) || !Array.isArray(value.sources)) throw new Error("Not a Wandeo project.");
  return value;
}
async function updateProject(root, update) {
  return withLock(path5.join(projectRoot(root), ".project.lock"), async () => {
    const manifest = await getProject(root);
    const result = await update(manifest);
    await writeJson(manifestFile(root), manifest);
    return result;
  });
}
async function initProject(root, title = "Untitled film") {
  root = projectRoot(root);
  if (await exists(manifestFile(root))) return { root, manifest: await getProject(root), reused: true };
  await fs3.mkdir(root, { recursive: true });
  for (const name of ["assets", "sources", "work", "outputs", "versions", "evidence"]) await fs3.mkdir(path5.join(root, name), { recursive: true });
  const manifest = { schemaVersion: 1, id: randomUUID3(), title, createdAt: (/* @__PURE__ */ new Date()).toISOString(), revision: 0, assets: [], sources: [], artifacts: [] };
  await writeJson(manifestFile(root), manifest);
  await writeJson(path5.join(root, "director-state.json"), { goal: "", evidence: [], shots: [], decisions: [], openQuestions: [], revisionDeltas: [] });
  await writeJson(path5.join(root, "project.json"), { schemaVersion: "1.1.0", projectId: manifest.id, width: 1920, height: 1080, fps: 30, durationSeconds: 0, scenes: [] });
  return { root, manifest, reused: false };
}
async function assetById(root, id) {
  const asset = (await getProject(root)).assets.find((item) => item.id === id);
  if (!asset) throw new Error(`Unknown asset: ${id}`);
  return { ...asset, path: inside(root, asset.relativePath) };
}
async function registerAsset(root, file, kind, metadata, provenance) {
  file = path5.resolve(file);
  const hash2 = await sha256(file);
  return updateProject(root, async (manifest) => {
    const existing = manifest.assets.find((asset2) => asset2.sha256 === hash2 && asset2.kind === kind);
    if (existing) return existing;
    const extension = path5.extname(file).toLowerCase();
    const id = `asset-${hash2.slice(0, 20)}`, relativePath = `assets/${id}${extension}`;
    const destination = inside(root, relativePath);
    if (destination !== file) await fs3.copyFile(file, destination);
    const asset = { id, relativePath, name: path5.basename(file), sha256: hash2, kind, metadata, provenance };
    manifest.assets.push(asset);
    return asset;
  });
}
async function saveArtifact(root, kind, file, revision, renderContext) {
  const relativePath = path5.relative(projectRoot(root), path5.resolve(file)).replaceAll("\\", "/");
  inside(root, relativePath);
  if (renderContext) inside(root, renderContext);
  return updateProject(root, (manifest) => {
    const artifact = { kind, relativePath, revision: revision ?? manifest.revision, createdAt: (/* @__PURE__ */ new Date()).toISOString(), ...renderContext ? { renderContext } : {} };
    manifest.artifacts.push(artifact);
    return artifact;
  });
}
async function loadTimeline(root, input) {
  const value = await readJson(input ? path5.resolve(input) : path5.join(root, "project.json"));
  const manifest = await getProject(root);
  if (value.projectId !== manifest.id) throw new Error(`Timeline projectId must equal ${manifest.id}.`);
  return value;
}
async function checkpointTimeline(root, timeline) {
  return updateProject(root, async (manifest) => {
    const previous = await readJson(path5.join(root, "versions", `r${manifest.revision}.json`)).catch(() => null);
    if (JSON.stringify(previous) !== JSON.stringify(timeline)) {
      manifest.revision++;
      await writeJson(path5.join(root, "versions", `r${manifest.revision}.json`), timeline);
    }
    await writeJson(path5.join(root, "project.json"), timeline);
    return manifest.revision;
  });
}

// src/media.ts
import fs5 from "node:fs/promises";
import os3 from "node:os";
import path7 from "node:path";
import { randomUUID as randomUUID4 } from "node:crypto";
init_util();

// src/core/spatial3d.ts
import fs4 from "node:fs/promises";
import path6 from "node:path";
import { createHash as createHash2 } from "node:crypto";

// src/core/native-anatomy.ts
import { existsSync, readFileSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath as fileURLToPath2, pathToFileURL } from "node:url";

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
var tenth = (value) => {
  const text = (Math.round(value * 10) / 10).toFixed(1).replace(/\.0$/, "");
  return text === "-0" ? "0" : text;
};
function pathOf(points, closed = false) {
  if (!points.length)
    return "";
  return points.map(([x, y], at) => `${at ? "L" : "M"}${tenth(x)} ${tenth(y)}`).join("") + (closed ? "Z" : "");
}
function roundedPlan({ x, y, w, d, r }, steps = 8) {
  const radius = Math.max(0, Math.min(r, w / 2, d / 2));
  const corners = [
    [x + w - radius, y + radius, -90],
    [x + w - radius, y + d - radius, 0],
    [x + radius, y + d - radius, 90],
    [x + radius, y + radius, 180]
  ];
  const out2 = [];
  for (const [cx, cy, start] of corners) {
    const count = radius > 0 ? steps : 0;
    for (let step = 0; step <= count; step++) {
      const angle = (start + (count ? 90 * step / count : 45)) * RADIANS;
      out2.push([cx + radius * Math.cos(angle), cy + radius * Math.sin(angle)]);
    }
  }
  return out2;
}
var escape = (text) => text.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
var attrs = (pairs) => Object.entries(pairs).filter(([, value]) => value !== void 0 && value !== false).map(([key, value]) => ` ${key}="${escape(String(value))}"`).join("");
function solidSvg(paths, { tone = "hi", crease = "faint", halo = false, lit = false, flat = false, className, inner = "" } = {}) {
  const parts = [];
  if (halo)
    parts.push(`<path class="iso-halo" d="${paths.fill}"/>`);
  parts.push(`<path class="iso-fill" d="${paths.fill}"/>`);
  if (!flat) {
    paths.shades.forEach((d, shade) => {
      if (d)
        parts.push(`<path class="iso-shade" data-shade="${shade}" d="${d}"/>`);
    });
    parts.push(`<path class="iso-top" d="${paths.top}"/>`);
  }
  if (crease !== "none" && paths.crease)
    parts.push(`<path class="iso-line iso-crease" data-tone="${crease}" d="${paths.crease}"/>`);
  if (crease !== "none" && paths.bevel)
    parts.push(`<path class="iso-line iso-bevel" data-tone="${crease}" d="${paths.bevel}"/>`);
  if (inner)
    parts.push(inner);
  parts.push(`<path class="iso-line iso-edge" data-tone="${tone}" d="${paths.outline}"/>`);
  return `<g${attrs({ class: className ? `iso-solid ${className}` : "iso-solid", "data-lit": lit ? "" : void 0, "data-seamless": paths.seamless ? "" : void 0 })}>${parts.join("")}</g>`;
}
function lineSvg(d, { tone = "lo", dotted = false, dashed = false, flow = false, className, free: free2 } = {}) {
  if (!d)
    return "";
  return `<path${attrs({
    class: className ? `iso-line ${className}` : "iso-line",
    "data-tone": tone,
    "data-free": free2 === true ? "" : free2 || void 0,
    "data-dotted": dotted ? "" : void 0,
    "data-dashed": dashed ? "" : void 0,
    "data-flow": flow ? "" : void 0,
    d
  })}/>`;
}
var ISO_CSS = `
.iso{
  --anatomy-page:#0b0b0b;--anatomy-card:#131313;--anatomy-text:#a3a3a3;--anatomy-strong:#e6e6e6;--anatomy-muted:#6e6e6e;
  --anatomy-paper:#131313;--anatomy-face:#1b1b1b;--anatomy-top:#1c1c1c;
  --anatomy-shade-0:#0f0f0f;--anatomy-shade-1:#121212;--anatomy-shade-2:#151515;--anatomy-shade-3:#181818;
  --anatomy-lit-top:#262626;--anatomy-lit-shade:#1d1d1d;
  --anatomy-hi:#d4d4d4;--anatomy-mid:#6a6a6a;--anatomy-lo:#3e3e3e;--anatomy-faint:#2a2a2a;--anatomy-lit:#ffffff;
  --anatomy-halo:#050505;--anatomy-halo-opacity:.9;--anatomy-dot:#e6e6e6;
  --anatomy-red:#ff6b6b;--anatomy-green:#6be0a0;--anatomy-blue:#6b9bff;
  --anatomy-weight:.6px;--anatomy-ease:cubic-bezier(.32,.72,0,1);
  --anatomy-mono:ui-monospace,"SF Mono",Menlo,Consolas,monospace;
  --anatomy-lift:inset 0 1px 0 0 #ffffff0a,inset 0 0 0 1px #ffffff06,0 0 0 1px #00000026,0 1px 1px -.5px #00000014,0 3px 3px -1.5px #00000014,0 6px 6px -3px #00000014,0 12px 12px -6px #00000014;
}
.iso[data-theme="light"]{
  --anatomy-page:#f2f2ef;--anatomy-card:#fbfbfa;--anatomy-text:#57575a;--anatomy-strong:#18181a;--anatomy-muted:#8c8c90;
  --anatomy-paper:#fbfbfa;--anatomy-face:#ffffff;--anatomy-top:#ffffff;
  --anatomy-shade-0:#dcdcd9;--anatomy-shade-1:#e5e5e2;--anatomy-shade-2:#ededea;--anatomy-shade-3:#f4f4f1;
  --anatomy-lit-top:#ffffff;--anatomy-lit-shade:#eeeeeb;
  --anatomy-hi:#26262a;--anatomy-mid:#8a8a8f;--anatomy-lo:#b4b4b8;--anatomy-faint:#d4d4d6;--anatomy-lit:#000000;
  --anatomy-halo:#8a8a80;--anatomy-halo-opacity:.32;--anatomy-dot:#3a3a3e;
  --anatomy-red:#e5484d;--anatomy-green:#30a46c;--anatomy-blue:#3e63dd;
  --anatomy-lift:inset 0 1px 0 0 #ffffff,0 0 0 1px #0000000f,0 1px 1px -.5px #0000000a,0 3px 3px -1.5px #0000000a,0 6px 6px -3px #0000000a,0 12px 12px -6px #0000000a;
}
.iso-svg{display:block;width:100%;height:auto;overflow:visible}
.iso-svg path,.iso-svg circle{vector-effect:non-scaling-stroke}
.iso-fill{fill:var(--anatomy-paper);stroke:none}
.iso-solid[data-lit]>.iso-fill{fill:var(--anatomy-face)}
.iso-shade,.iso-top{stroke:none}
.iso-shade[data-shade="0"]{fill:var(--anatomy-shade-0)}
.iso-shade[data-shade="1"]{fill:var(--anatomy-shade-1)}
.iso-shade[data-shade="2"]{fill:var(--anatomy-shade-2)}
.iso-shade[data-shade="3"]{fill:var(--anatomy-shade-3)}
.iso-top{fill:var(--anatomy-top)}
.iso-solid[data-lit]>.iso-top{fill:var(--anatomy-lit-top)}
.iso-solid[data-lit]>.iso-shade{fill:var(--anatomy-lit-shade)}
.iso-solid[data-seamless]>.iso-shade,.iso-solid[data-seamless]>.iso-top{stroke-width:.4;stroke-linejoin:round}
.iso-solid[data-seamless]>.iso-shade[data-shade="0"]{stroke:var(--anatomy-shade-0)}
.iso-solid[data-seamless]>.iso-shade[data-shade="1"]{stroke:var(--anatomy-shade-1)}
.iso-solid[data-seamless]>.iso-shade[data-shade="2"]{stroke:var(--anatomy-shade-2)}
.iso-solid[data-seamless]>.iso-shade[data-shade="3"]{stroke:var(--anatomy-shade-3)}
.iso-solid[data-seamless]>.iso-top{stroke:var(--anatomy-top)}
.iso-solid[data-seamless][data-lit]>.iso-top{stroke:var(--anatomy-lit-top)}
.iso-solid[data-seamless][data-lit]>.iso-shade{stroke:var(--anatomy-lit-shade)}
.iso-solid[data-lit]>.iso-edge{stroke:var(--anatomy-lit)}
.iso-halo{fill:var(--anatomy-halo);stroke:none;filter:blur(9px);opacity:var(--anatomy-halo-opacity);transform:translateY(3px)}
.iso-line{fill:none;stroke:var(--anatomy-lo);stroke-width:var(--anatomy-weight);stroke-linecap:round;stroke-linejoin:round}
.iso-line[data-tone="hi"]{stroke:var(--anatomy-hi)}
.iso-line[data-tone="mid"]{stroke:var(--anatomy-mid)}
.iso-line[data-tone="lo"]{stroke:var(--anatomy-lo)}
.iso-line[data-tone="faint"]{stroke:var(--anatomy-faint)}
.iso-line[data-tone="lit"]{stroke:var(--anatomy-lit)}
.iso-line[data-tone="red"]{stroke:var(--anatomy-red)}
.iso-line[data-tone="green"]{stroke:var(--anatomy-green)}
.iso-line[data-tone="blue"]{stroke:var(--anatomy-blue)}
.iso-line[data-dotted]{stroke-dasharray:.01 3.5;stroke-width:1}
.iso-line[data-dashed]{stroke-dasharray:3 3}
.iso-line[data-flow]{stroke-dasharray:2 6}
.iso-wire-end{fill:var(--anatomy-paper);stroke:var(--anatomy-lo);stroke-width:var(--anatomy-weight)}
.iso-wire[data-tone="hi"] .iso-wire-end{stroke:var(--anatomy-hi)}
.iso-wire[data-tone="mid"] .iso-wire-end{stroke:var(--anatomy-mid)}
.iso-wire[data-tone="faint"] .iso-wire-end{stroke:var(--anatomy-faint)}
.iso-wire[data-tone="lit"] .iso-wire-end{stroke:var(--anatomy-lit)}
.iso-dots circle{fill:var(--anatomy-dot);stroke:none;opacity:.32}
.iso-dots[data-tone="hi"] circle{opacity:.85}
.iso-dots[data-tone="mid"] circle{opacity:.45}
.iso-dots[data-tone="lo"] circle{opacity:.22}
.iso-dots[data-tone="faint"] circle{opacity:.12}
.iso-face-text{fill:var(--anatomy-mid);font-family:var(--anatomy-mono);letter-spacing:.04em}
.iso-face-text[data-tone="hi"]{fill:var(--anatomy-hi)}
.iso-face-text[data-tone="lo"]{fill:var(--anatomy-lo)}
.iso-face-text[data-tone="faint"]{fill:var(--anatomy-faint)}
.tb-body{fill:var(--anatomy-shade-2);stroke:none}
.tb-shine{fill:var(--anatomy-top);stroke:none}
.tb-shade{fill:var(--anatomy-shade-0);stroke:none}
.tb-ring{fill:none;stroke:var(--anatomy-lo);stroke-width:.45;stroke-linecap:butt;stroke-linejoin:round}
.tb-ring[data-tone="mid"]{stroke:var(--anatomy-mid)}
.tb-ring[data-tone="faint"]{stroke:var(--anatomy-faint)}
.tb-ring[data-tone="hi"]{stroke:var(--anatomy-hi)}
@keyframes iso-flow{to{stroke-dashoffset:-32}}
@keyframes iso-pulse{0%,100%{opacity:.18}12%{opacity:1}40%{opacity:.18}}
.iso-line[data-flow]{animation:iso-flow 1600ms linear infinite}
.iso-dots circle[data-pulse]{animation:iso-pulse 1600ms steps(1,end) infinite;animation-delay:var(--pulse-at,0ms)}
.iso-figure{margin:32px 0 36px}
.iso-plate{position:relative;padding:52px 24px;border-radius:0;background:var(--anatomy-card);box-shadow:0 0 0 1px var(--anatomy-mid);--anatomy-paper:var(--anatomy-card)}
.iso-plate-corners{position:absolute;inset:18px 20px;pointer-events:none}
.iso-plate-corner{position:absolute;color:var(--anatomy-muted);font-family:var(--anatomy-mono);font-size:10.5px;line-height:1;letter-spacing:.04em;white-space:nowrap}
.iso-plate-corner[data-corner="fig"]{top:0;left:0;color:var(--anatomy-text)}
.iso-plate-corner[data-corner="title"]{top:0;right:0;text-transform:uppercase;letter-spacing:.1em}
.iso-plate-corner[data-corner="hint"]{bottom:0;left:0;text-transform:uppercase;letter-spacing:.1em}
.iso-plate-corner[data-corner="readout"]{right:0;bottom:0;color:var(--anatomy-text);font-variant-numeric:tabular-nums}
.iso-plate .iso-svg{margin:0 auto}
.iso-legend{display:grid;gap:8px;margin-top:12px;color:var(--anatomy-muted);font-size:13px;line-height:1.55}
.iso-keys{display:flex;flex-wrap:wrap;gap:6px 18px}
.iso-key{display:inline-flex;align-items:center;gap:7px}
.iso-swatch{width:16px;height:10px;flex:none;overflow:visible}
.iso-swatch path{fill:none;stroke:var(--anatomy-hi);stroke-width:1;vector-effect:non-scaling-stroke;stroke-linejoin:round;stroke-linecap:round}
.iso-swatch[data-mark="raised"] path,.iso-swatch[data-mark="flat"] path{stroke:var(--anatomy-mid)}
.iso-swatch[data-mark="lit"] path{stroke:var(--anatomy-lit)}
.iso-swatch[data-mark="dim"] path{stroke:var(--anatomy-lo)}
.iso-swatch[data-mark="dotted"] path{stroke-dasharray:.01 3;stroke-width:1.4}
.iso-swatch[data-mark="dashed"] path{stroke-dasharray:3 2.5}
.iso-swatch[data-mark="red"] path{stroke:var(--anatomy-red)}
.iso-swatch[data-mark="green"] path{stroke:var(--anatomy-green)}
.iso-swatch[data-mark="blue"] path{stroke:var(--anatomy-blue)}
.iso-swatch-crease{stroke:var(--anatomy-lo)!important}
@media (max-width:560px){.iso-plate{padding:48px 12px 70px}.iso-plate-corner[data-corner="hint"]{bottom:18px}}
@media (prefers-reduced-motion:reduce){.iso-line[data-flow],.iso-dots circle[data-pulse]{animation:none}}
`;

// src/core/native-anatomy.ts
var nativeRoot = dirname(fileURLToPath2(import.meta.url));
var nativeExamplePath = [
  resolve(nativeRoot, "../third_party/anatomy/examples/turning-dial/build.mjs"),
  resolve(nativeRoot, "../../third_party/anatomy/examples/turning-dial/build.mjs"),
  join(process.cwd(), "third_party/anatomy/examples/turning-dial/build.mjs")
].find(existsSync);
if (!nativeExamplePath) throw new Error("ANATOMY_NATIVE_SOURCE_MISSING: turning-dial/build.mjs is not present in the plugin package.");
var { out } = await import(pathToFileURL(nativeExamplePath).href);
var dialCssPath = [
  resolve(nativeRoot, "../third_party/anatomy/examples/turning-dial/dial.css"),
  resolve(nativeRoot, "../../third_party/anatomy/examples/turning-dial/dial.css"),
  join(process.cwd(), "third_party/anatomy/examples/turning-dial/dial.css")
].find(existsSync);
if (!dialCssPath) throw new Error("ANATOMY_NATIVE_SOURCE_MISSING: turning-dial/dial.css is not present in the plugin package.");
var dialCss = readFileSync(dialCssPath, "utf8");
var nativePagePath = [
  resolve(nativeRoot, "../third_party/anatomy/examples/turning-dial/turning-dial-light.html"),
  resolve(nativeRoot, "../../third_party/anatomy/examples/turning-dial/turning-dial-light.html"),
  join(process.cwd(), "third_party/anatomy/examples/turning-dial/turning-dial-light.html")
].find(existsSync);
var nativePage = nativePagePath ? readFileSync(nativePagePath, "utf8") : "";
var stageStart = nativePage.indexOf('<div class="iso-stage');
var stageOpenEnd = stageStart >= 0 ? nativePage.indexOf(">", stageStart) : -1;
var stageClose = stageOpenEnd >= 0 ? nativePage.indexOf("</div></div><figcaption", stageOpenEnd) : -1;
var authoredStageMarkup = stageOpenEnd >= 0 && stageClose > stageOpenEnd ? nativePage.slice(stageOpenEnd + 1, stageClose) : "";
function compileNativeAnatomy(scene, width, height) {
  if (scene.nativeExample !== "turning-dial") throw new Error(`Unsupported native anatomy example: ${scene.nativeExample ?? "none"}`);
  const nativeParts = out.data.parts.map((part) => ({
    id: String(part.name),
    kind: "fixed",
    position: [0, 0, 0],
    visible: true
  }));
  const layers = out.data.layers.map((layer) => String(layer.name));
  const markup = authoredStageMarkup || layers.map((layer) => out.layerSvg(layer, { width: 640, height: 470 })).join("");
  return {
    data: out.data,
    markup,
    css: `${ISO_CSS}
${out.css}
${dialCss}
.iso .iso-svg{width:100%;height:auto;max-height:100%;margin:0 auto;}`,
    projection: out.data.P,
    bindings: out.data.parts.map((part, index) => ({ index, partId: String(part.name), removed: false })),
    parts: nativeParts,
    audits: {
      source: "pinned upstream anatomy native example",
      checks: { nativeExample: "turning-dial", parts: out.report.parts, groups: out.report.groups, layers: out.report.layers },
      motion: {}
    },
    nativeExample: "turning-dial",
    nativeFollow: "turning-dial",
    nativeDefaults: out.data.values
  };
}

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
  const out2 = new Float64Array(9);
  for (let r = 0; r < 3; r++) for (let c = 0; c < 3; c++) out2[r * 3 + c] = A[r * 3] * B[c] + A[r * 3 + 1] * B[3 + c] + A[r * 3 + 2] * B[6 + c];
  return out2;
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
function t3PreparePrism(run3, part) {
  const spec = part.spec;
  const n = spec.ring.length / 2;
  run3.n = n;
  run3.up = Boolean(spec.up);
  const ring = Float64Array.from(spec.ring);
  run3.ring = ring;
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
  run3.nx = nx;
  run3.ny = ny;
  const F = spec.up ? { o: [0, 0, 0], a: [0, 0, 1], u: [1, 0, 0], v: [0, 1, 0] } : spec.F;
  run3.F = F;
  run3.s0 = spec.up ? spec.z0 : spec.s0;
  run3.s1 = spec.up ? spec.z1 : spec.s1;
  const lo = new Float64Array(3 * n);
  const hi = new Float64Array(3 * n);
  const N3 = new Float64Array(3 * n);
  for (let i = 0; i < n; i++) {
    const x = ring[2 * i];
    const y = ring[2 * i + 1];
    for (let c = 0; c < 3; c++) {
      const base = F.o[c] + F.u[c] * x + F.v[c] * y;
      lo[3 * i + c] = base + F.a[c] * run3.s0;
      hi[3 * i + c] = base + F.a[c] * run3.s1;
      N3[3 * i + c] = F.u[c] * nx[i] + F.v[c] * ny[i];
    }
  }
  run3.lo = lo;
  run3.hi = hi;
  run3.N3 = N3;
  run3.sharp = new Uint8Array(n);
  for (let i = 0; i < n; i++) {
    const p = (i - 1 + n) % n;
    run3.sharp[i] = nx[p] * nx[i] + ny[p] * ny[i] < Math.cos(0.35) ? 1 : 0;
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
    run3.inset = inset;
  }
  run3.seams = part.details && part.details.seams ? part.details.seams.slice() : null;
  run3.cut = spec.cuts && spec.cuts.length ? spec.cuts : null;
}
function t3Axes(run3, part) {
  if (run3.kind === "ball") return run3.flats.map((flat) => flat.n);
  if (run3.kind === "tube") return run3.tips.slice();
  if (run3.kind === "prism") {
    const out2 = [run3.F.a];
    for (let i = 0; i < run3.n; i++) {
      const n = [run3.N3[3 * i], run3.N3[3 * i + 1], run3.N3[3 * i + 2]];
      if (out2.every((m) => Math.abs(m[0] * n[0] + m[1] * n[1] + m[2] * n[2]) < 0.9995)) out2.push(n);
    }
    return out2;
  }
  if (run3.F) return [run3.F.a];
  if (part.spec && part.spec.F) return [part.spec.F.a];
  return [];
}
function t3Cloud(run3, part) {
  const out2 = [];
  const ring = (F, s, r, count) => {
    for (let j = 0; j < count; j++) {
      const c = Math.cos(j / count * T3_TAU);
      const n = Math.sin(j / count * T3_TAU);
      out2.push(F.o[0] + F.a[0] * s + r * (c * F.u[0] + n * F.v[0]), F.o[1] + F.a[1] * s + r * (c * F.u[1] + n * F.v[1]), F.o[2] + F.a[2] * s + r * (c * F.u[2] + n * F.v[2]));
    }
  };
  if (run3.kind === "prism") {
    for (let i = 0; i < 3 * run3.n; i++) out2.push(run3.lo[i]);
    for (let i = 0; i < 3 * run3.n; i++) out2.push(run3.hi[i]);
  } else if (run3.kind === "round") {
    ring(run3.F, run3.s0, run3.r0, 24);
    ring(run3.F, run3.s1, run3.r1, 24);
    for (const [end, s, r] of [[0, run3.s0, run3.r0], [1, run3.s1, run3.r1]]) {
      if (run3.ends[end] !== "dome") continue;
      const sign = end ? 1 : -1;
      for (const b of [0.5, 1, 1.35]) ring(run3.F, s + sign * r * Math.sin(b), r * Math.cos(b), 6);
      out2.push(run3.F.o[0] + run3.F.a[0] * (s + sign * r), run3.F.o[1] + run3.F.a[1] * (s + sign * r), run3.F.o[2] + run3.F.a[2] * (s + sign * r));
    }
  } else if (run3.kind === "ball") {
    const golden = Math.PI * (3 - Math.sqrt(5));
    for (let i = 0; i < 64; i++) {
      const y = 1 - 2 * (i + 0.5) / 64;
      const rad = Math.sqrt(1 - y * y);
      const w = [Math.cos(golden * i) * rad, Math.sin(golden * i) * rad, y];
      const p = [run3.c[0] + run3.r * w[0], run3.c[1] + run3.r * w[1], run3.c[2] + run3.r * w[2]];
      let inside2 = true;
      for (const flat of run3.flats) if ((p[0] - run3.c[0]) * flat.n[0] + (p[1] - run3.c[1]) * flat.n[1] + (p[2] - run3.c[2]) * flat.n[2] > flat.d + 1e-9) inside2 = false;
      if (inside2) out2.push(p[0], p[1], p[2]);
    }
    for (const flat of run3.flats)
      for (let j = 0; j < 12; j++) {
        const c = Math.cos(j / 12 * T3_TAU) * flat.rho;
        const n = Math.sin(j / 12 * T3_TAU) * flat.rho;
        out2.push(run3.c[0] + flat.n[0] * flat.d + c * flat.u[0] + n * flat.v[0], run3.c[1] + flat.n[1] * flat.d + c * flat.u[1] + n * flat.v[1], run3.c[2] + flat.n[2] * flat.d + c * flat.u[2] + n * flat.v[2]);
      }
  } else if (run3.kind === "lathe") {
    const lv = run3.levels;
    const step = Math.max(4, Math.floor(lv.length / 4 / 8)) * 4;
    for (let i = 0; i < lv.length; i += step) ring(run3.F, lv[i], lv[i + 1], 8);
    ring(run3.F, lv[lv.length - 4], lv[lv.length - 3], 8);
  } else if (run3.kind === "tube") {
    const b = run3.body;
    const stride = Math.max(1, Math.floor(b.count / 8));
    for (let i = 0; i < b.count; i += stride) {
      const T = t3Unit([b.D3[3 * i], b.D3[3 * i + 1], b.D3[3 * i + 2]]);
      const [u, v] = t3Basis(T);
      ring({ o: [b.P3[3 * i], b.P3[3 * i + 1], b.P3[3 * i + 2]], a: T, u, v }, 0, run3.r, 8);
    }
  } else if (part.cloud) for (const v of part.cloud) out2.push(v);
  return Float64Array.from(out2);
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
  const out2 = new Float64Array(count * stride);
  for (let e = 0; e < count; e++) {
    let o = e * size;
    const at = e * stride;
    out2[at] = view.getUint16(o);
    out2[at + 1] = view.getUint16(o + 2);
    o += 4;
    if (grouped) {
      out2[at + 2] = view.getUint16(o) - 1;
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
    out2[at + stride - 3] = x / l;
    out2[at + stride - 2] = y / l;
    out2[at + stride - 1] = z / l;
  }
  return out2;
}
function t3Prepare(data, { unit = 1 } = {}) {
  const P = data.P;
  const runs = data.parts.map((part, index) => {
    const run3 = { index, name: part.name, kind: part.kind, group: part.group ?? -1, layer: part.layer, part, roles: t3Roles(part), planes: t3Planes(part.planes), dots: t3Dots(part.dots), unit };
    run3.role = Object.fromEntries(run3.roles.map((role, j) => [role.name, j]));
    if (part.kind === "prism") t3PreparePrism(run3, part);
    else if (part.kind === "round") t3PrepareRound(run3, part, P, unit);
    else if (part.kind === "ball") t3PrepareBall(run3, part, P, unit);
    else if (part.kind === "lathe") t3PrepareLathe(run3, part, P, unit);
    else if (part.kind === "tube") t3PrepareTube(run3, part, data);
    else if (part.kind === "fixed") {
      run3.anchor = part.spec.anchor;
      run3.home = part.spec.home;
      run3.box0 = part.spec.box;
      run3.hull0 = Float64Array.from(part.spec.hull);
      run3.F = part.spec.F ?? null;
      run3.ribs = part.details && part.details.ribs ? part.details.ribs : null;
    }
    run3.slots = part.spec.slots ?? {};
    run3.cloud = t3Cloud(run3, part);
    run3.axes = t3Axes(run3, part);
    const cn = run3.cloud.length / 3;
    run3.centroid = [0, 0, 0];
    for (let i = 0; i < cn; i++) for (let c = 0; c < 3; c++) run3.centroid[c] += run3.cloud[3 * i + c] / Math.max(1, cn);
    return run3;
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
function t3Frame(run3) {
  const count = run3.roles.length;
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
function t3Faded(f, run3, prefix, lines, count) {
  if (!f.fade) f.fade = {};
  const detail = t3State.detail;
  if (detail < 1) for (let i = 0; i < count; i++) lines.alpha[i] *= detail;
  if (detail < 0.01) count = 0;
  f.fade[prefix] = { key: lines.key.slice(0, count), alpha: lines.alpha.slice(0, count) };
  const slots = run3.slots[prefix === "v" ? "bevel" : "ribs"] ?? 6;
  const levels = run3._levels ?? (run3._levels = new Array(T3_LEVELS + 1));
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
    const role = run3.role[`${prefix}${j}`];
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
function t3EmitPrism(run3, cam, f) {
  const n = run3.n;
  const m = cam.m;
  const ox = cam.ox;
  const oy = cam.oy;
  const V = cam.V;
  const L = cam.L;
  const lo = run3.lo;
  const hi = run3.hi;
  const N3 = run3.N3;
  const bot = t3Scratch("a", 2 * n);
  const top = t3Scratch("b", 2 * n);
  for (let i = 0; i < n; i++) {
    const a = 3 * i;
    bot[2 * i] = ox + m[0] * lo[a] + m[1] * lo[a + 1] + m[2] * lo[a + 2];
    bot[2 * i + 1] = oy + m[3] * lo[a] + m[4] * lo[a + 1] + m[5] * lo[a + 2];
    top[2 * i] = ox + m[0] * hi[a] + m[1] * hi[a + 1] + m[2] * hi[a + 2];
    top[2 * i + 1] = oy + m[3] * hi[a] + m[4] * hi[a + 1] + m[5] * hi[a + 2];
  }
  const F = run3.F;
  const aV = F.a[0] * V[0] + F.a[1] * V[1] + F.a[2] * V[2];
  const near = aV >= 0 ? top : bot;
  const far = aV >= 0 ? bot : top;
  const facing = run3._facing ?? (run3._facing = new Float64Array(n));
  for (let i = 0; i < n; i++) facing[i] = N3[3 * i] * V[0] + N3[3 * i + 1] * V[1] + N3[3 * i + 2] * V[2];
  const on = (i) => facing[(i % n + n) % n] > 1e-9;
  let i0 = -1;
  for (let i = 0; i < n; i++)
    if (on(i) && !on(i - 1)) {
      i0 = i;
      break;
    }
  const sil = t3Scratch("c", 4 * n + 8);
  const silAt = run3._silAt ?? (run3._silAt = new Int32Array(2 * n + 4));
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
  f.d[run3.role.fill] = outline;
  if (run3.cut) {
    const inPlane = (index) => {
      const at = silAt[index];
      const set = at < 0 ? farSet : nearSet;
      const v = at < 0 ? -1 - at : at;
      return run3.cut.some((cut2) => Math.abs(cut2.n[0] * set[3 * v] + cut2.n[1] * set[3 * v + 1] + cut2.n[2] * set[3 * v + 2] - cut2.d) < 1e-3);
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
      return run3.cut.some((cut2) => Math.abs(cut2.n[0] * p[0] + cut2.n[1] * p[1] + cut2.n[2] * p[2] - cut2.d) < 1e-3 && Math.abs(cut2.n[0] * q[0] + cut2.n[1] * q[1] + cut2.n[2] * q[2] - cut2.d) < 1e-3);
    };
    for (let j = 0; j < count; j++) flags[j] = inPlane(j) && onSame(j, (j + 1) % count) ? 1 : 0;
    f.d[run3.role.edge] = t3Broken(sil, count, flags);
  } else f.d[run3.role.edge] = outline;
  t3Box(sil, count, f.box);
  t3SetHull(f, sil, count);
  const quad = new Float64Array(8);
  for (let i = 0; i < n; i++) {
    const role = run3.role[`f${i}`];
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
    if (run3.up) {
      score = (run3.nx[i] * cam.lx + run3.ny[i] * cam.ly + 1) / 2;
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
  if (run3.up) {
    const z = run3.s1;
    f.t[run3.role.top] = `matrix(${t3Fix(m[0], 1e5)} ${t3Fix(m[3], 1e5)} ${t3Fix(m[1], 1e5)} ${t3Fix(m[4], 1e5)} ${t3Fix(ox + m[2] * z, 100)} ${t3Fix(oy + m[5] * z, 100)})`;
  } else {
    for (let side = 0; side < 2; side++) {
      const role = run3.role[`f${n + side}`];
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
  if (run3.role.crease !== void 0) {
    let crease = "";
    if (run3.up) {
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
        if (run3.sharp[i] && facing[i] > 1e-6 && facing[p] > 1e-6) {
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
    f.d[run3.role.crease] = crease;
  }
  if (run3.inset && run3.role.v0 !== void 0 && t3State.detail < 0.01) f.levels = t3Faded(f, run3, "v", t3None, 0);
  else if (run3.inset && run3.role.v0 !== void 0) {
    const lines = t3Lines;
    lines.d.length = 0;
    lines.alpha.length = 0;
    lines.key.length = 0;
    lines.key.length = 0;
    const capSide = aV >= 0 ? 1 : 0;
    const s = capSide ? run3.s1 : run3.s0;
    const capAlpha = run3.up ? 1 : t3Step(0.02, 0.2, Math.abs(aV));
    const ins = t3Scratch("c", 2 * n);
    for (let i = 0; i < n; i++) {
      const x = run3.inset[2 * i];
      const y = run3.inset[2 * i + 1];
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
    f.levels = t3Faded(f, run3, "v", lines, lines.d.length);
  }
  if (run3.seams && run3.role.inner !== void 0) {
    let inner = "";
    if (i0 >= 0) {
      const rim = t3Scratch("c", 2 * n + 4);
      for (const s of run3.seams) {
        let c = 0;
        for (let j = i0; j <= i1; j++) {
          const i = j % n;
          const x = run3.ring[2 * i];
          const y = run3.ring[2 * i + 1];
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
    f.d[run3.role.inner] = inner;
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
  let out2 = "";
  let run3 = [];
  for (let step = 0; step < count; step++) {
    const j = (start + step) % count;
    if (skip[j]) {
      if (run3.length) {
        run3.push((j + 0) % count);
        out2 += t3PathOf(run3.map((i) => [buf[2 * i], buf[2 * i + 1]]), false);
        run3 = [];
      }
      continue;
    }
    run3.push(j);
  }
  if (run3.length) {
    run3.push((start + count) % count);
    out2 += t3PathOf(run3.map((i) => [buf[2 * i], buf[2 * i + 1]]), false);
  }
  return out2;
}
function t3EmitPlanes(run3, cam, f, sx = 0, sy = 0) {
  const m = cam.m;
  const V = cam.V;
  for (let j = 0; j < run3.planes.length; j++) {
    const plane = run3.planes[j];
    const role = run3.role[`plane${j}`];
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
function t3EmitDots(run3, cam, f, sx = 0, sy = 0) {
  const m = cam.m;
  const V = cam.V;
  for (let j = 0; j < run3.dots.length; j++) {
    const dot = run3.dots[j];
    const role = run3.role[`c${j}`];
    const p = dot.p;
    f.cx[role] = cam.ox - sx + m[0] * p[0] + m[1] * p[1] + m[2] * p[2];
    f.cy[role] = cam.oy - sy + m[3] * p[0] + m[4] * p[1] + m[5] * p[2];
    const alpha = (dot.n ? t3Step(dot.fade[0], dot.fade[1], dot.n[0] * V[0] + dot.n[1] * V[1] + dot.n[2] * V[2]) : 1) * t3State.detail;
    f.o[role] = alpha < 5e-3 ? 0 : Math.round(alpha * 100) / 100;
  }
}
function t3EmitFixed(run3, cam, f) {
  const a = run3.anchor;
  const m = cam.m;
  const X = cam.ox + m[0] * a[0] + m[1] * a[1] + m[2] * a[2];
  const Y = cam.oy + m[3] * a[0] + m[4] * a[1] + m[5] * a[2];
  const dx = X - run3.home[0];
  const dy = Y - run3.home[1];
  const rx = Math.round(dx * 100) / 100;
  const ry = Math.round(dy * 100) / 100;
  f.t[run3.role.move] = rx || ry ? `translate(${t3Num(rx)} ${t3Num(ry)})` : "";
  f.shiftX = rx;
  f.shiftY = ry;
  const b = run3.box0;
  f.box[0] = b[0] + rx;
  f.box[1] = b[1] + ry;
  f.box[2] = b[2] + rx;
  f.box[3] = b[3] + ry;
  const count = run3.hull0.length / 2;
  const hull = t3Grow(f, "hull", 2 * count, Float64Array);
  for (let i = 0; i < count; i++) {
    hull[2 * i] = run3.hull0[2 * i] + rx;
    hull[2 * i + 1] = run3.hull0[2 * i + 1] + ry;
  }
  f.hullN = count;
  if (run3.ribs && run3.F) t3EmitRibs(run3, cam, f, run3.F, run3.ribs, rx, ry);
  t3EmitPlanes(run3, cam, f, rx, ry);
  t3EmitDots(run3, cam, f, rx, ry);
}
function t3EmitRibs(run3, cam, f, F, ribs, sx, sy) {
  if (t3State.detail < 0.01) {
    f.levels = t3Faded(f, run3, "r", t3None, 0);
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
  const at = (s, r, t, out2, index) => {
    const c = Math.cos(t);
    const n = Math.sin(t);
    const px = F.o[0] + F.a[0] * s + r * (c * F.u[0] + n * F.v[0]);
    const py = F.o[1] + F.a[1] * s + r * (c * F.u[1] + n * F.v[1]);
    const pz = F.o[2] + F.a[2] * s + r * (c * F.u[2] + n * F.v[2]);
    out2[index] = cam.ox - sx + m[0] * px + m[1] * py + m[2] * pz;
    out2[index + 1] = cam.oy - sy + m[3] * px + m[4] * py + m[5] * pz;
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
  f.levels = t3Faded(f, run3, "r", lines, lines.d.length);
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
  const out2 = [];
  for (const arc of merged) if (arc.tone >= 0) out2.push(arc);
  return out2;
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
    const out2 = [];
    for (let j = 0; j < count; j++) {
      const cs = table[2 * j] * rad;
      const sn = table[2 * j + 1] * rad;
      const n = [W[0] * value + U[0] * cs + Q[0] * sn, W[1] * value + U[1] * cs + Q[1] * sn, W[2] * value + U[2] * cs + Q[2] * sn];
      if (keep(n)) out2.push(n);
    }
    return out2;
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
  let err2 = 0;
  for (let j = 0; j < most; j++) {
    const a = thin[j];
    const b = thin[(j + 1) % most];
    const dx = b[0] - a[0];
    const dy = b[1] - a[1];
    const l = Math.hypot(dx, dy) || 1;
    const end = j + 1 < most ? picks[j + 1] : picks[0] + n;
    for (let i = picks[j] + 1; i < end; i++) {
      const p = points[i % n];
      const out2 = ((p[0] - a[0]) * dy - (p[1] - a[1]) * dx) / l;
      if (Math.abs(out2) > err2) err2 = Math.abs(out2);
    }
  }
  return t3Grown(thin, err2);
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
function t3ArcPoints(geo, s, r, from, to, k, out2, cut2 = false) {
  const count = Math.max(2, Math.ceil(Math.abs(to - from) * 48 / T3_TAU), Math.ceil(Math.abs(to - from) * Math.max(r, 1e-6) * k / 1.5));
  for (let j = 0; j <= count; j++) {
    const t = from + (to - from) * j / count;
    const c = Math.cos(t);
    const n = Math.sin(t);
    const p = [geo.O[0] + s * geo.SA[0] + r * (c * geo.SU[0] + n * geo.SV[0]), geo.O[1] + s * geo.SA[1] + r * (c * geo.SU[1] + n * geo.SV[1])];
    if (cut2) p.cut = true;
    out2.push(p);
  }
}
function t3RoundOutline(run3, geo, cam) {
  const k = cam.k;
  const { s0, s1, r0, r1, ends } = run3;
  const domes = (ends[0] === "dome" ? 1 : 0) + (ends[1] === "dome" ? 1 : 0);
  if (domes === 2) {
    const c0 = [geo.O[0] + s0 * geo.SA[0], geo.O[1] + s0 * geo.SA[1]];
    const c1 = [geo.O[0] + s1 * geo.SA[0], geo.O[1] + s1 * geo.SA[1]];
    const rk = r0 * k;
    const dx = c1[0] - c0[0];
    const dy = c1[1] - c0[1];
    const l = Math.hypot(dx, dy);
    const count = Math.max(24, Math.ceil(Math.PI * rk / 1.5));
    const out3 = [];
    if (l < 1e-6) {
      for (let j = 0; j < 2 * count; j++) {
        const t = j / (2 * count) * T3_TAU;
        out3.push([c1[0] + rk * Math.cos(t), c1[1] + rk * Math.sin(t)]);
      }
      return out3;
    }
    const beta = Math.atan2(dy, dx);
    for (let j = 0; j <= count; j++) {
      const t = beta - Math.PI / 2 + Math.PI * j / count;
      out3.push([c1[0] + rk * Math.cos(t), c1[1] + rk * Math.sin(t)]);
    }
    for (let j = 0; j <= count; j++) {
      const t = beta + Math.PI / 2 + Math.PI * j / count;
      out3.push([c0[0] + rk * Math.cos(t), c0[1] + rk * Math.sin(t)]);
    }
    return out3;
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
  const out2 = [];
  let c;
  if (view.flat < 1e-9) c = run3.na * view.a > 0 ? -2 : 2;
  else c = -(run3.na * view.a) / (run3.nr * view.flat);
  if (c <= -1 || c >= 1) {
    const side = c <= -1;
    const capFirst = -geo.aV > 0;
    const keepFirst = side ? !capFirst : capFirst;
    const s = keepFirst ? s0 : s1;
    const r = keepFirst ? r0 : r1;
    t3ArcPoints(geo, s, r, 0, T3_TAU, k, out2, run3.cutS !== null && Math.abs(run3.cutS - s) < 1e-6);
    out2.pop();
    return out2;
  }
  const d = Math.acos(c);
  const lo = view.phi - d;
  const hi = view.phi + d;
  const cut0 = run3.cutS !== null && Math.abs(run3.cutS - s0) < 1e-6;
  const cut1 = run3.cutS !== null && Math.abs(run3.cutS - s1) < 1e-6;
  if (-geo.aV > 0) t3ArcPoints(geo, s0, r0, hi, lo + T3_TAU, k, out2, cut0);
  else t3ArcPoints(geo, s0, r0, lo, hi, k, out2, cut0);
  const tail = [];
  if (geo.aV > 0) t3ArcPoints(geo, s1, r1, hi, lo + T3_TAU, k, tail, cut1);
  else t3ArcPoints(geo, s1, r1, lo, hi, k, tail, cut1);
  const first = out2[out2.length - 1];
  const a = tail[0];
  const b = tail[tail.length - 1];
  if (Math.hypot(a[0] - first[0], a[1] - first[1]) > Math.hypot(b[0] - first[0], b[1] - first[1])) tail.reverse();
  for (const p of tail) out2.push(p);
  return out2;
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
function t3LatheOutline(run3, geo, cam) {
  const k = cam.k;
  const view = geo.view;
  const lv = run3.levels;
  const pts = [];
  const cut2 = (L) => view.flat < 1e-9 ? Infinity : -(L.na * view.a) / (L.nr * view.flat);
  const inside2 = (L) => L.r <= 1e-9 || Math.abs(cut2(L)) < 1;
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
    if (inside2(L)) pts.push(...sides(L));
    if (previous) {
      const pin = inside2(previous);
      const lin = inside2(L);
      if (pin && lin) refine(previous, L, 0);
      else if (pin !== lin) {
        let a = pin ? previous : L;
        let b = pin ? L : previous;
        const start = a;
        for (let it = 0; it < 14; it++) {
          const mid = t3LatheMid(a.s < b.s ? a : b, a.s < b.s ? b : a);
          if (inside2(mid)) a = mid;
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
function t3PrepareRound(run3, part, P, unit) {
  const spec = part.spec;
  const k = P.scale * T3_ROOT;
  run3.F = spec.F;
  run3.s0 = spec.s0;
  run3.s1 = spec.s1;
  run3.r0 = spec.r0;
  run3.r1 = spec.r1;
  run3.ends = spec.ends;
  const g = (spec.r1 - spec.r0) / (spec.s1 - spec.s0 || 1);
  const norm = Math.hypot(1, g);
  run3.nr = 1 / norm;
  run3.na = -g / norm;
  run3.g = g;
  const rmax = Math.max(spec.r0, spec.r1);
  const around = T3_TAU * rmax * k * unit;
  run3.fine = Math.max(around < 30 ? 16 : 24, Math.min(96, Math.ceil(around / 2.2)));
  run3.dirs = Math.max(around < 30 ? 16 : 32, Math.min(256, Math.ceil(around / 1.5)));
  run3.capCount = Math.max(around < 30 ? 16 : 24, Math.min(160, Math.ceil(around / 1.5)));
  run3.domeCount = Math.max(around < 30 ? 12 : 16, Math.min(48, Math.round(run3.fine * 0.75)));
  const comps = [];
  for (const [end, s, r] of [[0, spec.s0, spec.r0], [1, spec.s1, spec.r1]]) comps.push(spec.ends[end] === "dome" ? 1 : 0, s, r);
  run3.components = comps;
  const details = part.details ?? {};
  run3.seams = (details.seams ?? []).map((s) => ({ s, r: spec.r0 + g * (s - spec.s0), slope: g }));
  run3.ribs = details.ribs ? { ...details.ribs, r0: details.ribs.r0 ?? spec.r0 + g * (details.ribs.s0 - spec.s0), r1: details.ribs.r1 ?? spec.r0 + g * (details.ribs.s1 - spec.s0) } : null;
  run3.cutS = null;
  for (const cut2 of spec.cuts ?? []) {
    const along = cut2.n[0] * spec.F.a[0] + cut2.n[1] * spec.F.a[1] + cut2.n[2] * spec.F.a[2];
    const sCut = (cut2.d - (cut2.n[0] * spec.F.o[0] + cut2.n[1] * spec.F.o[1] + cut2.n[2] * spec.F.o[2])) / along;
    if (Math.abs(sCut - spec.s0) < 1e-6 || Math.abs(sCut - spec.s1) < 1e-6) run3.cutS = sCut;
  }
}
function t3EmitRound(run3, cam, f) {
  const geo = t3Geo(run3.F, cam);
  const k = cam.k;
  const step = T3_TAU / run3.fine;
  const sheets = ["", "", "", "", ""];
  const { s0, s1, r0, r1 } = run3;
  for (const arc of t3Arcs(run3.nr, run3.na, geo.view, geo.light)) sheets[arc.tone] += t3Strip(geo, s0, r0, s1, r1, arc.from, arc.to, step);
  const F = run3.F;
  for (let end = 0; end < 2; end++) {
    if (run3.ends[end] !== "dome") continue;
    const s = end ? s1 : s0;
    const sign = end ? 1 : -1;
    const C = [F.o[0] + F.a[0] * s, F.o[1] + F.a[1] * s, F.o[2] + F.a[2] * s];
    t3Dome(cam, C, [F.a[0] * sign, F.a[1] * sign, F.a[2] * sign], end ? r1 : r0, run3.domeCount, sheets);
  }
  for (let t = 0; t < 5; t++) f.d[run3.role[`s${t}`]] = sheets[t];
  const pts = t3RoundOutline(run3, geo, cam);
  const outline = t3PathOf(pts, true);
  f.d[run3.role.fill] = outline;
  if (run3.cutS !== null) {
    const buf = new Float64Array(2 * pts.length);
    const skip = new Uint8Array(pts.length);
    pts.forEach((p, j) => {
      buf[2 * j] = p[0];
      buf[2 * j + 1] = p[1];
    });
    for (let j = 0; j < pts.length; j++) skip[j] = pts[j].cut && pts[(j + 1) % pts.length].cut ? 1 : 0;
    f.d[run3.role.edge] = t3Broken(buf, pts.length, skip);
  } else f.d[run3.role.edge] = outline;
  t3BoxOf(pts, f.box);
  t3HullOut(f, pts);
  const view = geo.view;
  let crease = "";
  for (let end = 0; end < 2; end++) {
    if (run3.ends[end] !== "flat") continue;
    const role = run3.role[`k${end}`];
    const sign = end ? 1 : -1;
    const s = end ? s1 : s0;
    const r = end ? r1 : r0;
    const face = sign * geo.aV;
    if (!(face > 1e-9)) {
      f.d[role] = "";
      continue;
    }
    const n = run3.capCount;
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
    if (run3.role.crease === void 0) continue;
    let lo;
    let hi;
    if (view.flat < 1e-9) {
      if (!(run3.na * view.a > 1e-9)) continue;
      lo = 0;
      hi = T3_TAU;
    } else {
      const cc = -(run3.na * view.a) / (run3.nr * view.flat);
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
  if (run3.role.crease !== void 0) f.d[run3.role.crease] = crease;
  if (run3.role.inner !== void 0) {
    let inner = "";
    for (const seam of run3.seams) inner += t3SeamArc(geo, seam.s, seam.r, seam.slope, k);
    if (run3.ribs && run3.ribs.seams) {
      const rs = run3.ribs;
      const slope = (rs.r1 - rs.r0) / (rs.s1 - rs.s0 || 1);
      if (rs.seams !== "last") inner += t3SeamArc(geo, rs.s0, rs.r0, slope, k);
      if (rs.seams !== "first") inner += t3SeamArc(geo, rs.s1, rs.r1, slope, k);
    }
    f.d[run3.role.inner] = inner;
  }
  if (run3.ribs) {
    const lines = t3State.detail < 0.01 ? t3None : t3RibLines(geo, run3.F, cam, run3.ribs, 0, 0);
    f.levels = t3Faded(f, run3, "r", lines, lines.d.length);
  }
}
function t3PrepareBall(run3, part, P, unit) {
  const spec = part.spec;
  const k = P.scale * T3_ROOT;
  run3.c = spec.c;
  run3.r = spec.r;
  run3.flats = spec.flats.map((flat) => {
    const n = t3Unit(flat.n);
    const rho = Math.sqrt(Math.max(0, spec.r * spec.r - flat.d * flat.d));
    const [u, v] = t3Basis(n);
    return { n, d: flat.d, rho, u, v };
  });
  run3.limb = Math.max(32, Math.min(160, Math.ceil(T3_TAU * spec.r * k * unit / 1.5)));
  run3.rimCount = run3.flats.map((flat) => Math.max(20, Math.min(120, Math.ceil(T3_TAU * flat.rho * k * unit / 1.5))));
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
  let out2 = subject;
  for (let i = 0; i < clip.length && out2.length; i++) {
    const a = clip[i];
    const b = clip[(i + 1) % clip.length];
    const side = (p) => sign * ((b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0]));
    const input = out2;
    out2 = [];
    for (let j = 0; j < input.length; j++) {
      const p = input[j];
      const q = input[(j + 1) % input.length];
      const sp = side(p);
      const sq = side(q);
      if (sp >= 0) out2.push(p);
      if (sp >= 0 !== sq >= 0) {
        const t = sp / (sp - sq);
        out2.push([p[0] + (q[0] - p[0]) * t, p[1] + (q[1] - p[1]) * t]);
      }
    }
  }
  return out2;
}
function t3EmitBall(run3, cam, f) {
  const m = cam.m;
  const V = cam.V;
  const L = cam.L;
  const { c, r, flats } = run3;
  const Cx = cam.ox + m[0] * c[0] + m[1] * c[1] + m[2] * c[2];
  const Cy = cam.oy + m[3] * c[0] + m[4] * c[1] + m[5] * c[2];
  const dot = (a, b) => a[0] * b[0] + a[1] * b[1] + a[2] * b[2];
  const flat = (w) => [Cx + r * (m[0] * w[0] + m[1] * w[1] + m[2] * w[2]), Cy + r * (m[3] * w[0] + m[4] * w[1] + m[5] * w[2])];
  const inside2 = (w, skip = -1) => {
    for (let i = 0; i < flats.length; i++) if (i !== skip && dot(w, flats[i].n) * r > flats[i].d + 1e-7) return false;
    return true;
  };
  const [U, W] = t3Basis(V);
  const n = run3.limb;
  const table = t3Table(n);
  const limb = [];
  for (let j = 0; j < n; j++) limb.push([U[0] * table[2 * j] + W[0] * table[2 * j + 1], U[1] * table[2 * j] + W[1] * table[2 * j + 1], U[2] * table[2 * j] + W[2] * table[2 * j + 1]]);
  const sil = [];
  for (const w of limb) if (inside2(w)) sil.push(flat(w));
  const rims = flats.map((cut2, ci) => {
    const count = run3.rimCount[ci];
    const t = t3Table(count);
    const list = [];
    for (let j = 0; j < count; j++) {
      const w = [(cut2.n[0] * cut2.d + cut2.rho * (cut2.u[0] * t[2 * j] + cut2.v[0] * t[2 * j + 1])) / r, (cut2.n[1] * cut2.d + cut2.rho * (cut2.u[1] * t[2 * j] + cut2.v[1] * t[2 * j + 1])) / r, (cut2.n[2] * cut2.d + cut2.rho * (cut2.u[2] * t[2 * j] + cut2.v[2] * t[2 * j + 1])) / r];
      list.push({ w, keep: inside2(w, ci), p: flat(w) });
    }
    return list;
  });
  flats.forEach((cut2, ci) => {
    for (const w of t3Meet(V, 0, cut2.n, cut2.d / r)) if (inside2(w, ci)) sil.push(flat(w));
    rims[ci].forEach(({ keep, p }) => keep && sil.push(p));
  });
  const hull = t3Hull(sil);
  const outline = t3PathOf(hull, true);
  f.d[run3.role.fill] = outline;
  f.d[run3.role.edge] = outline;
  f.d[run3.role.s0] = outline;
  const capOf = (threshold) => {
    const points = [];
    for (const w of limb) if (dot(w, L) >= threshold && inside2(w)) points.push(flat(w));
    const radius = Math.sqrt(Math.max(0, 1 - threshold * threshold));
    const [LU, LW] = t3Basis(L);
    for (let j = 0; j < n; j++) {
      const w = [L[0] * threshold + radius * (LU[0] * table[2 * j] + LW[0] * table[2 * j + 1]), L[1] * threshold + radius * (LU[1] * table[2 * j] + LW[1] * table[2 * j + 1]), L[2] * threshold + radius * (LU[2] * table[2 * j] + LW[2] * table[2 * j + 1])];
      if (dot(w, V) >= -1e-9) points.push(flat(w));
    }
    if (dot(L, V) > threshold) points.push(flat(V));
    for (const w of t3Meet(L, threshold, V, 0)) if (inside2(w)) points.push(flat(w));
    flats.forEach((cut2, ci) => {
      for (const w of t3Meet(V, 0, cut2.n, cut2.d / r)) if (inside2(w, ci) && dot(w, L) >= threshold) points.push(flat(w));
      for (const w of t3Meet(L, threshold, cut2.n, cut2.d / r)) if (inside2(w, ci) && dot(w, V) >= -1e-9) points.push(flat(w));
      for (const { w, keep, p } of rims[ci]) if (keep && dot(w, L) >= threshold && dot(w, V) >= -1e-9) points.push(p);
    });
    if (points.length < 3) return "";
    const region = t3ClipConvex(t3Hull(points), hull);
    return region.length >= 3 ? t3PathOf(region, true) : "";
  };
  f.d[run3.role.s1] = capOf(T3_LB[1]);
  f.d[run3.role.s2] = capOf(T3_LB[2]);
  f.d[run3.role.s3] = capOf(T3_LB[3]);
  let crease = "";
  flats.forEach((cut2, ci) => {
    const role = run3.role[`f${ci}`];
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
      if (seen[i]) (cur ??= []).push(list[i].p);
      else if (cur) {
        if (cur.length > 1) crease += t3PathOf(cur, false);
        cur = null;
      }
    }
    if (cur && cur.length > 1) crease += t3PathOf(cur, false);
  });
  if (run3.role.crease !== void 0) f.d[run3.role.crease] = crease;
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
function t3PrepareLathe(run3, part, P, unit) {
  const spec = part.spec;
  const k = P.scale * T3_ROOT;
  run3.F = spec.F;
  run3.levels = spec.levels;
  run3.caps = spec.caps;
  let rmax = 0;
  for (let i = 0; i < spec.levels.length; i += 4) rmax = Math.max(rmax, spec.levels[i + 1]);
  run3.fine = Math.max(24, Math.min(96, Math.ceil(T3_TAU * rmax * k * unit / 2.2)));
  run3.dirs = Math.max(32, Math.min(256, Math.ceil(T3_TAU * rmax * k * unit / 1.5)));
  run3.capCount = Math.max(24, Math.min(160, Math.ceil(T3_TAU * rmax * k * unit / 1.5)));
  const comps = [];
  for (let i = 0; i < spec.levels.length; i += 4) comps.push(0, spec.levels[i], spec.levels[i + 1]);
  run3.components = comps;
  const details = part.details ?? {};
  run3.seams = (details.seams ?? []).map((seam) => typeof seam === "number" ? t3LatheSeam(spec.levels, seam) : seam);
  run3.ribs = details.ribs ?? null;
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
    const out2 = new Array(count + 1);
    for (let index = 0; index <= count; index++) out2[index] = at(L, from + (to - from) * index / count);
    return out2;
  };
  const oriented2 = (points) => {
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
    const out2 = { ...arc };
    const centre = (reference.from + reference.to) / 2;
    while ((out2.from + out2.to) / 2 - centre > Math.PI) {
      out2.from -= T3_TAU;
      out2.to -= T3_TAU;
    }
    while (centre - (out2.from + out2.to) / 2 > Math.PI) {
      out2.from += T3_TAU;
      out2.to += T3_TAU;
    }
    return out2;
  };
  const overlap2 = (x, y) => Math.min(x.to, y.to) - Math.max(x.from, y.from);
  const sheet = (tone, run3) => {
    const chains2 = run3[0].groups[tone].map((arc) => [arc]);
    for (let q = 1; q < run3.length; q++) {
      const next = run3[q].groups[tone];
      const used = new Uint8Array(next.length);
      for (const chain of chains2) {
        const prev = chain[q - 1];
        let best = -1;
        let score = -Infinity;
        for (let j = 0; j < next.length; j++) {
          if (used[j]) continue;
          const value = overlap2(prev, align(prev, next[j]));
          if (value > score) {
            score = value;
            best = j;
          }
        }
        used[best] = 1;
        chain.push(align(prev, next[best]));
      }
    }
    chains2.forEach((chain) => {
      const last = run3.length - 1;
      const points = arcPoints(run3[0], chain[0].from, chain[0].to);
      for (let q = 1; q < last; q++) points.push(at(run3[q], chain[q].to));
      points.push(...arcPoints(run3[last], chain[last].from, chain[last].to).reverse());
      for (let q = last - 1; q >= 1; q--) points.push(at(run3[q], chain[q].from));
      buckets[tone] += t3PathOf(oriented2(points), true);
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
      buckets[tone] += t3PathOf(oriented2(points), true);
    };
    const links = below.map(() => []);
    const back2 = above.map(() => []);
    below.forEach(
      (lo, i) => above.forEach((hi, j) => {
        if (overlap2(lo, align(lo, hi)) > -0.05) {
          links[i].push(j);
          back2[j].push(i);
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
      if (back2[j].length < 2 || back2[j].some((i) => links[i].length !== 1)) continue;
      share(above[j], back2[j].map((i) => below[i]), false);
      doneHi[j] = 1;
      for (const i of back2[j]) doneLo[i] = 1;
    }
    for (let i = 0; i < below.length; i++) {
      if (doneLo[i] || links[i].length < 2 || links[i].some((j) => back2[j].length !== 1)) continue;
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
        const value = overlap2(lo, align(lo, above[j]));
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
function t3EmitLathe(run3, cam, f) {
  const geo = t3Geo(run3.F, cam);
  const k = cam.k;
  const step = T3_TAU / run3.fine;
  const sheets = ["", "", "", "", ""];
  const lv = run3.levels;
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
  for (let t = 0; t < 5; t++) f.d[run3.role[`s${t}`]] = sheets[t];
  const pts = t3LatheOutline(run3, geo, cam);
  const outline = t3PathOf(pts, true);
  f.d[run3.role.fill] = outline;
  f.d[run3.role.edge] = outline;
  t3BoxOf(pts, f.box);
  t3HullOut(f, pts);
  let crease = "";
  const view = geo.view;
  const ends = [[0, lv[0], lv[1], -1, 4], [1, lv[lv.length - 4], lv[lv.length - 3], 1, lv.length - 8]];
  for (const [end, s, r, sign, near] of ends) {
    const role = run3.role[`k${end}`];
    if (role === void 0) continue;
    const face = sign * geo.aV;
    if (!(face > 1e-9) || r <= 1e-9) {
      f.d[role] = "";
      continue;
    }
    const n = run3.capCount;
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
    if (run3.role.crease === void 0) continue;
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
  if (run3.role.crease !== void 0) f.d[run3.role.crease] = crease;
  if (run3.role.inner !== void 0) {
    let inner = "";
    for (const seam of run3.seams) inner += t3SeamArc(geo, seam.s, seam.r, seam.slope, k);
    f.d[run3.role.inner] = inner;
  }
  if (run3.ribs) {
    const lines = t3State.detail < 0.01 ? t3None : t3RibLines(geo, run3.F, cam, run3.ribs, 0, 0);
    f.levels = t3Faded(f, run3, "r", lines, lines.d.length);
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
  const out2 = [];
  for (let i = 1; i < n; i++) {
    const start = along[i - 1];
    const end = along[i];
    if (end >= from && start <= to) {
      const length = end - start || 1;
      const t0 = Math.max(0, (from - start) / length);
      const t1 = Math.min(1, (to - start) / length);
      const at = (t) => [flat[3 * i - 3] + (flat[3 * i] - flat[3 * i - 3]) * t, flat[3 * i - 2] + (flat[3 * i + 1] - flat[3 * i - 2]) * t, flat[3 * i - 1] + (flat[3 * i + 2] - flat[3 * i - 1]) * t];
      if (!out2.length) out2.push(at(t0));
      out2.push(at(t1));
    }
  }
  return out2;
}
function t3TangentAlong(route, at) {
  const a = t3PointAlong(route, Math.max(0, at - 0.6));
  const b = t3PointAlong(route, Math.min(route.total, at + 0.6));
  return t3Unit([b[0] - a[0], b[1] - a[1], b[2] - a[2]]);
}
var t3RouteCache = /* @__PURE__ */ new WeakMap();
function t3PrepareTube(run3, part, data) {
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
  run3.r = r;
  run3.wide = Boolean(source.wide);
  run3.hue = source.hue ?? null;
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
  run3.body = partOf(openStart ? spec.from - lead : spec.from, openEnd ? spec.to + lead : spec.to);
  run3.stripe = openStart || openEnd ? partOf(openStart ? spec.from - 2 * lead : spec.from, openEnd ? spec.to + 2 * lead : spec.to) : run3.body;
  const ends = [!spec.open0 && (spec.from <= 1e-6 || spec.gap0), !spec.open1 && (spec.to >= total - 1e-6 || spec.gap1)];
  run3.capped = [ends[0] && (spec.gap0 || spec.caps[0]), ends[1] && (spec.gap1 || spec.caps[1])];
  const P3 = run3.body.P3;
  const last = run3.body.count - 1;
  const vec = (i, j) => t3Unit([P3[3 * i] - P3[3 * j], P3[3 * i + 1] - P3[3 * j + 1], P3[3 * i + 2] - P3[3 * j + 2]]);
  run3.tips = [vec(1, 0), vec(last, last - 1)];
  run3.rings = null;
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
    run3.rings = { segments, fade, tone: source.rings.tone ?? "lo" };
  }
}
function t3Sides(part, cam, r) {
  const m = cam.m;
  const k = cam.k;
  const n = part.count;
  const out2 = { n, flat: new Float64Array(2 * n), left: new Float64Array(2 * n), right: new Float64Array(2 * n), shineA: new Float64Array(2 * n), shineB: new Float64Array(2 * n), shadeA: new Float64Array(2 * n), shadeB: new Float64Array(2 * n), frames: [] };
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
    out2.flat[2 * i] = px;
    out2.flat[2 * i + 1] = py;
    out2.frames.push({ p: [px, py], nx, ny, half });
    out2.left[2 * i] = px + nx * half;
    out2.left[2 * i + 1] = py + ny * half;
    out2.right[2 * i] = px - nx * half;
    out2.right[2 * i + 1] = py - ny * half;
    const toward = nx * T3_SHINE[0] + ny * T3_SHINE[1];
    const shineAt = half * 0.44 * toward;
    const shineHalf = half * 0.24;
    out2.shineA[2 * i] = px + nx * (shineAt + shineHalf);
    out2.shineA[2 * i + 1] = py + ny * (shineAt + shineHalf);
    out2.shineB[2 * i] = px + nx * (shineAt - shineHalf);
    out2.shineB[2 * i + 1] = py + ny * (shineAt - shineHalf);
    const shadeAt = -half * 0.62 * toward;
    const shadeHalf = half * 0.2;
    out2.shadeA[2 * i] = px + nx * (shadeAt + shadeHalf);
    out2.shadeA[2 * i + 1] = py + ny * (shadeAt + shadeHalf);
    out2.shadeB[2 * i] = px + nx * (shadeAt - shadeHalf);
    out2.shadeB[2 * i + 1] = py + ny * (shadeAt - shadeHalf);
  }
  return out2;
}
var t3Pts = (buf, n) => {
  const out2 = new Array(n);
  for (let i = 0; i < n; i++) out2[i] = [buf[2 * i], buf[2 * i + 1]];
  return out2;
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
  const probe2 = proj([centre[0] + n2[0], centre[1] + n2[1], centre[2] + n2[2]]);
  const along = (probe2[0] - C[0]) * inward[0] + (probe2[1] - C[1]) * inward[1];
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
function t3EmitTube(run3, cam, f) {
  const r = run3.r;
  const sides = t3Sides(run3.body, cam, r);
  const bands = run3.stripe === run3.body ? sides : t3Sides(run3.stripe, cam, r);
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
  let body2 = t3PathOf(loop, true);
  let edges = t3PathOf(left, false) + t3PathOf(right, false);
  const tips = [null, null];
  const last = n - 1;
  const quads = [];
  for (let i = 0; i < last; i++) quads.push([left[i], left[i + 1], right[i + 1], right[i]]);
  for (const side of [0, 1]) {
    if (!run3.capped[side]) continue;
    const at = side ? last : 0;
    const other = side ? last - 1 : 1;
    const tangent = run3.tips[side];
    const outward = side ? tangent : [-tangent[0], -tangent[1], -tangent[2]];
    const inward = [sides.flat[2 * other] - sides.flat[2 * at], sides.flat[2 * other + 1] - sides.flat[2 * at + 1]];
    const centre = [run3.body.P3[3 * at], run3.body.P3[3 * at + 1], run3.body.P3[3 * at + 2]];
    const { ring, arc, inner } = t3TubeCap(cam, centre, tangent, r, inward);
    let ringArea = 0;
    for (let i = 0; i < ring.length; i++) {
      const a = ring[i];
      const b = ring[(i + 1) % ring.length];
      ringArea += a[0] * b[1] - b[0] * a[1];
    }
    body2 += t3PathOf(Math.sign(ringArea) === sign ? ring : ring.slice().reverse(), true);
    edges += t3PathOf(arc, false);
    const V = cam.V;
    const open = outward[0] * V[0] + outward[1] * V[1] + outward[2] * V[2] > 0;
    if (open) edges += t3PathOf(inner, false);
    tips[side] = { half: open ? inner : arc, frame: sides.frames[at] };
    quads.push(ring);
  }
  f.d[run3.role.body] = body2;
  f.d[run3.role.edges] = edges;
  if (run3.wide) {
    const toward = (frame) => frame.nx * T3_SHINE[0] + frame.ny * T3_SHINE[1];
    const shineOffsets = (frame) => [frame.half * 0.44 * toward(frame) + frame.half * 0.24, frame.half * 0.44 * toward(frame) - frame.half * 0.24];
    const shadeOffsets = (frame) => [-frame.half * 0.62 * toward(frame) + frame.half * 0.2, -frame.half * 0.62 * toward(frame) - frame.half * 0.2];
    const bn = bands.n;
    const band = (A, B, offsets) => {
      const head = tips[1] ? t3StripeEnd(tips[1].half, tips[1].frame.p, tips[1].frame.nx, tips[1].frame.ny, offsets(tips[1].frame)[0], offsets(tips[1].frame)[1]) : [];
      const tail = tips[0] ? t3StripeEnd(tips[0].half, tips[0].frame.p, tips[0].frame.nx, tips[0].frame.ny, offsets(tips[0].frame)[1], offsets(tips[0].frame)[0]) : [];
      return t3PathOf([...t3Pts(A, bn), ...head, ...t3Pts(B, bn).reverse(), ...tail], true);
    };
    f.d[run3.role.shine] = band(bands.shineA, bands.shineB, shineOffsets);
    f.d[run3.role.shade] = band(bands.shadeA, bands.shadeB, shadeOffsets);
  }
  if (run3.rings) {
    const lines = t3Lines;
    lines.d.length = 0;
    lines.alpha.length = 0;
    lines.key.length = 0;
    lines.key.length = 0;
    const V = cam.V;
    const m = cam.m;
    const seg = new Float64Array(4);
    const surface = (sample, out2, index2) => {
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
      out2[index2] = cam.ox + m[0] * p[0] + m[1] * p[1] + m[2] * p[2];
      out2[index2 + 1] = cam.oy + m[3] * p[0] + m[4] * p[1] + m[5] * p[2];
      return normal[0] * V[0] + normal[1] * V[1] + normal[2] * V[2];
    };
    const fade = run3.rings.fade;
    let index = -1;
    for (const [a, b] of run3.rings.segments) {
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
    f.levels = t3Faded(f, run3, "r", lines, lines.d.length);
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
function t3Emit(run3, cam, out2) {
  const f = out2 ?? t3Frame(run3);
  if (run3.kind === "prism") t3EmitPrism(run3, cam, f);
  else if (run3.kind === "round") t3EmitRound(run3, cam, f);
  else if (run3.kind === "ball") t3EmitBall(run3, cam, f);
  else if (run3.kind === "lathe") t3EmitLathe(run3, cam, f);
  else if (run3.kind === "tube") {
    t3EmitTube(run3, cam, f);
    return f;
  } else if (run3.kind === "fixed") {
    t3EmitFixed(run3, cam, f);
    return f;
  }
  t3EmitPlanes(run3, cam, f);
  t3EmitDots(run3, cam, f);
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
function t3Order(layer, frames2, cams, previous, stats, scene) {
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
  const addEdge = (back2, front) => {
    to[edges] = front;
    next[edges] = head[back2];
    live[edges] = 1;
    head[back2] = edges;
    indeg[front]++;
    edges++;
  };
  const runs = scene ? scene.runs : null;
  const groupOf = (global) => runs ? runs[global].group : -1;
  const planar = layer.planar;
  for (let p = 0; p < planar.length; p += 5) {
    const i = planar[p];
    const j = planar[p + 1];
    const fi = frames2[i];
    const fj = frames2[j];
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
      if (!t3Overlap(frames2[i].box, frames2[j].box, -0.05)) continue;
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
          const b = frames2[list[q]].box;
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
        const bi = frames2[i].box;
        if (!t3Overlap(bi, gp.boxB, -0.05)) continue;
        for (let y = 0; y < gp.b.length; y++) {
          const j = gp.b[y];
          if (!t3Overlap(bi, frames2[j].box, -0.05)) continue;
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
    if (!t3Overlap(frames2[i].box, frames2[j].box, -0.05)) continue;
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
      const bi = frames2[i].box;
      for (let b = 0; b < count; b++) {
        const j = parts[b];
        if (j === i || runs[j].group === gi) continue;
        if (isLoose[b] && j < i) continue;
        if (!t3Overlap(bi, frames2[j].box, -0.05)) continue;
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
  const out2 = new Int32Array(count);
  let placed2 = 0;
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
              if (t3Disjoint(frames2[parts[a]], frames2[parts[b]], 0.1)) {
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
  while (placed2 < count) {
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
      let pick2 = -1;
      for (let v2 = 0; v2 < count; v2++) if (!done[v2] && (pick2 < 0 || indeg[v2] < indeg[pick2] || indeg[v2] === indeg[pick2] && rank[v2] < rank[pick2])) pick2 = v2;
      forced++;
      indeg[pick2] = 0;
      push(pick2);
    }
    const v = pop();
    if (done[v]) continue;
    done[v] = 1;
    out2[placed2++] = parts[v];
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
  return out2;
}
function t3Keep(values) {
  const n = values.length;
  const tails = [];
  const tailAt = [];
  const back2 = new Int32Array(n).fill(-1);
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
    back2[i] = lo > 0 ? tailAt[lo - 1] : -1;
  }
  const keep = new Uint8Array(n);
  let k = tails.length ? tailAt[tails.length - 1] : -1;
  while (k >= 0) {
    keep[k] = 1;
    k = back2[k];
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
  for (const run3 of scene.runs) {
    const layer = data.layers[run3.layer];
    const container = containers.get(layer.name);
    const node = container ? container.querySelector(`[data-p="${run3.index}"]`) : null;
    nodes[run3.index] = node;
    const map = {};
    if (node) {
      map.move = node;
      node.querySelectorAll("[data-r]").forEach((el) => map[el.getAttribute("data-r")] = el);
    }
    bound[run3.index] = run3.roles.map((role) => map[role.name] ?? null);
    cache[run3.index] = run3.roles.map(() => ({ d: null, q: null, b: null, f: null, w: null, t: null, o: null, cx: null, cy: null }));
  }
  const frames2 = scene.runs.map((run3) => t3Frame(run3));
  const values = Object.fromEntries(data.groups.map((g) => [g.name, data.values ? data.values[g.name] ?? 0 : 0]));
  let lastPoses = null;
  let cams = null;
  const orders = scene.layers.map((layer) => Int32Array.from(layer.rest));
  const changes = [];
  const stats = { ms: 0, writes: 0, moved: 0, forced: 0, refined: 0, unseparated: 0, emitted: 0 };
  let writes = 0;
  const write = (index) => {
    const run3 = scene.runs[index];
    const f = frames2[index];
    const els = bound[index];
    const memo = cache[index];
    for (let r = 0; r < run3.roles.length; r++) {
      const el = els[r];
      if (!el) continue;
      const role = run3.roles[r];
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
  let moved2 = 0;
  const render2 = () => {
    const t0 = performance.now();
    writes = 0;
    moved2 = 0;
    cams = t3Cams(scene, values);
    t3State.detail = detail;
    const poses = cams.poses;
    const fresh = lastUnit !== unit || !lastPoses;
    let emitted = 0;
    for (const run3 of scene.runs) {
      const g = run3.group;
      const changed = fresh || (g >= 0 ? !samePose(poses[g], lastPoses[g]) : false);
      if (!changed) continue;
      t3Emit(run3, g >= 0 ? cams[g] : cams.world, frames2[run3.index]);
      write(run3.index);
      emitted++;
    }
    lastPoses = poses;
    lastUnit = unit;
    const orderStats = { forced: 0, refined: 0, unseparated: 0, edges: 0 };
    scene.layers.forEach((layer, index) => {
      const previous = orders[index];
      const order = t3Order(layer, frames2, cams, previous, orderStats, scene);
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
          moved2++;
          shifted.push(scene.runs[order[j]].name);
        }
        if (node) after = node;
      }
      orders[index] = order;
      if (shifted.length) changes.push({ layer: layer.name, moved: shifted });
    });
    stats.ms = performance.now() - t0;
    stats.writes = writes;
    stats.moved = moved2;
    stats.forced = orderStats.forced;
    stats.refined = orderStats.refined;
    stats.unseparated = orderStats.unseparated;
    stats.emitted = emitted;
    t3State.detail = 1;
    if (onFrame) onFrame(controller);
    return { ...stats };
  };
  let detail = 1;
  const set = (next, options2) => {
    if (options2 && options2.detail !== void 0) {
      const value = Math.max(0, Math.min(1, options2.detail));
      if (value !== detail) {
        detail = value;
        lastPoses = null;
      }
    }
    if (typeof next === "number") {
      const g = data.groups.find((group2) => group2.kind === "turn");
      if (g) values[g.name] = next;
    } else if (next) for (const [name, value] of Object.entries(next)) values[name] = value;
    if (follow) Object.assign(values, follow({ ...values }));
    return render2();
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
    const group2 = data.groups.find((g) => g.name === groupName) ?? data.groups.find((g) => g.kind === "turn");
    const pivot = group2 ? group2.origin : [0, 0, 0];
    const raw = Math.atan2(wy - pivot[1], wx - pivot[0]) * 180 / Math.PI;
    const key = group2 ? group2.name : "";
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
    render2();
  }) : null;
  if (observer) observer.observe(first);
  if (follow) Object.assign(values, follow({ ...values }));
  const controller = {
    set,
    render: render2,
    angleAt,
    get values() {
      return { ...values };
    },
    cover: (names, options2) => t3Cover(controller, names, options2),
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
    frames: () => frames2,
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
  render2();
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
  const frames2 = controller.frames();
  const sets = Array.isArray(names) ? names.length && Array.isArray(names[0]) ? names : [names] : [[names]];
  const candidates = [];
  const taken = /* @__PURE__ */ new Set();
  for (const list of sets) {
    const targets = scene.runs.filter((run3) => list.includes(run3.name));
    if (!targets.length) continue;
    const box = [Infinity, Infinity, -Infinity, -Infinity];
    for (const run3 of targets) {
      const b = frames2[run3.index].box;
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
        for (let at = 0; at < order.length; at++) if (targets.some((run3) => run3.index === order[at])) from = at + 1;
      } else if (!(layers && layers.includes(layer.name)) || index < home) return;
      for (let at = from; at < order.length; at++) {
        const run3 = scene.runs[order[at]];
        if (list.includes(run3.name) || taken.has(run3.index)) continue;
        const f = frames2[run3.index];
        const b = f.box;
        if (!(b[0] < box[2] + pad && box[0] < b[2] + pad && b[1] < box[3] + pad && box[1] < b[3] + pad)) continue;
        if (!targets.some((target) => !t3Disjoint(frames2[target.index], f, -pad))) continue;
        taken.add(run3.index);
        const share = (Math.min(b[2], box[2]) - Math.max(b[0], box[0])) * (Math.min(b[3], box[3]) - Math.max(b[1], box[1]));
        candidates.push({ run: run3, f, share });
      }
    });
  }
  candidates.sort((a, b) => b.share - a.share);
  const parts = [];
  let slot = 0;
  for (const { run: run3, f } of candidates) {
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
    parts.push(run3.name);
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
  const out2 = { world, screen };
  if (direction) out2.direction = [R[0] * direction[0] + R[1] * direction[1] + R[2] * direction[2], R[3] * direction[0] + R[4] * direction[1] + R[5] * direction[2], R[6] * direction[0] + R[7] * direction[1] + R[8] * direction[2]];
  return out2;
}
function t3FloorOf(scene, name, R = T3_EYE) {
  const index = scene.groups.findIndex((g) => g.name === name);
  let low = Infinity;
  for (const run3 of scene.runs) {
    if (run3.group !== index) continue;
    const c = run3.cloud;
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
function t3PoseUniforms(controller, group2, prefix = "uGroup") {
  const scene = controller.scene();
  const index = scene.groups.findIndex((g) => g.name === group2);
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

// third_party/anatomy/kit/lathe.mjs
var TAU = Math.PI * 2;
var LIGHT_UP = 1.2;
var BANDS = [0, 0.2, 0.42, 0.62];
var dot3 = (a, b) => a[0] * b[0] + a[1] * b[1] + a[2] * b[2];
var add3 = (a, b) => [a[0] + b[0], a[1] + b[1], a[2] + b[2]];
var sub3 = (a, b) => [a[0] - b[0], a[1] - b[1], a[2] - b[2]];
var mul3 = (a, k) => [a[0] * k, a[1] * k, a[2] * k];
var len3 = (a) => Math.hypot(a[0], a[1], a[2]);
var unit3 = (a) => {
  const length = len3(a) || 1;
  return [a[0] / length, a[1] / length, a[2] / length];
};
var cross3 = (a, b) => [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]];
var lerp3 = (a, b, t) => [a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t, a[2] + (b[2] - a[2]) * t];
function viewOf(P) {
  const { sinA, cosA, sinE, cosE } = cameraOf(P);
  return [cosA * cosE, sinA * cosE, sinE];
}
function lightOf(P) {
  const { sinA, cosA } = cameraOf(P);
  return unit3([-sinA, cosA, LIGHT_UP]);
}
var scaleOf = (P) => cameraOf(P).k;
function bandOf(score) {
  let tone = 0;
  while (tone < BANDS.length && score >= BANDS[tone]) tone++;
  return tone;
}
function frameAlong(o, a) {
  const axis = unit3(a);
  const helper = Math.abs(axis[2]) > 0.9 ? [1, 0, 0] : [0, 0, 1];
  const u = unit3(cross3(helper, axis));
  const v = cross3(axis, u);
  return { o, a: axis, u, v };
}
function pointOf(F, s, r, angle) {
  const c = Math.cos(angle);
  const n = Math.sin(angle);
  return [
    F.o[0] + F.a[0] * s + r * (c * F.u[0] + n * F.v[0]),
    F.o[1] + F.a[1] * s + r * (c * F.u[1] + n * F.v[1]),
    F.o[2] + F.a[2] * s + r * (c * F.u[2] + n * F.v[2])
  ];
}
var radialOf = (F, angle) => {
  const c = Math.cos(angle);
  const n = Math.sin(angle);
  return [c * F.u[0] + n * F.v[0], c * F.u[1] + n * F.v[1], c * F.u[2] + n * F.v[2]];
};
var angleToward = (F, direction) => Math.atan2(dot3(direction, F.v), dot3(direction, F.u));
function hullTagged(points) {
  const sorted = [...points].sort((a, b) => a.p[0] - b.p[0] || a.p[1] - b.p[1]);
  if (sorted.length < 3) return sorted;
  const cross = (o, a, b) => (a.p[0] - o.p[0]) * (b.p[1] - o.p[1]) - (a.p[1] - o.p[1]) * (b.p[0] - o.p[0]);
  const lower = [];
  for (const point of sorted) {
    while (lower.length >= 2 && cross(lower[lower.length - 2], lower[lower.length - 1], point) <= 1e-9) lower.pop();
    lower.push(point);
  }
  const upper = [];
  for (let index = sorted.length - 1; index >= 0; index--) {
    const point = sorted[index];
    while (upper.length >= 2 && cross(upper[upper.length - 2], upper[upper.length - 1], point) <= 1e-9) upper.pop();
    upper.push(point);
  }
  return [...lower.slice(0, -1), ...upper.slice(0, -1)];
}
var hullOf = (points) => hullTagged(points.map((p) => ({ p }))).map(({ p }) => p);
function groupsOf(keys) {
  const count = keys.length;
  const out2 = [];
  const start = keys.findIndex((key, index) => key !== keys[(index + count - 1) % count]);
  if (start < 0) {
    if (keys[0] !== null) out2.push({ key: keys[0], run: Array.from({ length: count + 1 }, (_, index) => index % count) });
    return out2;
  }
  let current = null;
  for (let step = 0; step < count; step++) {
    const index = (start + step) % count;
    const key = keys[index];
    if (current && current.key === key) {
      current.run.push((index + 1) % count);
      continue;
    }
    if (current && current.key !== null) out2.push(current);
    current = { key, run: [index, (index + 1) % count] };
  }
  if (current && current.key !== null) out2.push(current);
  return out2;
}
var stepsFor = (radius, least = 16, most = 112, scale = 0) => Math.max(least, Math.min(most, scale ? Math.ceil(TAU * radius * scale / 3) : Math.round(radius * 1.3 / 4) * 4));
function chains(edges) {
  const out2 = [];
  let current = null;
  for (const [a, b, keep] of edges) {
    if (!keep) {
      if (current) out2.push(current);
      current = null;
      continue;
    }
    if (!current) current = [a];
    current.push(b);
  }
  if (current) out2.push(current);
  if (out2.length > 1 && edges[0][2] && edges[edges.length - 1][2]) {
    const last = out2.pop();
    out2[0] = [...last, ...out2[0].slice(1)];
  }
  return out2;
}
function labelledArcs(nr, na, view, light, gr = nr, ga = na) {
  const cuts = [];
  if (Math.abs(gr) > 1e-9) {
    const visibleCut = -(ga * view.a) / (gr * view.flat);
    if (visibleCut > -1 && visibleCut < 1) {
      const d = Math.acos(visibleCut);
      cuts.push(view.phi - d, view.phi + d);
    }
  }
  if (Math.abs(nr) > 1e-9) {
    for (const threshold of BANDS) {
      const c = (threshold - na * light.a) / (nr * light.flat);
      if (c > -1 && c < 1) {
        const d = Math.acos(c);
        cuts.push(light.phi - d, light.phi + d);
      }
    }
  }
  const wrap = (angle) => (angle % TAU + TAU) % TAU;
  const sorted = [...new Set(cuts.map((angle) => Math.round(wrap(angle) * 1e9) / 1e9))].sort((a, b) => a - b);
  const label = (angle) => {
    const facing = gr * view.flat * Math.cos(angle - view.phi) + ga * view.a;
    if (facing <= 1e-9) return -1;
    return bandOf(nr * light.flat * Math.cos(angle - light.phi) + na * light.a);
  };
  if (!sorted.length) {
    const tone = label(0);
    return tone < 0 ? [] : [{ tone, from: 0, to: TAU, full: true }];
  }
  const arcs = sorted.map((from, index) => {
    const to = index + 1 < sorted.length ? sorted[index + 1] : sorted[0] + TAU;
    return { tone: label((from + to) / 2), from, to };
  });
  const merged = [];
  for (const arc of arcs) {
    const last = merged[merged.length - 1];
    if (last && last.tone === arc.tone && Math.abs(last.to - arc.from) < 1e-9) last.to = arc.to;
    else merged.push({ ...arc });
  }
  if (merged.length > 1 && merged[0].tone === merged[merged.length - 1].tone && Math.abs(merged[merged.length - 1].to - TAU - merged[0].from) < 1e-9) {
    const last = merged.pop();
    merged[0].from = last.from - TAU;
  }
  return merged.filter((arc) => arc.tone >= 0);
}
function hermiteSlopes(run3) {
  const n = run3.length - 1;
  const h = Array.from({ length: n }, (_, j) => run3[j + 1][0] - run3[j][0]);
  const delta = h.map((value, j) => (run3[j + 1][1] - run3[j][1]) / value);
  const d = new Array(n + 1).fill(0);
  const end = (h0, h1, d0, d1) => {
    let value = ((2 * h0 + h1) * d0 - h0 * d1) / (h0 + h1);
    if (Math.sign(value) !== Math.sign(d0)) value = 0;
    else if (Math.sign(d0) !== Math.sign(d1) && Math.abs(value) > Math.abs(3 * d0)) value = 3 * d0;
    return value;
  };
  if (n === 1) d[0] = d[1] = delta[0];
  else {
    d[0] = end(h[0], h[1], delta[0], delta[1]);
    d[n] = end(h[n - 1], h[n - 2], delta[n - 1], delta[n - 2]);
  }
  for (let k = 1; k < n; k++) {
    if (delta[k - 1] * delta[k] <= 0) continue;
    const w1 = 2 * h[k] + h[k - 1];
    const w2 = h[k] + 2 * h[k - 1];
    d[k] = (w1 + w2) / (w1 / delta[k - 1] + w2 / delta[k]);
  }
  return d;
}
function curveRuns(meridian) {
  const m = meridian.length;
  const segments = new Array(m - 1).fill(null);
  let start = 0;
  while (start < m - 1) {
    let end = start + 1;
    while (end < m - 1 && meridian[end][2] && Math.abs(meridian[end + 1][0] - meridian[end][0]) > 1e-9 && Math.abs(meridian[end][0] - meridian[end - 1][0]) > 1e-9) end++;
    const run3 = meridian.slice(start, end + 1);
    const n = run3.length - 1;
    if (n >= 2 && run3.every((point, j) => j === 0 || Math.abs(point[0] - run3[j - 1][0]) > 1e-9)) {
      const d = hermiteSlopes(run3);
      for (let j = 0; j < n; j++) {
        const [s0, r0] = run3[j];
        const [s1, r1] = run3[j + 1];
        const hj = s1 - s0;
        const d0 = d[j];
        const d1 = d[j + 1];
        const radius = (s) => {
          const t = (s - s0) / hj;
          return (2 * t ** 3 - 3 * t ** 2 + 1) * r0 + (t ** 3 - 2 * t ** 2 + t) * hj * d0 + (-2 * t ** 3 + 3 * t ** 2) * r1 + (t ** 3 - t ** 2) * hj * d1;
        };
        const slope = (s) => {
          const t = (s - s0) / hj;
          return ((6 * t ** 2 - 6 * t) * r0 + (6 * t - 6 * t ** 2) * r1) / hj + (3 * t ** 2 - 4 * t + 1) * d0 + (3 * t ** 2 - 2 * t) * d1;
        };
        segments[start + j] = { radius, slope };
      }
    }
    start = end;
  }
  return segments;
}
function curved(meridian, P, segments, { error = 0.2, depth = 6 } = {}) {
  const k = scaleOf(P);
  const out2 = [meridian[0]];
  for (let i = 0; i < meridian.length - 1; i++) {
    const curve = segments[i];
    const [s0] = meridian[i];
    const [s1] = meridian[i + 1];
    if (curve) {
      const split = (a, b, level) => {
        const mid = (a + b) / 2;
        const chord = (curve.radius(a) + curve.radius(b)) / 2;
        if (level < depth && Math.abs(curve.radius(mid) - chord) * k > error) {
          split(a, mid, level + 1);
          out2.push([mid, curve.radius(mid), 1]);
          split(mid, b, level + 1);
        }
      };
      split(s0, s1, 0);
    }
    out2.push(meridian[i + 1]);
  }
  return out2;
}
function smoothRows(meridian, F, P, { rows = 6, slope = null, radius = null, steps = 48, error = 0.35, depth: deepest = 8, fineness = 0.1 } = {}) {
  const V = viewOf(P);
  const L = lightOf(P);
  const view = { a: dot3(F.a, V), flat: Math.hypot(dot3(F.u, V), dot3(F.v, V)), phi: Math.atan2(dot3(F.v, V), dot3(F.u, V)) };
  const light = { a: dot3(F.a, L), flat: Math.hypot(dot3(F.u, L), dot3(F.v, L)), phi: Math.atan2(dot3(F.v, L), dot3(F.u, L)) };
  const m = meridian.length;
  const faces = [];
  for (let i = 0; i < m - 1; i++) {
    const ds = meridian[i + 1][0] - meridian[i][0];
    const dr = meridian[i + 1][1] - meridian[i][1];
    const length = Math.hypot(ds, dr) || 1;
    faces.push([ds / length, -dr / length]);
  }
  const splines = slope ? null : curveRuns(meridian);
  const vertexNormal = (k2, own) => {
    if (k2 <= 0 || k2 >= m - 1 || !meridian[k2][2]) return own;
    const a = faces[k2 - 1];
    const b = faces[k2];
    const x = a[0] + b[0];
    const y = a[1] + b[1];
    const length = Math.hypot(x, y) || 1;
    return [x / length, y / length];
  };
  const normalAt = (i, u) => {
    const [s0] = meridian[i];
    const [s1] = meridian[i + 1];
    const s = s0 + (s1 - s0) * u;
    const sign = Math.sign(s1 - s0) || 1;
    const g = slope ? slope(s) : splines[i] ? splines[i].slope(s) : null;
    if (g !== null) {
      const length2 = Math.hypot(1, g);
      return [sign / length2, -sign * g / length2];
    }
    const a = vertexNormal(i, faces[i]);
    const b = vertexNormal(i + 1, faces[i]);
    const x = a[0] + (b[0] - a[0]) * u;
    const y = a[1] + (b[1] - a[1]) * u;
    const length = Math.hypot(x, y) || 1;
    return [x / length, y / length];
  };
  const pointAt = (i, u, angle) => {
    const [s0, r0] = meridian[i];
    const [s1, r1] = meridian[i + 1];
    const s = s0 + (s1 - s0) * u;
    return iso(pointOf(F, s, radius ? radius(s) : splines && splines[i] ? splines[i].radius(s) : r0 + (r1 - r0) * u, angle), P);
  };
  const buckets = [[], [], [], [], []];
  const fine2 = TAU / Math.max(24, Math.min(192, steps * 1.5));
  const arcPoints = (i, u, from, to) => {
    const count = Math.max(1, Math.ceil((to - from) / fine2));
    return Array.from({ length: count + 1 }, (_, index) => pointAt(i, u, from + (to - from) * index / count));
  };
  const centreOf = (arc, reference) => {
    let mid = (arc.from + arc.to) / 2 - reference;
    mid = (mid % TAU + TAU) % TAU;
    return mid;
  };
  const levelOf = (i, u) => {
    const [nr, na] = normalAt(i, u);
    const groups = /* @__PURE__ */ new Map();
    for (const arc of labelledArcs(nr, na, view, light, faces[i][0], faces[i][1])) {
      if (!groups.has(arc.tone)) groups.set(arc.tone, []);
      groups.get(arc.tone).push(arc);
    }
    for (const list of groups.values()) list.sort((x, y) => centreOf(x, light.phi) - centreOf(y, light.phi));
    return { i, u, groups };
  };
  const same = (x, y) => {
    if (x.groups.size !== y.groups.size) return false;
    for (const [tone, list] of x.groups) if ((y.groups.get(tone) ?? []).length !== list.length) return false;
    return true;
  };
  const align = (reference, arc) => {
    const out2 = { ...arc };
    const centre = (reference.from + reference.to) / 2;
    while ((out2.from + out2.to) / 2 - centre > Math.PI) {
      out2.from -= TAU;
      out2.to -= TAU;
    }
    while (centre - (out2.from + out2.to) / 2 > Math.PI) {
      out2.from += TAU;
      out2.to += TAU;
    }
    return out2;
  };
  const strayOf = (i, a, mid, b) => {
    let worst = 0;
    for (const [tone, list] of mid.groups) {
      list.forEach((arc, index) => {
        const lo = align(arc, a.groups.get(tone)[index]);
        const hi = align(arc, b.groups.get(tone)[index]);
        for (const key of ["from", "to"]) {
          const p = pointAt(i, mid.u, arc[key]);
          const p0 = pointAt(i, a.u, lo[key]);
          const p1 = pointAt(i, b.u, hi[key]);
          worst = Math.max(worst, Math.hypot(p[0] - (p0[0] + p1[0]) / 2, p[1] - (p0[1] + p1[1]) / 2));
        }
      });
    }
    return worst;
  };
  const sheet = (tone, levels) => {
    levels[0].groups.get(tone).forEach((arc, index) => {
      const chain = [arc];
      for (let k2 = 1; k2 < levels.length; k2++) chain.push(align(chain[k2 - 1], levels[k2].groups.get(tone)[index]));
      const last = levels.length - 1;
      const points = [...arcPoints(levels[0].i, levels[0].u, chain[0].from, chain[0].to)];
      for (let k2 = 1; k2 < last; k2++) points.push(pointAt(levels[k2].i, levels[k2].u, chain[k2].to));
      points.push(...arcPoints(levels[last].i, levels[last].u, chain[last].from, chain[last].to).reverse());
      for (let k2 = last - 1; k2 >= 1; k2--) points.push(pointAt(levels[k2].i, levels[k2].u, chain[k2].from));
      buckets[tone].push(pathOf(oriented(points), true));
    });
  };
  const overlap2 = (x, y) => Math.min(x.to, y.to) - Math.max(x.from, y.from);
  const strip = (tone, a, b) => {
    const below = a.groups.get(tone) ?? [];
    const above = (b.groups.get(tone) ?? []).map((arc) => ({ arc, used: false }));
    const quad = (lo, hi) => {
      const points = [...arcPoints(a.i, a.u, lo.from, lo.to), ...arcPoints(b.i, b.u, hi.from, hi.to).reverse()];
      buckets[tone].push(pathOf(oriented(points), true));
    };
    for (const arc of below) {
      let best = null;
      let score = -Infinity;
      for (const entry of above) {
        if (entry.used) continue;
        const aligned = align(arc, entry.arc);
        const value = overlap2(arc, aligned);
        if (value > score) score = value, best = entry;
      }
      if (best && score > -0.05) {
        best.used = true;
        quad(arc, align(arc, best.arc));
      } else {
        const centre = (arc.from + arc.to) / 2;
        quad(arc, { from: centre, to: centre });
      }
    }
    for (const entry of above) {
      if (entry.used) continue;
      const centre = (entry.arc.from + entry.arc.to) / 2;
      quad({ from: centre, to: centre }, entry.arc);
    }
  };
  const k = scaleOf(P);
  let run3 = [];
  const flush = () => {
    const tones = [...new Set(run3.flatMap((level) => [...level.groups.keys()]))].sort((x, y) => x - y);
    for (const tone of tones) {
      const countOf = (level) => (level.groups.get(tone) ?? []).length;
      let start = 0;
      for (let at = 1; at <= run3.length; at++) {
        if (at < run3.length && countOf(run3[at - 1]) === countOf(run3[at])) continue;
        if (at - 1 > start && countOf(run3[start])) sheet(tone, run3.slice(start, at));
        if (at < run3.length) strip(tone, run3[at - 1], run3[at]);
        start = at;
      }
    }
    run3 = [];
  };
  for (let i = 0; i < m - 1; i++) {
    const ds = meridian[i + 1][0] - meridian[i][0];
    if (Math.abs(ds) < 1e-9) {
      flush();
      continue;
    }
    const count = Math.max(1, rows);
    const reach = Math.hypot(ds, meridian[i + 1][1] - meridian[i][1]) * k / count;
    const limit = Math.max(1, Math.min(deepest, Math.ceil(Math.log2(Math.max(2, reach / fineness)))));
    const coarse = Array.from({ length: count + 1 }, (_, index) => levelOf(i, index / count));
    run3.push(coarse[0]);
    const refine = (a, b, depth) => {
      const mid = levelOf(i, (a.u + b.u) / 2);
      const split = depth < limit && (!same(a, b) || !same(a, mid) || depth < 6 && strayOf(i, a, mid, b) > error);
      if (!split) {
        run3.push(b);
        return;
      }
      refine(a, mid, depth + 1);
      refine(mid, b, depth + 1);
    };
    for (let index = 1; index <= count; index++) refine(coarse[index - 1], coarse[index], 0);
  }
  flush();
  return buckets;
}
function sideOf(meridian) {
  const m = meridian.length;
  let first = 0;
  let last = m - 1;
  if (meridian[0][1] <= 1e-9) first = 1;
  if (meridian[m - 1][1] <= 1e-9) last = m - 2;
  const side = meridian.slice(first, last + 1);
  for (let index = 1; index < side.length; index++) if (side[index][0] - side[index - 1][0] <= 1e-9) return null;
  return side.length >= 3 ? side : null;
}
function surfaceOf(side, F, P, rims, { samples = 96, slope = null } = {}) {
  const V = viewOf(P);
  const aV = dot3(F.a, V);
  const facing = Math.atan2(dot3(F.v, V), dot3(F.u, V));
  const [left, right] = silhouettePoints(side, F, P, { samples, slope });
  if (left.length <= samples || right.length <= samples) return null;
  const s0 = side[0][0];
  const s1 = side[side.length - 1][0];
  const angleOf = (point) => angleToward(F, sub3(point, add3(F.o, mul3(F.a, dot3(sub3(point, F.o), F.a)))));
  const wrap = (angle) => (angle % TAU + TAU) % TAU;
  const arc = (s, r, from, to, through) => {
    let sweep = wrap(to - from);
    if (wrap(through - from) > sweep) sweep -= TAU;
    const count = Math.max(4, Math.ceil(Math.abs(sweep) / (TAU / 96)), Math.ceil(Math.abs(sweep) * r * scaleOf(P) / 1.5));
    return Array.from({ length: count + 1 }, (_, index) => iso(pointOf(F, s, r, from + sweep * index / count), P));
  };
  const r0 = side[0][1];
  const r1 = side[side.length - 1][1];
  const bottom = -aV > 0 ? facing + Math.PI : facing;
  const top = aV > 0 ? facing + Math.PI : facing;
  const L = left.map((point) => iso(point, P));
  const R = right.map((point) => iso(point, P));
  const topArc = arc(s1, r1, angleOf(left[left.length - 1]), angleOf(right[right.length - 1]), top);
  const bottomArc = arc(s0, r0, angleOf(right[0]), angleOf(left[0]), bottom);
  const keepFirst = rims === "all" || rims === "first" || rims === "ends";
  const keepLast = rims === "all" || rims === "last" || rims === "ends";
  const fill = pathOf([...L, ...topArc, ...[...R].reverse(), ...bottomArc], true);
  const outline = [pathOf(L), pathOf(R), keepLast ? pathOf(topArc) : "", keepFirst ? pathOf(bottomArc) : ""].join("");
  const hull = hullOf([...arc(s0, r0, 0, TAU - 1e-6, Math.PI), ...arc(s1, r1, 0, TAU - 1e-6, Math.PI), ...L, ...R]);
  let gap = 0;
  for (const p of [...L, ...R]) {
    let best = Infinity;
    for (let index = 0; index < hull.length; index++) {
      const a = hull[index];
      const b = hull[(index + 1) % hull.length];
      const dx = b[0] - a[0];
      const dy = b[1] - a[1];
      const t = Math.max(0, Math.min(1, ((p[0] - a[0]) * dx + (p[1] - a[1]) * dy) / (dx * dx + dy * dy || 1)));
      best = Math.min(best, Math.hypot(p[0] - a[0] - dx * t, p[1] - a[1] - dy * t));
    }
    gap = Math.max(gap, best);
  }
  return { fill, outline, gap };
}
var softOf = (meridian) => meridian.some((point) => Boolean(point[2]));
function lathe(meridian, F, P, { steps = stepsFor(Math.max(...meridian.map(([, r]) => r)), 32, 160, scaleOf(P)), fill = "auto", hole = null, bevel = 0, rims = "all", smooth: asked = "auto", waist = 0.5 } = {}) {
  const smooth = asked === "auto" ? softOf(meridian) : asked;
  const V = viewOf(P);
  const L = lightOf(P);
  const aV = dot3(F.a, V);
  const uV = dot3(F.u, V);
  const vV = dot3(F.v, V);
  const aL = dot3(F.a, L);
  const uL = dot3(F.u, L);
  const vL = dot3(F.v, L);
  const n = steps;
  const m = meridian.length;
  const rings = meridian.map(([s, r]) => Array.from({ length: n }, (_, j) => iso(pointOf(F, s, r, j / n * TAU), P)));
  const midC = [];
  const midS = [];
  for (let j = 0; j < n; j++) {
    const t = (j + 0.5) / n * TAU;
    midC.push(Math.cos(t));
    midS.push(Math.sin(t));
  }
  const seen = [];
  const tones = [];
  for (let i = 0; i < m - 1; i++) {
    const ds = meridian[i + 1][0] - meridian[i][0];
    const dr = meridian[i + 1][1] - meridian[i][1];
    const length = Math.hypot(ds, dr);
    const row = [];
    const toneRow = [];
    for (let j = 0; j < n; j++) {
      if (length < 1e-9) {
        row.push(false);
        toneRow.push(0);
        continue;
      }
      const facing = ds * (midC[j] * uV + midS[j] * vV) - dr * aV;
      const lit = (ds * (midC[j] * uL + midS[j] * vL) - dr * aL) / length;
      row.push(facing > 1e-6 * length);
      toneRow.push(bandOf(lit));
    }
    seen.push(row);
    tones.push(toneRow);
  }
  const buckets = [[], [], [], [], []];
  const all = [];
  const smoothed = smooth ? smoothRows(meridian, F, P, { steps, ...smooth === true ? {} : smooth }) : null;
  if (smoothed) smoothed.forEach((list, tone) => list.forEach((d) => (buckets[tone].push(d), all.push(d))));
  for (let i = 0; i < m - 1; i++) {
    if (smoothed && Math.abs(meridian[i + 1][0] - meridian[i][0]) > 1e-9) continue;
    const keys = seen[i].map((visible, j) => visible ? tones[i][j] : null);
    for (const { key, run: run3 } of groupsOf(keys)) {
      const a = run3.map((j) => rings[i][j]);
      const b = run3.map((j) => rings[i + 1][j]).reverse();
      const d = pathOf(oriented([...a, ...b]), true);
      buckets[key].push(d);
      all.push(d);
    }
  }
  const phi = Math.atan2(vV, uV);
  const flatV = Math.hypot(uV, vV);
  const rangeOf = (i) => {
    const ds = meridian[i + 1][0] - meridian[i][0];
    const dr = meridian[i + 1][1] - meridian[i][1];
    if (Math.hypot(ds, dr) < 1e-9) return null;
    if (Math.abs(ds) < 1e-9 || flatV < 1e-9) return -dr * aV > 1e-9 ? [-1, 1] : null;
    const c = dr * aV / (ds * flatV);
    return ds > 0 ? [Math.max(-1, c), 1] : [-1, Math.min(1, c)];
  };
  const arcsOf = (ranges) => {
    if (ranges.some((range) => !range)) return [];
    const lo = Math.max(...ranges.map(([x]) => x));
    const hi = Math.min(...ranges.map(([, x]) => x));
    if (lo >= hi - 1e-9) return [];
    const near = Math.acos(Math.min(1, hi));
    const far = Math.acos(Math.max(-1, lo));
    if (hi >= 1 && lo <= -1) return [[phi, phi + TAU]];
    if (hi >= 1) return [[phi - far, phi + far]];
    if (lo <= -1) return [[phi + near, phi + TAU - near]];
    return [[phi + near, phi + far], [phi - far, phi - near]];
  };
  const along = (s, r, [from, to]) => {
    const count = Math.max(2, Math.ceil((to - from) * Math.max(r, 1e-6) * scaleOf(P) / 1.5));
    return Array.from({ length: count + 1 }, (_, j) => iso(pointOf(F, s, r, from + (to - from) * j / count), P));
  };
  const creases = [];
  for (let i = 1; i < m - 1; i++) {
    if (meridian[i][2] || meridian[i][1] <= 1e-9) continue;
    for (const arc of arcsOf([rangeOf(i - 1), rangeOf(i)])) creases.push(pathOf(along(meridian[i][0], meridian[i][1], arc)));
  }
  let bevelPath = "";
  if (bevel > 0 && m > 2) {
    const ends = [];
    if (meridian[0][1] <= 1e-9) ends.push([0, 1, 1]);
    if (meridian[m - 1][1] <= 1e-9) ends.push([m - 2, m - 2, m - 3]);
    for (const [cap, rim, side] of ends) {
      const [s, r] = meridian[rim];
      for (const arc of arcsOf([rangeOf(cap), rangeOf(side)])) {
        const inset = along(s, Math.max(0, r - bevel), arc);
        const edge = along(s, r, arc);
        bevelPath += pathOf([edge[0], ...inset.slice(1, -1), edge[edge.length - 1]]);
      }
    }
  }
  const { fill: fillPath, outline } = outlineOf(meridian, F, P, { steps: n, fill, hole, rims, smooth, waist, all });
  return {
    fill: fillPath,
    outline,
    crease: creases.join(""),
    top: buckets[4].join(""),
    shades: buckets.slice(0, 4).map((list) => list.join("")),
    bevel: bevelPath || void 0,
    seamless: Boolean(smoothed)
  };
}
function shapeOf(meridian, P, smooth) {
  if (smooth && smooth.radius) {
    const segments = meridian.slice(0, -1).map(([s0], index) => Math.abs(meridian[index + 1][0] - s0) > 1e-9 ? { radius: smooth.radius, slope: smooth.slope } : null);
    return curved(meridian, P, segments);
  }
  const curves = smooth && !smooth.slope ? curveRuns(meridian) : null;
  return curves && curves.some(Boolean) ? curved(meridian, P, curves) : meridian;
}
function outlineOf(meridian, F, P, { steps = stepsFor(Math.max(...meridian.map(([, r]) => r)), 32, 160, scaleOf(P)), fill = "auto", hole = null, rims = "all", smooth: asked = "auto", waist = 0.5, all = null } = {}) {
  const smooth = asked === "auto" ? softOf(meridian) : asked;
  const n = steps;
  let fillPath;
  let outline;
  const shape = shapeOf(meridian, P, smooth);
  const side = fill === "auto" || fill === "surface" ? sideOf(shape) : null;
  const surface = side && !hole ? surfaceOf(side, F, P, rims, { slope: smooth && smooth.slope ? smooth.slope : null }) : null;
  if (surface && (fill === "surface" || surface.gap > waist)) {
    fillPath = surface.fill;
    outline = surface.outline;
  } else if (fill === "hull" || fill === "auto" || fill === "surface") {
    const most = Math.max(...shape.map(([, r]) => r));
    const around = Math.min(320, Math.max(n, Math.ceil(TAU * most * scaleOf(P) / 1.5)));
    const tagged = [];
    shape.forEach(([s, r], index) => {
      for (let j = 0; j < around; j++) tagged.push({ p: iso(pointOf(F, s, r, j / around * TAU), P), ring: index });
    });
    const hull = hullTagged(tagged);
    const holePath = hole ? pathOf(Array.from({ length: around }, (_, j) => iso(pointOf(F, hole[0], hole[1], j / around * TAU), P)), true) : "";
    fillPath = pathOf(hull.map(({ p }) => p), true) + holePath;
    if (rims === "all") {
      outline = pathOf(hull.map(({ p }) => p), true) + holePath;
    } else {
      const keepFirst = rims === "first" || rims === "ends";
      const keepLast = rims === "last" || rims === "ends";
      const edges = hull.map((a, index) => {
        const b = hull[(index + 1) % hull.length];
        const same = a.ring === b.ring;
        const keep = !same || a.ring !== 0 && a.ring !== shape.length - 1 || keepFirst && a.ring === 0 || keepLast && a.ring === shape.length - 1;
        return [a.p, b.p, keep];
      });
      outline = chains(edges).map((points) => pathOf(points)).join("") + holePath;
    }
  } else {
    fillPath = all ? all.join("") : (({ shades, top }) => [...shades, top].join(""))(lathe(meridian, F, P, { steps: n, fill: "auto", hole, rims, smooth, waist }));
    outline = "";
  }
  return { fill: fillPath, outline };
}
var signedArea = (points) => points.reduce((sum, [x, y], index) => {
  const [nx, ny] = points[(index + 1) % points.length];
  return sum + x * ny - nx * y;
}, 0);
var oriented = (points) => signedArea(points) < 0 ? [...points].reverse() : points;
function sphereOf(centre, r, P, { steps = 48 } = {}) {
  const V = viewOf(P);
  const L = lightOf(P);
  const F = frameAlong(centre, V);
  const flat = (p) => iso(p, P);
  const rim = Array.from({ length: steps }, (_, index) => pointOf(F, 0, r, index / steps * TAU));
  const outline = pathOf(rim.map(flat), true);
  const capOf = (threshold) => {
    const points = rim.filter((p) => dot3(sub3(p, centre), L) / r >= threshold).map(flat);
    const c = dot3(L, V);
    const LF = frameAlong(add3(centre, mul3(L, r * threshold)), L);
    const radius = r * Math.sqrt(Math.max(0, 1 - threshold * threshold));
    for (let index = 0; index < steps; index++) {
      const p = pointOf(LF, 0, radius, index / steps * TAU);
      if (dot3(sub3(p, centre), V) >= -1e-9) points.push(flat(p));
    }
    if (c > threshold) points.push(flat(add3(centre, mul3(V, r))));
    return points.length > 2 ? pathOf(hullOf(points), true) : "";
  };
  const shades = [outline, capOf(BANDS[1]), capOf(BANDS[2]), capOf(BANDS[3])];
  return { fill: outline, outline, crease: "", top: "", shades, seamless: true };
}
function silhouettePoints(profile, F, P, { samples = 72, slope: given = null, radius = null } = {}) {
  const V = viewOf(P);
  const aV = dot3(F.a, V);
  const uV = dot3(F.u, V);
  const vV = dot3(F.v, V);
  const facing = Math.atan2(vV, uV);
  const flat = Math.hypot(uV, vV) || 1e-9;
  const s0 = profile[0][0];
  const s1 = profile[profile.length - 1][0];
  const radiusAt = radius ?? ((s) => {
    let index = 1;
    while (index < profile.length - 1 && profile[index][0] < s) index++;
    const [sa, ra] = profile[index - 1];
    const [sb, rb] = profile[index];
    return ra + (rb - ra) * (s - sa) / (sb - sa || 1);
  });
  const side = (sign) => {
    const points = [];
    for (let step = 0; step <= samples; step++) {
      const s = s0 + (s1 - s0) * step / samples;
      const h = (s1 - s0) / samples / 2 || 0.01;
      const slope = given ? given(s) : (radiusAt(Math.min(s1, s + h)) - radiusAt(Math.max(s0, s - h))) / (Math.min(s1, s + h) - Math.max(s0, s - h) || 1);
      const c = slope * aV / flat;
      if (Math.abs(c) > 1) continue;
      points.push(pointOf(F, s, radiusAt(s), facing + sign * Math.acos(c)));
    }
    return points;
  };
  return [side(1), side(-1)];
}
function profileCurve(profile, { slope = null, radius = null } = {}) {
  for (let index = 1; index < profile.length; index++) if (profile[index][0] - profile[index - 1][0] <= 1e-9) throw new Error(`profileCurve: s must rise along the profile (point ${index} at s = ${profile[index][0]})`);
  const segments = curveRuns(profile);
  const s0 = profile[0][0];
  const s1 = profile[profile.length - 1][0];
  const find = (s) => {
    let lo = 0;
    let hi = profile.length - 2;
    while (lo < hi) {
      const mid = lo + hi + 1 >> 1;
      if (profile[mid][0] <= s) lo = mid;
      else hi = mid - 1;
    }
    return lo;
  };
  const linear = (index, s) => {
    const [sa, ra] = profile[index];
    const [sb, rb] = profile[index + 1];
    return [ra + (rb - ra) * (s - sa) / (sb - sa), (rb - ra) / (sb - sa)];
  };
  const radiusAt = radius ?? ((s) => {
    const at = Math.max(s0, Math.min(s1, s));
    const index = find(at);
    return segments[index] ? segments[index].radius(at) : linear(index, at)[0];
  });
  const slopeAt = slope ?? ((s) => {
    const at = Math.max(s0, Math.min(s1, s));
    const index = find(at);
    return segments[index] ? segments[index].slope(at) : linear(index, at)[1];
  });
  return { s0, s1, radius: radiusAt, slope: slopeAt, analytic: Boolean(slope && radius) };
}
function arcOf(F, s, r, P, { slope = 0, steps = 0, least = 0.02, inward = false, from = 0, to = TAU, trim = 0.3 } = {}) {
  const V = viewOf(P);
  const aV = dot3(F.a, V);
  const uV = dot3(F.u, V);
  const vV = dot3(F.v, V);
  const flat = Math.hypot(uV, vV);
  const phi = Math.atan2(vV, uV);
  const norm = Math.hypot(1, slope);
  const full = Math.abs(to - from - TAU) < 1e-9;
  let visible;
  if (flat < 1e-9) visible = (inward ? slope * aV / norm > least : -slope * aV / norm > least) ? [[phi, phi + TAU]] : [];
  else if (inward) {
    const c = (slope * aV - least * norm) / flat;
    visible = c <= -1 ? [] : c >= 1 ? [[phi, phi + TAU]] : [[phi + Math.acos(c), phi + TAU - Math.acos(c)]];
  } else {
    const c = (least * norm + slope * aV) / flat;
    visible = c >= 1 ? [] : c <= -1 ? [[phi, phi + TAU]] : [[phi - Math.acos(c), phi + Math.acos(c)]];
  }
  const at = (t) => iso(pointOf(F, s, r, t), P);
  const speed = (t) => {
    const a = at(t - 1e-3);
    const b = at(t + 1e-3);
    return Math.hypot(b[0] - a[0], b[1] - a[1]) / 2e-3;
  };
  const count = (span) => Math.max(2, Math.ceil((steps || stepsFor(r, 24, 112)) * span / TAU), Math.ceil(span * r * scaleOf(P) / 1.5));
  const out2 = [];
  for (const [a, b] of visible) {
    if (b - a >= TAU - 1e-9 && full) {
      const n = count(TAU);
      out2.push(pathOf(Array.from({ length: n }, (_, j) => at(from + j / n * TAU)), true));
      continue;
    }
    const pieces = full ? [[a, b, true, true]] : [];
    if (!full)
      for (let turn = -2; turn <= 2; turn++) {
        const lo = Math.max(a + turn * TAU, from);
        const hi = Math.min(b + turn * TAU, to);
        if (hi - lo > 1e-6) pieces.push([lo, hi, lo > from + 1e-9, hi < to - 1e-9]);
      }
    for (const [lo, hi, limb0, limb1] of pieces) {
      const span = hi - lo;
      const cut0 = limb0 && trim > 0 ? Math.min(span * 0.25, trim / (speed(lo) || 1)) : 0;
      const cut1 = limb1 && trim > 0 ? Math.min(span * 0.25, trim / (speed(hi) || 1)) : 0;
      const t0 = lo + cut0;
      const t1 = hi - cut1;
      const n = count(t1 - t0);
      out2.push(pathOf(Array.from({ length: n + 1 }, (_, j) => at(t0 + (t1 - t0) * j / n))));
    }
  }
  return out2.join("");
}
function resample(points, spacing) {
  const lengths = [0];
  for (let index = 1; index < points.length; index++) lengths.push(lengths[index - 1] + len3(sub3(points[index], points[index - 1])));
  const total = lengths[lengths.length - 1];
  const count = Math.max(1, Math.round(total / spacing));
  const out2 = [];
  let segment = 1;
  for (let step = 0; step <= count; step++) {
    const at = total * step / count;
    while (segment < points.length - 1 && lengths[segment] < at) segment++;
    const a = points[segment - 1];
    const b = points[segment];
    const span = lengths[segment] - lengths[segment - 1] || 1;
    out2.push(lerp3(a, b, Math.min(1, Math.max(0, (at - lengths[segment - 1]) / span))));
  }
  return out2;
}
function pathLength(points) {
  let total = 0;
  for (let index = 1; index < points.length; index++) total += len3(sub3(points[index], points[index - 1]));
  return total;
}
function cut(points, from, to) {
  const out2 = [];
  let walked = 0;
  for (let index = 1; index < points.length; index++) {
    const a = points[index - 1];
    const b = points[index];
    const length = len3(sub3(b, a));
    const start = walked;
    const end = walked + length;
    if (end >= from && start <= to) {
      const t0 = Math.max(0, (from - start) / (length || 1));
      const t1 = Math.min(1, (to - start) / (length || 1));
      if (!out2.length) out2.push(lerp3(a, b, t0));
      out2.push(lerp3(a, b, t1));
    }
    walked = end;
  }
  return out2;
}
var pointAlong = (points, at) => {
  const piece = cut(points, at, at + 0.01);
  return piece[0] ?? points[points.length - 1];
};
function tangentAlong(points, at) {
  const total = pathLength(points);
  const a = pointAlong(points, Math.max(0, at - 0.6));
  const b = pointAlong(points, Math.min(total, at + 0.6));
  return unit3(sub3(b, a));
}

// third_party/anatomy/kit/tube.mjs
var LIGHT = (() => {
  const length = Math.hypot(-0.55, -0.835);
  return [-0.55 / length, -0.835 / length];
})();
function runsOf(total, gaps = []) {
  const cuts = gaps.map(([a, b]) => [Math.max(0, Math.min(a, b)), Math.min(total, Math.max(a, b))]).filter(([a, b]) => b - a > 1e-6).sort((x, y) => x[0] - y[0]);
  const runs = [];
  let at = 0;
  for (const [a, b] of cuts) {
    if (a > at + 1e-6) runs.push([at, a]);
    at = Math.max(at, b);
  }
  if (total > at + 1e-6) runs.push([at, total]);
  return runs;
}

// third_party/anatomy/kit/audit.mjs
var BIG = 1e9;
function body(F, poly, meta = {}) {
  return { kind: "body", F, poly: poly.map(([s, r]) => [s, Math.max(0, r)]), ...meta };
}
function traced(meridian, { radius = null, error = 0.02, depth = 6 } = {}) {
  const segments = radius ? null : curveRuns(meridian);
  const out2 = [[meridian[0][0], meridian[0][1]]];
  for (let index = 0; index < meridian.length - 1; index++) {
    const [s0] = meridian[index];
    const [s1, r1] = meridian[index + 1];
    const along = Math.abs(s1 - s0) > 1e-9;
    const at = along && radius ? radius : along && segments[index] ? segments[index].radius : null;
    if (at) {
      const split = (a, b, level) => {
        const mid = (a + b) / 2;
        if (level >= depth) return;
        const ra = at(a);
        const rb = at(b);
        const deviation = Math.max(...[0.25, 0.5, 0.75].map((t) => Math.abs(at(a + (b - a) * t) - (ra + (rb - ra) * t))));
        if (deviation <= error) return;
        split(a, mid, level + 1);
        out2.push([mid, at(mid)]);
        split(mid, b, level + 1);
      };
      split(s0, s1, 0);
    }
    out2.push([s1, r1]);
  }
  return out2;
}
function solid(F, profile, { radius = null, ...meta } = {}) {
  const first = profile[0];
  const last = profile[profile.length - 1];
  return body(F, traced([[first[0], 0], ...profile, [last[0], 0]], { radius: radius && ((s) => radius(Math.max(first[0], Math.min(last[0], s)))) }), meta);
}
function prism(F, polygon, s0, s1, meta = {}) {
  return { kind: "prism", F, poly: polygon.map(([x, y]) => [x, y]), s0: Math.min(s0, s1), s1: Math.max(s0, s1), ...meta };
}
var ball = (at, r, meta = {}) => ({ kind: "ball", o: at, r, ...meta });
function tube(points, radius, meta = {}) {
  const total = pathLength(points) || 1;
  let walked = 0;
  const radii = Array.isArray(radius) ? radius : points.map((point, index) => {
    if (index > 0) walked += len3(sub3(point, points[index - 1]));
    return typeof radius === "function" ? radius(walked / total) : radius;
  });
  return { kind: "tube", points, radii, round: meta.round ?? [false, false], ...meta };
}
function moved(shape, offset) {
  if (!offset || !offset[0] && !offset[1] && !offset[2]) return shape;
  if (shape.slide) {
    const { from, to, r } = shape.slide;
    const reach = Math.max(from + 1e-3, to + dot3(offset, shape.F.a));
    return { ...shape, poly: [[from, 0], [from, r], [reach, r], [reach, 0]], slide: { from, to: reach, r }, _b: void 0, _f: void 0 };
  }
  const cut2 = shape.cut ? Array.isArray(shape.cut) ? shape.cut.map((one) => moved(one, offset)) : moved(shape.cut, offset) : void 0;
  if (shape.kind === "body" || shape.kind === "prism") return { ...shape, cut: cut2, F: { ...shape.F, o: add3(shape.F.o, offset) }, _b: void 0, _f: void 0 };
  if (shape.kind === "tube") return { ...shape, cut: cut2, points: shape.points.map((p) => add3(p, offset)), tips: shape.tips && shape.tips.map((tip) => tip && add3(tip, offset)), _b: void 0 };
  return { ...shape, cut: cut2, o: add3(shape.o, offset), _b: void 0 };
}
function polyDistance(poly, s, r) {
  let best = BIG;
  let inside2 = false;
  for (let i = 0, j = poly.length - 1; i < poly.length; j = i++) {
    const [s0, r0] = poly[j];
    const [s1, r1] = poly[i];
    const ds = s1 - s0;
    const dr = r1 - r0;
    const span = ds * ds + dr * dr;
    const t = span > 0 ? Math.max(0, Math.min(1, ((s - s0) * ds + (r - r0) * dr) / span)) : 0;
    const es = s - s0 - ds * t;
    const er = r - r0 - dr * t;
    const d2 = es * es + er * er;
    if (d2 < best && (r0 > 1e-9 || r1 > 1e-9)) best = d2;
    if (r0 > r !== r1 > r && s < s0 + (r - r0) * ds / (dr || 1e-12)) inside2 = !inside2;
  }
  const d = Math.sqrt(best);
  return inside2 ? -d : d;
}
function polygonDistance(poly, x, y) {
  let best = BIG;
  let inside2 = false;
  for (let i = 0, j = poly.length - 1; i < poly.length; j = i++) {
    const [x0, y0] = poly[j];
    const [x1, y1] = poly[i];
    const dx = x1 - x0;
    const dy = y1 - y0;
    const span = dx * dx + dy * dy;
    const t = span > 0 ? Math.max(0, Math.min(1, ((x - x0) * dx + (y - y0) * dy) / span)) : 0;
    const ex = x - x0 - dx * t;
    const ey = y - y0 - dy * t;
    const d2 = ex * ex + ey * ey;
    if (d2 < best) best = d2;
    if (y0 > y !== y1 > y && x < x0 + (y - y0) * dx / (dy || 1e-12)) inside2 = !inside2;
  }
  const d = Math.sqrt(best);
  return inside2 ? -d : d;
}
function cappedSegment(p, a, b, r, endRadius = r) {
  const bx = b[0] - a[0];
  const by = b[1] - a[1];
  const bz = b[2] - a[2];
  const px = p[0] - a[0];
  const py = p[1] - a[1];
  const pz = p[2] - a[2];
  const baba = bx * bx + by * by + bz * bz || 1e-12;
  const paba = px * bx + py * by + pz * bz;
  if (endRadius !== r) {
    const length = Math.sqrt(baba);
    const along = paba / length;
    const radial = Math.hypot(px - bx * paba / baba, py - by * paba / baba, pz - bz * paba / baba);
    return polyDistance([[0, 0], [0, r], [length, endRadius], [length, 0]], along, radial);
  }
  const x = Math.hypot(px * baba - bx * paba, py * baba - by * paba, pz * baba - bz * paba) - r * baba;
  const y = Math.abs(paba - baba * 0.5) - baba * 0.5;
  const x2 = x * x;
  const y2 = y * y * baba;
  const d = Math.max(x, y) < 0 ? -Math.min(x2, y2) : (x > 0 ? x2 : 0) + (y > 0 ? y2 : 0);
  return Math.sign(d) * Math.sqrt(Math.abs(d)) / baba;
}
function segmentPoint(p, a, b) {
  const ba = sub3(b, a);
  const pa = sub3(p, a);
  const t = Math.max(0, Math.min(1, dot3(pa, ba) / (dot3(ba, ba) || 1e-12)));
  return { d: len3(sub3(pa, mul3(ba, t))), t };
}
function sdf(shape, p) {
  const d = baseSdf(shape, p);
  return shape.cut ? Math.max(d, -cutDistance(shape, p)) : d;
}
function cutDistance(shape, p) {
  if (!Array.isArray(shape.cut)) return sdf(shape.cut, p);
  let best = BIG;
  for (const cut2 of shape.cut) best = Math.min(best, sdf(cut2, p));
  return best;
}
function baseSdf(shape, p) {
  if (shape.kind === "body") {
    const { F } = shape;
    const q = sub3(p, F.o);
    const s = dot3(q, F.a);
    const x = dot3(q, F.u);
    const y = dot3(q, F.v);
    return polyDistance(shape.poly, s, Math.hypot(x, y));
  }
  if (shape.kind === "ball") {
    let d = len3(sub3(p, shape.o)) - shape.r;
    if (shape.flats) for (const [nx, ny, nz, cut2] of shape.flats) d = Math.max(d, nx * (p[0] - shape.o[0]) + ny * (p[1] - shape.o[1]) + nz * (p[2] - shape.o[2]) - cut2);
    return d;
  }
  if (shape.kind === "prism") {
    const { F } = shape;
    const q = sub3(p, F.o);
    const s = dot3(q, F.a);
    const flat = polygonDistance(shape.poly, dot3(q, F.u), dot3(q, F.v));
    const along = Math.max(shape.s0 - s, s - shape.s1);
    return Math.hypot(Math.max(flat, 0), Math.max(along, 0)) + Math.min(Math.max(flat, along), 0);
  }
  if (shape.kind === "box") {
    const q = sub3(p, shape.o);
    const d = shape.axes.map((axis, index) => Math.abs(dot3(q, axis)) - shape.half[index]);
    const outside = Math.hypot(Math.max(d[0], 0), Math.max(d[1], 0), Math.max(d[2], 0));
    return outside + Math.min(Math.max(d[0], d[1], d[2]), 0);
  }
  const { points, radii, round: round2 } = shape;
  let best = BIG;
  const last = points.length - 1;
  for (let index = 0; index < last; index++) {
    const d = cappedSegment(p, points[index], points[index + 1], radii[index], radii[index + 1]);
    if (d < best) best = d;
  }
  if (round2[0]) best = Math.min(best, len3(sub3(p, points[0])) - radii[0]);
  if (round2[1]) best = Math.min(best, len3(sub3(p, points[last])) - radii[last]);
  return best;
}
function boundsOf(shape) {
  if (shape._b) return shape._b;
  let min;
  let max2;
  if (shape.kind === "body") {
    const { F, poly } = shape;
    const s0 = Math.min(...poly.map(([s]) => s));
    const s1 = Math.max(...poly.map(([s]) => s));
    const rm = Math.max(...poly.map(([, r]) => r));
    const a = add3(F.o, mul3(F.a, s0));
    const b = add3(F.o, mul3(F.a, s1));
    const spread2 = [0, 1, 2].map((i) => rm * Math.sqrt(Math.max(0, 1 - F.a[i] * F.a[i])));
    min = [0, 1, 2].map((i) => Math.min(a[i], b[i]) - spread2[i]);
    max2 = [0, 1, 2].map((i) => Math.max(a[i], b[i]) + spread2[i]);
  } else if (shape.kind === "ball") {
    min = shape.o.map((v) => v - shape.r);
    max2 = shape.o.map((v) => v + shape.r);
  } else if (shape.kind === "prism") {
    const { F } = shape;
    min = [BIG, BIG, BIG];
    max2 = [-BIG, -BIG, -BIG];
    for (const s of [shape.s0, shape.s1])
      for (const [x, y] of shape.poly) {
        const p = add3(add3(F.o, mul3(F.a, s)), add3(mul3(F.u, x), mul3(F.v, y)));
        for (let i = 0; i < 3; i++) min[i] = Math.min(min[i], p[i]), max2[i] = Math.max(max2[i], p[i]);
      }
  } else if (shape.kind === "box") {
    const extent = [0, 1, 2].map((i) => shape.axes.reduce((sum, axis, j) => sum + Math.abs(axis[i]) * shape.half[j], 0));
    min = shape.o.map((v, i) => v - extent[i]);
    max2 = shape.o.map((v, i) => v + extent[i]);
  } else {
    min = [BIG, BIG, BIG];
    max2 = [-BIG, -BIG, -BIG];
    shape.points.forEach((p, index) => {
      for (let i = 0; i < 3; i++) {
        min[i] = Math.min(min[i], p[i] - shape.radii[index]);
        max2[i] = Math.max(max2[i], p[i] + shape.radii[index]);
      }
    });
  }
  shape._b = { min, max: max2 };
  return shape._b;
}
function cameraBasis(P) {
  const { sinA, cosA, sinE, cosE, k } = cameraOf(P);
  return { R: [sinA, -cosA, 0], D: [cosA * sinE, sinA * sinE, -cosE], V: [cosA * cosE, sinA * cosE, sinE], k, origin: P.origin };
}
function screenBox(shape, cam, offset) {
  const { min, max: max2 } = boundsOf(shape);
  let x0 = BIG;
  let y0 = BIG;
  let x1 = -BIG;
  let y1 = -BIG;
  const visit = (p) => {
    const x = cam.origin[0] + dot3(p, cam.R) * cam.k;
    const y = cam.origin[1] + dot3(p, cam.D) * cam.k;
    x0 = Math.min(x0, x);
    y0 = Math.min(y0, y);
    x1 = Math.max(x1, x);
    y1 = Math.max(y1, y);
  };
  if (shape.kind === "tube") {
    shape.points.forEach((p, index) => {
      const r = shape.radii[index];
      const q = add3(p, offset);
      visit(add3(q, mul3(cam.R, r)));
      visit(add3(q, mul3(cam.R, -r)));
      visit(add3(q, mul3(cam.D, r)));
      visit(add3(q, mul3(cam.D, -r)));
    });
  } else {
    for (const x of [min[0], max2[0]]) for (const y of [min[1], max2[1]]) for (const z of [min[2], max2[2]]) visit(add3([x, y, z], offset));
  }
  return [x0, y0, x1, y1];
}
function spanOf(c, V, min, max2) {
  let t0 = -BIG;
  let t1 = BIG;
  for (let i = 0; i < 3; i++) {
    if (Math.abs(V[i]) < 1e-12) {
      if (c[i] < min[i] || c[i] > max2[i]) return null;
      continue;
    }
    let a = (min[i] - c[i]) / V[i];
    let b = (max2[i] - c[i]) / V[i];
    if (a > b) [a, b] = [b, a];
    t0 = Math.max(t0, a);
    t1 = Math.min(t1, b);
  }
  return t0 <= t1 ? [t0, t1] : null;
}
function tubeDistance(shape, p, segments) {
  const { points, radii, round: round2 } = shape;
  const last = points.length - 1;
  let best = BIG;
  for (const index of segments) {
    const d = cappedSegment(p, points[index], points[index + 1], radii[index], radii[index + 1]);
    if (d < best) best = d;
    for (const [joint, flag] of [[0, round2[0]], [last, round2[1]]]) {
      if (!flag || joint !== index && joint !== index + 1) continue;
      const q = points[joint];
      const e = Math.hypot(p[0] - q[0], p[1] - q[1], p[2] - q[2]) - radii[joint];
      if (e < best) best = e;
    }
  }
  return best;
}
function bodyDepth(shape, c, V, eps) {
  const { F, poly } = shape;
  if (!shape._f || shape._f.view.some((value, index) => value !== V[index])) {
    const s = poly.map(([value]) => value);
    shape._f = { view: [...V], aV: dot3(F.a, V), uV: dot3(F.u, V), vV: dot3(F.v, V), s0: Math.min(...s), s1: Math.max(...s), rm: Math.max(...poly.map(([, r]) => r)) };
  }
  const { aV, uV, vV, s0, s1, rm } = shape._f;
  const q = [c[0] - F.o[0], c[1] - F.o[1], c[2] - F.o[2]];
  const sc = dot3(q, F.a);
  const xc = dot3(q, F.u);
  const yc = dot3(q, F.v);
  let lo = -BIG;
  let hi = BIG;
  if (Math.abs(aV) > 1e-9) {
    const a = (s0 - sc) / aV;
    const b = (s1 - sc) / aV;
    lo = Math.min(a, b);
    hi = Math.max(a, b);
  } else if (sc < s0 || sc > s1) return null;
  const qa = uV * uV + vV * vV;
  if (qa > 1e-12) {
    const qb = 2 * (xc * uV + yc * vV);
    const qc = xc * xc + yc * yc - rm * rm;
    const disc = qb * qb - 4 * qa * qc;
    if (disc < 0) return null;
    const root = Math.sqrt(disc);
    lo = Math.max(lo, (-qb - root) / (2 * qa));
    hi = Math.min(hi, (-qb + root) / (2 * qa));
  } else if (xc * xc + yc * yc > rm * rm) return null;
  if (lo > hi) return null;
  let t = hi + eps;
  for (let step = 0; step < 160 && t >= lo - eps; step++) {
    let d = polyDistance(poly, sc + t * aV, Math.hypot(xc + t * uV, yc + t * vV));
    if (shape.cut) d = Math.max(d, -cutDistance(shape, [c[0] + V[0] * t, c[1] + V[1] * t, c[2] + V[2] * t]));
    if (d < eps) return t;
    t -= Math.max(d, eps * 0.5);
  }
  return null;
}
function rayDepth(shape, c, V, eps, segments) {
  if (shape.kind === "body") return bodyDepth(shape, c, V, eps);
  const span = spanOf(c, V, boundsOf(shape).min, boundsOf(shape).max);
  if (!span) return null;
  let t = span[1] + eps;
  for (let step = 0; step < 160 && t >= span[0] - eps; step++) {
    const p = [c[0] + V[0] * t, c[1] + V[1] * t, c[2] + V[2] * t];
    const d = segments ? tubeDistance(shape, p, segments) : sdf(shape, p);
    if (d < eps) return t;
    t -= Math.max(d, eps * 0.5);
  }
  return null;
}
function flatDistance(x, y, a, b) {
  const dx = b[0] - a[0];
  const dy = b[1] - a[1];
  const span = dx * dx + dy * dy;
  const t = span > 0 ? Math.max(0, Math.min(1, ((x - a[0]) * dx + (y - a[1]) * dy) / span)) : 0;
  return Math.hypot(x - a[0] - dx * t, y - a[1] - dy * t);
}
var shareOf = (item, state) => typeof state === "number" ? state : state.shares[item.ride ?? item.piece] ?? 0;
var offsetOf = (item, state) => mul3(item.move ?? [0, 0, 0], shareOf(item, state));
var labelOf = (state) => typeof state === "number" ? `share ${Math.round(state * 1e3) / 1e3}` : state.label;
function springStates(order, { stagger = 0.035, stiffness = 64, damping = 14.2, substeps = 4, fps = 60, settle: settle2 = 1e-3, stride = 1, reversals = [] } = {}) {
  const out2 = [];
  const scripts = [[true], [false], ...reversals.flatMap((at) => [[true, at], [false, at]])];
  for (const [on, back2] of scripts) {
    const springs = Object.fromEntries(order.map((id) => [id, { x: on ? 0 : 1, v: 0, target: on ? 0 : 1, pending: null }]));
    const toggle = (value, clock2) => {
      const goal2 = value ? 1 : 0;
      let index = 0;
      for (const id of value ? order : [...order].reverse()) {
        if (springs[id].target === goal2) springs[id].pending = null;
        else springs[id].pending = { value: goal2, at: clock2 + index++ * stagger };
      }
    };
    const name = back2 === void 0 ? on ? "apart" : "together" : `${on ? "apart" : "together"}, back at ${back2.toFixed(2)} s,`;
    const dt = 1 / fps;
    let clock = 0;
    let goal = on ? 1 : 0;
    toggle(on, 0);
    for (let frame = 0; frame < 1e5; frame++) {
      if (back2 !== void 0 && clock < back2 && clock + dt >= back2) toggle(!on, back2), goal = on ? 0 : 1;
      clock += dt;
      for (const spring of Object.values(springs)) {
        if (spring.pending && clock >= spring.pending.at) spring.target = spring.pending.value, spring.pending = null;
        for (let index = 0; index < substeps; index++) {
          const h = dt / substeps;
          spring.v += ((spring.target - spring.x) * stiffness - spring.v * damping) * h;
          spring.x += spring.v * h;
        }
      }
      const settled = (back2 === void 0 || clock >= back2) && Object.values(springs).every((spring) => !spring.pending && Math.abs(spring.x - goal) < settle2 && Math.abs(spring.v) < settle2);
      if (settled) break;
      if ((frame + 1) % stride === 0) out2.push({ label: `${name} ${clock.toFixed(3)} s`, shares: Object.fromEntries(Object.entries(springs).map(([id, spring]) => [id, spring.x])) });
    }
  }
  return out2;
}
var uniformStates = (count = 10) => Array.from({ length: count + 1 }, (_, index) => index / count);
var reversalsOf = (order, stagger = 0.035, margin = 8e-3) => order.flatMap((_, index) => [index * stagger - margin, index * stagger + margin]).filter((at) => at > 0);
function prefixStates(order, { shares = [0.25, 0.5, 0.75, 1] } = {}) {
  const out2 = [];
  for (let count = 1; count < order.length; count++)
    for (const s of shares)
      out2.push({ label: `first ${count - 1} out, ${order[count - 1]} at ${s}`, shares: Object.fromEntries(order.map((id, index) => [id, index < count - 1 ? 1 : index === count - 1 ? s : 0])) });
  return out2;
}
function rasterOf(item, cam, step, offset) {
  const shapes = item.shapes.map((shape) => moved(shape, offset));
  const flat = (p) => [cam.origin[0] + dot3(p, cam.R) * cam.k, cam.origin[1] + dot3(p, cam.D) * cam.k];
  const boxes = shapes.map((shape) => screenBox(shape, cam, [0, 0, 0]));
  const guides = shapes.map((shape) => {
    if (shape.kind === "tube") {
      const points = shape.points.map(flat);
      const widths = shape.radii.map((r) => r * cam.k);
      const boxes2 = new Float64Array((points.length - 1) * 4);
      for (let i = 0; i < points.length - 1; i++) {
        const pad = Math.max(widths[i], widths[i + 1]) + step * 0.5;
        boxes2[i * 4] = Math.min(points[i][0], points[i + 1][0]) - pad;
        boxes2[i * 4 + 1] = Math.max(points[i][0], points[i + 1][0]) + pad;
        boxes2[i * 4 + 2] = Math.min(points[i][1], points[i + 1][1]) - pad;
        boxes2[i * 4 + 3] = Math.max(points[i][1], points[i + 1][1]) + pad;
      }
      return { points, widths, boxes: boxes2 };
    }
    if (shape.kind === "body") {
      const s = shape.poly.map(([value]) => value);
      return { axis: [flat(add3(shape.F.o, mul3(shape.F.a, Math.min(...s)))), flat(add3(shape.F.o, mul3(shape.F.a, Math.max(...s))))], reach: Math.max(...shape.poly.map(([, r]) => r)) * cam.k };
    }
    return null;
  });
  const x0 = Math.floor(Math.min(...boxes.map((b) => b[0])) / step);
  const y0 = Math.floor(Math.min(...boxes.map((b) => b[1])) / step);
  const x1 = Math.ceil(Math.max(...boxes.map((b) => b[2])) / step);
  const y1 = Math.ceil(Math.max(...boxes.map((b) => b[3])) / step);
  const w = x1 - x0 + 1;
  const h = y1 - y0 + 1;
  return { x0, y0, x1, y1, w, h, boxes, shapes, guides, depth: null };
}
function depthAt(raster, cam, step, cx, cy) {
  if (!raster.depth) {
    raster.depth = new Float32Array(raster.w * raster.h);
    raster.done = new Uint8Array(raster.w * raster.h);
  }
  const cell = (cy - raster.y0) * raster.w + (cx - raster.x0);
  if (raster.done[cell]) return raster.depth[cell];
  const x = cx * step;
  const y = cy * step;
  const c = add3(mul3(cam.R, (x - cam.origin[0]) / cam.k), mul3(cam.D, (y - cam.origin[1]) / cam.k));
  let best = NaN;
  for (let index = 0; index < raster.shapes.length; index++) {
    const shape = raster.shapes[index];
    const b = raster.boxes[index];
    if (x < b[0] || x > b[2] || y < b[1] || y > b[3]) continue;
    const guide = raster.guides[index];
    let segments = null;
    if (shape.kind === "tube") {
      segments = [];
      const boxes = guide.boxes;
      for (let i = 0; i < guide.points.length - 1; i++) {
        if (x < boxes[i * 4] || x > boxes[i * 4 + 1] || y < boxes[i * 4 + 2] || y > boxes[i * 4 + 3]) continue;
        if (flatDistance(x, y, guide.points[i], guide.points[i + 1]) <= Math.max(guide.widths[i], guide.widths[i + 1]) + step * 0.5) segments.push(i);
      }
      if (!segments.length) continue;
    } else if (shape.kind === "body" && flatDistance(x, y, guide.axis[0], guide.axis[1]) > guide.reach + step) continue;
    const t = rayDepth(shape, c, cam.V, 0.02, segments);
    if (t !== null && !(t <= best)) best = t;
  }
  raster.depth[cell] = best;
  raster.done[cell] = 1;
  return best;
}
function regionOf(flags, gw, gh, value, step) {
  const n = gw * gh;
  const on = new Uint8Array(n);
  let all = 0;
  let inner = 0;
  for (let cell = 0; cell < n; cell++) if (flags[cell] === value) on[cell] = 1, all++;
  if (!all) return { all, inner, area: 0 };
  const grow = new Uint8Array(n);
  for (let y = 0; y < gh; y++)
    for (let x = 0; x < gw; x++) {
      const cell = y * gw + x;
      if (on[cell] && x > 0 && x < gw - 1 && y > 0 && y < gh - 1 && on[cell - 1] && on[cell + 1] && on[cell - gw] && on[cell + gw]) inner++;
      if (on[cell] || x > 0 && on[cell - 1] || x < gw - 1 && on[cell + 1] || y > 0 && on[cell - gw] || y < gh - 1 && on[cell + gw]) grow[cell] = 1;
    }
  const shut = new Uint8Array(n);
  for (let y = 0; y < gh; y++)
    for (let x = 0; x < gw; x++) {
      const cell = y * gw + x;
      shut[cell] = on[cell] || grow[cell] && (x === 0 || grow[cell - 1]) && (x === gw - 1 || grow[cell + 1]) && (y === 0 || grow[cell - gw]) && (y === gh - 1 || grow[cell + gw]) ? 1 : 0;
    }
  const core = new Uint8Array(n);
  for (let y = 1; y < gh - 1; y++)
    for (let x = 1; x < gw - 1; x++) {
      const cell = y * gw + x;
      core[cell] = shut[cell] && shut[cell - 1] && shut[cell + 1] && shut[cell - gw] && shut[cell + gw] ? 1 : 0;
    }
  const seen = new Uint8Array(n);
  const stack = new Int32Array(n);
  let largest = 0;
  for (let start = 0; start < n; start++) {
    if (!core[start] || seen[start]) continue;
    let top = 0;
    let size = 0;
    stack[top++] = start;
    seen[start] = 1;
    while (top) {
      const cell = stack[--top];
      size++;
      const x = cell % gw;
      const y = (cell - x) / gw;
      const visit = (next) => {
        if (core[next] && !seen[next]) seen[next] = 1, stack[top++] = next;
      };
      if (x > 0) visit(cell - 1);
      if (x < gw - 1) visit(cell + 1);
      if (y > 0) visit(cell - gw);
      if (y < gh - 1) visit(cell + gw);
    }
    if (size > largest) largest = size;
  }
  return { all, inner, area: largest * step * step };
}
function measure(ra, rb, dx, dy, dz, cam, step, tolerance, least) {
  if (ra.x1 < rb.x0 + dx || rb.x1 + dx < ra.x0 || ra.y1 < rb.y0 + dy || rb.y1 + dy < ra.y0) return null;
  const ix0 = Math.max(ra.x0, rb.x0 + dx);
  const ix1 = Math.min(ra.x1, rb.x1 + dx);
  const iy0 = Math.max(ra.y0, rb.y0 + dy);
  const iy1 = Math.min(ra.y1, rb.y1 + dy);
  const gw = ix1 - ix0 + 1;
  const gh = iy1 - iy0 + 1;
  const flags = new Int8Array(gw * gh);
  const worst = [0, 0];
  const at = [null, null];
  let any = false;
  for (let y = iy0; y <= iy1; y++) {
    for (let x = ix0; x <= ix1; x++) {
      const ta = depthAt(ra, cam, step, x, y);
      if (Number.isNaN(ta)) continue;
      const tb = depthAt(rb, cam, step, x - dx, y - dy) + dz;
      if (Number.isNaN(tb)) continue;
      const cell = (y - iy0) * gw + (x - ix0);
      if (ta > tb + tolerance) {
        flags[cell] = 1;
        any = true;
        if (ta - tb > worst[0]) worst[0] = ta - tb, at[0] = [x * step, y * step];
      } else if (tb > ta + tolerance) {
        flags[cell] = -1;
        any = true;
        if (tb - ta > worst[1]) worst[1] = tb - ta, at[1] = [x * step, y * step];
      }
    }
  }
  if (!any) return null;
  const front = [regionOf(flags, gw, gh, 1, step), regionOf(flags, gw, gh, -1, step)];
  if (front[0].area < least && front[1].area < least) return null;
  return front.map((region, side) => ({ ...region, depth: worst[side], at: at[side] }));
}
function overlapsOf(items, P, { step = 0.25, tolerance = 0.3, least = 0.25, states = [0], skip = () => false } = {}) {
  const cam = cameraBasis(P);
  const live = items.map((item, index) => ({ item, index })).filter(({ item }) => item.shapes && item.shapes.length);
  const homes = live.map(() => null);
  let uid = 0;
  const stamp = (raster) => Object.assign(raster, { uid: uid++ });
  const home = (index) => homes[index] ?? (homes[index] = stamp(rasterOf(live[index].item, cam, step, [0, 0, 0])));
  const sliding = live.map(({ item }) => item.shapes.some((shape) => shape.slide));
  const slid = /* @__PURE__ */ new Map();
  const rasterAt = (index, offset) => {
    if (!sliding[index]) return home(index);
    const id = `${index}|${offset.map((v) => v.toFixed(2)).join(",")}`;
    if (!slid.has(id)) slid.set(id, stamp(rasterOf(live[index].item, cam, step, offset)));
    return slid.get(id);
  };
  const shiftOf = (offset) => ({ gx: Math.round(dot3(offset, cam.R) * cam.k / step), gy: Math.round(dot3(offset, cam.D) * cam.k / step), dz: dot3(offset, cam.V) });
  const memo = /* @__PURE__ */ new Map();
  const pairs = [];
  for (const state of states) {
    const offsets = live.map(({ item }) => offsetOf(item, state));
    const shifts = live.map((_, index) => sliding[index] ? { gx: 0, gy: 0, dz: 0 } : shiftOf(offsets[index]));
    for (let a = 0; a < live.length; a++) {
      const ra = rasterAt(a, offsets[a]);
      const sa = shifts[a];
      for (let b = a + 1; b < live.length; b++) {
        const rb = rasterAt(b, offsets[b]);
        const sb = shifts[b];
        if (ra.x1 + sa.gx < rb.x0 + sb.gx || rb.x1 + sb.gx < ra.x0 + sa.gx || ra.y1 + sa.gy < rb.y0 + sb.gy || rb.y1 + sb.gy < ra.y0 + sa.gy) continue;
        if (skip(live[a].item, live[b].item)) continue;
        const dx = sb.gx - sa.gx;
        const dy = sb.gy - sa.gy;
        const dz = sb.dz - sa.dz;
        const id = `${ra.uid}|${rb.uid}|${dx},${dy},${dz.toFixed(3)}`;
        let hit = memo.get(id);
        if (hit === void 0) {
          hit = measure(ra, rb, dx, dy, dz, cam, step, tolerance, least);
          memo.set(id, hit);
        }
        if (!hit) continue;
        pairs.push({ state, a: live[a].index, b: live[b].index, front: hit.map((side) => ({ ...side, at: side.at && [side.at[0] + sa.gx * step, side.at[1] + sa.gy * step] })) });
      }
    }
  }
  return { pairs, least, states, step, V: cam.V };
}
var liftOf = (item, V) => dot3(item.move ?? [0, 0, 0], V);
var keyAt = (item, state, V) => item.key + liftOf(item, V) * shareOf(item, state);
function orderKeys(items, overlaps2, { gap = 0.02, rounds = 0 } = {}) {
  const { pairs, least, V } = overlaps2;
  const start = items.map((item) => item.key);
  const strongest = /* @__PURE__ */ new Map();
  const cycles = [];
  for (const pair of pairs) {
    const aFront = pair.front[0].area >= least;
    const bFront = pair.front[1].area >= least;
    if (aFront && bFront) {
      cycles.push(pair);
      continue;
    }
    const [front, back2] = aFront ? [pair.a, pair.b] : [pair.b, pair.a];
    const weight = pair.front[aFront ? 0 : 1].area;
    const need2 = gap + shareOf(items[back2], pair.state) * liftOf(items[back2], V) - shareOf(items[front], pair.state) * liftOf(items[front], V);
    const id = `${front}|${back2}`;
    const prior = strongest.get(id);
    if (!prior) strongest.set(id, { front, back: back2, weight, pair, need: need2 });
    else {
      prior.weight = Math.max(prior.weight, weight);
      if (need2 > prior.need) prior.need = need2, prior.pair = pair;
    }
  }
  const rules = [...strongest.values()];
  const limit = rounds || items.length + 1;
  const dropped = [];
  let keys = start.slice();
  let active = rules.slice();
  for (let attempt = 0; attempt < 400; attempt++) {
    keys = start.slice();
    const by = new Array(items.length).fill(null);
    let changed = true;
    let round2 = 0;
    let last = -1;
    for (; changed && round2 < limit; round2++) {
      changed = false;
      for (const rule of active) {
        if (keys[rule.front] - keys[rule.back] >= rule.need - 1e-9) continue;
        keys[rule.front] = keys[rule.back] + rule.need;
        by[rule.front] = rule;
        last = rule.front;
        changed = true;
      }
    }
    if (!changed) break;
    const seen = /* @__PURE__ */ new Map();
    let node = last;
    let step = 0;
    while (node !== -1 && by[node] && !seen.has(node) && step < items.length * 2) {
      seen.set(node, step++);
      node = by[node].back;
    }
    const loop = [];
    if (node !== -1 && seen.has(node)) {
      let walk = node;
      do {
        loop.push(by[walk]);
        walk = by[walk].back;
      } while (walk !== node && loop.length <= items.length);
    }
    const candidates = loop.length ? loop : active.filter((rule) => keys[rule.front] - keys[rule.back] < rule.need - 1e-9);
    if (!candidates.length) break;
    const victim = candidates.reduce((low, rule) => rule.weight < low.weight ? rule : low);
    dropped.push(victim);
    active = active.filter((rule) => rule !== victim);
  }
  return { keys, rules: rules.length, cycles, dropped };
}
function depthOrder(items, P, options2 = {}) {
  const overlaps2 = options2.overlaps ?? overlapsOf(items, P, options2);
  const { pairs, least, states, V } = overlaps2;
  const allow = options2.allow ?? [];
  const dropped = new Set((options2.solved?.dropped ?? []).map((rule) => `${rule.front}|${rule.back}`));
  const missing = items.filter((item) => !item.shapes || !item.shapes.length).map((item) => item.name);
  const ranks = /* @__PURE__ */ new Map();
  for (const state of states) {
    const order = items.map((item, index) => ({ index, key: keyAt(item, state, V) })).sort((x, y) => x.key - y.key || x.index - y.index);
    const rank = new Int32Array(items.length);
    order.forEach(({ index }, position) => rank[index] = position);
    ranks.set(state, rank);
  }
  const rest = options2.rest ?? states.filter((state) => state === 0 || state === 1);
  const problems = [];
  const passing = [];
  for (const pair of pairs) {
    const rank = ranks.get(pair.state);
    const aFirst = rank[pair.a] < rank[pair.b];
    const wrong = pair.front[aFirst ? 0 : 1];
    const right = pair.front[aFirst ? 1 : 0];
    if (wrong.area < least) continue;
    const front = items[aFirst ? pair.a : pair.b];
    const back2 = items[aFirst ? pair.b : pair.a];
    const excused = allow.find(([x, y]) => matches([x], front.name) && matches([y], back2.name) || matches([y], front.name) && matches([x], back2.name));
    const entry = {
      state: pair.state,
      label: labelOf(pair.state),
      front: front.name,
      back: back2.name,
      frontKey: keyAt(front, pair.state, V),
      backKey: keyAt(back2, pair.state, V),
      cells: wrong.all,
      area: wrong.area,
      against: right.area,
      cycle: right.area >= least,
      depth: wrong.depth,
      at: wrong.at
    };
    const front_ = aFirst ? pair.a : pair.b;
    const back_ = aFirst ? pair.b : pair.a;
    entry.unorderable = !rest.includes(pair.state) && dropped.has(`${front_}|${back_}`);
    const replayed = typeof pair.state !== "number";
    (!excused && (rest.includes(pair.state) || replayed || !entry.cycle && !entry.unorderable) ? problems : passing).push(entry);
  }
  return { problems, passing, missing };
}
function samplesOf(shape, spacing) {
  const dense = resample(shape.points, spacing);
  const total = pathLength(shape.points) || 1;
  const lengths = [0];
  for (let index = 1; index < shape.points.length; index++) lengths.push(lengths[index - 1] + len3(sub3(shape.points[index], shape.points[index - 1])));
  const radiusAt = (at) => {
    let index = 1;
    while (index < lengths.length - 1 && lengths[index] < at) index++;
    const span = lengths[index] - lengths[index - 1] || 1;
    const t = Math.max(0, Math.min(1, (at - lengths[index - 1]) / span));
    return shape.radii[index - 1] + (shape.radii[index] - shape.radii[index - 1]) * t;
  };
  const step = total / Math.max(1, dense.length - 1);
  return dense.map((p, index) => {
    const t = unit3(sub3(dense[Math.min(dense.length - 1, index + 1)], dense[Math.max(0, index - 1)]));
    return { p, t, along: index * step, edge: Math.min(index * step, total - index * step), r: radiusAt(index * step) };
  });
}
var overlaps = (a, b, pad) => a.min.every((v, i) => v - pad <= b.max[i] && b.min[i] - pad <= a.max[i]);
function centreline(shape, p) {
  let best = { d: BIG, r: 0 };
  for (let index = 0; index < shape.points.length - 1; index++) {
    const { d, t } = segmentPoint(p, shape.points[index], shape.points[index + 1]);
    if (d < best.d) best = { d, r: shape.radii[index] + (shape.radii[index + 1] - shape.radii[index]) * t };
  }
  return best;
}
var matches = (list, name) => (list ?? []).some((entry) => {
  if (typeof entry === "function") return entry(name);
  if (entry.endsWith("*")) return name.startsWith(entry.slice(0, -1));
  return name === entry || name.startsWith(entry + ".") || name.startsWith(entry + ":") || name.startsWith(entry + "#");
});
var sameOffset = (a, b) => Math.abs(a[0] - b[0]) + Math.abs(a[1] - b[1]) + Math.abs(a[2] - b[2]) < 1e-6;
var placed = (shape, state) => state === void 0 || !shape.move ? shape : moved(shape, offsetOf(shape, state));
var offsetAt = (shape, state) => state === void 0 || !shape.move ? [0, 0, 0] : offsetOf(shape, state);
function tipDistance(other, p) {
  if (other.kind === "tube") {
    const { d, r } = centreline(other, p);
    return d - r;
  }
  return sdf(other, p);
}
function rimOf(tube2, index) {
  const tip = tube2.tips[index];
  const axis = tube2.tipAxes ? tube2.tipAxes[index] : unit3(index ? sub3(tube2.points[tube2.points.length - 1], tube2.points[tube2.points.length - 2]) : sub3(tube2.points[1], tube2.points[0]));
  const radius = tube2.tipRims ? tube2.tipRims[index] : tube2.radii[index ? tube2.radii.length - 1 : 0];
  const helper = Math.abs(axis[2]) > 0.9 ? [1, 0, 0] : [0, 0, 1];
  const u = unit3([helper[1] * axis[2] - helper[2] * axis[1], helper[2] * axis[0] - helper[0] * axis[2], helper[0] * axis[1] - helper[1] * axis[0]]);
  const v = [axis[1] * u[2] - axis[2] * u[1], axis[2] * u[0] - axis[0] * u[2], axis[0] * u[1] - axis[1] * u[0]];
  return Array.from({ length: 12 }, (_, k) => add3(tip, add3(mul3(u, radius * Math.cos(k * Math.PI / 6)), mul3(v, radius * Math.sin(k * Math.PI / 6)))));
}
function mountsOf(tubes, solids, { tolerance = 0.15 } = {}) {
  const byName = new Map(tubes.map((tube2) => [tube2.name, tube2]));
  const out2 = /* @__PURE__ */ new Map();
  for (const tube2 of tubes) {
    const found = [null, null];
    (tube2.tips ?? []).forEach((tip, index) => {
      if (!tip) return;
      const rim = rimOf(tube2, index);
      let best = null;
      const consider = (other) => {
        if (other === tube2 || other.owner && other.owner === tube2.owner || other.name === tube2.owner || other.anchor === false) return;
        const { min, max: max2 } = boundsOf(other);
        if (!overlaps({ min: tip, max: tip }, { min, max: max2 }, 3 + (tube2.tipRims ? tube2.tipRims[index] : 0))) return;
        const ds = rim.map((p) => tipDistance(other, p));
        const score = (Math.abs(tipDistance(other, tip)) + ds.reduce((sum, d) => sum + Math.abs(d), 0) / ds.length) / 2;
        if (!best || score < best.score) best = { shape: other, score, d: tipDistance(other, tip), high: Math.max(...ds), low: Math.min(...ds) };
      };
      solids.forEach(consider);
      tubes.forEach(consider);
      if (best && byName.get(best.shape.owner) && best.shape.kind !== "tube") best.host = byName.get(best.shape.owner);
      found[index] = best && { ...best, tip, landed: best.high <= tolerance && best.low >= -tolerance };
    });
    out2.set(tube2, found);
  }
  return out2;
}
function ringAround(sample, r) {
  const axis = sample.t;
  const helper = Math.abs(axis[2]) > 0.9 ? [1, 0, 0] : [0, 0, 1];
  const u = unit3([helper[1] * axis[2] - helper[2] * axis[1], helper[2] * axis[0] - helper[0] * axis[2], helper[0] * axis[1] - helper[1] * axis[0]]);
  const v = [axis[1] * u[2] - axis[2] * u[1], axis[2] * u[0] - axis[0] * u[2], axis[0] * u[1] - axis[1] * u[0]];
  return Array.from({ length: 12 }, (_, k) => add3(sample.p, add3(mul3(u, r * Math.cos(k * Math.PI / 6)), mul3(v, r * Math.sin(k * Math.PI / 6)))));
}
function clearances(tubes, solids, { ratio = 0.5, least = 0.2, spacing = 0.5, touching = -0.05, through = -0.1, state, only, mounts = mountsOf(tubes, solids) } = {}) {
  const gapOf = (r) => Math.max(least, ratio * r);
  const problems = /* @__PURE__ */ new Map();
  const note = (tube2, other, kind, clearance, need2, sample) => {
    if (only && kind !== only) return;
    const id = `${tube2.name}|${other.name}`;
    const prior = problems.get(id);
    if (prior && prior.clearance <= clearance) {
      prior.from = Math.min(prior.from, sample.along);
      prior.to = Math.max(prior.to, sample.along);
      return;
    }
    problems.set(id, { tube: tube2.name, other: other.name, kind, clearance, need: need2, at: sample.p, from: prior ? Math.min(prior.from, sample.along) : sample.along, to: prior ? Math.max(prior.to, sample.along) : sample.along, length: pathLength(tube2.points), state: state === void 0 ? "" : labelOf(state) });
  };
  const poseOf = new Map([...tubes, ...solids].map((shape) => [shape, placed(shape, state)]));
  const offsets = new Map([...tubes, ...solids].map((shape) => [shape, offsetAt(shape, state)]));
  const widest = new Map(tubes.map((tube2) => [tube2, poseOf.get(tube2).radii.reduce((r, next) => Math.max(r, next), 0)]));
  const together = (a, b) => len3(sub3(offsets.get(a), offsets.get(b))) < 0.05;
  const runsBy = /* @__PURE__ */ new Map();
  for (const tube2 of tubes) runsBy.set(tube2.owner, [...runsBy.get(tube2.owner) ?? [], tube2]);
  const tipsOf = (owner) => (runsBy.get(owner) ?? []).flatMap((run3) => (mounts.get(run3) ?? []).filter(Boolean).map((mount) => ({ run: run3, mount })));
  const seatedOn2 = (shape, owner) => shape && shape.cut && [shape.cut].flat().some((cut2) => cut2.owner === owner);
  const zone = (r) => r + gapOf(r) + 1;
  const ownerOf = (other) => other.owner ?? other.name;
  const related = (tube2, other, sample) => {
    if (seatedOn2(other, tube2.owner)) return true;
    const tips = tipsOf(tube2.owner);
    const near = (entry) => len3(sub3(sample.p, add3(entry.mount.tip, offsets.get(entry.run)))) <= zone(sample.r) + (entry.run.tipRims ? Math.max(...entry.run.tipRims) : 0);
    for (const entry of tips) {
      if (!near(entry) || !together(tube2, entry.mount.shape)) continue;
      const mount = entry.mount.shape;
      if (mount === other || entry.mount.host && (entry.mount.host === other || other.owner === entry.mount.host.owner)) return true;
      if (tipsOf(ownerOf(other)).some((theirs) => theirs.mount.shape === mount)) return true;
    }
    for (const entry of tipsOf(ownerOf(other))) {
      const mount = entry.mount.shape;
      const lands = mount.owner === tube2.owner || seatedOn2(mount, tube2.owner);
      if (!lands || !together(entry.run, tube2)) continue;
      if (len3(sub3(sample.p, add3(entry.mount.tip, offsets.get(entry.run)))) <= zone(sample.r) + (entry.run.tipRims ? Math.max(...entry.run.tipRims) : 0) + sample.r) return true;
    }
    return false;
  };
  const nearTip = (tube2, sample) => {
    const at = (tube2.offset ?? 0) + sample.along;
    const total = tube2.total ?? pathLength(tube2.points);
    const tips = mounts.get(tube2) ?? [null, null];
    return tips[0] && at <= zone(sample.r) || tips[1] && total - at <= zone(sample.r);
  };
  const clearanceTo = (other, sample) => {
    if (sample.edge >= sample.r) return sdf(other, sample.p) - sample.r;
    return Math.min(...ringAround(sample, sample.r).map((q) => sdf(other, q)));
  };
  for (const tube2 of tubes) {
    const posed2 = poseOf.get(tube2);
    const samples = samplesOf(posed2, spacing);
    const tb = boundsOf(posed2);
    for (const shape of solids) {
      if (shape.owner && shape.owner === tube2.owner) continue;
      if (matches(tube2.touch, shape.name) || matches(shape.touch, tube2.name)) continue;
      const other = poseOf.get(shape);
      const ob = boundsOf(other);
      if (!overlaps(tb, ob, Math.max(4, gapOf(widest.get(tube2))))) continue;
      for (const sample of samples) {
        if (!overlaps({ min: sample.p, max: sample.p }, ob, sample.r + Math.max(3, gapOf(sample.r)))) continue;
        const gap = gapOf(sample.r);
        const clearance = clearanceTo(other, sample);
        if (clearance >= gap) continue;
        if (related(tube2, shape, sample)) continue;
        if (nearTip(tube2, sample) && clearance >= through) continue;
        note(tube2, shape, clearance < 0 ? "through" : "close", clearance, gap, sample);
      }
    }
  }
  for (let a = 0; a < tubes.length; a++) {
    const ta = poseOf.get(tubes[a]);
    const samples = samplesOf(ta, spacing);
    for (let b = 0; b < tubes.length; b++) {
      if (a === b) continue;
      const tb = poseOf.get(tubes[b]);
      if (tubes[a].owner && tubes[a].owner === tubes[b].owner && tubes[a].joined) continue;
      if (matches(tubes[a].touch, tubes[b].name) || matches(tubes[b].touch, tubes[a].name)) continue;
      const bundled = tubes[a].bundle && tubes[a].bundle === tubes[b].bundle;
      const widestB = widest.get(tubes[b]);
      const envelope = bundled ? 3 : Math.max(3, gapOf(Math.min(widest.get(tubes[a]), widestB)));
      if (!overlaps(boundsOf(ta), boundsOf(tb), envelope)) continue;
      for (const sample of samples) {
        const envelope2 = bundled ? 3 : Math.max(3, gapOf(Math.min(sample.r, widestB)));
        if (!overlaps({ min: sample.p, max: sample.p }, boundsOf(tb), sample.r + envelope2)) continue;
        const clearance = sample.edge >= sample.r ? sdf(tb, sample.p) - sample.r : Math.min(...ringAround(sample, sample.r).map((q) => sdf(tb, q)));
        const r = centreline(tb, sample.p).r;
        const gap = bundled ? touching : gapOf(Math.min(sample.r, r));
        if (clearance >= gap) continue;
        if (related(tubes[a], tubes[b], sample)) continue;
        if (nearTip(tubes[a], sample) && clearance >= through) continue;
        if (a > b && problems.has(`${tubes[b].name}|${tubes[a].name}`)) continue;
        note(tubes[a], tubes[b], clearance < 0 ? "through" : "close", clearance, gap, sample);
      }
    }
  }
  const seen = /* @__PURE__ */ new Set();
  return [...problems.values()].sort((x, y) => x.clearance - y.clearance).filter((c) => {
    const id = [c.tube, c.other].sort().join("|");
    if (seen.has(id)) return false;
    seen.add(id);
    return true;
  });
}
function terminals(tubes, solids, { tolerance = 0.15, mounts = mountsOf(tubes, solids, { tolerance }) } = {}) {
  const out2 = [];
  for (const tube2 of tubes) {
    (mounts.get(tube2) ?? []).forEach((mount, index) => {
      if (!tube2.tips || !tube2.tips[index] || mount && mount.landed) return;
      out2.push({ tube: tube2.name, end: index ? "end" : "start", at: tube2.tips[index], d: mount ? mount.d : Infinity, high: mount ? mount.high : Infinity, low: mount ? mount.low : -Infinity, nearest: mount ? mount.shape.name : "nothing" });
    });
  }
  return out2;
}
function looseEnds(tubes, solids, { state = 1, tolerance = 0.15 } = {}) {
  const out2 = [];
  for (const tube2 of tubes) {
    const offset = offsetAt(tube2, state);
    (tube2.tips ?? []).forEach((tip, index) => {
      if (!tip) return;
      const hit = solids.some((shape) => {
        if (shape.owner && shape.owner === tube2.owner || shape.name === tube2.owner) return false;
        if (!sameOffset(offsetAt(shape, state), offset)) return false;
        const { min, max: max2 } = boundsOf(shape);
        return overlaps({ min: tip, max: tip }, { min, max: max2 }, 1) && sdf(shape, tip) <= tolerance;
      });
      if (!hit) out2.push({ tube: tube2.name, end: index ? "end" : "start", at: add3(tip, offset), state: labelOf(state), free: Boolean(tube2.free && tube2.free[index]) });
    });
  }
  return out2;
}
function surfaceOf2(shape, spacing = 0.6) {
  const points = [];
  if (shape.kind === "body") {
    const { F, poly } = shape;
    const u = F.u ?? unit3(Math.abs(F.a[2]) > 0.9 ? [1, 0, 0] : [-F.a[1], F.a[0], 0]);
    const v = F.v ?? [F.a[1] * u[2] - F.a[2] * u[1], F.a[2] * u[0] - F.a[0] * u[2], F.a[0] * u[1] - F.a[1] * u[0]];
    for (let i = 0; i < poly.length - 1; i++) {
      const [s0, r0] = poly[i];
      const [s1, r1] = poly[i + 1];
      const steps = Math.max(1, Math.ceil(Math.hypot(s1 - s0, r1 - r0) / spacing));
      for (let j = 0; j <= steps; j++) {
        const s = s0 + (s1 - s0) * j / steps;
        const r = r0 + (r1 - r0) * j / steps;
        const around = Math.max(1, Math.min(160, Math.ceil(2 * Math.PI * r / spacing)));
        for (let k = 0; k < around; k++) {
          const t = k / around * 2 * Math.PI;
          points.push(add3(add3(F.o, mul3(F.a, s)), add3(mul3(u, r * Math.cos(t)), mul3(v, r * Math.sin(t)))));
        }
      }
    }
  } else if (shape.kind === "box") {
    for (let axis = 0; axis < 3; axis++)
      for (const sign of [-1, 1]) {
        const o1 = (axis + 1) % 3;
        const o2 = (axis + 2) % 3;
        const n1 = Math.max(1, Math.ceil(2 * shape.half[o1] / spacing));
        const n2 = Math.max(1, Math.ceil(2 * shape.half[o2] / spacing));
        for (let i = 0; i <= n1; i++)
          for (let j = 0; j <= n2; j++) {
            const c = [0, 0, 0];
            c[axis] = sign * shape.half[axis];
            c[o1] = -shape.half[o1] + 2 * shape.half[o1] * i / n1;
            c[o2] = -shape.half[o2] + 2 * shape.half[o2] * j / n2;
            points.push(add3(shape.o, add3(add3(mul3(shape.axes[0], c[0]), mul3(shape.axes[1], c[1])), mul3(shape.axes[2], c[2]))));
          }
      }
  } else if (shape.kind === "prism") {
    const { F, poly, s0, s1 } = shape;
    const at = (s, x, y) => add3(add3(F.o, mul3(F.a, s)), add3(mul3(F.u, x), mul3(F.v, y)));
    const rows = Math.max(1, Math.ceil((s1 - s0) / spacing));
    for (let i = 0, j = poly.length - 1; i < poly.length; j = i++) {
      const [x0, y0] = poly[j];
      const [x1, y1] = poly[i];
      const steps = Math.max(1, Math.ceil(Math.hypot(x1 - x0, y1 - y0) / spacing));
      for (let k = 0; k < steps; k++)
        for (let row = 0; row <= rows; row++) points.push(at(s0 + (s1 - s0) * row / rows, x0 + (x1 - x0) * k / steps, y0 + (y1 - y0) * k / steps));
    }
    const xs = poly.map(([x]) => x);
    const ys = poly.map(([, y]) => y);
    for (let x = Math.min(...xs); x <= Math.max(...xs); x += spacing)
      for (let y = Math.min(...ys); y <= Math.max(...ys); y += spacing) if (polygonDistance(poly, x, y) < 0) points.push(at(s0, x, y), at(s1, x, y));
  } else if (shape.kind === "ball") {
    const count = Math.max(24, Math.min(600, Math.ceil(4 * Math.PI * shape.r * shape.r / (spacing * spacing))));
    for (let i = 0; i < count; i++) {
      const z = 1 - 2 * (i + 0.5) / count;
      const ring = Math.sqrt(1 - z * z);
      const t = i * 2.399963;
      points.push(add3(shape.o, mul3([ring * Math.cos(t), ring * Math.sin(t), z], shape.r)));
    }
    if (shape.flats) {
      const kept = points.filter((p) => shape.flats.every(([nx, ny, nz, cut2]) => nx * (p[0] - shape.o[0]) + ny * (p[1] - shape.o[1]) + nz * (p[2] - shape.o[2]) <= cut2 + 1e-9));
      points.length = 0;
      points.push(...kept);
      for (const [nx, ny, nz, cut2] of shape.flats) {
        const n = [nx, ny, nz];
        const helper = Math.abs(nz) > 0.9 ? [1, 0, 0] : [0, 0, 1];
        const u = unit3([helper[1] * nz - helper[2] * ny, helper[2] * nx - helper[0] * nz, helper[0] * ny - helper[1] * nx]);
        const v = [ny * u[2] - nz * u[1], nz * u[0] - nx * u[2], nx * u[1] - ny * u[0]];
        const rho = Math.sqrt(Math.max(0, shape.r * shape.r - cut2 * cut2));
        const centre = add3(shape.o, mul3(n, cut2));
        for (let x = -rho; x <= rho; x += spacing)
          for (let y = -rho; y <= rho; y += spacing) {
            if (x * x + y * y > rho * rho) continue;
            const p = add3(centre, add3(mul3(u, x), mul3(v, y)));
            if (shape.flats.every(([mx, my, mz, other]) => mx * (p[0] - shape.o[0]) + my * (p[1] - shape.o[1]) + mz * (p[2] - shape.o[2]) <= other + 1e-6)) points.push(p);
          }
      }
    }
  } else {
    for (const sample of samplesOf(shape, spacing)) points.push(...ringAround(sample, sample.r));
  }
  return shape.cut ? points.filter((p) => cutDistance(shape, p) >= -1e-3) : points;
}
var seatedOn = (shape, host) => Boolean(shape.seated && shape.cut && [shape.cut].flat().some((cut2) => cut2 === host || cut2.name && cut2.name === host.name));
var grounded = (shape) => Boolean(shape.ground) || (shape.name ?? "").startsWith("stand.");
function supports(solids, tubes, { ground = grounded, touch = 0.15, sunk = 0.5 } = {}) {
  const nodes = [...solids, ...tubes.filter((tube2) => !tube2.limp)];
  const surfaces = nodes.map((shape) => surfaceOf2(shape));
  const links = nodes.map(() => []);
  const deep = [];
  for (let a = 0; a < nodes.length; a++) {
    const ba = boundsOf(nodes[a]);
    for (let b = a + 1; b < nodes.length; b++) {
      const bb = boundsOf(nodes[b]);
      if (!overlaps(ba, bb, touch + 0.05)) continue;
      const same = nodes[a].owner && (nodes[a].owner === nodes[b].owner || nodes[a].owner === nodes[b].name) || nodes[b].owner && nodes[b].owner === nodes[a].name;
      let gap = BIG;
      for (const p of surfaces[a]) gap = Math.min(gap, sdf(nodes[b], p));
      for (const p of surfaces[b]) gap = Math.min(gap, sdf(nodes[a], p));
      if (gap <= touch) links[a].push(b), links[b].push(a);
      const solidPair = nodes[a].kind !== "tube" && nodes[b].kind !== "tube";
      if (solidPair && !same && gap < -sunk && !seatedOn(nodes[a], nodes[b]) && !seatedOn(nodes[b], nodes[a])) deep.push({ a: nodes[a].name, b: nodes[b].name, depth: -gap });
    }
  }
  const held = new Uint8Array(nodes.length);
  const queue = [];
  nodes.forEach((shape, index) => ground(shape) && (held[index] = 1, queue.push(index)));
  while (queue.length) {
    const index = queue.pop();
    for (const next of links[index]) if (!held[next]) held[next] = 1, queue.push(next);
  }
  const loose = nodes.filter((_, index) => !held[index] && nodes[index].kind !== "tube").map((shape) => shape.name);
  const hanging = nodes.filter((_, index) => !held[index] && nodes[index].kind === "tube").map((shape) => shape.name);
  return { loose, hanging, sunk: deep.sort((x, y) => y.depth - x.depth) };
}
function folds(routes, P, { fold = 140, turn = 110, pinch = 2, items = null } = {}) {
  const cam = cameraBasis(P);
  const entries = items ? entriesOf(items, cam) : null;
  const shown = (name, p) => !entries || frontAt(entries, cam, cam.origin[0] + dot3(p, cam.R) * cam.k, cam.origin[1] + dot3(p, cam.D) * cam.k) === name;
  const flat = (p) => [dot3(p, cam.R) * cam.k, dot3(p, cam.D) * cam.k];
  const angle = (a, b) => Math.acos(Math.max(-1, Math.min(1, (a[0] * b[0] + a[1] * b[1]) / (Math.hypot(a[0], a[1]) * Math.hypot(b[0], b[1]) || 1)))) * 180 / Math.PI;
  const out2 = [];
  for (const { name, points, r } of routes) {
    const step = Math.max(0.25, r * 0.5);
    const dense = resample(points, step);
    const screen = dense.map(flat);
    const reach = Math.max(2, Math.round(4 * r / step));
    const width = r * cam.k;
    let worst = null;
    for (const span of [1.5, 3, 6]) {
      const near = Math.max(1, Math.round(span * r / step));
      for (let i = near; i < dense.length - near; i++) {
        const p0 = screen[i - near];
        const p1 = screen[i];
        const p2 = screen[i + near];
        const a = [p1[0] - p0[0], p1[1] - p0[1]];
        const b = [p2[0] - p1[0], p2[1] - p1[1]];
        const c = [p2[0] - p0[0], p2[1] - p0[1]];
        const la = Math.hypot(a[0], a[1]);
        const lb = Math.hypot(b[0], b[1]);
        if (la < width * 0.3 || lb < width * 0.3) continue;
        const bend = angle(a, b);
        const area = Math.abs(a[0] * b[1] - a[1] * b[0]) / 2;
        const radius = area > 1e-9 ? la * lb * Math.hypot(c[0], c[1]) / (4 * area) : Infinity;
        if (bend > 90 && radius < pinch * width && (!worst || radius < worst.radius) && shown(name, dense[i])) worst = { name, kind: "pinch", flatTurn: bend, radius, width, at: dense[i], index: i };
      }
    }
    if (worst) {
      let toStart = 0;
      for (let i = 1; i <= worst.index; i++) toStart += Math.hypot(screen[i][0] - screen[i - 1][0], screen[i][1] - screen[i - 1][1]);
      let toEnd = 0;
      for (let i = worst.index + 1; i < screen.length; i++) toEnd += Math.hypot(screen[i][0] - screen[i - 1][0], screen[i][1] - screen[i - 1][1]);
      if (Math.min(toStart, toEnd) > 3 * width) out2.push(worst);
    }
    for (let i = reach; i < dense.length - reach; i++) {
      const a = [screen[i][0] - screen[i - reach][0], screen[i][1] - screen[i - reach][1]];
      const b = [screen[i + reach][0] - screen[i][0], screen[i + reach][1] - screen[i][1]];
      if (Math.hypot(a[0], a[1]) < 1e-6 || Math.hypot(b[0], b[1]) < 1e-6) continue;
      const flatTurn = angle(a, b);
      const A3 = sub3(dense[i], dense[i - reach]);
      const B3 = sub3(dense[i + reach], dense[i]);
      const realTurn = Math.acos(Math.max(-1, Math.min(1, dot3(A3, B3) / (len3(A3) * len3(B3) || 1)))) * 180 / Math.PI;
      if (flatTurn > fold && realTurn < turn && shown(name, dense[i])) {
        out2.push({ name, kind: "fold", flatTurn, realTurn, at: dense[i] });
        i += 2 * reach;
      }
    }
  }
  return out2;
}
function linksOf(tubes, mounts) {
  const links = /* @__PURE__ */ new Map();
  const link = (a, b) => {
    if (!a || !b || a === b) return;
    if (!links.has(a)) links.set(a, /* @__PURE__ */ new Set());
    if (!links.has(b)) links.set(b, /* @__PURE__ */ new Set());
    links.get(a).add(b);
    links.get(b).add(a);
  };
  const ownerOf = (shape) => shape.owner ?? shape.name;
  const seats2 = /* @__PURE__ */ new Map();
  for (const tube2 of tubes)
    for (const mount of mounts.get(tube2) ?? []) {
      if (!mount) continue;
      const host = ownerOf(mount.shape);
      link(tube2.owner, host);
      if (!seats2.has(host)) seats2.set(host, []);
      seats2.get(host).push(tube2.owner);
      if (mount.shape.cut) for (const cut2 of [mount.shape.cut].flat()) link(tube2.owner, ownerOf(cut2));
    }
  for (const owners of seats2.values()) for (const a of owners) for (const b of owners) link(a, b);
  return links;
}
var entriesOf = (items, cam) => items.flatMap((item) => (item.shapes ?? []).map((shape) => ({ shape, box: screenBox(shape, cam, [0, 0, 0]).map((v, i) => v + (i < 2 ? -1 : 1)), owner: item.route ?? shape.owner ?? item.name, bundle: shape.bundle ?? null, item: item.name })));
function frontEntry(entries, cam, x, y) {
  const c = add3(mul3(cam.R, (x - cam.origin[0]) / cam.k), mul3(cam.D, (y - cam.origin[1]) / cam.k));
  let best = -BIG;
  let who = null;
  for (const entry of entries) {
    const { shape, box } = entry;
    if (x < box[0] || x > box[2] || y < box[1] || y > box[3]) continue;
    const t = rayDepth(shape, c, cam.V, 0.02, null);
    if (t !== null && t > best) best = t, who = entry;
  }
  return who;
}
function frontAt(entries, cam, x, y) {
  const entry = frontEntry(entries, cam, x, y);
  return entry ? entry.owner : null;
}
var belongs = (entry, name, bundle) => Boolean(entry) && (entry.owner === name || entry.item === name || bundle && entry.bundle === bundle);
function slenderOf(solids, { ratio = 4, least = 0.3 } = {}) {
  const out2 = [];
  const axisLine = (centre, axis, half, r, shape) => {
    out2.push({ name: shape.owner ?? shape.name, solid: shape.name, owners: new Set([shape.name, shape.owner].filter(Boolean)), points: [add3(centre, mul3(axis, -half)), add3(centre, mul3(axis, half))], r, move: shape.move, ride: shape.ride, piece: shape.piece, rod: true });
  };
  for (const shape of solids) {
    if (!shape || shape.kind === "tube" || shape.kind === "ball" || shape.fitting) continue;
    if (shape.kind === "body") {
      const s = shape.poly.map(([value]) => value);
      const s0 = Math.min(...s);
      const s1 = Math.max(...s);
      const r2 = Math.max(...shape.poly.map(([, value]) => value));
      if (r2 >= least && s1 - s0 >= ratio * r2) axisLine(add3(shape.F.o, mul3(shape.F.a, (s0 + s1) / 2)), shape.F.a, (s1 - s0) / 2, r2, shape);
      continue;
    }
    let axes;
    let half;
    let centre;
    if (shape.kind === "prism") {
      const xs = shape.poly.map(([x]) => x);
      const ys = shape.poly.map(([, y]) => y);
      const [x0, x1, y0, y1] = [Math.min(...xs), Math.max(...xs), Math.min(...ys), Math.max(...ys)];
      axes = [shape.F.u, shape.F.v, shape.F.a];
      half = [(x1 - x0) / 2, (y1 - y0) / 2, (shape.s1 - shape.s0) / 2];
      centre = add3(shape.F.o, add3(add3(mul3(shape.F.u, (x0 + x1) / 2), mul3(shape.F.v, (y0 + y1) / 2)), mul3(shape.F.a, (shape.s0 + shape.s1) / 2)));
    } else if (shape.kind === "box") {
      axes = shape.axes;
      half = shape.half;
      centre = shape.o;
    } else continue;
    const order = [0, 1, 2].sort((a, b) => half[b] - half[a]);
    const r = half[order[1]];
    if (r >= least && half[order[0]] >= ratio * r) axisLine(centre, axes[order[0]], half[order[0]], r, shape);
  }
  return out2;
}
function crowding(routes, P, { gap = 1, bend = 30, links = /* @__PURE__ */ new Map(), items = null, allow = [], state, clear = 2, rods = [] } = {}) {
  const cam = cameraBasis(P);
  const shift = (thing) => state === void 0 ? [0, 0, 0] : offsetOf(thing, state);
  const entries = items ? entriesOf(items.map((item) => ({ ...item, shapes: (item.shapes ?? []).map((shape) => moved(shape, shift(item))) })), cam) : null;
  const bundles = new Map(routes.map((route) => [route.name, route.bundle]));
  const shown = (owner, x, y, rod) => {
    if (!entries) return true;
    const entry = frontEntry(entries, cam, x, y);
    if (rod) return Boolean(entry) && (entry.shape.name === rod.solid || !entry.shape.name && entry.item === rod.solid);
    return belongs(entry, owner, bundles.get(owner));
  };
  const flat = (p) => [cam.origin[0] + dot3(p, cam.R) * cam.k, cam.origin[1] + dot3(p, cam.D) * cam.k];
  const lines = [...routes, ...rods].map((route) => {
    const step = Math.max(0.25, route.r * 0.5);
    const offset = shift(route);
    const dense = resample(route.points.map((p) => add3(p, offset)), step);
    return { ...route, step, dense, screen: dense.map(flat), width: route.r * cam.k };
  });
  const marksOf = (line) => {
    const out2 = [];
    const reach = Math.max(2, Math.round(2 * line.r / line.step));
    const last = line.dense.length - 1;
    for (let i = 0; i <= last; i++) {
      if (i <= reach || i >= last - reach) {
        out2.push({ i, where: i <= reach ? "start" : "end" });
        continue;
      }
      const A = sub3(line.dense[i], line.dense[i - reach]);
      const B = sub3(line.dense[i + reach], line.dense[i]);
      const turn = Math.acos(Math.max(-1, Math.min(1, dot3(A, B) / (len3(A) * len3(B) || 1)))) * 180 / Math.PI;
      if (turn > bend) out2.push({ i, where: "bend" });
    }
    return out2;
  };
  const found = /* @__PURE__ */ new Map();
  for (const a of lines) {
    if (a.rod) continue;
    const marks = marksOf(a);
    for (const b of lines) {
      if (a === b || a.bundle && a.bundle === b.bundle || links.get(a.name)?.has(b.name)) continue;
      if (b.rod && [...b.owners].some((name) => name === a.name || links.get(a.name)?.has(name))) continue;
      if (allow.some(([x, y]) => [b.name, b.solid].filter(Boolean).some((name) => matches([x], a.name) && matches([y], name) || matches([y], a.name) && matches([x], name)))) continue;
      for (const { i, where } of marks) {
        const [x, y] = a.screen[i];
        let best = { d: BIG, j: -1 };
        for (let j = 0; j < b.screen.length; j++) {
          const d = Math.hypot(b.screen[j][0] - x, b.screen[j][1] - y);
          if (d < best.d) best = { d, j };
        }
        const touch = best.d - a.width - b.width;
        if (touch >= gap) continue;
        if (where !== "bend" && touch <= -2 * Math.min(a.width, b.width)) {
          const tip = a.screen[where === "start" ? 0 : a.screen.length - 1];
          let clearTip = BIG;
          for (const q of b.screen) clearTip = Math.min(clearTip, Math.hypot(q[0] - tip[0], q[1] - tip[1]));
          const reachB = Math.max(2, Math.round(2 * b.r / b.step));
          const j0 = Math.max(0, best.j - reachB);
          const j1 = Math.min(b.dense.length - 1, best.j + reachB);
          const straight = j1 - j0 >= 2 && dot3(unit3(sub3(b.dense[best.j], b.dense[j0])), unit3(sub3(b.dense[j1], b.dense[best.j]))) > Math.cos(bend * Math.PI / 180);
          if (straight && clearTip > b.width + a.width + 1) continue;
        }
        const [bx, by] = b.screen[best.j];
        const u = [(bx - x) / (best.d || 1), (by - y) / (best.d || 1)];
        const inA = Math.max(0.2, a.width - 0.35);
        const inB = Math.max(0.2, b.width - 0.35);
        if (!shown(a.name, x + u[0] * inA, y + u[1] * inA)) continue;
        if (b.rod) {
          if (!shown(b.name, bx - u[0] * inB, by - u[1] * inB, b) && !shown(b.name, bx + u[0] * inB, by + u[1] * inB, b)) continue;
        } else if (!shown(b.name, bx - u[0] * inB, by - u[1] * inB)) continue;
        const depth = Math.abs(dot3(sub3(a.dense[i], b.dense[best.j]), cam.V));
        const need2 = 2 * (a.r + b.r);
        const id = [a.name, b.name].sort().join("|");
        const prior = found.get(id);
        if (!prior || Math.abs(touch) < Math.abs(prior.gap)) found.set(id, { a: a.name, b: b.rod ? `${b.solid} (rod)` : b.name, where, gap: touch, depth, need: need2, screen: [x, y], at: a.dense[i], state: state === void 0 ? "" : labelOf(state) });
      }
    }
  }
  if (entries)
    for (const fitting of entries.filter((entry) => entry.shape.fitting && entry.shape.kind === "body")) {
      const { shape } = fitting;
      const reach = Math.max(...shape.poly.map(([, r]) => r));
      const [x, y] = flat(shape.F.o);
      for (const b of lines) {
        if (b.rod) continue;
        if (fitting.bundle && b.bundle === fitting.bundle || b.name === fitting.owner || links.get(fitting.owner)?.has(b.name)) continue;
        if (allow.some(([p, q]) => matches([p], fitting.item) && matches([q], b.name) || matches([q], fitting.item) && matches([p], b.name))) continue;
        let best = { d: BIG, j: -1 };
        for (let j = 0; j < b.screen.length; j++) {
          const d = Math.hypot(b.screen[j][0] - x, b.screen[j][1] - y);
          if (d < best.d) best = { d, j };
        }
        const touch = best.d - reach * cam.k - b.width;
        if (touch >= clear) continue;
        const front = frontEntry(entries, cam, x, y);
        if (!(front === fitting || belongs(front, fitting.owner, fitting.bundle))) continue;
        const id = [fitting.item, b.name].sort().join("|");
        const prior = found.get(id);
        if (!prior || Math.abs(touch) < Math.abs(prior.gap)) found.set(id, { a: fitting.item, b: b.name, where: "fitting", gap: touch, depth: Math.abs(dot3(sub3(shape.F.o, b.dense[best.j]), cam.V)), need: 0, screen: [x, y], at: shape.F.o, state: state === void 0 ? "" : labelOf(state) });
      }
    }
  return [...found.values()].sort((x, y) => Math.abs(x.gap) - Math.abs(y.gap));
}
var multiply = (m, n) => [m[0] * n[0] + m[2] * n[1], m[1] * n[0] + m[3] * n[1], m[0] * n[2] + m[2] * n[3], m[1] * n[2] + m[3] * n[3], m[0] * n[4] + m[2] * n[5] + m[4], m[1] * n[4] + m[3] * n[5] + m[5]];
function matrixOf(text) {
  let m = [1, 0, 0, 1, 0, 0];
  if (!text) return m;
  for (const [, kind, args] of text.matchAll(/(matrix|translate|scale|rotate|skewX|skewY)\s*\(([^)]*)\)/g)) {
    const v = (args.match(/-?(?:\d+\.?\d*|\.\d+)(?:e[-+]?\d+)?/gi) ?? []).map(Number);
    let n = [1, 0, 0, 1, 0, 0];
    if (kind === "matrix" && v.length === 6) n = v;
    else if (kind === "translate") n = [1, 0, 0, 1, v[0] ?? 0, v[1] ?? 0];
    else if (kind === "scale") n = [v[0] ?? 1, 0, 0, v[1] ?? v[0] ?? 1, 0, 0];
    else if (kind === "rotate") {
      const a = (v[0] ?? 0) * Math.PI / 180;
      const [cx, cy] = [v[1] ?? 0, v[2] ?? 0];
      n = multiply(multiply([1, 0, 0, 1, cx, cy], [Math.cos(a), Math.sin(a), -Math.sin(a), Math.cos(a), 0, 0]), [1, 0, 0, 1, -cx, -cy]);
    } else if (kind === "skewX") n = [1, 0, Math.tan((v[0] ?? 0) * Math.PI / 180), 1, 0, 0];
    else if (kind === "skewY") n = [1, Math.tan((v[0] ?? 0) * Math.PI / 180), 0, 1, 0, 0];
    m = multiply(m, n);
  }
  return m;
}
var NUMBER = /-?(?:\d+\.?\d*|\.\d+)(?:e[-+]?\d+)?/gi;
var attributeOf = (attrs3, name) => {
  const hit = [...attrs3.matchAll(/(?:^|\s)([^\s=/>]+)\s*=\s*(["'])([\s\S]*?)\2/g)].find((match) => match[1] === name);
  if (!hit) return null;
  const named = { amp: "&", lt: "<", gt: ">", quot: '"', apos: "'" };
  return hit[3].replace(/&(#x[0-9a-fA-F]+|#\d+|amp|lt|gt|quot|apos);/g, (all, code) => {
    if (code[0] !== "#") return named[code];
    const value = code[1] === "x" ? parseInt(code.slice(2), 16) : Number(code.slice(1));
    return value > 0 && value <= 1114111 ? String.fromCodePoint(value) : all;
  });
};
function pointsOfShape(tag, attrs3) {
  const get = (name) => attributeOf(attrs3, name);
  const num = (name) => Number(get(name) ?? 0);
  if (tag === "path") {
    const d = get("d") ?? "";
    const out2 = [];
    let x = 0;
    let y = 0;
    let sx = 0;
    let sy = 0;
    for (const [, command, args] of d.matchAll(/([MmLlHhVvCcSsQqTtAaZz])([^MmLlHhVvCcSsQqTtAaZz]*)/g)) {
      const v = (args.match(NUMBER) ?? []).map(Number);
      const rel = command === command.toLowerCase();
      const C = command.toUpperCase();
      const pair = (i) => [v[i] + (rel ? x : 0), v[i + 1] + (rel ? y : 0)];
      const take = (p) => {
        out2.push(p);
        return p;
      };
      if (C === "H") for (const value of v) [x] = take([value + (rel ? x : 0), y]);
      else if (C === "V") for (const value of v) [, y] = take([x, value + (rel ? y : 0)]);
      else if (C === "A") for (let i = 0; i + 6 < v.length; i += 7) [x, y] = take([v[i + 5] + (rel ? x : 0), v[i + 6] + (rel ? y : 0)]);
      else if (C === "Z") {
        x = sx;
        y = sy;
      } else {
        const width = C === "C" ? 6 : C === "S" || C === "Q" ? 4 : 2;
        for (let i = 0; i + 1 < v.length; i += width) {
          for (let j = 0; j < width; j += 2) out2.push(pair(i + j));
          [x, y] = pair(i + width - 2);
          if (C === "M" && i === 0) {
            sx = x;
            sy = y;
          }
        }
      }
    }
    return out2;
  }
  if (tag === "circle" || tag === "ellipse") {
    const r = Number(get("r") ?? get("rx") ?? 0);
    const ry = Number(get("r") ?? get("ry") ?? 0);
    return [[num("cx") - r, num("cy") - ry], [num("cx") + r, num("cy") + ry]];
  }
  if (tag === "line") return [[num("x1"), num("y1")], [num("x2"), num("y2")]];
  if (tag === "rect") return cornersOfBox([num("x"), num("y"), num("x") + num("width"), num("y") + num("height")]);
  if (tag === "polyline" || tag === "polygon") {
    const v = (get("points") ?? "").match(NUMBER)?.map(Number) ?? [];
    const out2 = [];
    for (let i = 0; i + 1 < v.length; i += 2) out2.push([v[i], v[i + 1]]);
    return out2;
  }
  return [];
}
var boxOfPoints = (points, m) => {
  let box = null;
  for (const [x, y] of points) {
    const px = m[0] * x + m[2] * y + m[4];
    const py = m[1] * x + m[3] * y + m[5];
    box = box ? [Math.min(box[0], px), Math.min(box[1], py), Math.max(box[2], px), Math.max(box[3], py)] : [px, py, px, py];
  }
  return box;
};
var cornersOfBox = ([x0, y0, x1, y1]) => [[x0, y0], [x1, y0], [x1, y1], [x0, y1]];
var boxOfShape = (tag, attrs3, m) => {
  if (tag !== "circle" && tag !== "ellipse") return boxOfPoints(pointsOfShape(tag, attrs3), m);
  const num = (name) => Number(attributeOf(attrs3, name) ?? 0);
  const rx = tag === "circle" ? num("r") : num("rx");
  const ry = tag === "circle" ? rx : num("ry");
  const x = m[0] * num("cx") + m[2] * num("cy") + m[4];
  const y = m[1] * num("cx") + m[3] * num("cy") + m[5];
  const dx = Math.hypot(m[0] * rx, m[2] * ry);
  const dy = Math.hypot(m[1] * rx, m[3] * ry);
  return [x - dx, y - dy, x + dx, y + dy];
};
var unionBox = (a, b) => !a ? b : !b ? a : [Math.min(a[0], b[0]), Math.min(a[1], b[1]), Math.max(a[2], b[2]), Math.max(a[3], b[3])];
var meetBox = (a, b) => {
  if (!a || !b) return a ?? null;
  const box = [Math.max(a[0], b[0]), Math.max(a[1], b[1]), Math.min(a[2], b[2]), Math.min(a[3], b[3])];
  return box[0] <= box[2] && box[1] <= box[3] ? box : null;
};
var areaOf = (box) => box ? Math.max(0, box[2] - box[0]) * Math.max(0, box[3] - box[1]) : 0;
function markupBox(svg) {
  const tags = [...svg.matchAll(/<(\/?)([a-zA-Z]+)((?:"[^"]*"|'[^']*'|[^'">])*?)(\/?)>/g)];
  const clips = /* @__PURE__ */ new Map();
  let clipId = null;
  for (const [, close, tag, attrs3, self] of tags) {
    if (tag === "clipPath" && !close) {
      const id = attributeOf(attrs3, "id");
      if (id) clips.set(id, null);
      clipId = self ? null : id;
      continue;
    }
    if (clipId) {
      if (tag === "clipPath" && close) {
        clipId = null;
        continue;
      }
      clips.set(clipId, unionBox(clips.get(clipId), boxOfShape(tag, attrs3, matrixOf(attributeOf(attrs3, "transform")))));
    }
  }
  const stack = [{ m: [1, 0, 0, 1, 0, 0], clip: null, skip: false }];
  let box = null;
  for (const [, close, tag, attrs3, self] of tags) {
    const top = stack[stack.length - 1];
    if (close) {
      if (stack.length > 1) stack.pop();
      continue;
    }
    const m = multiply(top.m, matrixOf(attributeOf(attrs3, "transform")));
    const ref = ((attributeOf(attrs3, "clip-path") ?? "").match(/url\(#([^)]*)\)/) ?? [])[1];
    const own = ref && clips.get(ref) ? boxOfPoints(cornersOfBox(clips.get(ref)), m) : null;
    const clip = own ? meetBox(top.clip ?? own, own) : top.clip;
    const empty = ref && clips.has(ref) && (!own || areaOf(own) === 0 || top.clip && (!clip || areaOf(clip) === 0));
    const frame = { m, clip, skip: Boolean(empty) || top.skip || ["defs", "clipPath", "mask", "linearGradient", "radialGradient", "pattern", "text", "title"].includes(tag) || (attributeOf(attrs3, "class") ?? "").includes("iso-halo") };
    if (!frame.skip) {
      const shape = boxOfShape(tag, attrs3, m);
      if (shape) box = unionBox(box, frame.clip ? meetBox(shape, frame.clip) : shape);
    }
    if (!self) stack.push(frame);
  }
  return box;
}
function footprintOf(shape, cam) {
  const flat = (p) => [cam.origin[0] + dot3(p, cam.R) * cam.k, cam.origin[1] + dot3(p, cam.D) * cam.k];
  if (shape.kind === "body") {
    const { F } = shape;
    const points = [];
    for (const [s, r] of shape.poly) {
      if (r <= 0) {
        points.push(flat(add3(F.o, mul3(F.a, s))));
        continue;
      }
      for (let i = 0; i < 16; i++) {
        const a = i / 16 * Math.PI * 2;
        points.push(flat(add3(add3(F.o, mul3(F.a, s)), add3(mul3(F.u, r * Math.cos(a)), mul3(F.v, r * Math.sin(a))))));
      }
    }
    return boxOfPoints(points, [1, 0, 0, 1, 0, 0]);
  }
  if (shape.kind === "prism") {
    const { F } = shape;
    const points = [];
    for (const s of [shape.s0, shape.s1]) for (const [x, y] of shape.poly) points.push(flat(add3(add3(F.o, mul3(F.a, s)), add3(mul3(F.u, x), mul3(F.v, y)))));
    return boxOfPoints(points, [1, 0, 0, 1, 0, 0]);
  }
  const [x0, y0, x1, y1] = screenBox(shape, cam, [0, 0, 0]);
  return [x0, y0, x1, y1];
}
function coverage(items, P, { least = 0.6, pad = 1, allow = [] } = {}) {
  const cam = cameraBasis(P);
  const out2 = [];
  for (const item of items) {
    if (typeof item.svg !== "string" || !item.shapes || !item.shapes.length || matches(allow, item.name)) continue;
    const drawn = markupBox(item.svg);
    if (!drawn) continue;
    const grow = (box) => [box[0] - pad, box[1] - pad, box[2] + pad, box[3] + pad];
    const shapes = item.shapes.map((shape) => footprintOf(shape, cam)).reduce(unionBox, null);
    const share = areaOf(meetBox(grow(drawn), grow(shapes))) / (areaOf(grow(drawn)) || 1);
    if (share < least) out2.push({ name: item.name, share, drawn, shapes });
  }
  return out2.sort((a, b) => a.share - b.share);
}
function selfOverlaps(items, P, { entries: given = null, fold = 0.25, least = 0.5 } = {}) {
  const cam = cameraBasis(P);
  const entries = given ?? entriesOf(items, cam);
  const flat = (p) => [cam.origin[0] + dot3(p, cam.R) * cam.k, cam.origin[1] + dot3(p, cam.D) * cam.k];
  const out2 = [];
  for (const item of items) {
    if (!item.route || !item.shapes || !item.shapes.length || item.shapes[0].kind !== "tube") continue;
    const shape = item.shapes[0];
    const r = shape.radii.reduce((sum, value) => sum + value, 0) / shape.radii.length;
    const dense = resample(shape.points, Math.max(0.1, r * 0.2));
    const screen = dense.map(flat);
    const n = screen.length;
    if (n < 4) continue;
    const width = r * cam.k;
    const span = 3;
    const normals = screen.map((_, i) => {
      const a = screen[Math.max(0, i - span)];
      const b = screen[Math.min(n - 1, i + span)];
      const length = Math.hypot(b[0] - a[0], b[1] - a[1]) || 1;
      return [-(b[1] - a[1]) / length, (b[0] - a[0]) / length];
    });
    let worst = null;
    for (const side of [1, -1]) {
      const edge = screen.map((p, i) => [p[0] + side * normals[i][0] * width, p[1] + side * normals[i][1] * width]);
      for (let i = span; i < n - span - 1; i++) {
        const along = [screen[i + 1][0] - screen[i][0], screen[i + 1][1] - screen[i][1]];
        const step = [edge[i + 1][0] - edge[i][0], edge[i + 1][1] - edge[i][1]];
        const length = Math.hypot(along[0], along[1]);
        if (length < 1e-6) continue;
        const forward = (step[0] * along[0] + step[1] * along[1]) / length;
        if (forward > -fold * length) continue;
        const x = (screen[i][0] + screen[i + 1][0]) / 2;
        const y = (screen[i][1] + screen[i + 1][1]) / 2;
        const front = frontEntry(entries, cam, x, y);
        if (front && front.owner !== item.route && front.item !== item.name) continue;
        const radius = Math.abs(forward / length - 1) > 1e-6 ? width / Math.abs(1 - forward / length) : Infinity;
        if (width - radius < least) continue;
        if (!worst || radius < worst.radius) worst = { name: item.name, route: item.route, radius, width, at: dense[i], screen: [x, y] };
      }
    }
    if (worst) out2.push(worst);
  }
  return out2;
}
function solidClearances(solids, { state, sunk = 0.5, spacing = 0.6, cell = 4 } = {}) {
  const stretched = /* @__PURE__ */ new Set();
  const list = solids.filter((shape) => shape.kind !== "tube").map((shape) => {
    if (!(shape.slide && state !== void 0 && shape.move)) return shape;
    const next = { ...moved(shape, offsetOf(shape, state)), move: void 0 };
    if (next.slide.to !== shape.slide.to) stretched.add(next);
    return next;
  });
  if (!solidClearances.cache) solidClearances.cache = /* @__PURE__ */ new WeakMap();
  const cache = solidClearances.cache;
  const gridOf = (shape) => {
    let samples = cache.get(shape);
    if (!samples) cache.set(shape, samples = /* @__PURE__ */ new Map());
    const key = `${spacing}:${cell}`;
    let grid = samples.get(key);
    if (grid) return grid;
    grid = /* @__PURE__ */ new Map();
    for (const p of surfaceOf2(shape, spacing)) {
      const key2 = p.map((v) => Math.floor(v / cell)).join(",");
      if (!grid.has(key2)) grid.set(key2, []);
      grid.get(key2).push(p);
    }
    samples.set(key, grid);
    return grid;
  };
  const pointsIn = (shape, box) => {
    const grid = gridOf(shape);
    const lo = box.min.map((v) => Math.floor(v / cell));
    const hi = box.max.map((v) => Math.floor(v / cell));
    const out2 = [];
    if ((hi[0] - lo[0] + 1) * (hi[1] - lo[1] + 1) * (hi[2] - lo[2] + 1) > grid.size) {
      for (const points of grid.values()) for (const p of points) if (p.every((v, i) => v >= box.min[i] && v <= box.max[i])) out2.push(p);
      return out2;
    }
    for (let x = lo[0]; x <= hi[0]; x++)
      for (let y = lo[1]; y <= hi[1]; y++)
        for (let z = lo[2]; z <= hi[2]; z++) {
          const points = grid.get(`${x},${y},${z}`);
          if (points) {
            for (const p of points) if (p.every((v, i) => v >= box.min[i] && v <= box.max[i])) out2.push(p);
          }
        }
    return out2;
  };
  const offsets = list.map((shape) => offsetAt(shape, state));
  const bounds = list.map((shape) => boundsOf(shape));
  const found = [];
  for (let a = 0; a < list.length; a++)
    for (let b = a + 1; b < list.length; b++) {
      const rel = sub3(offsets[a], offsets[b]);
      if (Math.abs(rel[0]) + Math.abs(rel[1]) + Math.abs(rel[2]) < 1e-6 && !stretched.has(list[a]) && !stretched.has(list[b])) continue;
      const box = { min: [0, 1, 2].map((i) => Math.max(bounds[a].min[i] + rel[i], bounds[b].min[i])), max: [0, 1, 2].map((i) => Math.min(bounds[a].max[i] + rel[i], bounds[b].max[i])) };
      if (box.min.some((v, i) => v > box.max[i] - sunk)) continue;
      if (seatedOn(list[a], list[b]) || seatedOn(list[b], list[a])) continue;
      let worst = -sunk;
      let at = null;
      const local = { min: sub3(box.min, rel), max: sub3(box.max, rel) };
      for (const p of pointsIn(list[a], local)) {
        const d = sdf(list[b], add3(p, rel));
        if (d < worst) worst = d, at = add3(p, offsets[a]);
      }
      for (const p of pointsIn(list[b], box)) {
        const d = sdf(list[a], sub3(p, rel));
        if (d < worst) worst = d, at = add3(p, offsets[b]);
      }
      if (at) found.push({ tube: list[a].name, other: list[b].name, kind: "through", solid: true, clearance: worst, need: -sunk, at, from: 0, to: 0, length: 0, state: state === void 0 ? "" : labelOf(state) });
    }
  return found.sort((x, y) => x.clearance - y.clearance);
}
function wobble(solids, { samples = 20 } = {}) {
  const out2 = [];
  for (const shape of solids) {
    const profile = shape.curve;
    if (!profile) continue;
    const segments = curveRuns(profile);
    let run3 = [];
    const flush = () => {
      if (run3.length) {
        const values = [];
        for (const index of run3) {
          const [s0] = profile[index];
          const [s1] = profile[index + 1];
          for (let j = values.length ? 1 : 0; j <= samples; j++) {
            const s = s0 + (s1 - s0) * j / samples;
            values.push([s, segments[index].slope(s)]);
          }
        }
        const scale = Math.max(1, ...values.map(([, g]) => Math.abs(g))) * 1e-6;
        const turns = [];
        let last = 0;
        for (let i = 1; i < values.length; i++) {
          const d = values[i][1] - values[i - 1][1];
          if (Math.abs(d) <= scale) continue;
          const sign = Math.sign(d);
          if (last && sign !== last) turns.push(Math.round(values[i - 1][0] * 100) / 100);
          last = sign;
        }
        if (turns.length) out2.push({ name: shape.name, at: turns, from: profile[run3[0]][0], to: profile[run3[run3.length - 1] + 1][0] });
      }
      run3 = [];
    };
    segments.forEach((segment, index) => segment ? run3.push(index) : flush());
    flush();
  }
  return out2;
}
function seats(solids) {
  const out2 = [];
  for (const shape of solids) {
    if (!shape.seated || !shape.cut) continue;
    for (const host of [shape.cut].flat()) {
      const mine = mul3(shape.move ?? [0, 0, 0], 1);
      const theirs = mul3(host.move ?? [0, 0, 0], 1);
      if ((shape.ride ?? shape.piece) === (host.ride ?? host.piece) && sameOffset(mine, theirs)) continue;
      out2.push({ name: shape.name, host: host.name, piece: shape.ride ?? shape.piece, hostPiece: host.ride ?? host.piece });
    }
  }
  return out2;
}
var sameRun = (a, b) => Boolean(a.route) && a.route === b.route && Math.abs(a.chunk - b.chunk) <= 1;
function recorder(P, { order = [], spring = {}, ground = grounded } = {}) {
  const V = cameraBasis(P).V;
  const counts = /* @__PURE__ */ new Map();
  const R = { P, V, order, spring, ground, items: [], solids: [], tubes: [], routes: [], settled: null };
  R.nameFor = (base) => {
    const count = (counts.get(base) ?? 0) + 1;
    counts.set(base, count);
    return count === 1 ? base : `${base}#${count}`;
  };
  R.solid = (shape) => {
    R.solids.push(shape);
    return shape;
  };
  R.put = ({ at = null, bias = 0, key, name, piece = "", move = [0, 0, 0], ride, shapes = [], ...rest } = {}) => {
    const item = { ...rest, piece, ride: ride ?? piece, key: key ?? (at ? dot3(at, V) : 0) + bias, move, shapes, name: name ?? R.nameFor(`${piece || "item"}.item`) };
    for (const shape of shapes) shape.move = item.move, shape.ride = item.ride, shape.piece = piece;
    R.items.push(item);
    return item;
  };
  R.route = (name, points, radius, { owner = name, touch, bundle, limp = false, gaps = [], closed = false, ends = [true, true], rims, free: free2 = [false, false], piece = "", move = [0, 0, 0], ride = piece } = {}) => {
    const total = pathLength(points);
    const radiusOf = typeof radius === "function" ? radius : () => radius;
    const runs = runsOf(total, gaps);
    const recorded = runs.map(([from, to], index) => ({
      ...tube(cut(points, from, to), (t) => radiusOf((from + (to - from) * t) / total), { name, owner, touch, bundle, limp, joined: true }),
      tips: closed ? [null, null] : [index === 0 && ends[0] ? points[0] : null, index === runs.length - 1 && ends[1] ? points[points.length - 1] : null],
      tipAxes: [tangentAlong(points, 0), tangentAlong(points, total)],
      tipRims: rims ?? [radiusOf(0), radiusOf(1)],
      free: [index === 0 && free2[0], index === runs.length - 1 && free2[1]],
      offset: from,
      total,
      move,
      ride,
      piece
    }));
    R.tubes.push(...recorded);
    R.routes.push({ name, points, r: radiusOf(0.5), bundle, move, ride, piece });
    return recorded;
  };
  return R;
}
function explodeStates(order = [], spring = {}, { uniform = 10, stride = 4 } = {}) {
  if (!order.length) return { depth: [0], frames: [], apart: false };
  const reversals = reversalsOf(order, spring.stagger ?? 0.035);
  const prefix = prefixStates(order);
  return {
    depth: [...uniformStates(uniform), ...springStates(order, { ...spring, stride, reversals }), ...prefix],
    frames: [...springStates(order, { ...spring, reversals }), ...prefix],
    apart: true
  };
}
function settle(R, P = R.P, { states = explodeStates(R.order, R.spring).depth, skip = sameRun, ...options2 } = {}) {
  const items = R.items.slice();
  const overlaps2 = overlapsOf(items, P, { states, skip, ...options2 });
  const solved = orderKeys(items, overlaps2);
  items.forEach((item, index) => item.key = solved.keys[index]);
  R.settled = { items, overlaps: overlaps2, solved, states };
  return R.settled;
}
var worstOf = (lists) => [...lists.flat().reduce((all, c) => all.has(`${c.tube}|${c.other}`) && all.get(`${c.tube}|${c.other}`).clearance <= c.clearance ? all : all.set(`${c.tube}|${c.other}`, c), /* @__PURE__ */ new Map()).values()].sort((x, y) => x.clearance - y.clearance);
function audit(R, P = R.P, { allow = [], crowd = [], cover = [], ground = R.ground, frames: frames2 = explodeStates(R.order, R.spring).frames, apart = R.order.length > 0 } = {}) {
  const { items, overlaps: overlaps2, solved } = R.settled ?? settle(R, P);
  const mounts = mountsOf(R.tubes, R.solids);
  const links = linksOf(R.tubes, mounts);
  return {
    clearance: clearances(R.tubes, R.solids, { mounts }),
    apart: apart ? [...clearances(R.tubes, R.solids, { state: 1, mounts, only: "through" }), ...solidClearances(R.solids, { state: 1 })] : [],
    flight: worstOf(frames2.map((state) => [...clearances(R.tubes, R.solids, { state, mounts, only: "through" }), ...solidClearances(R.solids, { state })])),
    crowding: (apart ? [0, 1] : [0]).flatMap((state) => crowding(R.routes, P, { links, items, allow: crowd, state, rods: slenderOf(R.solids) })),
    cover: coverage(items, P, { allow: cover }),
    terminals: terminals(R.tubes, R.solids, { mounts }),
    loose: looseEnds(R.tubes, R.solids, { state: 1 }),
    folds: folds(R.routes, P, { items }),
    self: selfOverlaps(items, P),
    wobble: wobble(R.solids),
    seats: seats(R.solids),
    supports: supports(R.solids, R.tubes, { ground }),
    depth: depthOrder(items, P, { overlaps: overlaps2, solved, allow })
  };
}

// third_party/anatomy/kit/turn-build.mjs
var TAU2 = Math.PI * 2;
var r4 = (v) => Math.round(v * 1e4) / 1e4;
var r3 = (v) => Math.round(v * 1e3) / 1e3;
var pack3 = (value) => JSON.parse(JSON.stringify(value, (key, v) => typeof v === "number" ? r3(v) : v instanceof Float64Array || v instanceof Float32Array ? Array.from(v, r3) : v));
var pack = (value) => JSON.parse(JSON.stringify(value, (key, v) => typeof v === "number" ? r4(v) : v instanceof Float64Array || v instanceof Float32Array ? Array.from(v, r4) : v));
var esc = (text) => String(text).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
function octOf(n) {
  const l = Math.abs(n[0]) + Math.abs(n[1]) + Math.abs(n[2]) || 1;
  let x = n[0] / l;
  let y = n[1] / l;
  if (n[2] < 0) {
    const ox = (1 - Math.abs(y)) * (x >= 0 ? 1 : -1);
    const oy = (1 - Math.abs(x)) * (y >= 0 ? 1 : -1);
    x = ox;
    y = oy;
  }
  return [Math.round((x * 0.5 + 0.5) * 65535), Math.round((y * 0.5 + 0.5) * 65535)];
}
function packPairs(byLayer, stride, grouped) {
  const out2 = {};
  for (const [name, list] of Object.entries(byLayer)) {
    const count = list.length / stride;
    const bytes = new Uint8Array(count * (grouped ? 10 : 8));
    const view = new DataView(bytes.buffer);
    for (let e = 0; e < count; e++) {
      const at = e * stride;
      let o = e * (grouped ? 10 : 8);
      view.setUint16(o, list[at]);
      view.setUint16(o + 2, list[at + 1]);
      o += 4;
      if (grouped) {
        view.setUint16(o, list[at + 2] + 1);
        o += 2;
      }
      const [u, v] = octOf(list.slice(at + stride - 3, at + stride));
      view.setUint16(o, u);
      view.setUint16(o + 2, v);
    }
    out2[name] = Buffer.from(bytes).toString("base64");
  }
  return out2;
}
function signedArea2(points) {
  let s = 0;
  for (let i = 0; i < points.length; i++) {
    const a = points[i];
    const b = points[(i + 1) % points.length];
    s += a[0] * b[1] - b[0] * a[1];
  }
  return s / 2;
}
function convexOrThrow(ring, name) {
  const points = ring.filter((p, i) => Math.hypot(p[0] - ring[(i + ring.length - 1) % ring.length][0], p[1] - ring[(i + ring.length - 1) % ring.length][1]) > 1e-9);
  const n = points.length;
  let sign = 0;
  let turned = 0;
  for (let i = 0; i < n; i++) {
    const a = points[i];
    const b = points[(i + 1) % n];
    const c = points[(i + 2) % n];
    const cross = (b[0] - a[0]) * (c[1] - b[1]) - (b[1] - a[1]) * (c[0] - b[0]);
    if (Math.abs(cross) < 1e-9) continue;
    if (!sign) sign = Math.sign(cross);
    else if (Math.sign(cross) !== sign) throw new Error(`turning: part ${name} is not convex; split it into convex pieces`);
    turned += Math.atan2(cross, (b[0] - a[0]) * (c[0] - b[0]) + (b[1] - a[1]) * (c[1] - b[1]));
  }
  if (sign && Math.abs(Math.abs(turned) - TAU2) > 1e-6) throw new Error(`turning: part ${name} is not convex; split it into convex pieces`);
}
function roundedPolygon(polygon, radius = 0, steps = 4) {
  const ordered = signedArea2(polygon) < 0 ? polygon.slice().reverse() : polygon.slice();
  if (!(radius > 0)) return ordered.map(([x, y]) => [x, y]);
  const same = (p, q) => Math.hypot(p[0] - q[0], p[1] - q[1]) <= 1e-9;
  const poly = ordered.filter((p, i) => i === 0 || !same(p, ordered[i - 1]));
  while (poly.length > 1 && same(poly[0], poly[poly.length - 1])) poly.pop();
  if (poly.length < 3) return poly.map(([x, y]) => [x, y]);
  const n = poly.length;
  const normals = poly.map((a, i) => {
    const b = poly[(i + 1) % n];
    const l = Math.hypot(b[0] - a[0], b[1] - a[1]) || 1;
    return [(b[1] - a[1]) / l, -(b[0] - a[0]) / l];
  });
  const out2 = [];
  for (let i = 0; i < n; i++) {
    const na = normals[(i - 1 + n) % n];
    const nb = normals[i];
    const denom = 1 + na[0] * nb[0] + na[1] * nb[1];
    const c = [poly[i][0] - radius * (na[0] + nb[0]) / denom, poly[i][1] - radius * (na[1] + nb[1]) / denom];
    const a0 = Math.atan2(na[1], na[0]);
    let a1 = Math.atan2(nb[1], nb[0]);
    while (a1 < a0 - 1e-9) a1 += TAU2;
    for (let s = 0; s <= steps; s++) {
      const t = a0 + (a1 - a0) * s / steps;
      out2.push([c[0] + radius * Math.cos(t), c[1] + radius * Math.sin(t)]);
    }
  }
  return out2;
}
var fine = (v) => {
  const t = Math.round(v * 1e3) / 1e3;
  return t === 0 ? "0" : String(t);
};
var finePath = (points) => points.map(([x, y], i) => `${i ? "L" : "M"}${fine(x)} ${fine(y)}`).join("") + "Z";
var dot32 = dot3;
var sub32 = sub3;
var add32 = add3;
var mul32 = mul3;
function marginOf(n, A, B) {
  let hiA = -Infinity;
  for (const a of A) {
    const v = n[0] * a[0] + n[1] * a[1] + n[2] * a[2];
    if (v > hiA) hiA = v;
  }
  let loB = Infinity;
  for (const b of B) {
    const v = n[0] * b[0] + n[1] * b[1] + n[2] * b[2];
    if (v < loB) loB = v;
  }
  return { margin: loB - hiA, d: (loB + hiA) / 2 };
}
function closest(A, B, rounds = 200) {
  let w = sub32(B[0], A[0]);
  for (let it = 0; it < rounds; it++) {
    const l = len3(w);
    if (l < 1e-12) break;
    let hi = -Infinity;
    let a = A[0];
    for (const p of A) {
      const v = dot32(p, w);
      if (v > hi) {
        hi = v;
        a = p;
      }
    }
    let lo = Infinity;
    let b = B[0];
    for (const p of B) {
      const v = dot32(p, w);
      if (v < lo) {
        lo = v;
        b = p;
      }
    }
    const s = sub32(b, a);
    const ds = sub32(w, s);
    const dd = dot32(ds, ds);
    if (dd < 1e-14) break;
    const t = Math.max(0, Math.min(1, dot32(w, ds) / dd));
    const next = sub32(w, mul32(ds, t));
    if (len3(sub32(next, w)) < 1e-10) break;
    w = next;
  }
  return w;
}
function quickSeparate(A, B, hints = []) {
  const centre = (list) => mul32(list.reduce((sum, p) => add32(sum, p), [0, 0, 0]), 1 / list.length);
  const candidates = [sub32(centre(B), centre(A)), ...hints.flatMap((h) => [h, mul32(h, -1)])].filter((n2) => len3(n2) > 1e-9).map(unit3);
  let best = null;
  for (const n2 of candidates) {
    const { margin: margin2 } = marginOf(n2, A, B);
    if (!best || margin2 > best.margin) best = { n: n2, margin: margin2 };
  }
  if (best.margin >= 0.1) return best;
  let { n, margin } = best;
  for (const step of [0.3, 0.1, 0.03]) {
    for (let round2 = 0; round2 < 12; round2++) {
      const F = frameAlong([0, 0, 0], n);
      let improved = false;
      for (let j = 0; j < 8; j++) {
        const t = j / 8 * TAU2;
        const trial = unit3(add32(n, add32(mul32(F.u, step * Math.cos(t)), mul32(F.v, step * Math.sin(t)))));
        const value = marginOf(trial, A, B).margin;
        if (value > margin + 1e-9) {
          margin = value;
          n = trial;
          improved = true;
        }
      }
      if (!improved) break;
    }
  }
  return { n, margin };
}
function separate(A, B, hints = []) {
  const centre = (list) => mul32(list.reduce((s, p) => add32(s, p), [0, 0, 0]), 1 / list.length);
  const candidates = [sub32(centre(B), centre(A)), closest(A, B), ...hints.flatMap((h) => [h, mul32(h, -1)])].filter((n2) => len3(n2) > 1e-9).map(unit3);
  let best = null;
  for (const n2 of candidates) {
    const { margin: margin2 } = marginOf(n2, A, B);
    if (!best || margin2 > best.margin) best = { n: n2, margin: margin2 };
  }
  let { n, margin } = best;
  for (const step of [0.3, 0.1, 0.03, 0.01, 3e-3, 1e-3]) {
    for (let round2 = 0; round2 < 40; round2++) {
      const F = frameAlong([0, 0, 0], n);
      let improved = false;
      for (let j = 0; j < 8; j++) {
        const t = j / 8 * TAU2;
        const trial = unit3(add32(n, add32(mul32(F.u, step * Math.cos(t)), mul32(F.v, step * Math.sin(t)))));
        const value = marginOf(trial, A, B).margin;
        if (value > margin + 1e-9) {
          margin = value;
          n = trial;
          improved = true;
        }
      }
      if (!improved) break;
    }
  }
  return { n, d: marginOf(n, A, B).d, margin };
}
function frameFrom(F) {
  const a = unit3(F.a);
  let u = F.u ? unit3(sub32(F.u, mul32(a, dot32(F.u, a)))) : null;
  if (!u || len3(u) < 1e-9) u = frameAlong([0, 0, 0], a).u;
  const v = F.v && Math.abs(dot32(cross3(a, u), F.v)) > 0.999 ? unit3(F.v) : cross3(a, u);
  return { o: F.o.slice(), a, u, v };
}
function sampleShape(shape, count = 48) {
  const out2 = [];
  if (shape.kind === "body") {
    const F = frameFrom(shape.F);
    for (const [s, r] of shape.poly) {
      if (r < 1e-9) {
        out2.push(pointOf(F, s, 0, 0));
        continue;
      }
      for (let j = 0; j < count; j++) out2.push(pointOf(F, s, r, j / count * TAU2));
    }
  } else if (shape.kind === "prism") {
    const F = shape.F;
    for (const s of [shape.s0, shape.s1]) for (const [x, y] of shape.poly) out2.push(add32(add32(F.o, mul32(F.a, s)), add32(mul32(F.u, x), mul32(F.v, y))));
  } else if (shape.kind === "ball") {
    const golden = Math.PI * (3 - Math.sqrt(5));
    const total = Math.max(count * 3, 96);
    for (let i = 0; i < total; i++) {
      const y = 1 - 2 * (i + 0.5) / total;
      const rad = Math.sqrt(1 - y * y);
      const t = golden * i;
      const n = [Math.cos(t) * rad, Math.sin(t) * rad, y];
      if ((shape.flats ?? []).some(([nx, ny, nz, d]) => nx * n[0] * shape.r + ny * n[1] * shape.r + nz * n[2] * shape.r > d + 1e-9)) continue;
      out2.push(add32(shape.o, mul32(n, shape.r)));
    }
    for (const [nx, ny, nz, d] of shape.flats ?? []) {
      const F = frameAlong(add32(shape.o, mul32([nx, ny, nz], d)), [nx, ny, nz]);
      const rho = Math.sqrt(Math.max(0, shape.r * shape.r - d * d));
      for (let j = 0; j < count; j++) {
        const p = pointOf(F, 0, rho, j / count * TAU2);
        if ((shape.flats ?? []).every(([mx, my, mz, e]) => mx * (p[0] - shape.o[0]) + my * (p[1] - shape.o[1]) + mz * (p[2] - shape.o[2]) <= e + 1e-6)) out2.push(p);
      }
    }
  } else if (shape.kind === "box") {
    for (const sx of [-1, 1]) for (const sy of [-1, 1]) for (const sz of [-1, 1]) out2.push(add32(shape.o, add32(add32(mul32(shape.axes[0], sx * shape.half[0]), mul32(shape.axes[1], sy * shape.half[1])), mul32(shape.axes[2], sz * shape.half[2]))));
  } else if (shape.kind === "tube") {
    const pts = shape.points;
    for (let i = 0; i < pts.length; i++) {
      const t = unit3(sub32(pts[Math.min(pts.length - 1, i + 1)], pts[Math.max(0, i - 1)]));
      const F = frameAlong(pts[i], t);
      const ring = Math.max(8, Math.round(count / 4));
      for (let j = 0; j < ring; j++) out2.push(pointOf(F, 0, shape.radii[i], j / ring * TAU2));
    }
  }
  return out2;
}
function hull2(points) {
  return hullOf(points);
}
function thinCloud(points, most = 64) {
  if (points.length <= most) return points;
  const out2 = [];
  const step = points.length / most;
  for (let i = 0; i < most; i++) out2.push(points[Math.floor(i * step)]);
  return out2;
}
function turning(P, { recorder: recorder2 = null, scale = 1 } = {}) {
  const T = { P, R: recorder2, scale, groups: [], layers: [], order: [], parts: [], built: null };
  const groupOf = (g) => {
    if (g === void 0 || g === null) return null;
    if (typeof g !== "string") return g;
    const group2 = T.groups.find((x) => x.name === g);
    if (!group2) throw new Error(`turning: unknown group ${g}`);
    return group2;
  };
  const layerOf = (l) => typeof l === "string" ? T.layers.find((x) => x.name === l) : l;
  const origin = (group2) => group2 ? group2.origin : [0, 0, 0];
  const local = (group2, p) => sub32(p, origin(group2));
  T.group = (name, options2 = {}) => {
    if (T.groups.some((group3) => group3.name === name)) throw new Error(`turning: duplicate group ${name}`);
    const parent = groupOf(options2.parent);
    const po = origin(parent);
    let kind;
    let spec;
    if (options2.turn) {
      kind = "turn";
      const pivot = options2.turn.pivot ?? [0, 0];
      spec = { origin: [pivot[0], pivot[1], 0], pivot: [pivot[0], pivot[1]], range: options2.turn.range ?? null };
    } else if (options2.slide) {
      kind = "slide";
      spec = { origin: po.slice(), direction: unit3(options2.slide.direction), travel: options2.slide.travel ?? 0, range: [0, options2.slide.travel ?? 0] };
    } else if (options2.hinge) {
      kind = "hinge";
      spec = { origin: options2.hinge.point.slice(), point: options2.hinge.point.slice(), axis: unit3(options2.hinge.axis), range: options2.hinge.range ?? [0, 0] };
    } else if (options2.free) {
      kind = "free";
      const at = options2.free.origin ?? po;
      spec = { origin: at.slice(), range: null };
    } else throw new Error(`turning: group ${name} needs turn, slide, hinge or free`);
    const upright = kind !== "free" && (parent ? parent.upright : true) && (kind !== "hinge" || Math.abs(spec.axis[2]) > 0.9999);
    const loose = kind === "free" || Boolean(parent && parent.loose);
    const group2 = { name, index: T.groups.length, parent, kind, upright, loose, ...spec };
    T.groups.push(group2);
    return group2;
  };
  T.layer = (name) => {
    const layer = { name, index: T.layers.length, live: true };
    T.layers.push(layer);
    return layer;
  };
  T.stack = (names) => {
    T.order = names.slice();
    return T;
  };
  const common = (options2, kind) => {
    const group2 = groupOf(options2.group);
    const layer = layerOf(options2.layer ?? T.layers[0]);
    if (!layer) throw new Error(`turning: part ${options2.name} has no live layer`);
    const name = options2.name ?? `${kind}#${T.parts.length}`;
    const material = options2.material ?? null;
    if (material && !TURN.materials.includes(material)) throw new Error(`turning: part ${name} has material ${material}; use one of ${TURN.materials.join(", ")}`);
    return { id: T.parts.length, name, kind, group: group2, layer, owner: options2.owner, tone: options2.tone ?? "hi", crease: options2.crease ?? "faint", lit: Boolean(options2.lit), material, details: options2.details ?? {}, shapes: [], planes: [], dots: [], samples: [], hints: [] };
  };
  const record = (part, shape) => {
    shape.name = shape.name ?? part.name;
    if (part.owner && !shape.owner) shape.owner = part.owner;
    part.shapes.push(shape);
    if (T.R) T.R.solid(shape);
    return shape;
  };
  const toLocalDots = (part, F, list) => {
    for (const dot of list ?? []) {
      const [s, x, y] = dot.at;
      const p = add32(add32(F.o, mul32(F.a, s)), add32(mul32(F.u, x), mul32(F.v, y)));
      part.dots.push({ p: local(part.group, p), n: dot.normal ? unit3(dot.normal) : null, size: dot.size ?? 0.5, tone: dot.tone ?? "mid", fade: dot.fade ?? [0.04, 0.42] });
    }
  };
  T.prism = (options2) => {
    const part = common(options2, "prism");
    let F;
    let ring;
    let s0;
    let s1;
    if (options2.plan) {
      F = { o: [0, 0, 0], a: [0, 0, 1], u: [1, 0, 0], v: [0, 1, 0] };
      ring = roundedPlan(options2.plan, options2.steps ?? 4);
      s0 = options2.z ?? options2.s0 ?? 0;
      s1 = options2.h !== void 0 ? s0 + options2.h : options2.s1;
    } else {
      F = frameFrom(options2.F);
      ring = roundedPolygon(options2.polygon, options2.round ?? 0, options2.steps ?? 4);
      s0 = options2.s0;
      s1 = options2.s1;
    }
    if (s1 < s0) [s0, s1] = [s1, s0];
    if (signedArea2(ring) < 0) ring = ring.slice().reverse();
    convexOrThrow(ring, part.name);
    const bevel = options2.bevel ?? part.details.bevel ?? 0;
    const upright = Math.abs(F.a[2]) > 0.9999 && (!part.group || part.group.upright);
    record(part, prism(F, ring, s0, s1, { name: part.name }));
    const corner = (s, [x, y]) => add32(add32(F.o, mul32(F.a, s)), add32(mul32(F.u, x), mul32(F.v, y)));
    part.world = { F, ring, s0, s1 };
    if (upright) {
      const flip = F.a[2] < 0;
      const pts = ring.map((p) => local(part.group, corner(flip ? s1 : s0, p)));
      let xy = pts.map(([x, y]) => [x, y]);
      if (signedArea2(xy) < 0) xy = xy.reverse();
      const z0 = pts[0][2];
      const z1 = z0 + (s1 - s0);
      part.spec = { up: 1, ring: xy.flat(), z0, z1, bevel };
      part.planPath = finePath(xy);
      part.localSeams = (part.details.seams ?? []).map((s) => flip ? z1 - (s - s0) : z0 + (s - s0));
    } else {
      const FL = { o: local(part.group, F.o), a: F.a, u: F.u, v: F.v };
      part.spec = { up: 0, F: FL, ring: ring.flat(), s0, s1, bevel };
      part.localSeams = (part.details.seams ?? []).slice();
    }
    toLocalDots(part, F, part.details.dots);
    for (const s of [s0, s1]) for (const p of ring) part.samples.push(local(part.group, corner(s, p)));
    part.hints.push(F.a);
    const n = ring.length;
    for (let i = 0; i < n; i++) {
      const a = ring[i];
      const b = ring[(i + 1) % n];
      const l = Math.hypot(b[0] - a[0], b[1] - a[1]);
      if (l > 1e-6) part.hints.push(unit3(add32(mul32(F.u, (b[1] - a[1]) / l), mul32(F.v, -(b[0] - a[0]) / l))));
    }
    T.parts.push(part);
    return part;
  };
  const detailParts = (part, F, radiusAt, ends) => {
    const details = part.details ?? {};
    for (const bolt of details.bolts ?? []) {
      const { s, r, count, phase = 0, size = 0.5, tone = "mid", fade = [0.04, 0.42] } = bolt;
      const atEnd = ends ? Math.abs(s - ends[0]) < 1e-6 ? -1 : Math.abs(s - ends[1]) < 1e-6 ? 1 : 0 : 0;
      const onCap = atEnd !== 0 && (!radiusAt || r < radiusAt(s) - 1e-6);
      const slope = radiusAt ? (radiusAt(s + 1e-3) - radiusAt(s - 1e-3)) / 2e-3 : 0;
      for (let j = 0; j < count; j++) {
        const t = phase + j / count * TAU2;
        const p = pointOf(F, s, r, t);
        const radial = radialOf(F, t);
        const n = onCap ? mul32(F.a, atEnd) : unit3(sub32(radial, mul32(F.a, slope)));
        part.dots.push({ p: local(part.group, p), n, size, tone, fade });
      }
    }
    toLocalDots(part, F, details.dots);
    for (const ring of details.rings ?? []) {
      const [s, x, y] = ring.at;
      const o = add32(add32(F.o, mul32(F.a, s)), add32(mul32(F.u, x), mul32(F.v, y)));
      const n = unit3(ring.normal ?? F.a);
      const B = frameAlong([0, 0, 0], n);
      const steps = Math.max(12, Math.ceil(TAU2 * ring.r * cameraOf(P).k / 1.2));
      const pts = Array.from({ length: steps }, (_, j) => [ring.r * Math.cos(j / steps * TAU2), ring.r * Math.sin(j / steps * TAU2)]);
      T.plane({ part, o, u: B.u, v: B.v, normal: n, fade: ring.fade ?? [0.04, 0.3], svg: `<path class="iso-line" data-tone="${ring.tone ?? "lo"}" d="${finePath(pts)}"/>` });
    }
    for (const rule of details.rules ?? []) {
      const pts = rule.points.map(([s, x, y]) => add32(add32(F.o, mul32(F.a, s)), add32(mul32(F.u, x), mul32(F.v, y))));
      let n = rule.normal ? unit3(rule.normal) : null;
      if (!n) {
        for (let i = 2; i < pts.length && !n; i++) {
          const c = cross3(sub32(pts[1], pts[0]), sub32(pts[i], pts[0]));
          if (len3(c) > 1e-9) n = unit3(c);
        }
        n = n ?? F.a;
      }
      const B = frameAlong([0, 0, 0], n);
      const o = pts[0];
      const flat = pts.map((p) => [dot32(sub32(p, o), B.u), dot32(sub32(p, o), B.v)]);
      const d = flat.map(([x, y], i) => `${i ? "L" : "M"}${fine(x)} ${fine(y)}`).join("");
      const free2 = rule.free === true ? ' data-free=""' : rule.free ? ` data-free="${rule.free}"` : "";
      T.plane({ part, o, u: B.u, v: B.v, normal: n, fade: rule.fade ?? [0.04, 0.3], svg: `<path class="iso-line" data-tone="${rule.tone ?? "lo"}"${free2} d="${d}"/>` });
    }
  };
  T.round = (options2) => {
    const F = frameFrom(options2.F);
    const r0 = Array.isArray(options2.r) ? options2.r[0] : options2.r0 ?? options2.r;
    const r1 = Array.isArray(options2.r) ? options2.r[1] : options2.r1 ?? options2.r;
    let s0 = options2.s0;
    let s1 = options2.s1;
    const ends = (options2.ends ?? ["flat", "flat"]).slice();
    if (s1 < s0) throw new Error(`turning: round ${options2.name} needs s0 < s1`);
    ends.forEach((end, j) => {
      if (end === "dome" && Math.abs(r0 - r1) > 1e-9) throw new Error(`turning: round ${options2.name} can only have a dome where the end radius equals the side's (a capsule)`);
    });
    const profile = [];
    const arc = (sAt, sign, r) => Array.from({ length: 9 }, (_, j) => j / 8 * (Math.PI / 2)).map((b) => [sAt + sign * r * Math.cos(b), r * Math.sin(b), 1]);
    if (ends[0] === "dome") profile.push(...arc(s0, -1, r0).slice(0, -1).map((p, j) => j === 0 ? [p[0], 0] : p), [s0, r0, 1]);
    else profile.push([s0, r0]);
    if (ends[1] === "dome") profile.push([s1, r1, 1], ...arc(s1, 1, r1).reverse().slice(1).map((p, j, list) => j === list.length - 1 ? [p[0], 0] : p));
    else profile.push([s1, r1]);
    const vertical = Math.abs(F.a[2]) > 0.9999;
    const groupOk = !options2.group || groupOf(options2.group).upright;
    const radiusAt = (s) => r0 + (r1 - r0) * (Math.max(s0, Math.min(s1, s)) - s0) / (s1 - s0 || 1);
    if (vertical && groupOk && options2.fixed !== false) {
      const meridian = [[profile[0][0], 0], ...profile.filter((p) => p[1] > 1e-9), [profile[profile.length - 1][0], 0]];
      const seams = (options2.details?.seams ?? []).map((sv) => arcOf(F, sv, radiusAt(sv), P, { slope: (r1 - r0) / (s1 - s0 || 1), least: 0 })).join("");
      const paths = lathe(meridian, F, P, ends.includes("dome") ? { smooth: true } : {});
      const svg = solidSvg(paths, { tone: options2.tone ?? "hi", crease: options2.crease ?? "faint", lit: options2.lit, inner: seams ? lineSvg(seams, { tone: "faint" }) : "" });
      const ribs = options2.details?.ribs ? { ...options2.details.ribs, r0: options2.details.ribs.r0 ?? radiusAt(options2.details.ribs.s0), r1: options2.details.ribs.r1 ?? radiusAt(options2.details.ribs.s1) } : void 0;
      const part2 = T.fixed({ ...options2, svg, anchor: pointOf(F, s0, 0, 0), F, details: { ...options2.details ?? {}, ribs, seams: void 0 }, shapes: [solid(F, profile, { name: options2.name })], skipDetails: true });
      part2.round = { F, s0, s1, r0, r1, ends };
      detailParts(part2, F, radiusAt, [s0, s1]);
      return part2;
    }
    const part = common(options2, "round");
    record(part, solid(F, profile, { name: part.name }));
    part.world = { F, s0, s1, r0, r1, ends, profile };
    part.spec = { F: { o: local(part.group, F.o), a: F.a, u: F.u, v: F.v }, s0, s1, r0, r1, ends };
    detailParts(part, F, radiusAt, [s0, s1]);
    const ring = (s, r, count = 48) => Array.from({ length: count }, (_, j) => pointOf(F, s, r, j / count * TAU2));
    const pts = [...ring(s0, r0), ...ring(s1, r1)];
    for (const [end, sAt, r] of [[0, s0, r0], [1, s1, r1]]) {
      if (ends[end] !== "dome") continue;
      const sign = end ? 1 : -1;
      for (let j = 1; j <= 6; j++) {
        const b = j / 6 * (Math.PI / 2);
        if (j === 6) pts.push(add32(F.o, mul32(F.a, sAt + sign * r)));
        else pts.push(...ring(sAt + sign * r * Math.sin(b), r * Math.cos(b), 32));
      }
    }
    part.samples = pts.map((p) => local(part.group, p));
    part.hints.push(F.a);
    T.parts.push(part);
    return part;
  };
  T.ball = (options2) => {
    const c = options2.c;
    const r = options2.r;
    const flats = (options2.flats ?? []).map(({ n, d }) => ({ n: unit3(n), d }));
    const shape = ball(c, r, { name: options2.name, flats: flats.map(({ n, d }) => [n[0], n[1], n[2], d]) });
    if (!flats.length && options2.fixed !== false) {
      const svg = solidSvg(sphereOf(c, r, P, { steps: 48 }), { tone: options2.tone ?? "hi", crease: options2.crease ?? "faint", lit: options2.lit });
      return T.fixed({ ...options2, svg, anchor: c, shapes: [shape] });
    }
    const part = common(options2, "ball");
    record(part, shape);
    part.world = { c, r, flats };
    part.spec = { c: local(part.group, c), r, flats };
    part.samples = sampleShape(shape, 48).map((p) => local(part.group, p));
    for (const { n } of flats) part.hints.push(n);
    detailParts(part, frameAlong(c, flats.length ? flats[0].n : [0, 0, 1]), null, null);
    T.parts.push(part);
    return part;
  };
  T.lathe = (options2) => {
    const F = frameFrom(options2.F);
    const profile = options2.profile;
    const curve = profileCurve(profile.map(([sv, rv]) => [sv, rv]), { slope: options2.slope ?? null, radius: options2.radius ?? null });
    const kk = cameraOf(P).k;
    const knots = [curve.s0];
    const split = (a, b, level) => {
      const mid = (a + b) / 2;
      if (level < 7 && (Math.abs(curve.radius(mid) - (curve.radius(a) + curve.radius(b)) / 2) * kk > 0.1 || b - a > 4)) {
        split(a, mid, level + 1);
        knots.push(mid);
        split(mid, b, level + 1);
      }
    };
    const stops = [curve.s0, ...profile.map(([sv]) => sv).filter((sv) => sv > curve.s0 && sv < curve.s1), curve.s1];
    for (let i = 0; i < stops.length - 1; i++) {
      split(stops[i], stops[i + 1], 0);
      knots.push(stops[i + 1]);
    }
    for (let i = 1; i < knots.length - 1; i++) {
      const a = curve.radius(knots[i - 1]);
      const b = curve.radius(knots[i]);
      const c = curve.radius(knots[i + 1]);
      const h0 = knots[i] - knots[i - 1];
      const h1 = knots[i + 1] - knots[i];
      if ((c - b) / h1 - (b - a) / h0 > 1e-6) throw new Error(`turning: lathe ${options2.name} is not convex near s = ${knots[i].toFixed(2)} (r(s) must be concave); split it`);
    }
    const levels = [];
    for (const sv of knots) {
      const g = curve.slope(sv);
      const norm = Math.hypot(1, g);
      levels.push(sv, curve.radius(sv), 1 / norm, -g / norm);
    }
    const caps = [curve.radius(curve.s0) > 1e-6, curve.radius(curve.s1) > 1e-6];
    const shape = solid(F, profile.map(([sv, rv]) => [sv, rv, 1]), { name: options2.name, radius: curve.radius });
    const vertical = Math.abs(F.a[2]) > 0.9999;
    const groupOk = !options2.group || groupOf(options2.group).upright;
    if (vertical && groupOk && options2.fixed !== false) {
      const meridian = [[curve.s0, 0], ...knots.map((sv) => [sv, curve.radius(sv), 1]), [curve.s1, 0]];
      meridian[1] = [meridian[1][0], meridian[1][1]];
      meridian[meridian.length - 2] = [meridian[meridian.length - 2][0], meridian[meridian.length - 2][1]];
      const seams = (options2.details?.seams ?? []).map((sv) => arcOf(F, sv, curve.radius(sv), P, { slope: curve.slope(sv), least: 0 })).join("");
      const svg = solidSvg(lathe(meridian, F, P, { smooth: { slope: curve.slope, radius: curve.radius } }), { tone: options2.tone ?? "hi", crease: options2.crease ?? "faint", lit: options2.lit, inner: seams ? lineSvg(seams, { tone: "faint" }) : "" });
      const part2 = T.fixed({ ...options2, svg, anchor: pointOf(F, curve.s0, 0, 0), F, details: { ...options2.details ?? {}, seams: void 0 }, shapes: [shape], skipDetails: true });
      detailParts(part2, F, curve.radius, [curve.s0, curve.s1]);
      return part2;
    }
    const part = common(options2, "lathe");
    record(part, shape);
    part.spec = { F: { o: local(part.group, F.o), a: F.a, u: F.u, v: F.v }, levels, caps };
    part.world = { F, profile, curve, knots };
    const pts = [];
    for (const sv of knots) for (let j = 0; j < 32; j++) pts.push(pointOf(F, sv, curve.radius(sv), j / 32 * TAU2));
    part.samples = pts.map((p) => local(part.group, p));
    part.hints.push(F.a);
    detailParts(part, F, curve.radius, [curve.s0, curve.s1]);
    T.parts.push(part);
    return part;
  };
  T.routes = [];
  T.tube = (options2) => {
    const { route, r, chunk = 6, turn = 20, gaps = [], breaks = [], caps = true, rings = null, hue = null, spacing = 0.8, owner, touch, bundle, rims, free: free2 } = options2;
    const group2 = groupOf(options2.group);
    const name = options2.name ?? `tube#${T.routes.length}`;
    const dense = resample(route, spacing);
    const total = pathLength(dense);
    const turnBreaks = [];
    let walked = 0;
    let bent = 0;
    for (let i = 1; i < dense.length - 1; i++) {
      walked += len3(sub32(dense[i], dense[i - 1]));
      const a = unit3(sub32(dense[i], dense[i - 1]));
      const b = unit3(sub32(dense[i + 1], dense[i]));
      bent += Math.acos(Math.max(-1, Math.min(1, dot32(a, b)))) * 180 / Math.PI;
      if (bent > turn) {
        turnBreaks.push(walked);
        bent = 0;
      }
    }
    const allBreaks = [...breaks, ...turnBreaks].sort((x, y) => x - y);
    const pieces = spansOf(total, gaps, allBreaks, chunk);
    const wide = r * cameraOf(P).k > 1.3;
    const routeIndex = T.routes.length;
    const capList = [caps].flat();
    T.routes.push({ name, group: group2, points: dense.map((p) => local(group2, p)), r, spacing, wide, hue, rings, world: route, gaps, breaks: allBreaks, chunk, caps });
    if (T.R) T.R.route(name, route, r, { gaps, limp: options2.limp ?? true, owner: owner ?? name, touch, bundle, rims, free: free2 });
    const chunks = pieces.map((piece, index) => {
      const part = common({ ...options2, name: `${name}:${index}` }, "tube");
      part.route = name;
      part.chunk = index;
      part.hue = hue;
      part.spec = { route: routeIndex, from: piece.from, to: piece.to, open0: piece.open0, open1: piece.open1, gap0: piece.gap0, gap1: piece.gap1, caps: [capList[0], capList[capList.length - 1]], wide, rings: rings ? { tone: rings.tone ?? "lo" } : null };
      const core = cut(dense, piece.from, piece.to);
      part.shapes.push(tube(core, r, { name: part.name, owner: owner ?? name }));
      part.world = { route, r, index };
      for (let i = 0; i < core.length; i++) {
        const t = unit3(sub32(core[Math.min(core.length - 1, i + 1)], core[Math.max(0, i - 1)]));
        const F = frameAlong(core[i], t);
        for (let j = 0; j < 10; j++) part.samples.push(local(group2, pointOf(F, 0, r, j / 10 * TAU2)));
      }
      part.hints.push(unit3(sub32(core[1], core[0])), unit3(sub32(core[core.length - 1], core[core.length - 2])));
      T.parts.push(part);
      return part;
    });
    return { name, chunks, total, dense };
  };
  T.fixed = (options2) => {
    const part = common(options2, "fixed");
    const anchor = options2.anchor;
    for (const shape of options2.shapes ?? []) record(part, shape);
    const world = part.shapes.flatMap((shape) => sampleShape(shape, 48));
    const flat = world.map((p) => iso(p, P));
    const hull = options2.hull ?? hull2(flat);
    const box = markupBox(options2.svg) ?? [Math.min(...hull.map((p) => p[0])), Math.min(...hull.map((p) => p[1])), Math.max(...hull.map((p) => p[0])), Math.max(...hull.map((p) => p[1]))];
    part.svg = options2.svg;
    const F = options2.F ? frameFrom(options2.F) : null;
    part.spec = { anchor: local(part.group, anchor), home: iso(anchor, P), box: [box[0] - 0.5, box[1] - 0.5, box[2] + 0.5, box[3] + 0.5], hull: hull.flat(), F: F ? { o: local(part.group, F.o), a: F.a, u: F.u, v: F.v } : null };
    if (F && !options2.skipDetails) detailParts(part, F, null, null);
    part.samples = world.map((p) => local(part.group, p));
    if (F) part.hints.push(F.a);
    T.parts.push(part);
    return part;
  };
  T.item = (options2) => {
    const part = common(options2, "item");
    const cloud = options2.cloud ?? [[0, 0, 0]];
    part.spec = { item: 1 };
    part.cloud = cloud.map((p) => local(part.group, p)).flat();
    part.samples = cloud.map((p) => local(part.group, p));
    T.parts.push(part);
    return part;
  };
  T.plane = ({ part, o, u, v, svg, fade = [0.04, 0.3], normal = null }) => {
    const U = unit3(u);
    const W = unit3(v);
    const n = normal ? unit3(normal) : unit3(cross3(U, W));
    part.planes.push({ o: local(part.group, o), u: U, v: W, n, fade, svg });
    return part;
  };
  T.billboard = ({ part, at, normal, svg, fade = [0.04, 0.3] }) => {
    part.planes.push({ o: local(part.group, at), u: [1, 0, 0], v: [0, 1, 0], n: unit3(normal), fade, svg, billboard: true });
    return part;
  };
  const drop = (part) => {
    T.parts.splice(T.parts.indexOf(part), 1);
    T.parts.forEach((p, index) => p.id = index);
  };
  T.split = (part, { n, d }) => {
    const N = unit3(n);
    if (part.kind === "prism") {
      const { F, ring, s0, s1 } = part.world;
      const along = dot32(N, F.a);
      const base = { name: part.name, owner: part.owner, group: part.group, layer: part.layer, tone: part.tone, crease: part.crease, lit: part.lit, material: part.material, details: { ...part.details }, bevel: part.spec.bevel };
      let halves;
      if (Math.abs(Math.abs(along) - 1) < 1e-6) {
        const sCut = (d - dot32(N, F.o)) / along;
        if (!(sCut > s0 + 1e-6 && sCut < s1 - 1e-6)) throw new Error(`turning: split plane misses ${part.name}`);
        halves = [{ s0, s1: sCut }, { s0: sCut, s1 }].map((span) => ({ ...base, F, polygon: ring, s0: span.s0, s1: span.s1 }));
      } else if (Math.abs(along) < 1e-6) {
        const nu = dot32(N, F.u);
        const nv = dot32(N, F.v);
        const c = d - dot32(N, F.o);
        const side = (p) => nu * p[0] + nv * p[1] - c;
        const clip = (sign) => {
          const out2 = [];
          for (let i = 0; i < ring.length; i++) {
            const a = ring[i];
            const b = ring[(i + 1) % ring.length];
            const sa = sign * side(a);
            const sb = sign * side(b);
            if (sa <= 0) out2.push(a);
            if (sa < 0 && sb > 0 || sa > 0 && sb < 0) {
              const t = sa / (sa - sb);
              out2.push([a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t]);
            }
          }
          return out2;
        };
        halves = [clip(1), clip(-1)].map((polygon) => ({ ...base, F, polygon, s0, s1 }));
        if (halves.some((h) => h.polygon.length < 3)) throw new Error(`turning: split plane misses ${part.name}`);
      } else throw new Error(`turning: a prism can only be split by a plane along or across its axis (${part.name})`);
      part.dead = true;
      if (T.R) T.R.solids.splice(T.R.solids.indexOf(part.shapes[0]), 1);
      const made = halves.map((h, index) => T.prism({ ...h, name: `${part.name}.${index ? "b" : "a"}`, round: 0, details: index ? { ...h.details, dots: [] } : h.details }));
      for (const half of made) {
        half.spec.cuts = [...part.spec.cuts ?? [], { n: N, d: d - dot32(N, half.group ? half.group.origin : [0, 0, 0]) }];
        half.hints.unshift(N);
      }
      drop(part);
      return made;
    }
    if (part.kind === "round" || part.kind === "fixed" && part.round) {
      const { F, s0, s1, r0, r1, ends } = part.round ?? part.world;
      const along = dot32(N, F.a);
      if (Math.abs(Math.abs(along) - 1) > 1e-6) throw new Error(`turning: a round can only be split across its axis (${part.name})`);
      const sCut = (d - dot32(N, F.o)) / along;
      if (!(sCut > s0 + 1e-6 && sCut < s1 - 1e-6)) throw new Error(`turning: split plane misses ${part.name}`);
      const rAt = r0 + (r1 - r0) * (sCut - s0) / (s1 - s0);
      part.dead = true;
      if (T.R) T.R.solids.splice(T.R.solids.indexOf(part.shapes[0]), 1);
      const base = { owner: part.owner, group: part.group, layer: part.layer, tone: part.tone, crease: part.crease, lit: part.lit, material: part.material, F, fixed: false };
      const made = [
        T.round({ ...base, name: `${part.name}.a`, s0, s1: sCut, r: [r0, rAt], ends: [ends[0], "open"], details: part.details }),
        T.round({ ...base, name: `${part.name}.b`, s0: sCut, s1, r: [rAt, r1], ends: ["open", ends[1]] })
      ];
      for (const half of made) {
        half.spec.cuts = [...part.spec.cuts ?? [], { n: N, d: d - dot32(N, half.group ? half.group.origin : [0, 0, 0]) }];
        half.hints.unshift(N);
      }
      drop(part);
      return made;
    }
    throw new Error(`turning: split supports prisms and rounds (${part.name})`);
  };
  T.build = (options2 = {}) => build(T, options2);
  return T;
}
function spansOf(total, gaps, breaks, maxLength) {
  const cuts = gaps.map(([a, b]) => [Math.max(0, Math.min(a, b)), Math.min(total, Math.max(a, b))]).filter(([a, b]) => b - a > 1e-6).sort((x, y) => x[0] - y[0]);
  const runs = [];
  let at = 0;
  for (const [a, b] of cuts) {
    if (a > at + 1e-6) runs.push([at, a, at > 0, true]);
    at = Math.max(at, b);
  }
  if (total > at + 1e-6) runs.push([at, total, at > 0, cuts.length > 0 && cuts[cuts.length - 1][1] >= total - 1e-6]);
  const pieces = [];
  for (const [from, to, gapStart, gapEnd] of runs) {
    const stops = [from, ...breaks.filter((b) => b > from + 1e-6 && b < to - 1e-6).sort((x, y) => x - y), to];
    for (let index = 0; index < stops.length - 1; index++) {
      const a = stops[index];
      const b = stops[index + 1];
      const count = Math.max(1, Math.ceil((b - a) / maxLength - 1e-9));
      for (let c = 0; c < count; c++) {
        pieces.push({
          from: a + (b - a) * c / count,
          to: a + (b - a) * (c + 1) / count,
          open0: !(index === 0 && c === 0),
          open1: !(index === stops.length - 2 && c === count - 1),
          gap0: index === 0 && c === 0 && gapStart,
          gap1: index === stops.length - 2 && c === count - 1 && gapEnd
        });
      }
    }
  }
  return pieces;
}
function groupData(T) {
  return T.groups.map((g) => ({
    name: g.name,
    parent: g.parent ? g.parent.index : -1,
    kind: g.kind,
    origin: g.origin,
    pivot: g.pivot,
    direction: g.direction,
    travel: g.travel,
    point: g.point,
    axis: g.axis,
    range: g.range,
    upright: g.upright,
    loose: g.loose || void 0
  }));
}
function partData(part) {
  const details = {};
  const seams = part.kind === "prism" ? part.localSeams : part.kind === "fixed" ? null : part.details.seams;
  if (seams && seams.length) details.seams = seams;
  if (part.details.ribs) details.ribs = part.details.ribs;
  const out2 = { name: part.name, kind: part.kind, group: part.group ? part.group.index : -1, layer: part.layer.index };
  if (part.tone !== "hi") out2.tone = part.tone;
  if (part.crease !== "faint") out2.crease = part.crease;
  if (part.lit) out2.lit = true;
  if (part.material) out2.mat = part.material;
  out2.spec = part.spec;
  if (Object.keys(details).length) out2.details = details;
  if (part.planes.length) out2.planes = part.planes.map(({ o, u, v, n, fade, billboard }) => ({ o, u, v, n, fade, billboard }));
  if (part.dots.length) out2.dots = part.dots.map(({ p, n, size, tone, fade }) => ({ p, n, size, tone, fade }));
  if (part.kind === "item") out2.cloud = part.cloud;
  return out2;
}
function statesOf(T, poses) {
  if (typeof poses === "function") poses = poses();
  if (Array.isArray(poses) && poses.length) return poses;
  const out2 = [];
  for (let deg = 0; deg < 360; deg += 2) out2.push(Object.fromEntries(T.groups.map((g) => [g.name, g.kind === "turn" ? deg : g.range ? g.range[0] + (g.range[1] - g.range[0]) * (deg % 90) / 90 : 0])));
  return out2;
}
function tumbleStates(T, group2, count = 160) {
  let root = group2;
  while (root && root.kind !== "free") root = root.parent;
  if (!root) return [];
  let seed = 977;
  const rand = () => (seed = seed * 16807 % 2147483647) / 2147483647;
  const out2 = [];
  for (let i = 0; i < count; i++) {
    const u = rand();
    const a = rand() * TAU2;
    const b = rand() * TAU2;
    const q = [Math.sqrt(1 - u) * Math.sin(a), Math.sqrt(1 - u) * Math.cos(a), Math.sqrt(u) * Math.sin(b), Math.sqrt(u) * Math.cos(b)];
    const values = { [root.name]: { q } };
    for (const g of T.groups) if (g.kind === "hinge" && g.loose) values[g.name] = g.range[0] + (g.range[1] - g.range[0]) * rand();
    out2.push(values);
  }
  return out2;
}
function groupStates(T, group2, states, { tumble = false } = {}) {
  if (!group2) return [{}];
  let chain = [];
  for (let g = group2; g; g = g.parent) chain.push(g);
  if (group2.loose) return tumble ? [...states, ...tumbleStates(T, group2)] : states.length ? states : [{}];
  if (chain.length === 1 && group2.kind === "turn") return Array.from({ length: 360 }, (_, deg) => ({ [group2.name]: deg }));
  if (chain.length === 1) {
    const [lo, hi] = group2.range ?? [0, 0];
    return Array.from({ length: 33 }, (_, i) => ({ [group2.name]: lo + (hi - lo) * i / 32 }));
  }
  return states;
}
function sweptGroups(T, layer, states, scene) {
  const V = viewOf(T.P);
  const cam = cameraOf(T.P);
  const byGroup = /* @__PURE__ */ new Map();
  for (const part of T.parts) {
    if (part.layer !== layer || part.dead) continue;
    const key = part.group ? part.group.index : -1;
    if (!byGroup.has(key)) byGroup.set(key, []);
    byGroup.get(key).push(part);
  }
  const out2 = [];
  for (const [key, parts] of byGroup) {
    const group2 = key >= 0 ? T.groups[key] : null;
    const local = parts.flatMap((part) => part.samples);
    const root = group2 && group2.kind === "turn" && !group2.parent;
    const list = root ? Array.from({ length: 72 }, (_, i) => ({ [group2.name]: i * 5 })) : group2 ? groupStates(T, group2, states) : [{}];
    let zmin = Infinity;
    let zmax = -Infinity;
    const box = [Infinity, Infinity, -Infinity, -Infinity];
    const cloud = [];
    const stride = Math.max(1, Math.floor(local.length * list.length / 4e3));
    let counter = 0;
    for (const values of list) {
      const cams = TURN.cams(scene, values);
      const c = key >= 0 ? cams[key] : cams.world;
      for (const q of local) {
        const p = [c.R[0] * q[0] + c.R[1] * q[1] + c.R[2] * q[2] + c.t[0], c.R[3] * q[0] + c.R[4] * q[1] + c.R[5] * q[2] + c.t[1], c.R[6] * q[0] + c.R[7] * q[1] + c.R[8] * q[2] + c.t[2]];
        if (p[2] < zmin) zmin = p[2];
        if (p[2] > zmax) zmax = p[2];
        const [x, y] = iso(p, T.P);
        if (x < box[0]) box[0] = x;
        if (y < box[1]) box[1] = y;
        if (x > box[2]) box[2] = x;
        if (y > box[3]) box[3] = y;
        if (counter++ % stride === 0) cloud.push(p);
      }
    }
    let radius = 0;
    let envelope = cloud;
    if (root) {
      const slices = /* @__PURE__ */ new Map();
      for (const q of local) {
        const band = Math.floor(q[2]);
        slices.set(band, Math.max(slices.get(band) ?? 0, Math.hypot(q[0], q[1])));
        radius = Math.max(radius, Math.hypot(q[0], q[1]));
      }
      envelope = [];
      for (const [band, r] of slices)
        for (const z of [band, band + 1])
          for (let j = 0; j < 48; j++) envelope.push([group2.origin[0] + r * Math.cos(j / 48 * TAU2), group2.origin[1] + r * Math.sin(j / 48 * TAU2), Math.max(zmin, Math.min(zmax, z))]);
      const pad = radius * cam.k;
      const c = iso([group2.origin[0], group2.origin[1], 0], T.P);
      box[0] = Math.min(box[0], c[0] - pad);
      box[2] = Math.max(box[2], c[0] + pad);
    }
    out2.push({ key, group: group2, parts, root, radius, zmin, zmax, box, envelope, V });
  }
  return out2;
}
function relation(points, box, swept, P) {
  const V = viewOf(P);
  let zmin = Infinity;
  let zmax = -Infinity;
  for (const p of points) {
    zmin = Math.min(zmin, p[2]);
    zmax = Math.max(zmax, p[2]);
  }
  if (zmax <= swept.zmin + 1e-6) return { side: "behind", rule: "horizontal plane" };
  if (zmin >= swept.zmax - 1e-6) return { side: "front", rule: "horizontal plane" };
  if (swept.root) {
    const a = (P.azimuth ?? 45) * Math.PI / 180;
    const along = points.map((p) => (p[0] - swept.group.origin[0]) * Math.cos(a) + (p[1] - swept.group.origin[1]) * Math.sin(a));
    if (Math.max(...along) <= -swept.radius) return { side: "behind", rule: "cylinder" };
    if (Math.min(...along) >= swept.radius) return { side: "front", rule: "cylinder" };
  }
  if (box && (box[2] < swept.box[0] - 1 || swept.box[2] < box[0] - 1 || box[3] < swept.box[1] - 1 || swept.box[3] < box[1] - 1)) return { side: "apart", rule: "never overlap" };
  const hit = separate(points, swept.envelope, [[0, 0, 1], [Math.cos((P.azimuth ?? 45) * Math.PI / 180), Math.sin((P.azimuth ?? 45) * Math.PI / 180), 0]]);
  if (hit.margin >= -0.08) return { side: dot32(hit.n, V) > 0 ? "behind" : "front", rule: "swept envelope", margin: hit.margin };
  return null;
}
function proveLayers(T, statics, states, scene) {
  const order = T.order.length ? T.order : T.layers.map((layer) => layer.name);
  const rank = new Map(order.map((name, index) => [name, index]));
  const problems = [];
  const proofs = [];
  const swept = new Map(T.layers.map((layer) => [layer.name, sweptGroups(T, layer, states, scene)]));
  for (const layer of T.layers) if (!rank.has(layer.name)) problems.push(`live layer ${layer.name} is missing from T.stack`);
  for (const item of statics) {
    if (!item.shapes || !item.shapes.length) continue;
    const layerName = item.layer;
    if (!rank.has(layerName)) {
      problems.push(`static ${item.name} has layer ${layerName ?? "(none)"}, which is not in T.stack`);
      continue;
    }
    const points = item.shapes.flatMap((shape) => sampleShape(shape, 24));
    const flat = points.map((p) => iso(p, T.P));
    const box = [Math.min(...flat.map((p) => p[0])), Math.min(...flat.map((p) => p[1])), Math.max(...flat.map((p) => p[0])), Math.max(...flat.map((p) => p[1]))];
    for (const layer of T.layers) {
      const want = rank.get(layerName) < rank.get(layer.name) ? "behind" : "front";
      for (const group2 of swept.get(layer.name)) {
        const proof = relation(points, box, group2, T.P);
        const label = `${item.name} \xD7 ${layer.name}${group2.group ? `/${group2.group.name}` : ""}`;
        if (!proof) {
          const zs = points.map((p) => p[2]);
          const top = Math.max(...zs);
          const bottom = Math.min(...zs);
          const where = top > group2.zmax + 1e-6 ? `at z = ${group2.zmax.toFixed(2)}` : bottom < group2.zmin - 1e-6 ? `at z = ${group2.zmin.toFixed(2)}` : `into a piece behind and a piece in front of ${group2.group ? `the ${group2.group.name} axis` : "the layer"}`;
          problems.push(`static ${item.name} interleaves live layer ${layer.name}: split ${item.name} ${where}, or move it`);
          continue;
        }
        if (proof.side !== "apart" && proof.side !== want) {
          problems.push(`static ${item.name} is ${proof.side === "behind" ? "behind" : "in front of"} live layer ${layer.name} (${proof.rule}) but its layer ${layerName} is ${want === "behind" ? "under" : "over"} it: move it to a layer ${proof.side === "behind" ? "under" : "over"} ${layer.name}`);
          continue;
        }
        proofs.push({ static: item.name, layer: layer.name, group: group2.group ? group2.group.name : "world", rule: proof.rule, side: proof.side });
        void label;
      }
    }
  }
  const live = T.layers.slice().sort((a, b) => rank.get(a.name) - rank.get(b.name));
  for (let i = 0; i < live.length; i++)
    for (let j = i + 1; j < live.length; j++)
      for (const lower of swept.get(live[i].name))
        for (const upper of swept.get(live[j].name)) {
          let ok = lower.zmax <= upper.zmin + 1e-6 ? "horizontal plane" : null;
          if (!ok && (lower.box[2] < upper.box[0] - 1 || upper.box[2] < lower.box[0] - 1 || lower.box[3] < upper.box[1] - 1 || upper.box[3] < lower.box[1] - 1)) ok = "never overlap";
          if (!ok) {
            const hit = separate(lower.envelope, upper.envelope, [[0, 0, 1]]);
            if (hit.margin >= -0.08 && dot32(hit.n, viewOf(T.P)) > 0) ok = "swept envelope";
          }
          if (!ok) problems.push(`live layer ${live[i].name} interleaves live layer ${live[j].name} (${lower.group ? lower.group.name : "world"} \xD7 ${upper.group ? upper.group.name : "world"}): move parts between them or reorder T.stack`);
          else proofs.push({ static: `layer ${live[i].name}`, layer: live[j].name, group: upper.group ? upper.group.name : "world", rule: ok, side: "behind" });
        }
  return { problems, proofs };
}
function build(T, { statics = [], verify = false, poses = null, strict = true, fullClouds = false } = {}) {
  const P = T.P;
  const started = Date.now();
  const states = statesOf(T, poses);
  const groups = groupData(T);
  const parts = T.parts.map(partData);
  const sweep = (layerParts, list) => {
    const data2 = { P, groups, layers: T.layers.map((layer) => ({ name: layer.name, parts: [], rest: [] })), parts };
    const scene2 = TURN.prepare(data2, { unit: T.scale });
    const frames3 = scene2.runs.map((run3) => TURN.frame(run3));
    return { scene: scene2, frames: frames3, data: data2 };
  };
  void sweep;
  const routes = T.routes.map((route) => ({ points: route.points.flat().map(r4), r: route.r, spacing: route.spacing, wide: route.wide, hue: route.hue, rings: route.rings }));
  const scratch = { P, groups, layers: T.layers.map((layer) => ({ name: layer.name, parts: [], rest: [] })), parts, routes };
  let scene = TURN.prepare(scratch, { unit: T.scale });
  const slotNeed = parts.map(() => ({ bevel: 0, ribs: 0 }));
  const sampleCams = /* @__PURE__ */ new Map();
  const camsFor = (group2) => {
    const key = group2 ? group2.index : -1;
    if (!sampleCams.has(key)) {
      const list = groupStates(T, group2, states, { tumble: true }).map((values2) => TURN.cams(scene, values2));
      sampleCams.set(key, list);
    }
    return sampleCams.get(key);
  };
  T.parts.forEach((part, index) => {
    const run3 = scene.runs[index];
    const needs = part.kind === "item" ? false : part.kind === "prism" ? Boolean(part.spec.bevel) : part.kind === "tube" ? Boolean(part.spec.rings) : Boolean(part.details.ribs);
    if (!needs) return;
    const g = part.group ? part.group.index : -1;
    const wide = { ...run3, slots: { bevel: 64, ribs: 64 }, role: { ...run3.role } };
    for (let j = 0; j < 64; j++) {
      wide.role[`v${j}`] = 1e3 + j;
      wide.role[`r${j}`] = 2e3 + j;
    }
    const f = TURN.frame(run3);
    f.d = new Array(3e3).fill("");
    f.o = new Float64Array(3e3);
    f.q = new Int32Array(3e3);
    f.w = new Float64Array(3e3);
    f.t = new Array(3e3).fill("");
    f.cx = new Float64Array(3e3);
    f.cy = new Float64Array(3e3);
    let most = 0;
    for (const cams2 of camsFor(part.group)) {
      TURN.emit(wide, g >= 0 ? cams2[g] : cams2.world, f);
      most = Math.max(most, f.levels ?? 0);
    }
    slotNeed[index][part.kind === "prism" ? "bevel" : "ribs"] = Math.max(1, most);
  });
  parts.forEach((data2, index) => {
    data2.spec = slotNeed[index].bevel || slotNeed[index].ribs ? { ...data2.spec, slots: slotNeed[index] } : { ...data2.spec };
  });
  scene = TURN.prepare({ ...scratch, parts }, { unit: T.scale });
  const centre = (list) => mul32(list.reduce((s, p) => add32(s, p), [0, 0, 0]), 1 / Math.max(1, list.length));
  const spheres = T.parts.map((part) => {
    const c = centre(part.samples);
    let r = 0;
    for (const p of part.samples) r = Math.max(r, len3(sub32(p, c)));
    return { c, r };
  });
  const planes = {};
  const dynamic = {};
  const free2 = {};
  let stateCamList = null;
  const stateCams = () => stateCamList ?? (stateCamList = states.map((values2) => TURN.cams(scene, values2)));
  const boxCache = /* @__PURE__ */ new Map();
  const boxesOf = (part, list, key) => {
    const id = `${part.id}|${key}`;
    if (boxCache.has(id)) return boxCache.get(id);
    const local = thinCloud(part.samples, 40);
    const out3 = new Float64Array(4 * list.length + 1);
    const steps = [];
    list.forEach((cams2, at) => {
      const c = part.group ? cams2[part.group.index] : cams2.world;
      let x0 = Infinity;
      let y0 = Infinity;
      let x1 = -Infinity;
      let y1 = -Infinity;
      for (const q of local) {
        const x = c.ox + c.m[0] * q[0] + c.m[1] * q[1] + c.m[2] * q[2];
        const y = c.oy + c.m[3] * q[0] + c.m[4] * q[1] + c.m[5] * q[2];
        if (x < x0) x0 = x;
        if (x > x1) x1 = x;
        if (y < y0) y0 = y;
        if (y > y1) y1 = y;
      }
      if (at) steps.push(Math.max(Math.abs(x0 - out3[4 * at - 4]), Math.abs(y0 - out3[4 * at - 3]), Math.abs(x1 - out3[4 * at - 2]), Math.abs(y1 - out3[4 * at - 1])));
      out3.set([x0, y0, x1, y1], 4 * at);
    });
    steps.sort((x, y) => x - y);
    out3[4 * list.length] = steps.length ? steps[Math.floor(steps.length * 0.95)] : 0;
    boxCache.set(id, out3);
    return out3;
  };
  const boxesMeet = (a, b, list, key) => {
    const A = boxesOf(a, list, key);
    const B = boxesOf(b, list, key);
    const pad = 1.5 + A[4 * list.length] + B[4 * list.length];
    for (let i = 0; i < list.length; i++) {
      const o = 4 * i;
      if (A[o] < B[o + 2] + pad && B[o] < A[o + 2] + pad && A[o + 1] < B[o + 3] + pad && B[o + 1] < A[o + 3] + pad) return true;
    }
    return false;
  };
  let framedCount = 0;
  const framedAll = {};
  const groupPairsAll = {};
  const ancestors = (g) => {
    const out3 = [];
    for (let x = g; x; x = x.parent) out3.push(x);
    return out3;
  };
  const commonOf = (g1, g2) => {
    const list = ancestors(g1);
    for (let x = g2; x; x = x.parent) if (list.includes(x)) return x;
    return null;
  };
  const sampleStates = () => {
    const all = stateCams();
    const count = Math.min(all.length, 24);
    return Array.from({ length: count }, (_, i) => all[Math.floor(i * all.length / count)]);
  };
  const toFrame = (dir, from, frame) => {
    if (from === frame) return dir;
    const cams2 = sampleStates()[0] ?? TURN.cams(scene, {});
    const Rf = from ? cams2[from.index].R : [1, 0, 0, 0, 1, 0, 0, 0, 1];
    const w = [Rf[0] * dir[0] + Rf[1] * dir[1] + Rf[2] * dir[2], Rf[3] * dir[0] + Rf[4] * dir[1] + Rf[5] * dir[2], Rf[6] * dir[0] + Rf[7] * dir[1] + Rf[8] * dir[2]];
    const Rc = frame ? cams2[frame.index].R : [1, 0, 0, 0, 1, 0, 0, 0, 1];
    return [Rc[0] * w[0] + Rc[3] * w[1] + Rc[6] * w[2], Rc[1] * w[0] + Rc[4] * w[1] + Rc[7] * w[2], Rc[2] * w[0] + Rc[5] * w[1] + Rc[8] * w[2]];
  };
  const cloudCache = /* @__PURE__ */ new Map();
  const framedCloud = (part, frame) => {
    const key = `${part.id}|${frame ? frame.index : -1}`;
    if (cloudCache.has(key)) return cloudCache.get(key);
    const local = thinCloud(part.samples, 32);
    const out3 = [];
    for (const cams2 of sampleStates()) {
      const c = part.group ? cams2[part.group.index] : cams2.world;
      const f = frame ? cams2[frame.index] : cams2.world;
      for (const q of local) {
        const p = [c.R[0] * q[0] + c.R[1] * q[1] + c.R[2] * q[2] + c.t[0] - f.t[0], c.R[3] * q[0] + c.R[4] * q[1] + c.R[5] * q[2] + c.t[1] - f.t[1], c.R[6] * q[0] + c.R[7] * q[1] + c.R[8] * q[2] + c.t[2] - f.t[2]];
        out3.push([f.R[0] * p[0] + f.R[3] * p[1] + f.R[6] * p[2], f.R[1] * p[0] + f.R[4] * p[1] + f.R[7] * p[2], f.R[2] * p[0] + f.R[5] * p[1] + f.R[8] * p[2]]);
      }
    }
    cloudCache.set(key, out3);
    return out3;
  };
  const skip = {};
  const problems = [];
  const margins = [];
  const planesByName = /* @__PURE__ */ new Map();
  const layerData = [];
  for (const layer of T.layers) {
    const members = T.parts.filter((part) => part.layer === layer);
    const plan = [];
    const dyn = [];
    const framed = [];
    const skipped2 = [];
    const pairsOfGroups = [];
    const settled = /* @__PURE__ */ new Set();
    const byGroup = /* @__PURE__ */ new Map();
    for (const part of members) {
      if (part.group && part.group.loose) continue;
      const key = part.group ? part.group.index : -1;
      if (!byGroup.has(key)) byGroup.set(key, []);
      byGroup.get(key).push(part);
    }
    const keys = [...byGroup.keys()];
    if (states.length)
      for (let x = 0; x < keys.length; x++)
        for (let y = x + 1; y < keys.length; y++) {
          const A = byGroup.get(keys[x]);
          const B = byGroup.get(keys[y]);
          const ga = keys[x] >= 0 ? T.groups[keys[x]] : null;
          const gb = keys[y] >= 0 ? T.groups[keys[y]] : null;
          const common = commonOf(ga, gb);
          const ca = A.flatMap((part) => framedCloud(part, common).filter((_, i) => fullClouds || i % 2 === 0));
          const cb = B.flatMap((part) => framedCloud(part, common).filter((_, i) => fullClouds || i % 2 === 0));
          const hit = quickSeparate(ca, cb, [[0, 0, 1], ...A.flatMap((part) => part.hints).slice(0, 6).map((h) => toFrame(h, ga, common)), ...B.flatMap((part) => part.hints).slice(0, 6).map((h) => toFrame(h, gb, common))]);
          if (hit.margin < 0.1) continue;
          pairsOfGroups.push(keys[x], keys[y], common ? common.index : -1, hit.n[0], hit.n[1], hit.n[2]);
          settled.add(`${keys[x]}|${keys[y]}`);
          settled.add(`${keys[y]}|${keys[x]}`);
        }
    groupPairsAll[layer.name] = pairsOfGroups;
    for (let x = 0; x < members.length; x++)
      for (let y = x + 1; y < members.length; y++) {
        const a = members[x];
        const b = members[y];
        if (a.route && a.route === b.route && Math.abs(a.chunk - b.chunk) <= 1) {
          skipped2.push(a.id, b.id);
          continue;
        }
        const sa = spheres[a.id];
        const sb = spheres[b.id];
        if (a.group === b.group) {
          const g = a.group ? a.group.index : -1;
          const reach = len3(sub32(sb.c, sa.c)) + sa.r + sb.r;
          let near = false;
          void reach;
          if (a.group && a.group.loose) near = len3(sub32(sb.c, sa.c)) < sa.r + sb.r + 1;
          else near = boxesMeet(a, b, camsFor(a.group), `g${g}`);
          if (!near) continue;
          const hit = separate(a.samples, b.samples, [[0, 0, 1], ...a.hints, ...b.hints]);
          margins.push({ a: a.name, b: b.name, margin: hit.margin });
          const o = a.group ? a.group.origin : [0, 0, 0];
          planesByName.set(`${a.name}|${b.name}`, { n: hit.n, d: hit.d + dot32(hit.n, o) });
          if (hit.margin < -0.08) {
            problems.push(`interlock ${a.name} \xD7 ${b.name} ${hit.margin.toFixed(2)}: split, flats or a flush contact`);
            if (strict) continue;
          }
          plan.push(a.id, b.id, hit.n[0], hit.n[1], hit.n[2]);
        } else if (a.group && a.group.loose || b.group && b.group.loose) {
          continue;
        } else if (settled.has(`${a.group ? a.group.index : -1}|${b.group ? b.group.index : -1}`)) {
          continue;
        } else {
          const near = !states.length || boxesMeet(a, b, stateCams(), "states");
          if (!near) continue;
          const common = commonOf(a.group, b.group);
          const ca = framedCloud(a, common);
          const cb = framedCloud(b, common);
          const hit = quickSeparate(ca, cb, [[0, 0, 1], ...a.hints, ...b.hints].map((h) => toFrame(h, a.group, common)).concat([[0, 0, 1], ...b.hints.map((h) => toFrame(h, b.group, common))]));
          if (hit.margin >= 0.1) {
            framed.push(a.id, b.id, common ? common.index : -1, hit.n[0], hit.n[1], hit.n[2]);
            framedCount++;
          } else dyn.push(a.id, b.id);
        }
      }
    planes[layer.name] = plan;
    dynamic[layer.name] = dyn;
    framedAll[layer.name] = framed;
    free2[layer.name] = members.filter((part) => part.group && part.group.loose).map((part) => part.id);
    skip[layer.name] = skipped2;
    layerData.push({ name: layer.name, parts: members.map((part) => part.id), rest: [] });
  }
  if (problems.length && strict) throw new Error(`turning: ${problems.length} pair${problems.length === 1 ? "" : "s"} with no separating plane
  ${problems.join("\n  ")}`);
  const layered = proveLayers(T, statics, states, scene);
  if (layered.problems.length) throw new Error(`turning: ${layered.problems.length} layer problem${layered.problems.length === 1 ? "" : "s"}
  ${layered.problems.join("\n  ")}`);
  const values = Object.fromEntries(T.groups.map((g) => [g.name, g.kind === "free" ? null : 0]));
  const data = { P, groups, layers: layerData, parts, routes, planes: packPairs(planes, 5, false), framed: packPairs(framedAll, 6, true), groupPairs: pack(groupPairsAll), dynamic, free: free2, skip, values };
  const clouds = T.parts.map((part) => thinCloud(part.samples, 64));
  data.parts.forEach((p, index) => {
    if (p.kind === "fixed") p.cloud = clouds[index].flat().map(r4);
  });
  const packed = { ...pack({ ...data, parts: [] }), parts: pack3(data.parts) };
  scene = TURN.prepare(packed, { unit: T.scale });
  const cams = TURN.cams(scene, values);
  const frames2 = scene.runs.map((run3) => TURN.emit(run3, run3.group >= 0 ? cams[run3.group] : cams.world, TURN.frame(run3)));
  const V = viewOf(P);
  scene.layers.forEach((layer, index) => {
    const provisional = Int32Array.from(Array.from(layer.parts).sort((i, j) => dot32(spheres[i].c, V) - dot32(spheres[j].c, V)));
    const order = TURN.order(layer, frames2, cams, provisional, {}, scene);
    packed.layers[index].rest = Array.from(order);
    layer.rest = order;
  });
  const markup = {};
  scene.layers.forEach((layer, index) => {
    markup[layer.name] = `<g class="iso-parts" data-layer="${esc(layer.name)}">${packed.layers[index].rest.map((i) => partMarkup(T.parts[i], scene.runs[i], frames2[i])).join("")}</g>`;
  });
  const report = {
    parts: T.parts.length,
    groups: T.groups.length,
    layers: T.layers.map((layer) => ({ name: layer.name, parts: packed.layers[layer.index].parts.length, planar: planes[layer.name].length / 5, framed: framedAll[layer.name].length / 6, groupPairs: groupPairsAll[layer.name].length / 6, dynamic: dynamic[layer.name].length / 2, skip: skipped(skip[layer.name]) })),
    tight: margins.filter((m) => m.margin < 0).sort((a, b) => a.margin - b.margin),
    margins,
    proofs: layered.proofs,
    seconds: (Date.now() - started) / 1e3
  };
  const out2 = { svg: markup, data: packed, css: TURN_CSS, report, scene, frames: frames2, planesByName };
  out2.layerSvg = (name, { width, height, label = "" }) => `<svg xmlns="http://www.w3.org/2000/svg" class="iso-svg iso-live iso-layer" data-live="${esc(name)}" viewBox="0 0 ${width} ${height}" aria-hidden="true"${label ? ` aria-label="${esc(label)}"` : ""}>${markup[name]}</svg>`;
  if (verify) out2.verify = verifyData(T, statics);
  T.built = out2;
  T.data = packed;
  return out2;
}
var skipped = (list) => list.length / 2;
function attrs2(pairs) {
  return Object.entries(pairs).filter(([, v]) => v !== void 0 && v !== null && v !== false).map(([key, v]) => ` ${key}="${esc(v)}"`).join("");
}
function roleMarkup(part, run3, f, r) {
  const role = run3.roles[r];
  if (role.type === "path") return `<path${attrs2({ class: role.cls, "data-shade": role.shade === void 0 ? void 0 : String(role.shade), "data-tone": role.tone, "data-r": role.name, d: f.d[r] })}/>`;
  if (role.type === "face") {
    const q = f.q[r];
    const band = Math.min(3, Math.floor(q / TURN.q));
    const mix = (q - TURN.q * band) / TURN.q;
    const style = [mix ? `--f:${mix}` : "", f.w[r] >= 0 ? `stroke-width:${f.w[r]}` : ""].filter(Boolean).join(";");
    return `<path${attrs2({ class: "iso-tn", "data-r": role.name, "data-b": band ? String(band) : void 0, style: style || void 0, d: f.d[r] })}/>`;
  }
  if (role.type === "slot") return `<path${attrs2({ class: role.cls, "data-tone": role.tone, "data-r": role.name, opacity: String(Math.round(f.o[r] * 1e3) / 1e3), d: f.d[r] })}/>`;
  if (role.type === "xform") return `<path${attrs2({ class: role.cls, "data-r": role.name, transform: f.t[r], d: part.planPath })}/>`;
  if (role.type === "plane") {
    const index = Number(role.name.slice(5));
    return `<g${attrs2({ "data-r": role.name, transform: f.t[r], opacity: String(f.o[r]) })}>${part.planes[index].svg}</g>`;
  }
  return "";
}
function dotsMarkup(part, run3, f) {
  let out2 = "";
  let open = null;
  run3.roles.forEach((role, r) => {
    if (role.type !== "dot") return;
    if (open !== role.tone) {
      if (open !== null) out2 += "</g>";
      out2 += `<g class="iso-dots" data-tone="${role.tone}">`;
      open = role.tone;
    }
    out2 += `<circle data-r="${role.name}" cx="${Math.round(f.cx[r] * 100) / 100}" cy="${Math.round(f.cy[r] * 100) / 100}" r="${role.size}" fill-opacity="${f.o[r]}"/>`;
  });
  return open !== null ? out2 + "</g>" : out2;
}
function partMarkup(part, run3, f) {
  if (part.kind === "item") return `<g class="iso-item" data-p="${run3.index}" data-name="${esc(part.name)}"></g>`;
  const head = (cls, extra = {}) => `<g${attrs2({ class: cls, "data-p": String(run3.index), "data-name": part.name, "data-mat": part.material ?? void 0, "data-lit": part.lit ? "" : void 0, ...extra })}>`;
  const inner = run3.roles.map((role, r) => role.type === "dot" || role.type === "self" ? "" : roleMarkup(part, run3, f, r)).join("");
  if (part.kind === "tube") return head("tb", { "data-hue": part.hue ?? void 0 }) + inner + "</g>";
  if (part.kind === "fixed") {
    const at = part.svg.lastIndexOf('<path class="iso-line iso-edge"');
    const body2 = at >= 0 ? part.svg.slice(0, at) + inner + part.svg.slice(at) : part.svg + inner;
    return head("iso-part", { transform: f.t[run3.role.move] || void 0 }) + body2 + dotsMarkup(part, run3, f) + "</g>";
  }
  return head("iso-solid", { "data-seamless": part.kind === "round" || part.kind === "ball" || part.kind === "lathe" ? "" : void 0 }) + inner + dotsMarkup(part, run3, f) + "</g>";
}
function verifyData(T, statics = []) {
  const order = T.order.length ? T.order : T.layers.map((layer) => layer.name);
  const live = new Set(T.layers.map((layer) => layer.name));
  const staticLayers = order.filter((name) => !live.has(name));
  const liveShapes = new Set(T.parts.flatMap((part) => part.shapes));
  return {
    parts: T.parts.map((part) => ({ name: part.name, group: part.group ? part.group.index : -1, layer: part.layer.index, shapes: part.shapes.map((shape) => localShape(shape, part.group)) })),
    statics: statics.filter((item) => item.shapes && item.shapes.length && staticLayers.includes(item.layer)).map((item) => ({ name: item.name, rank: staticLayers.indexOf(item.layer), shapes: item.shapes.filter((shape) => !liveShapes.has(shape)).map((shape) => localShape(shape, null)) }))
  };
}
function localShape(shape, group2) {
  const o = group2 ? group2.origin : [0, 0, 0];
  const out2 = { kind: shape.kind };
  if (shape.F) out2.F = { o: sub32(shape.F.o, o), a: shape.F.a, u: shape.F.u, v: shape.F.v };
  for (const key of ["poly", "s0", "s1", "r", "radii", "flats"]) if (shape[key] !== void 0) out2[key] = shape[key];
  if (shape.o && shape.kind !== "body" && shape.kind !== "prism") out2.o = sub32(shape.o, o);
  if (shape.points) out2.points = shape.points.map((p) => sub32(p, o));
  if (shape.axes) out2.axes = shape.axes;
  if (shape.half) out2.half = shape.half;
  return pack(out2);
}

// third_party/anatomy/kit/turn-audit.mjs
var TAU3 = Math.PI * 2;
var EYE = [1, 0, 0, 0, 1, 0, 0, 0, 1];
var f2 = (v) => (Math.round(v * 100) / 100).toFixed(2);
var f3 = (v) => (Math.round(v * 1e3) / 1e3).toFixed(3);
var apply = (R, v) => [R[0] * v[0] + R[1] * v[1] + R[2] * v[2], R[3] * v[0] + R[4] * v[1] + R[5] * v[2], R[6] * v[0] + R[7] * v[1] + R[8] * v[2]];
var back = (R, v) => [R[0] * v[0] + R[3] * v[1] + R[6] * v[2], R[1] * v[0] + R[4] * v[1] + R[7] * v[2], R[2] * v[0] + R[5] * v[1] + R[8] * v[2]];
var place = (pose, p) => {
  const q = apply(pose.R, [p[0] - pose.origin[0], p[1] - pose.origin[1], p[2] - pose.origin[2]]);
  return [q[0] + pose.t[0], q[1] + pose.t[1], q[2] + pose.t[2]];
};
var unplace = (pose, p) => {
  const q = back(pose.R, [p[0] - pose.t[0], p[1] - pose.t[1], p[2] - pose.t[2]]);
  return [q[0] + pose.origin[0], q[1] + pose.origin[1], q[2] + pose.origin[2]];
};
function posed(shape, pose) {
  if (!pose) return shape;
  const out2 = { ...shape, _b: void 0, _f: void 0 };
  if (shape.F) out2.F = { o: place(pose, shape.F.o), a: apply(pose.R, shape.F.a), u: shape.F.u ? apply(pose.R, shape.F.u) : void 0, v: shape.F.v ? apply(pose.R, shape.F.v) : void 0 };
  if (shape.kind === "ball" || shape.kind === "box") out2.o = place(pose, shape.o);
  if (shape.flats) out2.flats = shape.flats.map(([nx, ny, nz, d]) => [...apply(pose.R, [nx, ny, nz]), d]);
  if (shape.axes) out2.axes = shape.axes.map((axis) => apply(pose.R, axis));
  if (shape.points) out2.points = shape.points.map((p) => place(pose, p));
  if (shape.tips) out2.tips = shape.tips.map((tip) => tip && place(pose, tip));
  if (shape.tipAxes) out2.tipAxes = shape.tipAxes.map((axis) => axis && apply(pose.R, axis));
  if (shape.cut) out2.cut = Array.isArray(shape.cut) ? shape.cut.map((one) => posed(one, pose)) : posed(shape.cut, pose);
  return out2;
}
var IDENTITY = { R: EYE, t: [0, 0, 0], origin: [0, 0, 0] };
var poseFor = (cams, group2) => group2 && group2 !== "static" ? { R: cams[group2.index].R, t: cams[group2.index].t, origin: group2.origin } : IDENTITY;
function polygonArea(poly) {
  let s = 0;
  for (let i = 0; i < poly.length; i++) {
    const a = poly[i];
    const b = poly[(i + 1) % poly.length];
    s += a[0] * b[1] - b[0] * a[1];
  }
  return s / 2;
}
function clipArea(subject, clip) {
  if (subject.length < 3 || clip.length < 3) return 0;
  const sign = polygonArea(clip) >= 0 ? 1 : -1;
  let out2 = subject;
  for (let i = 0; i < clip.length && out2.length; i++) {
    const a = clip[i];
    const b = clip[(i + 1) % clip.length];
    const side = (p) => sign * ((b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0]));
    const input = out2;
    out2 = [];
    for (let j = 0; j < input.length; j++) {
      const p = input[j];
      const q = input[(j + 1) % input.length];
      const sp = side(p);
      const sq = side(q);
      if (sp >= 0) out2.push(p);
      if (sp >= 0 !== sq >= 0) {
        const t = sp / (sp - sq);
        out2.push([p[0] + (q[0] - p[0]) * t, p[1] + (q[1] - p[1]) * t]);
      }
    }
  }
  return out2.length >= 3 ? Math.abs(polygonArea(out2)) : 0;
}
var pathPolys = (d) => [...(d ?? "").matchAll(/M([^M]*)/g)].map(([, body2]) => {
  const nums = (body2.match(/-?\d+(?:\.\d+)?(?:e-?\d+)?/g) ?? []).map(Number);
  const pts = [];
  for (let i = 0; i + 1 < nums.length; i += 2) pts.push([nums[i], nums[i + 1]]);
  return pts;
});
function convexHull(points) {
  const sorted = points.slice().sort((a, b) => a[0] - b[0] || a[1] - b[1]);
  if (sorted.length < 3) return sorted;
  const cross = (o, a, b) => (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0]);
  const lower = [];
  for (const p of sorted) {
    while (lower.length >= 2 && cross(lower[lower.length - 2], lower[lower.length - 1], p) <= 0) lower.pop();
    lower.push(p);
  }
  const upper = [];
  for (let i = sorted.length - 1; i >= 0; i--) {
    const p = sorted[i];
    while (upper.length >= 2 && cross(upper[upper.length - 2], upper[upper.length - 1], p) <= 0) upper.pop();
    upper.push(p);
  }
  return lower.slice(0, -1).concat(upper.slice(0, -1));
}
function footprints(run3, f) {
  if (run3.kind === "tube") return f.quadList.map(([buf, n]) => convexHull(Array.from({ length: n }, (_, i) => [buf[2 * i], buf[2 * i + 1]])));
  if (run3.kind === "fixed") return [Array.from({ length: f.hullN }, (_, i) => [f.hull[2 * i], f.hull[2 * i + 1]])];
  const polys = pathPolys(f.d[run3.role.fill]);
  return polys.length ? [convexHull(polys.flat())] : [];
}
function overlapArea(runA, fa, runB, fb) {
  if (fa.box[2] < fb.box[0] || fb.box[2] < fa.box[0] || fa.box[3] < fb.box[1] || fb.box[3] < fa.box[1]) return 0;
  let best = 0;
  for (const a of footprints(runA, fa)) for (const b of footprints(runB, fb)) best = Math.max(best, clipArea(a, b));
  return best;
}
function hausdorffish(A, B) {
  if (!A.length || !B.length) return 0;
  const seg = (p, a, b) => {
    const dx = b[0] - a[0];
    const dy = b[1] - a[1];
    const l = dx * dx + dy * dy;
    const t = l ? Math.max(0, Math.min(1, ((p[0] - a[0]) * dx + (p[1] - a[1]) * dy) / l)) : 0;
    return Math.hypot(p[0] - a[0] - dx * t, p[1] - a[1] - dy * t);
  };
  const one = (P, Q) => {
    let worst = 0;
    const m = Q.length;
    const n = P.length;
    for (let i = 0; i < n; i++) {
      const centre = Math.round(i / n * m);
      let best = Infinity;
      for (let w = -10; w <= 10; w++) {
        const j = ((centre + w) % m + m) % m;
        best = Math.min(best, seg(P[i], Q[j], Q[(j + 1) % m]));
      }
      if (best > 0.02) for (let j = 0; j < m; j++) best = Math.min(best, seg(P[i], Q[j], Q[(j + 1) % m]));
      worst = Math.max(worst, best);
    }
    return worst;
  };
  return Math.max(one(A, B), one(B, A));
}
var areaOfPath = (d) => pathPolys(d).reduce((sum, poly) => sum + Math.abs(polygonArea(poly)), 0);
function flatPolys(d) {
  const out2 = [];
  for (const [, body2] of (d ?? "").matchAll(/M([^M]*)/g)) {
    const nums = (body2.match(/-?\d+(?:\.\d+)?(?:e-?\d+)?/g) ?? []).map(Number);
    if (nums.length >= 6) out2.push(nums);
  }
  return out2;
}
var jitter = (a, b) => {
  const t = Math.sin(a * 12.9898 + b * 78.233) * 43758.5453;
  return t - Math.floor(t);
};
function toneRaster(layers, box, scale) {
  const x0 = box[0];
  const y0 = box[1];
  const w = Math.max(1, Math.ceil((box[2] - x0) * scale));
  const h = Math.max(1, Math.ceil((box[3] - y0) * scale));
  const out2 = new Float32Array(w * h).fill(-1);
  const owner = new Int16Array(w * h).fill(-1);
  for (const { polys, v, id } of layers) {
    if (!polys.length) continue;
    let ymin = Infinity;
    let ymax = -Infinity;
    for (const p of polys) for (let i = 1; i < p.length; i += 2) {
      if (p[i] < ymin) ymin = p[i];
      if (p[i] > ymax) ymax = p[i];
    }
    const r0 = Math.max(0, Math.floor((ymin - y0) * scale));
    const r1 = Math.min(h - 1, Math.ceil((ymax - y0) * scale));
    const hits = [];
    for (let row = r0; row <= r1; row++)
      for (let sub = 0; sub < 8; sub++) {
        const y = y0 + (row + (sub + 0.5) / 8) / scale;
        hits.length = 0;
        for (const p of polys) {
          const n = p.length;
          for (let i = 0; i < n; i += 2) {
            const ax = p[i];
            const ay = p[i + 1];
            const bx = p[(i + 2) % n];
            const by = p[(i + 3) % n];
            if (ay <= y === by <= y) continue;
            hits.push([ax + (y - ay) * (bx - ax) / (by - ay), by > ay ? 1 : -1]);
          }
        }
        if (hits.length < 2) continue;
        hits.sort((a, b) => a[0] - b[0]);
        let winding = 0;
        for (let k = 0; k < hits.length - 1; k++) {
          winding += hits[k][1];
          if (!winding) continue;
          const xa = hits[k][0];
          const xb = hits[k + 1][0];
          const c0 = Math.max(0, Math.floor((xa - x0) * scale));
          const c1 = Math.min(w - 1, Math.floor((xb - x0) * scale));
          for (let c = c0; c <= c1; c++) {
            if (Math.floor(jitter(c, row) * 8) !== sub) continue;
            if (c === c0 || c === c1) {
              const x = x0 + (c + jitter(row, c)) / scale;
              if (x < xa || x >= xb) continue;
            }
            out2[row * w + c] = v;
            owner[row * w + c] = id;
          }
        }
      }
  }
  return { out: out2, owner };
}
function toneLayers(run3, f) {
  const layers = [];
  run3.roles.forEach((role, r) => {
    const d = f.d[r];
    if (!d) return;
    if (role.type === "face") layers.push({ polys: flatPolys(d), v: f.q[r] / TURN.q, id: r });
    else if (role.type === "path" && role.name === "fill") layers.push({ polys: flatPolys(d), v: 2, id: r });
    else if (role.type === "path" && /^s[0-4]$/.test(role.name)) layers.push({ polys: flatPolys(d), v: Number(role.name.slice(1)), id: r });
    else if (role.name === "body") layers.push({ polys: flatPolys(d), v: 2, id: r });
    else if (role.name === "shine") layers.push({ polys: flatPolys(d), v: 4, id: r });
    else if (role.name === "shade") layers.push({ polys: flatPolys(d), v: 0, id: r });
  });
  return layers;
}
function visibleChange(run3, frames2, scale = 4) {
  const box = [Infinity, Infinity, -Infinity, -Infinity];
  for (const f of frames2) {
    box[0] = Math.min(box[0], f.box[0] - 1);
    box[1] = Math.min(box[1], f.box[1] - 1);
    box[2] = Math.max(box[2], f.box[2] + 1);
    box[3] = Math.max(box[3], f.box[3] + 1);
  }
  const rasters = frames2.map((f) => toneRaster(toneLayers(run3, f), box, scale));
  const steps = [];
  for (let i = 1; i < rasters.length; i++) {
    const a = rasters[i - 1];
    const b = rasters[i];
    let sum = 0;
    for (let j = 0; j < a.out.length; j++) {
      if (a.owner[j] === b.owner[j]) continue;
      const va = a.out[j];
      const vb = b.out[j];
      if (va < 0 || vb < 0) sum += 2;
      else {
        const d = Math.abs(va - vb);
        if (d > 1 / 16 + 1e-6) sum += d;
      }
    }
    steps.push(sum / (scale * scale));
  }
  return steps;
}
function surfacePoints(shape, spacing = 0.6) {
  return sampleShape(shape, Math.max(16, Math.round(TAU3 / Math.max(0.05, spacing / Math.max(1, shape.r ?? 3)))));
}
function sphereOf2(points) {
  const c = [0, 0, 0];
  for (const p of points) for (let i = 0; i < 3; i++) c[i] += p[i] / Math.max(1, points.length);
  let r = 0;
  for (const p of points) r = Math.max(r, Math.hypot(p[0] - c[0], p[1] - c[1], p[2] - c[2]));
  return { c, r };
}
function familiesOf(T, { sweep, clips }) {
  const groups = T.groups;
  const out2 = [];
  const roots = groups.filter((g) => g.kind === "turn" && !g.parent);
  if (sweep) out2.push({ name: "sweep", frame: 0.3, periodic: true, unit: "\xB0", ...sweep });
  else if (roots.length) out2.push({ name: "sweep", at: (x) => Object.fromEntries(roots.map((g) => [g.name, x])), from: 0, to: 360, frame: 0.3, periodic: true, unit: "\xB0" });
  for (const clip of clips ?? []) out2.push({ from: 0, frame: 1 / 60, unit: "s", ...clip });
  return out2;
}
function samplesOf2(family, frame) {
  const xs = [];
  if (family.periodic) {
    const count2 = Math.max(1, Math.round((family.to - family.from) / frame));
    for (let i = 0; i < count2; i++) xs.push(family.from + i * frame);
    return xs;
  }
  const count = Math.max(0, Math.ceil((family.to - family.from) / frame - 1e-9));
  for (let i = 0; i <= count; i++) xs.push(Math.min(family.to, family.from + i * frame));
  return xs;
}
var ORBIT_LINES = { separation: null, unseparated: "order", cycles: "order", forced: "order", swaps: "order", layers: "depth", rigid: "rigid", swept: "swept", posed: "posed", folds: "routes", self: "routes", crowding: "routes", endon: "routes", coverage: "coverage", depth: "depth", continuity: "continuity" };
var ORBIT_CHECKS = ["order", "rigid", "swept", "posed", "routes", "coverage", "continuity", "depth"];
function orbit(T, R, P, options2 = {}) {
  const started = Date.now();
  const { sweep = null, clips = [], poses = null, random = 2e3, step = 0.05, crowd = [], cover = [], fittings = [], depthAngles = 36, depthEvents = 36, quick = false, log: log2 = null, routeStates = 240, posedStep = null, only = null } = options2;
  const say = (text) => log2 && log2(text);
  const unknown = (only ?? []).filter((name) => !ORBIT_CHECKS.includes(name));
  if (unknown.length) throw new Error(`orbit: unknown check ${unknown.join(", ")} in only (the checks are ${ORBIT_CHECKS.join(", ")})`);
  const wants = (name) => !only || only.includes(name);
  const data = T.data;
  const scene = TURN.prepare(data, { unit: 1 });
  const runs = scene.runs;
  const groups = T.groups;
  const E = (P.elevation ?? 30) * Math.PI / 180;
  const result = { separation: [], unseparated: [], cycles: [], forced: [], swaps: [], layers: [], rigid: [], swept: [], posed: [], folds: [], self: [], crowding: [], endon: [], coverage: [], depth: [], continuity: [], notes: [], stats: {}, quick, skipped: Object.keys(ORBIT_LINES).filter((line) => ORBIT_LINES[line] && !wants(ORBIT_LINES[line])) };
  const families = familiesOf(T, { sweep, clips });
  const extra = typeof poses === "function" ? poses() : Array.isArray(poses) ? poses : [];
  const frameOf = (family) => quick ? family.frame * (family.periodic ? Math.max(1, 1 / family.frame) : 3) : family.frame;
  const label = (family, x) => `${family.name} ${x.toFixed(3)}${family.unit ?? ""}`;
  const emitAll = (values, frames2 = runs.map((run3) => TURN.frame(run3))) => {
    const cams = TURN.cams(scene, values);
    for (const run3 of runs) TURN.emit(run3, run3.group >= 0 ? cams[run3.group] : cams.world, frames2[run3.index]);
    return { cams, frames: frames2 };
  };
  say("separation");
  const allMargins = T.built?.report?.margins ?? [];
  for (const m of allMargins) if (m.margin < -0.08) result.separation.push({ a: m.a, b: m.b, margin: m.margin });
  result.stats.planes = allMargins.length;
  result.stats.tightest = allMargins.length ? Math.min(...allMargins.map((m) => m.margin)) : 0;
  const relationOf = (layer, i, j, cams) => {
    const plan = layer.planar;
    for (let p = 0; p < plan.length; p += 5)
      if (plan[p] === i && plan[p + 1] === j || plan[p] === j && plan[p + 1] === i) {
        const g = runs[plan[p]].group;
        const V2 = g >= 0 ? cams[g].V : cams.world.V;
        const s = plan[p + 2] * V2[0] + plan[p + 3] * V2[1] + plan[p + 4] * V2[2];
        return plan[p] === i ? s : -s;
      }
    const a = runs[i];
    const b = runs[j];
    const ca = a.group >= 0 ? cams[a.group] : cams.world;
    const cb = b.group >= 0 ? cams[b.group] : cams.world;
    const hit = TURN.gjk(a.cloud, ca, b.cloud, cb, null, 32, TURN.hintsOf(a, ca, b, cb, cams.world));
    const V = cams.world.V;
    return hit.n[0] * V[0] + hit.n[1] * V[1] + hit.n[2] * V[2];
  };
  const pairsOf = (layer) => {
    if (layer._pairs) return layer._pairs;
    const list = [];
    const seen = /* @__PURE__ */ new Set();
    for (let p = 0; p < layer.planar.length; p += 5) list.push([layer.planar[p], layer.planar[p + 1]]);
    for (let p = 0; p < layer.dynamic.length; p += 2) list.push([layer.dynamic[p], layer.dynamic[p + 1]]);
    for (let p = 0; p < (layer.framed ? layer.framed.length : 0); p += 6) list.push([layer.framed[p], layer.framed[p + 1]]);
    for (const gp of layer.groupPairs ?? []) for (const i of gp.a) for (const j of gp.b) list.push([i, j]);
    for (const [i, j] of list) seen.add(i * 65536 + j);
    for (const i of layer.free) for (const j of layer.parts) {
      if (i === j || runs[i].group === runs[j].group) continue;
      const key = Math.min(i, j) * 65536 + Math.max(i, j);
      if (seen.has(key)) continue;
      seen.add(key);
      list.push([Math.min(i, j), Math.max(i, j)]);
    }
    layer._pairs = list;
    return list;
  };
  const checkState = (values, tag, previous, record) => {
    const { cams, frames: frames2 } = emitAll(values);
    const orders = [];
    scene.layers.forEach((layer, index) => {
      const stats = {};
      const order = TURN.order(layer, frames2, cams, previous ? previous[index] : null, stats, scene);
      orders.push(order);
      if (stats.forced) result.forced.push({ layer: layer.name, state: tag, forced: stats.forced });
      const framed = layer.framed ?? [];
      for (let p = 0; p < framed.length; p += 6) {
        const i = framed[p];
        const j = framed[p + 1];
        if (TURN.disjoint(frames2[i], frames2[j], 0.1)) continue;
        const g = framed[p + 2];
        const R2 = g >= 0 ? cams[g].R : EYE;
        const n2 = [R2[0] * framed[p + 3] + R2[1] * framed[p + 4] + R2[2] * framed[p + 5], R2[3] * framed[p + 3] + R2[4] * framed[p + 4] + R2[5] * framed[p + 5], R2[6] * framed[p + 3] + R2[7] * framed[p + 4] + R2[8] * framed[p + 5]];
        const extent = (run3) => {
          const c = run3.group >= 0 ? cams[run3.group] : cams.world;
          let lo2 = Infinity;
          let hi = -Infinity;
          for (let q = 0; q < run3.cloud.length; q += 3) {
            const x = run3.cloud[q];
            const y = run3.cloud[q + 1];
            const z = run3.cloud[q + 2];
            const v = n2[0] * (c.R[0] * x + c.R[1] * y + c.R[2] * z + c.t[0]) + n2[1] * (c.R[3] * x + c.R[4] * y + c.R[5] * z + c.t[1]) + n2[2] * (c.R[6] * x + c.R[7] * y + c.R[8] * z + c.t[2]);
            if (v < lo2) lo2 = v;
            if (v > hi) hi = v;
          }
          return [lo2, hi];
        };
        const margin = extent(runs[j])[0] - extent(runs[i])[1];
        if (margin < -0.08) result.unseparated.push({ layer: layer.name, state: tag, a: runs[i].name, b: runs[j].name, margin, framed: true });
      }
      for (const gp of layer.groupPairs ?? []) {
        const R2 = gp.frame >= 0 ? cams[gp.frame].R : EYE;
        const nw = [R2[0] * gp.n[0] + R2[1] * gp.n[1] + R2[2] * gp.n[2], R2[3] * gp.n[0] + R2[4] * gp.n[1] + R2[5] * gp.n[2], R2[6] * gp.n[0] + R2[7] * gp.n[1] + R2[8] * gp.n[2]];
        const along = (list, high) => {
          let best = high ? -Infinity : Infinity;
          for (const index2 of list) {
            const run3 = runs[index2];
            const c = run3.group >= 0 ? cams[run3.group] : cams.world;
            for (let q = 0; q < run3.cloud.length; q += 3) {
              const x = run3.cloud[q];
              const y = run3.cloud[q + 1];
              const z = run3.cloud[q + 2];
              const v = nw[0] * (c.R[0] * x + c.R[1] * y + c.R[2] * z + c.t[0]) + nw[1] * (c.R[3] * x + c.R[4] * y + c.R[5] * z + c.t[1]) + nw[2] * (c.R[6] * x + c.R[7] * y + c.R[8] * z + c.t[2]);
              best = high ? Math.max(best, v) : Math.min(best, v);
            }
          }
          return best;
        };
        const margin = along(gp.b, false) - along(gp.a, true);
        if (margin < -0.08) result.unseparated.push({ layer: layer.name, state: tag, a: runs[gp.a[0]].name, b: runs[gp.b[0]].name, margin, framed: true });
      }
      const n = layer.parts.length;
      const local = layer.local;
      const adj = Array.from({ length: n }, () => []);
      const indeg = new Int32Array(n);
      for (const [i, j] of pairsOf(layer)) {
        if (TURN.disjoint(frames2[i], frames2[j], 0.1)) continue;
        const ri = runs[i];
        const rj = runs[j];
        if (stats.unseparated && ri.group !== rj.group) {
          const ca = ri.group >= 0 ? cams[ri.group] : cams.world;
          const cb = rj.group >= 0 ? cams[rj.group] : cams.world;
          const hit = TURN.gjk(ri.cloud, ca, rj.cloud, cb, null, 32, TURN.hintsOf(ri, ca, rj, cb, cams.world));
          if (hit.margin < -0.08) result.unseparated.push({ layer: layer.name, state: tag, a: ri.name, b: rj.name, margin: hit.margin });
        }
        const s = relationOf(layer, i, j, cams);
        if (s < 1e-7 && s > -1e-7) continue;
        const from = s > 0 ? local.get(i) : local.get(j);
        const to = s > 0 ? local.get(j) : local.get(i);
        adj[from].push(to);
        indeg[to]++;
      }
      const queue = [];
      for (let v = 0; v < n; v++) if (!indeg[v]) queue.push(v);
      let seen = 0;
      while (queue.length) {
        const v = queue.pop();
        seen++;
        for (const w of adj[v]) if (--indeg[w] === 0) queue.push(w);
      }
      if (seen < n) {
        const stuck = [];
        for (let v = 0; v < n; v++) if (indeg[v] > 0) stuck.push(runs[layer.parts[v]].name);
        let split = null;
        for (const m of T.built?.report?.margins ?? []) if (stuck.includes(m.a) && stuck.includes(m.b) && (!split || m.margin > split.margin)) split = m;
        const plane = split && T.built.planesByName ? T.built.planesByName.get(`${split.a}|${split.b}`) : null;
        result.cycles.push({ layer: layer.name, state: tag, parts: stuck.slice(0, 8), split: plane ? { part: split.b, a: split.a, b: split.b, n: plane.n, d: plane.d } : null });
      }
    });
    if (record) record(cams, frames2, orders);
    return { cams, frames: frames2, orders };
  };
  const swapsOf = (a, b) => {
    const list = [];
    scene.layers.forEach((layer, index) => {
      const pa = a.orders[index];
      const pb = b.orders[index];
      const rankA = /* @__PURE__ */ new Map();
      pa.forEach((g, at) => rankA.set(g, at));
      const rankB = /* @__PURE__ */ new Map();
      pb.forEach((g, at) => rankB.set(g, at));
      const moved2 = /* @__PURE__ */ new Set();
      for (let at = 0; at < pb.length; at++) if (pa[at] !== pb[at]) moved2.add(pb[at]);
      const moving = [...moved2];
      for (let x = 0; x < moving.length; x++)
        for (const j of layer.parts) {
          const i = moving[x];
          if (i === j || moved2.has(j) && j < i) continue;
          if (rankA.get(i) < rankA.get(j) === rankB.get(i) < rankB.get(j)) continue;
          if (T.parts[i].route && T.parts[i].route === T.parts[j].route && Math.abs(T.parts[i].chunk - T.parts[j].chunk) <= 1) continue;
          const area = Math.min(overlapArea(runs[i], a.frames[i], runs[j], a.frames[j]), overlapArea(runs[i], b.frames[i], runs[j], b.frames[j]));
          list.push({ layer: layer.name, i, j, area });
        }
    });
    return list;
  };
  const clone = (frames2) => frames2.map((f) => ({ ...f, d: f.d.slice(), box: Float64Array.from(f.box), hull: Float64Array.from(f.hull), quadList: f.quadList, fill: void 0 }));
  const flush = /* @__PURE__ */ new Set();
  for (const m of T.built?.report?.margins ?? []) if (Math.abs(m.margin) < 0.05) flush.add(`${m.a}|${m.b}`);
  const flushOf = (a, b) => flush.has(`${a}|${b}`) || flush.has(`${b}|${a}`);
  const changes = [];
  let orderStates = 0;
  for (const family of wants("order") ? families : []) {
    const xs = samplesOf2(family, frameOf(family));
    say(`order scan ${family.name}: ${xs.length} states`);
    let previous = null;
    const local = [];
    for (const x of xs) {
      const values = family.at(x);
      const tag = label(family, x);
      const state = checkState(values, tag, previous ? previous.orders : null);
      orderStates++;
      const snapshot = { orders: state.orders.map((o) => Int32Array.from(o)), frames: clone(state.frames), x };
      if (previous) {
        const swaps = swapsOf(previous, snapshot);
        for (const swap of swaps) {
          if (swap.area <= 0.25) continue;
          const layerIndex = scene.layers.findIndex((l) => l.name === swap.layer);
          const layer = scene.layers[layerIndex];
          const prior = previous.orders[layerIndex];
          const probe2 = (value) => {
            const { cams, frames: frames3 } = emitAll(family.at(value));
            const order = TURN.order(layer, frames3, cams, prior, {}, scene);
            const at = /* @__PURE__ */ new Map();
            order.forEach((g, index) => at.set(g, index));
            return { first: at.get(swap.i) < at.get(swap.j), frames: frames3 };
          };
          const start = probe2(previous.x).first;
          let lo2 = previous.x;
          let hi = x;
          let frames2 = null;
          for (let it = 0; it < 16; it++) {
            const mid = (lo2 + hi) / 2;
            const next = probe2(mid);
            if (next.first === start) lo2 = mid;
            else {
              hi = mid;
              frames2 = next.frames;
            }
          }
          if (!frames2) frames2 = probe2(hi).frames;
          const area = overlapArea(runs[swap.i], frames2[swap.i], runs[swap.j], frames2[swap.j]);
          const built = flushOf(runs[swap.i].name, runs[swap.j].name);
          if (area > (built ? 0.5 : 0.25)) result.swaps.push({ layer: swap.layer, a: runs[swap.i].name, b: runs[swap.j].name, area, at: `${family.name} ${f3(hi)}` });
        }
        if (swaps.length) local.push({ family, x, count: swaps.length, pairs: swaps });
      }
      previous = snapshot;
    }
    changes.push(...local);
    const share = Math.round((quick ? Math.min(200, random) : random) / families.length);
    let seed = 12345 + families.indexOf(family);
    const rand = () => (seed = (seed * 1103515245 + 12345) % 2147483648) / 2147483648;
    const events = local.flatMap((c) => [c.x - (family.delta ?? (family.periodic ? 1e-3 : family.frame / 50)), c.x + (family.delta ?? (family.periodic ? 1e-3 : family.frame / 50))]);
    say(`order scan ${family.name}: ${share} random states, ${events.length} event states`);
    for (let i = 0; i < share; i++) {
      const x = family.from + rand() * (family.to - family.from);
      checkState(family.at(x), `random ${label(family, x)}`, null);
    }
    for (const x of events.slice(0, quick ? 100 : 4e3)) checkState(family.at(x), `event ${label(family, x)}`, null);
    orderStates += share + Math.min(events.length, quick ? 100 : 4e3);
  }
  for (const values of wants("order") ? extra.slice(0, quick ? 100 : extra.length) : []) checkState(values, `pose ${JSON.stringify(values).slice(0, 60)}`, null);
  result.stats.orderStates = orderStates + extra.length;
  result.stats.changes = changes.length;
  result.changes = changes.sort((a, b) => b.count - a.count).slice(0, 10).map((c) => ({ family: c.family.name, x: c.x, count: c.count, pairs: c.pairs.slice(0, 4).map((p) => `${runs[p.i].name} / ${runs[p.j].name}`), at: c.family.at }));
  say("rigid");
  const mounts = mountsOf(R.tubes, R.solids);
  if (wants("rigid")) {
    for (const c of clearances(R.tubes, R.solids, { mounts })) result.rigid.push({ kind: "clearance", text: `${c.kind} ${c.tube} \xD7 ${c.other} clearance ${f2(c.clearance)} < ${f2(c.need)}` });
    for (const e of terminals(R.tubes, R.solids, { mounts })) result.rigid.push({ kind: "terminal", text: `${e.tube} ${e.end} ${Number.isFinite(e.d) ? f2(e.d) : "\u221E"} from ${e.nearest}` });
    const held = supports(R.solids, R.tubes);
    for (const name of held.loose) result.rigid.push({ kind: "support", text: `loose ${name}` });
    for (const name of held.hanging ?? []) result.rigid.push({ kind: "support", text: `hanging ${name}` });
    for (const d of held.sunk) result.rigid.push({ kind: "support", text: `sunk ${d.a} \xD7 ${d.b} ${f2(d.depth)} deep` });
    for (const c of solidClearances(R.solids)) result.rigid.push({ kind: "solid", text: `${c.tube} \xD7 ${c.other} sunk ${f2(-c.clearance)}` });
  }
  say("swept");
  const liveShapes = [];
  for (const part of T.parts) for (const shape of part.shapes) liveShapes.push({ shape, part, group: part.group });
  const liveSet = new Set(liveShapes.map((entry) => entry.shape));
  const staticShapes = [];
  for (const item of R.items) for (const shape of item.shapes ?? []) if (!liveSet.has(shape)) staticShapes.push({ shape, item });
  const pointsCache = /* @__PURE__ */ new Map();
  const pointsOf = (shape) => {
    if (!pointsCache.has(shape)) pointsCache.set(shape, surfacePoints(shape));
    return pointsCache.get(shape);
  };
  for (const g of wants("swept") ? groups : []) {
    if (g.kind !== "turn" || g.parent) continue;
    const mine = liveShapes.filter((entry) => entry.group === g);
    const slices = /* @__PURE__ */ new Map();
    for (const { shape } of mine)
      for (const p of pointsOf(shape)) {
        const band = Math.floor(p[2] * 2);
        const r = Math.hypot(p[0] - g.origin[0], p[1] - g.origin[1]);
        slices.set(band, Math.max(slices.get(band) ?? 0, r));
      }
    const flagged = [];
    for (const { shape, item } of staticShapes) {
      let worst = Infinity;
      for (const p of pointsOf(shape)) {
        const r = Math.hypot(p[0] - g.origin[0], p[1] - g.origin[1]);
        for (const band of [Math.floor(p[2] * 2), Math.floor(p[2] * 2 - 0.2), Math.floor(p[2] * 2 + 0.2)]) {
          const reach = slices.get(band);
          if (reach !== void 0) worst = Math.min(worst, r - reach);
        }
      }
      if (worst < -0.1) flagged.push({ shape, item });
    }
    for (const { shape, item } of flagged) {
      let deepest = 0;
      let where = 0;
      const count = quick ? 90 : 720;
      for (let i = 0; i < count; i++) {
        const angle = i * 360 / count;
        const cams = TURN.cams(scene, { [g.name]: angle });
        const pose = poseFor(cams, g);
        const b = boundsOf(shape);
        for (const { shape: other } of mine)
          for (const p of pointsOf(other)) {
            const q = place(pose, p);
            if (q[0] < b.min[0] - 0.5 || q[0] > b.max[0] + 0.5 || q[1] < b.min[1] - 0.5 || q[1] > b.max[1] + 0.5 || q[2] < b.min[2] - 0.5 || q[2] > b.max[2] + 0.5) continue;
            const d = sdf(shape, q);
            if (d < deepest) {
              deepest = d;
              where = angle;
            }
          }
      }
      if (deepest < -0.1) result.swept.push({ text: `${item.name} \xD7 ${g.name} sweep: ${f2(-deepest)} deep at ${f2(where)}\xB0` });
    }
  }
  say("posed");
  const posedStates = [];
  for (const family of families) {
    const frame = posedStep ?? (family.periodic ? quick ? 4 : 0.5 : family.frame * (quick ? 4 : 1));
    for (const x of samplesOf2(family, frame)) posedStates.push({ values: family.at(x), tag: label(family, x) });
  }
  for (const values of extra.slice(0, quick ? 40 : extra.length)) posedStates.push({ values, tag: "pose" });
  const entries = [
    ...liveShapes.map((entry) => ({ ...entry, kind: "live", sphere: sphereOf2(pointsOf(entry.shape)) })),
    ...staticShapes.map((entry) => ({ shape: entry.shape, part: { name: entry.item.name }, group: "static", item: entry.item, kind: "static", sphere: sphereOf2(pointsOf(entry.shape)) }))
  ];
  const posedSeen = /* @__PURE__ */ new Set();
  const movingGroups = groups.filter((g) => !(g.kind === "turn" && !g.parent));
  const needsStatic = movingGroups.length > 0;
  for (const { values, tag } of wants("posed") ? posedStates : []) {
    const cams = TURN.cams(scene, values);
    const placed2 = entries.map((entry) => {
      if (entry.kind === "static") return { entry, c: entry.sphere.c, pose: null };
      const pose = poseFor(cams, entry.group);
      return { entry, c: entry.group ? place(pose, entry.sphere.c) : entry.sphere.c, pose: entry.group ? pose : null };
    });
    placed2.sort((a, b) => a.c[0] - a.entry.sphere.r - (b.c[0] - b.entry.sphere.r));
    for (let i = 0; i < placed2.length; i++) {
      const A0 = placed2[i];
      const reachA = A0.c[0] + A0.entry.sphere.r + 0.5;
      for (let j = i + 1; j < placed2.length; j++) {
        const B0 = placed2[j];
        if (B0.c[0] - B0.entry.sphere.r > reachA) break;
        const a = A0.entry;
        const b = B0.entry;
        if (a.group === b.group) continue;
        if (a.kind === "static" && b.kind === "static") continue;
        if ((a.kind === "static" || b.kind === "static") && !needsStatic) continue;
        if (a.kind === "static" || b.kind === "static") {
          const live = a.kind === "static" ? b : a;
          if (!live.group || live.group.kind === "turn" && !live.group.parent) continue;
        }
        if (a.shape.kind === "tube" && b.shape.kind === "tube") continue;
        if (Math.hypot(A0.c[0] - B0.c[0], A0.c[1] - B0.c[1], A0.c[2] - B0.c[2]) > a.sphere.r + b.sphere.r + 0.5) continue;
        const key = `${a.part.name}|${b.part.name}`;
        if (posedSeen.has(key)) continue;
        const pa = A0.pose ?? IDENTITY;
        const pb = B0.pose ?? IDENTITY;
        let deepest = 0;
        for (const p of pointsOf(a.shape)) {
          const d = sdf(b.shape, unplace(pb, place(pa, p)));
          if (d < deepest) deepest = d;
        }
        for (const p of pointsOf(b.shape)) {
          const d = sdf(a.shape, unplace(pa, place(pb, p)));
          if (d < deepest) deepest = d;
        }
        const limit = a.shape.kind === "tube" || b.shape.kind === "tube" ? -0.1 : -0.5;
        if (deepest < limit) {
          posedSeen.add(key);
          result.posed.push({ text: `${a.part.name} \xD7 ${b.part.name} through ${f2(-deepest)} at ${tag}` });
        }
      }
    }
  }
  result.stats.posedStates = posedStates.length;
  say("folds, self, crowding, endon");
  const routes = T.routes ?? [];
  const turnGroups = groups.filter((g) => g.kind === "turn" && !g.parent);
  const tubesAll = R.tubes;
  const linkMap = linksOf(tubesAll, mounts);
  const routeSample = [];
  {
    const all = posedStates.filter((s) => s.tag !== "pose");
    const stride = Math.max(1, Math.floor(all.length / (quick ? 48 : routeStates)));
    for (let i = 0; i < all.length; i += stride) routeSample.push(all[i]);
    for (const values of extra.slice(0, 24)) routeSample.push({ values, tag: "pose" });
  }
  const foldSeen = /* @__PURE__ */ new Set();
  const crowdSeen = /* @__PURE__ */ new Set();
  const lo = E * 180 / Math.PI;
  for (const route of wants("routes") ? routes : []) {
    const g = route.group;
    const root = g && g.kind === "turn" && !g.parent;
    const records = R.routes.filter((r) => r.name === route.name);
    const groupParts = T.parts.filter((part) => part.group === g);
    const itemsAt = (pose) => groupParts.map((part) => ({ name: part.name, route: part.route, shapes: pose ? part.shapes.map((shape) => posed(shape, pose)) : part.shapes }));
    const views = [];
    if (!g) views.push({ P, pose: null, tag: "rest" });
    else if (root) {
      const count = quick ? 72 : 720;
      for (let i = 0; i < count; i++) {
        const x = i * 360 / count;
        views.push({ P: { ...P, azimuth: (P.azimuth ?? 45) - x }, pose: null, tag: `${f2(x)}\xB0` });
      }
    } else for (const { values, tag } of routeSample) views.push({ P, pose: poseFor(TURN.cams(scene, values), g), tag });
    for (const view of views) {
      const posedRecords = view.pose ? records.map((r) => ({ ...r, points: r.points.map((p) => place(view.pose, p)) })) : records;
      const items = itemsAt(view.pose);
      for (const fold of folds(posedRecords, view.P, { items })) {
        const key = `${fold.name}|${fold.kind}`;
        if (foldSeen.has(key)) continue;
        foldSeen.add(key);
        result.folds.push({ text: `${fold.name} ${fold.kind} at ${view.tag}: turns ${fold.flatTurn.toFixed(0)}\xB0 on screen${fold.kind === "pinch" ? ` round a ${f2(fold.radius)} px bend` : ` for ${fold.realTurn.toFixed(0)}\xB0 in 3D`}` });
      }
      for (const s of selfOverlaps(items.filter((item) => item.route === route.name), view.P)) {
        const key = `self|${s.name}`;
        if (foldSeen.has(key)) continue;
        foldSeen.add(key);
        result.self.push({ text: `${s.name} folds back at ${view.tag}: radius ${f2(s.radius)} px under its half-width ${f2(s.width)} px` });
      }
    }
    const dense = route.world;
    const total = pathLength(dense);
    const stations = resample(dense, 0.25);
    const rotations = !g || root || g.upright ? [null] : routeSample.map(({ values }) => poseFor(TURN.cams(scene, values), g).R);
    const bad = [];
    let walked = 0;
    for (let i = 1; i < stations.length - 1; i++) {
      walked += len3(sub3(stations[i], stations[i - 1]));
      if (route.gaps.some(([a, b]) => walked >= a - 1e-6 && walked <= b + 1e-6)) continue;
      if (fittings.some(([name, a, b]) => name === route.name && walked >= a && walked <= b)) continue;
      const t0 = unit3(sub3(stations[i + 1], stations[i - 1]));
      for (const Rm of rotations) {
        const t = Rm ? apply(Rm, t0) : t0;
        const phi = Math.asin(Math.max(-1, Math.min(1, t[2]))) * 180 / Math.PI;
        if (phi > lo - 15 && phi < lo + 15 || phi > -lo - 15 && phi < -lo + 15) {
          bad.push({ at: walked, phi });
          break;
        }
      }
    }
    if (bad.length) result.endon.push({ text: `${route.name} points within 15\xB0 of the view along ${f2(bad[0].at)}\u2013${f2(bad[bad.length - 1].at)} of ${f2(total)} (slope ${bad[0].phi.toFixed(1)}\xB0): bend flat or inside a fitting` });
  }
  const crowdViews = [];
  for (const g of turnGroups) {
    const count = quick ? 24 : 72;
    for (let i = 0; i < count; i++) crowdViews.push({ group: g, P: { ...P, azimuth: (P.azimuth ?? 45) - i * 360 / count }, tag: `${f2(i * 360 / count)}\xB0`, values: null });
  }
  const others = [...new Set(routes.map((route) => route.group).filter((g) => g && !(g.kind === "turn" && !g.parent)))];
  for (const g of others) for (const { values, tag } of routeSample.slice(0, quick ? 24 : 72)) crowdViews.push({ group: g, P, tag, values });
  for (const view of wants("routes") ? crowdViews : []) {
    const g = view.group;
    const pose = view.values ? poseFor(TURN.cams(scene, view.values), g) : null;
    const mineRoutes = R.routes.filter((r) => routes.some((route) => route.name === r.name && route.group === g)).map((r) => pose ? { ...r, points: r.points.map((p) => place(pose, p)) } : r);
    if (!mineRoutes.length) continue;
    const groupParts = T.parts.filter((part) => part.group === g);
    const items = groupParts.map((part) => ({ name: part.name, route: part.route, shapes: pose ? part.shapes.map((shape) => posed(shape, pose)) : part.shapes }));
    const rods = slenderOf(items.flatMap((item) => item.shapes).filter((shape) => shape.kind !== "tube"));
    for (const c of crowding(mineRoutes, view.P, { links: linkMap, items, allow: crowd, rods })) {
      const key = [c.a, c.b, c.where].join("|");
      if (crowdSeen.has(key)) continue;
      crowdSeen.add(key);
      result.crowding.push({ text: `${c.a} ${c.where} \xD7 ${c.b} at ${view.tag}: outlines ${c.gap < 0 ? `overlap ${f2(-c.gap)}` : `${f2(c.gap)} apart`} px` });
    }
  }
  say("coverage");
  const rest = emitAll(Object.fromEntries(groups.map((g) => [g.name, g.kind === "free" ? null : 0])));
  const coverItems = T.parts.map((part) => {
    const run3 = runs[part.id];
    const f = rest.frames[part.id];
    const outline = run3.kind === "fixed" ? part.svg : run3.kind === "tube" ? f.d[run3.role.body] : f.d[run3.role.fill];
    return { name: part.name, svg: `<path d="${outline}"/>`, shapes: part.shapes };
  });
  for (const c of wants("coverage") ? coverage(coverItems, P, { allow: cover }) : []) result.coverage.push({ text: `${c.name} its shapes cover ${Math.round(c.share * 100)}% of its drawing` });
  say("continuity");
  if (wants("continuity")) {
    TURN.exact(true);
    try {
      continuity(T, scene, runs, groups, { step, quick, result, say, families, frameOf });
    } finally {
      TURN.exact(false);
    }
  }
  say("depth oracle");
  const depthStates = [];
  const first = families[0];
  if (first) for (let i = 0; i < (quick ? 6 : depthAngles); i++) {
    const x = first.from + (first.to - first.from) * i / (quick ? 6 : depthAngles);
    depthStates.push({ values: first.at(x), tag: label(first, x) });
  }
  for (const family of families.slice(1)) for (let i = 0; i <= (quick ? 3 : 12); i++) {
    const x = family.from + (family.to - family.from) * i / (quick ? 3 : 12);
    depthStates.push({ values: family.at(x), tag: label(family, x) });
  }
  for (const change of result.changes.slice(0, quick ? 4 : depthEvents)) depthStates.push({ values: change.at(change.x), tag: `${change.family} ${f3(change.x)}` });
  let checked = 0;
  for (const { values, tag } of wants("depth") ? depthStates : []) {
    const state = checkState(values, `depth ${tag}`, null);
    scene.layers.forEach((layer, index) => {
      const items = [];
      for (const global of layer.parts) {
        const part = T.parts[global];
        const pose = poseFor(state.cams, part.group);
        items.push({ name: part.name, global, shapes: part.shapes.map((shape) => posed(shape, pose)), route: part.route, chunk: part.chunk });
      }
      const ranks = new Map((T.order.length ? T.order : T.layers.map((l) => l.name)).map((name, at) => [name, at]));
      for (const item of R.items) if (item.layer && ranks.has(item.layer) && item.shapes && item.shapes.length) items.push({ name: item.name, static: ranks.get(item.layer) < ranks.get(layer.name) ? "below" : "above", shapes: item.shapes });
      const overlaps2 = overlapsOf(items, P, { step: quick ? 0.5 : 0.25, skip: (a, b) => sameRun(a, b) || a.static && b.static });
      for (const pair of overlaps2.pairs) {
        const a = items[pair.a];
        const b = items[pair.b];
        if (!a.static === !b.static) continue;
        const sideIndex = a.static ? 0 : 1;
        const fixed = a.static ? a : b;
        const moving = a.static ? b : a;
        const staticFront = pair.front[sideIndex].area >= overlaps2.least;
        const liveFront = pair.front[1 - sideIndex].area >= overlaps2.least;
        if (fixed.static === "below" && staticFront) result.layers.push({ text: `${fixed.name} (under ${layer.name}) is in front of ${moving.name} at ${tag}: ${f2(pair.front[sideIndex].area)} px\xB2` });
        if (fixed.static === "above" && liveFront) result.layers.push({ text: `${fixed.name} (over ${layer.name}) is behind ${moving.name} at ${tag}: ${f2(pair.front[1 - sideIndex].area)} px\xB2` });
      }
      const rank = /* @__PURE__ */ new Map();
      state.orders[index].forEach((global, at) => rank.set(global, at));
      for (const pair of overlaps2.pairs) {
        if (items[pair.a].static || items[pair.b].static) continue;
        checked++;
        const aFront = pair.front[0].area >= overlaps2.least;
        const bFront = pair.front[1].area >= overlaps2.least;
        if (aFront === bFront) continue;
        const front = items[aFront ? pair.a : pair.b];
        const backItem = items[aFront ? pair.b : pair.a];
        if (rank.get(front.global) < rank.get(backItem.global)) result.depth.push({ text: `${layer.name} at ${tag}: ${front.name} is in front of ${backItem.name} but drawn first (${f2(pair.front[aFront ? 0 : 1].area)} px\xB2)` });
      }
    });
  }
  result.stats.depthStates = depthStates.length;
  result.stats.depthPairs = checked;
  result.stats.seconds = (Date.now() - started) / 1e3;
  return result;
}
function continuity(T, scene, runs, groups, { step, quick, result, say, families = [], frameOf = (f) => f.frame }) {
  const stepSize = quick ? step * 10 : step;
  const measures = [];
  const worst = { q: 0, birth: 0, dot: 0, fade: 0, motion: 0, merge: 0 };
  const failures = [];
  const k = scene.P.scale * Math.sqrt(1.6);
  const sweeps = [];
  for (const g of groups) {
    if (g.loose) continue;
    if (g.kind === "turn") sweeps.push({ group: g, from: 0, to: 360, unit: "\xB0" });
    else if (g.kind === "hinge") sweeps.push({ group: g, from: g.range[0], to: g.range[1], unit: "\xB0" });
    else sweeps.push({ group: g, from: 0, to: g.travel, unit: "" });
  }
  for (const sweep of sweeps) {
    const g = sweep.group;
    const parts = runs.filter((run3) => run3.group === g.index);
    if (!parts.length) continue;
    const span = sweep.to - sweep.from;
    const delta = g.kind === "slide" ? Math.max(0.01, span / 400) : stepSize;
    const count = Math.max(1, Math.round(span / delta));
    const reach = parts.map((run3) => {
      let r = 0;
      const part = T.parts[run3.index];
      for (const p of part.samples) r = Math.max(r, g.kind === "slide" ? 0 : Math.hypot(p[0], p[1]));
      return r;
    });
    const valuesAt = (x) => ({ [g.name]: x });
    const emitPart = (run3, x, f) => {
      const cams = TURN.cams(scene, valuesAt(x));
      TURN.emit(run3, cams[g.index], f);
      return f;
    };
    say(`continuity ${g.name}: ${count} steps of ${delta}${sweep.unit} over ${parts.length} parts`);
    const snap = (run3, f) => {
      const roles = run3.roles;
      const out2 = { faces: [], sheets: [], dots: [], planes: [], fade: {}, outline: null, levels: f.levels ?? 0 };
      roles.forEach((role, r) => {
        if (role.type === "face") out2.faces.push([f.d[r] ? areaOfPath(f.d[r]) : 0, f.q[r], Boolean(f.d[r])]);
        else if (role.type === "path" && /^s[0-4]$/.test(role.name)) out2.sheets.push([areaOfPath(f.d[r]), (f.d[r].match(/M/g) ?? []).length]);
        else if (role.type === "dot") out2.dots.push(f.o[r]);
        else if (role.type === "plane") out2.planes.push(f.o[r]);
      });
      for (const [prefix, set] of Object.entries(f.fade ?? {})) {
        const map = /* @__PURE__ */ new Map();
        set.key.forEach((key, i) => map.set(key, Math.round(set.alpha[i] * TURN.levels) / TURN.levels));
        out2.fade[prefix] = map;
      }
      const edge = run3.role.fill !== void 0 ? f.d[run3.role.fill] : run3.role.body !== void 0 ? f.d[run3.role.body] : "";
      out2.outline = run3.kind === "fixed" ? [Array.from({ length: f.hullN }, (_, i) => [f.hull[2 * i], f.hull[2 * i + 1]])] : pathPolys(edge);
      out2.slots = run3.slots;
      return out2;
    };
    const compare = (run3, a, b, dx, reachPx) => {
      const m = { q: 0, birth: 0, dot: 0, fade: 0, motion: 0, merge: 0 };
      for (let i = 0; i < Math.min(a.faces.length, b.faces.length); i++) {
        const [areaA, qa, onA] = a.faces[i];
        const [areaB, qb, onB] = b.faces[i];
        if (onA && onB) m.q = Math.max(m.q, Math.abs(qa - qb) * 16 / TURN.q);
        if (onA !== onB) m.birth = Math.max(m.birth, onA ? areaA : areaB);
        m.area = Math.max(m.area ?? 0, Math.abs(areaA - areaB));
      }
      for (let i = 0; i < Math.min(a.sheets.length, b.sheets.length); i++) {
        const [areaA, countA] = a.sheets[i];
        const [areaB, countB] = b.sheets[i];
        if (!countA !== !countB) m.birth = Math.max(m.birth, Math.abs(areaA - areaB));
        m.area = Math.max(m.area ?? 0, Math.abs(areaA - areaB));
      }
      for (let i = 0; i < Math.min(a.dots.length, b.dots.length); i++) m.dot = Math.max(m.dot, Math.abs(a.dots[i] - b.dots[i]));
      for (let i = 0; i < Math.min(a.planes.length, b.planes.length); i++) m.dot = Math.max(m.dot, Math.abs(a.planes[i] - b.planes[i]));
      for (const prefix of /* @__PURE__ */ new Set([...Object.keys(a.fade), ...Object.keys(b.fade)])) {
        const A0 = a.fade[prefix] ?? /* @__PURE__ */ new Map();
        const B0 = b.fade[prefix] ?? /* @__PURE__ */ new Map();
        for (const key of /* @__PURE__ */ new Set([...A0.keys(), ...B0.keys()])) m.fade = Math.max(m.fade, Math.abs((A0.get(key) ?? 0) - (B0.get(key) ?? 0)));
      }
      const slots = Math.max(run3.slots.bevel ?? 0, run3.slots.ribs ?? 0);
      if (slots && (a.levels > slots || b.levels > slots)) m.merge = Math.max(a.levels, b.levels) - slots;
      if (a.outline.length && b.outline.length && a.outline[0].length && b.outline[0].length) m.motion = Math.max(0, hausdorffish(a.outline[0], b.outline[0]) - (1.5 * reachPx * dx + 0.05));
      return m;
    };
    const frames2 = parts.map((run3) => TURN.frame(run3));
    let previous = parts.map((run3, i) => snap(run3, emitPart(run3, sweep.from, frames2[i])));
    for (let c = 1; c <= count; c++) {
      const x = sweep.from + c * delta;
      parts.forEach((run3, i) => {
        const current = snap(run3, emitPart(run3, x, frames2[i]));
        const reachPx = g.kind === "slide" ? k : reach[i] * k * Math.PI / 180;
        const m = compare(run3, previous[i], current, g.kind === "slide" ? delta : delta, reachPx);
        for (const key of Object.keys(worst)) worst[key] = Math.max(worst[key], m[key] ?? 0);
        const scale = delta / step;
        if (m.q > Math.ceil(scale) || m.birth > 2 * scale || m.dot > 0.0105 * scale || m.fade > Math.ceil(scale) / 32 + 5e-3 || m.merge > 0 || m.motion > 0) failures.push({ part: run3.name, group: g.name, at: x, m });
        measures.push({ run: run3, x: x - delta, dx: delta, value: m.birth + m.motion * 4 + (m.area ?? 0), motion: m.motion, birth: m.birth, valuesAt, reachPx });
        previous[i] = current;
      });
    }
  }
  measures.sort((a, b) => b.value - a.value);
  let halvingFails = 0;
  let halvingChecked = 0;
  const halving = (run3, at, x, dx) => {
    const emitAt = (value) => {
      const f = TURN.frame(run3);
      const cams = TURN.cams(scene, at(value));
      TURN.emit(run3, run3.group >= 0 ? cams[run3.group] : cams.world, f);
      return f;
    };
    const frames2 = Array.from({ length: 9 }, (_, j) => emitAt(x + dx * j / 8));
    const measure2 = (scale) => {
      const eighth = Math.max(...visibleChange(run3, frames2, scale));
      const quarter = Math.max(...visibleChange(run3, [0, 2, 4, 6, 8].map((j) => frames2[j]), scale));
      const half = Math.max(...visibleChange(run3, [frames2[0], frames2[4], frames2[8]], scale));
      const full = visibleChange(run3, [frames2[0], frames2[8]], scale)[0];
      return { full, half, quarter, eighth, fails: full >= 2 && half > 0.6 * full && quarter > 0.6 * half && eighth > 0.6 * quarter && eighth >= 2 };
    };
    const coarse = measure2(4);
    return coarse.fails ? measure2(16) : coarse;
  };
  const seen = /* @__PURE__ */ new Set();
  for (const entry of measures.slice(0, quick ? 40 : 400)) {
    if (!(entry.value > 1e-6)) break;
    const key = `${entry.run.index}|${entry.x.toFixed(4)}`;
    if (seen.has(key)) continue;
    seen.add(key);
    halvingChecked++;
    const g = groups[entry.run.group];
    const h = halving(entry.run, entry.valuesAt, entry.x, entry.dx);
    if (!h.fails) continue;
    halvingFails++;
    failures.push({ part: entry.run.name, group: g.name, at: entry.x, m: { halving: `${f2(h.full)} tone\xB7px\xB2 step stays ${f2(h.half)}, ${f2(h.quarter)} and ${f2(h.eighth)} at a half, a quarter and an eighth of the step` } });
  }
  const areaRoles = (run3) => run3.roles.map((role, r) => role.type === "face" || /^s[0-4]$/.test(role.name) || run3.kind === "tube" && role.name === "body" ? r : -1).filter((r) => r >= 0);
  const clipSteps = [];
  for (const family of families) {
    if (family.periodic) continue;
    const xs = samplesOf2(family, frameOf(family));
    say(`continuity ${family.name}: ${xs.length} frames over ${runs.length} parts`);
    const frames2 = runs.map((run3) => TURN.frame(run3));
    let previous = null;
    for (const x of xs) {
      const cams = TURN.cams(scene, family.at(x));
      const current = runs.map((run3, index) => {
        TURN.emit(run3, run3.group >= 0 ? cams[run3.group] : cams.world, frames2[index]);
        return areaRoles(run3).map((r) => areaOfPath(frames2[index].d[r]));
      });
      if (previous)
        runs.forEach((run3, index) => {
          let most = 0;
          let role = -1;
          current[index].forEach((v, k2) => {
            const d = Math.abs(v - previous[index][k2]);
            if (d > most) {
              most = d;
              role = k2;
            }
          });
          if (most >= 0.5) clipSteps.push({ family, run: run3, x: x - frameOf(family), dx: frameOf(family), role, value: most });
        });
      previous = current;
    }
  }
  clipSteps.sort((a, b) => b.value - a.value);
  let clipChecked = 0;
  for (const entry of clipSteps.slice(0, quick ? 60 : 400)) {
    clipChecked++;
    const h = halving(entry.run, entry.family.at, entry.x, entry.dx);
    if (!h.fails) continue;
    halvingFails++;
    failures.push({ part: entry.run.name, group: entry.family.name, at: entry.x, m: { halving: `${f2(h.full)} tone\xB7px\xB2 step stays ${f2(h.half)}, ${f2(h.quarter)} and ${f2(h.eighth)} at a half, a quarter and an eighth of the frame` } });
  }
  result.continuity = failures;
  result.stats.continuity = { worst, halvingChecked: halvingChecked + clipChecked, halvingFails, measures: measures.length + clipSteps.length };
}

// src/core/anatomy-adapter.ts
var add33 = (a, b) => [
  a[0] + b[0],
  a[1] + b[1],
  a[2] + b[2]
];
var zero = [0, 0, 0];
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
  const frames2 = [...scene.keyframes ?? []].sort(
    (a, b) => a.atSeconds - b.atSeconds
  );
  const values = Object.fromEntries(
    (scene.groups ?? []).map((g) => {
      const normalize = (v) => g.type === "free" ? free(v) : v;
      let before = {
        atSeconds: 0,
        value: normalize(g.type === "free" ? zero : 0)
      }, value = before.value;
      for (const f of frames2) {
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
    const nativeIds = new Set(frames2.flatMap((frame) => Object.keys(frame.values)));
    for (const id of nativeIds) {
      let before = { atSeconds: 0, value: 0 }, value = before.value;
      for (const frame of frames2) {
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
function resolveAnatomyParts(scene) {
  const resolved = /* @__PURE__ */ new Map(), parts = scene.parts ?? [], pending = new Map(parts.map((p) => [p.id, p]));
  const visit = (id, stack = /* @__PURE__ */ new Set()) => {
    if (resolved.has(id)) return resolved.get(id);
    const p = pending.get(id);
    if (!p || stack.has(id))
      throw new Error(`Invalid anatomy part hierarchy: ${id}`);
    stack.add(id);
    const parent = p.parentId ? visit(p.parentId, stack) : void 0;
    stack.delete(id);
    const out2 = {
      ...p,
      position: add33(parent?.position ?? zero, p.position ?? zero),
      groupId: p.groupId ?? parent?.groupId
    };
    resolved.set(id, out2);
    return out2;
  };
  return parts.map((p) => visit(p.id));
}
function compilePrimitiveAnatomy(scene, width, height) {
  const P = {
    scale: (scene.projection?.scale ?? 1) * Math.min(width, height) / 10,
    azimuth: scene.projection?.azimuth ?? 45,
    elevation: scene.projection?.elevation ?? 30,
    origin: scene.projection?.origin ?? [width / 2, height / 2]
  };
  const R = recorder(P), T = turning(P, { recorder: R });
  const layers = scene.layers?.length ? scene.layers : ["main"];
  layers.forEach((l) => T.layer(l));
  T.stack(layers);
  const pending = new Map((scene.groups ?? []).map((g) => [g.id, g]));
  const makeGroup = (id, seen = /* @__PURE__ */ new Set()) => {
    if (T.groups.some((g2) => g2.name === id)) return;
    const g = pending.get(id);
    if (!g || seen.has(id))
      throw new Error(`Invalid anatomy group hierarchy: ${id}`);
    seen.add(id);
    if (g.parentId) makeGroup(g.parentId, seen);
    const range = g.range ?? [0, 360];
    const config = g.type === "turn" ? { turn: { pivot: g.pivot ?? zero, range } } : g.type === "slide" ? {
      slide: {
        direction: g.direction ?? [1, 0, 0],
        travel: Math.max(Math.abs(range[0]), Math.abs(range[1]))
      }
    } : g.type === "hinge" ? {
      hinge: {
        point: g.pivot ?? zero,
        axis: g.axis ?? [1, 0, 0],
        range
      }
    } : { free: { origin: g.pivot ?? zero } };
    T.group(id, { ...config, parent: g.parentId });
    seen.delete(id);
  };
  pending.forEach((g) => makeGroup(g.id));
  const parts = resolveAnatomyParts(scene);
  const owners = /* @__PURE__ */ new Map();
  for (const part of parts) {
    if (part.kind === "label") continue;
    const at = part.position ?? zero, r = part.radius ?? 0.8, h = part.height ?? part.size?.[2] ?? 0.22, axis = part.axis ?? [0, 0, 1];
    const F = frameAlong(at, axis), options2 = {
      name: part.id,
      owner: part.id,
      group: part.groupId,
      layer: part.layer ?? layers[0],
      material: part.material,
      tone: part.tone,
      crease: part.crease,
      lit: part.lit,
      details: part.details,
      fixed: false
    };
    const first = T.parts.length;
    const prism2 = (polygon, name = part.id) => T.prism({ ...options2, name, F, polygon, s0: -h / 2, s1: h / 2 });
    if (part.kind === "fixed" || part.kind === "billboard") {
      const polygon = part.polygon ?? [
        [-1, -0.5],
        [1, -0.5],
        [1, 0.5],
        [-1, 0.5]
      ];
      const fixedShape = {
        kind: "prism",
        F,
        poly: polygon,
        s0: -h / 2,
        s1: h / 2,
        name: part.id
      };
      const fixed = T.fixed({
        ...options2,
        fixed: void 0,
        svg: part.svg ?? "",
        anchor: part.anchor ?? at,
        shapes: [fixedShape]
      });
      if (part.kind === "billboard" && part.plane)
        T.billboard({
          part: fixed,
          at: part.plane.origin,
          normal: part.plane.normal ?? [0, 0, 1],
          svg: part.plane.svg,
          fade: part.plane.fade
        });
    } else if (part.kind === "item") {
      T.item({ ...options2, cloud: (part.cloud ?? [[0, 0, 0]]).map((point) => add33(at, point)) });
    } else if (part.kind === "box" || part.kind === "plane") {
      const [x, y] = part.size ?? [2, 1, 0.25];
      prism2([
        [-x / 2, -y / 2],
        [x / 2, -y / 2],
        [x / 2, y / 2],
        [-x / 2, y / 2]
      ]);
    } else if (part.kind === "prism") prism2(part.polygon);
    else if (part.kind === "lathe")
      T.lathe({ ...options2, F, profile: part.profile });
    else if (part.kind === "sphere") T.ball({ ...options2, c: at, r });
    else if (part.kind === "round")
      T.round({
        ...options2,
        F,
        s0: -h / 2,
        s1: h / 2,
        r: [r, r],
        ends: ["flat", "flat"]
      });
    else if (part.kind === "gear" || part.kind === "ring") {
      const inner = part.innerRadius ?? (part.kind === "ring" ? r * 0.65 : 0), n = part.kind === "gear" ? Math.max(6, Math.round(part.teeth ?? 16)) : Math.max(12, Math.round(part.segments ?? 32));
      if (inner <= 0)
        T.round({
          ...options2,
          name: part.id + ".hub",
          F,
          s0: -h / 2,
          s1: h / 2,
          r: [r * 0.9, r * 0.9],
          ends: ["flat", "flat"]
        });
      const polar = (a, d) => [
        Math.cos(a) * d,
        Math.sin(a) * d
      ];
      for (let i = 0; i < n; i++) {
        const a = i / n * Math.PI * 2, b = (i + 1) / n * Math.PI * 2;
        if (inner > 0)
          prism2(
            [
              polar(a, inner),
              polar(a, r * 0.9),
              polar(b, r * 0.9),
              polar(b, inner)
            ],
            `${part.id}.rim-${i}`
          );
        if (part.kind === "gear")
          prism2(
            [
              polar(a + 0.12 * (b - a), r * 0.86),
              polar(a + 0.28 * (b - a), r * 1.07),
              polar(a + 0.72 * (b - a), r * 1.07),
              polar(a + 0.88 * (b - a), r * 0.86)
            ],
            `${part.id}.tooth-${i}`
          );
      }
    } else {
      let route = (part.points ?? [
        [0, 0, 0],
        [0, 0, 2]
      ]).map((p) => add33(at, p));
      if (part.kind === "spring") {
        const turns = part.turns ?? 5, n = Math.max(24, Math.round(turns * 24)), length = part.height ?? 2;
        route = Array.from(
          { length: n + 1 },
          (_, i) => add33(at, [
            F.u[0] * r * Math.cos(i / n * turns * Math.PI * 2) + F.v[0] * r * Math.sin(i / n * turns * Math.PI * 2) + F.a[0] * i / n * length,
            F.u[1] * r * Math.cos(i / n * turns * Math.PI * 2) + F.v[1] * r * Math.sin(i / n * turns * Math.PI * 2) + F.a[1] * i / n * length,
            F.u[2] * r * Math.cos(i / n * turns * Math.PI * 2) + F.v[2] * r * Math.sin(i / n * turns * Math.PI * 2) + F.a[2] * i / n * length
          ])
        );
      }
      if (part.route?.closed && route.length > 1) {
        const firstPoint = route[0], lastPoint = route.at(-1);
        if (firstPoint.some((value, index) => Math.abs(value - lastPoint[index]) > 1e-9)) route = [...route, firstPoint];
      }
      const thickness = part.strokeWidth ? part.strokeWidth / (P.scale * Math.sqrt(1.6) * 2) : part.kind === "tube" ? 0.09 : 0.035;
      const routeConfig = part.route;
      T.tube({
        ...options2,
        route,
        r: thickness,
        spacing: routeConfig?.spacing ?? Math.max(0.025, thickness * 2),
        chunk: routeConfig?.chunk ?? 2,
        turn: routeConfig?.turn ?? 45,
        free: routeConfig?.free ?? part.freeEnds ?? [true, true],
        limp: routeConfig?.limp ?? true,
        closed: routeConfig?.closed ?? false,
        gaps: routeConfig?.gaps ?? [],
        breaks: routeConfig?.breaks ?? [],
        caps: routeConfig?.caps ?? true,
        rims: routeConfig?.rims,
        bundle: routeConfig?.bundle,
        touch: routeConfig?.touch,
        hue: routeConfig?.hue,
        rings: routeConfig?.rings
      });
      if (part.kind === "arrow") {
        const end = route.at(-1), prev = route.at(-2), d = end.map((v, i) => v - prev[i]);
        T.round({
          ...options2,
          name: part.id + ".tip",
          F: frameAlong(end, d),
          s0: -thickness * 7,
          s1: 0,
          r: [thickness * 3, 0],
          ends: ["flat", "flat"]
        });
      }
    }
    const planePart = T.parts.slice(first)[0];
    if (part.plane && planePart) {
      if (part.plane.billboard)
        T.billboard({
          part: planePart,
          at: part.plane.origin,
          normal: part.plane.normal ?? [0, 0, 1],
          svg: part.plane.svg,
          fade: part.plane.fade
        });
      else
        T.plane({
          part: planePart,
          o: part.plane.origin,
          u: part.plane.u,
          v: part.plane.v,
          normal: part.plane.normal,
          svg: part.plane.svg,
          fade: part.plane.fade
        });
    }
    if (T.parts.length > 2048)
      throw new Error(
        "ANATOMY_COMPLEXITY_LIMIT: expanded geometry exceeds 2048 parts."
      );
    const made = [...T.parts.slice(first)], section = part.section ?? scene.section;
    for (const shape of made) {
      owners.set(shape, { partId: part.id, removed: false });
      if (!section || section.mode === "none") continue;
      const raw = section.plane ?? [1, 0, 0], norm = Math.hypot(...raw), n = raw.map((v) => v / norm), d = (section.offset ?? 0) / norm;
      const points = shape.shapes.flatMap((s) => sampleShape(s, 24));
      const sides = points.map(
        (p) => p.reduce((sum, v, i) => sum + v * n[i], -d)
      );
      if (sides.every((s) => s <= 1e-7)) continue;
      if (sides.every((s) => s >= -1e-7)) {
        owners.set(shape, { partId: part.id, removed: true });
        continue;
      }
      let halves;
      try {
        halves = T.split(shape, { n, d });
      } catch (error) {
        throw new Error(
          `ANATOMY_SECTION_UNSUPPORTED (${part.id}): ${String(error)}. Use a convex prism or an axis-aligned round section.`
        );
      }
      halves.forEach((half) => {
        const points2 = half.shapes.flatMap((s) => sampleShape(s, 24));
        const side = points2.reduce(
          (sum, p) => sum + p.reduce((s, v, i) => s + v * n[i], -d),
          0
        ) / points2.length;
        owners.set(half, { partId: part.id, removed: side > 0 });
      });
    }
  }
  if (T.parts.length > 2048)
    throw new Error(
      "ANATOMY_COMPLEXITY_LIMIT: expanded geometry exceeds 2048 parts. Reduce segments/teeth."
    );
  const built = T.build({
    strict: false,
    verify: true,
    fullClouds: scene.fullClouds ?? true,
    poses: [anatomyValues(scene, 0)]
  });
  const bindings = T.parts.map((p, index) => ({
    index,
    ...owners.get(p)
  }));
  let checks = {}, motion = {};
  if (scene.audit !== false) {
    const auditConfig = typeof scene.audit === "object" ? scene.audit : {};
    checks = audit(R, P, { ...auditConfig, apart: auditConfig.apart ?? false, frames: auditConfig.frames ?? [] });
    const times2 = [0, ...(scene.keyframes ?? []).map((k) => k.atSeconds)].sort(
      (a, b) => a - b
    );
    const poses = [
      .../* @__PURE__ */ new Set([
        ...times2,
        ...times2.slice(1).map((t, i) => (times2[i] + t) / 2)
      ])
    ].map((t) => anatomyValues(scene, t));
    const result = orbit(T, R, P, {
      poses,
      random: 0,
      quick: auditConfig.quick ?? true,
      depthAngles: 0,
      depthEvents: 0,
      routeStates: 0,
      only: ["order", "posed"]
    });
    motion = Object.fromEntries(
      Object.entries(result).filter(
        ([k, v]) => k !== "stats" && Array.isArray(v) && v.length
      )
    );
  }
  return {
    data: built.data,
    markup: layers.map((name) => built.layerSvg(name, { width, height })).join(""),
    css: ISO_CSS + "\n" + built.css,
    projection: P,
    bindings,
    parts,
    audits: { source: "anatomy audit + turn-audit", checks, motion }
  };
}

// src/core/anatomy.ts
var ANATOMY_SOURCE_COMMIT = "1482e8469b0a9e0d8cc18ea2740a01423d29ae80";
var ANATOMY_RUNTIME_VERSION = `0.6.0-anatomy-${ANATOMY_SOURCE_COMMIT.slice(0, 12)}`;
function spatialBackend(scene) {
  if (scene.backend === "anatomy") return "anatomy";
  if (scene.backend === "three") return "three";
  return scene.anatomy ? "anatomy" : "three";
}
function anatomyAudit(scene) {
  if (scene.figureId) return [{ code: "ANATOMY_AUTHORED_FIGURE", severity: "info", message: `\u4F7F\u7528\u9879\u76EE\u5185\u5B8C\u6574 authored figure: ${scene.figureId}\uFF1B\u51E0\u4F55\u5BA1\u8BA1\u7531\u4F5C\u8005\u6784\u5EFA\u6D41\u7A0B\u63D0\u4F9B\uFF0C\u8FD0\u884C\u65F6\u9A8C\u8BC1\u663E\u5F0F\u7ED8\u5236\u4E0E\u8D44\u6E90\u5B8C\u6574\u6027\u3002` }];
  if (scene.nativeExample) return [{ code: "ANATOMY_NATIVE_EXAMPLE", severity: "info", message: `\u4F7F\u7528 pinned upstream authored anatomy example: ${scene.nativeExample}\u3002` }];
  const parts = scene.parts ?? [];
  const ids = new Set(parts.map((part) => part.id));
  const groups = new Set((scene.groups ?? []).map((group2) => group2.id));
  const findings = [];
  for (const part of parts) {
    if (part.parentId && !ids.has(part.parentId)) findings.push({ code: "ANATOMY_PARENT_MISSING", severity: "error", message: `\u90E8\u4EF6 ${part.id} \u7684 parentId ${part.parentId} \u4E0D\u5B58\u5728\u3002`, partId: part.id });
    if (part.groupId && !groups.has(part.groupId)) findings.push({ code: "ANATOMY_GROUP_MISSING", severity: "error", message: `\u90E8\u4EF6 ${part.id} \u7684 groupId ${part.groupId} \u4E0D\u5B58\u5728\u3002`, partId: part.id });
    if (part.kind === "gear" && (part.teeth ?? 0) < 6) findings.push({ code: "ANATOMY_GEAR_TOO_FEW_TEETH", severity: "warning", message: `\u9F7F\u8F6E ${part.id} \u7684\u9F7F\u6570\u8FC7\u5C11\uFF0C\u7F29\u5C0F\u540E\u53EF\u80FD\u65E0\u6CD5\u8BFB\u51FA\u556E\u5408\u5173\u7CFB\u3002`, partId: part.id });
    if (["line", "tube", "arrow", "spring"].includes(part.kind) && (part.points?.length ?? 0) < 2) findings.push({ code: "ANATOMY_ROUTE_UNGROUNDED", severity: "warning", message: `\u8DEF\u5F84\u90E8\u4EF6 ${part.id} \u7F3A\u5C11\u4E24\u4E2A\u53EF\u89C2\u5BDF\u7AEF\u70B9\u3002`, partId: part.id });
  }
  const layerNames = new Set(scene.layers ?? []);
  for (const part of parts) if (part.layer && layerNames.size && !layerNames.has(part.layer)) findings.push({ code: "ANATOMY_LAYER_MISSING", severity: "error", message: `\u90E8\u4EF6 ${part.id} \u5F15\u7528\u4E86\u4E0D\u5B58\u5728\u7684\u56FE\u5C42 ${part.layer}\u3002`, partId: part.id });
  for (const group2 of scene.groups ?? []) {
    if (group2.parentId && !groups.has(group2.parentId)) findings.push({ code: "ANATOMY_GROUP_PARENT_MISSING", severity: "error", message: `\u52A8\u6001\u7EC4 ${group2.id} \u7684 parentId ${group2.parentId} \u4E0D\u5B58\u5728\u3002` });
    const seen = /* @__PURE__ */ new Set();
    let parent = group2.parentId;
    while (parent) {
      if (seen.has(parent)) {
        findings.push({ code: "ANATOMY_GROUP_CYCLE", severity: "error", message: `\u52A8\u6001\u7EC4 ${group2.id} \u7684\u7236\u7EA7\u5173\u7CFB\u5B58\u5728\u5FAA\u73AF\u3002` });
        break;
      }
      seen.add(parent);
      parent = scene.groups?.find((candidate) => candidate.id === parent)?.parentId;
    }
  }
  for (const annotation of scene.annotations ?? []) {
    const partId = Array.isArray(annotation.anchor) ? void 0 : annotation.anchor.partId;
    if (partId && !ids.has(partId)) findings.push({ code: "ANATOMY_ANNOTATION_PART_MISSING", severity: "error", message: `\u6807\u6CE8 ${annotation.id} \u5F15\u7528\u4E86\u4E0D\u5B58\u5728\u7684\u90E8\u4EF6 ${partId}\u3002`, partId });
  }
  if (scene.section && !scene.section.plane) findings.push({ code: "ANATOMY_SECTION_DEFAULT_PLANE", severity: "info", message: "anatomy \u5256\u9762\u672A\u6307\u5B9A\u5E73\u9762\uFF0C\u5C06\u4F7F\u7528 [1, 0, 0]\u3002" });
  if (scene.audit === false) findings.push({ code: "ANATOMY_AUDIT_DISABLED", severity: "warning", message: "\u8BE5\u573A\u666F\u5173\u95ED\u4E86 upstream geometry audit\uFF1B\u5B8C\u6574 anatomy \u573A\u666F\u5E94\u4FDD\u7559\u5BA1\u8BA1\u6216\u63D0\u4F9B\u660E\u786E\u8C41\u514D\u3002" });
  if (!scene.projection) findings.push({ code: "ANATOMY_PROJECTION_DEFAULTED", severity: "info", message: "\u672A\u6307\u5B9A anatomy \u6295\u5F71\uFF0C\u5C06\u4F7F\u7528 45\xB0 \u65B9\u4F4D\u89D2\u548C 30\xB0 \u4EF0\u89D2\u3002" });
  return findings;
}
function compileAnatomy(scene, width, height) {
  if (scene.figureId) throw new Error("ANATOMY_AUTHORED_COMPILE_PATH: authored figures execute their own explicit-time factory; do not convert them to primitive geometry.");
  return scene.nativeExample ? compileNativeAnatomy(scene, width, height) : compilePrimitiveAnatomy(scene, width, height);
}

// src/core/spatial3d.ts
var SPATIAL_RUNTIME_VERSION = "0.6.0-three-0.180.0";
function modelFormat(file) {
  const extension = path6.extname(file).toLowerCase();
  return extension === ".glb" || extension === ".gltf" ? extension.slice(1) : void 0;
}
function decodeGlbJson(buffer) {
  if (buffer.length < 20 || buffer.toString("ascii", 0, 4) !== "glTF")
    throw new Error("The GLB header is invalid.");
  const version = buffer.readUInt32LE(4);
  if (version !== 2) throw new Error(`Only glTF 2.x GLB files are supported (received ${version}).`);
  const length = buffer.readUInt32LE(8);
  if (length > buffer.length) throw new Error("The GLB declares a length larger than the file.");
  let offset = 12;
  while (offset + 8 <= Math.min(length, buffer.length)) {
    const chunkLength = buffer.readUInt32LE(offset);
    const chunkType = buffer.readUInt32LE(offset + 4);
    const chunk = buffer.subarray(offset + 8, offset + 8 + chunkLength);
    if (chunkType === 1313821514) return JSON.parse(chunk.toString("utf8").replace(/\u0000+$/g, ""));
    offset += 8 + chunkLength;
  }
  throw new Error("The GLB does not contain a JSON chunk.");
}
async function readGltfJson(file) {
  const format = modelFormat(file);
  if (format === "glb") return decodeGlbJson(await fs4.readFile(file));
  if (format !== "gltf") throw new Error(`Unsupported model format: ${path6.extname(file) || "unknown"}.`);
  const value = JSON.parse(await fs4.readFile(file, "utf8"));
  if (!value || value.asset?.version !== "2.0") throw new Error("Only glTF 2.0 JSON files are supported.");
  return value;
}
function uriDependency(uri) {
  if (typeof uri !== "string" || !uri || uri.startsWith("data:")) return void 0;
  if (/^(?:https?|file|javascript):/i.test(uri)) throw new Error(`Model dependency must be local or embedded: ${uri}`);
  const decoded = decodeURIComponent(uri);
  if (path6.isAbsolute(decoded) || decoded.split(/[\\/]/).includes("..")) throw new Error(`Model dependency escapes its model directory: ${uri}`);
  return decoded;
}
function accessorBounds(json2) {
  const mins = [];
  const maxs = [];
  for (const accessor of json2.accessors ?? []) {
    if (!Array.isArray(accessor.min) || !Array.isArray(accessor.max)) continue;
    if (!["VEC3", "VEC4"].includes(accessor.type)) continue;
    for (let index = 0; index < 3; index++) {
      if (Number.isFinite(accessor.min[index])) mins[index] = Math.min(mins[index] ?? Infinity, accessor.min[index]);
      if (Number.isFinite(accessor.max[index])) maxs[index] = Math.max(maxs[index] ?? -Infinity, accessor.max[index]);
    }
  }
  return mins.length === 3 && maxs.length === 3 ? { min: mins, max: maxs } : void 0;
}
async function probeSpatialModel(file) {
  const absolute = path6.resolve(file);
  const format = modelFormat(absolute);
  if (!format) throw new Error("Model probe requires a .glb or .gltf file.");
  const json2 = await readGltfJson(absolute);
  const dependencies = /* @__PURE__ */ new Set();
  for (const buffer of json2.buffers ?? []) {
    const dependency = uriDependency(buffer.uri);
    if (dependency) dependencies.add(dependency);
  }
  for (const image of json2.images ?? []) {
    const dependency = uriDependency(image.uri);
    if (dependency) dependencies.add(dependency);
  }
  const animations = (json2.animations ?? []).map((animation) => {
    let durationSeconds = 0;
    for (const sampler of animation.samplers ?? []) {
      const input = json2.accessors?.[sampler.input];
      const max2 = input?.max?.[0];
      if (Number.isFinite(max2)) durationSeconds = Math.max(durationSeconds, max2);
    }
    return { name: animation.name, channels: Array.isArray(animation.channels) ? animation.channels.length : 0, durationSeconds };
  });
  const result = {
    format,
    version: String(json2.asset?.version ?? "2.0"),
    generator: typeof json2.asset?.generator === "string" ? json2.asset.generator : void 0,
    scenes: Array.isArray(json2.scenes) ? json2.scenes.length : 0,
    nodes: (json2.nodes ?? []).map((node) => ({ name: node.name, mesh: node.mesh, children: Array.isArray(node.children) ? node.children : void 0 })),
    meshes: Array.isArray(json2.meshes) ? json2.meshes.length : 0,
    animations,
    materials: Array.isArray(json2.materials) ? json2.materials.length : 0,
    textures: Array.isArray(json2.textures) ? json2.textures.length : 0,
    images: Array.isArray(json2.images) ? json2.images.length : 0,
    buffers: Array.isArray(json2.buffers) ? json2.buffers.length : 0,
    externalDependencies: [...dependencies].sort(),
    bounds: accessorBounds(json2),
    hasDraco: Boolean(json2.extensionsUsed?.includes("KHR_draco_mesh_compression") || json2.extensionsRequired?.includes("KHR_draco_mesh_compression")),
    hasKtx2: Boolean(json2.extensionsUsed?.some((item) => item.includes("BASISU") || item.includes("KTX2"))),
    unitScale: Number.isFinite(json2.asset?.extras?.unitScale) ? Number(json2.asset.extras.unitScale) : 1,
    coordinateSystem: json2.asset?.extras?.coordinateSystem === "y-up-right-handed" ? "y-up-right-handed" : "unknown",
    supportsCompression: Boolean(json2.extensionsUsed?.some((item) => item.includes("DRACO") || item.includes("MESHOPT") || item.includes("BASISU") || item.includes("KTX2"))),
    supportsSkeletalAnimation: (json2.nodes ?? []).some((node) => Array.isArray(node.skin)),
    supportsNodeAnimation: animations.length > 0,
    sha256: createHash2("sha256").update(await fs4.readFile(absolute)).digest("hex")
  };
  return result;
}
function serializeSpatialRuntimeConfig(config) {
  return JSON.stringify(config).replace(/</g, "\\u003c");
}

// src/media.ts
async function probe(file) {
  const model = modelFormat(file);
  if (model) {
    const metadata = await probeSpatialModel(file);
    return { kind: "model3d", format: model, durationSeconds: 0, width: void 0, height: void 0, fps: 0, hasAudio: false, model: metadata };
  }
  const { stdout } = await run(getFfprobeBinaryPath(), ["-v", "error", "-show_entries", "format=duration,format_name:stream=codec_type,codec_name,width,height,avg_frame_rate,r_frame_rate,duration,pix_fmt,sample_rate", "-of", "json", path7.resolve(file)]);
  const value = JSON.parse(stdout), video = value.streams?.find((s) => s.codec_type === "video"), audio = value.streams?.find((s) => s.codec_type === "audio");
  const rate = String(video?.avg_frame_rate || video?.r_frame_rate || "0/1").split("/").map(Number);
  let durationSeconds = Number(value.format?.duration || video?.duration || audio?.duration || 0);
  if (!durationSeconds && !/image2|_pipe/.test(value.format?.format_name || "") && (video || audio)) {
    const packets = await run(getFfprobeBinaryPath(), ["-v", "error", "-select_streams", video ? "v:0" : "a:0", "-show_entries", "packet=pts_time,duration_time", "-of", "csv=p=0", path7.resolve(file)], { timeout: 10 * 6e4 });
    for (const line of packets.stdout.split("\n")) {
      const [pts, duration] = line.split(",").map(Number);
      if (Number.isFinite(pts)) durationSeconds = Math.max(durationSeconds, pts + (Number.isFinite(duration) ? duration : 0));
    }
  }
  return { durationSeconds, width: video?.width, height: video?.height, fps: rate[1] ? rate[0] / rate[1] : 0, hasAudio: !!audio, videoCodec: video?.codec_name, pixelFormat: video?.pix_fmt, audioCodec: audio?.codec_name, sampleRate: Number(audio?.sample_rate || 0) };
}
async function importMedia(root, file, provenance) {
  const isUrl = /^https:\/\//i.test(file);
  let localFile = file;
  let temporary;
  if (isUrl) {
    const parsed = new URL(file);
    const extension2 = path7.extname(parsed.pathname).toLowerCase();
    if (![".glb", ".gltf"].includes(extension2)) throw new Error("Public imports currently support GLB and GLTF model URLs only.");
    temporary = path7.join(os3.tmpdir(), `wandeo-model-${randomUUID4()}${extension2}`);
    await download(file, temporary, void 0, 512 * 1024 * 1024);
    localFile = temporary;
    provenance = { ...provenance ?? {}, url: file, downloadedAt: (/* @__PURE__ */ new Date()).toISOString() };
  }
  const extension = path7.extname(localFile).toLowerCase();
  if ([".srt", ".vtt"].includes(extension)) return registerAsset(root, file, "subtitle", void 0, provenance);
  if ([".glb", ".gltf"].includes(extension)) {
    try {
      const metadata2 = await probeSpatialModel(localFile);
      const asset = await registerSpatialAsset(root, localFile, metadata2, provenance, isUrl ? new URL(".", file).toString() : provenance?.url ? new URL(".", provenance.url).toString() : void 0);
      return asset;
    } finally {
      if (temporary) await fs5.rm(temporary, { force: true });
    }
  }
  const metadata = await probe(file);
  const kind = [".png", ".jpg", ".jpeg", ".webp", ".gif", ".avif", ".bmp"].includes(extension) && metadata.durationSeconds === 0 ? "image" : metadata.width ? "video" : metadata.hasAudio ? "audio" : "";
  if (!kind) throw new Error("The selected file has no supported image, video or audio stream.");
  return registerAsset(root, file, kind, metadata, provenance);
}
async function registerSpatialAsset(root, file, metadata, provenance, remoteOrigin) {
  const absolute = path7.resolve(file);
  const hash2 = await sha256(absolute);
  return updateProject(root, async (manifest) => {
    const existing = manifest.assets.find((asset2) => asset2.sha256 === hash2 && asset2.kind === "model3d");
    if (existing) return existing;
    const id = `asset-${hash2.slice(0, 20)}`;
    const extension = path7.extname(absolute).toLowerCase();
    const relativePath = `assets/${id}/model${extension}`;
    const destination = inside(root, relativePath);
    try {
      await fs5.mkdir(path7.dirname(destination), { recursive: true });
      await fs5.copyFile(absolute, destination);
      const dependencyRoot = path7.dirname(absolute);
      for (const dependency of metadata.externalDependencies) {
        const localDependency = path7.resolve(dependencyRoot, dependency);
        if (path7.relative(dependencyRoot, localDependency).startsWith(`..${path7.sep}`) || path7.isAbsolute(path7.relative(dependencyRoot, localDependency)))
          throw new Error(`Model dependency escapes its source directory: ${dependency}`);
        const target = inside(root, `assets/${id}/${dependency}`);
        await fs5.mkdir(path7.dirname(target), { recursive: true });
        if (await fs5.stat(localDependency).then((stat) => !stat.isFile(), () => true)) {
          if (!remoteOrigin) throw new Error(`Model dependency is missing: ${dependency}`);
          const remoteUrl = new URL(dependency.replaceAll("\\", "/"), remoteOrigin).toString();
          await download(remoteUrl, target, void 0, 512 * 1024 * 1024);
        } else await fs5.copyFile(localDependency, target);
      }
    } catch (error) {
      await fs5.rm(inside(root, `assets/${id}`), { recursive: true, force: true });
      throw error;
    }
    const asset = {
      id,
      relativePath,
      name: path7.basename(absolute),
      sha256: hash2,
      kind: "model3d",
      metadata: { ...metadata, sourceDirectory: metadata.externalDependencies.length ? "bundled-dependencies" : "single-file" },
      provenance: provenance ?? { type: "local-file", importedAt: (/* @__PURE__ */ new Date()).toISOString() }
    };
    manifest.assets.push(asset);
    return asset;
  });
}
async function frames(root, idOrFile, times2, prefix = "source") {
  const input = idOrFile.startsWith("asset-") ? (await assetById(root, idOrFile)).path : path7.resolve(idOrFile);
  const metadata = await probe(input);
  if (!metadata.width) throw new Error("Frames require visual media.");
  if (times2.length < 1 || times2.length > 24) throw new Error("Select 1\u201324 frame timestamps per request.");
  const outputs = [];
  await fs5.mkdir(path7.join(root, "evidence"), { recursive: true });
  for (const time of times2) {
    if (!Number.isFinite(time) || time < 0 || metadata.durationSeconds > 0 && time >= metadata.durationSeconds) throw new Error(`Frame ${time} is outside the media duration.`);
    const output = inside(root, `evidence/${prefix.replace(/[^a-z0-9_-]/gi, "_")}-${time.toFixed(3)}.jpg`);
    const frameStep = metadata.fps > 0 ? 1 / metadata.fps : 1 / 30;
    const candidates = [...new Set([
      time,
      time - frameStep,
      time - frameStep * 2,
      metadata.durationSeconds > 0 ? metadata.durationSeconds - frameStep * 2 : time
    ].map((value) => Math.max(0, Number(value.toFixed(6)))))];
    let extractedAt;
    let lastError;
    for (const candidate of candidates) {
      await fs5.rm(output, { force: true });
      try {
        await run(getFfmpegBinaryPath(), ["-hide_banner", "-loglevel", "error", "-y", "-ss", String(candidate), "-i", input, "-frames:v", "1", "-vf", "scale='min(1920,iw)':-2", "-q:v", "2", output]);
        const info = await fs5.stat(output);
        if (info.size > 0) {
          extractedAt = candidate;
          break;
        }
      } catch (error) {
        lastError = error;
      }
    }
    if (extractedAt === void 0) {
      await fs5.rm(output, { force: true });
      throw new Error(`Could not extract a frame near ${time}s${lastError instanceof Error ? `: ${lastError.message}` : "."}`);
    }
    outputs.push({ atSeconds: extractedAt, path: output });
  }
  await writeJson(path7.join(root, "evidence", `${prefix.replace(/[^a-z0-9_-]/gi, "_")}-frames.json`), { input, frames: outputs });
  return { input, frames: outputs, instruction: "Open and inspect these actual images with the host image tool; filenames are not visual evidence." };
}
function timestamp(seconds3, vtt) {
  const milliseconds = Math.round(seconds3 * 1e3), ms = milliseconds % 1e3;
  return `${Math.floor(milliseconds / 36e5).toString().padStart(2, "0")}:${Math.floor(milliseconds / 6e4) % 60}`.replace(/:(\d)$/, ":0$1") + `:${(Math.floor(milliseconds / 1e3) % 60).toString().padStart(2, "0")}${vtt ? "." : ","}${ms.toString().padStart(3, "0")}`;
}
function subtitles(cues, vtt = false) {
  return (vtt ? "WEBVTT\n\n" : "") + cues.map((cue, i) => `${vtt ? "" : `${i + 1}
`}${timestamp(cue.start, vtt)} --> ${timestamp(cue.end, vtt)}
${cue.text.replaceAll("-->", "\u2192")}
`).join("\n");
}
async function writeSubtitles(root, cues, basename, revision) {
  const results = [];
  for (const extension of ["srt", "vtt"]) {
    const output = inside(root, `outputs/${basename}.${extension}`);
    await fs5.writeFile(output, subtitles(cues, extension === "vtt"));
    await saveArtifact(root, extension, output, revision);
    results.push(output);
  }
  return results;
}

// src/render-evidence.ts
import { createHash as createHash3 } from "node:crypto";
var hash = (value) => createHash3("sha256").update(
  JSON.stringify(
    value,
    (_key, v) => v && typeof v === "object" && !Array.isArray(v) ? Object.fromEntries(
      Object.keys(v).filter((k) => k !== "assetPath").sort().map((k) => [k, v[k]])
    ) : v
  )
).digest("hex");
function sceneSourceUsage(project, assets) {
  const byId = new Map(assets.map((a) => [a.id, a]));
  return project.scenes.map((scene) => {
    const used = /* @__PURE__ */ new Set();
    const scan = (v) => {
      if (!v || typeof v !== "object") return;
      if (v.assetId) used.add(v.assetId);
      Object.entries(v).forEach(([key, child]) => {
        if (key !== "authoredFigure") Array.isArray(child) ? child.forEach(scan) : scan(child);
      });
    };
    scan(scene.visualLayers);
    scan(scene.motionLayers);
    scan(scene.spatial);
    const figureId = scene.spatial?.anatomy?.figureId;
    if (figureId && project.anatomyFigures?.[figureId]) used.add(project.anatomyFigures[figureId].assetId);
    const sources = [...used].sort().map((id) => ({
      assetId: id,
      sha256: byId.get(id)?.sha256,
      kind: byId.get(id)?.kind,
      provenance: byId.get(id)?.provenance
    }));
    return {
      sceneId: scene.id,
      backend: scene.spatial ? spatialBackend(scene.spatial) : "2d",
      backends: scene.spatial?.anatomy && scene.spatial.models.length ? ["anatomy", "three"] : [scene.spatial ? spatialBackend(scene.spatial) : "2d"],
      containsPrerenderedVideo: sources.some((s) => s.kind === "video"),
      ...figureId ? { authoredFigure: { figureId, assetId: project.anatomyFigures?.[figureId]?.assetId } } : {},
      sources,
      visualFingerprint: hash({
        // Use the bound visual timeline: generated captions and motion are already expanded.
        range: scene.range,
        layers: scene.visualLayers,
        motion: scene.motionLayers,
        spatial: scene.spatial,
        graphics: scene.graphics,
        captions: scene.captions,
        shotRole: scene.shotRole,
        idleMotion: scene.idleMotion,
        enterAnimation: scene.enterAnimation,
        exitAnimation: scene.exitAnimation,
        recipe: scene.recipe,
        transitionIn: scene.transitionIn,
        transitionOut: scene.transitionOut,
        brand: project.brand,
        presentation: project.presentation,
        stylesheet: project.stylesheet,
        durationSeconds: project.durationSeconds,
        width: project.width,
        height: project.height,
        sources: sources.map((s) => ({ assetId: s.assetId, sha256: s.sha256 }))
      })
    };
  });
}
function visualRevisionFindings(current, baseline, request) {
  const required = request?.kind === "visual-upgrade";
  const findings = [];
  const issue = (code, message, sceneId) => findings.push({
    code,
    message,
    sceneId,
    category: "semantic_alignment",
    severity: required ? "error" : "info"
  });
  if (required && (!baseline || !Array.isArray(request.sceneIds) || !request.sceneIds.length)) {
    issue(
      "VISUAL_REVISION_BASELINE_REQUIRED",
      "\u89C6\u89C9\u5347\u7EA7\u9700\u8981 baselineRenderContext \u548C\u975E\u7A7A sceneIds\uFF0C\u624D\u80FD\u6838\u5BF9\u54EA\u4E9B\u753B\u9762\u5E94\u53D1\u751F\u53D8\u5316\u3002"
    );
    return findings;
  }
  for (const id of required ? request.sceneIds : current.map((s) => s.sceneId)) {
    const now = current.find((s) => s.sceneId === id), prior = baseline?.find((s) => s.sceneId === id);
    if (!now) {
      issue(
        "VISUAL_REVISION_SCENE_MISSING",
        `\u6307\u5B9A\u5347\u7EA7\u7684\u573A\u666F ${id} \u4E0D\u5B58\u5728\u3002`,
        id
      );
      continue;
    }
    if (prior?.visualFingerprint === now.visualFingerprint)
      issue(
        "VISUAL_REVISION_UNCHANGED",
        `\u573A\u666F ${id} \u7684\u753B\u9762\u914D\u7F6E\u548C\u7D20\u6750\u54C8\u5E0C\u4E0E\u57FA\u7EBF\u5B8C\u5168\u76F8\u540C\uFF1B\u91CD\u65B0\u7F16\u7801\u4E0D\u4F1A\u63D0\u5347\u753B\u9762\u3002`,
        id
      );
    const expected = request?.expectedBackends?.[id];
    if (expected && !(now.backends ?? [now.backend]).includes(expected))
      issue(
        "VISUAL_REVISION_BACKEND_MISMATCH",
        `\u573A\u666F ${id} \u8981\u6C42 ${expected}\uFF0C\u5B9E\u9645\u7F16\u6392\u4E3A ${now.backend}\uFF1B\u65E7 MP4 \u4E0D\u7B97\u539F\u751F\u540E\u7AEF\u4F7F\u7528\u3002`,
        id
      );
  }
  return findings;
}

// src/edit.ts
import path12 from "node:path";
import { randomUUID as randomUUID6 } from "node:crypto";

// src/core/types.ts
var MOTION_NODE_TAGS = [
  "div",
  "span",
  "img",
  "svg",
  "g",
  "path",
  "rect",
  "circle",
  "ellipse",
  "line",
  "polyline",
  "polygon",
  "text"
];
function assertFiniteRange(range, label) {
  if (!Number.isFinite(range.start) || !Number.isFinite(range.end) || range.start < 0 || range.end <= range.start) {
    throw new Error(`${label} must have a finite start before end.`);
  }
}
var SOUND_EFFECT_SCENE_OVERHANG_SECONDS = 1.5;
function assertVideoProject(value) {
  if (!["1.0.0", "1.1.0"].includes(value.schemaVersion) || !value.projectId.trim()) {
    throw new Error("VideoProject identity is invalid.");
  }
  if (![value.width, value.height, value.fps, value.durationSeconds].every(
    (item) => Number.isFinite(item) && item > 0
  )) {
    throw new Error("VideoProject media settings are invalid.");
  }
  if (!Array.isArray(value.scenes) || value.scenes.length === 0) {
    throw new Error("VideoProject requires at least one scene.");
  }
  if (value.anatomyFigures !== void 0) {
    if (!value.anatomyFigures || typeof value.anatomyFigures !== "object" || Array.isArray(value.anatomyFigures)) throw new Error("VideoProject.anatomyFigures must be an object.");
    for (const [id, figure] of Object.entries(value.anatomyFigures)) {
      requireNonEmptyString(id, "VideoProject.anatomyFigures id");
      if (!figure || typeof figure !== "object") throw new Error(`VideoProject.anatomyFigures.${id} is invalid.`);
      requireNonEmptyString(figure.assetId, `VideoProject.anatomyFigures.${id}.assetId`);
    }
  }
  if (value.presentation !== void 0) {
    if (typeof value.presentation !== "object" || value.presentation === null)
      throw new Error("VideoProject.presentation is invalid.");
    for (const key of ["showTimelineProgress", "showChapterRail"]) {
      if (value.presentation[key] !== void 0 && typeof value.presentation[key] !== "boolean")
        throw new Error(`VideoProject.presentation.${key} must be boolean.`);
    }
  }
  for (const scene of value.scenes) {
    const figureId = scene.spatial?.anatomy?.figureId;
    if (figureId && !Object.prototype.hasOwnProperty.call(value.anatomyFigures ?? {}, figureId)) throw new Error(`Scene ${scene.id} references missing anatomy figure ${figureId}.`);
    assertFiniteRange(scene.range, `Scene ${scene.id}`);
    if (scene.shotRole !== void 0 && ![
      "hook",
      "problem",
      "promise",
      "feature",
      "evidence",
      "process",
      "result",
      "breather",
      "cta"
    ].includes(scene.shotRole))
      throw new Error(`Scene ${scene.id}.shotRole is invalid.`);
    if (scene.proofFlow) {
      requireNonEmptyString(scene.proofFlow.id, `Scene ${scene.id}.proofFlow.id`);
      if (!["context", "action", "processing", "result"].includes(scene.proofFlow.stage))
        throw new Error(`Scene ${scene.id}.proofFlow.stage is invalid.`);
      requireNonEmptyString(
        scene.proofFlow.continuityNote,
        `Scene ${scene.id}.proofFlow.continuityNote`
      );
    }
    if (scene.recipe) {
      requireNonEmptyString(scene.recipe.id, `Scene ${scene.id}.recipe.id`);
      if (scene.recipe.version !== void 0)
        requireNonEmptyString(scene.recipe.version, `Scene ${scene.id}.recipe.version`);
      if (scene.recipe.parameters !== void 0 && (!scene.recipe.parameters || typeof scene.recipe.parameters !== "object" || Array.isArray(scene.recipe.parameters) || Object.values(scene.recipe.parameters).some(
        (item) => typeof item !== "string" && typeof item !== "number" && typeof item !== "boolean"
      )))
        throw new Error(`Scene ${scene.id}.recipe.parameters is invalid.`);
    }
    if (scene.stage) assertSceneStage(scene.stage, `Scene ${scene.id}.stage`);
    if (scene.idleMotion !== void 0 && !["breathe", "none"].includes(scene.idleMotion))
      throw new Error(`Scene ${scene.id}.idleMotion is invalid.`);
    if (!scene.visualLayers.length && !(scene.motionLayers?.length ?? 0) && !scene.spatial)
      throw new Error(`Scene ${scene.id} has no visual layer or motion layer.`);
    for (const caption of scene.captions) {
      assertFiniteRange(caption.range, `Caption ${caption.id}`);
      if (caption.range.start < scene.range.start || caption.range.end > scene.range.end)
        throw new Error(`Caption ${caption.id} is outside its scene.`);
      requireNonEmptyString(caption.id, "Caption.id");
      requireNonEmptyString(caption.text, `Caption ${caption.id}.text`);
      assertNormalizedRect(caption.bbox, `Caption ${caption.id}.bbox`);
      if (!Number.isInteger(caption.maxCharsPerLine) || caption.maxCharsPerLine <= 0)
        throw new Error(`Caption ${caption.id}.maxCharsPerLine is invalid.`);
      if (caption.style) assertRenderStyle(caption.style, `Caption ${caption.id}.style`);
      if (caption.enterAnimation)
        assertRenderAnimation(
          caption.enterAnimation,
          `Caption ${caption.id}.enterAnimation`
        );
      if (caption.exitAnimation)
        assertRenderAnimation(caption.exitAnimation, `Caption ${caption.id}.exitAnimation`);
    }
    for (const graphic of scene.graphics ?? []) {
      requireNonEmptyString(graphic.id, "Graphic.id");
      requireNonEmptyString(graphic.text, `Graphic ${graphic.id}.text`);
      assertFiniteRange(graphic.range, `Graphic ${graphic.id}`);
      if (graphic.range.start < scene.range.start || graphic.range.end > scene.range.end)
        throw new Error(`Graphic ${graphic.id} is outside its scene.`);
      requireNonEmptyString(graphic.kind, `Graphic ${graphic.id}.kind`);
      requireNonEmptyString(graphic.position, `Graphic ${graphic.id}.position`);
      requireNonEmptyString(graphic.animation, `Graphic ${graphic.id}.animation`);
      if (graphic.style) assertRenderStyle(graphic.style, `Graphic ${graphic.id}.style`);
      if (graphic.enterAnimation)
        assertRenderAnimation(
          graphic.enterAnimation,
          `Graphic ${graphic.id}.enterAnimation`
        );
      if (graphic.exitAnimation)
        assertRenderAnimation(graphic.exitAnimation, `Graphic ${graphic.id}.exitAnimation`);
    }
    for (const layer of scene.visualLayers) {
      if (layer.crop) assertNormalizedRect(layer.crop, `Visual ${layer.id}.crop`);
      if (layer.sourceRange) assertFiniteRange(layer.sourceRange, `Visual ${layer.id}`);
      if (layer.sourcePlaybackRate !== void 0 && (!Number.isFinite(layer.sourcePlaybackRate) || layer.sourcePlaybackRate <= 0))
        throw new Error(`Visual ${layer.id}.sourcePlaybackRate is invalid.`);
      if (layer.audioGainDb !== void 0 && !Number.isFinite(layer.audioGainDb))
        throw new Error(`Visual ${layer.id}.audioGainDb is invalid.`);
      if (layer.cameraMotion)
        assertCameraMotion(
          layer.cameraMotion,
          scene.range.end - scene.range.start,
          `Visual ${layer.id}.cameraMotion`
        );
      if (layer.style) assertRenderStyle(layer.style, `Visual ${layer.id}.style`);
      if (layer.enterAnimation)
        assertRenderAnimation(layer.enterAnimation, `Visual ${layer.id}.enterAnimation`);
      if (layer.exitAnimation)
        assertRenderAnimation(layer.exitAnimation, `Visual ${layer.id}.exitAnimation`);
      if (layer.cursorOverlay)
        assertCursorOverlay(
          layer.cursorOverlay,
          scene.range,
          `Visual ${layer.id}.cursorOverlay`
        );
    }
    for (const layer of scene.motionLayers ?? [])
      assertMotionLayer(layer, scene.range, `Motion layer ${layer.id}`);
    if (scene.spatial) assertSpatialScene(scene.spatial, scene.range, `Scene ${scene.id}.spatial`);
    if (scene.enterAnimation)
      assertRenderAnimation(scene.enterAnimation, `Scene ${scene.id}.enterAnimation`);
    if (scene.exitAnimation)
      assertRenderAnimation(scene.exitAnimation, `Scene ${scene.id}.exitAnimation`);
    if (scene.transitionIn)
      assertSceneTransition(scene.transitionIn, `Scene ${scene.id}.transitionIn`);
    if (scene.transitionOut)
      assertSceneTransition(scene.transitionOut, `Scene ${scene.id}.transitionOut`);
    if (scene.voiceover)
      assertFiniteRange(scene.voiceover.range, `Voiceover ${scene.voiceover.id}`);
    if (scene.music) assertFiniteRange(scene.music.range, `Music ${scene.music.id}`);
    if (scene.voiceover?.sourceStartSeconds !== void 0 && (!Number.isFinite(scene.voiceover.sourceStartSeconds) || scene.voiceover.sourceStartSeconds < 0))
      throw new Error(`Voiceover ${scene.voiceover.id}.sourceStartSeconds is invalid.`);
    if (scene.music?.sourceStartSeconds !== void 0 && (!Number.isFinite(scene.music.sourceStartSeconds) || scene.music.sourceStartSeconds < 0))
      throw new Error(`Music ${scene.music.id}.sourceStartSeconds is invalid.`);
    for (const soundEffect of scene.soundEffects ?? []) {
      requireNonEmptyString(soundEffect.id, "SoundEffect.id");
      requireNonEmptyString(soundEffect.assetId, `SoundEffect ${soundEffect.id}.assetId`);
      assertFiniteRange(soundEffect.range, `SoundEffect ${soundEffect.id}`);
      if (soundEffect.range.start < scene.range.start - SOUND_EFFECT_SCENE_OVERHANG_SECONDS || soundEffect.range.end > scene.range.end + SOUND_EFFECT_SCENE_OVERHANG_SECONDS || soundEffect.range.start < 0 || soundEffect.range.end > value.durationSeconds + 1e-3)
        throw new Error(
          `SoundEffect ${soundEffect.id} is outside its scene (it may extend at most ${SOUND_EFFECT_SCENE_OVERHANG_SECONDS} s past either cut, inside the film).`
        );
      if (!Number.isFinite(soundEffect.gainDb))
        throw new Error(`SoundEffect ${soundEffect.id}.gainDb is invalid.`);
      if (![
        "ui-tick",
        "whoosh",
        "impact",
        "reveal",
        "transition",
        "brand-sting",
        "riser",
        "sparkle"
      ].includes(soundEffect.purpose))
        throw new Error(`SoundEffect ${soundEffect.id}.purpose is invalid.`);
      if (![
        "scene-enter",
        "scene-exit",
        "recipe-event",
        "transition-boundary",
        "custom"
      ].includes(soundEffect.syncPoint))
        throw new Error(`SoundEffect ${soundEffect.id}.syncPoint is invalid.`);
    }
  }
  if (value.brand)
    for (const [name, item] of Object.entries(value.brand))
      requireNonEmptyString(item, `VideoProject.brand.${name}`);
  if (value.stylesheet !== void 0 && typeof value.stylesheet !== "string")
    throw new Error("VideoProject.stylesheet must be a string.");
  if (value.finalAudioFilter !== void 0 && typeof value.finalAudioFilter !== "string")
    throw new Error("VideoProject.finalAudioFilter must be a string.");
  return value;
}
function assertVec3(value, label) {
  if (!Array.isArray(value) || value.length !== 3 || !value.every((item) => typeof item === "number" && Number.isFinite(item)))
    throw new Error(`${label} must be a finite [x,y,z] tuple.`);
}
function assertSpatialColor(value, label) {
  if (typeof value !== "string" || !/^#[0-9a-f]{6}$/i.test(value))
    throw new Error(`${label} must be a #rrggbb color.`);
}
function assertAnatomySection(value, label) {
  if (value === void 0) return;
  if (!value || typeof value !== "object" || !["none", "clip", "slice"].includes(value.mode))
    throw new Error(`${label}.mode is invalid.`);
  if (value.plane) {
    assertVec3(value.plane, `${label}.plane`);
    if (!Math.hypot(...value.plane)) throw new Error(`${label}.plane must be nonzero.`);
  }
  if (value.offset !== void 0 && !Number.isFinite(value.offset))
    throw new Error(`${label}.offset is invalid.`);
  if (value.opacity !== void 0 && (!Number.isFinite(value.opacity) || value.opacity < 0 || value.opacity > 1))
    throw new Error(`${label}.opacity is invalid.`);
}
function assertSpatialScene(value, sceneRange, label = "spatial") {
  if (!value || typeof value !== "object") throw new Error(`${label} is invalid.`);
  const camera = value.camera;
  if (!camera || !["perspective", "orthographic"].includes(camera.projection)) throw new Error(`${label}.camera.projection is invalid.`);
  assertVec3(camera.position, `${label}.camera.position`);
  assertVec3(camera.target, `${label}.camera.target`);
  if (camera.fov !== void 0 && (!Number.isFinite(camera.fov) || camera.fov <= 1 || camera.fov >= 179)) throw new Error(`${label}.camera.fov is invalid.`);
  if (camera.near !== void 0 && (!Number.isFinite(camera.near) || camera.near <= 0)) throw new Error(`${label}.camera.near is invalid.`);
  if (camera.far !== void 0 && (!Number.isFinite(camera.far) || camera.far <= (camera.near ?? 0))) throw new Error(`${label}.camera.far is invalid.`);
  for (const keyframe of camera.keyframes ?? []) {
    if (!Number.isFinite(keyframe.atSeconds) || keyframe.atSeconds < 0 || keyframe.atSeconds > sceneRange.end - sceneRange.start + 1e-3) throw new Error(`${label}.camera.keyframes has an out-of-range time.`);
    assertVec3(keyframe.position, `${label}.camera.keyframes.position`);
    assertVec3(keyframe.target, `${label}.camera.keyframes.target`);
  }
  const backend = value.backend ?? "auto";
  if (!["auto", "three", "anatomy"].includes(backend))
    throw new Error(`${label}.backend is invalid.`);
  if (!Array.isArray(value.models)) throw new Error(`${label}.models must be an array.`);
  if (value.models.length === 0 && !value.anatomy)
    throw new Error(`${label} needs models or an anatomy scene.`);
  if (value.models.length > 128) throw new Error(`${label}.models cannot contain more than 128 models.`);
  const ids = /* @__PURE__ */ new Set();
  for (const model of value.models) {
    requireNonEmptyString(model.id, `${label}.models.id`);
    if (ids.has(model.id)) throw new Error(`${label}.models contains duplicate id ${model.id}.`);
    ids.add(model.id);
    const modelRange = model.range ?? sceneRange;
    assertFiniteRange(modelRange, `${label}.models.${model.id}.range`);
    if (modelRange.start < sceneRange.start || modelRange.end > sceneRange.end) throw new Error(`${label}.models.${model.id}.range is outside the scene.`);
    const sources = [model.assetId, model.procedural, model.instanceOf].filter(Boolean);
    if (sources.length !== 1) throw new Error(`${label}.models.${model.id} needs exactly one of assetId, procedural or instanceOf.`);
    if (model.instanceOf && model.instanceOf === model.id) throw new Error(`${label}.models.${model.id} cannot instance itself.`);
    if (model.position) assertVec3(model.position, `${label}.models.${model.id}.position`);
    if (model.rotation) assertVec3(model.rotation, `${label}.models.${model.id}.rotation`);
    if (model.scale) assertVec3(model.scale, `${label}.models.${model.id}.scale`);
    if (model.scale && model.scale.some((item) => item === 0)) throw new Error(`${label}.models.${model.id}.scale cannot contain zero.`);
    if (model.section) {
      if (!["none", "clip", "slice"].includes(model.section.mode)) throw new Error(`${label}.models.${model.id}.section.mode is invalid.`);
      if (model.section.plane) assertVec3(model.section.plane, `${label}.models.${model.id}.section.plane`);
      if (model.section.offset !== void 0 && !Number.isFinite(model.section.offset)) throw new Error(`${label}.models.${model.id}.section.offset is invalid.`);
      if (model.section.opacity !== void 0 && (!Number.isFinite(model.section.opacity) || model.section.opacity < 0 || model.section.opacity > 1)) throw new Error(`${label}.models.${model.id}.section.opacity is invalid.`);
    }
    if (model.material?.color) assertSpatialColor(model.material.color, `${label}.models.${model.id}.material.color`);
    if (model.material?.metalness !== void 0 && (!Number.isFinite(model.material.metalness) || model.material.metalness < 0 || model.material.metalness > 1)) throw new Error(`${label}.models.${model.id}.material.metalness is invalid.`);
    if (model.material?.roughness !== void 0 && (!Number.isFinite(model.material.roughness) || model.material.roughness < 0 || model.material.roughness > 1)) throw new Error(`${label}.models.${model.id}.material.roughness is invalid.`);
    for (const animation of model.animations ?? []) {
      requireNonEmptyString(animation.id, `${label}.models.${model.id}.animations.id`);
      assertFiniteRange(animation.range, `${label}.models.${model.id}.animations.${animation.id}`);
      if (animation.range.start < sceneRange.start || animation.range.end > sceneRange.end) throw new Error(`${label}.models.${model.id}.animations.${animation.id} is outside the scene.`);
      if (!["transform", "camera", "visibility", "material", "light", "path", "instance"].includes(animation.track)) throw new Error(`${label}.models.${model.id}.animations.${animation.id}.track is invalid.`);
    }
  }
  for (const model of value.models) if (model.instanceOf && !ids.has(model.instanceOf)) throw new Error(`${label}.models.${model.id}.instanceOf references missing model ${model.instanceOf}.`);
  for (const model of value.models) for (const link of ["parentId", "instanceOf"]) {
    const seen = /* @__PURE__ */ new Set([model.id]);
    let next = model[link];
    while (next) {
      if (!ids.has(next)) throw new Error(`${label}.models.${model.id}.${link} references missing model ${next}.`);
      if (seen.has(next)) throw new Error(`${label}.models contains a ${link} cycle.`);
      seen.add(next);
      next = value.models.find((m) => m.id === next)?.[link];
    }
  }
  const lightIds = /* @__PURE__ */ new Set();
  const assertSpatialAnimations = (animations, owner) => {
    for (const animation of animations ?? []) {
      requireNonEmptyString(animation.id, `${owner}.animations.id`);
      assertFiniteRange(animation.range, `${owner}.animations.${animation.id}`);
      if (animation.range.start < sceneRange.start || animation.range.end > sceneRange.end) throw new Error(`${owner}.animations.${animation.id} is outside the scene.`);
      if (!["transform", "camera", "visibility", "material", "light", "path", "instance"].includes(animation.track)) throw new Error(`${owner}.animations.${animation.id}.track is invalid.`);
    }
  };
  assertSpatialAnimations(value.animations, label);
  for (const light of value.lights ?? []) {
    requireNonEmptyString(light.id, `${label}.lights.id`);
    if (lightIds.has(light.id)) throw new Error(`${label}.lights contains duplicate id ${light.id}.`);
    lightIds.add(light.id);
    if (!["ambient", "directional", "point", "hemisphere"].includes(light.type)) throw new Error(`${label}.lights.${light.id}.type is invalid.`);
    assertSpatialColor(light.color, `${label}.lights.${light.id}.color`);
    if (!Number.isFinite(light.intensity) || light.intensity < 0) throw new Error(`${label}.lights.${light.id}.intensity is invalid.`);
    if (light.position) assertVec3(light.position, `${label}.lights.${light.id}.position`);
    if (light.distance !== void 0 && (!Number.isFinite(light.distance) || light.distance < 0)) throw new Error(`${label}.lights.${light.id}.distance is invalid.`);
    assertSpatialAnimations(light.animations, `${label}.lights.${light.id}`);
  }
  const annotationIds = /* @__PURE__ */ new Set();
  for (const annotation of value.annotations ?? []) {
    requireNonEmptyString(annotation.id, `${label}.annotations.id`);
    if (annotationIds.has(annotation.id)) throw new Error(`${label}.annotations contains duplicate id ${annotation.id}.`);
    annotationIds.add(annotation.id);
    requireNonEmptyString(annotation.text, `${label}.annotations.${annotation.id}.text`);
    assertFiniteRange(annotation.range, `${label}.annotations.${annotation.id}`);
    if (annotation.range.start < sceneRange.start || annotation.range.end > sceneRange.end) throw new Error(`${label}.annotations.${annotation.id} is outside the scene.`);
    if (Array.isArray(annotation.anchor)) assertVec3(annotation.anchor, `${label}.annotations.${annotation.id}.anchor`);
    else {
      requireNonEmptyString(annotation.anchor.modelId, `${label}.annotations.${annotation.id}.anchor.modelId`);
      if (!ids.has(annotation.anchor.modelId)) throw new Error(`${label}.annotations.${annotation.id} references missing model ${annotation.anchor.modelId}.`);
      if (annotation.anchor.offset) assertVec3(annotation.anchor.offset, `${label}.annotations.${annotation.id}.anchor.offset`);
    }
  }
  if (value.background) assertSpatialColor(value.background, `${label}.background`);
  if (value.anatomy) assertAnatomyScene(value.anatomy, sceneRange, `${label}.anatomy`);
  if (backend === "anatomy" && !value.anatomy) throw new Error(`${label}.backend anatomy requires an anatomy scene.`);
  if (value.modelViewport) assertNormalizedRect(value.modelViewport, `${label}.modelViewport`);
  if (backend === "three" && value.anatomy) throw new Error(`${label}.backend three cannot include an anatomy scene.`);
}
function assertAuthoredAnatomyFigure(value, label = "anatomy figure") {
  if (!value || typeof value !== "object" || Array.isArray(value)) throw new Error(`${label} must be an object.`);
  const figure = value;
  if (figure.schemaVersion !== "1.0") throw new Error(`${label}.schemaVersion must be 1.0.`);
  for (const dimension2 of ["width", "height"]) if (!Number.isInteger(figure[dimension2]) || figure[dimension2] < 1 || figure[dimension2] > 16384) throw new Error(`${label}.${dimension2} must be an integer in [1,16384].`);
  for (const field of ["markup", "css", "script"]) {
    if (typeof figure[field] !== "string" || figure[field].length > 16 * 1024 * 1024) throw new Error(`${label}.${field} must be a string of at most 16 MiB.`);
    if (field !== "css" && !figure[field].trim()) throw new Error(`${label}.${field} cannot be empty.`);
  }
  if (!Array.isArray(figure.parts) || !figure.parts.length || figure.parts.length > 4096) throw new Error(`${label}.parts must contain 1..4096 named parts.`);
  const ids = /* @__PURE__ */ new Set();
  for (const part of figure.parts) {
    if (!part || typeof part !== "object") throw new Error(`${label}.parts contains an invalid part.`);
    requireNonEmptyString(part.id, `${label}.parts.id`);
    if (ids.has(part.id)) throw new Error(`${label}.parts contains duplicate id ${part.id}.`);
    ids.add(part.id);
  }
  if (figure.provenance !== void 0 && (!figure.provenance || typeof figure.provenance !== "object" || Array.isArray(figure.provenance))) throw new Error(`${label}.provenance must be an object.`);
}
function assertAnatomyView(value, duration, partIds, label) {
  if (value === void 0) return;
  if (!value || typeof value !== "object" || Array.isArray(value)) throw new Error(`${label} is invalid.`);
  if (value.timeOffsetSeconds !== void 0 && (!Number.isFinite(value.timeOffsetSeconds) || value.timeOffsetSeconds < 0)) throw new Error(`${label}.timeOffsetSeconds must be finite and nonnegative.`);
  if (value.timeScale !== void 0 && (!Number.isFinite(value.timeScale) || value.timeScale < 0 || value.timeScale > 1e4)) throw new Error(`${label}.timeScale must be in [0,10000].`);
  if (value.keyframes !== void 0 && !Array.isArray(value.keyframes)) throw new Error(`${label}.keyframes must be an array.`);
  const times2 = /* @__PURE__ */ new Set();
  for (const frame of value.keyframes ?? []) {
    if (!frame || !Number.isFinite(frame.atSeconds) || frame.atSeconds < 0 || frame.atSeconds > duration + 1e-3) throw new Error(`${label}.keyframes has an out-of-range time.`);
    if (times2.has(frame.atSeconds)) throw new Error(`${label}.keyframes contains duplicate time ${frame.atSeconds}.`);
    times2.add(frame.atSeconds);
    if (frame.frame) assertNormalizedRect(frame.frame, `${label}.keyframes.frame`);
    if (frame.dimOpacity !== void 0 && (!Number.isFinite(frame.dimOpacity) || frame.dimOpacity < 0 || frame.dimOpacity > 1)) throw new Error(`${label}.keyframes.dimOpacity must be in [0,1].`);
    if (frame.focusPartIds !== void 0) {
      if (!Array.isArray(frame.focusPartIds) || new Set(frame.focusPartIds).size !== frame.focusPartIds.length) throw new Error(`${label}.keyframes.focusPartIds must contain unique IDs.`);
      for (const id of frame.focusPartIds) {
        requireNonEmptyString(id, `${label}.keyframes.focusPartIds`);
        if (partIds && !partIds.has(id)) throw new Error(`${label}.keyframes references missing focus part ${id}.`);
      }
    }
  }
}
function assertAnatomyScene(value, sceneRange, label) {
  if (value.figureId !== void 0 || value.authoredFigure !== void 0) {
    requireNonEmptyString(value.figureId, `${label}.figureId`);
    for (const field of ["nativeExample", "projection", "section", "effect", "effects", "readouts", "controls", "annotations", "presentation"]) if (value[field] !== void 0) throw new Error(`${label}.${field} is not supported with figureId; author it in the figure script or use video 2D overlays.`);
    for (const field of ["parts", "groups", "layers", "keyframes"]) if (value[field]?.length) throw new Error(`${label}.${field} cannot override an authored figure; use view or the figure source.`);
    if (value.authoredFigure) assertAuthoredAnatomyFigure(value.authoredFigure, `${label}.authoredFigure`);
    assertAnatomyView(value.view, sceneRange.end - sceneRange.start, value.authoredFigure ? new Set(value.authoredFigure.parts.map((part) => part.id)) : void 0, `${label}.view`);
    return;
  }
  if (value.view !== void 0) throw new Error(`${label}.view requires figureId.`);
  if (value.nativeExample !== void 0 && value.nativeExample !== "turning-dial") throw new Error(`${label}.nativeExample is unsupported.`);
  const authoredParts = value.parts ?? [];
  const nativeGroupIds = /* @__PURE__ */ new Set(["dial", "wheel", "pawl", "f2.mcp", "f2.pip", "f2.dip", "pod"]);
  if (!value.nativeExample && authoredParts.length === 0) throw new Error(`${label}.parts must contain at least one part.`);
  if (authoredParts.length > 512) throw new Error(`${label}.parts cannot contain more than 512 parts.`);
  const kinds = /* @__PURE__ */ new Set(["box", "round", "ring", "gear", "tube", "line", "arrow", "spring", "plane", "label", "sphere", "lathe", "prism", "fixed", "item", "billboard"]);
  const ids = /* @__PURE__ */ new Set();
  for (const part of authoredParts) {
    requireNonEmptyString(part.id, `${label}.parts.id`);
    if (ids.has(part.id)) throw new Error(`${label}.parts contains duplicate id ${part.id}.`);
    ids.add(part.id);
    if (!kinds.has(part.kind)) throw new Error(`${label}.parts.${part.id}.kind is invalid.`);
    if (part.position) assertVec3(part.position, `${label}.parts.${part.id}.position`);
    if (part.size) assertVec3(part.size, `${label}.parts.${part.id}.size`);
    if (part.points) {
      if (part.points.length < 2) throw new Error(`${label}.parts.${part.id}.points needs at least two points.`);
      part.points.forEach((point, index) => assertVec3(point, `${label}.parts.${part.id}.points[${index}]`));
    }
    for (const [name, number2] of [["radius", part.radius], ["innerRadius", part.innerRadius], ["height", part.height], ["opacity", part.opacity], ["strokeWidth", part.strokeWidth], ["teeth", part.teeth], ["turns", part.turns], ["segments", part.segments], ["fontSize", part.fontSize]]) {
      if (number2 !== void 0 && (!Number.isFinite(number2) || name !== "opacity" && number2 < 0)) throw new Error(`${label}.parts.${part.id}.${name} is invalid.`);
    }
    if (part.radius !== void 0 && part.radius <= 0 || part.height !== void 0 && part.height <= 0) throw new Error(`${label}.parts.${part.id} radius/height must be positive.`);
    if (part.innerRadius !== void 0 && part.innerRadius >= (part.radius ?? 0.8)) throw new Error(`${label}.parts.${part.id}.innerRadius must be smaller than radius.`);
    if (part.teeth !== void 0 && (!Number.isInteger(part.teeth) || part.teeth < 6 || part.teeth > 256)) throw new Error(`${label}.parts.${part.id}.teeth must be an integer in [6,256].`);
    if (part.segments !== void 0 && (!Number.isInteger(part.segments) || part.segments < 6 || part.segments > 256)) throw new Error(`${label}.parts.${part.id}.segments must be an integer in [6,256].`);
    if (part.turns !== void 0 && (part.turns <= 0 || part.turns > 64)) throw new Error(`${label}.parts.${part.id}.turns must be in (0,64].`);
    if (part.opacity !== void 0 && (part.opacity < 0 || part.opacity > 1)) throw new Error(`${label}.parts.${part.id}.opacity is invalid.`);
    if (part.color) assertSpatialColor(part.color, `${label}.parts.${part.id}.color`);
    if (part.secondaryColor) assertSpatialColor(part.secondaryColor, `${label}.parts.${part.id}.secondaryColor`);
    if (part.text !== void 0 && typeof part.text !== "string") throw new Error(`${label}.parts.${part.id}.text is invalid.`);
    if (part.size?.some((v) => v <= 0)) throw new Error(`${label}.parts.${part.id}.size must be positive.`);
    if (part.axis) {
      assertVec3(part.axis, `${label}.parts.${part.id}.axis`);
      if (!Math.hypot(...part.axis)) throw new Error(`${label}.parts.${part.id}.axis must be nonzero.`);
    }
    if (part.material && !["gold", "chrome", "steel", "gunmetal", "rubber", "brass", "copper"].includes(part.material)) throw new Error(`${label}.parts.${part.id}.material is invalid.`);
    for (const points of [part.profile, part.polygon]) if (points && (!Array.isArray(points) || points.some((p) => !Array.isArray(p) || p.length !== 2 || !p.every(Number.isFinite)))) throw new Error(`${label}.parts.${part.id} has invalid profile/polygon.`);
    if (part.kind === "lathe" && (!part.profile || part.profile.length < 2)) throw new Error(`${label}.parts.${part.id}.profile is required.`);
    if (part.kind === "prism" && (!part.polygon || part.polygon.length < 3)) throw new Error(`${label}.parts.${part.id}.polygon is required.`);
    if ((part.kind === "fixed" || part.kind === "billboard") && (!part.svg || !part.svg.trim())) throw new Error(`${label}.parts.${part.id}.svg is required.`);
    if (part.kind === "item" && (!part.cloud || part.cloud.length === 0)) throw new Error(`${label}.parts.${part.id}.cloud is required.`);
    if (part.cloud && part.cloud.length > 65536) throw new Error(`${label}.parts.${part.id}.cloud cannot contain more than 65536 points.`);
    if (part.cloud) part.cloud.forEach((point, index) => assertVec3(point, `${label}.parts.${part.id}.cloud[${index}]`));
    if (part.anchor) assertVec3(part.anchor, `${label}.parts.${part.id}.anchor`);
    if (part.details) {
      if (part.details.bevel !== void 0 && (!Number.isFinite(part.details.bevel) || part.details.bevel < 0)) throw new Error(`${label}.parts.${part.id}.details.bevel is invalid.`);
      for (const value2 of part.details.seams ?? []) if (!Number.isFinite(value2)) throw new Error(`${label}.parts.${part.id}.details.seams is invalid.`);
      if (part.details.ribs) {
        for (const value2 of [part.details.ribs.s0, part.details.ribs.s1, part.details.ribs.r0, part.details.ribs.r1, part.details.ribs.fade?.[0], part.details.ribs.fade?.[1]]) if (value2 !== void 0 && !Number.isFinite(value2)) throw new Error(`${label}.parts.${part.id}.details.ribs contains a non-finite value.`);
        if (part.details.ribs.count !== void 0 && (!Number.isInteger(part.details.ribs.count) || part.details.ribs.count < 1 || part.details.ribs.count > 4096)) throw new Error(`${label}.parts.${part.id}.details.ribs.count is invalid.`);
      }
      for (const dot of part.details.dots ?? []) {
        assertVec3(dot.at, `${label}.parts.${part.id}.details.dots.at`);
        if (dot.normal) assertVec3(dot.normal, `${label}.parts.${part.id}.details.dots.normal`);
        if (dot.size !== void 0 && (!Number.isFinite(dot.size) || dot.size <= 0)) throw new Error(`${label}.parts.${part.id}.details.dots.size is invalid.`);
      }
      for (const bolt of part.details.bolts ?? []) {
        for (const [name, number2] of [["s", bolt.s], ["r", bolt.r], ["phase", bolt.phase], ["size", bolt.size], ["fadeStart", bolt.fade?.[0]], ["fadeEnd", bolt.fade?.[1]]]) if (number2 !== void 0 && !Number.isFinite(number2)) throw new Error(`${label}.parts.${part.id}.details.bolts.${name} is invalid.`);
        if (!Number.isFinite(bolt.s) || !Number.isFinite(bolt.r) || bolt.r < 0 || !Number.isInteger(bolt.count) || bolt.count < 1 || bolt.count > 512) throw new Error(`${label}.parts.${part.id}.details.bolts requires finite s/r and an integer count in [1,512].`);
        if (bolt.size !== void 0 && bolt.size <= 0) throw new Error(`${label}.parts.${part.id}.details.bolts.size is invalid.`);
      }
      for (const ring of part.details.rings ?? []) {
        assertVec3(ring.at, `${label}.parts.${part.id}.details.rings.at`);
        if (!Number.isFinite(ring.r) || ring.r <= 0) throw new Error(`${label}.parts.${part.id}.details.rings.r is invalid.`);
        if (ring.normal) assertVec3(ring.normal, `${label}.parts.${part.id}.details.rings.normal`);
      }
      for (const rule of part.details.rules ?? []) {
        if (!Array.isArray(rule.points) || rule.points.length < 2) throw new Error(`${label}.parts.${part.id}.details.rules.points is invalid.`);
        rule.points.forEach((point, index) => assertVec3(point, `${label}.parts.${part.id}.details.rules.points[${index}]`));
        if (rule.normal) assertVec3(rule.normal, `${label}.parts.${part.id}.details.rules.normal`);
      }
    }
    if (part.plane) {
      assertVec3(part.plane.origin, `${label}.parts.${part.id}.plane.origin`);
      assertVec3(part.plane.u, `${label}.parts.${part.id}.plane.u`);
      assertVec3(part.plane.v, `${label}.parts.${part.id}.plane.v`);
      if (!Math.hypot(...part.plane.u) || !Math.hypot(...part.plane.v)) throw new Error(`${label}.parts.${part.id}.plane axes must be nonzero.`);
      if (part.plane.normal) assertVec3(part.plane.normal, `${label}.parts.${part.id}.plane.normal`);
      if (!part.plane.svg.trim()) throw new Error(`${label}.parts.${part.id}.plane.svg is required.`);
    }
    if (part.route) {
      for (const gap of part.route.gaps ?? []) if (!Array.isArray(gap) || gap.length !== 2 || !gap.every(Number.isFinite) || gap[1] < gap[0]) throw new Error(`${label}.parts.${part.id}.route.gaps is invalid.`);
      for (const value2 of part.route.breaks ?? []) if (!Number.isFinite(value2) || value2 < 0) throw new Error(`${label}.parts.${part.id}.route.breaks is invalid.`);
      for (const value2 of part.route.rims ?? []) if (!Number.isFinite(value2) || value2 < 0) throw new Error(`${label}.parts.${part.id}.route.rims is invalid.`);
      if (part.route.caps !== void 0 && !(typeof part.route.caps === "boolean" || Array.isArray(part.route.caps) && part.route.caps.length === 2 && part.route.caps.every((value2) => typeof value2 === "boolean"))) throw new Error(`${label}.parts.${part.id}.route.caps is invalid.`);
      if (part.route.free !== void 0 && (!Array.isArray(part.route.free) || part.route.free.length !== 2 || part.route.free.some((value2) => typeof value2 !== "boolean"))) throw new Error(`${label}.parts.${part.id}.route.free is invalid.`);
      if (part.route.limp !== void 0 && typeof part.route.limp !== "boolean" || part.route.closed !== void 0 && typeof part.route.closed !== "boolean") throw new Error(`${label}.parts.${part.id}.route limp/closed is invalid.`);
      for (const name of ["spacing", "chunk", "turn"]) if (part.route[name] !== void 0 && (!Number.isFinite(part.route[name]) || part.route[name] <= 0)) throw new Error(`${label}.parts.${part.id}.route.${name} is invalid.`);
      if (part.route.rings) {
        if (!Number.isFinite(part.route.rings.pitch) || part.route.rings.pitch <= 0) throw new Error(`${label}.parts.${part.id}.route.rings.pitch is invalid.`);
        for (const value2 of [part.route.rings.twist, part.route.rings.phase, part.route.rings.steps, part.route.rings.fade?.[0], part.route.rings.fade?.[1]]) if (value2 !== void 0 && !Number.isFinite(value2)) throw new Error(`${label}.parts.${part.id}.route.rings contains a non-finite value.`);
        if (part.route.rings.steps !== void 0 && (!Number.isInteger(part.route.rings.steps) || part.route.rings.steps < 1)) throw new Error(`${label}.parts.${part.id}.route.rings.steps is invalid.`);
      }
    }
    assertAnatomySection(part.section, `${label}.parts.${part.id}.section`);
  }
  if (value.layers !== void 0) {
    if (!Array.isArray(value.layers) || value.layers.some((layer) => typeof layer !== "string" || !layer.trim())) throw new Error(`${label}.layers must contain non-empty strings.`);
    if (new Set(value.layers).size !== value.layers.length) throw new Error(`${label}.layers contains duplicate names.`);
  }
  const groups = /* @__PURE__ */ new Set();
  for (const group2 of value.groups ?? []) {
    requireNonEmptyString(group2.id, `${label}.groups.id`);
    if (groups.has(group2.id)) throw new Error(`${label}.groups contains duplicate id ${group2.id}.`);
    groups.add(group2.id);
    if (!["turn", "slide", "hinge", "free"].includes(group2.type)) throw new Error(`${label}.groups.${group2.id}.type is invalid.`);
    if (group2.pivot) assertVec3(group2.pivot, `${label}.groups.${group2.id}.pivot`);
    if (group2.axis) assertVec3(group2.axis, `${label}.groups.${group2.id}.axis`);
    if (group2.direction) assertVec3(group2.direction, `${label}.groups.${group2.id}.direction`);
    if (group2.axis && !Math.hypot(...group2.axis) || group2.direction && !Math.hypot(...group2.direction)) throw new Error(`${label}.groups.${group2.id} axis/direction must be nonzero.`);
    if (group2.range && (!Array.isArray(group2.range) || group2.range.length !== 2 || !group2.range.every(Number.isFinite) || group2.range[1] < group2.range[0])) throw new Error(`${label}.groups.${group2.id}.range is invalid.`);
  }
  for (const group2 of value.groups ?? []) if (group2.parentId && !groups.has(group2.parentId)) throw new Error(`${label}.groups.${group2.id}.parentId references missing group ${group2.parentId}.`);
  for (const group2 of value.groups ?? []) {
    const seen = /* @__PURE__ */ new Set();
    let parent = group2.parentId;
    while (parent) {
      if (seen.has(parent)) throw new Error(`${label}.groups contains a parent cycle at ${group2.id}.`);
      seen.add(parent);
      parent = value.groups?.find((candidate) => candidate.id === parent)?.parentId;
    }
  }
  for (const part of authoredParts) {
    if (part.groupId && !groups.has(part.groupId)) throw new Error(`${label}.parts.${part.id}.groupId references missing group ${part.groupId}.`);
    if (part.parentId && !ids.has(part.parentId)) throw new Error(`${label}.parts.${part.id}.parentId references missing part ${part.parentId}.`);
    if (part.parentId === part.id) throw new Error(`${label}.parts.${part.id}.parentId cannot reference itself.`);
  }
  for (const part of authoredParts) {
    const seen = /* @__PURE__ */ new Set();
    let parent = part.parentId;
    while (parent) {
      if (seen.has(parent)) throw new Error(`${label}.parts contains a parent cycle at ${part.id}.`);
      seen.add(parent);
      parent = authoredParts.find((candidate) => candidate.id === parent)?.parentId;
    }
  }
  for (const keyframe of value.keyframes ?? []) {
    if (!Number.isFinite(keyframe.atSeconds) || keyframe.atSeconds < 0 || keyframe.atSeconds > sceneRange.end - sceneRange.start + 1e-3) throw new Error(`${label}.keyframes has an out-of-range time.`);
    if (keyframe.easing && !["linear", "none", "power1.in", "power1.out", "power1.inOut", "power2.in", "power2.out", "power2.inOut", "sine.inOut"].includes(keyframe.easing)) throw new Error(`${label}.keyframes easing is unsupported.`);
    for (const [id, state] of Object.entries(keyframe.parts ?? {})) {
      if (!ids.has(id) && !value.nativeExample) throw new Error(`${label}.keyframes.parts references missing part ${id}.`);
      for (const n of [state.opacity, state.removedOpacity]) if (n !== void 0 && (!Number.isFinite(n) || n < 0 || n > 1)) throw new Error(`${label}.keyframes.parts opacity must be in [0,1].`);
      if (state.visible !== void 0 && typeof state.visible !== "boolean") throw new Error(`${label}.keyframes.parts visible must be boolean.`);
    }
    if (!keyframe.values || typeof keyframe.values !== "object" || Array.isArray(keyframe.values)) throw new Error(`${label}.keyframes.values is invalid.`);
    for (const [id, valueAtTime] of Object.entries(keyframe.values)) {
      if (!groups.has(id) && !(value.nativeExample && nativeGroupIds.has(id))) throw new Error(`${label}.keyframes references missing group ${id}.`);
      const group2 = value.groups?.find((group3) => group3.id === id);
      if (!group2 || group2.type !== "free") {
        if (typeof valueAtTime !== "number" || !Number.isFinite(valueAtTime)) throw new Error(`${label}.keyframes.${id} must be a finite number.`);
      } else if (Array.isArray(valueAtTime)) assertVec3(valueAtTime, `${label}.keyframes.${id}`);
      else if (valueAtTime && typeof valueAtTime === "object") {
        if (!valueAtTime.translation && !valueAtTime.rotation || Object.keys(valueAtTime).some((k) => !["translation", "rotation"].includes(k))) throw new Error(`${label}.keyframes.${id} needs a supported free pose.`);
        if (valueAtTime.translation) assertVec3(valueAtTime.translation, `${label}.keyframes.${id}.translation`);
        if (valueAtTime.rotation) assertVec3(valueAtTime.rotation, `${label}.keyframes.${id}.rotation`);
      } else throw new Error(`${label}.keyframes.${id} must be a Vec3 or free pose.`);
    }
  }
  if (value.projection) {
    for (const [name, number2] of [["azimuth", value.projection.azimuth], ["elevation", value.projection.elevation], ["scale", value.projection.scale]]) if (number2 !== void 0 && (!Number.isFinite(number2) || name === "scale" && number2 <= 0)) throw new Error(`${label}.projection.${name} is invalid.`);
    if (value.projection.origin && (!Array.isArray(value.projection.origin) || value.projection.origin.length !== 2 || !value.projection.origin.every(Number.isFinite))) throw new Error(`${label}.projection.origin is invalid.`);
  }
  if (value.theme && !["light", "dark"].includes(value.theme)) throw new Error(`${label}.theme is invalid.`);
  if (value.fullClouds !== void 0 && typeof value.fullClouds !== "boolean") throw new Error(`${label}.fullClouds must be boolean.`);
  for (const readout of value.readouts ?? []) {
    requireNonEmptyString(readout.id, `${label}.readouts.id`);
    if (readout.groupId && !groups.has(readout.groupId)) throw new Error(`${label}.readouts.${readout.id}.groupId references missing group.`);
    if (readout.position && (!Array.isArray(readout.position) || readout.position.length !== 2 || !readout.position.every(Number.isFinite))) throw new Error(`${label}.readouts.${readout.id}.position is invalid.`);
    if (readout.fontSize !== void 0 && (!Number.isFinite(readout.fontSize) || readout.fontSize <= 0)) throw new Error(`${label}.readouts.${readout.id}.fontSize is invalid.`);
  }
  const controlIds = /* @__PURE__ */ new Set();
  for (const control of value.controls ?? []) {
    requireNonEmptyString(control.id, `${label}.controls.id`);
    if (controlIds.has(control.id)) throw new Error(`${label}.controls contains duplicate id ${control.id}.`);
    controlIds.add(control.id);
    if (!["pointer", "keyboard", "button"].includes(control.type)) throw new Error(`${label}.controls.${control.id}.type is invalid.`);
    if (!groups.has(control.groupId)) throw new Error(`${label}.controls.${control.id}.groupId references missing group.`);
    for (const n of [control.min, control.max, control.step, control.initial]) if (n !== void 0 && !Number.isFinite(n)) throw new Error(`${label}.controls.${control.id} contains a non-finite value.`);
    if (control.min !== void 0 && control.max !== void 0 && control.max <= control.min) throw new Error(`${label}.controls.${control.id}.max must exceed min.`);
  }
  if (value.effect) {
    requireNonEmptyString(value.effect.fragment, `${label}.effect.fragment`);
    if (value.effect.required !== void 0 && typeof value.effect.required !== "boolean") throw new Error(`${label}.effect.required must be boolean.`);
    for (const [name, uniform] of Object.entries(value.effect.uniforms ?? {})) if (!/^[a-zA-Z_][a-zA-Z0-9_]*$/.test(name) || !(typeof uniform === "number" ? Number.isFinite(uniform) : Array.isArray(uniform) && uniform.length >= 1 && uniform.length <= 4 && uniform.every(Number.isFinite))) throw new Error(`${label}.effect.uniforms.${name} is invalid.`);
  }
  const effects = value.effects ?? [];
  const effectIds = /* @__PURE__ */ new Set();
  for (const effect of effects) {
    requireNonEmptyString(effect.id, `${label}.effects.id`);
    if (effectIds.has(effect.id)) throw new Error(`${label}.effects contains duplicate id ${effect.id}.`);
    effectIds.add(effect.id);
    if (!["back", "front"].includes(effect.order)) throw new Error(`${label}.effects.${effect.id}.order is invalid.`);
    requireNonEmptyString(effect.fragment, `${label}.effects.${effect.id}.fragment`);
    if (effect.opacity !== void 0 && (!Number.isFinite(effect.opacity) || effect.opacity < 0 || effect.opacity > 1)) throw new Error(`${label}.effects.${effect.id}.opacity is invalid.`);
    for (const [name, uniform] of Object.entries(effect.uniforms ?? {})) if (!/^[a-zA-Z_][a-zA-Z0-9_]*$/.test(name) || !(typeof uniform === "number" ? Number.isFinite(uniform) : Array.isArray(uniform) && uniform.length >= 1 && uniform.length <= 4 && uniform.every(Number.isFinite))) throw new Error(`${label}.effects.${effect.id}.uniforms.${name} is invalid.`);
  }
  assertAnatomySection(value.section, `${label}.section`);
  const annotationIds = /* @__PURE__ */ new Set();
  for (const annotation of value.annotations ?? []) {
    requireNonEmptyString(annotation.id, `${label}.annotations.id`);
    if (annotationIds.has(annotation.id)) throw new Error(`${label}.annotations contains duplicate id ${annotation.id}.`);
    annotationIds.add(annotation.id);
    requireNonEmptyString(annotation.text, `${label}.annotations.${annotation.id}.text`);
    if (annotation.fontSize !== void 0 && (!Number.isFinite(annotation.fontSize) || annotation.fontSize <= 0)) throw new Error(`${label}.annotations.${annotation.id}.fontSize is invalid.`);
    if (annotation.labelOffset && (!Array.isArray(annotation.labelOffset) || annotation.labelOffset.length !== 2 || !annotation.labelOffset.every(Number.isFinite))) throw new Error(`${label}.annotations.${annotation.id}.labelOffset is invalid.`);
    if (annotation.range) {
      assertFiniteRange(annotation.range, `${label}.annotations.${annotation.id}`);
      if (annotation.range.start < 0 || annotation.range.end > sceneRange.end - sceneRange.start + 1e-3) throw new Error(`${label}.annotations.${annotation.id} is outside the scene.`);
    }
    if (Array.isArray(annotation.anchor)) assertVec3(annotation.anchor, `${label}.annotations.${annotation.id}.anchor`);
    else {
      requireNonEmptyString(annotation.anchor.partId, `${label}.annotations.${annotation.id}.anchor.partId`);
      if (!ids.has(annotation.anchor.partId)) throw new Error(`${label}.annotations.${annotation.id} references missing part ${annotation.anchor.partId}.`);
      if (annotation.anchor.offset) assertVec3(annotation.anchor.offset, `${label}.annotations.${annotation.id}.anchor.offset`);
    }
    if (annotation.color) assertSpatialColor(annotation.color, `${label}.annotations.${annotation.id}.color`);
    if (annotation.lineColor) assertSpatialColor(annotation.lineColor, `${label}.annotations.${annotation.id}.lineColor`);
  }
  if (value.background) assertSpatialColor(value.background, `${label}.background`);
}
function assertMotionLayer(layer, sceneRange, label) {
  requireNonEmptyString(layer.id, `${label}.id`);
  assertFiniteRange(layer.range, label);
  if (layer.range.start < sceneRange.start || layer.range.end > sceneRange.end)
    throw new Error(`${label} is outside its scene.`);
  if (!Number.isFinite(layer.zIndex)) throw new Error(`${label}.zIndex is invalid.`);
  if (layer.className !== void 0 && typeof layer.className !== "string")
    throw new Error(`${label}.className is invalid.`);
  if (layer.style) assertRenderStyle(layer.style, `${label}.style`);
  if (!Array.isArray(layer.nodes) || !layer.nodes.length)
    throw new Error(`${label} requires at least one node.`);
  if (!Array.isArray(layer.timeline)) throw new Error(`${label}.timeline is invalid.`);
  const ids = /* @__PURE__ */ new Set();
  for (const node of layer.nodes) {
    requireNonEmptyString(node.id, `${label}.node.id`);
    if (ids.has(node.id)) throw new Error(`${label} contains duplicate node ID ${node.id}.`);
    ids.add(node.id);
    if (!MOTION_NODE_TAGS.includes(node.tag))
      throw new Error(`${label} node ${node.id}.tag is invalid.`);
    if (node.parentId !== void 0)
      requireNonEmptyString(node.parentId, `${label} node ${node.id}.parentId`);
    if (node.text !== void 0 && typeof node.text !== "string")
      throw new Error(`${label} node ${node.id}.text is invalid.`);
    if (node.className !== void 0 && typeof node.className !== "string")
      throw new Error(`${label} node ${node.id}.className is invalid.`);
    if (node.style) assertRenderStyle(node.style, `${label} node ${node.id}.style`);
    if (node.attributes)
      assertRenderStyle(node.attributes, `${label} node ${node.id}.attributes`);
    if (node.measure !== void 0 && typeof node.measure !== "boolean")
      throw new Error(`${label} node ${node.id}.measure is invalid.`);
    if (node.semanticRole !== void 0)
      requireNonEmptyString(node.semanticRole, `${label} node ${node.id}.semanticRole`);
    if (node.tag === "img") {
      if (!node.assetId || !node.assetPath)
        throw new Error(
          `${label} image node ${node.id} references no authorized image asset.`
        );
    } else if (node.assetId || node.assetPath) {
      throw new Error(`${label} node ${node.id} can bind assets only when tag is img.`);
    }
  }
  for (const node of layer.nodes) {
    if (node.parentId && !ids.has(node.parentId))
      throw new Error(`${label} node ${node.id} has an unknown parent.`);
    const ancestors = /* @__PURE__ */ new Set([node.id]);
    let parentId = node.parentId;
    while (parentId) {
      if (ancestors.has(parentId))
        throw new Error(`${label} node hierarchy contains a cycle.`);
      ancestors.add(parentId);
      parentId = layer.nodes.find((candidate) => candidate.id === parentId)?.parentId;
    }
  }
  const layerDuration = layer.range.end - layer.range.start;
  const stepIds = /* @__PURE__ */ new Set();
  for (const step of layer.timeline) {
    requireNonEmptyString(step.id, `${label}.timeline.id`);
    if (stepIds.has(step.id))
      throw new Error(`${label} contains duplicate timeline step ID ${step.id}.`);
    stepIds.add(step.id);
    if (!["set", "to", "fromTo"].includes(step.method))
      throw new Error(`${label} step ${step.id}.method is invalid.`);
    if (!Array.isArray(step.targetIds) || !step.targetIds.length || step.targetIds.some((id) => !ids.has(id)))
      throw new Error(`${label} step ${step.id} has an invalid target.`);
    if (!Number.isFinite(step.atSeconds) || step.atSeconds < 0 || step.atSeconds > layerDuration)
      throw new Error(`${label} step ${step.id}.atSeconds is invalid.`);
    if (!Number.isFinite(step.durationSeconds) || step.durationSeconds < 0)
      throw new Error(`${label} step ${step.id}.durationSeconds is invalid.`);
    if (step.method === "set" && step.durationSeconds !== 0)
      throw new Error(`${label} set step ${step.id} must have zero duration.`);
    if (step.method === "fromTo" && !step.from)
      throw new Error(`${label} fromTo step ${step.id} requires a from state.`);
    if (step.method !== "fromTo" && step.from)
      throw new Error(`${label} step ${step.id} cannot include a from state.`);
    assertMotionTweenState(step.to, `${label} step ${step.id}.to`);
    if (step.from) assertMotionTweenState(step.from, `${label} step ${step.id}.from`);
    if (step.easing !== void 0 && typeof step.easing !== "string")
      throw new Error(`${label} step ${step.id}.easing is invalid.`);
    if (step.staggerSeconds !== void 0 && (!Number.isFinite(step.staggerSeconds) || step.staggerSeconds < 0))
      throw new Error(`${label} step ${step.id}.staggerSeconds is invalid.`);
    if (step.repeat !== void 0 && (!Number.isInteger(step.repeat) || step.repeat < 0))
      throw new Error(`${label} step ${step.id}.repeat is invalid.`);
    if (step.yoyo !== void 0 && typeof step.yoyo !== "boolean")
      throw new Error(`${label} step ${step.id}.yoyo is invalid.`);
    const repeatedDuration = step.durationSeconds * ((step.repeat ?? 0) + 1);
    const staggerDuration = (step.staggerSeconds ?? 0) * Math.max(0, step.targetIds.length - 1);
    if (step.atSeconds + repeatedDuration + staggerDuration > layerDuration + 1e-3)
      throw new Error(`${label} step ${step.id} exceeds the layer range.`);
  }
}
function assertMotionTweenState(value, label) {
  if (!value || typeof value !== "object" || Array.isArray(value) || !value.style && !value.attributes)
    throw new Error(`${label} is invalid.`);
  if (value.style) assertRenderStyle(value.style, `${label}.style`);
  if (value.attributes) assertRenderStyle(value.attributes, `${label}.attributes`);
}
function requireNonEmptyString(value, label) {
  if (typeof value !== "string" || !value.trim()) throw new Error(`${label} is required.`);
}
function assertSceneStage(value, label) {
  if (!value || typeof value !== "object") throw new Error(`${label} is invalid.`);
  if (!["none", "browser", "window", "card"].includes(value.kind))
    throw new Error(`${label}.kind is invalid.`);
  const numberWithin = (item, minimum, maximum, name) => {
    if (item === void 0) return;
    if (typeof item !== "number" || !Number.isFinite(item) || item < minimum || item > maximum)
      throw new Error(`${label}.${name} must be between ${minimum} and ${maximum}.`);
  };
  numberWithin(value.inset, 0.02, 0.18, "inset");
  numberWithin(value.radius, 0, 40, "radius");
  if (value.shadow !== void 0 && typeof value.shadow !== "boolean")
    throw new Error(`${label}.shadow must be boolean.`);
  if (value.tilt !== void 0) {
    if (!value.tilt || typeof value.tilt !== "object")
      throw new Error(`${label}.tilt is invalid.`);
    numberWithin(value.tilt.rotateX, -12, 12, "tilt.rotateX");
    numberWithin(value.tilt.rotateY, -18, 18, "tilt.rotateY");
  }
  if (value.background !== void 0)
    requireNonEmptyString(value.background, `${label}.background`);
  if (value.title !== void 0) {
    requireNonEmptyString(value.title, `${label}.title`);
    if (value.title.length > 80)
      throw new Error(`${label}.title must be at most 80 characters.`);
  }
  return value;
}
function assertRenderStyle(value, label) {
  if (!value || typeof value !== "object" || Array.isArray(value) || Object.entries(value).some(
    ([property, item]) => !property.trim() || typeof item !== "string" && typeof item !== "number"
  ))
    throw new Error(`${label} is invalid.`);
}
function assertRenderAnimation(value, label) {
  if (!Number.isFinite(value.durationSeconds) || value.durationSeconds < 0)
    throw new Error(`${label}.durationSeconds is invalid.`);
  if (value.from) assertRenderStyle(value.from, `${label}.from`);
  assertRenderStyle(value.to, `${label}.to`);
  if (value.easing !== void 0 && typeof value.easing !== "string")
    throw new Error(`${label}.easing is invalid.`);
}
function assertSceneTransition(value, label) {
  if (typeof value === "string") {
    requireNonEmptyString(value, label);
    return;
  }
  if ("id" in value) {
    requireNonEmptyString(value.id, `${label}.id`);
    if (value.durationSeconds !== void 0 && (!Number.isFinite(value.durationSeconds) || value.durationSeconds < 0))
      throw new Error(`${label}.durationSeconds is invalid.`);
    return;
  }
  assertRenderAnimation(value, label);
  for (const [property, item] of [
    ["kind", value.kind],
    ["direction", value.direction],
    ["mask", value.mask]
  ])
    if (item !== void 0) requireNonEmptyString(item, `${label}.${property}`);
  if (value.audioFade !== void 0 && typeof value.audioFade !== "boolean")
    throw new Error(`${label}.audioFade is invalid.`);
}
function assertNormalizedRect(value, label) {
  if (![value.x, value.y, value.width, value.height].every(Number.isFinite) || value.x < 0 || value.y < 0 || value.width <= 0 || value.height <= 0 || value.x + value.width > 1.001 || value.y + value.height > 1.001)
    throw new Error(`${label} is outside normalized bounds.`);
}
function assertCameraMotion(plan, durationSeconds, label) {
  requireNonEmptyString(plan.reason, `${label}.reason`);
  requireNonEmptyString(plan.mode, `${label}.mode`);
  if (!Array.isArray(plan.keyframes)) throw new Error(`${label}.keyframes is required.`);
  let previousTime = -1;
  for (const keyframe of plan.keyframes) {
    if (!Number.isFinite(keyframe.atSeconds) || keyframe.atSeconds < 0 || keyframe.atSeconds > durationSeconds + 1e-3 || keyframe.atSeconds <= previousTime || !Number.isFinite(keyframe.scale) || keyframe.scale <= 0 || !Number.isFinite(keyframe.focusX) || !Number.isFinite(keyframe.focusY) || keyframe.focusX < 0 || keyframe.focusX > 1 || keyframe.focusY < 0 || keyframe.focusY > 1 || typeof keyframe.easing !== "string" || !keyframe.easing.trim() || keyframe.blur !== void 0 && (!Number.isFinite(keyframe.blur) || keyframe.blur < 0 || keyframe.blur > 24) || keyframe.rotate !== void 0 && (!Number.isFinite(keyframe.rotate) || Math.abs(keyframe.rotate) > 25) || keyframe.frame !== void 0 && (typeof keyframe.frame !== "object" || keyframe.frame === null || ![
      keyframe.frame.x,
      keyframe.frame.y,
      keyframe.frame.width,
      keyframe.frame.height
    ].every((value) => Number.isFinite(value)) || keyframe.frame.width <= 0 || keyframe.frame.height <= 0 || keyframe.frame.x < 0 || keyframe.frame.y < 0 || keyframe.frame.x + keyframe.frame.width > 1.0001 || keyframe.frame.y + keyframe.frame.height > 1.0001))
      throw new Error(`${label} contains an invalid keyframe.`);
    previousTime = keyframe.atSeconds;
  }
}
function assertCursorOverlay(plan, sceneRange, label) {
  if (plan.sourceRange) assertFiniteRange(plan.sourceRange, `${label}.sourceRange`);
  if (plan.sourcePlaybackRate !== void 0 && (!Number.isFinite(plan.sourcePlaybackRate) || plan.sourcePlaybackRate <= 0))
    throw new Error(`${label}.sourcePlaybackRate is invalid.`);
  if (!Number.isInteger(plan.sampleIntervalMs) || plan.sampleIntervalMs < 50 || plan.sampleIntervalMs > 5e3)
    throw new Error(`${label}.sampleIntervalMs is invalid.`);
  for (const [name, value] of Object.entries({
    sizePixels: plan.sizePixels,
    clickDurationSeconds: plan.clickDurationSeconds,
    clickScale: plan.clickScale
  }))
    if (!Number.isFinite(value) || value <= 0) throw new Error(`${label}.${name} is invalid.`);
  if (!Number.isFinite(plan.zIndex)) throw new Error(`${label}.zIndex is invalid.`);
  if (!Number.isFinite(plan.opacity) || plan.opacity < 0 || plan.opacity > 1)
    throw new Error(`${label}.opacity is invalid.`);
  for (const [name, value] of Object.entries({
    shape: plan.shape,
    color: plan.color,
    outlineColor: plan.outlineColor,
    moveEasing: plan.moveEasing,
    clickColor: plan.clickColor
  }))
    requireNonEmptyString(value, `${label}.${name}`);
  if (typeof plan.showClicks !== "boolean") throw new Error(`${label}.showClicks is invalid.`);
  if (plan.style) assertRenderStyle(plan.style, `${label}.style`);
  if (plan.clickStyle) assertRenderStyle(plan.clickStyle, `${label}.clickStyle`);
  if (plan.samples !== void 0) {
    if (!Array.isArray(plan.samples)) throw new Error(`${label}.samples is invalid.`);
    let previousTime = Number.NEGATIVE_INFINITY;
    for (const sample of plan.samples) {
      if (!Number.isFinite(sample.atSeconds) || sample.atSeconds < sceneRange.start - 1e-3 || sample.atSeconds > sceneRange.end + 1e-3 || sample.atSeconds < previousTime || !Number.isFinite(sample.x) || !Number.isFinite(sample.y) || sample.x < 0 || sample.x > 1 || sample.y < 0 || sample.y > 1)
        throw new Error(`${label} contains an invalid sample.`);
      previousTime = sample.atSeconds;
    }
  }
}

// src/core/renderer.ts
import { pathToFileURL as pathToFileURL2 } from "node:url";

// src/core/spatial-capture-hook.ts
var SPATIAL_CAPTURE_MARKER = "[wandeo-spatial]";
var SPATIAL_CAPTURE_ANCHOR = "  await waitForPendingSeekCompletion(page);\n  await page.evaluate(async () => {";
function patchHyperFramesCapture(source) {
  if (source.split(SPATIAL_CAPTURE_ANCHOR).length !== 2)
    throw new Error(
      "HYPERFRAMES_CAPTURE_ADAPTER_MISMATCH: expected the pinned 0.8.3 pre-capture hook exactly once. Run setup; do not export with an unverified renderer."
    );
  return source.replace(
    SPATIAL_CAPTURE_ANCHOR,
    `  await waitForPendingSeekCompletion(page);
  const wandeoEvidence = await page.evaluate(async (time) => {
    if (typeof window.__wandeoCaptureAt !== 'function') throw new Error('SPATIAL_CAPTURE_HOOK_MISSING');
    return await window.__wandeoCaptureAt(time);
  }, quantizedTime);
  session.wandeoObserved = session.wandeoObserved || new Set();
  for (const evidence of wandeoEvidence) {
    const key = evidence.sceneId + ':' + evidence.backend + ':' + JSON.stringify(evidence.diagnostics);
    if (!session.wandeoObserved.has(key)) {
      session.wandeoObserved.add(key);
      console.error('${SPATIAL_CAPTURE_MARKER}' + JSON.stringify(evidence));
    }
  }
  await page.evaluate(async () => {`
  );
}
function spatialLoaderSource(cliUrl) {
  return `const target=${JSON.stringify(cliUrl)};const SPATIAL_CAPTURE_MARKER=${JSON.stringify(SPATIAL_CAPTURE_MARKER)};const SPATIAL_CAPTURE_ANCHOR=${JSON.stringify(SPATIAL_CAPTURE_ANCHOR)};const patch=${patchHyperFramesCapture.toString()};
export async function load(url, context, nextLoad) {const result=await nextLoad(url,context);if(url!==target)return result;return {...result,source:patch(typeof result.source==='string'?result.source:new TextDecoder().decode(result.source))};}`;
}

// src/core/spatial-bootstrap.ts
function spatialBootstrap(entries, renderStart) {
  return `(function(){
    const entries=${entries}, instances=[]; let current=${renderStart};
    for(const entry of entries){
      const canvas=document.getElementById(entry.canvasId),runtime=entry.backend==='anatomy'?window.__wandeoAnatomy:window.__wandeoSpatial;
      if(!canvas||!runtime)throw new Error('SPATIAL_BACKEND_UNAVAILABLE: '+entry.sceneId);
      const handle=runtime.mount(canvas,entry.config);instances.push({...entry,handle});
    }
    const ready=Promise.all(instances.map(i=>i.handle.ready)).then(()=>document.fonts.ready);
    ready.catch(error=>{window.__wandeoSpatialError=String(error);});
    window.__wandeoSpatialReady=ready;
    window.__wandeoSpatialInstances=Object.fromEntries(instances.map(i=>[i.canvasId,i.handle]));
    window.__wandeoRenderAt=(time)=>{current=time;for(const i of instances)i.handle.renderAt(time);};
    window.__wandeoCaptureAt=async(relative)=>{
      await ready;const time=${renderStart}+relative;window.__wandeoRenderAt(time);
      await Promise.all(instances.map(i=>i.handle.paintReady?.()));
      document.getElementById('composition-root').getBoundingClientRect();
      const evidence=instances.filter(i=>time>=i.config.sceneRange.start&&time<i.config.sceneRange.end).map(i=>({sceneId:i.sceneId,requestedBackend:i.backend,atSeconds:time,...(i.handle.evidence?i.handle.evidence():i.handle.metadata),diagnostics:i.handle.diagnostics||[]}));
      window.__wandeoSpatialDiagnostics=evidence.flatMap(i=>i.diagnostics);
      const errors=evidence.flatMap(i=>i.diagnostics.filter(d=>d.severity==='error'));
      if(errors.length)throw new Error(JSON.stringify(errors));
      return evidence;
    };
    ready.then(()=>window.__wandeoCaptureAt(0)).catch(()=>{});
    // Preview players may seek independently; production always uses the explicit pre-capture hook.
    window.__wandeoTimeline?.eventCallback('onUpdate',()=>{current=${renderStart}+window.__wandeoTimeline.time();ready.then(()=>window.__wandeoRenderAt(current)).catch(()=>{});});
    window.addEventListener('hf-seek',e=>{const p=window.__wandeoCaptureAt(Number(e.detail?.time)||0);e.detail?.waitUntil?.(p);});
  })();`;
}

// src/core/renderer.ts
import { execFile, spawn as spawn2 } from "node:child_process";
import { createHash as createHash4 } from "node:crypto";
import fs7 from "node:fs/promises";
import { existsSync as existsSync2 } from "node:fs";
import os4 from "node:os";
import path9 from "node:path";
import { promisify } from "node:util";

// src/core/cinematicFx.ts
var ENVIRONMENT_TRACK = 1;
var POST_FX_TRACK = 9500;
var LIFT_TRACK_OFFSET = 30;
var LIFT_RECIPE_IDS = /* @__PURE__ */ new Set(["element-lift", "layer-explode", "depth-parallax"]);
var FX_TRANSITION_IDS = [
  "glitch-cut",
  "light-leak",
  "ripple",
  "cube-rotate",
  "slice-wipe",
  "chroma-split"
];
function seconds(value) {
  return Number(value.toFixed(4));
}
function json(value) {
  return JSON.stringify(value).replace(/</g, "\\u003c");
}
function escapeHtml(value) {
  return value.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
}
function seededRandom(seed) {
  let state = 2654435769;
  for (const char of seed) state = Math.imul(state ^ char.charCodeAt(0), 2246822507) >>> 0;
  return () => {
    state = state + 1831565813 >>> 0;
    let t = state;
    t = Math.imul(t ^ t >>> 15, t | 1);
    t ^= t + Math.imul(t ^ t >>> 7, t | 61);
    return ((t ^ t >>> 14) >>> 0) / 4294967296;
  };
}
function assertSafeColor(value) {
  const trimmed = value.trim();
  if (!trimmed || /[;<>{}]/.test(trimmed) || /url\s*\(|expression|javascript/i.test(trimmed))
    throw new Error(`Environment colour is not a safe CSS colour: ${value}`);
  return trimmed;
}
var GRAIN_SVG = "data:image/svg+xml;utf8," + encodeURIComponent(
  `<svg xmlns="http://www.w3.org/2000/svg" width="240" height="240"><filter id="g"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" stitchTiles="stitch" seed="3"/><feColorMatrix values="0 0 0 0 0.5 0 0 0 0 0.5 0 0 0 0 0.5 0 0 0 0.9 0"/></filter><rect width="100%" height="100%" filter="url(#g)"/></svg>`
);
function environmentMarkup(project, environment, timeline, clipDuration = project.durationSeconds) {
  if (environment.kind === "none") return "";
  const [base, mid, highlight] = environment.colors.map(assertSafeColor);
  const duration = seconds(project.durationSeconds);
  const intensity = Math.max(0, Math.min(1, environment.intensity));
  const random = seededRandom(project.projectId);
  const clip = `data-start="0" data-duration="${seconds(clipDuration)}" data-track-index="${ENVIRONMENT_TRACK}"`;
  const drift = (target, index) => {
    const amplitude = project.width * (0.06 + 0.05 * intensity);
    const period = 9 + index * 3.5;
    const cycles = Math.max(1, Math.ceil(project.durationSeconds / period));
    timeline.push(
      `tl.to(${json(target)},${json({ x: seconds(amplitude * (index % 2 ? -1 : 1)), y: seconds(amplitude * 0.45 * (index % 3 ? 1 : -1)), scale: 1.18, duration: period / 2, yoyo: true, repeat: cycles * 2, ease: "sine.inOut" })},0);`
    );
  };
  let inner = "";
  if (environment.kind === "aurora" || environment.kind === "mesh") {
    const blobs = environment.kind === "aurora" ? 3 : 4;
    inner = Array.from({ length: blobs }, (_, index) => {
      const colour = [highlight, mid, highlight, mid][index];
      const left = 10 + random() * 70;
      const top = 5 + random() * 70;
      const size = (environment.kind === "aurora" ? 0.62 : 0.5) * (0.85 + random() * 0.4);
      drift(`#env-blob-${index}`, index);
      return `<i id="env-blob-${index}" class="env-blob" style="left:${seconds(left)}%;top:${seconds(top)}%;width:${seconds(size * 100)}%;padding-top:${seconds(size * 70)}%;background:radial-gradient(circle at 50% 50%,${colour} 0%,transparent 66%);opacity:${seconds(0.28 + 0.34 * intensity)}"></i>`;
    }).join("");
  } else if (environment.kind === "grid") {
    drift("#env-grid-glow", 0);
    inner = `<i class="env-grid" style="background-image:linear-gradient(${mid} 1px,transparent 1px),linear-gradient(90deg,${mid} 1px,transparent 1px);opacity:${seconds(0.16 + 0.2 * intensity)}"></i><i id="env-grid-glow" class="env-blob" style="left:50%;top:40%;width:70%;padding-top:50%;background:radial-gradient(circle,${highlight} 0%,transparent 65%);opacity:${seconds(0.22 + 0.3 * intensity)}"></i>`;
    timeline.push(
      `tl.to(".env-grid",${json({ backgroundPosition: `${seconds(project.width * 0.08)}px ${seconds(project.height * 0.05)}px`, duration, ease: "none" })},0);`
    );
  } else if (environment.kind === "particles") {
    const count = 28;
    inner = Array.from({ length: count }, (_, index) => {
      const left = random() * 100;
      const top = random() * 100;
      const size = 2 + random() * 5;
      const rise = project.height * (0.08 + random() * 0.18);
      const period = 6 + random() * 8;
      const cycles = Math.max(1, Math.ceil(project.durationSeconds / period));
      timeline.push(
        `tl.fromTo(${json(`#env-p-${index}`)},${json({ y: 0, opacity: 0.1 })},${json({ y: seconds(-rise), opacity: seconds(0.35 + 0.5 * intensity), duration: period / 2, yoyo: true, repeat: cycles * 2, ease: "sine.inOut" })},${seconds(-random() * period)});`
      );
      return `<i id="env-p-${index}" class="env-particle" style="left:${seconds(left)}%;top:${seconds(top)}%;width:${seconds(size)}px;height:${seconds(size)}px;background:${index % 4 ? mid : highlight}"></i>`;
    }).join("");
    inner += `<i class="env-blob" style="left:50%;top:50%;width:80%;padding-top:60%;background:radial-gradient(circle,${mid} 0%,transparent 70%);opacity:${seconds(0.18 + 0.22 * intensity)}"></i>`;
  }
  return `<div id="environment" class="clip environment env-${environment.kind}" ${clip} style="background:${base}" aria-hidden="true">${inner}</div>`;
}
function postFxMarkup(project, environment, accentColor, timeline, clipDuration = project.durationSeconds) {
  const grain = Math.max(0, Math.min(1, environment.grain));
  const vignette = Math.max(0, Math.min(1, environment.vignette));
  if (grain <= 0 && vignette <= 0 && !environment.lightLeak) return "";
  const duration = seconds(project.durationSeconds);
  const clip = `data-start="0" data-duration="${seconds(clipDuration)}" data-track-index="${POST_FX_TRACK}"`;
  const layers = [];
  if (grain > 0) {
    layers.push(
      `<i class="post-grain" style="background-image:url('${GRAIN_SVG}');opacity:${seconds(0.05 + grain * 0.16)}"></i>`
    );
    const steps = Math.max(2, Math.round(project.durationSeconds * project.fps));
    timeline.push(
      `tl.to(".post-grain",${json({ backgroundPosition: `${240 * 13}px ${240 * 7}px`, duration, ease: `steps(${steps})` })},0);`
    );
  }
  if (vignette > 0)
    layers.push(
      `<i class="post-vignette" style="opacity:${seconds(0.35 + vignette * 0.55)}"></i>`
    );
  if (environment.lightLeak) {
    const period = 11;
    const cycles = Math.max(1, Math.ceil(project.durationSeconds / period));
    layers.push(
      `<i class="post-leak" style="background:radial-gradient(ellipse at 50% 50%,${assertSafeColor(accentColor)} 0%,transparent 60%)"></i>`
    );
    timeline.push(
      `tl.fromTo(".post-leak",${json({ xPercent: -70, yPercent: -30, opacity: 0 })},${json({ xPercent: 70, yPercent: 30, opacity: 0.32, duration: period / 2, yoyo: true, repeat: cycles * 2, ease: "sine.inOut" })},0);`
    );
  }
  return `<div id="post-fx" class="clip post-fx" ${clip} aria-hidden="true">${layers.join("")}</div>`;
}
function parameterNumber(recipe, name, fallback) {
  const value = recipe?.parameters?.[name];
  return typeof value === "number" && Number.isFinite(value) ? value : fallback;
}
function liftRegions(recipe) {
  const regions = [];
  for (const suffix of ["", "2", "3"]) {
    const x = recipe?.parameters?.[`x${suffix}`];
    const y = recipe?.parameters?.[`y${suffix}`];
    const width = recipe?.parameters?.[`width${suffix}`];
    const height = recipe?.parameters?.[`height${suffix}`];
    if ([x, y, width, height].every(
      (value) => typeof value === "number" && Number.isFinite(value)
    )) {
      const region = {
        x: Math.max(0, Math.min(0.95, x)),
        y: Math.max(0, Math.min(0.95, y)),
        width: Math.max(0.04, Math.min(1, width)),
        height: Math.max(0.04, Math.min(1, height))
      };
      region.width = Math.min(region.width, 1 - region.x);
      region.height = Math.min(region.height, 1 - region.y);
      regions.push(region);
    }
  }
  return regions;
}
function liftLayersMarkup(input) {
  const { scene, sceneIndex, project, timeline } = input;
  const recipeId = scene.recipe?.id;
  if (!recipeId || !LIFT_RECIPE_IDS.has(recipeId)) return "";
  const regions = liftRegions(scene.recipe);
  if (!regions.length) return "";
  const start = scene.range.start;
  const duration = scene.range.end - scene.range.start;
  const lift = parameterNumber(scene.recipe, "lift", recipeId === "depth-parallax" ? 1.06 : 1.12);
  const dim = parameterNumber(scene.recipe, "dim", recipeId === "depth-parallax" ? 0.18 : 0.42);
  const blur = parameterNumber(scene.recipe, "blur", recipeId === "depth-parallax" ? 2 : 8);
  const tilt = parameterNumber(scene.recipe, "tilt", 7);
  const radius = parameterNumber(scene.recipe, "radius", 12);
  const entrance = Math.min(0.9, duration * 0.3);
  const settle2 = duration > 2.4 ? Math.min(0.7, duration * 0.2) : 0;
  const baseTarget = `#visual-clip-${sceneIndex}-${input.layerIndex}`;
  const sceneTarget = `#scene-${sceneIndex}`;
  timeline.push(
    `tl.set(${json(baseTarget)},${json({ filter: "blur(0px) brightness(1)" })},${seconds(input.clipStart)});`,
    `tl.to(${json(baseTarget)},${json({ filter: `blur(${seconds(blur)}px) brightness(${seconds(1 - dim)})`, scale: 1.03, duration: seconds(entrance), ease: "power2.out" })},${seconds(start + 0.1)});`
  );
  if (settle2)
    timeline.push(
      `tl.to(${json(baseTarget)},${json({ filter: "blur(0px) brightness(1)", scale: 1, duration: seconds(settle2), ease: "power2.inOut" })},${seconds(scene.range.end - settle2)});`
    );
  if (recipeId !== "element-lift") {
    timeline.push(
      `tl.set(${json(sceneTarget)},${json({ perspective: 1500 })},${seconds(input.clipStart)});`,
      `tl.fromTo(${json(sceneTarget)},${json({ rotationY: -tilt, rotationX: tilt * 0.35 })},${json({ rotationY: tilt, rotationX: -tilt * 0.35, duration: seconds(duration), ease: "sine.inOut" })},${seconds(start)});`
    );
    if (settle2)
      timeline.push(
        `tl.to(${json(sceneTarget)},${json({ rotationY: 0, rotationX: 0, duration: seconds(settle2), ease: "power2.inOut", overwrite: "auto" })},${seconds(scene.range.end - settle2)});`
      );
  }
  if (recipeId === "depth-parallax") {
    const shift = project.width * 0.012;
    timeline.push(
      `tl.fromTo(${json(baseTarget)},${json({ x: -shift, y: -shift * 0.5 })},${json({ x: shift, y: shift * 0.5, duration: seconds(duration), ease: "sine.inOut" })},${seconds(start)});`
    );
  }
  return regions.map((region, regionIndex) => {
    const frameId = `lift-${sceneIndex}-${input.layerIndex}-${regionIndex}`;
    const mediaId = `${frameId}-media`;
    const regionLift = recipeId === "layer-explode" ? lift + regionIndex * 0.06 : lift;
    const rise = project.height * (recipeId === "depth-parallax" ? 6e-3 : 0.014) * (regionIndex + 1);
    const delay = regionIndex * 0.14;
    const frameStyle = [
      `left:${seconds(region.x * 100)}%`,
      `top:${seconds(region.y * 100)}%`,
      `width:${seconds(region.width * 100)}%`,
      `height:${seconds(region.height * 100)}%`,
      `border-radius:${seconds(radius)}px`,
      "opacity:0"
    ].join(";");
    const mediaStyle = [
      `left:${seconds(-region.x / region.width * 100)}%`,
      `top:${seconds(-region.y / region.height * 100)}%`,
      `width:${seconds(1 / region.width * 100)}%`,
      `height:${seconds(1 / region.height * 100)}%`
    ].join(";");
    timeline.push(
      `tl.set(${json(`#${frameId}`)},${json({ opacity: 0, scale: 1, y: 0, transformOrigin: "50% 50%" })},${seconds(input.clipStart)});`,
      `tl.to(${json(`#${frameId}`)},${json({ opacity: 1, scale: regionLift, y: seconds(-rise), boxShadow: "0 28px 70px rgba(0,0,0,.55),0 0 0 1px rgba(255,255,255,.12)", duration: seconds(entrance), ease: "expo.out" })},${seconds(start + 0.12 + delay)});`
    );
    if (recipeId === "depth-parallax") {
      const shift = project.width * 0.01 * (regionIndex + 1);
      timeline.push(
        `tl.fromTo(${json(`#${frameId}`)},${json({ x: shift })},${json({ x: -shift, duration: seconds(duration), ease: "sine.inOut" })},${seconds(start)});`
      );
    }
    if (settle2)
      timeline.push(
        `tl.to(${json(`#${frameId}`)},${json({ opacity: 0, scale: 1, y: 0, duration: seconds(settle2 * 0.8), ease: "power2.in" })},${seconds(scene.range.end - settle2)});`
      );
    return `<div id="${frameId}" class="lift-frame" style="${frameStyle}"><video id="${mediaId}" class="clip lift-media" src="${escapeHtml(input.mediaUrl)}" muted playsinline data-start="${seconds(input.clipStart)}" data-duration="${seconds(input.clipDuration)}" data-track-index="${input.trackIndex + regionIndex}" data-media-start="${seconds(input.mediaStart)}" data-playback-rate="${seconds(input.playbackRate)}" style="${mediaStyle}"></video></div>`;
  }).join("");
}
function isFxTransition(id) {
  return FX_TRANSITION_IDS.includes(id);
}
function fxTransitionMarkup(transition, index, boundarySeconds, accentColor, trackIndex, renderRange = { start: 0, end: Number.POSITIVE_INFINITY }) {
  if (!isFxTransition(transition.id)) return "";
  const duration = transition.durationSeconds ?? 0.5;
  const start = Math.max(renderRange.start, 0, boundarySeconds - duration / 2);
  const end = Math.min(renderRange.end, boundarySeconds + duration / 2);
  if (end <= start) return "";
  const clip = `data-start="${seconds(start - renderRange.start)}" data-duration="${seconds(end - start)}" data-track-index="${trackIndex}"`;
  const id = `transition-${index}`;
  switch (transition.id) {
    case "glitch-cut":
      return `<div id="${id}" class="clip transition-overlay transition-glitch-cut" ${clip} aria-hidden="true">${[
        0.12,
        0.31,
        0.47,
        0.66,
        0.82
      ].map(
        (top, i) => `<i style="top:${seconds(top * 100)}%;height:${3 + i % 3 * 2}%;background:${[accentColor, "#ff2d55", "#00e5ff", accentColor, "#ffffff"][i]}"></i>`
      ).join("")}</div>`;
    case "light-leak":
      return `<div id="${id}" class="clip transition-overlay transition-light-leak" ${clip} aria-hidden="true"><i style="background:radial-gradient(ellipse at 50% 50%,#ffd9a8 0%,${assertSafeColor(accentColor)} 30%,transparent 62%)"></i></div>`;
    case "ripple":
      return `<svg id="${id}-defs" class="fx-defs" width="0" height="0" aria-hidden="true"><filter id="fx-ripple-${index}" x="-10%" y="-10%" width="120%" height="120%"><feTurbulence type="fractalNoise" baseFrequency="0.011 0.019" numOctaves="2" seed="${7 + index}" result="noise"/><feDisplacementMap class="fx-ripple-map" in="SourceGraphic" in2="noise" scale="0" xChannelSelector="R" yChannelSelector="G"/></filter></svg>`;
    case "cube-rotate":
      return "";
    case "slice-wipe":
      return `<div id="${id}" class="clip transition-overlay transition-slice-wipe" ${clip} aria-hidden="true">${Array.from(
        { length: 8 },
        (_, i) => `<i style="left:${i * 12.5}%;background:${assertSafeColor(accentColor)}"></i>`
      ).join("")}</div>`;
    case "chroma-split":
      return `<svg id="${id}-defs" class="fx-defs" width="0" height="0" aria-hidden="true"><filter id="fx-chroma-${index}" x="-10%" y="-10%" width="120%" height="120%" color-interpolation-filters="sRGB"><feColorMatrix in="SourceGraphic" type="matrix" values="1 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 1 0" result="r"/><feOffset class="fx-chroma-r" in="r" dx="0" dy="0" result="ro"/><feColorMatrix in="SourceGraphic" type="matrix" values="0 0 0 0 0  0 1 0 0 0  0 0 0 0 0  0 0 0 1 0" result="g"/><feColorMatrix in="SourceGraphic" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 1 0 0  0 0 0 1 0" result="b"/><feOffset class="fx-chroma-b" in="b" dx="0" dy="0" result="bo"/><feBlend in="ro" in2="g" mode="screen" result="rg"/><feBlend in="rg" in2="bo" mode="screen"/></filter></svg>`;
    default:
      return "";
  }
}
function applyFxTransition(transition, index, current, timeline) {
  if (!isFxTransition(transition.id)) return false;
  const boundary = current.range.start;
  const duration = transition.durationSeconds ?? 0.5;
  const half = duration / 2;
  const direction = transition.direction ?? "left";
  const sign = direction === "right" || direction === "down" ? 1 : -1;
  const intensity = transition.intensity ?? 1;
  const outgoing = `#scene-${index}`;
  const incoming = `#scene-${index + 1}`;
  const overlay = `#transition-${index}`;
  switch (transition.id) {
    case "glitch-cut": {
      const steps = 7;
      const stepSeconds = duration / steps;
      timeline.push(
        `tl.set(${json(incoming)},${json({ opacity: 0 })},${seconds(boundary - half)});`
      );
      for (let step = 0; step < steps; step += 1) {
        const at = boundary - half + step * stepSeconds;
        const target = at < boundary ? outgoing : incoming;
        const offset = (step % 2 ? -1 : 1) * (10 + step * 4) * intensity;
        timeline.push(
          `tl.set(${json(target)},${json({ x: seconds(offset), skewX: seconds(offset * 0.15), filter: `hue-rotate(${seconds(step % 3 * 60)}deg) contrast(1.25)` })},${seconds(at)});`,
          `tl.set(${json(`${overlay} i`)},${json({ opacity: step % 2 ? 0.9 : 0.35, x: seconds(-offset * 2), scaleX: 1 + step % 3 * 0.2 })},${seconds(at)});`
        );
        if (step === Math.floor(steps / 2))
          timeline.push(
            `tl.set(${json(incoming)},${json({ opacity: 1 })},${seconds(at)});`
          );
      }
      timeline.push(
        `tl.set(${json(`${outgoing},${incoming}`)},${json({ x: 0, skewX: 0, filter: "none" })},${seconds(boundary + half)});`,
        `tl.set(${json(`${overlay} i`)},${json({ opacity: 0 })},${seconds(boundary + half)});`
      );
      return true;
    }
    case "light-leak":
      timeline.push(
        `tl.fromTo(${json(incoming)},${json({ opacity: 0 })},${json({ opacity: 1, duration: seconds(duration), ease: "power2.inOut" })},${seconds(boundary - half)});`,
        `tl.fromTo(${json(`${overlay} i`)},${json({ xPercent: sign * -60, opacity: 0, scale: 0.8 })},${json({ xPercent: sign * 60, opacity: 0.95 * intensity, scale: 1.3, duration: seconds(duration), ease: "sine.inOut" })},${seconds(boundary - half)});`,
        `tl.to(${json(`${overlay} i`)},${json({ opacity: 0, duration: seconds(half * 0.6), ease: "power2.out" })},${seconds(boundary + half * 0.4)});`
      );
      return true;
    case "ripple":
      timeline.push(
        `tl.set(${json(incoming)},${json({ opacity: 0, filter: `url(#fx-ripple-${index})` })},${seconds(boundary - half)});`,
        `tl.to(${json(`#fx-ripple-${index} .fx-ripple-map`)},${json({ attr: { scale: seconds(110 * intensity) }, duration: seconds(half), ease: "power2.in" })},${seconds(boundary - half)});`,
        `tl.to(${json(incoming)},${json({ opacity: 1, duration: seconds(duration * 0.7), ease: "power1.inOut" })},${seconds(boundary - half * 0.6)});`,
        `tl.to(${json(`#fx-ripple-${index} .fx-ripple-map`)},${json({ attr: { scale: 0 }, duration: seconds(half), ease: "power2.out" })},${seconds(boundary)});`,
        `tl.set(${json(incoming)},${json({ filter: "none" })},${seconds(boundary + half + 0.01)});`
      );
      return true;
    case "cube-rotate": {
      const horizontal = direction === "left" || direction === "right";
      const axis = horizontal ? "rotationY" : "rotationX";
      const outOrigin = horizontal ? sign < 0 ? "0% 50%" : "100% 50%" : sign < 0 ? "50% 0%" : "50% 100%";
      const inOrigin = horizontal ? sign < 0 ? "100% 50%" : "0% 50%" : sign < 0 ? "50% 100%" : "50% 0%";
      const shift = horizontal ? "xPercent" : "yPercent";
      timeline.push(
        `tl.set("#composition-root",${json({ perspective: 1400 })},${seconds(boundary - half)});`,
        `tl.set(${json(incoming)},${json({ [axis]: sign * -90 * (horizontal ? -1 : 1), transformOrigin: inOrigin, [shift]: sign * 100 })},${seconds(boundary - half)});`,
        `tl.to(${json(outgoing)},${json({ [axis]: sign * 90 * (horizontal ? -1 : 1), transformOrigin: outOrigin, [shift]: sign * -100, duration: seconds(duration), ease: "power2.inOut" })},${seconds(boundary - half)});`,
        `tl.to(${json(incoming)},${json({ [axis]: 0, [shift]: 0, duration: seconds(duration), ease: "power2.inOut" })},${seconds(boundary - half)});`
      );
      return true;
    }
    case "slice-wipe": {
      const from = direction === "right" ? "inset(0 0 0 100%)" : direction === "up" ? "inset(100% 0 0 0)" : direction === "down" ? "inset(0 0 100% 0)" : "inset(0 100% 0 0)";
      timeline.push(
        `tl.set(${json(incoming)},${json({ clipPath: from })},${seconds(boundary - half)});`,
        `tl.to(${json(incoming)},${json({ clipPath: "inset(0 0 0 0)", duration: seconds(duration), ease: "steps(8)" })},${seconds(boundary - half)});`,
        `tl.set(${json(incoming)},${json({ clipPath: "none" })},${seconds(boundary + half + 0.01)});`,
        `tl.fromTo(${json(`${overlay} i`)},${json({ scaleY: 0, opacity: 0.85 * intensity, transformOrigin: sign < 0 ? "50% 100%" : "50% 0%" })},${json({ scaleY: 1, duration: seconds(half), stagger: seconds(half / 8), ease: "power3.out" })},${seconds(boundary - half)});`,
        `tl.to(${json(`${overlay} i`)},${json({ opacity: 0, duration: seconds(half), stagger: seconds(half / 8), ease: "power2.in" })},${seconds(boundary - half * 0.4)});`
      );
      return true;
    }
    case "chroma-split": {
      const spread2 = seconds(22 * intensity);
      const filter = `url(#fx-chroma-${index})`;
      timeline.push(
        `tl.set(${json(`${outgoing},${incoming}`)},${json({ filter })},${seconds(boundary - half)});`,
        `tl.set(${json(incoming)},${json({ opacity: 0 })},${seconds(boundary - half)});`,
        `tl.to(${json(`#fx-chroma-${index} .fx-chroma-r`)},${json({ attr: { dx: spread2 }, duration: seconds(half), ease: "power3.in" })},${seconds(boundary - half)});`,
        `tl.to(${json(`#fx-chroma-${index} .fx-chroma-b`)},${json({ attr: { dx: -spread2 }, duration: seconds(half), ease: "power3.in" })},${seconds(boundary - half)});`,
        `tl.set(${json(incoming)},${json({ opacity: 1 })},${seconds(boundary)});`,
        `tl.to(${json(`#fx-chroma-${index} .fx-chroma-r`)},${json({ attr: { dx: 0 }, duration: seconds(half), ease: "power3.out" })},${seconds(boundary)});`,
        `tl.to(${json(`#fx-chroma-${index} .fx-chroma-b`)},${json({ attr: { dx: 0 }, duration: seconds(half), ease: "power3.out" })},${seconds(boundary)});`,
        `tl.set(${json(`${outgoing},${incoming}`)},${json({ filter: "none" })},${seconds(boundary + half + 0.01)});`
      );
      return true;
    }
    default:
      return false;
  }
}
function cameraShakeStatements(target, shake, start, duration, timeline) {
  const amplitude = Math.max(0, Math.min(40, shake.amplitude));
  const frequency = Math.max(0.2, Math.min(8, shake.frequency));
  if (amplitude <= 0 || duration <= 0) return;
  const step = 0.125;
  const count = Math.min(400, Math.floor(duration / step));
  timeline.push(
    `tl.set(${json(target)},${json({ x: 0, y: 0, rotation: 0 })},${seconds(start)});`
  );
  for (let i = 1; i <= count; i += 1) {
    const t = i * step;
    const phase = 2 * Math.PI * frequency * t;
    const x = amplitude * (Math.sin(phase) + 0.5 * Math.sin(phase * 2.3 + 1.1));
    const y = amplitude * 0.7 * (Math.cos(phase * 1.3) + 0.4 * Math.sin(phase * 3.1 + 0.4));
    const rotation = amplitude * 0.02 * Math.sin(phase * 0.7 + 0.8);
    timeline.push(
      `tl.to(${json(target)},${json({ x: seconds(x), y: seconds(y), rotation: seconds(rotation), duration: step, ease: "sine.inOut" })},${seconds(start + (i - 1) * step)});`
    );
  }
  timeline.push(
    `tl.to(${json(target)},${json({ x: 0, y: 0, rotation: 0, duration: 0.3, ease: "power2.out" })},${seconds(start + count * step)});`
  );
}
var CINEMATIC_FX_CSS = [
  ".environment{position:absolute;inset:0;overflow:hidden}",
  ".env-blob{position:absolute;display:block;transform:translate(-50%,-50%);filter:blur(60px);will-change:transform}",
  ".env-grid{position:absolute;inset:-20%;background-size:64px 64px}",
  ".env-particle{position:absolute;display:block;border-radius:50%;filter:blur(.5px)}",
  ".post-fx{position:absolute;inset:0;pointer-events:none}",
  ".post-grain{position:absolute;inset:-240px;background-size:240px 240px;mix-blend-mode:overlay}",
  ".post-vignette{position:absolute;inset:0;background:radial-gradient(120% 100% at 50% 50%,transparent 52%,rgba(0,0,0,.72) 100%)}",
  ".post-leak{position:absolute;left:-10%;top:-20%;width:120%;height:140%;mix-blend-mode:screen;opacity:0}",
  ".lift-frame{position:absolute;z-index:30;overflow:hidden;will-change:transform;background:#000}",
  ".lift-media{position:absolute;object-fit:cover;object-position:50% 50%}",
  ".transition-glitch-cut i{position:absolute;left:-5%;width:110%;opacity:0;mix-blend-mode:screen}",
  ".transition-light-leak i{position:absolute;left:-10%;top:-30%;width:120%;height:160%;mix-blend-mode:screen;opacity:0}",
  ".transition-slice-wipe i{position:absolute;top:0;bottom:0;width:12.5%;opacity:0}",
  ".fx-defs{position:absolute;width:0;height:0;overflow:hidden}"
].join("");
function defaultEnvironment(backgroundColor, accentColor, override) {
  const base = backgroundColor === "transparent" ? "#07090d" : backgroundColor;
  return {
    kind: override ?? "aurora",
    colors: [base, `color-mix(in srgb, ${accentColor} 35%, ${base})`, accentColor],
    intensity: 0.8,
    grain: 0.2,
    vignette: 0.45,
    lightLeak: true
  };
}

// src/core/brandStyles.ts
var SOFTWARE_PROMO_BRAND_STYLES = [
  {
    id: "precision-light",
    name: "\u7CBE\u5BC6\u660E\u4EAE",
    description: "\u6E05\u6670\u3001\u514B\u5236\u3001\u53EF\u4FE1\uFF0C\u9002\u5408\u6548\u7387\u5DE5\u5177\u3001\u534F\u4F5C\u8F6F\u4EF6\u548C\u6570\u636E\u4EA7\u54C1\u3002",
    colors: {
      primary: "#111827",
      accent: "#0ea5a4",
      background: "#f7f8fa",
      surface: "#ffffff",
      text: "#101828"
    },
    typography: { fontFamily: "Inter, PingFang SC, Microsoft YaHei", displayWeight: 700, bodyWeight: 500 },
    motion: { easing: "power2.out", entranceSeconds: 0.55, transitionIntensity: 0.7 },
    caption: { position: "bottom-safe", background: "rgba(16,24,40,.88)", color: "#ffffff" },
    surface: {
      radiusPixels: 8,
      shadow: "0 20px 60px rgba(16,24,40,.16)",
      border: "rgba(16,24,40,.12)"
    },
    environment: {
      kind: "mesh",
      colors: ["#f3f5f8", "#dfe8f2", "#bfe9e6"],
      intensity: 0.55,
      grain: 0.1,
      vignette: 0.22,
      lightLeak: false
    },
    recommendedRecipes: ["ui-focus-zoom", "feature-callout", "step-process-rail"],
    avoidRecipes: ["problem-pressure"]
  },
  {
    id: "cinematic-dark",
    name: "\u7535\u5F71\u6697\u573A",
    description: "\u9AD8\u5BF9\u6BD4\u3001\u805A\u5149\u548C\u6DF1\u8272\u821E\u53F0\uFF0C\u9002\u5408 AI\u3001\u5F00\u53D1\u8005\u5DE5\u5177\u4E0E\u9AD8\u7AEF\u53D1\u5E03\u7247\u3002",
    colors: {
      primary: "#f8fafc",
      accent: "#22d3ee",
      background: "#07090d",
      surface: "#11151c",
      text: "#f8fafc"
    },
    typography: { fontFamily: "Inter, PingFang SC, Microsoft YaHei", displayWeight: 750, bodyWeight: 500 },
    motion: { easing: "expo.out", entranceSeconds: 0.75, transitionIntensity: 1 },
    caption: { position: "bottom-safe", background: "rgba(0,0,0,.76)", color: "#ffffff" },
    surface: {
      radiusPixels: 8,
      shadow: "0 28px 90px rgba(0,0,0,.58)",
      border: "rgba(255,255,255,.14)"
    },
    environment: {
      kind: "aurora",
      colors: ["#05070b", "#0d2f3d", "#22d3ee"],
      intensity: 1,
      grain: 0.3,
      vignette: 0.6,
      lightLeak: true
    },
    recommendedRecipes: ["product-hero-spotlight", "browser-fly-in", "brand-close"],
    avoidRecipes: ["step-process-rail"]
  },
  {
    id: "bold-contrast",
    name: "\u5927\u80C6\u649E\u8272",
    description: "\u9C9C\u660E\u8272\u5757\u3001\u5FEB\u901F\u843D\u4F4D\u548C\u5F3A\u4FE1\u606F\u5C42\u7EA7\uFF0C\u9002\u5408\u589E\u957F\u3001\u8425\u9500\u4E0E\u521B\u4F5C\u8005\u4EA7\u54C1\u3002",
    colors: {
      primary: "#101010",
      accent: "#ff3d5a",
      background: "#fffdf8",
      surface: "#ffffff",
      text: "#101010"
    },
    typography: { fontFamily: "Arial, PingFang SC, Microsoft YaHei", displayWeight: 800, bodyWeight: 600 },
    motion: { easing: "back.out(1.25)", entranceSeconds: 0.42, transitionIntensity: 1.2 },
    caption: { position: "bottom-safe", background: "#101010", color: "#ffffff" },
    surface: { radiusPixels: 4, shadow: "10px 10px 0 rgba(16,16,16,.16)", border: "#101010" },
    environment: {
      kind: "particles",
      colors: ["#0b0b0f", "#f59e0b", "#fde68a"],
      intensity: 0.9,
      grain: 0.22,
      vignette: 0.5,
      lightLeak: true
    },
    recommendedRecipes: ["multi-screen-carousel", "before-after-split", "metric-proof"],
    avoidRecipes: ["product-hero-spotlight"]
  },
  {
    id: "editorial-tech",
    name: "\u6280\u672F\u7F16\u8F91\u611F",
    description: "\u7F51\u683C\u3001\u7CBE\u7EC6\u7EBF\u6761\u548C\u5185\u5BB9\u4F18\u5148\u7684\u6742\u5FD7\u5F0F\u8868\u8FBE\uFF0C\u9002\u5408\u590D\u6742\u529F\u80FD\u4E0E\u5DE5\u4F5C\u6D41\u3002",
    colors: {
      primary: "#132238",
      accent: "#e84a27",
      background: "#eef2f3",
      surface: "#ffffff",
      text: "#17202a"
    },
    typography: {
      fontFamily: "IBM Plex Sans, Inter, PingFang SC, Microsoft YaHei",
      displayWeight: 700,
      bodyWeight: 450
    },
    motion: { easing: "power3.out", entranceSeconds: 0.6, transitionIntensity: 0.8 },
    caption: { position: "lower-left", background: "rgba(255,255,255,.94)", color: "#17202a" },
    surface: {
      radiusPixels: 2,
      shadow: "0 18px 50px rgba(19,34,56,.18)",
      border: "rgba(19,34,56,.22)"
    },
    environment: {
      kind: "grid",
      colors: ["#0f1115", "#2a3140", "#8b9cff"],
      intensity: 0.7,
      grain: 0.18,
      vignette: 0.4,
      lightLeak: false
    },
    recommendedRecipes: ["workflow-flow", "panel-expansion", "feature-callout"],
    avoidRecipes: ["multi-screen-carousel"]
  }
];
var styleById = new Map(SOFTWARE_PROMO_BRAND_STYLES.map((style) => [style.id, style]));
function getBrandStyle(id) {
  return id ? styleById.get(id) : void 0;
}
function assertProjectBrandStyle(project) {
  const id = project.brand?.stylePackId;
  if (id && !styleById.has(id)) throw new Error(`Unknown brand style pack: ${id}.`);
}
function isLightColor(value) {
  const hex = /^#([0-9a-f]{3}|[0-9a-f]{6})$/i.exec(value.trim());
  if (!hex) return false;
  const digits = hex[1].length === 3 ? [...hex[1]].map((c) => c + c).join("") : hex[1];
  const [r, g, b] = [0, 2, 4].map(
    (offset) => Number.parseInt(digits.slice(offset, offset + 2), 16)
  );
  return (0.2126 * r + 0.7152 * g + 0.0722 * b) / 255 > 0.6;
}
function resolveProjectBrandStyle(project) {
  const pack2 = getBrandStyle(project.brand?.stylePackId);
  const primaryColor = project.brand?.primaryColor ?? pack2?.colors.primary ?? "#0f172a";
  const accentColor = project.brand?.accentColor ?? pack2?.colors.accent ?? "#22d3ee";
  const backgroundColor = project.brand?.backgroundColor ?? pack2?.colors.background ?? "transparent";
  const override = project.brand?.environment;
  const packEnvironment = pack2?.environment;
  const environment = packEnvironment ? { ...packEnvironment, ...override ? { kind: override } : {} } : defaultEnvironment(backgroundColor, accentColor, override);
  return {
    pack: pack2,
    primaryColor,
    accentColor,
    backgroundColor,
    fontFamily: project.brand?.fontFamily ?? pack2?.typography.fontFamily ?? "Inter, PingFang SC, Microsoft YaHei",
    environment,
    isLightBackground: isLightColor(
      backgroundColor === "transparent" ? "#000000" : backgroundColor
    )
  };
}

// src/core/cameraMath.ts
var FRAME_MARGIN = 0.94;
var MIN_CAMERA_SCALE = 1;
var MAX_FRAME_SCALE = 2.6;
function coverOverflow(mediaWidth, mediaHeight, canvasWidth, canvasHeight) {
  if (!mediaWidth || !mediaHeight || !canvasWidth || !canvasHeight) return { x: 1, y: 1 };
  const mediaAspect = mediaWidth / mediaHeight;
  const canvasAspect = canvasWidth / canvasHeight;
  if (!Number.isFinite(mediaAspect) || !Number.isFinite(canvasAspect)) return { x: 1, y: 1 };
  return {
    x: Math.max(1, mediaAspect / canvasAspect),
    y: Math.max(1, canvasAspect / mediaAspect)
  };
}
function coverSafeHalfBand(scale, overflow) {
  const effective = scale * overflow;
  return effective <= 1 ? 0 : (effective - 1) / (2 * effective);
}
function clampFocus(value, scale, overflow) {
  const half = coverSafeHalfBand(scale, overflow);
  return Math.min(0.5 + half, Math.max(0.5 - half, value));
}
function resolveCameraKeyframe(keyframe, overflow = { x: 1, y: 1 }) {
  let scale = Number.isFinite(keyframe.scale) && keyframe.scale > 0 ? keyframe.scale : 1;
  let focusX = keyframe.focusX;
  let focusY = keyframe.focusY;
  const frame = keyframe.frame;
  if (frame && frame.width > 0 && frame.height > 0) {
    const fitX = FRAME_MARGIN / (frame.width * overflow.x);
    const fitY = FRAME_MARGIN / (frame.height * overflow.y);
    scale = Math.max(MIN_CAMERA_SCALE, Math.min(MAX_FRAME_SCALE, fitX, fitY));
    focusX = frame.x + frame.width / 2;
    focusY = frame.y + frame.height / 2;
  }
  if (scale < 1) return { ...keyframe, scale, focusX: 0.5, focusY: 0.5 };
  return {
    ...keyframe,
    scale,
    focusX: clampFocus(focusX, scale, overflow.x),
    focusY: clampFocus(focusY, scale, overflow.y)
  };
}
function visibleWindow(keyframe, overflow = { x: 1, y: 1 }) {
  const halfWidth = 0.5 / (keyframe.scale * overflow.x);
  const halfHeight = 0.5 / (keyframe.scale * overflow.y);
  return {
    x: keyframe.focusX - halfWidth,
    y: keyframe.focusY - halfHeight,
    width: halfWidth * 2,
    height: halfHeight * 2
  };
}
function rectInside(inner, outer, tolerance = 5e-3) {
  return inner.x >= outer.x - tolerance && inner.y >= outer.y - tolerance && inner.x + inner.width <= outer.x + outer.width + tolerance && inner.y + inner.height <= outer.y + outer.height + tolerance;
}
function layerVisibleWindow(layer, keyframe, width, height) {
  const crop = layer.crop;
  if (!crop) {
    const overflow = coverOverflow(layer.mediaWidth, layer.mediaHeight, width, height);
    return visibleWindow(resolveCameraKeyframe(keyframe, overflow), overflow);
  }
  const local = {
    ...keyframe,
    focusX: (keyframe.focusX - crop.x) / crop.width,
    focusY: (keyframe.focusY - crop.y) / crop.height,
    ...keyframe.frame ? { frame: { x: (keyframe.frame.x - crop.x) / crop.width, y: (keyframe.frame.y - crop.y) / crop.height, width: keyframe.frame.width / crop.width, height: keyframe.frame.height / crop.height } } : {}
  };
  const window2 = visibleWindow(resolveCameraKeyframe(local));
  return { x: crop.x + window2.x * crop.width, y: crop.y + window2.y * crop.height, width: window2.width * crop.width, height: window2.height * crop.height };
}

// src/core/renderFonts.ts
import fs6 from "node:fs/promises";
import path8 from "node:path";
var nodeRequire = { resolve: (id) => runtimeRequire().resolve(id) };
var BUNDLED_FONTS = [
  {
    family: "Noto Sans SC",
    aliases: [
      "noto sans sc",
      "noto sans sc variable",
      "noto sans cjk sc",
      "source han sans sc",
      "source han sans",
      "\u601D\u6E90\u9ED1\u4F53"
    ],
    packageName: "@fontsource-variable/noto-sans-sc"
  },
  {
    family: "Noto Serif SC",
    aliases: [
      "noto serif sc",
      "noto serif sc variable",
      "noto serif cjk sc",
      "source han serif sc",
      "source han serif",
      "\u601D\u6E90\u5B8B\u4F53"
    ],
    packageName: "@fontsource-variable/noto-serif-sc"
  }
];
var faceCache = /* @__PURE__ */ new Map();
function parseUnicodeRange(value) {
  return value.split(",").map((part) => part.trim().replace(/^U\+/i, "")).filter(Boolean).map((part) => {
    const [start, end] = part.split("-");
    if (start.includes("?")) {
      return [
        Number.parseInt(start.replace(/\?/g, "0"), 16),
        Number.parseInt(start.replace(/\?/g, "f"), 16)
      ];
    }
    const low = Number.parseInt(start, 16);
    return [low, end ? Number.parseInt(end, 16) : low];
  });
}
function parseFontsourceFaces(css) {
  const faces = [];
  for (const block of css.matchAll(/@font-face\s*\{([^}]*)\}/g)) {
    const body2 = block[1] ?? "";
    const file = body2.match(/url\(\.\/files\/([^)]+\.woff2)\)/)?.[1];
    const unicodeRange = body2.match(/unicode-range:\s*([^;]+);/)?.[1]?.trim();
    if (!file || !unicodeRange) continue;
    faces.push({ file, unicodeRange, ranges: parseUnicodeRange(unicodeRange) });
  }
  return faces;
}
function loadFaces(font) {
  let cached = faceCache.get(font.packageName);
  if (!cached) {
    cached = (async () => {
      const cssPath = nodeRequire.resolve(`${font.packageName}/wght.css`);
      return {
        directory: path8.join(path8.dirname(cssPath), "files"),
        faces: parseFontsourceFaces(await fs6.readFile(cssPath, "utf8"))
      };
    })();
    faceCache.set(font.packageName, cached);
  }
  return cached;
}
function normalizeFamily(name) {
  return name.replace(/&quot;|&#0?39;/g, "").replace(/^["']|["']$/g, "").trim().toLowerCase();
}
function requestedFontFamilies(html) {
  const families = /* @__PURE__ */ new Map();
  const declarations = html.replace(/&quot;/g, '"').replace(/&#0?39;/g, "'");
  for (const match of declarations.matchAll(/font-?family"?\s*[:=]\s*([^;}<>\n]+)/gi)) {
    for (const piece of (match[1] ?? "").split(",")) {
      const name = piece.trim().replace(/^["'`]+|["'`)]+$/g, "").trim();
      if (name) families.set(normalizeFamily(name), name);
    }
  }
  return families;
}
function compositionCodePoints(html) {
  const points = /* @__PURE__ */ new Set();
  for (const character of html) points.add(character.codePointAt(0) ?? 0);
  for (const match of html.matchAll(/\\u([0-9a-fA-F]{4})/g))
    points.add(Number.parseInt(match[1] ?? "0", 16));
  return points;
}
function faceCovers(face, points) {
  for (const point of points)
    for (const [start, end] of face.ranges) if (point >= start && point <= end) return true;
  return false;
}
async function prepareBundledFontFaces(html, projectDir) {
  const requested = requestedFontFamilies(html);
  const points = compositionCodePoints(html);
  const rules = [];
  for (const font of BUNDLED_FONTS) {
    const names = [...requested].filter(([normalized]) => font.aliases.includes(normalized));
    if (!names.length) continue;
    const { directory, faces } = await loadFaces(font);
    const needed = faces.filter((face) => faceCovers(face, points));
    const targetDirectory = path8.join(projectDir, "assets", "fonts", path8.basename(font.packageName));
    await fs6.mkdir(targetDirectory, { recursive: true });
    for (const face of needed) {
      const target = path8.join(targetDirectory, face.file);
      await fs6.copyFile(path8.join(directory, face.file), target, fs6.constants.COPYFILE_EXCL).catch(
        (error) => {
          if (error.code !== "EEXIST") throw error;
        }
      );
    }
    for (const [, name] of names)
      for (const face of needed)
        rules.push(
          `@font-face{font-family:${JSON.stringify(name)};font-style:normal;font-display:block;font-weight:100 900;src:url("assets/fonts/${path8.basename(font.packageName)}/${face.file}") format("woff2");unicode-range:${face.unicodeRange}}`
        );
  }
  return rules.join("");
}

// src/core/shotRecipes.ts
var shotcraftReference = (reference) => ({
  project: "video-shotcraft",
  reference,
  license: "Apache-2.0"
});
var hyperFramesReference = (reference) => ({
  project: "HyperFrames",
  reference,
  license: "Apache-2.0"
});
var SOFTWARE_PROMO_SHOT_RECIPES = [
  {
    id: "product-hero-spotlight",
    version: "1.0.0",
    name: "\u805A\u5149\u4EA7\u54C1\u4E3B\u89C6\u89C9",
    description: "\u8BA9\u771F\u5B9E\u4EA7\u54C1\u754C\u9762\u4ECE\u6697\u573A\u4E2D\u805A\u5149\u51FA\u73B0\uFF0C\u9002\u5408\u5EFA\u7ACB\u9AD8\u7EA7\u3001\u53EF\u4FE1\u7684\u7B2C\u4E00\u5370\u8C61\u3002",
    shotRoles: ["hook", "promise"],
    intents: ["\u5EFA\u7ACB\u4EA7\u54C1\u4E3B\u89C6\u89C9", "\u7A81\u51FA\u6838\u5FC3\u4EF7\u503C", "\u9AD8\u7EA7\u5F00\u573A"],
    energy: "medium",
    durationSeconds: { minimum: 2, maximum: 6 },
    requiredVisualLayers: { minimum: 1, maximum: 1 },
    parameters: [
      {
        name: "intensity",
        type: "number",
        description: "\u805A\u5149\u548C\u60AC\u6D6E\u52A8\u6548\u5F3A\u5EA6\u3002",
        minimum: 0.4,
        maximum: 1.4,
        default: 1
      }
    ],
    soundCues: ["\u754C\u9762\u7A33\u5B9A\u843D\u4F4D\u65F6\u4F7F\u7528\u77ED\u4FC3\u3001\u4F4E\u9891\u7684\u54C1\u724C\u51B2\u51FB\u97F3\u3002"],
    knownFailures: ["\u754C\u9762\u672C\u8EAB\u8FC7\u6697\u65F6\u805A\u5149\u5C42\u4F1A\u964D\u4F4E\u53EF\u8BFB\u6027\u3002", "\u4E0D\u9002\u5408\u540C\u65F6\u5C55\u793A\u591A\u4E2A\u7A97\u53E3\u3002"],
    fallbackRecipeIds: ["browser-fly-in"],
    sourceReferences: [shotcraftReference("spotlight-hero-card")]
  },
  {
    id: "browser-fly-in",
    version: "1.0.0",
    name: "\u6D4F\u89C8\u5668\u7A97\u53E3\u98DE\u5165",
    description: "\u628A\u4EA7\u54C1\u754C\u9762\u88C5\u8FDB\u6D4F\u89C8\u5668\u821E\u53F0\uFF08\u6E10\u53D8\u80CC\u666F\u3001\u7A97\u53E3\u8FB9\u6846\u3001\u9634\u5F71\uFF09\uFF0C\u5E26\u900F\u89C6\u4ECE\u4E0B\u65B9\u98DE\u5165\u843D\u4F4D\u5E76\u4FDD\u6301\u8F7B\u5FAE\u60AC\u6D6E\u3002\u6CA1\u6709\u663E\u5F0F stage \u65F6\u81EA\u52A8\u5957\u7528 browser stage\u3002",
    shotRoles: ["hook", "feature", "promise"],
    intents: ["\u4EA7\u54C1\u767B\u573A", "\u8FDB\u5165\u6F14\u793A", "\u5F3A\u8C03\u7F51\u9875\u4EA7\u54C1"],
    energy: "high",
    durationSeconds: { minimum: 1.2, maximum: 4 },
    requiredVisualLayers: { minimum: 1, maximum: 1 },
    parameters: [
      {
        name: "intensity",
        type: "number",
        description: "\u98DE\u5165\u4F4D\u79FB\u548C\u900F\u89C6\u5F3A\u5EA6\u3002",
        minimum: 0.4,
        maximum: 1.5,
        default: 1
      }
    ],
    soundCues: ["\u7A97\u53E3\u843D\u4F4D\u5E27\u4F7F\u7528\u8F7B\u91CF whoosh \u548C click\u3002"],
    knownFailures: [
      "\u8F93\u5165\u7D20\u6750\u5DF2\u7ECF\u5E26\u5927\u9762\u79EF\u900F\u89C6\u6216\u65CB\u8F6C\u65F6\u4F1A\u663E\u5F97\u4E0D\u7A33\u5B9A\u3002",
      "scene.stage.kind \u8BBE\u4E3A none \u65F6\u53EA\u5269\u4F4D\u79FB\uFF0C\u5931\u53BB\u821E\u53F0\u611F\u3002"
    ],
    fallbackRecipeIds: ["ui-focus-zoom"],
    sourceReferences: [hyperFramesReference("browser-device-stage")]
  },
  {
    id: "ui-focus-zoom",
    version: "1.0.0",
    name: "UI \u805A\u7126\u63A8\u8FDB",
    description: "\u5728\u771F\u5B9E\u5F55\u5C4F\u4E0A\u5E73\u6ED1\u63A8\u8FDB\u5230\u5173\u952E\u529F\u80FD\u533A\u57DF\uFF0C\u5F3A\u5316\u64CD\u4F5C\u8BC1\u636E\u3002",
    shotRoles: ["feature", "evidence", "process"],
    intents: ["\u805A\u7126\u529F\u80FD", "\u7A81\u51FA\u70B9\u51FB\u76EE\u6807", "\u5C55\u793A\u771F\u5B9E\u64CD\u4F5C"],
    energy: "medium",
    durationSeconds: { minimum: 2, maximum: 8 },
    requiredVisualLayers: { minimum: 1, maximum: 1 },
    parameters: [
      {
        name: "scale",
        type: "number",
        description: "\u6CA1\u6709\u663E\u5F0F cameraMotion \u65F6\u4F7F\u7528\u7684\u76EE\u6807\u7F29\u653E\u3002",
        minimum: 1,
        maximum: 2.4,
        default: 1.35
      }
    ],
    soundCues: ["\u63A8\u8FDB\u5F00\u59CB\u53EF\u4F7F\u7528\u6781\u8F7B\u7684\u4E0A\u5347\u97F3\uFF0C\u70B9\u51FB\u4ECD\u4EE5\u771F\u5B9E\u4EA4\u4E92\u8282\u594F\u4E3A\u51C6\u3002"],
    knownFailures: ["\u6CA1\u6709\u76EE\u6807\u533A\u57DF\u6216\u5F55\u5C4F\u5206\u8FA8\u7387\u4E0D\u8DB3\u65F6\u4E0D\u5E94\u653E\u5927\u3002"],
    fallbackRecipeIds: ["feature-callout"],
    sourceReferences: [hyperFramesReference("ui-focus-zoom")]
  },
  {
    id: "feature-callout",
    version: "1.0.0",
    name: "\u529F\u80FD\u533A\u57DF\u6807\u6CE8",
    description: "\u7528\u63CF\u8FB9\u3001\u67D4\u5149\u548C\u6307\u793A\u70B9\u6807\u51FA\u754C\u9762\u4E2D\u7684\u6838\u5FC3\u533A\u57DF\u3002",
    shotRoles: ["feature", "evidence", "process"],
    intents: ["\u89E3\u91CA\u754C\u9762", "\u6807\u51FA\u529F\u80FD", "\u964D\u4F4E\u7406\u89E3\u6210\u672C"],
    energy: "low",
    durationSeconds: { minimum: 2, maximum: 8 },
    requiredVisualLayers: { minimum: 1, maximum: 1 },
    parameters: [
      {
        name: "x",
        type: "number",
        description: "\u6807\u6CE8\u6846\u5DE6\u4FA7\u5F52\u4E00\u5316\u5750\u6807\u3002",
        minimum: 0,
        maximum: 1,
        default: 0.58
      },
      {
        name: "y",
        type: "number",
        description: "\u6807\u6CE8\u6846\u9876\u90E8\u5F52\u4E00\u5316\u5750\u6807\u3002",
        minimum: 0,
        maximum: 1,
        default: 0.24
      },
      {
        name: "width",
        type: "number",
        description: "\u6807\u6CE8\u6846\u5F52\u4E00\u5316\u5BBD\u5EA6\u3002",
        minimum: 0.05,
        maximum: 1,
        default: 0.28
      },
      {
        name: "height",
        type: "number",
        description: "\u6807\u6CE8\u6846\u5F52\u4E00\u5316\u9AD8\u5EA6\u3002",
        minimum: 0.05,
        maximum: 1,
        default: 0.28
      }
    ],
    soundCues: ["\u6807\u6CE8\u6846\u51FA\u73B0\u65F6\u4F7F\u7528\u514B\u5236\u7684 UI tick\u3002"],
    knownFailures: ["\u9ED8\u8BA4\u5750\u6807\u4E0D\u662F\u4E8B\u5B9E\u76EE\u6807\uFF1BAgent \u5FC5\u987B\u6839\u636E\u771F\u5B9E\u753B\u9762\u586B\u5199\u53C2\u6570\u3002"],
    fallbackRecipeIds: ["ui-focus-zoom"],
    sourceReferences: [shotcraftReference("feature-callout patterns")]
  },
  {
    id: "step-process-rail",
    version: "1.0.0",
    name: "\u6B65\u9AA4\u8FDB\u5EA6\u8F68",
    description: "\u5728\u771F\u5B9E\u6F14\u793A\u65C1\u5EFA\u7ACB\u6B65\u9AA4\u8282\u594F\u548C\u8FDB\u5EA6\u611F\u3002",
    shotRoles: ["process", "feature"],
    intents: ["\u89E3\u91CA\u6D41\u7A0B", "\u4E09\u6B65\u6F14\u793A", "\u5EFA\u7ACB\u8FDB\u5EA6"],
    energy: "medium",
    durationSeconds: { minimum: 4, maximum: 14 },
    requiredVisualLayers: { minimum: 1 },
    parameters: [],
    soundCues: ["\u6BCF\u4E00\u6B65\u5207\u6362\u53EF\u4F7F\u7528\u540C\u4E00\u97F3\u8272\u3001\u9010\u6B65\u5347\u9AD8\u7684 UI tick\u3002"],
    knownFailures: ["\u6CA1\u6709\u6B65\u9AA4\u578B\u56FE\u5F62\u6216\u6587\u6848\u65F6\u53EA\u4F1A\u4EA7\u751F\u8F7B\u91CF\u821E\u53F0\u52A8\u6548\u3002"],
    fallbackRecipeIds: ["feature-callout"],
    sourceReferences: [shotcraftReference("three-step-process-rail")]
  },
  {
    id: "before-after-split",
    version: "1.0.0",
    name: "\u524D\u540E\u5BF9\u6BD4\u5206\u5C4F",
    description: "\u5E76\u7F6E\u65E7\u65B9\u6848\u4E0E\u4EA7\u54C1\u7ED3\u679C\uFF0C\u4F7F\u7528\u79FB\u52A8\u5206\u5272\u7EBF\u63ED\u793A\u5DEE\u5F02\u3002",
    shotRoles: ["problem", "evidence", "result"],
    intents: ["\u524D\u540E\u5BF9\u6BD4", "\u8BC1\u660E\u6539\u5584", "\u5C55\u793A\u7ED3\u679C"],
    energy: "high",
    durationSeconds: { minimum: 3, maximum: 8 },
    requiredVisualLayers: { minimum: 2, maximum: 2 },
    parameters: [],
    soundCues: ["\u5206\u5272\u7EBF\u8D8A\u8FC7\u4E2D\u70B9\u65F6\u4F7F\u7528\u4E00\u6B21\u660E\u786E\u7684\u63ED\u793A\u97F3\u3002"],
    knownFailures: ["\u4E24\u5C42\u7D20\u6750\u4E0D\u662F\u540C\u4E00\u5BF9\u8C61\u6216\u6784\u56FE\u5DEE\u5F02\u8FC7\u5927\u65F6\uFF0C\u5BF9\u6BD4\u5173\u7CFB\u4F1A\u5931\u6548\u3002"],
    fallbackRecipeIds: ["panel-expansion"],
    sourceReferences: [shotcraftReference("before-after-slider")]
  },
  {
    id: "multi-screen-carousel",
    version: "1.0.0",
    name: "\u591A\u9875\u9762\u529F\u80FD\u8F6E\u64AD",
    description: "\u628A\u591A\u4E2A\u771F\u5B9E\u4EA7\u54C1\u9875\u9762\u7EC4\u7EC7\u6210\u6709\u5C42\u7EA7\u7684\u5FEB\u901F\u529F\u80FD\u8499\u592A\u5947\u3002",
    shotRoles: ["hook", "feature", "evidence"],
    intents: ["\u5FEB\u901F\u5C55\u793A\u529F\u80FD\u9762", "\u4EA7\u54C1\u8499\u592A\u5947", "\u591A\u9875\u9762\u6982\u89C8"],
    energy: "high",
    durationSeconds: { minimum: 3, maximum: 9 },
    requiredVisualLayers: { minimum: 2, maximum: 5 },
    parameters: [],
    soundCues: ["\u9875\u9762\u5207\u6362\u4F7F\u7528\u7EDF\u4E00\u7684\u77ED whoosh\uFF0C\u6700\u540E\u4E00\u9875\u843D\u4F4D\u4F7F\u7528\u66F4\u91CD\u7684 hit\u3002"],
    knownFailures: ["\u9875\u9762\u6570\u91CF\u8FC7\u591A\u6216\u6587\u5B57\u8FC7\u5C0F\u4F1A\u53D8\u6210\u65E0\u6CD5\u9605\u8BFB\u7684\u7F29\u7565\u56FE\u5899\u3002"],
    fallbackRecipeIds: ["browser-fly-in"],
    sourceReferences: [hyperFramesReference("screen-flow-carousel")]
  },
  {
    id: "metric-proof",
    version: "1.0.0",
    name: "\u6307\u6807\u8BC1\u660E\u955C\u5934",
    description: "\u8BA9\u6570\u636E\u3001\u65F6\u95F4\u8282\u7701\u6216\u6027\u80FD\u6307\u6807\u4EE5\u53EF\u8BFB\u7684\u8282\u594F\u8FDB\u5165\u3002",
    shotRoles: ["evidence", "result"],
    intents: ["\u6570\u636E\u8BC1\u660E", "\u5C55\u793A\u7ED3\u679C", "\u5F3A\u5316\u53EF\u4FE1\u5EA6"],
    energy: "medium",
    durationSeconds: { minimum: 2.5, maximum: 7 },
    requiredVisualLayers: { minimum: 1 },
    parameters: [],
    soundCues: ["\u6570\u5B57\u7A33\u5B9A\u5728\u6700\u7EC8\u503C\u65F6\u4F7F\u7528\u4E00\u6B21\u6E05\u6670\u7684\u786E\u8BA4\u97F3\u3002"],
    knownFailures: ["\u6307\u6807\u6CA1\u6709\u771F\u5B9E\u4F9D\u636E\u6216\u7F3A\u5C11\u5355\u4F4D\u65F6\u7981\u6B62\u4F7F\u7528\u3002"],
    fallbackRecipeIds: ["feature-callout"],
    sourceReferences: [shotcraftReference("data and result cards")]
  },
  {
    id: "panel-expansion",
    version: "1.0.0",
    name: "\u9762\u677F\u6269\u5C55",
    description: "\u8BA9\u5C40\u90E8\u529F\u80FD\u9762\u677F\u4ECE\u754C\u9762\u4E2D\u6269\u5C55\u5230\u4E3B\u821E\u53F0\uFF0C\u518D\u56DE\u5230\u4EA7\u54C1\u4E0A\u4E0B\u6587\u3002",
    shotRoles: ["feature", "evidence"],
    intents: ["\u89E3\u91CA\u590D\u6742\u9762\u677F", "\u4ECE\u5C40\u90E8\u5230\u6574\u4F53", "\u5F3A\u8C03\u7ED3\u679C"],
    energy: "medium",
    durationSeconds: { minimum: 2, maximum: 7 },
    requiredVisualLayers: { minimum: 1 },
    parameters: [],
    soundCues: ["\u6269\u5C55\u548C\u56DE\u843D\u4F7F\u7528\u6210\u5BF9\u7684\u5347\u964D\u97F3\u3002"],
    knownFailures: ["\u6CA1\u6709\u660E\u786E\u5C40\u90E8\u4E3B\u4F53\u65F6\u4F1A\u9000\u5316\u4E3A\u666E\u901A\u7F29\u653E\u3002"],
    fallbackRecipeIds: ["ui-focus-zoom"],
    sourceReferences: [shotcraftReference("panel expansion and panel match cut")]
  },
  {
    id: "problem-pressure",
    version: "1.0.0",
    name: "\u75DB\u70B9\u538B\u529B\u955C\u5934",
    description: "\u7528\u8F7B\u5FAE\u9519\u4F4D\u3001\u62E5\u6324\u548C\u6697\u89D2\u8868\u8FBE\u65E7\u6D41\u7A0B\u7684\u6469\u64E6\uFF0C\u4F46\u4E0D\u7834\u574F\u4E8B\u5B9E\u753B\u9762\u3002",
    shotRoles: ["problem", "hook"],
    intents: ["\u5EFA\u7ACB\u75DB\u70B9", "\u8868\u8FBE\u4F4E\u6548", "\u5236\u9020\u5BF9\u6BD4\u8D77\u70B9"],
    energy: "high",
    durationSeconds: { minimum: 1.5, maximum: 5 },
    requiredVisualLayers: { minimum: 1 },
    parameters: [
      {
        name: "intensity",
        type: "number",
        description: "\u538B\u529B\u52A8\u6548\u5F3A\u5EA6\u3002",
        minimum: 0.2,
        maximum: 1,
        default: 0.55
      }
    ],
    soundCues: ["\u4F7F\u7528\u514B\u5236\u7684\u673A\u68B0\u566A\u58F0\u6216\u4F4E\u9891\u8109\u51B2\uFF0C\u4EA7\u54C1\u51FA\u73B0\u540E\u7ACB\u5373\u91CA\u653E\u3002"],
    knownFailures: ["\u6301\u7EED\u65F6\u95F4\u8FC7\u957F\u4F1A\u8BA9\u7528\u6237\u8BEF\u4EE5\u4E3A\u4EA7\u54C1\u672C\u8EAB\u4E0D\u7A33\u5B9A\u3002"],
    fallbackRecipeIds: ["feature-callout"],
    sourceReferences: [shotcraftReference("problem setup patterns")]
  },
  {
    id: "workflow-flow",
    version: "1.0.0",
    name: "\u81EA\u52A8\u5316\u6D41\u7A0B\u5C55\u793A",
    description: "\u7528\u56FE\u5F62\u548C\u4EA7\u54C1\u9875\u9762\u7684\u987A\u5E8F\u8FDB\u5165\u89E3\u91CA\u8F93\u5165\u3001\u5904\u7406\u4E0E\u8F93\u51FA\u3002",
    shotRoles: ["process", "promise", "evidence"],
    intents: ["\u89E3\u91CA\u81EA\u52A8\u5316", "\u5C55\u793A\u6570\u636E\u6D41", "\u5EFA\u7ACB\u7CFB\u7EDF\u7406\u89E3"],
    energy: "medium",
    durationSeconds: { minimum: 4, maximum: 12 },
    requiredVisualLayers: { minimum: 1, maximum: 4 },
    parameters: [],
    soundCues: ["\u8282\u70B9\u6FC0\u6D3B\u6309\u6D41\u7A0B\u987A\u5E8F\u4F7F\u7528\u76F8\u540C\u97F3\u8272\u3002"],
    knownFailures: ["\u6CA1\u6709\u56FE\u5F62\u5C42\u6216\u6B65\u9AA4\u6587\u672C\u65F6\uFF0C\u6D41\u7A0B\u5173\u7CFB\u4E0D\u4F1A\u81EA\u52A8\u4EA7\u751F\u3002"],
    fallbackRecipeIds: ["step-process-rail"],
    sourceReferences: [shotcraftReference("workflow diagram patterns")]
  },
  {
    id: "brand-close",
    version: "1.0.0",
    name: "\u54C1\u724C\u6536\u5C3E",
    description: "\u54C1\u724C\u6536\u5C3E\uFF1A\u4EA7\u54C1\u753B\u9762\u843D\u4F4D\u540E\uFF0Cgraphics\uFF08Logo\u3001\u6807\u8BED\u3001CTA\uFF09\u4F9D\u6B21\u6C47\u805A\u843D\u4F4D\uFF0C\u5E76\u5728\u7ED3\u5C3E\u9759\u6B62\u81F3\u5C11 1 \u79D2\u4F9B\u8BB0\u5FC6\u3002",
    shotRoles: ["cta", "result"],
    intents: ["\u54C1\u724C\u6536\u5C3E", "\u884C\u52A8\u53F7\u53EC", "\u7559\u4E0B\u4EA7\u54C1\u8BB0\u5FC6"],
    energy: "low",
    durationSeconds: { minimum: 2, maximum: 6 },
    requiredVisualLayers: { minimum: 1, maximum: 2 },
    parameters: [],
    soundCues: ["Logo \u5B8C\u5168\u843D\u4F4D\u65F6\u4F7F\u7528\u54C1\u724C\u7B7E\u540D\u97F3\uFF0C\u7ED3\u5C3E\u4FDD\u7559\u77ED\u6682\u547C\u5438\u3002"],
    knownFailures: ["CTA \u548C Logo \u540C\u65F6\u8FC7\u591A\u4F1A\u524A\u5F31\u89C6\u89C9\u4E2D\u5FC3\u3002"],
    fallbackRecipeIds: ["product-hero-spotlight"],
    sourceReferences: [shotcraftReference("logo-brand-close")]
  },
  {
    id: "title-blur-slide",
    version: "1.0.0",
    name: "\u6807\u9898\u6A21\u7CCA\u6ED1\u5165",
    description: "\u628A\u573A\u666F graphics \u4E2D\u7684\u6807\u9898\u6309\u8BCD\uFF08\u897F\u6587\uFF09\u6216\u6309\u5B57\uFF08\u4E2D\u6587\uFF09\u5206\u6279\u4ECE\u6A21\u7CCA\u4E0E\u4F4D\u79FB\u4E2D\u5347\u8D77\uFF0C\u5F62\u6210\u6709\u5C42\u6B21\u7684\u5F00\u573A\u6216\u4EF7\u503C\u9648\u8FF0\u6392\u7248\u3002",
    shotRoles: ["hook", "promise", "breather", "cta"],
    intents: ["\u6807\u9898\u5165\u573A", "\u4EF7\u503C\u9648\u8FF0", "\u5F00\u573A\u6392\u7248", "\u7AE0\u8282\u6807\u9898"],
    energy: "medium",
    durationSeconds: { minimum: 1.5, maximum: 6 },
    requiredVisualLayers: { minimum: 1 },
    parameters: [
      {
        name: "stagger",
        type: "number",
        description: "\u76F8\u90BB\u8BCD/\u5B57\u4E4B\u95F4\u7684\u5165\u573A\u95F4\u9694\uFF08\u79D2\uFF09\u3002",
        minimum: 0.03,
        maximum: 0.14,
        default: 0.06
      },
      {
        name: "rise",
        type: "number",
        description: "\u5165\u573A\u4F4D\u79FB\u50CF\u7D20\u3002",
        minimum: 16,
        maximum: 80,
        default: 40
      }
    ],
    soundCues: ["\u6BCF\u6279\u6587\u5B57\u843D\u4F4D\u53EF\u914D\u6781\u8F7B\u7684 text tick\uFF0C\u6574\u53E5\u5B8C\u6210\u540E\u7559 0.5 \u79D2\u9759\u6B62\u3002"],
    knownFailures: ["\u6807\u9898\u8D85\u8FC7\u4E24\u884C\u6216\u5B57\u53F7\u8FC7\u5C0F\u65F6\u5206\u8BCD\u5165\u573A\u4F1A\u663E\u5F97\u51CC\u4E71\u3002"],
    fallbackRecipeIds: ["product-hero-spotlight"],
    sourceReferences: [shotcraftReference("blur-slide")]
  },
  {
    id: "marker-underline",
    version: "1.0.0",
    name: "\u5173\u952E\u8BCD\u9A6C\u514B\u7B14\u4E0B\u5212\u7EBF",
    description: "\u5728\u573A\u666F\u7B2C\u4E00\u6761 graphic \u7684\u6587\u5B57\u4E0B\u65B9\u7ED8\u5236\u4E00\u6761\u9A6C\u514B\u7B14\u8D28\u611F\u7684\u5F3A\u8C03\u4E0B\u5212\u7EBF\u3002",
    shotRoles: ["feature", "promise", "result", "evidence"],
    intents: ["\u5F3A\u8C03\u5173\u952E\u8BCD", "\u7ED3\u679C\u5F3A\u8C03", "\u4EF7\u503C\u70B9\u5F3A\u8C03"],
    energy: "low",
    durationSeconds: { minimum: 1.5, maximum: 8 },
    requiredVisualLayers: { minimum: 1 },
    parameters: [
      {
        name: "thickness",
        type: "number",
        description: "\u4E0B\u5212\u7EBF\u7C97\u7EC6\u50CF\u7D20\u3002",
        minimum: 6,
        maximum: 18,
        default: 10
      },
      {
        name: "delay",
        type: "number",
        description: "\u4ECE\u573A\u666F\u5F00\u59CB\u5230\u4E0B\u5212\u7EBF\u5F00\u59CB\u7ED8\u5236\u7684\u5EF6\u8FDF\uFF08\u79D2\uFF09\u3002",
        minimum: 0,
        maximum: 2,
        default: 0.35
      }
    ],
    soundCues: ["\u4E0B\u5212\u7EBF\u7ED8\u5236\u8D77\u70B9\u53EF\u914D\u4E00\u58F0\u77ED\u4FC3 marker swipe\u3002"],
    knownFailures: ["graphic \u6587\u672C\u5F88\u77ED\u4E14\u5C45\u4E2D\u65F6\u4E0B\u5212\u7EBF\u4F1A\u663E\u5F97\u8FC7\u77ED\u3002"],
    fallbackRecipeIds: ["feature-callout"],
    sourceReferences: [shotcraftReference("marker-underline-title")]
  },
  {
    id: "crash-zoom-punch",
    version: "1.0.0",
    name: "\u6025\u63A8\u51B2\u51FB",
    description: "\u5728\u4E00\u4E2A\u8282\u62CD\u5185\u4ECE\u5168\u666F\u6025\u63A8\u5230\u76EE\u6807\u533A\u57DF\uFF1A\u22651 \u79D2\u9884\u7559 \u2192 6-8 \u5E27\u6025\u63A8\u5230 2.4 \u500D \u2192 \u843D\u4F4D\u56DE\u5F39\u6216\u9501\u5B9A\u6296\u52A8 \u2192 \u22651.5 \u79D2\u505C\u7559\u9605\u8BFB\u3002\u7528\u4E8E\u628A\u6CE8\u610F\u529B\u9489\u5728\u4E00\u4E2A\u6A21\u5757\u4E0A\u3002",
    shotRoles: ["feature", "evidence", "result"],
    intents: ["\u5F3A\u8C03\u5355\u4E2A\u6A21\u5757", "\u6025\u63A8", "\u51B2\u51FB\u843D\u70B9", "\u5173\u952E\u7ED3\u679C"],
    energy: "high",
    durationSeconds: { minimum: 2.5, maximum: 8 },
    requiredVisualLayers: { minimum: 1, maximum: 1 },
    parameters: [
      {
        name: "focusX",
        type: "number",
        description: "\u76EE\u6807\u4E2D\u5FC3 X\uFF080-1\uFF09\u3002",
        minimum: 0,
        maximum: 1,
        default: 0.5
      },
      {
        name: "focusY",
        type: "number",
        description: "\u76EE\u6807\u4E2D\u5FC3 Y\uFF080-1\uFF09\u3002",
        minimum: 0,
        maximum: 1,
        default: 0.5
      },
      {
        name: "scale",
        type: "number",
        description: "\u843D\u4F4D\u500D\u7387\uFF0C\u76EE\u6807\u5E94\u5360\u753B\u9762 60-75%\u3002",
        minimum: 1.6,
        maximum: 2.8,
        default: 2.4
      },
      {
        name: "holdBefore",
        type: "number",
        description: "\u6025\u63A8\u524D\u7684\u5168\u666F\u505C\u7559\u79D2\u6570\u3002",
        minimum: 0.6,
        maximum: 3,
        default: 1
      },
      {
        name: "variant",
        type: "string",
        description: "rebound\uFF08\u56DE\u5F39 3-6%\uFF09\u6216 impact\uFF08\u9501\u5B9A\u52A0\u8870\u51CF\u6296\u52A8\uFF09\u3002",
        default: "rebound"
      }
    ],
    soundCues: ["\u6025\u63A8\u8D77\u70B9\u9489 sfx-whoosh-fast\uFF0C\u843D\u4F4D\u5E27\u9489 sfx-impact-low\uFF1B\u4E0D\u8981\u4E24\u8005\u90FD\u62C9\u957F\u3002"],
    knownFailures: [
      "\u76EE\u6807\u533A\u57DF\u5206\u8FA8\u7387\u4E0D\u8DB3\u65F6\u653E\u5927\u540E\u7CCA\uFF1B\u5168\u7247\u8D85\u8FC7 2 \u6B21\u6025\u63A8\u4F1A\u5931\u53BB\u51B2\u51FB\u3002",
      "\u6025\u63A8\u8D85\u8FC7 10 \u5E27\u5C31\u53D8\u6210\u666E\u901A\u63A8\u955C\u3002"
    ],
    fallbackRecipeIds: ["ui-focus-zoom"],
    sourceReferences: [shotcraftReference("crash-zoom-punch")]
  },
  {
    id: "click-zoom-punch",
    version: "1.0.0",
    name: "\u70B9\u51FB\u5373\u63A8\u8FD1",
    description: "\u8BFB\u53D6\u8BE5\u89C6\u89C9\u5C42\u7684\u5F55\u5236\u5149\u6807\u70B9\u51FB\u6837\u672C\uFF0C\u5728\u6BCF\u6B21\u771F\u5B9E\u70B9\u51FB\u7684\u77AC\u95F4\u5411\u70B9\u51FB\u4F4D\u7F6E\u5FEB\u901F\u63A8\u8FD1\uFF080.25 \u79D2\uFF09\uFF0C\u505C\u7559\u540E\u56DE\u5230\u5168\u666F\u3002\u8BA9\u89C2\u4F17\u8DDF\u7740\u771F\u5B9E\u64CD\u4F5C\u8D70\u3002",
    shotRoles: ["feature", "evidence", "process"],
    intents: ["\u8DDF\u968F\u70B9\u51FB", "\u771F\u5B9E\u64CD\u4F5C\u5F3A\u8C03", "\u64CD\u4F5C\u8BC1\u636E"],
    energy: "medium",
    durationSeconds: { minimum: 2, maximum: 12 },
    requiredVisualLayers: { minimum: 1, maximum: 1 },
    parameters: [
      {
        name: "scale",
        type: "number",
        description: "\u70B9\u51FB\u65F6\u7684\u63A8\u8FD1\u500D\u7387\u3002",
        minimum: 1.15,
        maximum: 1.8,
        default: 1.35
      },
      {
        name: "hold",
        type: "number",
        description: "\u63A8\u8FD1\u540E\u505C\u7559\u79D2\u6570\u3002",
        minimum: 0.5,
        maximum: 2.5,
        default: 1
      },
      {
        name: "maxPunches",
        type: "number",
        description: "\u4E00\u4E2A\u955C\u5934\u5185\u6700\u591A\u54CD\u5E94\u51E0\u6B21\u70B9\u51FB\u3002",
        minimum: 1,
        maximum: 3,
        default: 2
      }
    ],
    soundCues: ["\u6BCF\u6B21\u63A8\u8FD1\u9489 sfx-ui-click\uFF1B\u4E0D\u518D\u989D\u5916\u52A0 whoosh\u3002"],
    knownFailures: [
      "\u89C6\u89C9\u5C42\u6CA1\u6709 cursorOverlay \u6837\u672C\u6216\u6CA1\u6709\u70B9\u51FB\u4E8B\u4EF6\u65F6\u4E0D\u4EA7\u751F\u4EFB\u4F55\u8FD0\u52A8\u3002",
      "\u70B9\u51FB\u95F4\u9694\u5C0F\u4E8E 1.2 \u79D2\u65F6\u4F1A\u8DF3\u8FC7\u540E\u7EED\u70B9\u51FB\u3002"
    ],
    fallbackRecipeIds: ["ui-focus-zoom"],
    sourceReferences: [
      shotcraftReference("cursor-flyover"),
      shotcraftReference("crash-zoom-punch")
    ]
  },
  {
    id: "pressure-push",
    version: "1.0.0",
    name: "\u52A0\u901F\u538B\u8FEB\u63A8\u8FDB",
    description: "\u6574\u6BB5\u4EE5\u4E8C\u6B21\u52A0\u901F\u66F2\u7EBF\u7F13\u6162\u63A8\u8FD1\uFF081.00\u21921.14\uFF09\uFF0C\u6697\u89D2\u540C\u6B65\u52A0\u6DF1\uFF0C\u7528\u5728\u91CD\u8981\u7ED3\u8BBA\u6216\u5927\u6570\u5B57\u63ED\u793A\u4E4B\u524D\uFF0C\u7ED3\u5C3E\u76F4\u63A5\u786C\u5207\u8FDB\u9AD8\u5BF9\u6BD4\u7684\u4E0B\u4E00\u573A\u3002",
    shotRoles: ["problem", "promise", "result"],
    intents: ["\u79EF\u7D2F\u5F20\u529B", "\u63ED\u793A\u524D\u94FA\u57AB", "\u95EE\u9898\u538B\u8FEB"],
    energy: "medium",
    durationSeconds: { minimum: 2.5, maximum: 6 },
    requiredVisualLayers: { minimum: 1, maximum: 1 },
    parameters: [
      {
        name: "scale",
        type: "number",
        description: "\u7ED3\u675F\u65F6\u7684\u500D\u7387\u3002",
        minimum: 1.06,
        maximum: 1.25,
        default: 1.14
      },
      {
        name: "vignette",
        type: "number",
        description: "\u7ED3\u675F\u65F6\u7684\u6697\u89D2\u5F3A\u5EA6\u3002",
        minimum: 0,
        maximum: 0.8,
        default: 0.5
      }
    ],
    soundCues: ["\u63A8\u8FDB\u4E2D\u4E0D\u94FA\u6301\u7EED\u97F3\uFF0C\u5207\u70B9\u9489\u4E00\u4E2A sfx-impact-low\uFF0C\u5207\u70B9\u540E\u4E0D\u7559\u5C3E\u5DF4\u3002"],
    knownFailures: ["\u5300\u901F\u63A8\u8FDB\u8BFB\u4F5C\u666E\u901A\u8FD0\u955C\uFF0C\u52A0\u901F\u66F2\u7EBF\u624D\u662F\u5173\u952E\uFF1B\u540E\u9762\u63A5\u6DE1\u5165\u6DE1\u51FA\u4F1A\u6CC4\u6389\u5F20\u529B\u3002"],
    fallbackRecipeIds: ["ui-focus-zoom"],
    sourceReferences: [shotcraftReference("tension-camera-moves")]
  },
  {
    id: "dutch-roll-level",
    version: "1.0.0",
    name: "\u503E\u659C\u56DE\u6B63",
    description: "\u95EE\u9898\u6BB5\u4EE5 -10\xB0 \u503E\u659C\u52A0\u7F13\u6162\u6F02\u79FB\u5448\u73B0\u4E0D\u5B89\uFF0C\u5728 correctAt \u5904 14 \u5E27\u56DE\u6B63\u5E76\u8F7B\u5FAE\u8FC7\u51B2\u5230 +1.2\xB0\uFF0C\u500D\u7387 1.15\u21921.08\uFF0C\u8BED\u4E49\u662F\u201C\u4ECE\u95EE\u9898\u5230\u88AB\u7EA0\u6B63\u201D\u3002",
    shotRoles: ["problem", "promise"],
    intents: ["\u95EE\u9898\u5230\u89E3\u51B3", "\u7EA0\u6B63", "\u4E0D\u5B89\u5230\u7A33\u5B9A"],
    energy: "medium",
    durationSeconds: { minimum: 2.5, maximum: 7 },
    requiredVisualLayers: { minimum: 1, maximum: 1 },
    parameters: [
      {
        name: "tilt",
        type: "number",
        description: "\u95EE\u9898\u6BB5\u503E\u659C\u89D2\u5EA6\uFF08\u5EA6\uFF09\u3002",
        minimum: 4,
        maximum: 14,
        default: 10
      },
      {
        name: "correctAt",
        type: "number",
        description: "\u56DE\u6B63\u53D1\u751F\u5728\u573A\u666F\u65F6\u957F\u7684\u6BD4\u4F8B\u4F4D\u7F6E\u3002",
        minimum: 0.3,
        maximum: 0.85,
        default: 0.55
      }
    ],
    soundCues: ["\u56DE\u6B63\u5E27\u9489 sfx-mech-lock \u6216 sfx-impact-low\uFF08\u4E8C\u9009\u4E00\uFF09\u3002"],
    knownFailures: ["\u7EAF\u9759\u6001\u503E\u659C\u8BFB\u4F5C\u6784\u56FE\u9519\u8BEF\uFF0C\u6F02\u79FB\u662F\u5FC5\u9700\u7684\uFF1B\u4E0D\u80FD\u548C\u5176\u4ED6\u76F8\u673A\u914D\u65B9\u53E0\u52A0\u3002"],
    fallbackRecipeIds: ["problem-pressure"],
    sourceReferences: [shotcraftReference("tension-camera-moves")]
  },
  {
    id: "pull-back-isolation",
    version: "1.0.0",
    name: "\u62C9\u8FDC\u5B64\u7ACB",
    description: "\u4ECE 2.2 \u500D\u8FD1\u666F\u4EE5\u4E09\u6B21\u7F13\u51FA\u62C9\u56DE\uFF0C\u821E\u53F0\u5916\u6846\u7F29\u5C0F\u5230 0.62 \u500D\uFF0C\u80CC\u666F\u540C\u6B65\u538B\u6697\u5E76\u7ED9\u5916\u6846\u4E00\u5708\u5149\u6655\uFF0C\u4F5C\u4E3A\u7AE0\u8282\u6216\u5168\u7247\u7684\u6536\u675F\u955C\u5934\u3002",
    shotRoles: ["result", "cta", "breather"],
    intents: ["\u6536\u675F", "\u5B64\u7ACB\u4E3B\u4F53", "\u7ED3\u5C3E\u524D\u7684\u6C89\u9759"],
    energy: "low",
    durationSeconds: { minimum: 3, maximum: 7 },
    requiredVisualLayers: { minimum: 1, maximum: 1 },
    parameters: [
      {
        name: "endScale",
        type: "number",
        description: "\u821E\u53F0\u5916\u6846\u6700\u7EC8\u7F29\u653E\u3002",
        minimum: 0.5,
        maximum: 0.85,
        default: 0.62
      }
    ],
    soundCues: ["\u62C9\u8FDC\u5F00\u59CB\u5904\u4E00\u58F0\u67D4\u548C sfx-whoosh-soft\uFF0C\u4E4B\u540E\u4FDD\u6301\u5B89\u9759\u3002"],
    knownFailures: ["\u6CA1\u6709\u821E\u53F0\u65F6\u53EA\u80FD\u505A\u76F8\u673A\u62C9\u56DE\u5230 1.0\uFF0C\u5B64\u7ACB\u611F\u51CF\u5F31\uFF1B\u540E\u9762\u81F3\u5C11\u7559 1.3 \u79D2\u771F\u6B63\u9759\u6B62\u3002"],
    fallbackRecipeIds: ["brand-close"],
    sourceReferences: [shotcraftReference("tension-camera-moves")]
  },
  {
    id: "freeze-orbit",
    version: "1.0.0",
    name: "\u5B9A\u683C\u73AF\u7ED5",
    description: "\u821E\u53F0\u5916\u6846\u4EE5 1600px \u900F\u89C6\u505A 0\xB0\u219255\xB0\u21920\xB0 \u7684 rotateY \u73AF\u7ED5\uFF0C\u500D\u7387 1\u21921.12\u21921\uFF0C\u9876\u70B9\u505C\u7559\u7EA6 0.35 \u79D2\uFF0C\u7528\u4E8E\u5F3A\u8C03\u4E00\u4E2A\u503C\u5F97\u9A7B\u8DB3\u7684\u6570\u636E\u6216\u7ED3\u679C\u753B\u9762\u3002",
    shotRoles: ["result", "evidence", "hook"],
    intents: ["\u9A7B\u8DB3\u5F3A\u8C03", "\u73AF\u7ED5\u5C55\u793A", "\u6570\u636E\u65F6\u523B"],
    energy: "high",
    durationSeconds: { minimum: 3, maximum: 6 },
    requiredVisualLayers: { minimum: 1, maximum: 1 },
    parameters: [
      {
        name: "angle",
        type: "number",
        description: "\u73AF\u7ED5\u9876\u70B9\u89D2\u5EA6\uFF08\u5EA6\uFF09\u3002",
        minimum: 20,
        maximum: 60,
        default: 55
      }
    ],
    soundCues: ["\u73AF\u7ED5\u8D77\u70B9\u9489 sfx-whoosh-soft\uFF0C\u9876\u70B9\u9489 sfx-sparkle\u3002"],
    knownFailures: [
      "\u5F55\u5C4F\u753B\u9762\u5728\u73AF\u7ED5\u671F\u95F4\u4ECD\u5728\u64AD\u653E\uFF0C\u4E0D\u662F\u771F\u6B63\u7684\u5B9A\u683C\uFF1B\u5185\u5BB9\u53D8\u5316\u5267\u70C8\u65F6\u4F1A\u5206\u6563\u6CE8\u610F\u3002",
      "\u9700\u8981\u821E\u53F0\uFF1B\u6CA1\u6709\u821E\u53F0\u65F6\u9000\u5316\u4E3A\u89C6\u89C9\u5C42\u900F\u89C6\u65CB\u8F6C\u3002"
    ],
    fallbackRecipeIds: ["panel-expansion"],
    sourceReferences: [shotcraftReference("tension-camera-moves")]
  },
  {
    id: "split-flap-title",
    version: "1.0.0",
    name: "\u7FFB\u724C\u6807\u9898",
    description: "\u673A\u573A\u7FFB\u724C\u677F\u5F0F\u6807\u9898\uFF1A\u6BCF\u4E2A\u5B57\u7B26\u7ECF\u8FC7 2 \u4E2A\u9519\u8BEF\u5B57\u5F62\u540E\u9501\u5B9A\u5230\u76EE\u6807\uFF0C\u5B57\u7B26\u95F4 4 \u5E27\u7EA7\u8054\uFF0C\u9501\u5B9A\u65F6\u6574\u4F53\u4E0B\u6C89 6px \u518D\u56DE\u5F39\uFF0C\u5168\u7247\u53EA\u7528\u4E00\u6B21\u3002",
    shotRoles: ["hook", "promise", "cta"],
    intents: ["\u673A\u68B0\u516C\u544A\u611F", "\u53D1\u5E03\u65E5\u671F", "\u5F00\u573A\u6807\u9898", "\u6570\u636E\u63ED\u793A"],
    energy: "medium",
    durationSeconds: { minimum: 2.5, maximum: 6 },
    requiredVisualLayers: { minimum: 1 },
    parameters: [
      {
        name: "stagger",
        type: "number",
        description: "\u5B57\u7B26\u95F4\u7EA7\u8054\u95F4\u9694\uFF08\u79D2\uFF09\u3002",
        minimum: 0.08,
        maximum: 0.2,
        default: 0.13
      }
    ],
    soundCues: ["\u6BCF\u4E2A\u5B57\u7B26\u9501\u5B9A\u9489 sfx-mech-lock\uFF0C\u4EA4\u66FF\u97F3\u91CF\u907F\u514D\u673A\u5173\u67AA\u611F\uFF1B\u97F3\u6548\u662F\u8FD9\u4E2A\u914D\u65B9\u7684\u4E00\u534A\u3002"],
    knownFailures: ["\u8D85\u8FC7 14 \u4E2A\u5B57\u7B26\u4F1A\u8D85\u51FA\u89C2\u4F17\u8010\u5FC3\uFF1B\u4E00\u4E2A\u573A\u666F\u53EA\u5141\u8BB8\u4E00\u7EC4\u7FFB\u724C\u3002"],
    fallbackRecipeIds: ["title-blur-slide"],
    sourceReferences: [shotcraftReference("split-flap-title")]
  },
  {
    id: "typewriter-reveal",
    version: "1.0.0",
    name: "\u6253\u5B57\u673A\u9010\u5B57",
    description: "graphics \u6587\u5B57\u4EE5\u771F\u5B9E\u6253\u5B57\u8282\u594F\u9010\u5B57\u51FA\u73B0\u5E76\u5E26\u95EA\u70C1\u5149\u6807\uFF0C\u9002\u5408\u547D\u4EE4\u3001\u63D0\u793A\u8BCD\u3001\u7528\u6237\u8F93\u5165\u8FD9\u7C7B\u201C\u6B63\u5728\u8F93\u5165\u201D\u7684\u8BED\u4E49\u3002",
    shotRoles: ["process", "feature", "hook"],
    intents: ["\u6B63\u5728\u8F93\u5165", "\u547D\u4EE4\u5C55\u793A", "\u63D0\u793A\u8BCD\u5C55\u793A"],
    energy: "low",
    durationSeconds: { minimum: 1.5, maximum: 8 },
    requiredVisualLayers: { minimum: 1 },
    parameters: [
      {
        name: "charsPerSecond",
        type: "number",
        description: "\u6253\u5B57\u901F\u5EA6\u3002",
        minimum: 8,
        maximum: 30,
        default: 18
      }
    ],
    soundCues: ["\u6BCF 2-3 \u4E2A\u5B57\u7B26\u9489\u4E00\u6B21 sfx-typewriter-hit\uFF0C\u97F3\u91CF\u9010\u6B21\u4EA4\u66FF\u3002"],
    knownFailures: ["\u6587\u5B57\u8D85\u8FC7 60 \u4E2A\u5B57\u7B26\u4F1A\u62D6\u6162\u8282\u594F\uFF1B\u4E0E\u771F\u5B9E\u5F55\u5C4F\u91CC\u7684\u8F93\u5165\u540C\u65F6\u51FA\u73B0\u4F1A\u4E92\u76F8\u62A2\u620F\u3002"],
    fallbackRecipeIds: ["title-blur-slide"],
    sourceReferences: [
      shotcraftReference("document-typewriter-reveal"),
      shotcraftReference("typewriter-moves")
    ]
  },
  {
    id: "gradient-word-sweep",
    version: "1.0.0",
    name: "\u6E10\u53D8\u626B\u5B57",
    description: "\u4E00\u9053\u54C1\u724C\u8272\u6E10\u53D8\u4ECE\u5DE6\u5230\u53F3\u626B\u8FC7\u6807\u9898\u6587\u5B57\uFF08background-clip: text\uFF09\uFF0C\u626B\u8FC7\u540E\u6587\u5B57\u56DE\u5230\u54C1\u724C\u6B63\u6587\u8272\u3002\u7528\u4E8E\u4EF7\u503C\u53E5\u7684\u9AD8\u5149\u3002",
    shotRoles: ["promise", "hook", "result"],
    intents: ["\u4EF7\u503C\u53E5\u9AD8\u5149", "\u5173\u952E\u8BCD\u626B\u4EAE"],
    energy: "low",
    durationSeconds: { minimum: 1.5, maximum: 6 },
    requiredVisualLayers: { minimum: 1 },
    parameters: [
      {
        name: "sweepSeconds",
        type: "number",
        description: "\u626B\u8FC7\u4E00\u6B21\u7684\u65F6\u957F\u3002",
        minimum: 0.6,
        maximum: 2.4,
        default: 1.2
      }
    ],
    soundCues: ["\u626B\u8FC7\u8D77\u70B9\u53EF\u914D sfx-sparkle\u3002"],
    knownFailures: ["\u6D45\u8272\u80CC\u666F\u4E0A\u9700\u8981 graphic \u6587\u672C\u672C\u8EAB\u6709\u8DB3\u591F\u5BF9\u6BD4\uFF1B\u6BCF\u4E2A\u573A\u666F\u53EA\u626B\u4E00\u6B21\u3002"],
    fallbackRecipeIds: ["marker-underline"],
    sourceReferences: [shotcraftReference("gradient-word-sweep")]
  },
  {
    id: "title-demote-to-label",
    version: "1.0.0",
    name: "\u6807\u9898\u964D\u7EA7\u4E3A\u6807\u7B7E",
    description: "\u5C45\u4E2D\u7684\u5927\u6807\u9898\u5728 demoteAt \u5904\u7F29\u5C0F\u5E76\u79FB\u5230\u5DE6\u4E0A\u89D2\u53D8\u6210\u7AE0\u8282\u6807\u7B7E\uFF0C\u8BA9\u753B\u9762\u4E3B\u4F53\u8BA9\u4F4D\u7ED9\u4EA7\u54C1\u3002\u7528\u4E8E\u7AE0\u8282\u5F00\u5934\u3002",
    shotRoles: ["hook", "promise", "feature"],
    intents: ["\u7AE0\u8282\u6807\u9898", "\u6807\u9898\u8BA9\u4F4D", "\u4ECE\u9648\u8FF0\u5230\u6F14\u793A"],
    energy: "low",
    durationSeconds: { minimum: 2.5, maximum: 8 },
    requiredVisualLayers: { minimum: 1 },
    parameters: [
      {
        name: "demoteAt",
        type: "number",
        description: "\u964D\u7EA7\u53D1\u751F\u5728\u573A\u666F\u65F6\u957F\u7684\u6BD4\u4F8B\u4F4D\u7F6E\u3002",
        minimum: 0.2,
        maximum: 0.7,
        default: 0.4
      },
      {
        name: "labelScale",
        type: "number",
        description: "\u6807\u7B7E\u76F8\u5BF9\u6807\u9898\u7684\u7F29\u653E\u3002",
        minimum: 0.3,
        maximum: 0.6,
        default: 0.45
      }
    ],
    soundCues: ["\u964D\u7EA7\u79FB\u52A8\u9489 sfx-whoosh-soft\u3002"],
    knownFailures: ["graphics[0] \u9700\u8981\u4EE5\u767E\u5206\u6BD4 left/top \u5C45\u4E2D\u653E\u7F6E\uFF0C\u5426\u5219\u964D\u7EA7\u4F4D\u79FB\u4F1A\u8DF3\u3002"],
    fallbackRecipeIds: ["title-blur-slide"],
    sourceReferences: [shotcraftReference("title-demote-to-label")]
  },
  {
    id: "odometer-digit-roll",
    version: "1.0.0",
    name: "\u91CC\u7A0B\u8868\u6570\u5B57\u6EDA\u52A8",
    description: "graphics[0] \u4E2D\u7684\u6570\u5B57\u9010\u4F4D\u50CF\u8001\u864E\u673A\u4E00\u6837\u6EDA\u52A8\uFF0C\u4ECE\u5DE6\u5230\u53F3\u4F9D\u6B21\u9501\u5B9A\u5E76\u534A\u683C\u8FC7\u51B2\u56DE\u5F39\uFF0C\u5168\u90E8\u9501\u5B9A\u540E\u6574\u4F53 1.035 \u500D\u8109\u51B2\u3002\u7528\u4E8E\u552F\u4E00\u7684\u6838\u5FC3\u6307\u6807\u3002",
    shotRoles: ["result", "evidence", "promise"],
    intents: ["\u6838\u5FC3\u6307\u6807", "\u5927\u6570\u5B57\u63ED\u793A", "\u6570\u636E\u8BC1\u660E"],
    energy: "high",
    durationSeconds: { minimum: 3, maximum: 7 },
    requiredVisualLayers: { minimum: 1 },
    parameters: [
      {
        name: "digitStagger",
        type: "number",
        description: "\u76F8\u90BB\u6570\u4F4D\u9501\u5B9A\u95F4\u9694\uFF08\u79D2\uFF09\u3002",
        minimum: 0.12,
        maximum: 0.35,
        default: 0.23
      }
    ],
    soundCues: ["\u6BCF\u4F4D\u9501\u5B9A\u9489 sfx-mech-lock\uFF0C\u5168\u90E8\u9501\u5B9A\u9489\u4E00\u58F0 sfx-impact-low\u3002"],
    knownFailures: ["\u8D85\u8FC7 6 \u4F4D\u6570\u5B57\u8D85\u51FA\u89C2\u4F17\u8010\u5FC3\uFF1B\u5FC5\u987B\u6EDA\u5230\u771F\u5B9E\u6570\u503C\uFF1B\u5168\u7247\u53EA\u7528\u4E00\u6B21\u3002"],
    fallbackRecipeIds: ["metric-counter"],
    sourceReferences: [shotcraftReference("odometer-digit-roll")]
  },
  {
    id: "metric-counter",
    version: "1.0.0",
    name: "\u6570\u5B57\u8BA1\u6570",
    description: "graphics \u4E2D\u7B2C\u4E00\u4E2A\u6570\u5B57\u4ECE 0 \u4EE5\u7F13\u51FA\u66F2\u7EBF\u8BA1\u6570\u5230\u76EE\u6807\u503C\uFF0C\u524D\u540E\u7F00\uFF08%\u3001x\u3001\u5355\u4F4D\uFF09\u4FDD\u6301\u4E0D\u52A8\u3002\u6BD4\u91CC\u7A0B\u8868\u8F7B\uFF0C\u53EF\u7528\u4E8E\u591A\u4E2A\u6B21\u7EA7\u6307\u6807\u3002",
    shotRoles: ["result", "evidence"],
    intents: ["\u6307\u6807\u8BA1\u6570", "\u6B21\u7EA7\u6570\u636E", "\u767E\u5206\u6BD4"],
    energy: "medium",
    durationSeconds: { minimum: 1.5, maximum: 6 },
    requiredVisualLayers: { minimum: 1 },
    parameters: [
      {
        name: "countSeconds",
        type: "number",
        description: "\u8BA1\u6570\u65F6\u957F\u3002",
        minimum: 0.6,
        maximum: 3,
        default: 1.4
      }
    ],
    soundCues: ["\u8BA1\u6570\u7ED3\u675F\u9489 sfx-ui-tick\u3002"],
    knownFailures: ["\u6587\u5B57\u91CC\u6CA1\u6709\u6570\u5B57\u65F6\u4E0D\u4EA7\u751F\u52A8\u753B\uFF1B\u5C0F\u6570\u4F4D\u7531\u539F\u6587\u51B3\u5B9A\u3002"],
    fallbackRecipeIds: ["metric-proof"],
    sourceReferences: [shotcraftReference("counter-confetti")]
  },
  {
    id: "deck-deal-flyin",
    version: "1.0.0",
    name: "\u53D1\u724C\u98DE\u5165",
    description: "2-6 \u4E2A\u89C6\u89C9\u5C42\u50CF\u4E00\u53E0\u5361\u7247\u4ECE\u53F3\u4E0B\u65B9\u5E26\u65CB\u8F6C\u6296\u52A8\u4F9D\u6B21\u53D1\u5230\u4E00\u6392\u4F4D\u7F6E\uFF0C\u95F4\u9694\u6309\u52A0\u901F\u66F2\u7EBF\u6536\u7D27\uFF0C\u6700\u540E\u4E00\u5F20\u7565\u5FAE\u8FC7\u51B2\u843D\u4F4D\u3002\u7528\u4E8E\u591A\u9875\u9762\u6216\u591A\u529F\u80FD\u4E00\u89C8\u3002",
    shotRoles: ["feature", "hook", "evidence"],
    intents: ["\u591A\u9875\u9762\u4E00\u89C8", "\u529F\u80FD\u77E9\u9635", "\u5361\u7247\u53D1\u724C"],
    energy: "high",
    durationSeconds: { minimum: 2, maximum: 6 },
    requiredVisualLayers: { minimum: 2, maximum: 6 },
    parameters: [
      {
        name: "cardScale",
        type: "number",
        description: "\u6BCF\u5F20\u5361\u7247\u7684\u7F29\u653E\u3002",
        minimum: 0.28,
        maximum: 0.6,
        default: 0.42
      }
    ],
    soundCues: ["\u7B2C\u4E00\u5F20\u9489 sfx-whoosh-fast\uFF0C\u540E\u7EED\u5408\u5E76\u6210\u4E00\u6761 sfx-whoosh-soft \u5C3E\u5DF4\u3002"],
    knownFailures: ["\u540C\u65F6\u53D1\u51FA\u8BFB\u4F5C\u7206\u70B8\uFF0C\u5FC5\u987B\u6709\u52A0\u901F\u7EA7\u8054\uFF1B\u5361\u7247\u7EB9\u7406\u5FC5\u987B\u662F\u771F\u5B9E\u754C\u9762\u88C1\u5207\u3002"],
    fallbackRecipeIds: ["multi-screen-carousel"],
    sourceReferences: [shotcraftReference("deck-deal-flyin")]
  },
  {
    id: "list-reveal",
    version: "1.0.0",
    name: "\u5217\u8868\u9010\u9879\u63ED\u793A",
    description: "graphics \u4F5C\u4E3A\u5217\u8868\u9879\u4ECE\u5DE6\u4FA7\u5E26 accent \u8272\u77ED\u7EBF\u4F9D\u6B21\u6ED1\u5165\uFF0C\u95F4\u9694 0.14 \u79D2\uFF0C\u9002\u5408\u529F\u80FD\u8981\u70B9\u3001\u6B65\u9AA4\u6E05\u5355\u548C\u6743\u76CA\u5217\u8868\u3002",
    shotRoles: ["feature", "promise", "process"],
    intents: ["\u8981\u70B9\u5217\u8868", "\u6B65\u9AA4\u6E05\u5355", "\u6743\u76CA\u5217\u8868"],
    energy: "low",
    durationSeconds: { minimum: 2, maximum: 8 },
    requiredVisualLayers: { minimum: 1 },
    parameters: [
      {
        name: "stagger",
        type: "number",
        description: "\u5217\u8868\u9879\u95F4\u9694\uFF08\u79D2\uFF09\u3002",
        minimum: 0.08,
        maximum: 0.3,
        default: 0.14
      }
    ],
    soundCues: ["\u6BCF\u9879\u843D\u4F4D\u9489 sfx-ui-tick\uFF0C\u97F3\u91CF\u9012\u51CF\u3002"],
    knownFailures: ["\u8D85\u8FC7 6 \u9879\u4F1A\u62D6\u6162\uFF1B\u5217\u8868\u9879\u9700\u8981\u7528 graphics \u7684 top \u767E\u5206\u6BD4\u624B\u52A8\u6392\u5217\u3002"],
    fallbackRecipeIds: ["metric-proof"],
    sourceReferences: [shotcraftReference("list-reveal")]
  },
  {
    id: "skeleton-reveal",
    version: "1.0.0",
    name: "\u9AA8\u67B6\u53D8\u771F\u5B9E",
    description: "\u5728\u771F\u5B9E\u754C\u9762\u4E0A\u5148\u8986\u76D6\u7070\u8272\u9AA8\u67B6\u6761\uFF08\u5E26\u5FAE\u5149\u626B\u52A8\uFF09\uFF0C\u5728 revealAt \u5904\u9AA8\u67B6\u6574\u4F53\u6D88\u6563\u9732\u51FA\u771F\u5B9E\u754C\u9762\uFF0C\u540C\u65F6\u76F8\u673A\u8F7B\u63A8 1\u21921.08 \u5236\u9020\u201C\u51D1\u8FD1\u770B\u6E05\u201D\u7684\u52A8\u673A\u3002",
    shotRoles: ["feature", "process", "hook"],
    intents: ["\u4ECE\u6982\u5FF5\u5230\u771F\u5B9E", "\u52A0\u8F7D\u5B8C\u6210", "\u751F\u6210\u5B8C\u6210"],
    energy: "medium",
    durationSeconds: { minimum: 2.5, maximum: 7 },
    requiredVisualLayers: { minimum: 1, maximum: 1 },
    parameters: [
      {
        name: "revealAt",
        type: "number",
        description: "\u9AA8\u67B6\u6D88\u6563\u53D1\u751F\u5728\u573A\u666F\u65F6\u957F\u7684\u6BD4\u4F8B\u4F4D\u7F6E\u3002",
        minimum: 0.25,
        maximum: 0.7,
        default: 0.4
      }
    ],
    soundCues: ["\u9AA8\u67B6\u6D88\u6563\u5E27\u9489 sfx-sparkle\u3002"],
    knownFailures: ["\u9AA8\u67B6\u4E0E\u771F\u5B9E\u754C\u9762\u5E03\u5C40\u5FC5\u987B\u5BF9\u9F50\uFF0C\u5426\u5219\u8BFB\u4F5C\u6362\u9875\uFF1B\u6D88\u6563\u4E0D\u80FD\u62D6\u6210\u6162\u6DE1\u51FA\u3002"],
    fallbackRecipeIds: ["ui-focus-zoom"],
    sourceReferences: [shotcraftReference("skeleton-reveal")]
  },
  {
    id: "glint-sweep",
    version: "1.0.0",
    name: "\u9AD8\u5149\u63A0\u8FC7",
    description: "\u4E00\u9053\u659C\u5411\u9AD8\u5149\u6CBF\u821E\u53F0\u5916\u6846\uFF08\u6216\u6574\u5E45\u753B\u9762\uFF09\u4ECE\u5DE6\u5230\u53F3\u626B\u8FC7\u4E00\u6B21\uFF0C\u4E25\u683C\u88C1\u5207\u5728\u5916\u6846\u5706\u89D2\u5185\u3002\u7528\u4E8E\u4EA7\u54C1\u7B2C\u4E00\u6B21\u5B8C\u6574\u51FA\u73B0\u7684\u90A3\u4E00\u523B\uFF0C\u5168\u7247\u6700\u591A\u4E24\u6B21\u3002",
    shotRoles: ["hook", "result", "cta"],
    intents: ["\u4EA7\u54C1\u767B\u573A\u9AD8\u5149", "\u7ED3\u679C\u9AD8\u5149"],
    energy: "low",
    durationSeconds: { minimum: 1.5, maximum: 6 },
    requiredVisualLayers: { minimum: 1 },
    parameters: [
      {
        name: "at",
        type: "number",
        description: "\u9AD8\u5149\u5F00\u59CB\u5728\u573A\u666F\u65F6\u957F\u7684\u6BD4\u4F8B\u4F4D\u7F6E\u3002",
        minimum: 0,
        maximum: 0.8,
        default: 0.25
      },
      {
        name: "width",
        type: "number",
        description: "\u9AD8\u5149\u5E26\u5BBD\u5EA6\u5360\u753B\u9762\u6BD4\u4F8B\u3002",
        minimum: 0.1,
        maximum: 0.4,
        default: 0.22
      }
    ],
    soundCues: ["\u8D77\u70B9\u9489 sfx-sparkle\u3002"],
    knownFailures: ["\u6BCF\u4E2A\u5143\u7D20\u6700\u591A\u4E00\u6B21\u9AD8\u5149\uFF1B\u9AD8\u5149\u6EA2\u51FA\u5706\u89D2\u4F1A\u663E\u5F97\u5EC9\u4EF7\u3002"],
    fallbackRecipeIds: ["product-hero-spotlight"],
    sourceReferences: [shotcraftReference("spotlight-sweep-moves")]
  },
  {
    id: "spotlight-sweep",
    version: "1.0.0",
    name: "\u805A\u5149\u6A2A\u626B\u63ED\u793A",
    description: "\u753B\u9762\u5148\u5904\u4E8E\u534A\u6697\uFF0C\u4E00\u675F\u67D4\u8FB9\u805A\u5149\u4ECE\u5DE6\u5411\u53F3\u5300\u901F\u626B\u8FC7\u628A\u754C\u9762\u70B9\u4EAE\uFF0C\u626B\u5B8C\u540E\u6697\u5C42\u6574\u4F53\u9000\u53BB\u3002\u5300\u901F\u662F\u523B\u610F\u7684\uFF0C\u5236\u9020\u673A\u68B0\u626B\u63CF\u611F\u3002",
    shotRoles: ["hook", "feature", "problem"],
    intents: ["\u9010\u6B65\u70B9\u4EAE\u754C\u9762", "\u626B\u63CF\u63ED\u793A", "\u4ECE\u6697\u5230\u4EAE"],
    energy: "medium",
    durationSeconds: { minimum: 2.5, maximum: 6 },
    requiredVisualLayers: { minimum: 1 },
    parameters: [
      {
        name: "sweepSeconds",
        type: "number",
        description: "\u626B\u8FC7\u4E00\u6B21\u7684\u65F6\u957F\u3002",
        minimum: 1,
        maximum: 4,
        default: 2.2
      },
      {
        name: "darkness",
        type: "number",
        description: "\u672A\u70B9\u4EAE\u533A\u57DF\u7684\u6697\u5EA6\u3002",
        minimum: 0.4,
        maximum: 0.9,
        default: 0.72
      }
    ],
    soundCues: ["\u626B\u8FC7\u65F6\u4E0D\u94FA\u6301\u7EED\u97F3\uFF0C\u70B9\u4EAE\u5B8C\u6210\u9489 sfx-sparkle\u3002"],
    knownFailures: ["\u52A0\u7F13\u52A8\u4F1A\u5931\u53BB\u673A\u68B0\u611F\uFF1B\u626B\u8FC7\u671F\u95F4\u4E0D\u8981\u518D\u53E0\u52A0\u5176\u4ED6\u5165\u573A\u52A8\u753B\u3002"],
    fallbackRecipeIds: ["product-hero-spotlight"],
    sourceReferences: [shotcraftReference("spotlight-sweep-moves")]
  },
  {
    id: "brand-frame-snap",
    version: "1.0.0",
    name: "\u54C1\u724C\u8272\u6846\u6536\u7D27",
    description: "\u56DB\u6761\u54C1\u724C\u8272\u5B9E\u4F53\u8FB9\u4ECE 0 \u957F\u5230\u8BBE\u5B9A\u539A\u5EA6\uFF0C\u968F\u540E\u821E\u53F0\u5916\u6846\u4ECE\u4E0B\u65B9\u5E26\u5F39\u6027\u843D\u5165\u5E76\u4ECE 0.82 \u7F29\u653E\u5230 1\uFF0C\u8FB9\u6846\u5728\u843D\u4F4D\u5E27\u8F7B\u5FAE\u5F39\u52A8\u3002\u7528\u4E8E\u7AE0\u8282\u5F00\u5934\u6216\u6A21\u5F0F\u5207\u6362\u3002",
    shotRoles: ["hook", "feature", "promise"],
    intents: ["\u7AE0\u8282\u5F00\u573A", "\u54C1\u724C\u6846\u5B9A", "\u6A21\u5F0F\u5207\u6362"],
    energy: "high",
    durationSeconds: { minimum: 2, maximum: 6 },
    requiredVisualLayers: { minimum: 1 },
    parameters: [
      {
        name: "thickness",
        type: "number",
        description: "\u8FB9\u6846\u539A\u5EA6\u50CF\u7D20\u3002",
        minimum: 12,
        maximum: 80,
        default: 44
      }
    ],
    soundCues: ["\u8FB9\u6846\u957F\u6EE1\u4E0D\u53D1\u58F0\uFF0C\u5916\u6846\u843D\u4F4D\u5E27\u9489 sfx-impact-low \u6216 sfx-mech-lock\u3002"],
    knownFailures: ["\u54C1\u724C\u8272\u548C\u5E95\u8272\u5BF9\u6BD4\u4E0D\u8DB3\u65F6\u8BFB\u4F5C\u6CA1\u53D1\u751F\uFF1B\u5168\u7247\u8272\u6846\u5207\u6362\u4E0D\u8D85\u8FC7 2 \u6B21\u3002"],
    fallbackRecipeIds: ["browser-fly-in"],
    sourceReferences: [shotcraftReference("brand-frame-snap")]
  },
  {
    id: "impact-feedback",
    version: "1.0.0",
    name: "\u843D\u70B9\u51B2\u51FB\u53CD\u9988",
    description: "\u5728 at \u4F4D\u7F6E\u7ED9\u821E\u53F0\u5916\u6846\u4E00\u6B21 1\u21921.04\u21921 \u7684\u77AC\u65F6\u51B2\u51FB\u548C\u4E00\u6B21 3 \u5E27\u767D\u95EA\uFF0C\u7528\u4E8E\u70B9\u51FB\u6210\u529F\u3001\u751F\u6210\u5B8C\u6210\u3001\u6307\u6807\u843D\u4F4D\u8FD9\u79CD\u201C\u6709\u4E86\u201D\u7684\u77AC\u95F4\u3002",
    shotRoles: ["result", "evidence", "feature"],
    intents: ["\u6210\u529F\u53CD\u9988", "\u843D\u4F4D\u5F3A\u8C03", "\u5B8C\u6210\u77AC\u95F4"],
    energy: "high",
    durationSeconds: { minimum: 1.5, maximum: 8 },
    requiredVisualLayers: { minimum: 1 },
    parameters: [
      {
        name: "at",
        type: "number",
        description: "\u51B2\u51FB\u53D1\u751F\u5728\u573A\u666F\u65F6\u957F\u7684\u6BD4\u4F8B\u4F4D\u7F6E\u3002",
        minimum: 0.05,
        maximum: 0.95,
        default: 0.5
      },
      {
        name: "flash",
        type: "number",
        description: "\u767D\u95EA\u5CF0\u503C\u4E0D\u900F\u660E\u5EA6\u3002",
        minimum: 0,
        maximum: 0.7,
        default: 0.35
      }
    ],
    soundCues: ["\u51B2\u51FB\u5E27\u9489 sfx-impact-low\uFF08\u91CD\uFF09\u6216 sfx-ui-click\uFF08\u8F7B\uFF09\u3002"],
    knownFailures: ["\u4E0E crash-zoom-punch \u6216\u901F\u5EA6\u53D8\u5316\u53E0\u52A0\u4F1A\u6253\u67B6\uFF1B\u4E00\u4E2A\u955C\u5934\u53EA\u5141\u8BB8\u4E00\u6B21\u3002"],
    fallbackRecipeIds: ["feature-callout"],
    sourceReferences: [shotcraftReference("impact-feedback")]
  },
  {
    id: "scanline-annotate-focus",
    version: "1.0.0",
    name: "\u626B\u63CF\u7EBF\u6807\u6CE8\u805A\u7126",
    description: "\u4E00\u6761\u53D1\u5149\u626B\u63CF\u7EBF\u81EA\u4E0A\u800C\u4E0B\u626B\u8FC7\u754C\u9762\uFF0C\u968F\u540E\u56DB\u4E2A\u89D2\u62EC\u53F7\u5728\u76EE\u6807\u77E9\u5F62\u5904\u4ECE 1.3 \u500D\u6536\u62E2\u9501\u5B9A\uFF0C\u914D\u5408\u5FAE\u6697\u906E\u7F69\u7A81\u51FA\u76EE\u6807\u3002\u9002\u5408\u201CAI \u6B63\u5728\u5206\u6790/\u8BC6\u522B\u201D\u7684\u8BED\u4E49\u3002",
    shotRoles: ["process", "feature", "evidence"],
    intents: ["AI \u5206\u6790", "\u8BC6\u522B\u5B9A\u4F4D", "\u626B\u63CF\u6807\u6CE8"],
    energy: "medium",
    durationSeconds: { minimum: 2, maximum: 8 },
    requiredVisualLayers: { minimum: 1 },
    parameters: [
      {
        name: "x",
        type: "number",
        description: "\u76EE\u6807\u77E9\u5F62\u5DE6\u4E0A X\uFF080-1\uFF09\u3002",
        minimum: 0,
        maximum: 1,
        default: 0.3
      },
      {
        name: "y",
        type: "number",
        description: "\u76EE\u6807\u77E9\u5F62\u5DE6\u4E0A Y\uFF080-1\uFF09\u3002",
        minimum: 0,
        maximum: 1,
        default: 0.3
      },
      {
        name: "width",
        type: "number",
        description: "\u76EE\u6807\u77E9\u5F62\u5BBD\u5EA6\uFF080-1\uFF09\u3002",
        minimum: 0.05,
        maximum: 1,
        default: 0.4
      },
      {
        name: "height",
        type: "number",
        description: "\u76EE\u6807\u77E9\u5F62\u9AD8\u5EA6\uFF080-1\uFF09\u3002",
        minimum: 0.05,
        maximum: 1,
        default: 0.3
      }
    ],
    soundCues: ["\u626B\u63CF\u7EBF\u79FB\u52A8\u65F6\u4E0D\u94FA\u6301\u7EED\u97F3\uFF0C\u62EC\u53F7\u9501\u5B9A\u9489 sfx-mech-lock\u3002"],
    knownFailures: ["\u77E9\u5F62\u5FC5\u987B\u843D\u5728\u753B\u5E03\u5185\uFF1B\u626B\u63CF\u7EBF\u8D85\u8FC7 1.2 \u79D2\u4F1A\u62D6\u6C93\u3002"],
    fallbackRecipeIds: ["feature-callout"],
    sourceReferences: [
      shotcraftReference("scanline-annotate-focus"),
      shotcraftReference("scan-bracket-sweep")
    ]
  }
];
var UI_EXTRACTION_RECIPES = [
  {
    id: "element-lift",
    version: "1.0.0",
    name: "\u754C\u9762\u5143\u7D20\u62AC\u5347",
    description: "\u628A\u5F55\u5C4F\u91CC\u7684\u4E00\u4E2A\u771F\u5B9E\u754C\u9762\u533A\u57DF\uFF08\u6309\u94AE\u3001\u9762\u677F\u3001\u7ED3\u679C\u5361\uFF09\u4ECE\u753B\u9762\u4E2D\u62AC\u8D77\u5230\u524D\u666F\uFF1A\u533A\u57DF\u4FDD\u6301\u771F\u5B9E\u50CF\u7D20\u5E76\u653E\u5927 1.12 \u500D\uFF0C\u5E26\u6295\u5F71\u4E0E\u5706\u89D2\uFF0C\u80CC\u666F\u5F55\u5C4F\u540C\u65F6\u6A21\u7CCA\u538B\u6697\u3002\u662F\u8F6F\u4EF6\u5BA3\u4F20\u7247\u91CC\u6700\u6709\u201C\u53D1\u5E03\u4F1A\u611F\u201D\u7684\u955C\u5934\uFF0C\u4E5F\u4E0D\u8FDD\u53CD\u8BC1\u636E\u89C4\u5219\u3002\u533A\u57DF\u5750\u6807\u6765\u81EA analyze_video_range \u7684\u89C2\u5BDF\u6216 protectedRegions\u3002",
    shotRoles: ["feature", "result", "evidence", "promise"],
    intents: ["\u7A81\u51FA\u4E00\u4E2A\u63A7\u4EF6", "\u7ED3\u679C\u5361\u7247\u62AC\u8D77", "\u754C\u9762\u62C6\u51FA\u524D\u666F", "\u53D1\u5E03\u4F1A\u5F0F\u805A\u7126"],
    energy: "medium",
    durationSeconds: { minimum: 2.5, maximum: 8 },
    requiredVisualLayers: { minimum: 1, maximum: 1 },
    parameters: [
      {
        name: "x",
        type: "number",
        description: "\u533A\u57DF\u5DE6\u8FB9\uFF080-1\uFF0C\u753B\u9762\u6BD4\u4F8B\uFF09\u3002",
        minimum: 0,
        maximum: 0.95
      },
      {
        name: "y",
        type: "number",
        description: "\u533A\u57DF\u9876\u8FB9\uFF080-1\uFF09\u3002",
        minimum: 0,
        maximum: 0.95
      },
      {
        name: "width",
        type: "number",
        description: "\u533A\u57DF\u5BBD\u5EA6\uFF080.04-1\uFF09\u3002",
        minimum: 0.04,
        maximum: 1
      },
      {
        name: "height",
        type: "number",
        description: "\u533A\u57DF\u9AD8\u5EA6\uFF080.04-1\uFF09\u3002",
        minimum: 0.04,
        maximum: 1
      },
      {
        name: "lift",
        type: "number",
        description: "\u62AC\u5347\u540E\u7684\u7F29\u653E\u3002",
        minimum: 1.02,
        maximum: 1.4,
        default: 1.12
      },
      {
        name: "dim",
        type: "number",
        description: "\u80CC\u666F\u538B\u6697\u7A0B\u5EA6\u3002",
        minimum: 0,
        maximum: 0.8,
        default: 0.42
      },
      {
        name: "blur",
        type: "number",
        description: "\u80CC\u666F\u6A21\u7CCA\u50CF\u7D20\u3002",
        minimum: 0,
        maximum: 24,
        default: 8
      },
      {
        name: "radius",
        type: "number",
        description: "\u62AC\u5347\u533A\u57DF\u5706\u89D2\u50CF\u7D20\u3002",
        minimum: 0,
        maximum: 40,
        default: 12
      }
    ],
    soundCues: ["\u62AC\u8D77\u77AC\u95F4 sfx-whoosh-soft\uFF0C\u843D\u4F4D\u9489\u4E00\u4E2A sfx-ui-tick\u3002"],
    knownFailures: [
      "\u533A\u57DF\u5FC5\u987B\u6765\u81EA\u771F\u5B9E\u89C2\u5BDF\u5750\u6807\uFF0C\u51ED\u7A7A\u731C\u6D4B\u4F1A\u62AC\u8D77\u534A\u4E2A\u6309\u94AE\uFF1B\u4E0D\u8981\u4E0E cameraMotion \u540C\u7528\uFF0C\u955C\u5934\u7F29\u653E\u4F1A\u8BA9\u62AC\u5347\u533A\u57DF\u9519\u4F4D\u3002"
    ],
    fallbackRecipeIds: ["feature-callout", "ui-focus-zoom"],
    sourceReferences: [
      { project: "OOVideo", reference: "ui-extraction-lift", license: "internal" }
    ]
  },
  {
    id: "layer-explode",
    version: "1.0.0",
    name: "\u754C\u9762\u5206\u5C42\u7206\u70B8",
    description: "\u628A\u6700\u591A\u4E09\u4E2A\u771F\u5B9E\u754C\u9762\u533A\u57DF\u6309\u5C42\u62AC\u5230\u4E0D\u540C\u6DF1\u5EA6\uFF081.12/1.18/1.24 \u500D\uFF09\uFF0C\u6574\u5E45\u753B\u9762\u5E26\u900F\u89C6\u7F13\u6162\u6446\u52A8\uFF0C\u80CC\u666F\u6A21\u7CCA\u538B\u6697\uFF0C\u5F62\u6210 Apple \u53D1\u5E03\u4F1A\u5F0F\u7684\u7206\u70B8\u5206\u5C42\u89C6\u56FE\u3002\u533A\u57DF\u8D8A\u5C11\u8D8A\u5E72\u51C0\u3002",
    shotRoles: ["hook", "promise", "feature"],
    intents: ["\u62C6\u89E3\u754C\u9762\u7ED3\u6784", "\u5C55\u793A\u591A\u4E2A\u6A21\u5757", "\u7206\u70B8\u5206\u5C42\u89C6\u56FE", "\u4E09\u7EF4\u7A7A\u95F4\u611F"],
    energy: "high",
    durationSeconds: { minimum: 3, maximum: 8 },
    requiredVisualLayers: { minimum: 1, maximum: 1 },
    parameters: [
      { name: "x", type: "number", description: "\u7B2C\u4E00\u533A\u57DF\u5DE6\u8FB9\u3002", minimum: 0, maximum: 0.95 },
      { name: "y", type: "number", description: "\u7B2C\u4E00\u533A\u57DF\u9876\u8FB9\u3002", minimum: 0, maximum: 0.95 },
      {
        name: "width",
        type: "number",
        description: "\u7B2C\u4E00\u533A\u57DF\u5BBD\u3002",
        minimum: 0.04,
        maximum: 1
      },
      {
        name: "height",
        type: "number",
        description: "\u7B2C\u4E00\u533A\u57DF\u9AD8\u3002",
        minimum: 0.04,
        maximum: 1
      },
      {
        name: "x2",
        type: "number",
        description: "\u7B2C\u4E8C\u533A\u57DF\u5DE6\u8FB9\uFF08\u53EF\u9009\uFF09\u3002",
        minimum: 0,
        maximum: 0.95
      },
      {
        name: "y2",
        type: "number",
        description: "\u7B2C\u4E8C\u533A\u57DF\u9876\u8FB9\uFF08\u53EF\u9009\uFF09\u3002",
        minimum: 0,
        maximum: 0.95
      },
      {
        name: "width2",
        type: "number",
        description: "\u7B2C\u4E8C\u533A\u57DF\u5BBD\uFF08\u53EF\u9009\uFF09\u3002",
        minimum: 0.04,
        maximum: 1
      },
      {
        name: "height2",
        type: "number",
        description: "\u7B2C\u4E8C\u533A\u57DF\u9AD8\uFF08\u53EF\u9009\uFF09\u3002",
        minimum: 0.04,
        maximum: 1
      },
      {
        name: "x3",
        type: "number",
        description: "\u7B2C\u4E09\u533A\u57DF\u5DE6\u8FB9\uFF08\u53EF\u9009\uFF09\u3002",
        minimum: 0,
        maximum: 0.95
      },
      {
        name: "y3",
        type: "number",
        description: "\u7B2C\u4E09\u533A\u57DF\u9876\u8FB9\uFF08\u53EF\u9009\uFF09\u3002",
        minimum: 0,
        maximum: 0.95
      },
      {
        name: "width3",
        type: "number",
        description: "\u7B2C\u4E09\u533A\u57DF\u5BBD\uFF08\u53EF\u9009\uFF09\u3002",
        minimum: 0.04,
        maximum: 1
      },
      {
        name: "height3",
        type: "number",
        description: "\u7B2C\u4E09\u533A\u57DF\u9AD8\uFF08\u53EF\u9009\uFF09\u3002",
        minimum: 0.04,
        maximum: 1
      },
      {
        name: "tilt",
        type: "number",
        description: "\u6574\u5E45\u753B\u9762\u7684\u900F\u89C6\u6446\u52A8\u89D2\u5EA6\u3002",
        minimum: 2,
        maximum: 14,
        default: 7
      },
      {
        name: "lift",
        type: "number",
        description: "\u7B2C\u4E00\u5C42\u7684\u7F29\u653E\uFF0C\u540E\u7EED\u6BCF\u5C42\u518D\u52A0 0.06\u3002",
        minimum: 1.04,
        maximum: 1.3,
        default: 1.12
      },
      {
        name: "dim",
        type: "number",
        description: "\u80CC\u666F\u538B\u6697\u7A0B\u5EA6\u3002",
        minimum: 0,
        maximum: 0.8,
        default: 0.42
      }
    ],
    soundCues: ["\u6BCF\u5C42\u62AC\u8D77\u4E00\u4E2A sfx-whoosh-soft \u4F9D\u6B21\u9519\u5F00\uFF0C\u4E0D\u94FA\u6301\u7EED\u97F3\u3002"],
    knownFailures: ["\u533A\u57DF\u91CD\u53E0\u4F1A\u4E92\u76F8\u906E\u6321\uFF1B\u8D85\u8FC7\u4E09\u4E2A\u533A\u57DF\u8BFB\u4E0D\u6E05\uFF1B\u4E0D\u8981\u4E0E cameraMotion \u540C\u7528\u3002"],
    fallbackRecipeIds: ["element-lift"],
    sourceReferences: [
      { project: "OOVideo", reference: "ui-extraction-explode", license: "internal" }
    ]
  },
  {
    id: "depth-parallax",
    version: "1.0.0",
    name: "2.5D \u89C6\u5DEE",
    description: "\u5F55\u5C4F\u6574\u4F53\u5E26\u8F7B\u5FAE\u900F\u89C6\u6446\u52A8\u5E76\u6162\u901F\u5E73\u79FB\uFF0C\u4E00\u4E2A\u771F\u5B9E\u754C\u9762\u533A\u57DF\u4EE5\u76F8\u53CD\u65B9\u5411\u3001\u7565\u9AD8\u4E00\u5C42\u7684\u4F4D\u7F6E\u6F02\u6D6E\uFF0C\u5F62\u6210\u524D\u540E\u666F\u89C6\u5DEE\u3002\u80CC\u666F\u53EA\u8F7B\u5FAE\u6A21\u7CCA\uFF0C\u9002\u5408\u957F\u955C\u5934\u4FDD\u6301\u547C\u5438\u611F\u800C\u4E0D\u62A2\u620F\u3002",
    shotRoles: ["breather", "feature", "process", "promise"],
    intents: ["\u957F\u955C\u5934\u547C\u5438", "\u8F7B\u5FAE\u4E09\u7EF4\u611F", "\u89C6\u5DEE\u6F02\u6D6E", "\u6C89\u7A33\u5C55\u793A"],
    energy: "low",
    durationSeconds: { minimum: 3, maximum: 12 },
    requiredVisualLayers: { minimum: 1, maximum: 1 },
    parameters: [
      { name: "x", type: "number", description: "\u6F02\u6D6E\u533A\u57DF\u5DE6\u8FB9\u3002", minimum: 0, maximum: 0.95 },
      { name: "y", type: "number", description: "\u6F02\u6D6E\u533A\u57DF\u9876\u8FB9\u3002", minimum: 0, maximum: 0.95 },
      {
        name: "width",
        type: "number",
        description: "\u6F02\u6D6E\u533A\u57DF\u5BBD\u3002",
        minimum: 0.04,
        maximum: 1
      },
      {
        name: "height",
        type: "number",
        description: "\u6F02\u6D6E\u533A\u57DF\u9AD8\u3002",
        minimum: 0.04,
        maximum: 1
      },
      {
        name: "tilt",
        type: "number",
        description: "\u900F\u89C6\u6446\u52A8\u89D2\u5EA6\u3002",
        minimum: 1,
        maximum: 10,
        default: 5
      },
      {
        name: "lift",
        type: "number",
        description: "\u6F02\u6D6E\u533A\u57DF\u7F29\u653E\u3002",
        minimum: 1.02,
        maximum: 1.2,
        default: 1.06
      }
    ],
    soundCues: ["\u4E0D\u9700\u8981\u97F3\u6548\uFF0C\u4EA4\u7ED9\u73AF\u5883\u97F3\u4E50\u3002"],
    knownFailures: ["\u533A\u57DF\u592A\u5927\u4F1A\u50CF\u6574\u5C4F\u6296\u52A8\uFF1B\u4E0D\u8981\u4E0E cameraMotion \u540C\u7528\u3002"],
    fallbackRecipeIds: ["element-lift"],
    sourceReferences: [
      { project: "OOVideo", reference: "ui-extraction-parallax", license: "internal" }
    ]
  }
];
var SOFTWARE_PROMO_TRANSITIONS = [
  { id: "cut", name: "\u76F4\u63A5\u5207", durationSeconds: { minimum: 0, maximum: 0 } },
  {
    id: "glitch-cut",
    name: "\u6545\u969C\u5207",
    durationSeconds: { minimum: 0.2, maximum: 0.6 },
    description: "\u524D\u540E\u4E24\u573A\u5728\u5207\u70B9\u524D\u540E\u5404\u6296\u52A8\u51E0\u5E27\uFF0C\u4F34\u968F\u54C1\u724C\u8272/\u7EA2/\u9752\u8272\u6761\u95EA\u70C1\u4E0E\u8272\u76F8\u504F\u79FB\uFF0C\u9002\u5408\u5F3A\u8282\u62CD\u3001AI \u4E0E\u5F00\u53D1\u8005\u4EA7\u54C1\u3002\u5168\u7247\u6700\u591A\u4E24\u6B21\u3002"
  },
  {
    id: "light-leak",
    name: "\u5149\u6CC4\u6F0F",
    durationSeconds: { minimum: 0.4, maximum: 1.2 },
    description: "\u4E00\u56E2\u6696\u8272\u5149\u6591\u6A2A\u626B\u753B\u9762\uFF0C\u540E\u4E00\u573A\u5728\u5149\u4E0B\u6DE1\u5165\uFF0C\u7535\u5F71\u611F\u6700\u5F3A\u7684\u67D4\u6027\u5207\u6362\uFF0C\u9002\u5408\u7AE0\u8282\u8F6C\u6362\u4E0E\u8FDB\u5165\u7247\u5C3E\u3002"
  },
  {
    id: "ripple",
    name: "\u6CE2\u7EB9\u6EB6\u89E3",
    durationSeconds: { minimum: 0.4, maximum: 1.2 },
    description: "\u540E\u4E00\u573A\u5E26\u6DB2\u6001\u4F4D\u79FB\u6CE2\u7EB9\u6DE1\u5165\u5E76\u9010\u6E10\u5E73\u9759\uFF0C\u9002\u5408\u201C\u751F\u6210/\u5904\u7406\u5B8C\u6210\u201D\u540E\u7684\u7ED3\u679C\u63ED\u793A\u3002"
  },
  {
    id: "cube-rotate",
    name: "\u7ACB\u65B9\u4F53\u65CB\u8F6C",
    durationSeconds: { minimum: 0.4, maximum: 1 },
    description: "\u4E24\u573A\u50CF\u7ACB\u65B9\u4F53\u4E24\u4E2A\u9762\u4E00\u6837\u7ED5\u8F74\u65CB\u8F6C\u5207\u6362\uFF0Cdirection \u51B3\u5B9A\u65CB\u8F6C\u65B9\u5411\uFF0C\u9002\u5408\u5E76\u5217\u6A21\u5757\u4E4B\u95F4\u3002"
  },
  {
    id: "slice-wipe",
    name: "\u6761\u7EB9\u5212\u50CF",
    durationSeconds: { minimum: 0.3, maximum: 0.8 },
    description: "\u516B\u6761\u54C1\u724C\u8272\u7AD6\u6761\u4F9D\u6B21\u626B\u8FC7\uFF0C\u540E\u4E00\u573A\u6309\u9636\u68AF\u9732\u51FA\uFF0C\u9002\u5408\u8282\u594F\u5F3A\u7684\u529F\u80FD\u5217\u4E3E\u3002"
  },
  {
    id: "chroma-split",
    name: "\u8272\u6563\u5207",
    durationSeconds: { minimum: 0.2, maximum: 0.6 },
    description: "\u7EA2\u84DD\u901A\u9053\u5206\u79BB\u5230\u5CF0\u503C\u65F6\u786C\u5207\uFF0C\u968F\u540E\u5408\u62E2\uFF0C\u9002\u5408\u51B2\u51FB\u578B\u8282\u62CD\u70B9\u3002\u5168\u7247\u6700\u591A\u4E24\u6B21\u3002"
  },
  { id: "crossfade", name: "\u4EA4\u53C9\u6DE1\u5316", durationSeconds: { minimum: 0.15, maximum: 1.2 } },
  { id: "whip-pan", name: "\u7529\u955C\u5207\u6362", durationSeconds: { minimum: 0.18, maximum: 0.7 } },
  { id: "hidden-cut", name: "\u906E\u6321\u9690\u85CF\u5207", durationSeconds: { minimum: 0.2, maximum: 0.8 } },
  { id: "zoom-through", name: "\u7A7F\u900F\u7F29\u653E", durationSeconds: { minimum: 0.2, maximum: 0.8 } },
  { id: "match-cut", name: "\u5339\u914D\u5207\u6362", durationSeconds: { minimum: 0.12, maximum: 0.6 } },
  {
    id: "iris",
    name: "\u5706\u5F62\u5149\u5708\u63ED\u793A",
    durationSeconds: { minimum: 0.4, maximum: 1.2 },
    description: "\u4EE5 focusX/focusY \u4E3A\u5706\u5FC3\u7684\u5706\u5F62\u63ED\u793A\uFF0C\u524D\u540E\u4E24\u573A\u5728\u5706\u5FC3\u5904\u5E94\u6709\u540C\u5F62\u72B6\u5143\u7D20\uFF08\u5934\u50CF\u2192\u6570\u636E\u73AF\u3001\u56FE\u6807\u2192\u6307\u6807\uFF09\u3002"
  },
  {
    id: "push",
    name: "\u63A8\u79FB\u5207\u6362",
    durationSeconds: { minimum: 0.25, maximum: 0.8 },
    description: "\u524D\u4E00\u573A\u6CBF direction \u88AB\u63A8\u51FA\uFF0C\u540E\u4E00\u573A\u540C\u5411\u63A8\u5165\uFF0C\u65E0\u6A21\u7CCA\uFF0C\u9002\u5408\u5E76\u5217\u6B65\u9AA4\u4E4B\u95F4\u3002"
  },
  {
    id: "flip",
    name: "\u7FFB\u9875\u5207\u6362",
    durationSeconds: { minimum: 0.4, maximum: 1 },
    description: "\u524D\u4E00\u573A\u7ED5\u5782\u76F4\u8F74\u7FFB\u8D70\uFF0C\u540E\u4E00\u573A\u7FFB\u5165\uFF0C\u9002\u5408\u201C\u7FFB\u5230\u4E0B\u4E00\u9875/\u4E0B\u4E00\u6A21\u5F0F\u201D\u3002"
  },
  {
    id: "blur-dissolve",
    name: "\u6A21\u7CCA\u6EB6\u89E3",
    durationSeconds: { minimum: 0.3, maximum: 1.2 },
    description: "\u4E24\u573A\u540C\u65F6\u6A21\u7CCA\u5E76\u4EA4\u53C9\u6DE1\u5316\uFF0C\u9002\u5408\u65F6\u95F4\u6D41\u901D\u6216\u4ECE\u6982\u5FF5\u8FDB\u5165\u4EA7\u54C1\u3002"
  },
  {
    id: "wipe",
    name: "\u8F6F\u8FB9\u5212\u50CF",
    durationSeconds: { minimum: 0.3, maximum: 0.9 },
    description: "\u540E\u4E00\u573A\u6CBF direction \u4EE5\u76F4\u7EBF\u5212\u5165\u8986\u76D6\u524D\u4E00\u573A\uFF0C\u9002\u5408\u524D\u540E\u5BF9\u6BD4\u4E0E\u7AE0\u8282\u5207\u6362\u3002"
  },
  {
    id: "white-flash",
    name: "\u767D\u95EA\u786C\u5207",
    durationSeconds: { minimum: 0.15, maximum: 0.5 },
    description: "\u767D\u5149\u95EA\u5230\u5CF0\u503C\u65F6\u786C\u5207\uFF0C\u9002\u5408 Logo \u7B80\u5316\u843D\u4F4D\u3001\u5F3A\u8282\u62CD\u70B9\u3002"
  }
];
var recipeById = new Map(
  [...SOFTWARE_PROMO_SHOT_RECIPES, ...UI_EXTRACTION_RECIPES].map((recipe) => [recipe.id, recipe])
);
var transitionById = new Map(SOFTWARE_PROMO_TRANSITIONS.map((item) => [item.id, item]));
var ALL_SHOT_RECIPES = [
  ...SOFTWARE_PROMO_SHOT_RECIPES,
  ...UI_EXTRACTION_RECIPES
];
function listShotRecipes(query = {}) {
  const normalizedIntent = query.intent?.trim().toLowerCase();
  const maximum = Math.max(1, Math.min(48, query.maxResults ?? 48));
  return ALL_SHOT_RECIPES.filter(
    (recipe) => (!query.shotRole || recipe.shotRoles.includes(query.shotRole)) && (!normalizedIntent || recipe.name.toLowerCase().includes(normalizedIntent) || recipe.description.toLowerCase().includes(normalizedIntent) || recipe.intents.some((intent) => intent.toLowerCase().includes(normalizedIntent)))
  ).slice(0, maximum);
}
function getShotRecipe(id) {
  return recipeById.get(id);
}
function editDistance(left, right) {
  const previous = Array.from({ length: right.length + 1 }, (_, index) => index);
  for (let i = 1; i <= left.length; i++) {
    let diagonal = previous[0];
    previous[0] = i;
    for (let j = 1; j <= right.length; j++) {
      const above = previous[j];
      previous[j] = Math.min(
        previous[j] + 1,
        previous[j - 1] + 1,
        diagonal + (left[i - 1] === right[j - 1] ? 0 : 1)
      );
      diagonal = above;
    }
  }
  return previous[right.length];
}
function closestShotRecipeIds(id) {
  const words = new Set(id.toLowerCase().split(/[^a-z0-9]+/).filter(Boolean));
  return [...recipeById.keys()].map((candidate) => {
    const shared = candidate.split("-").filter((word) => words.has(word)).length;
    return { candidate, score: shared * 10 - editDistance(id.toLowerCase(), candidate) };
  }).filter(({ candidate, score }) => score > -Math.max(6, candidate.length / 2)).sort((a, b) => b.score - a.score).slice(0, 3).map(({ candidate }) => candidate);
}
function assertProjectShotRecipes(project) {
  for (const scene of project.scenes) {
    normalizeTransition(scene.transitionIn);
    normalizeTransition(scene.transitionOut);
    if (!scene.recipe) continue;
    const manifest = recipeById.get(scene.recipe.id);
    if (!manifest) {
      const suggestions = closestShotRecipeIds(scene.recipe.id);
      throw new Error(
        `Scene ${scene.id} references unknown shot recipe ${scene.recipe.id}.` + (suggestions.length ? ` Closest shot recipes: ${suggestions.join(", ")}.` : "") + " scene.recipe only accepts IDs from list_shot_recipes; ShotCraft recipe names are motion references, so realise them with motionLayers and leave scene.recipe out."
      );
    }
    if (scene.recipe.version && !isCompatibleRecipeVersion(scene.recipe.version, manifest.version))
      throw new Error(
        `Scene ${scene.id} requires ${scene.recipe.id}@${scene.recipe.version}, but ${manifest.version} is installed.`
      );
    if (scene.shotRole && !manifest.shotRoles.includes(scene.shotRole))
      throw new Error(
        `Scene ${scene.id} uses ${scene.recipe.id} for unsupported shot role ${scene.shotRole}.`
      );
    const duration = scene.range.end - scene.range.start;
    if (duration < manifest.durationSeconds.minimum || duration > manifest.durationSeconds.maximum)
      throw new Error(
        `Scene ${scene.id} duration must be ${manifest.durationSeconds.minimum}-${manifest.durationSeconds.maximum}s for ${manifest.id}.`
      );
    if (scene.visualLayers.length < manifest.requiredVisualLayers.minimum || manifest.requiredVisualLayers.maximum !== void 0 && scene.visualLayers.length > manifest.requiredVisualLayers.maximum)
      throw new Error(
        `Scene ${scene.id} has ${scene.visualLayers.length} visual layers; ${manifest.id} requires ${manifest.requiredVisualLayers.minimum}-${manifest.requiredVisualLayers.maximum ?? "many"}.`
      );
    assertRecipeParameters(scene.id, scene.recipe, manifest);
  }
}
function isCompatibleRecipeVersion(requested, installed) {
  const major = (value) => value.trim().split(".")[0];
  return requested.trim() === installed.trim() || major(requested) !== "" && major(requested) === major(installed);
}
function assertRecipeParameters(sceneId, selection, manifest) {
  for (const [name, value] of Object.entries(selection.parameters ?? {})) {
    const parameter = manifest.parameters.find((item) => item.name === name);
    if (!parameter) continue;
    if (typeof value !== parameter.type)
      throw new Error(`Scene ${sceneId} parameter ${name} must be ${parameter.type}.`);
    if (typeof value === "number" && (parameter.minimum !== void 0 && value < parameter.minimum || parameter.maximum !== void 0 && value > parameter.maximum))
      throw new Error(`Scene ${sceneId} parameter ${name} is outside the supported range.`);
  }
  if (manifest.id === "feature-callout") {
    const parameterValue = (name) => {
      const authored = selection.parameters?.[name];
      if (typeof authored === "number") return authored;
      const defaultValue = manifest.parameters.find((item) => item.name === name)?.default;
      return typeof defaultValue === "number" ? defaultValue : 0;
    };
    if (parameterValue("x") + parameterValue("width") > 1 || parameterValue("y") + parameterValue("height") > 1)
      throw new Error(
        `Scene ${sceneId} feature-callout rectangle must fit inside the canvas.`
      );
  }
}
function normalizeTransition(value) {
  if (!value) return void 0;
  if (typeof value === "object" && "to" in value) return void 0;
  const transition = typeof value === "string" ? { id: value } : value;
  if (!transition || typeof transition !== "object" || typeof transition.id !== "string")
    throw new Error("HyperFrames transition must have a string id.");
  const aliases = {
    fade: "crossfade",
    "fade-in": "crossfade",
    "fade-out": "crossfade",
    whip: "whip-pan",
    "whip-pan-cut": "whip-pan",
    "transition-hidden-cut": "hidden-cut",
    "panel-match-cut": "match-cut",
    "circle-match-iris": "iris",
    "iris-reveal": "iris",
    "slide-push": "push",
    "page-turn": "flip",
    "card-flip-reveal": "flip",
    "blur-push": "blur-dissolve",
    "white-flash-cut": "white-flash",
    glitch: "glitch-cut",
    "rgb-split": "chroma-split",
    "chromatic-aberration": "chroma-split",
    "light-leak-cut": "light-leak",
    "liquid-ripple": "ripple",
    cube: "cube-rotate",
    "strip-wipe": "slice-wipe"
  };
  const id = aliases[transition.id] ?? transition.id;
  if (!transitionById.has(id))
    throw new Error(`Unknown HyperFrames transition: ${transition.id}.`);
  const manifest = transitionById.get(id);
  const defaultDuration = id === "cut" ? 0 : 0.4;
  const durationSeconds = transition.durationSeconds ?? defaultDuration;
  if (!Number.isFinite(durationSeconds))
    throw new Error(`Transition ${id} duration must be finite.`);
  if (durationSeconds < manifest.durationSeconds.minimum || durationSeconds > manifest.durationSeconds.maximum)
    throw new Error(
      `Transition ${id} duration must be ${manifest.durationSeconds.minimum}-${manifest.durationSeconds.maximum}s.`
    );
  if (transition.direction !== void 0 && !["left", "right", "up", "down"].includes(transition.direction))
    throw new Error(`Transition ${id} direction is invalid.`);
  if (transition.intensity !== void 0 && (!Number.isFinite(transition.intensity) || transition.intensity < 0.1 || transition.intensity > 2))
    throw new Error(`Transition ${id} intensity must be 0.1-2.`);
  for (const axis of ["focusX", "focusY"]) {
    const value2 = transition[axis];
    if (value2 !== void 0 && (!Number.isFinite(value2) || value2 < 0 || value2 > 1))
      throw new Error(`Transition ${id} ${axis} must be between 0 and 1.`);
  }
  return { ...transition, id, durationSeconds };
}

// src/core/renderer.ts
var resolveHyperFramesBrowserPath = async () => browserPath();
var getPackagedEsbuildEnvironment = () => ({});
var execFileAsync = promisify(execFile);
var SPATIAL_BROWSER_ARGS = [
  "--enable-webgl",
  "--ignore-gpu-blocklist",
  "--use-gl=angle",
  "--use-angle=swiftshader",
  "--enable-unsafe-swiftshader",
  "--disable-gpu-compositing",
  "--font-render-hinting=none",
  "--force-color-profile=srgb",
  "--disable-background-timer-throttling",
  "--disable-backgrounding-occluded-windows",
  "--disable-renderer-backgrounding",
  "--disable-background-media-suspend"
];
var nodeRequire2 = { resolve: (id) => runtimeRequire().resolve(id) };
var AUTO_EDIT_RENDER_CAPABILITIES = {
  schemaVersion: 1,
  renderer: "hyperframes+ffmpeg-finalize",
  timeline: {
    basis: "absolute-output-seconds",
    sceneRangesMayOverlap: true,
    mediaSourceRanges: true,
    mediaPlaybackRate: true,
    rangePreview: {
      sameCompiler: true,
      wholeCompositionScale: true,
      registeredAsProjectAsset: true
    }
  },
  visualLayers: {
    media: ["video", "image", "agent-authored-motion-div"],
    renderedProperties: [
      "zIndex",
      "opacity",
      "crop",
      "style",
      "className",
      "sourceRange",
      "sourcePlaybackRate",
      "audioGainDb"
    ],
    cameraKeyframes: true,
    cropViewport: {
      cropCoordinates: "normalized-source",
      layout: "With crop present, style lays out the outer viewport; media and cursor share its inner camera.",
      cameraCoordinates: "Source-normalized focus/frame mapped into the crop, then clamped to keep the viewport covered.",
      classNameTarget: "media-element-itself"
    },
    cursorOverlay: true,
    enterExitAnimation: true,
    note: "Visual-layer enterAnimation and exitAnimation run on the layer wrapper and its hydrated cursor overlay, while camera keyframes run inside that wrapper."
  },
  motionLayers: {
    declarativeDomAndSvg: true,
    imageAssetNodes: true,
    measuredNodes: true,
    gsapTimelineMethods: ["set", "to", "fromTo"],
    gsapFeatures: ["multi-target", "stagger", "repeat", "yoyo", "SVG attributes"],
    note: "Motion layers are Agent-authored node hierarchies and timeline steps. They provide general composition primitives rather than named effects or templates."
  },
  communicationLayers: {
    captions: { style: true, className: true, enterExitAnimation: true },
    graphics: {
      text: true,
      style: true,
      className: true,
      enterExitAnimation: true,
      note: "Graphic kind, position, and animation names only create CSS classes or editorial metadata; author style, stylesheet, or explicit animation values for visible behavior."
    },
    authoredStylesheet: true
  },
  transitions: {
    transitionLabelsRendered: false,
    structuredTransitionsRendered: true,
    executableProperties: [
      "from/to GSAP property values",
      "durationSeconds",
      "easing",
      "optional audioFade",
      "overlapping absolute scene ranges"
    ],
    note: "Structured transitionIn and transitionOut execute Agent-authored from/to values. Legacy string labels and optional kind, direction, or mask descriptors remain metadata; put executable transform, opacity, clipPath, filter, or mask values in from/to."
  },
  audio: {
    visualLayerSourceAudio: true,
    voiceover: true,
    music: true,
    gainDb: true,
    finalAudioFilter: true,
    duckUnderVoiceDbRendered: false,
    note: "duckUnderVoiceDb is descriptive metadata. Use an executable finalAudioFilter or execute_ffmpeg graph when audible ducking is required."
  },
  spatial: {
    enabled: true,
    runtime: SPATIAL_RUNTIME_VERSION,
    anatomy: ANATOMY_RUNTIME_VERSION,
    three: "0.180.0",
    modelFormats: ["glb", "gltf"],
    loader: "GLTFLoader",
    procedural: ["box", "plane", "sphere", "cylinder", "cone", "line", "curve", "tube", "arrow", "gear", "shaft", "spring", "ring", "grid", "axis", "measurement", "callout", "particle-field", "flow-field", "exploded-assembly", "gear-train", "molecule", "solar-system", "product-assembly", "custom"],
    animationTracks: ["transform", "camera", "visibility", "material", "light", "path", "instance"],
    animationPresets: ["orbit", "follow-path", "explode", "assemble", "reveal-section", "highlight", "measure", "flow", "rotate", "oscillate", "pulse", "morph"],
    backends: { webgl: true, angleSwiftShader: true, canvas2dProceduralFallback: true, canvas2dModelFallback: false, anatomyCanvas2d: true },
    browserArgs: [...SPATIAL_BROWSER_ARGS],
    deterministic: { renderAt: true, requestAnimationFrame: false, wallClock: false, physics: false },
    assetPolicy: { projectLocalOnlyAtRender: true, remoteCdn: false }
  },
  presentation: {
    timelineProgress: { default: false, explicitOptIn: true },
    chapterRail: { default: true, explicitOptOut: true }
  },
  freeform: {
    css: true,
    gsapPropertyValues: true,
    ffmpegArgv: true,
    externalUrls: false,
    shellSyntax: false
  }
};
function inspectAutoEditRenderCapabilities() {
  return structuredClone(AUTO_EDIT_RENDER_CAPABILITIES);
}
function isStructuredTransition(value) {
  return Boolean(value && typeof value === "object" && "to" in value);
}
function appendAnimationConsumption(entries, path18, value, mechanism, phase) {
  if (value) entries.push({ path: path18, status: phase, mechanism });
}
function appendTransitionConsumption(entries, path18, value, phase) {
  if (!value) return;
  if (typeof value === "object" && "id" in value) {
    entries.push({ path: path18, status: phase, mechanism: "recipe-transition" });
    return;
  }
  if (typeof value === "string") {
    entries.push({
      path: path18,
      status: "metadata_only",
      mechanism: "legacy-transition-label",
      note: "Use a structured transition with executable from/to values to affect pixels."
    });
    return;
  }
  entries.push({
    path: path18,
    status: phase,
    mechanism: value.audioFade ? "gsap-scene-properties+audio-volume" : "gsap-scene-properties"
  });
  for (const property of ["kind", "direction", "mask"])
    if (value[property])
      entries.push({
        path: `${path18}/${property}`,
        status: "metadata_only",
        mechanism: "transition-description",
        note: "The descriptor is retained for intent; executable visual values come from from/to."
      });
}
function buildRenderCoverageReport(project, revision, phase) {
  const entries = [];
  if (project.stylesheet)
    entries.push({
      path: "/stylesheet",
      status: phase,
      mechanism: "authored-css"
    });
  if (project.finalAudioFilter)
    entries.push({
      path: "/finalAudioFilter",
      status: phase,
      mechanism: "ffmpeg-audio-filter"
    });
  for (const [sceneIndex, scene] of project.scenes.entries()) {
    const scenePath = `/scenes/${sceneIndex}`;
    appendTransitionConsumption(
      entries,
      `${scenePath}/transitionIn`,
      scene.transitionIn,
      phase
    );
    appendTransitionConsumption(
      entries,
      `${scenePath}/transitionOut`,
      scene.transitionOut,
      phase
    );
    appendAnimationConsumption(
      entries,
      `${scenePath}/enterAnimation`,
      scene.enterAnimation,
      "gsap-scene-wrapper",
      phase
    );
    appendAnimationConsumption(
      entries,
      `${scenePath}/exitAnimation`,
      scene.exitAnimation,
      "gsap-scene-wrapper",
      phase
    );
    for (const [layerIndex, layer] of scene.visualLayers.entries()) {
      const layerPath = `${scenePath}/visualLayers/${layerIndex}`;
      if (layer.style || layer.className)
        entries.push({
          path: layer.style ? `${layerPath}/style` : `${layerPath}/className`,
          status: phase,
          mechanism: layer.style ? "inline-css" : "authored-css-class"
        });
      if (layer.cameraMotion)
        entries.push({
          path: `${layerPath}/cameraMotion`,
          status: phase,
          mechanism: "gsap-camera-keyframes"
        });
      if (layer.audioGainDb !== void 0)
        entries.push({
          path: `${layerPath}/audioGainDb`,
          status: layer.assetPath ? phase : "ignored",
          mechanism: "hyperframes-source-media-audio",
          ...!layer.assetPath ? { note: "The visual layer has no media asset." } : {}
        });
      if (layer.cursorOverlay)
        entries.push({
          path: `${layerPath}/cursorOverlay`,
          status: layer.cursorOverlay.samples?.length ? phase : "ignored",
          mechanism: "hydrated-interaction-telemetry",
          ...!layer.cursorOverlay.samples?.length ? { note: "No hydrated cursor samples were available for this range." } : {}
        });
      appendAnimationConsumption(
        entries,
        `${layerPath}/enterAnimation`,
        layer.enterAnimation,
        "gsap-visual-wrapper",
        phase
      );
      appendAnimationConsumption(
        entries,
        `${layerPath}/exitAnimation`,
        layer.exitAnimation,
        "gsap-visual-wrapper",
        phase
      );
    }
    for (const [layerIndex, layer] of (scene.motionLayers ?? []).entries()) {
      const layerPath = `${scenePath}/motionLayers/${layerIndex}`;
      entries.push({
        path: layerPath,
        status: phase,
        mechanism: "agent-authored-dom-svg-layer"
      });
      for (const [nodeIndex, node] of layer.nodes.entries())
        entries.push({
          path: `${layerPath}/nodes/${nodeIndex}`,
          status: phase,
          mechanism: node.tag === "img" ? "authorized-image-node" : "local-dom-svg-node"
        });
      for (const [stepIndex] of layer.timeline.entries())
        entries.push({
          path: `${layerPath}/timeline/${stepIndex}`,
          status: phase,
          mechanism: "gsap-motion-layer-step"
        });
    }
    if (scene.spatial) {
      const backend = spatialBackend(scene.spatial);
      entries.push({ path: `${scenePath}/spatial/camera`, status: phase, mechanism: backend === "anatomy" ? "anatomy-isometric-renderAt-camera" : "threejs-renderAt-camera" });
      if (scene.spatial.anatomy) entries.push({ path: `${scenePath}/spatial/anatomy`, status: phase, mechanism: "anatomy-audited-canvas-painter" });
      for (const [lightIndex] of (scene.spatial.lights ?? []).entries()) entries.push({ path: `${scenePath}/spatial/lights/${lightIndex}`, status: phase, mechanism: "threejs-light" });
      for (const [modelIndex, model] of scene.spatial.models.entries()) {
        entries.push({ path: `${scenePath}/spatial/models/${modelIndex}`, status: phase, mechanism: model.assetId ? "gltf-loader-project-asset" : model.instanceOf ? "threejs-instance" : "threejs-procedural" });
        for (const [animationIndex] of (model.animations ?? []).entries()) entries.push({ path: `${scenePath}/spatial/models/${modelIndex}/animations/${animationIndex}`, status: phase, mechanism: "deterministic-spatial-keyframe" });
      }
      for (const [annotationIndex] of (scene.spatial.annotations ?? []).entries()) entries.push({ path: `${scenePath}/spatial/annotations/${annotationIndex}`, status: phase, mechanism: "projected-spatial-annotation" });
    }
    for (const [captionIndex, caption] of scene.captions.entries()) {
      const captionPath = `${scenePath}/captions/${captionIndex}`;
      if (caption.style || caption.className)
        entries.push({
          path: caption.style ? `${captionPath}/style` : `${captionPath}/className`,
          status: phase,
          mechanism: caption.style ? "inline-css" : "authored-css-class"
        });
      appendAnimationConsumption(
        entries,
        `${captionPath}/enterAnimation`,
        caption.enterAnimation,
        "gsap-caption",
        phase
      );
      appendAnimationConsumption(
        entries,
        `${captionPath}/exitAnimation`,
        caption.exitAnimation,
        "gsap-caption",
        phase
      );
    }
    for (const [graphicIndex, graphic] of (scene.graphics ?? []).entries()) {
      const graphicPath = `${scenePath}/graphics/${graphicIndex}`;
      entries.push({
        path: `${graphicPath}/animation`,
        status: "metadata_only",
        mechanism: "css-class-token",
        note: "The animation name does not move pixels without explicit style or GSAP values."
      });
      appendAnimationConsumption(
        entries,
        `${graphicPath}/enterAnimation`,
        graphic.enterAnimation,
        "gsap-graphic-body",
        phase
      );
      appendAnimationConsumption(
        entries,
        `${graphicPath}/exitAnimation`,
        graphic.exitAnimation,
        "gsap-graphic-body",
        phase
      );
    }
    if (scene.music?.duckUnderVoiceDb !== void 0)
      entries.push({
        path: `${scenePath}/music/duckUnderVoiceDb`,
        status: "metadata_only",
        mechanism: "descriptive-audio-intent",
        note: "Use structured transition audioFade, executable gain automation, or an FFmpeg mix."
      });
  }
  const counts = {
    planned: 0,
    rendered: 0,
    metadata_only: 0,
    ignored: 0
  };
  for (const entry of entries) counts[entry.status] += 1;
  return { schemaVersion: 1, projectId: project.projectId, revision, phase, entries, counts };
}
function buildRenderConsumptionReport(project, revision) {
  return buildRenderCoverageReport(project, revision, "rendered");
}
function escapeHtml2(value) {
  return value.replace(
    /[&<>"']/g,
    (character) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#039;" })[character] || character
  );
}
function safeJson(value) {
  return JSON.stringify(value).replace(/</g, "\\u003c");
}
function projectAssetUrl(filePath, projectDir) {
  const relativePath = path9.relative(projectDir, path9.resolve(filePath));
  if (!relativePath || relativePath.startsWith(`..${path9.sep}`) || path9.isAbsolute(relativePath))
    throw new Error("HyperFrames media must be staged inside the auto-edit project.");
  return relativePath.split(path9.sep).map((segment) => segment === ".." ? segment : encodeURIComponent(segment)).join("/");
}
function isPathInside(filePath, directory) {
  const relativePath = path9.relative(directory, filePath);
  return Boolean(relativePath) && !relativePath.startsWith(`..${path9.sep}`) && !path9.isAbsolute(relativePath);
}
var RENDER_INPUT_VIDEO_EXTENSIONS = /* @__PURE__ */ new Set([".mp4", ".mov", ".m4v", ".webm", ".mkv"]);
function parseFrameRateFraction(value) {
  if (!value) return 0;
  const [numerator, denominator = "1"] = value.split("/");
  const fps = Number(numerator) / Number(denominator);
  return Number.isFinite(fps) && fps > 0 ? fps : 0;
}
function shouldNormalizeRenderInput(input) {
  if (!RENDER_INPUT_VIDEO_EXTENSIONS.has(input.extension.toLowerCase())) return false;
  if (!input.nominalFps || !input.averageFps) return false;
  return Math.abs(input.nominalFps - input.averageFps) > 0.05;
}
async function probeRenderInputFrameRates(filePath) {
  try {
    const { stdout } = await execFileAsync(
      getFfprobeBinaryPath(),
      [
        "-v",
        "error",
        "-select_streams",
        "v:0",
        "-show_entries",
        "stream=r_frame_rate,avg_frame_rate",
        "-of",
        "csv=p=0",
        filePath
      ],
      { windowsHide: true, encoding: "utf8", maxBuffer: 1024 * 1024 }
    );
    const [nominal, average] = stdout.trim().split(/\r?\n/)[0]?.split(",") ?? [];
    return {
      nominalFps: parseFrameRateFraction(nominal),
      averageFps: parseFrameRateFraction(average)
    };
  } catch {
    return { nominalFps: 0, averageFps: 0 };
  }
}
async function normalizeRenderInputToConstantFrameRate(sourcePath, targetPath, fps) {
  const temporaryPath = `${targetPath}.tmp-${process.pid}.mp4`;
  await execFileAsync(
    getFfmpegBinaryPath(),
    [
      "-y",
      "-hide_banner",
      "-loglevel",
      "error",
      "-i",
      sourcePath,
      "-map",
      "0:v:0",
      "-map",
      "0:a?",
      "-vf",
      `fps=${fps}`,
      "-c:v",
      "libx264",
      "-preset",
      "veryfast",
      "-crf",
      "18",
      "-g",
      String(fps),
      "-keyint_min",
      String(fps),
      "-pix_fmt",
      "yuv420p",
      "-c:a",
      "aac",
      "-b:a",
      "192k",
      "-movflags",
      "+faststart",
      temporaryPath
    ],
    { windowsHide: true, maxBuffer: 16 * 1024 * 1024 }
  );
  await fs7.rename(temporaryPath, targetPath);
}
var renderInputPreparations = /* @__PURE__ */ new Map();
async function stageHyperFramesAsset(filePath, projectDir, fps, normalizeVideo = true) {
  const absolutePath = path9.resolve(filePath);
  const source = await fs7.stat(absolutePath);
  if (!source.isFile()) throw new Error("HyperFrames media input is not a regular file.");
  const extension = path9.extname(absolutePath).toLowerCase();
  const stagingDirectory = path9.join(projectDir, "assets", "render-inputs");
  const identity = createHash4("sha256").update(`${absolutePath}\0${source.size}\0${source.mtimeMs}`).digest("hex").slice(0, 24);
  const normalizedPath = path9.join(stagingDirectory, `media-${identity}-cfr${fps}.mp4`);
  const bytes = source.size;
  if (normalizeVideo && RENDER_INPUT_VIDEO_EXTENSIONS.has(extension)) {
    const inFlight = renderInputPreparations.get(normalizedPath);
    if (inFlight) {
      await inFlight;
      return { path: normalizedPath, action: "cfr-cached", bytes };
    }
    if (await fileExists(normalizedPath))
      return { path: normalizedPath, action: "cfr-cached", bytes };
    const frameRates = await probeRenderInputFrameRates(absolutePath);
    if (shouldNormalizeRenderInput({ extension, ...frameRates })) {
      await fs7.mkdir(stagingDirectory, { recursive: true });
      const job = normalizeRenderInputToConstantFrameRate(absolutePath, normalizedPath, fps);
      renderInputPreparations.set(
        normalizedPath,
        job.catch(() => void 0).finally(() => renderInputPreparations.delete(normalizedPath))
      );
      await job;
      return { path: normalizedPath, action: "cfr-normalized", bytes };
    }
  }
  if (isPathInside(absolutePath, projectDir))
    return { path: absolutePath, action: "in-place", bytes };
  const stagedPath = path9.join(stagingDirectory, `media-${identity}${extension}`);
  await fs7.mkdir(stagingDirectory, { recursive: true });
  try {
    await fs7.link(absolutePath, stagedPath);
    return { path: stagedPath, action: "linked", bytes };
  } catch (error) {
    const code = error.code;
    if (code === "EEXIST") return { path: stagedPath, action: "existing", bytes };
    if (!["EXDEV", "EPERM", "EACCES", "ENOTSUP"].includes(code ?? "")) throw error;
    await fs7.copyFile(absolutePath, stagedPath);
    return { path: stagedPath, action: "copied", bytes };
  }
}
async function fileExists(filePath) {
  try {
    return (await fs7.stat(filePath)).isFile();
  } catch {
    return false;
  }
}
async function hyperFramesAssetUrls(project, projectDir, renderRange, normalizeVideo = true, onAssetStaged) {
  const paths = /* @__PURE__ */ new Set();
  for (const [index, scene] of project.scenes.entries()) {
    if (scene.voiceover?.assetPath && (!renderRange || intersectTimeRange(scene.voiceover.range, renderRange)))
      paths.add(scene.voiceover.assetPath);
    if (scene.music?.assetPath && (!renderRange || intersectTimeRange(scene.music.range, renderRange)))
      paths.add(scene.music.assetPath);
    for (const soundEffect of scene.soundEffects ?? [])
      if (soundEffect.assetPath && (!renderRange || intersectTimeRange(soundEffect.range, renderRange)))
        paths.add(soundEffect.assetPath);
    const before = index > 0 ? transitionOverlapSeconds(transitionAtBoundary(project.scenes[index - 1], scene)) : 0;
    const after = index < project.scenes.length - 1 ? transitionOverlapSeconds(transitionAtBoundary(scene, project.scenes[index + 1])) : 0;
    if (renderRange && !intersectTimeRange(
      { start: scene.range.start - before, end: scene.range.end + after },
      renderRange
    ))
      continue;
    for (const visual of scene.visualLayers) if (visual.assetPath) paths.add(visual.assetPath);
    for (const model of scene.spatial?.models ?? []) if (model.assetPath) paths.add(model.assetPath);
    for (const layer of scene.motionLayers ?? []) {
      if (renderRange && !intersectTimeRange(layer.range, renderRange)) continue;
      for (const node of layer.nodes) if (node.assetPath) paths.add(node.assetPath);
    }
  }
  return new Map(
    await Promise.all(
      [...paths].map(async (filePath) => {
        const startedAt = Date.now();
        const staged = await stageHyperFramesAsset(
          filePath,
          projectDir,
          project.fps,
          normalizeVideo
        );
        onAssetStaged?.({
          fileName: path9.basename(filePath),
          action: staged.action,
          durationMs: Date.now() - startedAt,
          bytes: staged.bytes
        });
        return [path9.resolve(filePath), projectAssetUrl(staged.path, projectDir)];
      })
    )
  );
}
function seconds2(value) {
  return Number(value.toFixed(4));
}
function intersectTimeRange(left, right) {
  const start = Math.max(left.start, right.start);
  const end = Math.min(left.end, right.end);
  return end - start > 1e-4 ? { start, end } : null;
}
function sourceContainViewport(layer, scene, width, height) {
  if (!(layer.source === "source-video" || layer.source === "original" || layer.assetId === "source-video") || layer.crop || layer.cameraMotion || layer.style?.objectFit || CAMERA_MOVING_RECIPES.has(scene.recipe?.id ?? "") || LIFT_RECIPE_IDS.has(scene.recipe?.id ?? "") || !layer.mediaWidth || !layer.mediaHeight)
    return null;
  const scale = Math.min(width / layer.mediaWidth, height / layer.mediaHeight);
  const fitWidth = layer.mediaWidth * scale;
  const fitHeight = layer.mediaHeight * scale;
  return {
    width: fitWidth,
    height: fitHeight,
    left: (width - fitWidth) / 2,
    top: (height - fitHeight) / 2
  };
}
function coverSafeCameraKeyframe(keyframe, overflow = { x: 1, y: 1 }) {
  return resolveCameraKeyframe(keyframe, overflow);
}
function cameraTransform(rawKeyframe, width, height, withFilter = false, overflow = { x: 1, y: 1 }) {
  const keyframe = coverSafeCameraKeyframe(rawKeyframe, overflow);
  return {
    scale: seconds2(keyframe.scale),
    x: seconds2(-keyframe.scale * width * overflow.x * (keyframe.focusX - 0.5)),
    y: seconds2(-keyframe.scale * height * overflow.y * (keyframe.focusY - 0.5)),
    rotation: seconds2(keyframe.rotate ?? 0),
    ...withFilter ? { filter: `blur(${seconds2(keyframe.blur ?? 0)}px)` } : {}
  };
}
function decibelsToAmplitude(decibels) {
  return seconds2(10 ** ((decibels ?? 0) / 20));
}
function cssPropertyName(value) {
  return value.replace(/[A-Z]/g, (character) => `-${character.toLowerCase()}`);
}
function assertSafeCssValue(value) {
  if (/@import|url\s*\(|expression\s*\(|javascript\s*:|behavior\s*:/i.test(value))
    throw new Error("VideoProject CSS cannot load external or executable content.");
}
function styleAttribute(style) {
  if (!style) return "";
  const declarations = Object.entries(style).map(([property, value]) => {
    if (!/^--?[a-zA-Z0-9_-]+$/.test(property) && !/^[a-zA-Z][a-zA-Z0-9_-]*$/.test(property))
      throw new Error(`Invalid CSS property: ${property}.`);
    const serialized = String(value);
    assertSafeCssValue(serialized);
    return `${cssPropertyName(property)}:${serialized}`;
  });
  return declarations.length ? ` style="${escapeHtml2(declarations.join(";"))}"` : "";
}
var CAPTION_BOX_STYLE_KEYS = /* @__PURE__ */ new Set([
  "left",
  "top",
  "right",
  "bottom",
  "width",
  "height",
  "zIndex",
  "opacity",
  "transform",
  "transformOrigin",
  "translate",
  "scale",
  "rotate",
  "filter",
  "clipPath",
  "mixBlendMode",
  "willChange"
]);
function splitCaptionStyle(style) {
  const box = {};
  const text = {};
  for (const [key, value] of Object.entries(style ?? {}))
    (CAPTION_BOX_STYLE_KEYS.has(key) ? box : text)[key] = value;
  const align = String(text.textAlign ?? "center").toLowerCase();
  box.justifyContent = align === "left" || align === "start" ? "flex-start" : align === "right" || align === "end" ? "flex-end" : "center";
  return { box, text };
}
function classAttribute(base, authored) {
  const authoredClasses = (authored ?? "").split(/\s+/).filter((value) => /^[a-zA-Z0-9_-]+$/.test(value));
  return escapeHtml2([base, ...authoredClasses].join(" "));
}
function motionNodeDomId(sceneIndex, layerIndex, nodeIndex) {
  return `motion-node-${sceneIndex}-${layerIndex}-${nodeIndex}`;
}
function safeMotionAttributeName(value) {
  if (!/^[a-zA-Z_][a-zA-Z0-9_.:-]*$/.test(value))
    throw new Error(`Invalid motion node attribute: ${value}.`);
  const normalized = value.toLowerCase();
  if (normalized === "src" || normalized === "href" || normalized === "xlink:href" || normalized === "style" || normalized.startsWith("on"))
    throw new Error(`Motion node attribute is not permitted: ${value}.`);
  return value;
}
function motionAttributes(attributes) {
  if (!attributes) return "";
  return Object.entries(attributes).map(([name, value]) => {
    const safeName = safeMotionAttributeName(name);
    const serialized = String(value);
    if (/javascript\s*:|https?\s*:|file\s*:|data\s*:/i.test(serialized))
      throw new Error(
        "Motion node attributes cannot load external or executable content."
      );
    return ` ${safeName}="${escapeHtml2(serialized)}"`;
  }).join("");
}
function motionNodeMarkup(layer, sceneIndex, layerIndex, assetUrl) {
  const indexById = new Map(layer.nodes.map((node, index) => [node.id, index]));
  const children = /* @__PURE__ */ new Map();
  for (const node of layer.nodes) {
    const siblings = children.get(node.parentId) ?? [];
    siblings.push(node);
    children.set(node.parentId, siblings);
  }
  const renderNode = (node) => {
    const nodeIndex = indexById.get(node.id);
    if (nodeIndex === void 0) throw new Error("Motion node identity is unavailable.");
    const id = motionNodeDomId(sceneIndex, layerIndex, nodeIndex);
    const body2 = `${node.text === void 0 ? "" : escapeHtml2(node.text)}${(children.get(node.id) ?? []).map(renderNode).join("")}`;
    const measurement = node.measure ? ` data-motion-measure="true" data-motion-role="${escapeHtml2(node.semanticRole ?? "motion")}"` : "";
    const common = ` id="${id}" data-motion-node-id="${escapeHtml2(node.id)}" class="${classAttribute("motion-node", node.className)}"${styleAttribute(node.style)}${motionAttributes(node.attributes)}${measurement}`;
    if (node.tag === "img") {
      if (!node.assetPath) throw new Error("Motion image asset was not bound.");
      return `<img${common} src="${escapeHtml2(assetUrl(node.assetPath))}" alt="" />`;
    }
    const svgNamespace = node.tag === "svg" ? ' xmlns="http://www.w3.org/2000/svg"' : "";
    return `<${node.tag}${common}${svgNamespace}>${body2}</${node.tag}>`;
  };
  return (children.get(void 0) ?? []).map(renderNode).join("");
}
function motionTweenValues(state) {
  for (const value of Object.values(state.style ?? {})) assertSafeCssValue(String(value));
  for (const [name, value] of Object.entries(state.attributes ?? {})) {
    safeMotionAttributeName(name);
    if (/javascript\s*:|https?\s*:|file\s*:|data\s*:/i.test(String(value)))
      throw new Error("Motion timeline attributes cannot load external content.");
  }
  return {
    ...state.style ?? {},
    ...state.attributes ? { attr: state.attributes } : {}
  };
}
function motionTimelineStatement(step, layer, sceneIndex, layerIndex) {
  const indexById = new Map(layer.nodes.map((node, index) => [node.id, index]));
  const selector = step.targetIds.map((id) => {
    const nodeIndex = indexById.get(id);
    if (nodeIndex === void 0) throw new Error(`Unknown motion timeline target: ${id}.`);
    return `#${motionNodeDomId(sceneIndex, layerIndex, nodeIndex)}`;
  }).join(",");
  const atSeconds = seconds2(layer.range.start + step.atSeconds);
  const to = {
    ...motionTweenValues(step.to),
    ...step.method === "set" ? {} : { duration: seconds2(step.durationSeconds) },
    ...step.easing ? { ease: step.easing } : {},
    ...step.staggerSeconds !== void 0 ? { stagger: seconds2(step.staggerSeconds) } : {},
    ...step.repeat !== void 0 ? { repeat: step.repeat } : {},
    ...step.yoyo !== void 0 ? { yoyo: step.yoyo } : {}
  };
  if (step.method === "set") return `tl.set(${safeJson(selector)},${safeJson(to)},${atSeconds});`;
  if (step.method === "fromTo")
    return `tl.fromTo(${safeJson(selector)},${safeJson(motionTweenValues(step.from))},${safeJson(to)},${atSeconds});`;
  return `tl.to(${safeJson(selector)},${safeJson(to)},${atSeconds});`;
}
function cropStyle(crop) {
  if (!crop) return {};
  return {
    position: "absolute",
    width: `${seconds2(100 / crop.width)}%`,
    height: `${seconds2(100 / crop.height)}%`,
    left: `${seconds2(-100 * crop.x / crop.width)}%`,
    top: `${seconds2(-100 * crop.y / crop.height)}%`
  };
}
function animationStatement(target, animation, atSeconds) {
  const to = {
    ...animation.to,
    duration: seconds2(animation.durationSeconds),
    ...animation.easing ? { ease: animation.easing } : {}
  };
  return animation.from ? `tl.fromTo(${safeJson(target)},${safeJson(animation.from)},${safeJson(to)},${seconds2(atSeconds)});` : `tl.to(${safeJson(target)},${safeJson(to)},${seconds2(atSeconds)});`;
}
function appendAudioTransitionStatements(scene, sceneIndex, transition, phase, timeline, renderRange) {
  if (!isStructuredTransition(transition) || !transition.audioFade) return;
  const audioTargets = [
    ...[...scene.visualLayers].sort((left, right) => left.zIndex - right.zIndex).flatMap(
      (layer, layerIndex) => layer.assetPath && layer.audioGainDb !== void 0 ? [
        {
          selector: `#audio-visual-${sceneIndex}-${layerIndex}`,
          range: scene.range,
          volume: decibelsToAmplitude(layer.audioGainDb)
        }
      ] : []
    ),
    scene.voiceover?.assetPath ? {
      selector: `#audio-voiceover-${sceneIndex}`,
      range: scene.voiceover.range,
      volume: decibelsToAmplitude(scene.voiceover.gainDb)
    } : null,
    scene.music?.assetPath ? {
      selector: `#audio-music-${sceneIndex}`,
      range: scene.music.range,
      volume: decibelsToAmplitude(scene.music.gainDb)
    } : null
  ].filter(
    (value) => Boolean(value && (!renderRange || intersectTimeRange(value.range, renderRange)))
  );
  for (const target of audioTargets) {
    if (phase === "in") {
      const start = Math.max(scene.range.start, target.range.start);
      const end = Math.min(scene.range.start + transition.durationSeconds, target.range.end);
      if (end <= start) continue;
      timeline.push(
        `tl.set(${safeJson(target.selector)},{volume:0},${seconds2(start)});`,
        `tl.to(${safeJson(target.selector)},{volume:${target.volume},duration:${seconds2(end - start)},ease:${safeJson(transition.easing ?? "none")}},${seconds2(start)});`
      );
    } else {
      const end = Math.min(scene.range.end, target.range.end);
      const start = Math.max(target.range.start, end - transition.durationSeconds);
      if (end <= start) continue;
      timeline.push(
        `tl.to(${safeJson(target.selector)},{volume:0,duration:${seconds2(end - start)},ease:${safeJson(transition.easing ?? "none")}},${seconds2(start)});`
      );
    }
  }
}
function authoredStylesheet(value) {
  if (!value) return "";
  assertSafeCssValue(value);
  if (/<\/style/i.test(value))
    throw new Error("VideoProject stylesheet contains invalid markup.");
  return value;
}
function resolveGsapBundle() {
  return nodeRequire2.resolve("gsap/dist/gsap.min.js");
}
function resolveSpatialRuntimeBundle() {
  const candidates = [
    path9.join(PLUGIN_ROOT, "dist", "spatial-runtime.mjs"),
    path9.join(path9.dirname(process.argv[1] ?? ""), "spatial-runtime.mjs"),
    path9.resolve(process.cwd(), "dist", "spatial-runtime.mjs")
  ];
  for (const candidate of candidates) {
    if (existsSync2(candidate)) return candidate;
  }
  return candidates[0];
}
function resolveAnatomyRuntimeBundle() {
  const candidates = [
    path9.join(PLUGIN_ROOT, "dist", "anatomy-runtime.mjs"),
    path9.join(path9.dirname(process.argv[1] ?? ""), "anatomy-runtime.mjs"),
    path9.resolve(process.cwd(), "dist", "anatomy-runtime.mjs")
  ];
  for (const candidate of candidates) {
    if (existsSync2(candidate)) return candidate;
  }
  return candidates[0];
}
function recipeNumber(recipe, name, fallback) {
  const value = recipe?.parameters?.[name];
  return typeof value === "number" && Number.isFinite(value) ? value : fallback;
}
var OVERLAP_TRANSITIONS = /* @__PURE__ */ new Set([
  "crossfade",
  "whip-pan",
  "zoom-through",
  "match-cut",
  "hidden-cut",
  "iris",
  "push",
  "flip",
  "blur-dissolve",
  "wipe",
  "white-flash",
  "glitch-cut",
  "light-leak",
  "ripple",
  "cube-rotate",
  "slice-wipe",
  "chroma-split"
]);
var CAMERA_MOVING_RECIPES = /* @__PURE__ */ new Set([
  "element-lift",
  "layer-explode",
  "depth-parallax",
  "ui-focus-zoom",
  "panel-expansion",
  "crash-zoom-punch",
  "click-zoom-punch",
  "pressure-push",
  "dutch-roll-level",
  "pull-back-isolation",
  "skeleton-reveal"
]);
var SCENE_TRACK_SPAN = 40;
var GRAPHIC_TRACK = 5100;
var CAPTION_TRACK = 5200;
var RECIPE_OVERLAY_TRACK = 5300;
var TRANSITION_TRACK = 9e3;
var SCENE_STACK = {
  background: 10,
  footage: 100,
  cursor: 200,
  overlay: 300,
  caption: 500,
  graphic: 600
};
function motionLayerStack(scene) {
  const layers = scene.motionLayers ?? [];
  const minVisual = scene.visualLayers.length ? Math.min(...scene.visualLayers.map((layer) => layer.zIndex)) : 0;
  const order = layers.map((layer, index) => ({ layer, index })).sort((left, right) => left.layer.zIndex - right.layer.zIndex);
  const result = new Array(layers.length).fill(SCENE_STACK.overlay);
  let backgrounds = 0;
  let overlays = 0;
  for (const { layer, index } of order) {
    const background = scene.visualLayers.length ? layer.zIndex < minVisual : layer.zIndex <= 0;
    result[index] = background ? SCENE_STACK.background + Math.min(backgrounds++, 89) : SCENE_STACK.overlay + Math.min(overlays++, 199);
  }
  return result;
}
function killProcessTree(child) {
  if (process.platform === "win32" && child.pid) {
    try {
      const killer = spawn2(
        path9.join(process.env.SystemRoot ?? "C:\\Windows", "System32", "taskkill.exe"),
        ["/PID", String(child.pid), "/T", "/F"],
        { windowsHide: true, stdio: "ignore" }
      );
      killer.on("error", () => child.kill());
      killer.unref();
      return;
    } catch {
    }
  }
  child.kill("SIGKILL");
}
function sceneTrack(sceneIndex, offset) {
  return sceneIndex * SCENE_TRACK_SPAN + offset;
}
function createClipTrackAllocator(base, capacity = 100) {
  const lanes = [];
  return (range) => {
    let index = lanes.findIndex(
      (ranges) => ranges.every((other) => range.end <= other.start || range.start >= other.end)
    );
    if (index < 0) {
      if (lanes.length >= capacity)
        throw new Error("Too many overlapping clips in one render track group.");
      index = lanes.push([]) - 1;
    }
    lanes[index].push({ ...range });
    return base + index;
  };
}
var BREATHE_SCALE = 1.025;
var BREATHE_DRIFT_RATIO = 4e-3;
function typographyMarkup(text) {
  const tokens = /\s/.test(text.trim()) ? text.split(/(\s+)/) : Array.from(text);
  return tokens.filter((token) => token.length > 0).map(
    (token) => /^\s+$/.test(token) ? escapeHtml2(token) : `<span class="word">${escapeHtml2(token)}</span>`
  ).join("");
}
function overlayFrameStyle(project) {
  return styleAttribute({
    left: "0px",
    top: "0px",
    width: `${project.width}px`,
    height: `${project.height}px`
  });
}
function graphicInnerMarkup(recipeId, text) {
  switch (recipeId) {
    case "title-blur-slide":
      return typographyMarkup(text);
    case "split-flap-title":
      return Array.from(text).map(
        (character) => /\s/.test(character) ? escapeHtml2(character) : `<span class="flap"><b data-char="${escapeHtml2(character)}">${escapeHtml2(character)}</b></span>`
      ).join("");
    case "typewriter-reveal":
      return `${Array.from(text).map((character) => `<span class="tw">${escapeHtml2(character)}</span>`).join("")}<i class="tw-caret"></i>`;
    case "odometer-digit-roll":
      return Array.from(text).map(
        (character) => /[0-9]/.test(character) ? `<span class="odo"><span class="odo-strip" data-digit="${character}">${"0123456789".split("").map((digit) => `<i>${digit}</i>`).join("")}</span></span>` : `<span class="odo-static">${escapeHtml2(character)}</span>`
      ).join("");
    case "metric-counter": {
      const match = /(\d[\d,]*(?:\.\d+)?)/.exec(text);
      if (!match) return escapeHtml2(text);
      const raw = match[1];
      const numeric = raw.replace(/,/g, "");
      const decimals = numeric.includes(".") ? numeric.split(".")[1].length : 0;
      return `${escapeHtml2(text.slice(0, match.index))}<span class="counter" data-target="${escapeHtml2(numeric)}" data-decimals="${decimals}">${escapeHtml2(raw)}</span>${escapeHtml2(text.slice(match.index + raw.length))}`;
    }
    case "list-reveal":
      return `<i class="list-marker"></i>${escapeHtml2(text)}`;
    default:
      return escapeHtml2(text);
  }
}
var CLIP_PATH_WIPE_FROM = {
  left: "inset(0 100% 0 0)",
  right: "inset(0 0 0 100%)",
  up: "inset(100% 0 0 0)",
  down: "inset(0 0 100% 0)"
};
function applyExtendedTransition(transition, index, current, timeline) {
  const boundary = current.range.start;
  const duration = transition.durationSeconds ?? 0.4;
  const half = duration / 2;
  const direction = transition.direction ?? "left";
  const axis = direction === "left" || direction === "right" ? "xPercent" : "yPercent";
  const sign = direction === "right" || direction === "down" ? 1 : -1;
  const outgoing = `#scene-${index}`;
  const incoming = `#scene-${index + 1}`;
  const overlay = `#transition-${index}`;
  switch (transition.id) {
    case "iris": {
      const focusX = seconds2((transition.focusX ?? 0.5) * 100);
      const focusY = seconds2((transition.focusY ?? 0.5) * 100);
      timeline.push(
        `tl.set(${safeJson(incoming)},${safeJson({ clipPath: `circle(0% at ${focusX}% ${focusY}%)` })},${seconds2(boundary - half)});`,
        `tl.to(${safeJson(incoming)},${safeJson({ clipPath: `circle(150% at ${focusX}% ${focusY}%)`, duration: seconds2(duration), ease: "power3.inOut" })},${seconds2(boundary - half)});`,
        `tl.set(${safeJson(incoming)},${safeJson({ clipPath: "none" })},${seconds2(boundary + half + 0.01)});`
      );
      return true;
    }
    case "push":
      timeline.push(
        `tl.set(${safeJson(incoming)},${safeJson({ [axis]: sign * 100 })},${seconds2(boundary - half)});`,
        `tl.to(${safeJson(outgoing)},${safeJson({ [axis]: sign * -100, duration: seconds2(duration), ease: "power3.inOut" })},${seconds2(boundary - half)});`,
        `tl.to(${safeJson(incoming)},${safeJson({ [axis]: 0, duration: seconds2(duration), ease: "power3.inOut" })},${seconds2(boundary - half)});`
      );
      return true;
    case "flip":
      timeline.push(
        `tl.set("#composition-root",${safeJson({ perspective: 1600 })},${seconds2(boundary - half)});`,
        `tl.set(${safeJson(incoming)},${safeJson({ rotationY: sign * 90, transformOrigin: "50% 50%" })},${seconds2(boundary - half)});`,
        `tl.to(${safeJson(outgoing)},${safeJson({ rotationY: sign * -90, transformOrigin: "50% 50%", duration: seconds2(half), ease: "power2.in" })},${seconds2(boundary - half)});`,
        `tl.to(${safeJson(incoming)},${safeJson({ rotationY: 0, duration: seconds2(half), ease: "power2.out" })},${seconds2(boundary)});`
      );
      return true;
    case "blur-dissolve":
      timeline.push(
        `tl.set(${safeJson(incoming)},${safeJson({ opacity: 0, filter: "blur(16px)" })},${seconds2(boundary - half)});`,
        `tl.to(${safeJson(outgoing)},${safeJson({ opacity: 0, filter: "blur(16px)", duration: seconds2(duration), ease: "power1.inOut" })},${seconds2(boundary - half)});`,
        `tl.to(${safeJson(incoming)},${safeJson({ opacity: 1, filter: "blur(0px)", duration: seconds2(duration), ease: "power1.inOut" })},${seconds2(boundary - half)});`
      );
      return true;
    case "wipe":
      timeline.push(
        `tl.set(${safeJson(incoming)},${safeJson({ clipPath: CLIP_PATH_WIPE_FROM[direction] })},${seconds2(boundary - half)});`,
        `tl.to(${safeJson(incoming)},${safeJson({ clipPath: "inset(0% 0% 0% 0%)", duration: seconds2(duration), ease: "power3.inOut" })},${seconds2(boundary - half)});`,
        `tl.set(${safeJson(incoming)},${safeJson({ clipPath: "none" })},${seconds2(boundary + half + 0.01)});`
      );
      return true;
    case "white-flash":
      timeline.push(
        `tl.set(${safeJson(incoming)},${safeJson({ opacity: 0 })},${seconds2(boundary - half)});`,
        `tl.fromTo(${safeJson(overlay)},${safeJson({ opacity: 0 })},${safeJson({ opacity: 1, duration: seconds2(half), ease: "power2.in" })},${seconds2(boundary - half)});`,
        `tl.set(${safeJson(incoming)},${safeJson({ opacity: 1 })},${seconds2(boundary)});`,
        `tl.to(${safeJson(overlay)},${safeJson({ opacity: 0, duration: seconds2(half), ease: "power3.out" })},${seconds2(boundary)});`
      );
      return true;
    default:
      return false;
  }
}
function recipeOverlayMarkup(scene, sceneIndex, project, renderRange) {
  const id = scene.recipe?.id;
  if (!id) return "";
  const visible = intersectTimeRange(scene.range, renderRange);
  if (!visible) return "";
  const overlayId = `recipe-overlay-${sceneIndex}`;
  const clipAttributes = `data-start="${seconds2(visible.start - renderRange.start)}" data-duration="${seconds2(visible.end - visible.start)}" data-track-index="${RECIPE_OVERLAY_TRACK}"`;
  if (id === "product-hero-spotlight")
    return `<div id="${overlayId}" class="clip recipe-overlay recipe-spotlight" ${clipAttributes} aria-hidden="true"></div>`;
  if (id === "feature-callout") {
    const x = recipeNumber(scene.recipe, "x", 0.58);
    const y = recipeNumber(scene.recipe, "y", 0.24);
    const width = recipeNumber(scene.recipe, "width", 0.28);
    const height = recipeNumber(scene.recipe, "height", 0.28);
    return `<div id="${overlayId}" class="clip recipe-overlay recipe-callout" ${clipAttributes} style="left:${seconds2(x * 100)}%;top:${seconds2(y * 100)}%;width:${seconds2(width * 100)}%;height:${seconds2(height * 100)}%" aria-hidden="true"><span></span></div>`;
  }
  if (id === "step-process-rail" && project.presentation?.showChapterRail !== false)
    return `<div id="${overlayId}" class="clip recipe-overlay recipe-step-rail" ${clipAttributes} aria-hidden="true"><b>1</b><b>2</b><b>3</b></div>`;
  if (id === "before-after-split")
    return `<div id="${overlayId}" class="clip recipe-overlay recipe-comparison-divider" ${clipAttributes} aria-hidden="true"><span></span></div>`;
  if (id === "problem-pressure")
    return `<div id="${overlayId}" class="clip recipe-overlay recipe-pressure-vignette" ${clipAttributes} aria-hidden="true"></div>`;
  const frameRect = overlayFrameStyle(project);
  if (id === "pressure-push")
    return `<div id="${overlayId}" class="clip recipe-overlay recipe-push-vignette" ${clipAttributes} aria-hidden="true"></div>`;
  if (id === "impact-feedback")
    return `<div id="${overlayId}" class="clip recipe-overlay recipe-impact-flash" ${clipAttributes} aria-hidden="true"></div>`;
  if (id === "glint-sweep") {
    const width = recipeNumber(scene.recipe, "width", 0.22);
    return `<div id="${overlayId}" class="clip recipe-overlay recipe-glint" ${clipAttributes}${frameRect} aria-hidden="true"><span style="--glint-width:${seconds2(width * 100)}%"></span></div>`;
  }
  if (id === "spotlight-sweep")
    return `<div id="${overlayId}" class="clip recipe-overlay recipe-sweep-mask" ${clipAttributes}${frameRect} aria-hidden="true"></div>`;
  if (id === "skeleton-reveal") {
    const rows = [
      [8, 62],
      [22, 88],
      [36, 74],
      [50, 90],
      [64, 55],
      [78, 80]
    ].map(([top, width]) => `<i style="top:${top}%;width:${width}%"></i>`).join("");
    return `<div id="${overlayId}" class="clip recipe-overlay recipe-skeleton" ${clipAttributes}${frameRect} aria-hidden="true">${rows}</div>`;
  }
  if (id === "brand-frame-snap")
    return `<div id="${overlayId}" class="clip recipe-overlay recipe-brand-frame" ${clipAttributes} aria-hidden="true"><i class="bf-top"></i><i class="bf-right"></i><i class="bf-bottom"></i><i class="bf-left"></i></div>`;
  if (id === "scanline-annotate-focus") {
    const x = recipeNumber(scene.recipe, "x", 0.3);
    const y = recipeNumber(scene.recipe, "y", 0.3);
    const width = recipeNumber(scene.recipe, "width", 0.4);
    const height = recipeNumber(scene.recipe, "height", 0.3);
    return `<div id="${overlayId}" class="clip recipe-overlay recipe-scan" ${clipAttributes}${frameRect} aria-hidden="true"><i class="scan-line"></i><div class="scan-target" style="left:${seconds2(x * 100)}%;top:${seconds2(y * 100)}%;width:${seconds2(width * 100)}%;height:${seconds2(height * 100)}%"><b class="c1"></b><b class="c2"></b><b class="c3"></b><b class="c4"></b></div></div>`;
  }
  return "";
}
function timelineProgressMarkup(project, renderRange, timeline) {
  if (project.presentation?.showTimelineProgress !== true) return "";
  const duration = renderRange.end - renderRange.start;
  if (!(duration > 0)) return "";
  const start = seconds2(0);
  const end = seconds2(duration);
  timeline.push(`tl.fromTo("#wandeo-timeline-progress-fill",{width:"0%"},{width:"100%",duration:${end},ease:"none"},${start});`);
  return `<div id="wandeo-timeline-progress" class="clip wandeo-timeline-progress" data-start="0" data-duration="${end}" aria-hidden="true"><i id="wandeo-timeline-progress-fill"></i></div>`;
}
function applyShotRecipe(scene, sceneIndex, timeline, context) {
  if (!scene.recipe) return;
  const manifest = getShotRecipe(scene.recipe.id);
  if (!manifest) throw new Error(`Unknown shot recipe: ${scene.recipe.id}.`);
  const start = scene.range.start;
  const duration = scene.range.end - scene.range.start;
  const intensity = recipeNumber(scene.recipe, "intensity", 1);
  const sceneTarget = `#scene-${sceneIndex}`;
  const overlayTarget = `#recipe-overlay-${sceneIndex}`;
  const orderedVisualLayers = [...scene.visualLayers].sort(
    (left, right) => left.zIndex - right.zIndex
  );
  const visualTargets = orderedVisualLayers.map(
    (layer, layerIndex) => layer.cursorOverlay && !layer.crop ? `#visual-clip-${sceneIndex}-${layerIndex},#cursor-clip-${sceneIndex}-${layerIndex}` : `#visual-clip-${sceneIndex}-${layerIndex}`
  );
  const cameraTargets = orderedVisualLayers.map(
    (layer, layerIndex) => layer.cursorOverlay && !layer.crop ? `#camera-${sceneIndex}-${layerIndex},#cursor-camera-${sceneIndex}-${layerIndex}` : `#camera-${sceneIndex}-${layerIndex}`
  );
  const graphics = scene.graphics ?? [];
  const floatLoop = (target, amplitude, from) => {
    const period = 2.4;
    const cycles = Math.floor((duration - from) / period);
    if (cycles < 1) return;
    timeline.push(
      `tl.to(${safeJson(target)},${safeJson({ y: -amplitude, duration: period / 2, yoyo: true, repeat: cycles * 2 - 1, ease: "sine.inOut" })},${seconds2(start + from)});`
    );
  };
  switch (manifest.id) {
    case "product-hero-spotlight": {
      const entrance = Math.min(1.2, duration * 0.32);
      timeline.push(
        `tl.fromTo(${safeJson(visualTargets[0])},${safeJson({ opacity: 0, scale: 0.9, y: 50 * intensity })},${safeJson({ opacity: 1, scale: 1, y: 0, duration: seconds2(entrance), ease: "expo.out" })},${seconds2(start)});`,
        `tl.fromTo(${safeJson(overlayTarget)},${safeJson({ opacity: 0, scale: 0.65 })},${safeJson({ opacity: 0.82, scale: 1, duration: seconds2(Math.min(1.4, duration * 0.38)), ease: "power2.out" })},${seconds2(start)});`,
        `tl.to(${safeJson(overlayTarget)},${safeJson({ x: 60 * intensity, y: -30 * intensity, duration: seconds2(duration), ease: "sine.inOut" })},${seconds2(start)});`
      );
      floatLoop(visualTargets[0], 6 * intensity, entrance);
      break;
    }
    case "browser-fly-in": {
      const target = visualTargets[0];
      const entrance = Math.min(1.1, duration * 0.42);
      timeline.push(
        `tl.set(${safeJson(sceneTarget)},${safeJson({ perspective: 1600 })},${seconds2(start)});`,
        `tl.fromTo(${safeJson(target)},${safeJson({ opacity: 0, y: 140 * intensity, scale: 0.86, rotationX: 11 * intensity })},${safeJson({ opacity: 1, y: 0, scale: 1, rotationX: 0, duration: seconds2(entrance), ease: "expo.out" })},${seconds2(start)});`
      );
      floatLoop(target, 5 * intensity, entrance);
      break;
    }
    case "ui-focus-zoom":
      if (!scene.visualLayers[0]?.cameraMotion) {
        const scale = recipeNumber(scene.recipe, "scale", 1.35);
        timeline.push(
          `tl.fromTo(${safeJson(cameraTargets[0])},${safeJson({ scale: 1, x: 0, y: 0 })},${safeJson({ scale, x: 0, y: 0, duration: seconds2(Math.min(1.4, duration * 0.38)), ease: "power2.inOut" })},${seconds2(start + duration * 0.15)});`
        );
      }
      break;
    case "feature-callout": {
      const entrance = start + duration * 0.18;
      timeline.push(
        `tl.fromTo(${safeJson(overlayTarget)},${safeJson({ opacity: 0, scale: 0.88 })},${safeJson({ opacity: 1, scale: 1, duration: seconds2(Math.min(0.5, duration * 0.2)), ease: "back.out(1.6)" })},${seconds2(entrance)});`
      );
      const pulses = Math.floor((duration - duration * 0.18 - 0.6) / 1.3);
      if (pulses >= 1)
        timeline.push(
          `tl.fromTo(${safeJson(`${overlayTarget} span`)},${safeJson({ scale: 1, opacity: 1 })},${safeJson({ scale: 2.1, opacity: 0, duration: 1.1, repeat: pulses - 1, repeatDelay: 0.2, ease: "power1.out" })},${seconds2(entrance + 0.6)});`
        );
      break;
    }
    case "step-process-rail":
      for (let index = 0; index < 3; index += 1) {
        const chip = `${overlayTarget} b:nth-child(${index + 1})`;
        const at = start + duration * (0.12 + index * 0.24);
        timeline.push(
          `tl.fromTo(${safeJson(chip)},${safeJson({ opacity: 0, scale: 0.6 })},${safeJson({ opacity: 1, scale: 1, duration: 0.35, ease: "back.out(2)" })},${seconds2(at)});`,
          `tl.to(${safeJson(chip)},${safeJson({ backgroundColor: context.accentColor, borderColor: "#ffffff", scale: 1.14, duration: 0.3, ease: "power2.out" })},${seconds2(at + 0.3)});`,
          `tl.to(${safeJson(chip)},${safeJson({ scale: 1, duration: 0.25, ease: "power2.inOut" })},${seconds2(at + 0.6)});`
        );
      }
      break;
    case "before-after-split":
      timeline.push(
        `tl.set(${safeJson(visualTargets[0])},${safeJson({ clipPath: "inset(0 50% 0 0)" })},${seconds2(start)});`,
        `tl.set(${safeJson(visualTargets[1])},${safeJson({ clipPath: "inset(0 0 0 50%)" })},${seconds2(start)});`,
        `tl.fromTo(${safeJson(overlayTarget)},${safeJson({ opacity: 0, xPercent: -24 })},${safeJson({ opacity: 1, xPercent: 0, duration: seconds2(Math.min(0.8, duration * 0.25)), ease: "power2.out" })},${seconds2(start + duration * 0.12)});`
      );
      break;
    case "multi-screen-carousel":
      visualTargets.forEach((target, index) => {
        const offset = (index - (visualTargets.length - 1) / 2) * 22;
        timeline.push(
          `tl.set(${safeJson(target)},${safeJson({ scale: 0.72, xPercent: offset, rotationY: offset * -0.14, transformOrigin: "50% 50%" })},${seconds2(start)});`,
          `tl.fromTo(${safeJson(target)},${safeJson({ opacity: 0, y: 70 })},${safeJson({ opacity: index === visualTargets.length - 1 ? 1 : 0.78, y: 0, duration: 0.65, ease: "expo.out" })},${seconds2(start + index * 0.16)});`
        );
      });
      break;
    case "metric-proof":
      graphics.forEach(
        (_graphic, index) => timeline.push(
          `tl.fromTo(${safeJson(`#graphic-${sceneIndex}-${index}-body`)},${safeJson({ opacity: 0, y: 28, scale: 0.92 })},${safeJson({ opacity: 1, y: 0, scale: 1, duration: 0.55, ease: "back.out(1.5)" })},${seconds2(start + 0.2 + index * 0.12)});`
        )
      );
      break;
    case "panel-expansion":
      if (orderedVisualLayers[0]?.cameraMotion) break;
      timeline.push(
        `tl.fromTo(${safeJson(cameraTargets[0])},${safeJson({ scale: 0.92 })},${safeJson({ scale: 1.06, duration: seconds2(Math.min(0.9, duration * 0.25)), ease: "expo.out" })},${seconds2(start)});`,
        `tl.to(${safeJson(cameraTargets[0])},${safeJson({ scale: 1, duration: seconds2(Math.min(0.7, duration * 0.2)), ease: "power2.inOut" })},${seconds2(scene.range.end - Math.min(0.7, duration * 0.2))});`
      );
      break;
    case "problem-pressure":
      timeline.push(
        `tl.fromTo(${safeJson(sceneTarget)},${safeJson({ filter: "saturate(0.7) brightness(0.8)" })},${safeJson({ filter: "saturate(0.9) brightness(0.92)", duration: seconds2(duration), ease: "none" })},${seconds2(start)});`,
        `tl.to(${safeJson(visualTargets[0])},${safeJson({ keyframes: [{ x: -4 * intensity }, { x: 4 * intensity }, { x: 0 }], duration: seconds2(Math.min(0.55, duration * 0.2)), ease: "power1.inOut" })},${seconds2(start + duration * 0.28)});`
      );
      break;
    case "workflow-flow":
      visualTargets.forEach(
        (target, index) => timeline.push(
          `tl.fromTo(${safeJson(target)},${safeJson({ opacity: 0, x: -36 })},${safeJson({ opacity: 1, x: 0, duration: 0.5, ease: "power2.out" })},${seconds2(start + 0.2 + index * 0.35)});`
        )
      );
      break;
    case "brand-close":
      timeline.push(
        `tl.fromTo(${safeJson(visualTargets[0])},${safeJson({ opacity: 0, scale: 0.84 })},${safeJson({ opacity: 1, scale: 1, duration: seconds2(Math.min(0.85, duration * 0.3)), ease: "back.out(1.4)" })},${seconds2(start)});`
      );
      graphics.forEach(
        (graphic, index) => timeline.push(
          `tl.fromTo(${safeJson(`#graphic-${sceneIndex}-${index}-body`)},${safeJson({ opacity: 0, y: 26, scale: 0.94 })},${safeJson({ opacity: 1, y: 0, scale: 1, duration: 0.6, ease: "back.out(1.4)" })},${seconds2(Math.max(start + 0.25 + index * 0.14, graphic.range.start))});`
        )
      );
      break;
    case "crash-zoom-punch": {
      if (scene.visualLayers[0]?.cameraMotion) break;
      const focusX = recipeNumber(scene.recipe, "focusX", 0.5);
      const focusY = recipeNumber(scene.recipe, "focusY", 0.5);
      const scale = recipeNumber(scene.recipe, "scale", 2.4);
      const holdBefore = Math.min(
        recipeNumber(scene.recipe, "holdBefore", 1),
        duration * 0.5
      );
      const variant = String(scene.recipe.parameters?.variant ?? "rebound");
      const punchAt = start + holdBefore;
      const landed = cameraTransform(
        { atSeconds: 0, scale, focusX, focusY, easing: "none" },
        context.viewport.width,
        context.viewport.height
      );
      timeline.push(
        `tl.set(${safeJson(cameraTargets[0])},${safeJson({ scale: 1, x: 0, y: 0 })},${seconds2(start)});`,
        `tl.to(${safeJson(cameraTargets[0])},${safeJson({ ...landed, duration: 0.22, ease: "power3.in" })},${seconds2(punchAt)});`
      );
      if (variant === "impact")
        timeline.push(
          `tl.to(${safeJson(cameraTargets[0])},${safeJson({ keyframes: [{ x: landed.x + 14 }, { x: landed.x - 10 }, { x: landed.x + 6 }, { x: landed.x - 3 }, { x: landed.x }], duration: 0.24, ease: "power2.out" })},${seconds2(punchAt + 0.22)});`
        );
      else {
        const settled = cameraTransform(
          { atSeconds: 0, scale: scale * 0.955, focusX, focusY, easing: "none" },
          context.viewport.width,
          context.viewport.height
        );
        timeline.push(
          `tl.to(${safeJson(cameraTargets[0])},${safeJson({ ...settled, duration: 0.17, ease: "power2.out" })},${seconds2(punchAt + 0.22)});`
        );
      }
      break;
    }
    case "click-zoom-punch": {
      const layer = orderedVisualLayers[0];
      if (!layer || layer.cameraMotion) break;
      const scale = recipeNumber(scene.recipe, "scale", 1.35);
      const hold = recipeNumber(scene.recipe, "hold", 1);
      const maxPunches = Math.round(recipeNumber(scene.recipe, "maxPunches", 2));
      const clicks = [...layer.cursorOverlay?.samples ?? []].filter(
        (sample) => sample.action && !["move", "mouseup"].includes(String(sample.action))
      ).sort((left, right) => left.atSeconds - right.atSeconds);
      const chosen = [];
      for (const sample of clicks) {
        if (chosen.length >= maxPunches) break;
        if (sample.atSeconds < start + 0.3 || sample.atSeconds > scene.range.end - hold - 0.5)
          continue;
        const previous = chosen[chosen.length - 1];
        if (previous && sample.atSeconds - previous.atSeconds < hold + 1.2) continue;
        chosen.push(sample);
      }
      timeline.push(
        `tl.set(${safeJson(cameraTargets[0])},${safeJson({ scale: 1, x: 0, y: 0 })},${seconds2(start)});`
      );
      for (const sample of chosen) {
        const crop = layer.crop;
        const focusX = crop ? (sample.x - crop.x) / crop.width : sample.x;
        const focusY = crop ? (sample.y - crop.y) / crop.height : sample.y;
        const punched = cameraTransform(
          { atSeconds: 0, scale, focusX, focusY, easing: "none" },
          context.viewport.width,
          context.viewport.height
        );
        timeline.push(
          `tl.to(${safeJson(cameraTargets[0])},${safeJson({ ...punched, duration: 0.25, ease: "power3.out" })},${seconds2(sample.atSeconds)});`,
          `tl.to(${safeJson(cameraTargets[0])},${safeJson({ scale: 1, x: 0, y: 0, duration: 0.4, ease: "power2.inOut" })},${seconds2(sample.atSeconds + 0.25 + hold)});`
        );
      }
      break;
    }
    case "pressure-push": {
      const scale = recipeNumber(scene.recipe, "scale", 1.14);
      const vignette = recipeNumber(scene.recipe, "vignette", 0.5);
      timeline.push(
        `tl.fromTo(${safeJson(cameraTargets[0])},${safeJson({ scale: 1, x: 0, y: 0 })},${safeJson({ scale, x: 0, y: 0, duration: seconds2(duration), ease: "power2.in" })},${seconds2(start)});`,
        `tl.fromTo(${safeJson(overlayTarget)},${safeJson({ opacity: 0 })},${safeJson({ opacity: vignette, duration: seconds2(duration), ease: "power2.in" })},${seconds2(start)});`
      );
      break;
    }
    case "dutch-roll-level": {
      const tilt = recipeNumber(scene.recipe, "tilt", 10);
      const correctAt = start + duration * recipeNumber(scene.recipe, "correctAt", 0.55);
      const frameTarget = visualTargets[0];
      const driftCycles = Math.max(1, Math.floor((correctAt - start) / 1.6));
      timeline.push(
        `tl.set(${safeJson(frameTarget)},${safeJson({ rotation: -tilt, transformOrigin: "50% 50%" })},${seconds2(start)});`,
        `tl.set(${safeJson(cameraTargets[0])},${safeJson({ scale: 1.22, x: 0, y: 0 })},${seconds2(start)});`,
        `tl.to(${safeJson(frameTarget)},${safeJson({ rotation: -tilt + 0.8, y: 2, duration: 0.8, yoyo: true, repeat: driftCycles * 2 - 1, ease: "sine.inOut" })},${seconds2(start)});`,
        `tl.to(${safeJson(frameTarget)},${safeJson({ rotation: 1.2, y: 0, duration: 0.47, ease: "power3.out", overwrite: "auto" })},${seconds2(correctAt)});`,
        `tl.to(${safeJson(frameTarget)},${safeJson({ rotation: 0, duration: 0.33, ease: "power2.inOut" })},${seconds2(correctAt + 0.47)});`,
        `tl.to(${safeJson(cameraTargets[0])},${safeJson({ scale: 1.12, duration: 0.8, ease: "power2.out" })},${seconds2(correctAt)});`
      );
      break;
    }
    case "pull-back-isolation": {
      const endScale = recipeNumber(scene.recipe, "endScale", 0.62);
      timeline.push(
        `tl.fromTo(${safeJson(cameraTargets[0])},${safeJson({ scale: 2.2, x: 0, y: 0 })},${safeJson({ scale: 1, x: 0, y: 0, duration: seconds2(duration * 0.7), ease: "power3.out" })},${seconds2(start)});`
      );
      timeline.push(
        `tl.to(${safeJson(visualTargets[0])},${safeJson({ scale: endScale, borderRadius: 14, duration: seconds2(duration * 0.7), ease: "power3.out" })},${seconds2(start + duration * 0.12)});`,
        `tl.to(${safeJson(visualTargets[0])},${safeJson({ boxShadow: "0 40px 120px rgba(0,0,0,.6),0 0 0 1px rgba(255,255,255,.14)", duration: seconds2(duration * 0.35), ease: "power2.out" })},${seconds2(start + duration * 0.55)});`
      );
      break;
    }
    case "freeze-orbit": {
      const angle = recipeNumber(scene.recipe, "angle", 55);
      const target = visualTargets[0];
      timeline.push(
        `tl.set(${safeJson(sceneTarget)},${safeJson({ perspective: 1600 })},${seconds2(start)});`,
        `tl.to(${safeJson(target)},${safeJson({ rotationY: angle, scale: 1.12, duration: seconds2(duration * 0.4), ease: "power2.inOut" })},${seconds2(start)});`,
        `tl.to(${safeJson(target)},${safeJson({ rotationY: 0, scale: 1, duration: seconds2(duration * 0.45), ease: "power2.inOut" })},${seconds2(start + duration * 0.4 + 0.35)});`
      );
      break;
    }
    case "split-flap-title": {
      const stagger = recipeNumber(scene.recipe, "stagger", 0.13);
      graphics.forEach((graphic, index) => {
        const body2 = `#graphic-${sceneIndex}-${index}-body`;
        timeline.push(
          `(function(){const els=document.querySelectorAll(${safeJson(`${body2} .flap b`)});const G="ABCDEFGHJKLMNPQRSTUVWXYZ0123456789";const T=${seconds2(graphic.range.start + 0.35)};const ST=${seconds2(stagger)};tl.call(function(){els.forEach(function(el,i){el.textContent=G[(i*5)%G.length];});},[],${seconds2(graphic.range.start)});els.forEach(function(el,i){var target=el.getAttribute("data-char");for(var k=0;k<3;k++){var at=T+i*ST+k*0.13;tl.call(function(kk){el.textContent=kk<2?G[(i*7+kk*11)%G.length]:target;},[k],at);tl.fromTo(el,{rotationX:-90,filter:"brightness(0.55)"},{rotationX:0,filter:"brightness(1)",duration:0.12,ease:"power1.out"},at);}});tl.to(${safeJson(body2)},{keyframes:[{y:6},{y:-1.5},{y:0}],duration:0.5,ease:"power2.out"},T+els.length*ST+0.3);})();`
        );
      });
      break;
    }
    case "typewriter-reveal": {
      const perChar = 1 / recipeNumber(scene.recipe, "charsPerSecond", 18);
      graphics.forEach((graphic, index) => {
        const body2 = `#graphic-${sceneIndex}-${index}-body`;
        const typingSeconds = Array.from(graphic.text).length * perChar;
        timeline.push(
          `tl.set(${safeJson(`${body2} .tw`)},${safeJson({ opacity: 0 })},${seconds2(graphic.range.start)});`,
          `tl.to(${safeJson(`${body2} .tw`)},${safeJson({ opacity: 1, duration: 0.01, stagger: seconds2(perChar) })},${seconds2(graphic.range.start + 0.15)});`,
          `tl.fromTo(${safeJson(`${body2} .tw-caret`)},${safeJson({ opacity: 1 })},${safeJson({ opacity: 0, duration: 0.38, yoyo: true, repeat: Math.max(1, Math.floor((graphic.range.end - graphic.range.start - typingSeconds) / 0.38)), ease: "steps(1)" })},${seconds2(graphic.range.start + 0.15 + typingSeconds)});`
        );
      });
      break;
    }
    case "gradient-word-sweep": {
      const sweepSeconds = recipeNumber(scene.recipe, "sweepSeconds", 1.2);
      graphics.forEach(
        (graphic, index) => timeline.push(
          `tl.fromTo(${safeJson(`#graphic-${sceneIndex}-${index}-body`)},${safeJson({ backgroundPosition: "100% 0%" })},${safeJson({ backgroundPosition: "0% 0%", duration: seconds2(sweepSeconds), ease: "power2.inOut" })},${seconds2(graphic.range.start + 0.2)});`
        )
      );
      break;
    }
    case "title-demote-to-label": {
      if (!graphics.length) break;
      const demoteAt = start + duration * recipeNumber(scene.recipe, "demoteAt", 0.4);
      const labelScale = recipeNumber(scene.recipe, "labelScale", 0.45);
      timeline.push(
        `tl.to(${safeJson(`#graphic-${sceneIndex}-0-body`)},${safeJson({ left: "5%", top: "7%", xPercent: 0, yPercent: 0, scale: labelScale, transformOrigin: "0 0", duration: 0.7, ease: "power3.inOut" })},${seconds2(Math.max(demoteAt, graphics[0].range.start + 0.8))});`
      );
      break;
    }
    case "odometer-digit-roll": {
      if (!graphics.length) break;
      const digitStagger = recipeNumber(scene.recipe, "digitStagger", 0.23);
      const body2 = `#graphic-${sceneIndex}-0-body`;
      timeline.push(
        `(function(){const strips=document.querySelectorAll(${safeJson(`${body2} .odo-strip`)});const T=${seconds2(graphics[0].range.start + 0.4)};const DS=${seconds2(digitStagger)};strips.forEach(function(el,i){var digit=Number(el.getAttribute("data-digit"));tl.fromTo(el,{yPercent:0},{yPercent:-(digit*10+5),duration:0.53,ease:"power3.out"},T+i*DS);tl.to(el,{yPercent:-digit*10,duration:0.2,ease:"power2.inOut"},T+i*DS+0.53);});tl.fromTo(${safeJson(body2)},{scale:1},{scale:1.035,duration:0.13,yoyo:true,repeat:1,ease:"power1.inOut"},T+strips.length*DS+0.75);})();`
      );
      break;
    }
    case "metric-counter": {
      const countSeconds = recipeNumber(scene.recipe, "countSeconds", 1.4);
      graphics.forEach((graphic, index) => {
        const body2 = `#graphic-${sceneIndex}-${index}-body`;
        timeline.push(
          `(function(){const el=document.querySelector(${safeJson(`${body2} .counter`)});if(!el)return;const target=Number(el.getAttribute("data-target"));const decimals=Number(el.getAttribute("data-decimals")||0);const o={v:0};const fmt=function(v){return v.toLocaleString("en-US",{minimumFractionDigits:decimals,maximumFractionDigits:decimals});};const T=${seconds2(graphic.range.start + 0.1)};tl.call(function(){el.textContent=fmt(0);},[],T);tl.to(o,{v:target,duration:${seconds2(countSeconds)},ease:"power2.out",onUpdate:function(){el.textContent=fmt(o.v);}},T);})();`
        );
      });
      break;
    }
    case "deck-deal-flyin": {
      const cardScale = recipeNumber(scene.recipe, "cardScale", 0.42);
      const count = visualTargets.length;
      const pitch = context.viewport.width * cardScale * 1.06;
      visualTargets.forEach((target, index) => {
        const restingX = seconds2((index - (count - 1) / 2) * pitch);
        const cue = Math.max(index * 0.06, index * 0.22 - 0.012 * index * (index - 1));
        const jitter2 = ((index * 7 % 9 - 4) * 2 + 18) * (index % 2 === 0 ? 1 : -1);
        timeline.push(
          `tl.set(${safeJson(target)},${safeJson({ scale: cardScale * 0.9, x: seconds2(context.viewport.width * 0.45), y: seconds2(context.viewport.height * 0.6), rotation: jitter2, opacity: 0, transformOrigin: "50% 50%" })},${seconds2(start)});`,
          `tl.to(${safeJson(target)},${safeJson({ x: restingX, y: 0, rotation: 0, scale: cardScale, opacity: 1, duration: 0.42, ease: "power3.out" })},${seconds2(start + 0.3 + cue)});`,
          `tl.to(${safeJson(target)},${safeJson({ scale: cardScale * 1.02, duration: 0.1, yoyo: true, repeat: 1, ease: "power1.inOut" })},${seconds2(start + 0.3 + cue + 0.42)});`
        );
      });
      break;
    }
    case "list-reveal": {
      const stagger = recipeNumber(scene.recipe, "stagger", 0.14);
      graphics.forEach((graphic, index) => {
        const body2 = `#graphic-${sceneIndex}-${index}-body`;
        const at = Math.max(graphic.range.start, start + 0.2 + index * stagger);
        timeline.push(
          `tl.fromTo(${safeJson(`${body2} .list-marker`)},${safeJson({ scaleX: 0 })},${safeJson({ scaleX: 1, duration: 0.3, ease: "power2.out" })},${seconds2(at)});`,
          `tl.fromTo(${safeJson(body2)},${safeJson({ opacity: 0, x: -40 })},${safeJson({ opacity: 1, x: 0, duration: 0.5, ease: "power3.out" })},${seconds2(at + 0.05)});`
        );
      });
      break;
    }
    case "skeleton-reveal": {
      const revealAt = start + duration * recipeNumber(scene.recipe, "revealAt", 0.4);
      timeline.push(
        `tl.fromTo(${safeJson(overlayTarget)},${safeJson({ opacity: 0 })},${safeJson({ opacity: 1, duration: 0.01 })},${seconds2(start)});`,
        `tl.fromTo(${safeJson(`${overlayTarget} i`)},${safeJson({ opacity: 0, x: -20 })},${safeJson({ opacity: 1, x: 0, duration: 0.35, stagger: 0.08, ease: "power2.out" })},${seconds2(start + 0.1)});`,
        `tl.fromTo(${safeJson(`${overlayTarget} i`)},${safeJson({ backgroundPositionX: "-200%" })},${safeJson({ backgroundPositionX: "200%", duration: 1.3, repeat: Math.max(0, Math.ceil((revealAt - start) / 1.3) - 1), ease: "none" })},${seconds2(start)});`,
        `tl.to(${safeJson(`${overlayTarget} i`)},${safeJson({ opacity: 0, scale: 0.96, duration: 0.28, stagger: 0.05, ease: "power2.in", overwrite: "auto" })},${seconds2(revealAt)});`,
        `tl.to(${safeJson(overlayTarget)},${safeJson({ opacity: 0, duration: 0.3, ease: "power2.in" })},${seconds2(revealAt + 0.2)});`,
        `tl.fromTo(${safeJson(cameraTargets[0])},${safeJson({ scale: 1, x: 0, y: 0 })},${safeJson({ scale: 1.08, x: 0, y: 0, duration: seconds2(Math.max(0.8, scene.range.end - revealAt)), ease: "power2.out" })},${seconds2(revealAt)});`
      );
      break;
    }
    case "glint-sweep": {
      const at = start + duration * recipeNumber(scene.recipe, "at", 0.25);
      timeline.push(
        `tl.fromTo(${safeJson(`${overlayTarget} span`)},${safeJson({ xPercent: -160 })},${safeJson({ xPercent: 260, duration: 0.9, ease: "power1.inOut" })},${seconds2(at)});`
      );
      break;
    }
    case "spotlight-sweep": {
      const sweepSeconds = recipeNumber(scene.recipe, "sweepSeconds", 2.2);
      const darkness = recipeNumber(scene.recipe, "darkness", 0.72);
      timeline.push(
        `tl.fromTo(${safeJson(overlayTarget)},${safeJson({ opacity: 0, "--spot-x": "-25%" })},${safeJson({ opacity: darkness, "--spot-x": "-25%", duration: 0.01 })},${seconds2(start)});`,
        `tl.to(${safeJson(overlayTarget)},${safeJson({ "--spot-x": "125%", duration: seconds2(sweepSeconds), ease: "none" })},${seconds2(start + 0.1)});`,
        `tl.to(${safeJson(overlayTarget)},${safeJson({ opacity: 0, duration: 0.4, ease: "power2.out" })},${seconds2(start + 0.1 + sweepSeconds)});`
      );
      break;
    }
    case "brand-frame-snap": {
      const thickness = recipeNumber(scene.recipe, "thickness", 44);
      const frameTarget = visualTargets[0];
      timeline.push(
        `tl.fromTo(${safeJson(`${overlayTarget} .bf-top,${overlayTarget} .bf-bottom`)},${safeJson({ height: 0 })},${safeJson({ height: thickness, duration: 0.6, ease: "power3.out" })},${seconds2(start)});`,
        `tl.fromTo(${safeJson(`${overlayTarget} .bf-left,${overlayTarget} .bf-right`)},${safeJson({ width: 0 })},${safeJson({ width: thickness, duration: 0.6, ease: "power3.out" })},${seconds2(start)});`,
        `tl.fromTo(${safeJson(frameTarget)},${safeJson({ y: seconds2(context.viewport.height * 0.55), scale: 0.82, opacity: 0 })},${safeJson({ y: 0, scale: 1, opacity: 1, duration: 0.7, ease: "back.out(1.3)" })},${seconds2(start + 0.45)});`,
        `tl.to(${safeJson(overlayTarget)},${safeJson({ scale: 1.012, duration: 0.08, yoyo: true, repeat: 1, ease: "power1.inOut" })},${seconds2(start + 1.15)});`
      );
      break;
    }
    case "impact-feedback": {
      const at = start + duration * recipeNumber(scene.recipe, "at", 0.5);
      const flash = recipeNumber(scene.recipe, "flash", 0.35);
      const frameTarget = visualTargets[0];
      timeline.push(
        `tl.to(${safeJson(frameTarget)},${safeJson({ scale: 1.04, duration: 0.08, ease: "power2.out" })},${seconds2(at)});`,
        `tl.to(${safeJson(frameTarget)},${safeJson({ scale: 1, duration: 0.22, ease: "power3.out" })},${seconds2(at + 0.08)});`,
        `tl.fromTo(${safeJson(overlayTarget)},${safeJson({ opacity: flash })},${safeJson({ opacity: 0, duration: 0.14, ease: "power2.out" })},${seconds2(at)});`
      );
      break;
    }
    case "scanline-annotate-focus": {
      timeline.push(
        `tl.fromTo(${safeJson(`${overlayTarget} .scan-line`)},${safeJson({ top: "0%", opacity: 0 })},${safeJson({ top: "100%", opacity: 1, duration: 0.9, ease: "none" })},${seconds2(start + 0.1)});`,
        `tl.to(${safeJson(`${overlayTarget} .scan-line`)},${safeJson({ opacity: 0, duration: 0.15 })},${seconds2(start + 1)});`,
        `tl.fromTo(${safeJson(`${overlayTarget} .scan-target`)},${safeJson({ opacity: 0, scale: 1.3 })},${safeJson({ opacity: 1, scale: 1, duration: 0.35, ease: "back.out(2)" })},${seconds2(start + 1.05)});`
      );
      break;
    }
    case "title-blur-slide": {
      const stagger = recipeNumber(scene.recipe, "stagger", 0.06);
      const rise = recipeNumber(scene.recipe, "rise", 40);
      graphics.forEach(
        (graphic, index) => timeline.push(
          `tl.fromTo(${safeJson(`#graphic-${sceneIndex}-${index}-body .word`)},${safeJson({ opacity: 0, y: rise, filter: "blur(14px)" })},${safeJson({ opacity: 1, y: 0, filter: "blur(0px)", duration: 0.72, ease: "power3.out", stagger })},${seconds2(graphic.range.start + 0.05)});`
        )
      );
      break;
    }
    case "marker-underline": {
      if (!graphics.length) break;
      const delay = recipeNumber(scene.recipe, "delay", 0.35);
      timeline.push(
        `tl.fromTo(${safeJson(`#graphic-${sceneIndex}-0-body .marker-underline`)},${safeJson({ scaleX: 0 })},${safeJson({ scaleX: 1, duration: 0.5, ease: "power2.out" })},${seconds2(Math.max(start + delay, graphics[0].range.start + 0.1))});`
      );
      break;
    }
  }
}
function transitionAtBoundary(previous, current) {
  const outgoing = normalizeTransition(previous.transitionOut);
  const incoming = normalizeTransition(current.transitionIn);
  if (outgoing && incoming && outgoing.id !== incoming.id)
    throw new Error(
      `Transition mismatch between ${previous.id} (${outgoing.id}) and ${current.id} (${incoming.id}).`
    );
  return incoming ?? outgoing;
}
function transitionOverlapSeconds(transition) {
  if (!transition || !OVERLAP_TRANSITIONS.has(transition.id)) return 0;
  return (transition.durationSeconds ?? 0.4) / 2;
}
function transitionOverlayMarkup(transition, index, boundarySeconds, renderRange) {
  if (["cut", "crossfade", "iris", "push", "flip", "blur-dissolve", "wipe"].includes(
    transition.id
  ))
    return "";
  const duration = transition.durationSeconds ?? 0.4;
  const visible = intersectTimeRange(
    { start: Math.max(0, boundarySeconds - duration / 2), end: boundarySeconds + duration / 2 },
    renderRange
  );
  if (!visible) return "";
  return `<div id="transition-${index}" class="clip transition-overlay transition-${transition.id}" data-start="${seconds2(visible.start - renderRange.start)}" data-duration="${seconds2(visible.end - visible.start)}" data-track-index="${TRANSITION_TRACK}" aria-hidden="true"><span></span></div>`;
}
function applyTransition(transition, index, current, timeline) {
  if (transition.id === "cut") return;
  if (applyExtendedTransition(transition, index, current, timeline)) return;
  const boundary = current.range.start;
  const duration = transition.durationSeconds ?? 0.4;
  const half = duration / 2;
  const direction = transition.direction ?? "left";
  const intensity = transition.intensity ?? 1;
  const axis = direction === "left" || direction === "right" ? "xPercent" : "yPercent";
  const sign = direction === "right" || direction === "down" ? 1 : -1;
  const outgoing = `#scene-${index}`;
  const incoming = `#scene-${index + 1}`;
  const overlay = `#transition-${index}`;
  if (transition.id === "crossfade") {
    timeline.push(
      `tl.fromTo(${safeJson(incoming)},${safeJson({ opacity: 0 })},${safeJson({ opacity: 1, duration: seconds2(duration), ease: "power1.inOut" })},${seconds2(boundary - half)});`
    );
  } else if (transition.id === "whip-pan") {
    timeline.push(
      `tl.set(${safeJson(incoming)},${safeJson({ [axis]: sign * 110, filter: `blur(${seconds2(12 * intensity)}px)` })},${seconds2(boundary - half)});`,
      `tl.to(${safeJson(outgoing)},${safeJson({ [axis]: sign * -22 * intensity, filter: `blur(${seconds2(12 * intensity)}px)`, duration: seconds2(half), ease: "power3.in" })},${seconds2(boundary - half)});`,
      `tl.to(${safeJson(incoming)},${safeJson({ [axis]: 0, filter: "blur(0px)", duration: seconds2(half), ease: "power3.out" })},${seconds2(boundary)});`,
      `tl.fromTo(${safeJson(overlay)},${safeJson({ opacity: 0, [axis]: sign * -45 })},${safeJson({ opacity: 0.9, [axis]: sign * 45, duration: seconds2(duration), ease: "power2.inOut" })},${seconds2(boundary - half)});`
    );
  } else if (transition.id === "hidden-cut") {
    timeline.push(
      `tl.set(${safeJson(incoming)},${safeJson({ opacity: 0 })},${seconds2(boundary - half)});`,
      `tl.fromTo(${safeJson(overlay)},${safeJson({ [axis]: sign * -105 })},${safeJson({ [axis]: 0, duration: seconds2(half), ease: "power3.in" })},${seconds2(boundary - half)});`,
      `tl.set(${safeJson(incoming)},${safeJson({ opacity: 1 })},${seconds2(boundary)});`,
      `tl.to(${safeJson(overlay)},${safeJson({ [axis]: sign * 105, duration: seconds2(half), ease: "power3.out" })},${seconds2(boundary)});`
    );
  } else if (transition.id === "zoom-through") {
    timeline.push(
      `tl.set(${safeJson(incoming)},${safeJson({ opacity: 0, scale: 0.9 })},${seconds2(boundary - half)});`,
      `tl.to(${safeJson(outgoing)},${safeJson({ scale: 1.1 * intensity, opacity: 0.3, duration: seconds2(half), ease: "power3.in" })},${seconds2(boundary - half)});`,
      `tl.to(${safeJson(incoming)},${safeJson({ scale: 1, opacity: 1, duration: seconds2(half), ease: "power3.out" })},${seconds2(boundary)});`,
      `tl.fromTo(${safeJson(overlay)},${safeJson({ opacity: 0, scale: 0.5 })},${safeJson({ opacity: 0.8, scale: 1.5, duration: seconds2(duration), ease: "power2.out" })},${seconds2(boundary - half)});`
    );
  } else if (transition.id === "match-cut") {
    timeline.push(
      `tl.set(${safeJson(incoming)},${safeJson({ opacity: 0 })},${seconds2(boundary - half)});`,
      `tl.fromTo(${safeJson(overlay)},${safeJson({ opacity: 0 })},${safeJson({ opacity: 0.65, duration: seconds2(half * 0.6), yoyo: true, repeat: 1, ease: "power1.inOut" })},${seconds2(boundary - half * 0.6)});`,
      `tl.set(${safeJson(incoming)},${safeJson({ opacity: 1, scale: 0.97 })},${seconds2(boundary)});`,
      `tl.to(${safeJson(incoming)},${safeJson({ scale: 1, duration: seconds2(half), ease: "power2.out" })},${seconds2(boundary)});`
    );
  }
}
function cursorPosition(sample, crop, width, height) {
  const x = crop ? (sample.x - crop.x) / crop.width : sample.x;
  const y = crop ? (sample.y - crop.y) / crop.height : sample.y;
  return {
    x: seconds2(x * width),
    y: seconds2(y * height),
    visible: x >= 0 && x <= 1 && y >= 0 && y <= 1
  };
}
function croppedCameraTransform(keyframe, crop) {
  const local = {
    ...keyframe,
    focusX: (keyframe.focusX - crop.x) / crop.width,
    focusY: (keyframe.focusY - crop.y) / crop.height,
    ...keyframe.frame ? {
      frame: {
        x: (keyframe.frame.x - crop.x) / crop.width,
        y: (keyframe.frame.y - crop.y) / crop.height,
        width: keyframe.frame.width / crop.width,
        height: keyframe.frame.height / crop.height
      }
    } : {}
  };
  const { x, y, ...rest } = cameraTransform(local, 100, 100, keyframe.blur !== void 0);
  return { ...rest, x: 0, y: 0, xPercent: x, yPercent: y };
}
function cursorOverlayMarkup(layer, sceneStart, sceneEnd, sceneIndex, layerIndex, viewport, timeline) {
  const plan = layer.cursorOverlay;
  const samples = [...plan?.samples ?? []].sort(
    (left, right) => left.atSeconds - right.atSeconds
  );
  if (!plan || !samples.length) return "";
  const cursorId = `cursor-${sceneIndex}-${layerIndex}`;
  const lifetimeId = `${cursorId}-lifetime`;
  timeline.push(
    `tl.set("#${lifetimeId}",{visibility:"hidden"},0);`,
    `tl.set("#${lifetimeId}",{visibility:"visible"},${seconds2(sceneStart)});`,
    `tl.set("#${lifetimeId}",{visibility:"hidden"},${seconds2(sceneEnd)});`
  );
  const glow = plan.glow ?? true;
  const trail = Math.max(0, Math.min(6, Math.round(plan.trail ?? 0)));
  const rippleRings = Math.max(1, Math.min(3, Math.round(plan.rippleRings ?? 1)));
  const cursorStyle = {
    width: `${seconds2(plan.sizePixels)}px`,
    height: `${seconds2(plan.sizePixels)}px`,
    color: plan.color,
    opacity: 0,
    zIndex: plan.zIndex,
    filter: glow ? `drop-shadow(0 1px 2px ${plan.outlineColor}) drop-shadow(0 0 ${seconds2(plan.sizePixels * 0.25)}px ${plan.clickColor}) drop-shadow(0 0 ${seconds2(plan.sizePixels * 0.7)}px ${plan.clickColor})` : `drop-shadow(0 1px 2px ${plan.outlineColor})`,
    ...plan.style ?? {}
  };
  const cursorBody = plan.shape.trim().toLowerCase() === "dot" ? `<span class="cursor-dot" style="display:block;width:100%;height:100%;border-radius:50%;background:currentColor;border:2px solid ${escapeHtml2(plan.outlineColor)}"></span>` : `<svg viewBox="0 0 32 32" aria-hidden="true"><path d="M3 2.5v23.2l6.1-5.5 4.2 9.3 4.2-1.9-4.1-9.1 8.1-.3L3 2.5z" fill="currentColor" stroke="${escapeHtml2(plan.outlineColor)}" stroke-width="2" stroke-linejoin="round"/></svg>`;
  const firstPosition = cursorPosition(samples[0], layer.crop, viewport.width, viewport.height);
  const placement = (position) => layer.crop ? {
    left: `${seconds2(position.x / viewport.width * 100)}%`,
    top: `${seconds2(position.y / viewport.height * 100)}%`
  } : { x: position.x, y: position.y };
  timeline.push(
    `tl.set("#${cursorId}",${safeJson({ ...placement(firstPosition), opacity: 0 })},${seconds2(sceneStart)});`,
    `tl.set("#${cursorId}",${safeJson({
      ...placement(firstPosition),
      opacity: firstPosition.visible ? plan.opacity : 0
    })},${seconds2(samples[0].atSeconds)});`
  );
  const ghostIds = Array.from({ length: trail }, (_, ghost) => `${cursorId}-ghost-${ghost + 1}`);
  for (const [ghost, ghostId] of ghostIds.entries())
    timeline.push(
      `tl.set("#${ghostId}",${safeJson({ ...placement(firstPosition), opacity: 0 })},${seconds2(sceneStart)});`,
      `tl.set("#${ghostId}",${safeJson({ ...placement(firstPosition), opacity: firstPosition.visible ? plan.opacity * 0.45 * (1 - ghost / (trail + 1)) : 0 })},${seconds2(samples[0].atSeconds + (ghost + 1) * 0.06)});`
    );
  for (let index = 1; index < samples.length; index += 1) {
    const previous = samples[index - 1];
    const sample = samples[index];
    const position = cursorPosition(sample, layer.crop, viewport.width, viewport.height);
    const duration = sample.atSeconds - previous.atSeconds;
    const values = {
      ...placement(position),
      opacity: position.visible ? plan.opacity : 0
    };
    timeline.push(
      duration > 0 ? `tl.to("#${cursorId}",{...${safeJson(values)},duration:${seconds2(duration)},ease:${safeJson(plan.moveEasing)}},${seconds2(previous.atSeconds)});` : `tl.set("#${cursorId}",${safeJson(values)},${seconds2(sample.atSeconds)});`
    );
    for (const [ghost, ghostId] of ghostIds.entries()) {
      const lag = (ghost + 1) * 0.06;
      const ghostValues = {
        ...placement(position),
        opacity: position.visible ? plan.opacity * 0.45 * (1 - ghost / (trail + 1)) : 0
      };
      timeline.push(
        duration > 0 ? `tl.to("#${ghostId}",{...${safeJson(ghostValues)},duration:${seconds2(duration)},ease:${safeJson(plan.moveEasing)}},${seconds2(previous.atSeconds + lag)});` : `tl.set("#${ghostId}",${safeJson(ghostValues)},${seconds2(sample.atSeconds + lag)});`
      );
    }
  }
  const clickBlocks = [];
  if (plan.showClicks) {
    for (const [clickIndex, sample] of samples.filter((item) => item.action && !["move", "mouseup"].includes(String(item.action))).entries()) {
      const position = cursorPosition(sample, layer.crop, viewport.width, viewport.height);
      if (!position.visible) continue;
      const clickId = `cursor-click-${sceneIndex}-${layerIndex}-${clickIndex}`;
      const bodyId = `${clickId}-body`;
      const diameter = seconds2(plan.sizePixels * 0.9);
      const clickPosition = layer.crop ? `left:${seconds2(position.x / viewport.width * 100)}%;top:${seconds2(position.y / viewport.height * 100)}%` : `left:${position.x}px;top:${position.y}px`;
      clickBlocks.push(
        `<div id="${clickId}" class="cursor-click" style="${clickPosition};z-index:${plan.zIndex}"><div id="${bodyId}" class="cursor-click-body"${styleAttribute(
          {
            width: `${diameter}px`,
            height: `${diameter}px`,
            marginLeft: `${seconds2(-diameter / 2)}px`,
            marginTop: `${seconds2(-diameter / 2)}px`,
            border: `${Math.max(2, seconds2(plan.sizePixels * 0.08))}px solid ${plan.clickColor}`,
            borderRadius: "50%",
            opacity: 0,
            ...plan.clickStyle ?? {}
          }
        )}></div></div>`
      );
      timeline.push(
        `tl.fromTo("#${bodyId}",${safeJson({ scale: 0.35, opacity: plan.opacity })},${safeJson({ scale: plan.clickScale, opacity: 0, duration: seconds2(plan.clickDurationSeconds), ease: "power2.out" })},${seconds2(sample.atSeconds)});`
      );
      for (let ring = 1; ring < rippleRings; ring += 1) {
        const ringId = `${bodyId}-ring-${ring}`;
        clickBlocks.push(
          `<div class="cursor-click" style="${clickPosition};z-index:${plan.zIndex}"><div id="${ringId}" class="cursor-click-body"${styleAttribute(
            {
              width: `${diameter}px`,
              height: `${diameter}px`,
              marginLeft: `${seconds2(-diameter / 2)}px`,
              marginTop: `${seconds2(-diameter / 2)}px`,
              border: `${Math.max(1, seconds2(plan.sizePixels * 0.05))}px solid ${plan.clickColor}`,
              borderRadius: "50%",
              opacity: 0
            }
          )}></div></div>`
        );
        timeline.push(
          `tl.fromTo("#${ringId}",${safeJson({ scale: 0.35, opacity: plan.opacity * 0.7 })},${safeJson({ scale: plan.clickScale * (1 + ring * 0.55), opacity: 0, duration: seconds2(plan.clickDurationSeconds * (1 + ring * 0.35)), ease: "power2.out" })},${seconds2(sample.atSeconds + ring * 0.09)});`
        );
      }
    }
  }
  const ghostMarkup = ghostIds.map((ghostId, ghost) => {
    const size = seconds2(plan.sizePixels * 0.42 * (1 - ghost / (trail + 1)));
    return `<div id="${ghostId}" class="cursor-ghost" style="width:${size}px;height:${size}px;margin:${seconds2(-size / 2 + plan.sizePixels * 0.12)}px 0 0 ${seconds2(-size / 2 + plan.sizePixels * 0.1)}px;background:${escapeHtml2(plan.clickColor)};z-index:${plan.zIndex - 1};opacity:0"></div>`;
  }).join("");
  return `<div id="${lifetimeId}" style="position:absolute;inset:0;visibility:hidden;pointer-events:none">${ghostMarkup}<div id="${cursorId}" class="${classAttribute(`cursor-overlay cursor-${plan.shape}`, plan.className)}"${styleAttribute(cursorStyle)}>${cursorBody}</div>${clickBlocks.join("")}</div>`;
}
var CAPTION_FIT_SCRIPT = `(function(){function fit(){var boxes=document.querySelectorAll('.caption');for(var i=0;i<boxes.length;i++){var box=boxes[i];var el=box.querySelector('.caption-text')||box;if(box.getAttribute('data-caption-fit')==='manual'||/\\n/.test(el.textContent||''))continue;var stored=el.getAttribute('data-caption-font');var base=stored?parseFloat(stored):parseFloat(getComputedStyle(el).fontSize);if(!(base>0))continue;if(!stored)el.setAttribute('data-caption-font',String(base));el.style.whiteSpace='nowrap';el.style.fontSize=base+'px';var limit=box.clientWidth;var scale=1;while(el.scrollWidth>limit+1&&scale>0.72){scale-=0.04;el.style.fontSize=(base*scale).toFixed(2)+'px';}if(el.scrollWidth>limit+1){el.style.fontSize=base+'px';el.style.whiteSpace='normal';}}}fit();if(document.fonts&&document.fonts.ready)document.fonts.ready.then(fit);window.addEventListener('load',fit);})();`;
async function compileHyperFramesProject(project, outputDir, projectDir = path9.dirname(outputDir), options2 = {}) {
  const renderFps = options2.renderFps ?? project.fps;
  if (!Number.isFinite(renderFps) || renderFps <= 0 || renderFps > project.fps)
    throw new Error("Render fps must be positive and no higher than project fps.");
  const renderScale = options2.renderScale ?? 1;
  if (!Number.isFinite(renderScale) || renderScale < 0.1 || renderScale > 1)
    throw new Error("HyperFrames renderScale must be between 0.1 and 1.");
  const renderRange = options2.renderRange ?? { start: 0, end: project.durationSeconds };
  if (!Number.isFinite(renderRange.start) || !Number.isFinite(renderRange.end) || renderRange.start < 0 || renderRange.end <= renderRange.start || renderRange.end > project.durationSeconds + 1e-4)
    throw new Error("HyperFrames renderRange must be inside the project duration.");
  const renderDuration = renderRange.end - renderRange.start;
  const renderWidth = Math.max(2, Math.round(project.width * renderScale / 2) * 2);
  const renderHeight = Math.max(2, Math.round(project.height * renderScale / 2) * 2);
  assertProjectShotRecipes(project);
  assertProjectBrandStyle(project);
  await fs7.mkdir(outputDir, { recursive: true });
  const assetUrls = await hyperFramesAssetUrls(
    project,
    path9.resolve(projectDir),
    options2.renderRange,
    options2.normalizeVideo,
    options2.onAssetStaged
  );
  const assetUrl = (filePath) => {
    const url = assetUrls.get(path9.resolve(filePath));
    if (!url) throw new Error("HyperFrames media input was not prepared.");
    return url;
  };
  const gsapBundlePath = resolveGsapBundle();
  const gsapSource = (await fs7.readFile(gsapBundlePath, "utf8")).replace(
    /<\/script/gi,
    "<\\/script"
  );
  const brandStyle = resolveProjectBrandStyle(project);
  const graphicTrack = createClipTrackAllocator(GRAPHIC_TRACK);
  const captionTrack = createClipTrackAllocator(CAPTION_TRACK);
  const voiceTrack = createClipTrackAllocator(1e4);
  const musicTrack = createClipTrackAllocator(11e3);
  const soundTrack = createClipTrackAllocator(12e3);
  const blocks = [];
  const transitionBlocks = [];
  const timeline = [];
  const spatialEntries = [];
  const environmentBlock = environmentMarkup(
    project,
    brandStyle.environment,
    timeline,
    renderDuration
  );
  const postFxBlock = postFxMarkup(
    project,
    brandStyle.environment,
    brandStyle.accentColor,
    timeline,
    renderDuration
  );
  const boundaryTransitions = project.scenes.slice(1).map((current, index) => transitionAtBoundary(project.scenes[index], current));
  const overlapFor = (sceneIndex) => ({
    leadIn: sceneIndex > 0 ? transitionOverlapSeconds(boundaryTransitions[sceneIndex - 1]) : 0,
    tailOut: sceneIndex < project.scenes.length - 1 ? transitionOverlapSeconds(boundaryTransitions[sceneIndex]) : 0
  });
  for (const [sceneIndex, scene] of project.scenes.entries()) {
    const visibleVoiceoverRange = scene.voiceover ? intersectTimeRange(scene.voiceover.range, renderRange) : null;
    if (scene.voiceover?.assetPath && visibleVoiceoverRange)
      blocks.push(
        `<audio id="audio-voiceover-${sceneIndex}" class="clip" data-start="${seconds2(visibleVoiceoverRange.start - renderRange.start)}" data-duration="${seconds2(visibleVoiceoverRange.end - visibleVoiceoverRange.start)}" data-track-index="${voiceTrack(scene.voiceover.range)}" data-media-start="${seconds2((scene.voiceover.sourceStartSeconds ?? 0) + visibleVoiceoverRange.start - scene.voiceover.range.start)}" data-volume="${decibelsToAmplitude(scene.voiceover.gainDb)}" src="${escapeHtml2(assetUrl(scene.voiceover.assetPath))}"></audio>`
      );
    const visibleMusicRange = scene.music ? intersectTimeRange(scene.music.range, renderRange) : null;
    if (scene.music?.assetPath && visibleMusicRange)
      blocks.push(
        `<audio id="audio-music-${sceneIndex}" class="clip" data-start="${seconds2(visibleMusicRange.start - renderRange.start)}" data-duration="${seconds2(visibleMusicRange.end - visibleMusicRange.start)}" data-track-index="${musicTrack(scene.music.range)}" data-media-start="${seconds2((scene.music.sourceStartSeconds ?? 0) + visibleMusicRange.start - scene.music.range.start)}" data-volume="${decibelsToAmplitude(scene.music.gainDb)}" src="${escapeHtml2(assetUrl(scene.music.assetPath))}"></audio>`
      );
    for (const [soundIndex, soundEffect] of (scene.soundEffects ?? []).entries()) {
      const visible = intersectTimeRange(soundEffect.range, renderRange);
      if (soundEffect.assetPath && visible)
        blocks.push(
          `<audio id="audio-sfx-${sceneIndex}-${soundIndex}" class="clip sound-effect" data-start="${seconds2(visible.start - renderRange.start)}" data-duration="${seconds2(visible.end - visible.start)}" data-media-start="${seconds2(visible.start - soundEffect.range.start)}" data-track-index="${soundTrack(soundEffect.range)}" data-volume="${decibelsToAmplitude(soundEffect.gainDb)}" data-purpose="${soundEffect.purpose}" data-sync-point="${soundEffect.syncPoint}" src="${escapeHtml2(assetUrl(soundEffect.assetPath))}"></audio>`
        );
    }
    const { leadIn, tailOut } = overlapFor(sceneIndex);
    if (!intersectTimeRange(
      { start: scene.range.start - leadIn, end: scene.range.end + tailOut },
      renderRange
    ))
      continue;
    const visibleSceneRange = intersectTimeRange(scene.range, renderRange);
    const authoredSceneDuration = scene.range.end - scene.range.start;
    const sceneDuration = visibleSceneRange ? visibleSceneRange.end - visibleSceneRange.start : 0;
    const sceneStart = (visibleSceneRange?.start ?? renderRange.start) - renderRange.start;
    const sceneLeftTrim = (visibleSceneRange?.start ?? scene.range.start) - scene.range.start;
    const sceneId = `scene-${sceneIndex}`;
    const viewport = { width: project.width, height: project.height };
    const stagedBlocks = [];
    const sceneBlocks = [];
    if (scene.spatial) {
      const modelUrls = {};
      const spatialScene = {
        ...scene.spatial,
        models: scene.spatial.models.map((model) => {
          const hydrated = model;
          if (hydrated.assetId && hydrated.assetPath) modelUrls[hydrated.assetId] = assetUrl(hydrated.assetPath);
          const { assetPath: _assetPath, ...portable } = hydrated;
          return portable;
        })
      };
      const visibleSpatialRange = intersectTimeRange(scene.range, renderRange);
      if (visibleSpatialRange) {
        if (spatialScene.anatomy?.figureId && !spatialScene.anatomy.authoredFigure) throw new Error(`ANATOMY_FIGURE_UNBOUND: ${spatialScene.anatomy.figureId}; compile through the project CLI to resolve registered figures.`);
        const backends = spatialScene.anatomy && spatialScene.models.length ? ["anatomy", "three"] : [spatialBackend(spatialScene)];
        for (const backend of backends) {
          const mixed = backends.length > 1;
          const viewport2 = backend === "three" ? spatialScene.modelViewport : void 0;
          const width = viewport2 ? Math.round(project.width * viewport2.width) : project.width, height = viewport2 ? Math.round(project.height * viewport2.height) : project.height;
          const canvasId = `spatial-canvas-${sceneIndex}-${backend}`;
          const config = serializeSpatialRuntimeConfig({
            version: backend === "anatomy" ? ANATOMY_RUNTIME_VERSION : SPATIAL_RUNTIME_VERSION,
            backend,
            width,
            height,
            sceneRange: scene.range,
            scene: backend === "three" ? { ...spatialScene, anatomy: void 0, transparentBackground: mixed || spatialScene.transparentBackground } : mixed ? { ...spatialScene, annotations: [] } : spatialScene,
            modelUrls,
            anatomyGeometry: backend === "anatomy" && !spatialScene.anatomy?.figureId ? compileAnatomy(spatialScene.anatomy, width, height) : void 0
          });
          spatialEntries.push({ sceneId: scene.id, canvasId, config, start: renderRange.start, backend });
          const placement = viewport2 ? `;left:${viewport2.x * 100}%;top:${viewport2.y * 100}%;width:${viewport2.width * 100}%;height:${viewport2.height * 100}%` : "";
          sceneBlocks.push(`<div id="spatial-layer-${sceneIndex}-${backend}" class="clip spatial-layer" data-start="${seconds2(visibleSpatialRange.start - renderRange.start)}" data-duration="${seconds2(visibleSpatialRange.end - visibleSpatialRange.start)}" data-track-index="${sceneTrack(sceneIndex, 39)}" style="z-index:${SCENE_STACK.background + 40 + (backend === "three" ? 1 : 0)}${placement}"><canvas id="${canvasId}" width="${width}" height="${height}"></canvas></div>`);
        }
      }
    }
    const breathe = scene.idleMotion !== "none" && !CAMERA_MOVING_RECIPES.has(scene.recipe?.id ?? "");
    for (const [layerIndex, layer] of [...scene.visualLayers].sort((left, right) => left.zIndex - right.zIndex).entries()) {
      const clipId = `visual-clip-${sceneIndex}-${layerIndex}`;
      const cameraId = `camera-${sceneIndex}-${layerIndex}`;
      const cursorClipId = `cursor-clip-${sceneIndex}-${layerIndex}`;
      const cursorCameraId = `cursor-camera-${sceneIndex}-${layerIndex}`;
      const contained = sourceContainViewport(layer, scene, viewport.width, viewport.height);
      const cameraBoxStyle = contained ? styleAttribute(
        Object.fromEntries(
          Object.entries(contained).map(([key, value]) => [
            key,
            `${seconds2(value)}px`
          ])
        )
      ) : "";
      const cropped = Boolean(layer.crop);
      const visualStyle = cropped ? {
        ...cropStyle(layer.crop),
        objectFit: "fill",
        maxWidth: "none",
        maxHeight: "none"
      } : { opacity: layer.opacity, ...layer.style ?? {} };
      const cropViewportStyle = cropped ? styleAttribute({
        position: "absolute",
        left: 0,
        top: 0,
        width: "100%",
        height: "100%",
        ...layer.style ?? {},
        opacity: layer.opacity,
        overflow: "hidden"
      }) : "";
      const mediaStart = layer.sourceRange?.start ?? 0;
      const playbackRate = layer.sourcePlaybackRate ?? (layer.sourceRange ? (layer.sourceRange.end - layer.sourceRange.start) / authoredSceneDuration : 1);
      const visibleMediaStart = mediaStart + sceneLeftTrim * playbackRate;
      const isVideo = Boolean(
        layer.assetPath && layer.mediaKind !== "image" && layer.source !== "generated_image"
      );
      const layerLeadIn = isVideo ? Math.min(leadIn, mediaStart / playbackRate) : leadIn;
      const authoredClipStart = scene.range.start - layerLeadIn;
      const authoredClipDuration = authoredSceneDuration + layerLeadIn + tailOut;
      const visibleClip = intersectTimeRange(
        { start: authoredClipStart, end: scene.range.end + tailOut },
        renderRange
      );
      if (!visibleClip) continue;
      const clipStart = visibleClip.start - renderRange.start;
      const clipDuration = visibleClip.end - visibleClip.start;
      const clipMediaStart = Math.max(
        0,
        mediaStart + (visibleClip.start - scene.range.start) * playbackRate
      );
      const visual = layer.assetPath ? layer.mediaKind === "image" || layer.source === "generated_image" ? `<img class="${classAttribute("visual", layer.className)}" src="${escapeHtml2(assetUrl(layer.assetPath))}"${styleAttribute(visualStyle)} />` : `<video id="${clipId}-media" class="${classAttribute("clip visual", layer.className)}" src="${escapeHtml2(assetUrl(layer.assetPath))}" muted playsinline data-start="${seconds2(clipStart)}" data-duration="${seconds2(clipDuration)}" data-track-index="${sceneTrack(sceneIndex, 2 + layerIndex)}" data-media-start="${seconds2(clipMediaStart)}" data-playback-rate="${seconds2(playbackRate)}"${styleAttribute(visualStyle)}></video>` : `<div class="${classAttribute("visual motion", layer.className)}"${styleAttribute(visualStyle)}></div>`;
      const cursorOverlay = cursorOverlayMarkup(
        layer,
        scene.range.start,
        scene.range.end + tailOut,
        sceneIndex,
        layerIndex,
        contained ?? viewport,
        timeline
      );
      if (layer.cameraMotion?.shake)
        cameraShakeStatements(
          cursorOverlay && !cropped ? `#${clipId},#${cursorClipId}` : `#${clipId}`,
          layer.cameraMotion.shake,
          scene.range.start,
          authoredSceneDuration,
          timeline
        );
      const cameraMarkup = `<div id="${cameraId}" class="camera"${cameraBoxStyle}>${visual}${cropped ? cursorOverlay : ""}</div>`;
      const mediaMarkup = cropped ? `<div class="crop-viewport"${cropViewportStyle}>${cameraMarkup}</div>` : cameraMarkup;
      if (isVideo) timeline.push(
        `tl.set("#${clipId}",{visibility:"hidden"},0);`,
        `tl.set("#${clipId}",{visibility:"visible"},${seconds2(visibleClip.start)});`,
        `tl.set("#${clipId}",{visibility:"hidden"},${seconds2(visibleClip.end)});`
      );
      stagedBlocks.push(
        isVideo ? `<div id="${clipId}" class="visual-clip" style="z-index:${SCENE_STACK.footage + layerIndex};visibility:hidden">${mediaMarkup}</div>` : `<div id="${clipId}" class="clip visual-clip" data-start="${seconds2(clipStart)}" data-duration="${seconds2(clipDuration)}" data-track-index="${sceneTrack(sceneIndex, 2 + layerIndex)}" style="z-index:${SCENE_STACK.footage + layerIndex}">${mediaMarkup}</div>`
      );
      if (isVideo && layer.audioGainDb !== void 0 && visibleSceneRange)
        sceneBlocks.push(
          `<audio id="audio-visual-${sceneIndex}-${layerIndex}" class="clip" data-start="${seconds2(sceneStart)}" data-duration="${seconds2(sceneDuration)}" data-track-index="${30 + layerIndex}" data-media-start="${seconds2(visibleMediaStart)}" data-playback-rate="${seconds2(playbackRate)}" data-volume="${decibelsToAmplitude(layer.audioGainDb)}" src="${escapeHtml2(assetUrl(layer.assetPath))}"></audio>`
        );
      if (cursorOverlay && !cropped)
        stagedBlocks.push(
          `<div id="${cursorClipId}" class="clip cursor-clip" data-start="${seconds2(clipStart)}" data-duration="${seconds2(clipDuration)}" data-track-index="${sceneTrack(sceneIndex, 20 + layerIndex)}" style="z-index:${SCENE_STACK.cursor + layerIndex}"><div id="${cursorCameraId}" class="cursor-camera"${cameraBoxStyle}>${cursorOverlay}</div></div>`
        );
      const layerTarget = cursorOverlay && !cropped ? `#${clipId},#${cursorClipId}` : `#${clipId}`;
      if (layer.enterAnimation)
        timeline.push(
          animationStatement(layerTarget, layer.enterAnimation, scene.range.start)
        );
      if (layer.exitAnimation)
        timeline.push(
          animationStatement(
            layerTarget,
            layer.exitAnimation,
            Math.max(
              scene.range.start,
              scene.range.end - layer.exitAnimation.durationSeconds
            )
          )
        );
      if (isVideo && layer.assetPath && LIFT_RECIPE_IDS.has(scene.recipe?.id ?? "") && layerIndex === 0)
        stagedBlocks.push(
          liftLayersMarkup({
            scene,
            sceneIndex,
            layerIndex,
            mediaUrl: assetUrl(layer.assetPath),
            clipStart,
            clipDuration,
            mediaStart: clipMediaStart,
            playbackRate,
            trackIndex: sceneTrack(sceneIndex, LIFT_TRACK_OFFSET),
            project,
            timeline
          })
        );
      const cameraTarget = cursorOverlay && !cropped ? `#${cameraId},#${cursorCameraId}` : `#${cameraId}`;
      if (layer.cameraMotion?.keyframes.length) {
        const keyframes = layer.cameraMotion.keyframes;
        const withFilter = keyframes.some((keyframe) => keyframe.blur !== void 0);
        const overflow = coverOverflow(
          layer.mediaWidth,
          layer.mediaHeight,
          viewport.width,
          viewport.height
        );
        const first = keyframes[0];
        const firstTransform = layer.crop ? croppedCameraTransform(first, layer.crop) : cameraTransform(first, viewport.width, viewport.height, withFilter, overflow);
        if (first.atSeconds === 0)
          timeline.push(
            `tl.set(${safeJson(cameraTarget)},${safeJson(firstTransform)},${seconds2(authoredClipStart)});`
          );
        else
          timeline.push(
            `tl.set(${safeJson(cameraTarget)},{scale:1,x:0,y:0},${seconds2(authoredClipStart)});`,
            `tl.to(${safeJson(cameraTarget)},{...${safeJson(firstTransform)},duration:${seconds2(first.atSeconds)},ease:${safeJson(first.easing)}},${seconds2(scene.range.start)});`
          );
        for (let index = 1; index < keyframes.length; index += 1) {
          const previous = keyframes[index - 1];
          const keyframe = keyframes[index];
          timeline.push(
            `tl.to(${safeJson(cameraTarget)},{...${safeJson(layer.crop ? croppedCameraTransform(keyframe, layer.crop) : cameraTransform(keyframe, viewport.width, viewport.height, withFilter, overflow))},duration:${seconds2(keyframe.atSeconds - previous.atSeconds)},ease:${safeJson(keyframe.easing)}},${seconds2(scene.range.start + previous.atSeconds)});`
          );
        }
      } else if (isVideo && breathe && !contained && !cropped) {
        const drift = seconds2(
          (sceneIndex % 2 === 0 ? 1 : -1) * viewport.width * BREATHE_DRIFT_RATIO
        );
        timeline.push(
          `tl.fromTo(${safeJson(cameraTarget)},${safeJson({ scale: 1, x: 0, y: 0 })},${safeJson({ scale: BREATHE_SCALE, x: drift, y: 0, duration: seconds2(authoredClipDuration), ease: "sine.inOut" })},${seconds2(authoredClipStart)});`
        );
      }
    }
    const motionStack = motionLayerStack(scene);
    for (const [layerIndex, layer] of (scene.motionLayers ?? []).entries()) {
      const visibleLayerRange = intersectTimeRange(layer.range, renderRange);
      if (!visibleLayerRange) continue;
      const layerId = `motion-layer-${sceneIndex}-${layerIndex}`;
      const markup = motionNodeMarkup(layer, sceneIndex, layerIndex, assetUrl);
      sceneBlocks.push(
        `<div id="${layerId}" class="${classAttribute("clip motion-layer", layer.className)}" data-start="${seconds2(visibleLayerRange.start - renderRange.start)}" data-duration="${seconds2(visibleLayerRange.end - visibleLayerRange.start)}" data-track-index="${layer.zIndex}"${styleAttribute({ ...layer.style ?? {}, zIndex: motionStack[layerIndex] })}>${markup}</div>`
      );
      for (const step of layer.timeline)
        timeline.push(motionTimelineStatement(step, layer, sceneIndex, layerIndex));
    }
    for (const [captionIndex, caption] of scene.captions.entries()) {
      const visibleCaptionRange = intersectTimeRange(caption.range, renderRange);
      if (!visibleCaptionRange) continue;
      const captionId = `caption-${sceneIndex}-${captionIndex}`;
      const { box, text } = splitCaptionStyle(caption.style);
      const captionStyle = {
        left: `${caption.bbox.x * 100}%`,
        top: `${caption.bbox.y * 100}%`,
        width: `${caption.bbox.width * 100}%`,
        height: `${caption.bbox.height * 100}%`,
        ...box
      };
      sceneBlocks.push(
        `<div id="${captionId}" class="clip caption" data-start="${seconds2(visibleCaptionRange.start - renderRange.start)}" data-duration="${seconds2(visibleCaptionRange.end - visibleCaptionRange.start)}" data-track-index="${captionTrack(caption.range)}"${styleAttribute({ ...captionStyle, zIndex: SCENE_STACK.caption + captionIndex })}><span class="${classAttribute("caption-text", caption.className)}"${styleAttribute(text)}>${escapeHtml2(caption.text)}</span></div>`
      );
      if (caption.enterAnimation)
        timeline.push(
          animationStatement(
            `#${captionId}`,
            caption.enterAnimation,
            caption.range.start
          )
        );
      if (caption.exitAnimation)
        timeline.push(
          animationStatement(
            `#${captionId}`,
            caption.exitAnimation,
            caption.range.end - caption.exitAnimation.durationSeconds
          )
        );
    }
    const recipeId = scene.recipe?.id;
    for (const [graphicIndex, graphic] of (scene.graphics ?? []).entries()) {
      const visibleGraphicRange = intersectTimeRange(graphic.range, renderRange);
      if (!visibleGraphicRange) continue;
      const graphicId = `graphic-${sceneIndex}-${graphicIndex}`;
      const bodyId = `${graphicId}-body`;
      const text = graphicInnerMarkup(recipeId, graphic.text);
      const marker = recipeId === "marker-underline" && graphicIndex === 0 ? `<i class="marker-underline" style="--marker-thickness:${seconds2(recipeNumber(scene.recipe, "thickness", 10))}px"></i>` : "";
      sceneBlocks.push(
        `<div id="${graphicId}" class="clip graphic" data-start="${seconds2(visibleGraphicRange.start - renderRange.start)}" data-duration="${seconds2(visibleGraphicRange.end - visibleGraphicRange.start)}" data-track-index="${graphicTrack(graphic.range)}" style="z-index:${SCENE_STACK.graphic + graphicIndex}"><div id="${bodyId}" class="${classAttribute(`graphic-body graphic-${graphic.kind} graphic-${graphic.position}${recipeId === "gradient-word-sweep" ? " gradient-sweep" : ""}`, graphic.className)}"${styleAttribute(graphic.style)}>${text}${marker}</div></div>`
      );
      if (graphic.enterAnimation)
        timeline.push(
          animationStatement(`#${bodyId}`, graphic.enterAnimation, graphic.range.start)
        );
      if (graphic.exitAnimation)
        timeline.push(
          animationStatement(
            `#${bodyId}`,
            graphic.exitAnimation,
            graphic.range.end - graphic.exitAnimation.durationSeconds
          )
        );
    }
    const recipeMarkup = recipeOverlayMarkup(scene, sceneIndex, project, renderRange);
    if (recipeMarkup) sceneBlocks.push(recipeMarkup);
    sceneBlocks.unshift(...stagedBlocks);
    const sceneClassName = classAttribute(
      "scene",
      [
        scene.shotRole ? `shot-role-${scene.shotRole}` : "",
        scene.recipe ? `recipe-${scene.recipe.id}` : ""
      ].filter(Boolean).join(" ")
    );
    blocks.push(
      `<section id="${sceneId}" class="${sceneClassName}">${sceneBlocks.join("")}</section>`
    );
    if (isStructuredTransition(scene.transitionIn))
      timeline.push(animationStatement(`#${sceneId}`, scene.transitionIn, scene.range.start));
    if (isStructuredTransition(scene.transitionOut))
      timeline.push(
        animationStatement(
          `#${sceneId}`,
          scene.transitionOut,
          Math.max(
            scene.range.start,
            scene.range.end - scene.transitionOut.durationSeconds
          )
        )
      );
    appendAudioTransitionStatements(
      scene,
      sceneIndex,
      scene.transitionIn,
      "in",
      timeline,
      renderRange
    );
    appendAudioTransitionStatements(
      scene,
      sceneIndex,
      scene.transitionOut,
      "out",
      timeline,
      renderRange
    );
    if (scene.enterAnimation)
      timeline.push(
        animationStatement(`#${sceneId}`, scene.enterAnimation, scene.range.start)
      );
    if (scene.exitAnimation)
      timeline.push(
        animationStatement(
          `#${sceneId}`,
          scene.exitAnimation,
          scene.range.end - scene.exitAnimation.durationSeconds
        )
      );
    applyShotRecipe(scene, sceneIndex, timeline, {
      accentColor: brandStyle.accentColor,
      viewport
    });
  }
  const timelineProgress = timelineProgressMarkup(project, renderRange, timeline);
  if (timelineProgress) blocks.push(timelineProgress);
  const transitionUsage = [];
  for (let index = 0; index < project.scenes.length - 1; index += 1) {
    const previous = project.scenes[index];
    const current = project.scenes[index + 1];
    const transition = boundaryTransitions[index];
    if (!transition) continue;
    const markup = isFxTransition(transition.id) ? fxTransitionMarkup(
      transition,
      index,
      current.range.start,
      brandStyle.accentColor,
      TRANSITION_TRACK,
      renderRange
    ) : transitionOverlayMarkup(transition, index, current.range.start, renderRange);
    if (markup) transitionBlocks.push(markup);
    if (!applyFxTransition(transition, index, current, timeline))
      applyTransition(transition, index, current, timeline);
    transitionUsage.push({
      boundaryIndex: index,
      fromSceneId: previous.id,
      toSceneId: current.id,
      transition,
      overlapSeconds: transitionOverlapSeconds(transition)
    });
  }
  const baseCss = `*{box-sizing:border-box}html,body{margin:0;width:100%;height:100%;overflow:hidden;background:#000}main{position:relative;width:${project.width}px;height:${project.height}px;overflow:hidden}.scene,.visual-clip,.camera,.visual,.motion,.motion-layer,.cursor-clip,.cursor-camera,.spatial-layer{position:absolute;inset:0;width:100%;height:100%}.spatial-layer{overflow:hidden;pointer-events:none}.spatial-layer canvas{display:block;width:100%;height:100%}.scene,.visual-clip,.camera,.motion-layer,.cursor-clip,.cursor-camera{overflow:hidden;transform-origin:50% 50%}video.visual,img.visual{object-fit:cover;object-position:50% 50%}.motion-layer,.motion-node{pointer-events:none}.caption,.graphic{position:absolute}.caption{display:flex;align-items:center}.caption-text{display:inline-block;max-width:100%;white-space:nowrap}.graphic{inset:0;pointer-events:none}.graphic-body{position:relative}.word{display:inline-block;white-space:pre;will-change:transform,filter}.marker-underline{position:absolute;left:0;bottom:-.08em;height:var(--marker-thickness,10px);width:100%;border-radius:999px;background:var(--recipe-accent);opacity:.92;transform:scaleX(0);transform-origin:0 50%}.cursor-overlay,.cursor-click,.cursor-ghost{position:absolute;left:0;top:0;pointer-events:none;transform-origin:0 0}.cursor-ghost{border-radius:50%;filter:blur(1px)}.cursor-overlay svg{display:block;width:100%;height:100%;overflow:visible}.cursor-click-body{transform-origin:50% 50%}.recipe-overlay,.transition-overlay{position:absolute;pointer-events:none}.recipe-spotlight{inset:-20%;background:radial-gradient(circle at 50% 45%,rgba(255,255,255,.3),transparent 48%);mix-blend-mode:screen}.recipe-callout{border:3px solid var(--recipe-accent);border-radius:8px;box-shadow:0 0 0 9999px rgba(0,0,0,.24),0 0 30px color-mix(in srgb,var(--recipe-accent) 55%,transparent)}.recipe-callout span{position:absolute;right:-8px;top:-8px;width:16px;height:16px;border:3px solid #fff;border-radius:50%;background:var(--recipe-accent);box-shadow:0 0 18px var(--recipe-accent)}.recipe-step-rail{left:8%;right:8%;bottom:8%;height:48px;display:flex;align-items:center;justify-content:space-between}.recipe-step-rail::before{content:"";position:absolute;left:24px;right:24px;top:50%;height:3px;transform:translateY(-50%);background:rgba(255,255,255,.34);box-shadow:0 6px 18px rgba(0,0,0,.3)}.recipe-step-rail b{position:relative;width:46px;height:46px;border-radius:50%;display:flex;align-items:center;justify-content:center;font:700 20px/1 Inter,"PingFang SC",sans-serif;color:#fff;background:rgba(20,24,32,.72);border:2px solid rgba(255,255,255,.7);box-shadow:0 8px 24px rgba(0,0,0,.32)}.recipe-comparison-divider{left:50%;top:0;bottom:0;width:4px;background:#fff;box-shadow:0 0 24px rgba(0,0,0,.45)}.recipe-comparison-divider span{position:absolute;left:50%;top:50%;width:42px;height:42px;border:2px solid #fff;border-radius:50%;background:var(--recipe-accent);transform:translate(-50%,-50%);box-shadow:0 8px 24px rgba(0,0,0,.32)}.recipe-pressure-vignette{inset:0;box-shadow:inset 0 0 160px rgba(150,0,20,.42)}.transition-overlay{inset:0;overflow:hidden}.transition-whip-pan span{position:absolute;left:-20%;top:42%;width:140%;height:16%;background:linear-gradient(90deg,transparent,rgba(255,255,255,.9),transparent);filter:blur(16px)}.transition-hidden-cut{background:var(--transition-color)}.transition-zoom-through{background:radial-gradient(circle,rgba(255,255,255,.92),rgba(255,255,255,.14) 34%,transparent 68%)}.transition-match-cut{background:rgba(255,255,255,.92)}.recipe-push-vignette{inset:0;box-shadow:inset 0 0 240px rgba(0,0,0,.9);opacity:0}.recipe-impact-flash{inset:0;background:#fff;opacity:0}.recipe-glint{overflow:hidden}.recipe-glint span{position:absolute;top:-20%;bottom:-20%;left:0;width:var(--glint-width,22%);background:linear-gradient(100deg,transparent,rgba(255,255,255,.5) 45%,rgba(255,255,255,.78) 50%,rgba(255,255,255,.5) 55%,transparent);transform:skewX(-14deg);mix-blend-mode:screen}.recipe-sweep-mask{background:#000;-webkit-mask-image:radial-gradient(circle at var(--spot-x,0%) 50%,transparent 0,transparent 16%,#000 40%);mask-image:radial-gradient(circle at var(--spot-x,0%) 50%,transparent 0,transparent 16%,#000 40%)}.recipe-skeleton{overflow:hidden;background:rgba(12,16,24,.94)}.recipe-skeleton i{position:absolute;left:6%;height:7%;border-radius:999px;background:linear-gradient(90deg,rgba(255,255,255,.14) 0%,rgba(255,255,255,.36) 50%,rgba(255,255,255,.14) 100%);background-size:200% 100%}.recipe-brand-frame{inset:0}.recipe-brand-frame i{position:absolute;background:var(--recipe-accent)}.recipe-brand-frame .bf-top{left:0;right:0;top:0;height:0}.recipe-brand-frame .bf-bottom{left:0;right:0;bottom:0;height:0}.recipe-brand-frame .bf-left{top:0;bottom:0;left:0;width:0}.recipe-brand-frame .bf-right{top:0;bottom:0;right:0;width:0}.recipe-scan{overflow:hidden}.recipe-scan .scan-line{position:absolute;left:0;right:0;height:3px;background:linear-gradient(90deg,transparent,var(--recipe-accent),transparent);box-shadow:0 0 18px var(--recipe-accent);opacity:0}.recipe-scan .scan-target{position:absolute;opacity:0;box-shadow:0 0 0 9999px rgba(0,0,0,.28)}.recipe-scan .scan-target b{position:absolute;width:18px;height:18px;border:3px solid var(--recipe-accent)}.recipe-scan .c1{left:-2px;top:-2px;border-right:0;border-bottom:0}.recipe-scan .c2{right:-2px;top:-2px;border-left:0;border-bottom:0}.recipe-scan .c3{left:-2px;bottom:-2px;border-right:0;border-top:0}.recipe-scan .c4{right:-2px;bottom:-2px;border-left:0;border-top:0}.flap{display:inline-block;perspective:420px;margin:0 .04em}.flap b{display:inline-block;font-weight:inherit;transform-origin:50% 50%;backface-visibility:hidden}.tw{opacity:0}.tw-caret{display:inline-block;width:.08em;height:1em;margin-left:.06em;background:currentColor;vertical-align:-.12em}.odo{display:inline-block;height:1em;line-height:1;overflow:hidden;vertical-align:baseline;font-variant-numeric:tabular-nums}.odo-strip{display:block}.odo-strip i{display:block;height:1em;line-height:1;font-style:normal}.odo-static{display:inline-block;line-height:1}.graphic-body.gradient-sweep{background:linear-gradient(100deg,var(--brand-text) 0 40%,var(--recipe-accent) 50%,var(--brand-text) 60% 100%);background-size:250% 100%;-webkit-background-clip:text;background-clip:text;color:transparent}.list-marker{position:absolute;left:-.9em;top:.42em;width:.5em;height:.14em;border-radius:999px;background:var(--recipe-accent);transform:scaleX(0);transform-origin:0 50%}.transition-white-flash{background:#fff}${project.presentation?.showTimelineProgress === true ? ".wandeo-timeline-progress{left:6%;right:6%;bottom:2.8%;height:2px;background:rgba(255,255,255,.18);z-index:9999}.wandeo-timeline-progress i{display:block;width:0;height:100%;background:var(--recipe-accent)}" : ""}${CINEMATIC_FX_CSS}`;
  const mainStyle = styleAttribute({
    background: brandStyle.backgroundColor,
    "--brand-primary": brandStyle.primaryColor,
    "--brand-accent": brandStyle.accentColor,
    "--brand-surface": brandStyle.pack?.colors.surface ?? "#ffffff",
    "--brand-text": brandStyle.pack?.colors.text ?? "#ffffff",
    "--brand-surface-radius": brandStyle.pack ? `${brandStyle.pack.surface.radiusPixels}px` : "8px",
    "--brand-surface-shadow": brandStyle.pack?.surface.shadow ?? "none",
    "--brand-motion-ease": brandStyle.pack?.motion.easing ?? "power2.out",
    "--recipe-accent": brandStyle.accentColor,
    "--transition-color": brandStyle.primaryColor,
    fontFamily: `${brandStyle.fontFamily},sans-serif`
  });
  const stylePackAttribute = brandStyle.pack ? ` data-style-pack="${escapeHtml2(brandStyle.pack.id)}"` : "";
  const isRangePreview = renderRange.start > 1e-4 || renderRange.end < project.durationSeconds - 1e-4;
  const timelineScript = isRangePreview ? `const sourceTl=gsap.timeline({paused:true});const tl=sourceTl;${timeline.join("")}sourceTl.to({},{duration:${seconds2(project.durationSeconds)},ease:"none"},0);const renderTl=gsap.timeline({paused:true});renderTl.fromTo(sourceTl,{time:${seconds2(renderRange.start)}},{time:${seconds2(renderRange.end)},duration:${seconds2(renderDuration)},ease:"none"},0);window.__timelines=window.__timelines||{};window.__timelines[${safeJson(project.projectId)}]=renderTl;window.__wandeoTimeline=renderTl;` : `const tl=gsap.timeline({paused:true});${timeline.join("")}tl.to({},{duration:${seconds2(project.durationSeconds)},ease:"none"},0);window.__timelines=window.__timelines||{};window.__timelines[${safeJson(project.projectId)}]=tl;window.__wandeoTimeline=tl;`;
  let spatialRuntimeScriptTag = "";
  let spatialRuntimeBundleCopy;
  let spatialBootstrap2 = "";
  if (spatialEntries.length) {
    const needsThree = spatialEntries.some((entry) => entry.backend === "three");
    const needsAnatomy = spatialEntries.some((entry) => entry.backend === "anatomy");
    const runtimePath = resolveSpatialRuntimeBundle();
    const anatomyRuntimePath = resolveAnatomyRuntimeBundle();
    if (needsThree && !await fileExists(runtimePath)) throw new Error(`Spatial runtime bundle is missing at ${runtimePath}; run npm run build.`);
    if (needsAnatomy && !await fileExists(anatomyRuntimePath)) throw new Error(`Anatomy runtime bundle is missing at ${anatomyRuntimePath}; run npm run build.`);
    if (needsThree && !(await fs7.readFile(runtimePath, "utf8")).includes("__wandeoSpatial")) throw new Error("Spatial runtime bundle does not expose __wandeoSpatial.");
    if (needsAnatomy && !(await fs7.readFile(anatomyRuntimePath, "utf8")).includes("__wandeoAnatomy")) throw new Error("Anatomy runtime bundle does not expose __wandeoAnatomy.");
    spatialRuntimeBundleCopy = Promise.all([
      needsThree ? fs7.copyFile(runtimePath, path9.join(outputDir, "spatial-runtime.js")) : void 0,
      needsAnatomy ? fs7.copyFile(anatomyRuntimePath, path9.join(outputDir, "anatomy-runtime.js")) : void 0
    ]).then(() => void 0);
    const runtimeUrl = (name) => "/" + path9.relative(projectDir, path9.join(outputDir, name)).split(path9.sep).map(encodeURIComponent).join("/");
    spatialRuntimeScriptTag = `${needsThree ? `<script src="${runtimeUrl("spatial-runtime.js")}"></script>` : ""}${needsAnatomy ? `<script src="${runtimeUrl("anatomy-runtime.js")}"></script>` : ""}`;
    const entries = spatialEntries.map((entry) => `{sceneId:${safeJson(entry.sceneId)},canvasId:${safeJson(entry.canvasId)},backend:${safeJson(entry.backend)},config:${entry.config}}`).join(",");
    spatialBootstrap2 = spatialBootstrap(`[${entries}]`, renderRange.start);
  }
  const outputSizeMetadata = renderScale === 1 ? "" : ` data-output-width="${renderWidth}" data-output-height="${renderHeight}"`;
  const body2 = `<body><main id="composition-root" data-composition-id="${escapeHtml2(project.projectId)}" ${stylePackAttribute} data-start="0" data-duration="${seconds2(renderDuration)}" data-width="${project.width}" data-height="${project.height}"${outputSizeMetadata} data-fps="${renderFps}"${mainStyle}>${environmentBlock}${blocks.join("")}${transitionBlocks.join("")}${postFxBlock}</main><script>${CAPTION_FIT_SCRIPT}</script><script>${gsapSource}</script>${spatialRuntimeScriptTag}<script>(function(){${timelineScript}})();</script>${spatialBootstrap2 ? `<script>${spatialBootstrap2}</script>` : ""}</body>`;
  const authoredCss = `${baseCss}${authoredStylesheet(project.stylesheet)}`;
  const bundledFontCss = await prepareBundledFontFaces(`${authoredCss}${body2}`, projectDir);
  const html = `<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><style>${bundledFontCss}${baseCss}${authoredStylesheet(project.stylesheet)}html,body,body *{cursor:none!important}</style></head>${body2}</html>`;
  const compositionPath = path9.join(outputDir, "index.html");
  await Promise.all([
    spatialRuntimeBundleCopy,
    fs7.writeFile(compositionPath, html, "utf8"),
    fs7.copyFile(gsapBundlePath, path9.join(outputDir, "gsap.min.js")),
    fs7.writeFile(
      path9.join(outputDir, "video-project.json"),
      `${JSON.stringify(project, null, 2)}
`,
      "utf8"
    ),
    fs7.writeFile(
      path9.join(outputDir, "shot-recipe-usage.json"),
      `${JSON.stringify(
        {
          schemaVersion: "1.0.0",
          stylePack: brandStyle.pack ?? null,
          soundEffects: project.scenes.flatMap(
            (scene) => (scene.soundEffects ?? []).map(
              ({ assetPath: _assetPath, ...soundEffect }) => ({
                sceneId: scene.id,
                ...soundEffect
              })
            )
          ),
          recipes: project.scenes.flatMap(
            (scene, sceneIndex) => scene.recipe ? [
              {
                sceneId: scene.id,
                sceneIndex,
                shotRole: scene.shotRole ?? null,
                selection: scene.recipe,
                manifest: getShotRecipe(scene.recipe.id)
              }
            ] : []
          ),
          transitions: transitionUsage,
          environment: brandStyle.environment
        },
        null,
        2
      )}
`,
      "utf8"
    )
  ]);
  return compositionPath;
}
function resolveHyperFramesCli() {
  const packagePath = nodeRequire2.resolve("hyperframes/package.json");
  return path9.join(path9.dirname(packagePath), "bin", "hyperframes.mjs");
}
function hyperFramesChildProcessOptions(options2, platform = process.platform) {
  const normalized = options2 && typeof options2 === "object" ? options2 : {};
  return {
    ...normalized,
    ...platform === "win32" ? { detached: false } : {},
    windowsHide: true
  };
}
var HYPERFRAMES_HIDDEN_CHILD_RUNNER = `"use strict";
const childProcess = require("node:child_process");
const { syncBuiltinESMExports } = require("node:module");
const { pathToFileURL } = require("node:url");
const hidden = ${hyperFramesChildProcessOptions.toString()};
const originalSpawn = childProcess.spawn;
childProcess.spawn = function(command, args, options) {
  return Array.isArray(args)
    ? originalSpawn.call(this, command, args, hidden(options))
    : originalSpawn.call(this, command, hidden(args));
};
const originalSpawnSync = childProcess.spawnSync;
childProcess.spawnSync = function(command, args, options) {
  return Array.isArray(args)
    ? originalSpawnSync.call(this, command, args, hidden(options))
    : originalSpawnSync.call(this, command, hidden(args));
};
const originalExecFile = childProcess.execFile;
childProcess.execFile = function(file, args, options, callback) {
  if (!Array.isArray(args)) return originalExecFile.call(this, file, hidden(args), options);
  if (typeof options === "function") return originalExecFile.call(this, file, args, hidden(), options);
  return originalExecFile.call(this, file, args, hidden(options), callback);
};
const originalExecFileSync = childProcess.execFileSync;
childProcess.execFileSync = function(file, args, options) {
  return Array.isArray(args)
    ? originalExecFileSync.call(this, file, args, hidden(options))
    : originalExecFileSync.call(this, file, hidden(args));
};
const originalExec = childProcess.exec;
childProcess.exec = function(command, options, callback) {
  if (typeof options === "function") return originalExec.call(this, command, hidden(), options);
  return originalExec.call(this, command, hidden(options), callback);
};
const originalExecSync = childProcess.execSync;
childProcess.execSync = function(command, options) {
  return originalExecSync.call(this, command, hidden(options));
};
const originalFork = childProcess.fork;
childProcess.fork = function(modulePath, args, options) {
  return Array.isArray(args)
    ? originalFork.call(this, modulePath, args, hidden(options))
    : originalFork.call(this, modulePath, [], hidden(args));
};
syncBuiltinESMExports();
if(process.env.WANDEO_SPATIAL_LOADER)require("node:module").register(pathToFileURL(process.env.WANDEO_SPATIAL_LOADER).href,pathToFileURL(__filename).href);
const cliPath = process.argv[2];
if (!cliPath) throw new Error("HyperFrames CLI path is required.");
process.argv.splice(1, 2, cliPath);
import(pathToFileURL(cliPath).href).catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
`;
async function writeHiddenChildRunner(projectDir) {
  const runtimeDirectory = path9.join(projectDir, "runtime");
  const runnerPath = path9.join(runtimeDirectory, "hyperframes-hidden-child-runner.cjs");
  await fs7.mkdir(runtimeDirectory, { recursive: true });
  await fs7.writeFile(runnerPath, HYPERFRAMES_HIDDEN_CHILD_RUNNER, "utf8");
  return runnerPath;
}
function resolveRenderWorkerCount(cpuCount = os4.cpus().length, override = process.env.AUTO_EDITOR_RENDER_WORKERS) {
  const requested = Number(override);
  if (Number.isInteger(requested) && requested >= 1) return Math.min(requested, 12);
  return Math.max(2, Math.min(8, Math.floor(cpuCount / 2)));
}
function resolveRenderEncoding(platform = process.platform, qualityOverride = process.env.AUTO_EDITOR_RENDER_QUALITY, gpuOverride = process.env.AUTO_EDITOR_RENDER_GPU) {
  const quality = ["draft", "standard", "high"].includes(qualityOverride?.trim() ?? "") ? qualityOverride?.trim() : "standard";
  const gpuFlag = gpuOverride?.trim();
  const gpu = gpuFlag === "1" || gpuFlag === "true" || (gpuFlag === void 0 || gpuFlag === "" ? false : false);
  return { quality, gpu };
}
function parseHyperFramesTraceLine(line) {
  const marker = "[Render:trace]";
  const index = line.indexOf(marker);
  if (index < 0) {
    if (!line.includes("Transient browser failure during capture; retrying")) return null;
    try {
      const detail = JSON.parse(line.slice(line.indexOf("{")));
      return {
        phase: "capture_retry",
        status: "retry",
        ...typeof detail.renderJobId === "string" ? { renderJobId: detail.renderJobId } : {},
        ...typeof detail.transientRetriesUsed === "number" ? { transientRetriesUsed: detail.transientRetriesUsed } : {}
      };
    } catch {
      return null;
    }
  }
  const json2 = line.slice(index + marker.length).trim();
  try {
    const parsed = JSON.parse(json2);
    if (typeof parsed.phase !== "string") return null;
    const number2 = (value) => typeof value === "number" && Number.isFinite(value) ? value : void 0;
    return {
      phase: parsed.phase,
      ...typeof parsed.renderJobId === "string" ? { renderJobId: parsed.renderJobId } : {},
      ...Object.fromEntries(
        ["elapsedMs", "durationMs", "workerCount", "transientRetriesUsed"].filter((key) => number2(parsed[key]) !== void 0).map((key) => [key, parsed[key]])
      ),
      ...typeof parsed.status === "string" ? { status: parsed.status } : {},
      ...number2(parsed.framesCompleted) !== void 0 ? { framesCompleted: number2(parsed.framesCompleted) } : {},
      ...number2(parsed.totalFrames) !== void 0 ? { totalFrames: number2(parsed.totalFrames) } : {},
      ...typeof parsed.message === "string" ? { message: parsed.message.slice(0, 200) } : {}
    };
  } catch {
    return null;
  }
}
var HYPERFRAMES_STDERR_TAIL_BYTES = 256 * 1024;
var HYPERFRAMES_INACTIVITY_ERROR_NAME = "HyperFramesInactivityError";
async function renderWithHyperFrames(compositionPath, outputPath, signal, projectDir = path9.dirname(compositionPath), onProgress, options2 = {}) {
  await fs7.mkdir(path9.dirname(outputPath), { recursive: true });
  const runnerPath = await writeHiddenChildRunner(projectDir);
  let loaderPath;
  if (options2.spatial) {
    const packagePath = nodeRequire2.resolve("hyperframes/package.json");
    if (JSON.parse(await fs7.readFile(packagePath, "utf8")).version !== "0.8.3") throw new Error("HYPERFRAMES_CAPTURE_ADAPTER_VERSION: expected 0.8.3");
    loaderPath = path9.join(projectDir, "runtime", "spatial-loader.mjs");
    await fs7.writeFile(loaderPath, spatialLoaderSource(pathToFileURL2(path9.join(path9.dirname(packagePath), "dist", "cli.js")).href));
  }
  const compositionEntry = path9.relative(projectDir, compositionPath).replace(/\\/g, "/");
  const browserStartedAt = Date.now();
  onProgress?.({ phase: "browser_resolve", status: "start" });
  const browserPath2 = await resolveHyperFramesBrowserPath();
  onProgress?.({
    phase: "browser_resolve",
    status: "end",
    durationMs: Date.now() - browserStartedAt
  });
  const encoding = resolveRenderEncoding();
  const args = [
    runnerPath,
    resolveHyperFramesCli(),
    "render",
    "-c",
    compositionEntry,
    "-o",
    outputPath,
    "--quality",
    encoding.quality,
    ...encoding.gpu ? ["--gpu"] : [],
    "--workers",
    String(resolveRenderWorkerCount()),
    ...options2.spatial ? ["--no-browser-gpu"] : [],
    projectDir
  ];
  const env = {
    ...process.env,
    ...getPackagedEsbuildEnvironment(),
    ...loaderPath ? { WANDEO_SPATIAL_LOADER: loaderPath } : {},
    ELECTRON_RUN_AS_NODE: "1",
    PRODUCER_FORCE_SCREENSHOT: "true",
    HYPERFRAMES_NO_UPDATE_CHECK: "1",
    HYPERFRAMES_NO_AUTO_INSTALL: "1",
    HYPERFRAMES_ALLOWED_FONT_DOWNLOADS: options2.allowedFontDownloads ?? "",
    HYPERFRAMES_FFMPEG_PATH: getFfmpegBinaryPath(),
    HYPERFRAMES_FFPROBE_PATH: getFfprobeBinaryPath(),
    ...options2.spatial ? { PRODUCER_BROWSER_GPU_MODE: "software" } : {},
    ...browserPath2 ? {
      HYPERFRAMES_BROWSER_PATH: browserPath2,
      PRODUCER_HEADLESS_SHELL_PATH: browserPath2
    } : {}
  };
  await new Promise((resolve2, reject) => {
    if (signal?.aborted) {
      reject(new DOMException("Aborted", "AbortError"));
      return;
    }
    const startedAt = Date.now();
    onProgress?.({ phase: "renderer_process", status: "start" });
    const child = spawn2(process.execPath, args, { windowsHide: true, env });
    let stderr = "";
    let pendingLine = "";
    let lastOutputAt = Date.now();
    let lastPhase = "starting";
    let inactivityError;
    const inactivityTimeoutMs = options2.inactivityTimeoutMs;
    const watchdog = inactivityTimeoutMs && inactivityTimeoutMs > 0 ? setInterval(
      () => {
        if (Date.now() - lastOutputAt < inactivityTimeoutMs) return;
        inactivityError = Object.assign(
          new Error(
            `HyperFrames printed nothing for ${Math.round(inactivityTimeoutMs / 1e3)} s during ${lastPhase}; the renderer process was stopped.`
          ),
          { name: HYPERFRAMES_INACTIVITY_ERROR_NAME }
        );
        killProcessTree(child);
      },
      Math.min(5e3, inactivityTimeoutMs)
    ) : void 0;
    const consume = (chunk) => {
      const text = chunk.toString("utf8");
      lastOutputAt = Date.now();
      stderr = `${stderr}${text}`.slice(-HYPERFRAMES_STDERR_TAIL_BYTES);
      if (!onProgress && !options2.onSpatialEvidence) return;
      const lines = `${pendingLine}${text}`.split(/\r?\n/);
      pendingLine = lines.pop() ?? "";
      for (const line of lines) {
        if (line.startsWith(SPATIAL_CAPTURE_MARKER)) {
          try {
            options2.onSpatialEvidence?.(JSON.parse(line.slice(SPATIAL_CAPTURE_MARKER.length)));
          } catch {
          }
          continue;
        }
        const progress = parseHyperFramesTraceLine(line);
        if (!progress) continue;
        if (progress.phase) lastPhase = progress.phase;
        onProgress?.(progress);
      }
    };
    child.stdout?.on("data", consume);
    child.stderr?.on("data", consume);
    const onAbort = () => {
      killProcessTree(child);
      reject(new DOMException("Aborted", "AbortError"));
    };
    signal?.addEventListener("abort", onAbort, { once: true });
    child.on("error", (error) => {
      if (watchdog) clearInterval(watchdog);
      signal?.removeEventListener("abort", onAbort);
      reject(error);
    });
    child.on("close", (code, childSignal) => {
      if (watchdog) clearInterval(watchdog);
      onProgress?.({
        phase: "renderer_process",
        status: code === 0 ? "end" : "error",
        durationMs: Date.now() - startedAt
      });
      signal?.removeEventListener("abort", onAbort);
      if (inactivityError) {
        inactivityError.stderr = stderr;
        reject(inactivityError);
        return;
      }
      if (code === 0) {
        resolve2();
        return;
      }
      const error = new Error(
        `HyperFrames render failed (${code ?? childSignal}): ${stderr.slice(-12e3)}`
      );
      error.code = code;
      error.signal = childSignal;
      error.stderr = stderr;
      reject(error);
    });
  });
  return outputPath;
}
function assertSafeAudioFilter(value) {
  if (/[;\r\n]/.test(value) || /\b(?:a?movie|subtitles|ass|a?zmq|a?sendcmd)\s*=/i.test(value) || /(?:https?|ftp|file):/i.test(value))
    throw new Error(
      "VideoProject finalAudioFilter cannot access files, URLs, or extra graphs."
    );
}
async function probeRenderedStreams(filePath, signal) {
  const { stdout } = await execFileAsync(
    getFfprobeBinaryPath(),
    [
      "-v",
      "error",
      "-show_entries",
      "stream=codec_type,codec_name,pix_fmt,width,height,r_frame_rate,avg_frame_rate,sample_aspect_ratio,sample_rate",
      "-of",
      "json",
      filePath
    ],
    { encoding: "utf8", windowsHide: true, signal }
  );
  return (JSON.parse(stdout).streams ?? []).filter(Boolean);
}
function frameRate(value) {
  const [numerator, denominator] = (value ?? "").split("/").map(Number);
  return denominator ? numerator / denominator : Number.NaN;
}
function isDeliveryReadyVideo(stream, project) {
  if (!stream || stream.codec_type !== "video") return false;
  const sar = stream.sample_aspect_ratio;
  return stream.codec_name === "h264" && stream.pix_fmt === "yuv420p" && stream.width === project.width && stream.height === project.height && Math.abs(frameRate(stream.r_frame_rate) - project.fps) < 0.01 && Math.abs(frameRate(stream.avg_frame_rate) - project.fps) < 0.01 && (!sar || sar === "1:1" || sar === "0:1" || sar === "N/A");
}
async function normalizeFinalRender(project, renderedPath, outputPath, signal) {
  const streams = await probeRenderedStreams(renderedPath, signal);
  const video = streams.find((stream) => stream.codec_type === "video");
  const audio = streams.find((stream) => stream.codec_type === "audio");
  const copyVideo = isDeliveryReadyVideo(video, project);
  const args = ["-y", "-hide_banner", "-loglevel", "error", "-i", renderedPath];
  if (!copyVideo)
    args.push(
      "-vf",
      `fps=${project.fps},scale=${project.width}:${project.height}:flags=lanczos,setsar=1,format=yuv420p`
    );
  args.push("-map", "0:v:0");
  if (audio) {
    args.push("-map", "0:a:0");
    if (project.finalAudioFilter) {
      assertSafeAudioFilter(project.finalAudioFilter);
      args.push(
        "-af",
        project.finalAudioFilter,
        "-c:a",
        "aac",
        "-b:a",
        "192k",
        "-ar",
        "48000"
      );
    } else if (audio.codec_name === "aac" && audio.sample_rate === "48000")
      args.push("-c:a", "copy");
    else args.push("-c:a", "aac", "-b:a", "192k", "-ar", "48000");
  } else args.push("-an");
  args.push("-t", project.durationSeconds.toFixed(3));
  if (copyVideo) args.push("-c:v", "copy");
  else
    args.push(
      "-fps_mode",
      "cfr",
      "-c:v",
      "libx264",
      "-preset",
      "fast",
      "-crf",
      "18",
      "-pix_fmt",
      "yuv420p"
    );
  args.push("-movflags", "+faststart", outputPath);
  await execFileAsync(getFfmpegBinaryPath(), args, {
    windowsHide: true,
    maxBuffer: 32 * 1024 * 1024,
    signal
  });
  return outputPath;
}

// src/core/motionIntents.ts
var MOTION_FEELS = ["snappy", "default", "heavy", "playful"];
var MOTION_INTENT_MOVES = {
  enter: ["drop", "rise", "pop", "slide", "unfold", "fade"],
  exit: ["lift", "sink", "shrink", "slide", "fade"],
  emphasis: ["pulse", "land", "nudge", "shake"]
};
var BEAT_SNAP_WINDOW_SECONDS = 0.5;
var FEELS = {
  snappy: { travel: 0.3, settle: 0.28, overshoot: "back.out(1.4)", squash: 0.06, stagger: 0.04 },
  default: { travel: 0.45, settle: 0.38, overshoot: "back.out(1.7)", squash: 0.08, stagger: 0.06 },
  heavy: { travel: 0.6, settle: 0.5, overshoot: "back.out(1.15)", squash: 0.12, stagger: 0.09 },
  playful: {
    travel: 0.45,
    settle: 0.65,
    overshoot: "elastic.out(1, 0.45)",
    squash: 0.15,
    stagger: 0.07
  }
};
var TEXT_TAGS = /* @__PURE__ */ new Set(["text"]);
var round = (value) => Math.round(value * 1e3) / 1e3;
function assertIntent(intent, label) {
  if (!intent || typeof intent !== "object") throw new Error(`${label} is invalid.`);
  const moves = MOTION_INTENT_MOVES[intent.phase];
  if (!moves)
    throw new Error(`${label}.phase must be one of ${Object.keys(MOTION_INTENT_MOVES).join(", ")}.`);
  if (!moves.includes(intent.move))
    throw new Error(`${label}.move for ${intent.phase} must be one of ${moves.join(", ")}.`);
  if (!Number.isFinite(intent.at) || intent.at < 0) throw new Error(`${label}.at is invalid.`);
  if (intent.feel !== void 0 && !MOTION_FEELS.includes(intent.feel))
    throw new Error(`${label}.feel must be one of ${MOTION_FEELS.join(", ")}.`);
  if (intent.direction !== void 0 && !["left", "right", "up", "down"].includes(intent.direction))
    throw new Error(`${label}.direction must be left, right, up or down.`);
  if (intent.distance !== void 0 && (!Number.isFinite(intent.distance) || intent.distance <= 0))
    throw new Error(`${label}.distance must be a positive number of pixels.`);
  if (intent.onBeat !== void 0 && typeof intent.onBeat !== "boolean")
    throw new Error(`${label}.onBeat must be true or false.`);
}
function accentOffset(intent, stages) {
  if (intent.move === "drop" || intent.phase === "exit") return stages[1]?.offset ?? 0;
  return 0;
}
function nearestBeat(beats, time) {
  let best;
  for (const beat of beats)
    if (best === void 0 || Math.abs(beat - time) < Math.abs(best - time)) best = beat;
  return best !== void 0 && Math.abs(best - time) <= BEAT_SNAP_WINDOW_SECONDS ? best : void 0;
}
function stagesFor(intent, isText, canvas) {
  const feel = FEELS[intent.feel ?? "default"];
  const squash = isText ? 0 : feel.squash;
  const overshoot = isText && intent.feel === "playful" ? FEELS.default.overshoot : feel.overshoot;
  const vertical = intent.distance ?? Math.round(canvas.height * (isText ? 0.06 : 0.12));
  const horizontal = intent.distance ?? Math.round(canvas.width * (isText ? 0.05 : 0.14));
  const direction = intent.direction ?? "left";
  const sign = direction === "left" || direction === "up" ? -1 : 1;
  const axis = direction === "up" || direction === "down" ? "y" : "x";
  const along = axis === "y" ? vertical : horizontal;
  const { travel, settle: settle2 } = feel;
  switch (`${intent.phase}:${intent.move}`) {
    case "enter:drop":
      if (!squash)
        return [
          {
            offset: 0,
            method: "fromTo",
            from: { style: { opacity: 0, y: -vertical } },
            to: { style: { opacity: 1, y: 0 } },
            durationSeconds: round(travel + settle2 * 0.6),
            easing: overshoot
          }
        ];
      return [
        // Falls accelerating and stretched along its travel...
        {
          offset: 0,
          method: "fromTo",
          from: {
            style: {
              opacity: 0,
              y: -vertical,
              scaleX: round(1 - squash * 0.6),
              scaleY: round(1 + squash),
              transformOrigin: "50% 100%"
            }
          },
          to: { style: { opacity: 1, y: 0 } },
          durationSeconds: travel,
          easing: "power2.in"
        },
        // ...squashes on contact...
        {
          offset: travel,
          method: "to",
          to: { style: { scaleX: round(1 + squash), scaleY: round(1 - squash) } },
          durationSeconds: 0.07,
          easing: "power1.out"
        },
        // ...and springs back to rest.
        {
          offset: round(travel + 0.07),
          method: "to",
          to: { style: { scaleX: 1, scaleY: 1 } },
          durationSeconds: settle2,
          easing: overshoot
        }
      ];
    case "enter:rise":
      return [
        {
          offset: 0,
          method: "fromTo",
          from: { style: { opacity: 0, y: vertical } },
          to: { style: { opacity: 1, y: 0 } },
          durationSeconds: round(travel + settle2),
          easing: overshoot
        }
      ];
    case "enter:pop":
      return [
        {
          offset: 0,
          method: "fromTo",
          from: { style: { opacity: 0, scale: isText ? 0.85 : 0.6, transformOrigin: "50% 50%" } },
          to: { style: { opacity: 1, scale: 1 } },
          durationSeconds: round(travel + settle2),
          easing: overshoot
        }
      ];
    case "enter:slide":
      return [
        {
          offset: 0,
          method: "fromTo",
          from: { style: { opacity: 0, [axis]: sign * along } },
          to: { style: { opacity: 1, [axis]: 0 } },
          durationSeconds: round(travel + settle2),
          easing: intent.feel === "playful" ? overshoot : "expo.out"
        }
      ];
    case "enter:unfold":
      return [
        {
          offset: 0,
          method: "fromTo",
          from: { style: { opacity: 0, clipPath: "inset(0% 0% 100% 0%)" } },
          to: { style: { opacity: 1, clipPath: "inset(0% 0% 0% 0%)" } },
          durationSeconds: round(travel + settle2 * 0.5),
          easing: "power3.out"
        }
      ];
    case "enter:fade":
      return [
        {
          offset: 0,
          method: "fromTo",
          from: { style: { opacity: 0 } },
          to: { style: { opacity: 1 } },
          durationSeconds: travel,
          easing: "power2.out"
        }
      ];
    case "exit:lift":
    case "exit:sink": {
      const up = intent.move === "lift" ? -1 : 1;
      return [
        // A small counter-move first, then the exit accelerates away.
        {
          offset: 0,
          method: "to",
          to: { style: { y: round(-up * vertical * 0.05) } },
          durationSeconds: 0.12,
          easing: "power2.out"
        },
        {
          offset: 0.12,
          method: "to",
          to: { style: { y: up * vertical, opacity: 0 } },
          durationSeconds: travel,
          easing: "power3.in"
        }
      ];
    }
    case "exit:shrink":
      return [
        {
          offset: 0,
          method: "to",
          to: { style: { scale: 1.04, transformOrigin: "50% 50%" } },
          durationSeconds: 0.1,
          easing: "power2.out"
        },
        {
          offset: 0.1,
          method: "to",
          to: { style: { scale: 0.6, opacity: 0 } },
          durationSeconds: travel,
          easing: "power3.in"
        }
      ];
    case "exit:slide":
      return [
        {
          offset: 0,
          method: "to",
          to: { style: { [axis]: round(-sign * along * 0.04) } },
          durationSeconds: 0.1,
          easing: "power2.out"
        },
        {
          offset: 0.1,
          method: "to",
          to: { style: { [axis]: sign * along, opacity: 0 } },
          durationSeconds: travel,
          easing: "expo.in"
        }
      ];
    case "exit:fade":
      return [
        {
          offset: 0,
          method: "to",
          to: { style: { opacity: 0 } },
          durationSeconds: travel,
          easing: "power2.in"
        }
      ];
    case "emphasis:pulse":
      return [
        {
          offset: 0,
          method: "to",
          to: { style: { scale: isText ? 1.04 : 1.07, transformOrigin: "50% 50%" } },
          durationSeconds: 0.14,
          easing: "power2.out"
        },
        {
          offset: 0.14,
          method: "to",
          to: { style: { scale: 1 } },
          durationSeconds: settle2,
          easing: overshoot
        }
      ];
    case "emphasis:land":
      if (!squash) return stagesFor({ ...intent, move: "pulse" }, isText, canvas);
      return [
        {
          offset: 0,
          method: "to",
          to: {
            style: {
              scaleX: round(1 + squash),
              scaleY: round(1 - squash),
              transformOrigin: "50% 100%"
            }
          },
          durationSeconds: 0.07,
          easing: "power1.out"
        },
        {
          offset: 0.07,
          method: "to",
          to: { style: { scaleX: 1, scaleY: 1 } },
          durationSeconds: settle2,
          easing: overshoot
        }
      ];
    case "emphasis:nudge":
      return [
        {
          offset: 0,
          method: "to",
          to: { style: { x: Math.round(canvas.width * 6e-3) } },
          durationSeconds: 0.08,
          easing: "power2.out"
        },
        {
          offset: 0.08,
          method: "to",
          to: { style: { x: 0 } },
          durationSeconds: settle2,
          easing: overshoot
        }
      ];
    case "emphasis:shake":
      return [
        {
          offset: 0,
          method: "to",
          to: { style: { rotation: 2.5, transformOrigin: "50% 50%" } },
          durationSeconds: 0.06,
          easing: "sine.inOut",
          repeat: 5,
          yoyo: true
        },
        { offset: 0.36, method: "set", to: { style: { rotation: 0 } }, durationSeconds: 0 }
      ];
    default:
      throw new Error(`Unsupported motion intent ${intent.phase}:${intent.move}.`);
  }
}
var stageLength = (stages) => Math.max(
  ...stages.map(
    (stage) => stage.offset + stage.durationSeconds * ((stage.repeat ?? 0) + 1)
  )
);
function expandMotionIntents(project, beats = []) {
  let changed = false;
  const canvas = { width: project.width, height: project.height };
  const scenes = project.scenes.map((scene, sceneIndex) => {
    if (!scene.motionLayers?.some((layer) => layer.nodes.some((node) => "motion" in node)))
      return scene;
    changed = true;
    const motionLayers = scene.motionLayers.map((layer, layerIndex) => {
      const nodes = layer.nodes;
      if (!nodes.some((node) => node.motion)) return layer;
      const layerEnd = layer.timeBase === "film" ? layer.range.end : layer.range.end - layer.range.start;
      const label = `scenes[${sceneIndex}].motionLayers[${layerIndex}]`;
      const startsTaken = /* @__PURE__ */ new Map();
      const steps = [];
      const cleanNodes = nodes.map((node) => {
        const { motion, ...rest } = node;
        if (motion === void 0) return node;
        if (!Array.isArray(motion)) throw new Error(`${label} node ${node.id}.motion must be a list.`);
        const isText = TEXT_TAGS.has(node.tag) || Boolean(node.text?.trim());
        motion.forEach((intent, index) => {
          const intentLabel = `${label} node ${node.id}.motion[${index}]`;
          assertIntent(intent, intentLabel);
          const key = `${intent.phase}@${round(intent.at)}`;
          const order = startsTaken.get(key) ?? 0;
          startsTaken.set(key, order + 1);
          const stages = stagesFor(intent, isText, canvas);
          let at = intent.at;
          if (intent.onBeat && beats.length) {
            const toFilm = layer.timeBase === "film" ? 0 : layer.range.start;
            const accent = toFilm + at + accentOffset(intent, stages);
            const beat = nearestBeat(beats, accent);
            if (beat !== void 0) at = Math.max(0, at + (beat - accent));
          }
          const start = round(at + order * FEELS[intent.feel ?? "default"].stagger);
          const available = layerEnd - start;
          if (available <= 0.05)
            throw new Error(`${intentLabel}.at leaves no time inside the layer range.`);
          const scale = Math.min(1, available / stageLength(stages));
          stages.forEach((stage, stageIndex) => {
            const { offset, ...step } = stage;
            steps.push({
              ...step,
              id: `${node.id}~${intent.phase}-${intent.move}-${index}-${stageIndex}`,
              targetIds: [node.id],
              atSeconds: round(start + offset * scale),
              durationSeconds: round(step.durationSeconds * scale)
            });
          });
        });
        return rest;
      });
      const generated = new Set(steps.map((step) => step.id));
      return {
        ...layer,
        nodes: cleanNodes,
        timeline: [
          ...layer.timeline.filter((step) => !generated.has(step.id)),
          ...steps
        ].sort((a, b) => a.atSeconds - b.atSeconds)
      };
    });
    return { ...scene, motionLayers };
  });
  return changed ? { ...project, scenes } : project;
}

// src/core/motionTimeBase.ts
function normalizeMotionTimeBases(project) {
  let changed = false;
  const scenes = project.scenes.map((scene) => {
    const layers = scene.motionLayers?.map((layer) => {
      if (layer.timeBase !== "film") {
        if (!layer.timeBase) return layer;
        const { timeBase: _timeBase2, ...rest2 } = layer;
        changed = true;
        return rest2;
      }
      const { timeBase: _timeBase, ...rest } = layer;
      changed = true;
      return {
        ...rest,
        timeline: layer.timeline.map((step) => ({
          ...step,
          atSeconds: Math.round((step.atSeconds - layer.range.start) * 1e3) / 1e3
        }))
      };
    });
    return layers ? { ...scene, motionLayers: layers } : scene;
  });
  return changed ? { ...project, scenes } : project;
}

// src/core/creativeQuality.ts
var HIGH_IMPACT_RECIPES = /* @__PURE__ */ new Set([
  "crash-zoom-punch",
  "click-zoom-punch",
  "impact-feedback",
  "freeze-orbit",
  "dutch-roll-level",
  "pull-back-isolation",
  "pressure-push"
]);
var TENSION_RECIPES = /* @__PURE__ */ new Set([
  "freeze-orbit",
  "dutch-roll-level",
  "pull-back-isolation",
  "pressure-push"
]);
var MAX_HIGH_IMPACT_SHOTS = 3;
var MAX_TENSION_SHOTS = 2;
var MIN_CAPTION_HEIGHT_RATIO = 0.052;
var MAX_LIFT_SCENE_RATIO = 0.4;
var MAX_HARSH_TRANSITIONS = 2;
var LIFT_RECIPES = /* @__PURE__ */ new Set(["element-lift", "layer-explode", "depth-parallax"]);
var HARSH_TRANSITIONS = /* @__PURE__ */ new Set(["glitch-cut", "chroma-split"]);
var CJK_GLYPH_EM = 1;
var LATIN_GLYPH_EM = 0.56;
function isRealRecordingLayer(layer) {
  return layer.source === "original" || layer.assetId === "source-video" || layer.semanticTags.some((tag) => /recording|product-evidence|source-video/i.test(tag));
}
function estimateCaptionWidthEm(text) {
  let width = 0;
  for (const character of text.trim()) {
    const code = character.codePointAt(0) ?? 0;
    const cjk = code >= 11904 && code <= 40959 || code >= 44032 && code <= 55215 || code >= 63744 && code <= 64255 || code >= 65280 && code <= 65519 || code >= 131072 && code <= 196607 || code >= 12288 && code <= 12351;
    width += cjk ? CJK_GLYPH_EM : LATIN_GLYPH_EM;
  }
  return width;
}
function fontSizePixels(style) {
  const value = style?.fontSize;
  if (typeof value === "number") return value;
  if (typeof value === "string") {
    const match = /^(\d+(?:\.\d+)?)px$/.exec(value.trim());
    if (match) return Number(match[1]);
  }
  return void 0;
}
function findMotionCraftFindings(project) {
  const findings = [];
  for (const scene of project.scenes) {
    const lockstep = /* @__PURE__ */ new Map();
    for (const layer of scene.motionLayers ?? []) {
      const textNodes = new Set(
        layer.nodes.filter((node) => node.tag === "text" || Boolean(node.text?.trim())).map((node) => node.id)
      );
      for (const step of layer.timeline) {
        if (step.method === "set") continue;
        const start = Math.round((layer.range.start + step.atSeconds) * 100) / 100;
        if (!step.id.includes("~")) {
          const key = `${start}|${step.durationSeconds}|${step.easing ?? ""}`;
          const entry = lockstep.get(key) ?? { targets: /* @__PURE__ */ new Set(), stagger: false };
          for (const target of step.targetIds) entry.targets.add(`${layer.id}/${target}`);
          entry.stagger ||= Boolean(step.staggerSeconds) && step.targetIds.length > 1;
          lockstep.set(key, entry);
        }
        const bouncyText = /elastic|bounce/i.test(step.easing ?? "") && step.targetIds.some((target) => textNodes.has(target));
        if (bouncyText)
          findings.push({
            code: "TEXT_BOUNCES_WHILE_READ",
            category: "text_layout",
            severity: "warning",
            message: `\u573A\u666F ${scene.id} \u7684\u6587\u5B57\u52A8\u6548 ${step.id} \u7528\u4E86 ${step.easing}\uFF0C\u6587\u5B57\u5728\u56DE\u5F39\u65F6\u5F88\u96BE\u9605\u8BFB\u3002`,
            sceneId: scene.id,
            range: { start, end: start + step.durationSeconds },
            suggestedOperation: "Use back.out(1.2-1.7) or expo.out for text, or a motion intent (text keeps its shape automatically); keep elastic for non-text accents."
          });
      }
      for (const node of layer.nodes) {
        if (!textNodes.has(node.id)) continue;
        const own = layer.timeline.filter((step) => step.id.startsWith(`${node.id}~`));
        const enter = own.filter((step) => step.id.includes("~enter-"));
        const exit = own.find((step) => step.id.includes("~exit-"));
        if (!enter.length || !exit) continue;
        const settled = Math.max(...enter.map((step) => step.atSeconds + step.durationSeconds));
        const hold = exit.atSeconds - settled;
        const needed = Math.max(1, [...node.text ?? ""].length / 12);
        if (hold < needed)
          findings.push({
            code: "TEXT_LEAVES_BEFORE_READ",
            category: "text_layout",
            severity: "warning",
            message: `\u573A\u666F ${scene.id} \u7684\u6587\u5B57 ${node.id} \u843D\u5B9A\u540E\u53EA\u505C\u7559 ${Math.max(0, hold).toFixed(2)} \u79D2\u5C31\u9000\u573A\uFF0C\u81F3\u5C11\u9700\u8981\u7EA6 ${needed.toFixed(1)} \u79D2\u624D\u8BFB\u5F97\u5B8C\u3002`,
            sceneId: scene.id,
            range: {
              start: layer.range.start + settled,
              end: layer.range.start + exit.atSeconds
            },
            suggestedOperation: "Start the exit later, shorten the text, or let the next shot carry it; a readable hold matters more than an early exit."
          });
      }
    }
    for (const [key, entry] of lockstep)
      if (entry.targets.size >= 3 && !entry.stagger) {
        const start = Number(key.split("|")[0]);
        findings.push({
          code: "MOTION_MOVES_IN_LOCKSTEP",
          category: "continuity",
          severity: "warning",
          message: `\u573A\u666F ${scene.id} \u5728 ${start} \u79D2\u6709 ${entry.targets.size} \u4E2A\u5143\u7D20\u4EE5\u76F8\u540C\u65F6\u957F\u548C\u7F13\u52A8\u540C\u65F6\u5F00\u59CB\u8FD0\u52A8\uFF0C\u753B\u9762\u4F1A\u50CF\u5E7B\u706F\u7247\u4E00\u6837\u6574\u4F53\u5E73\u79FB\u3002`,
          sceneId: scene.id,
          range: { start, end: start + Number(key.split("|")[1]) },
          evidence: { targets: [...entry.targets].slice(0, 8) },
          suggestedOperation: "Let the primary subject move first and offset the others by a few frames (staggerSeconds 0.04-0.12, or motion intents, which offset nodes that start together)."
        });
      }
  }
  return findings;
}
function findReviewMoments(project, limit = 10) {
  const moments = [];
  for (const scene of project.scenes) {
    for (const layer of scene.motionLayers ?? []) {
      const nodes = new Map(layer.nodes.map((node) => [node.id, node]));
      const imagery = [
        ...scene.visualLayers.map((visual) => visual.id),
        ...layer.nodes.filter((node) => node.assetId || node.tag === "img").map((node) => node.id)
      ];
      const texts = layer.nodes.filter((node) => node.text?.trim());
      if (!texts.length) continue;
      const length = layer.range.end - layer.range.start;
      for (const node of texts) {
        if (!imagery.length) break;
        const chain = /* @__PURE__ */ new Set();
        for (let id = node.id; id && !chain.has(id); id = nodes.get(id)?.parentId)
          chain.add(id);
        const settled = Math.max(
          0.1,
          ...layer.timeline.filter(
            (step) => step.method !== "set" && step.atSeconds < length / 2 && step.targetIds.some((target) => chain.has(target))
          ).map(
            (step) => step.atSeconds + step.durationSeconds + (step.staggerSeconds ?? 0) * Math.max(0, step.targetIds.length - 1)
          )
        );
        moments.push({
          atSeconds: layer.range.start + Math.min(settled + 0.05, Math.max(0.1, length - 0.1)),
          sceneId: scene.id,
          note: `"${[...(node.text ?? "").trim()].slice(0, 24).join("")}" settled over ${imagery.slice(0, 3).join(", ")}`
        });
      }
      if (layer.range.end >= scene.range.end - 0.05)
        moments.push({
          atSeconds: scene.range.end - 0.1,
          sceneId: scene.id,
          note: `scene end with ${layer.id} text still on screen`
        });
    }
  }
  const sorted = [];
  for (const moment of moments.map((item) => ({ ...item, atSeconds: Math.round(item.atSeconds * 100) / 100 })).sort((left, right) => left.atSeconds - right.atSeconds))
    if (!sorted.length || moment.atSeconds - sorted[sorted.length - 1].atSeconds >= 0.3)
      sorted.push(moment);
  if (sorted.length <= limit) return sorted;
  return Array.from(
    { length: limit },
    (_, index) => sorted[Math.round(index * (sorted.length - 1) / (limit - 1))]
  );
}
function findCreativeRhythmFindings(project) {
  const findings = [];
  const scenes = [...project.scenes].sort((left, right) => left.range.start - right.range.start);
  for (let index = 1; index < scenes.length; index += 1) {
    const previous = scenes[index - 1];
    const current = scenes[index];
    if (previous.recipe?.id && previous.recipe.id === current.recipe?.id)
      findings.push({
        code: "RECIPE_REPEATED_ADJACENT",
        category: "continuity",
        severity: "warning",
        message: `\u76F8\u90BB\u573A\u666F ${previous.id} \u4E0E ${current.id} \u91CD\u590D\u4F7F\u7528\u540C\u4E00\u4E2A\u955C\u5934\u914D\u65B9 ${current.recipe?.id}\uFF0C\u540C\u4E00\u79CD\u52A8\u6548\u4E0D\u5E94\u5728\u76F8\u90BB\u955C\u5934\u8FDE\u7EED\u62C5\u4EFB\u4E3B\u89D2\u3002`,
        sceneId: current.id,
        suggestedOperation: "Change one of the two scenes to a different recipe, a stage variation, or a plain evidence shot."
      });
  }
  const highImpact = scenes.filter((scene) => HIGH_IMPACT_RECIPES.has(scene.recipe?.id ?? ""));
  if (highImpact.length > MAX_HIGH_IMPACT_SHOTS)
    findings.push({
      code: "CAMERA_IMPACT_BUDGET_EXCEEDED",
      category: "continuity",
      severity: "warning",
      message: `\u5168\u7247\u4F7F\u7528\u4E86 ${highImpact.length} \u4E2A\u9AD8\u51B2\u51FB\u76F8\u673A\u955C\u5934\uFF0C\u8D85\u8FC7\u5EFA\u8BAE\u4E0A\u9650 ${MAX_HIGH_IMPACT_SHOTS}\uFF1B\u51B2\u51FB\u611F\u6765\u81EA\u7A00\u7F3A\uFF0C\u4E0D\u6765\u81EA\u6570\u91CF\u3002`,
      evidence: { sceneIds: highImpact.map((scene) => scene.id) },
      suggestedOperation: "Keep the impact recipes on the two or three most important beats and let the others breathe."
    });
  const tension = scenes.filter((scene) => TENSION_RECIPES.has(scene.recipe?.id ?? ""));
  if (tension.length > MAX_TENSION_SHOTS)
    findings.push({
      code: "TENSION_MOVE_BUDGET_EXCEEDED",
      category: "continuity",
      severity: "warning",
      message: `\u5F20\u529B\u578B\u76F8\u673A\u8FD0\u52A8\uFF08freeze-orbit\u3001dutch-roll-level\u3001pull-back-isolation\u3001pressure-push\uFF09\u4F7F\u7528\u4E86 ${tension.length} \u6B21\uFF0C\u5EFA\u8BAE\u5168\u7247\u4E0D\u8D85\u8FC7 ${MAX_TENSION_SHOTS} \u6B21\u4E14\u6BCF\u79CD\u53EA\u7528\u4E00\u6B21\u3002`,
      evidence: { sceneIds: tension.map((scene) => scene.id) }
    });
  const lifted = scenes.filter((scene) => LIFT_RECIPES.has(scene.recipe?.id ?? ""));
  if (scenes.length >= 4 && lifted.length / scenes.length > MAX_LIFT_SCENE_RATIO)
    findings.push({
      code: "LIFT_RECIPES_OVERUSED",
      category: "continuity",
      severity: "warning",
      message: `${lifted.length}/${scenes.length} \u4E2A\u573A\u666F\u4F7F\u7528\u4E86\u754C\u9762\u62AC\u5347/\u5206\u5C42/\u89C6\u5DEE\u914D\u65B9\uFF0C\u8D85\u8FC7 40%\uFF1B\u62AC\u5347\u662F\u91CD\u70B9\u955C\u5934\u7684\u7279\u6743\uFF0C\u7528\u591A\u4E86\u89C2\u4F17\u5C31\u4E0D\u77E5\u9053\u54EA\u91CC\u662F\u91CD\u70B9\u3002`,
      evidence: { sceneIds: lifted.map((scene) => scene.id) },
      suggestedOperation: "Keep element-lift/layer-explode on the two or three strongest proof beats and let the rest play full-bleed."
    });
  const harsh = scenes.filter((scene, index) => {
    const transition = normalizeTransition(scene.transitionIn) ?? (index > 0 ? normalizeTransition(scenes[index - 1].transitionOut) : void 0);
    return transition && HARSH_TRANSITIONS.has(transition.id);
  });
  if (harsh.length > MAX_HARSH_TRANSITIONS)
    findings.push({
      code: "HARSH_TRANSITIONS_STACKED",
      category: "continuity",
      severity: "warning",
      message: `\u6545\u969C\u5207/\u8272\u6563\u5207\u4E00\u5171\u7528\u4E86 ${harsh.length} \u6B21\uFF0C\u5EFA\u8BAE\u5168\u7247\u4E0D\u8D85\u8FC7 ${MAX_HARSH_TRANSITIONS} \u6B21\uFF0C\u7559\u7ED9\u6700\u5F3A\u7684\u8282\u62CD\u70B9\u3002`,
      evidence: { sceneIds: harsh.map((scene) => scene.id) }
    });
  for (const scene of scenes) {
    for (const layer of scene.visualLayers)
      if (isRealRecordingLayer(layer) && layer.crop && !rectInside({ x: 0, y: 0, width: 1, height: 1 }, layer.crop) && scene.protectedRegions.length === 0)
        findings.push({
          code: "REAL_FOOTAGE_FRAMING_UNPROTECTED",
          category: "continuity",
          severity: "error",
          message: "\u771F\u5B9E\u5F55\u5C4F\u4F7F\u7528\u4E86\u663E\u5F0F crop\uFF0C\u4F46\u573A\u666F\u6CA1\u6709 protectedRegions\uFF0C\u65E0\u6CD5\u8BC1\u660E\u5173\u952E\u4EA7\u54C1\u533A\u57DF\u4ECD\u7136\u53EF\u89C1\uFF0C\u7981\u6B62\u8FDB\u5165\u6E32\u67D3\u3002",
          sceneId: scene.id,
          range: scene.range,
          evidence: { layerId: layer.id, crop: layer.crop },
          suggestedOperation: "\u4E3A narration\u3001\u70B9\u51FB\u76EE\u6807\u548C\u7ED3\u679C\u533A\u57DF\u8865\u5145 source-normalized protectedRegions\uFF0C\u6216\u79FB\u9664 crop \u540E\u518D\u9884\u89C8\u3002"
        });
    if (!scene.protectedRegions.length) continue;
    for (const layer of scene.visualLayers) {
      if (isRealRecordingLayer(layer) && layer.crop) {
        const crop = layer.crop;
        const hidden = scene.protectedRegions.filter((region) => !rectInside(region, crop));
        if (hidden.length)
          findings.push({
            code: "SOURCE_CROP_HIDES_PROTECTED_REGION",
            category: "continuity",
            severity: "error",
            message: "\u771F\u5B9E\u5F55\u5C4F\u7684\u663E\u5F0F crop \u88C1\u6389\u4E86\u65C1\u767D\u6216\u8BF4\u660E\u6240\u4F9D\u8D56\u7684\u5173\u952E\u4EA7\u54C1\u533A\u57DF\uFF0C\u7981\u6B62\u8FDB\u5165\u6E32\u67D3\u3002",
            sceneId: scene.id,
            range: scene.range,
            evidence: { layerId: layer.id, crop, hiddenRegions: hidden },
            suggestedOperation: "\u6269\u5927 crop \u6216\u79FB\u9664 crop\uFF1B\u5982\u679C\u9700\u8981\u805A\u7126\uFF0C\u8BF7\u628A\u5173\u952E\u533A\u57DF\u5199\u5165 cameraMotion.keyframes[].frame\uFF0C\u8BA9\u6E32\u67D3\u5668\u6309\u8BC1\u636E\u533A\u57DF\u81EA\u52A8\u9002\u914D\u3002"
          });
      }
      const keyframes = layer.cameraMotion?.keyframes ?? [];
      if (!keyframes.length) continue;
      const overflow = coverOverflow(
        layer.mediaWidth,
        layer.mediaHeight,
        project.width,
        project.height
      );
      const cropped = keyframes.flatMap((keyframe, index) => {
        const window2 = layerVisibleWindow(layer, keyframe, project.width, project.height);
        const outside = scene.protectedRegions.filter(
          (region) => !rectInside(region, window2)
        );
        return outside.length ? [{ index, atSeconds: keyframe.atSeconds, outside }] : [];
      });
      if (!cropped.length) continue;
      findings.push({
        code: "CAMERA_CROPS_PROTECTED_REGION",
        category: "continuity",
        severity: "error",
        message: `\u573A\u666F ${scene.id} \u7684\u76F8\u673A\u5728\u7B2C ${cropped.map((item) => item.index + 1).join("\u3001")} \u4E2A\u5173\u952E\u5E27\u628A protectedRegions \u91CC\u7684\u5173\u952E\u754C\u9762\u88C1\u51FA\u4E86\u753B\u9762\uFF08${cropped[0].outside.length} \u4E2A\u533A\u57DF\u88AB\u5207\u6389\uFF09\uFF0C\u65C1\u767D\u5728\u8BB2\u7684\u4E1C\u897F\u89C2\u4F17\u770B\u4E0D\u5168\u3002`,
        sceneId: scene.id,
        range: scene.range,
        evidence: {
          layerId: layer.id,
          overflow,
          keyframes: cropped.map((item) => ({
            index: item.index,
            atSeconds: item.atSeconds,
            outside: item.outside
          }))
        },
        suggestedOperation: "Set keyframe.frame to the region that must stay visible (the renderer derives scale and focus from it), lower the scale, or move the focus toward the region; remember the source is cover-cropped when its aspect differs from the canvas."
      });
    }
  }
  const minimumCaptionPixels = project.height * MIN_CAPTION_HEIGHT_RATIO;
  for (const scene of scenes)
    for (const caption of scene.captions) {
      const pixels = fontSizePixels(caption.style);
      if (pixels !== void 0 && pixels < minimumCaptionPixels)
        findings.push({
          code: "CAPTION_TEXT_TOO_SMALL",
          category: "text_layout",
          // An error, not advice: fast delivery skips warnings, which shipped 38px captions
          // in a 1080p film because the director shrank text to keep cues on one line.
          severity: "error",
          message: `\u5B57\u5E55 ${caption.id} \u7684\u5B57\u53F7 ${pixels}px \u4F4E\u4E8E\u753B\u9762\u9AD8\u5EA6\u7684 5.2%\uFF08\u7EA6 ${Math.round(minimumCaptionPixels)}px\uFF09\uFF0C\u5728 ${project.width}\xD7${project.height} \u6210\u7247\u91CC\u96BE\u4EE5\u9605\u8BFB\u3002`,
          sceneId: scene.id,
          range: caption.range,
          suggestedOperation: "Raise fontSize to at least 5.2% of the output height and keep the cue on one line by splitting it into shorter timed cues at phrase boundaries; do not shrink the text to fit."
        });
      if (caption.text.includes("\n")) continue;
      const glyphs = [...caption.text.trim()].length;
      const boxPixels = caption.bbox.width * project.width;
      const estimatedPixels = pixels !== void 0 ? estimateCaptionWidthEm(caption.text) * pixels : void 0;
      const overflowsBox = estimatedPixels !== void 0 && estimatedPixels > boxPixels * 0.98;
      const exceedsAuthoredLine = glyphs > caption.maxCharsPerLine;
      if (overflowsBox || exceedsAuthoredLine)
        findings.push({
          code: "CAPTION_WOULD_WRAP",
          category: "text_layout",
          severity: "error",
          message: overflowsBox ? `\u5B57\u5E55 ${caption.id}\uFF08${glyphs} \u5B57\uFF09\u6309 ${pixels}px \u4F30\u7B97\u7EA6 ${Math.round(estimatedPixels ?? 0)}px \u5BBD\uFF0C\u8D85\u8FC7\u5B57\u5E55\u6846 ${Math.round(boxPixels)}px\uFF0C\u4F1A\u88AB\u538B\u7F29\u6216\u6362\u884C\uFF1B\u5B57\u5E55\u5FC5\u987B\u5355\u884C\u663E\u793A\u3002` : `\u5B57\u5E55 ${caption.id} \u6709 ${glyphs} \u5B57\uFF0C\u8D85\u8FC7\u5B83\u81EA\u5DF1\u58F0\u660E\u7684\u5355\u884C\u5BB9\u91CF maxCharsPerLine=${caption.maxCharsPerLine}\uFF0C\u4F1A\u6362\u884C\uFF1B\u5B57\u5E55\u5FC5\u987B\u5355\u884C\u663E\u793A\u3002`,
          sceneId: scene.id,
          range: caption.range,
          evidence: {
            glyphs,
            maxCharsPerLine: caption.maxCharsPerLine,
            ...estimatedPixels !== void 0 ? {
              estimatedPixels: Math.round(estimatedPixels),
              boxPixels: Math.round(boxPixels)
            } : {}
          },
          suggestedOperation: "Split the cue into shorter timed cues at a phrase boundary or widen bbox.width; never let a caption wrap, and never fix it by going below the minimum caption size."
        });
    }
  if (scenes.length >= 4) {
    const authored = scenes.slice(1).filter((scene, index) => {
      const transition = normalizeTransition(scene.transitionIn) ?? normalizeTransition(scenes[index].transitionOut);
      return transition && transition.id !== "cut";
    });
    if (authored.length === 0)
      findings.push({
        code: "TRANSITIONS_ALL_HARD_CUTS",
        category: "continuity",
        severity: "warning",
        message: "\u6240\u6709\u573A\u666F\u8FB9\u754C\u90FD\u662F\u786C\u5207\uFF1B\u4EA7\u54C1\u5BA3\u4F20\u7247\u81F3\u5C11\u5E94\u5728\u7AE0\u8282\u8F6C\u6362\u5904\u4F7F\u7528\u6709\u56E0\u679C\u7684\u8F6C\u573A\u3002",
        suggestedOperation: "Author transitionIn/transitionOut at chapter boundaries: hidden-cut behind UI panels, whip-pan for changes of place, zoom-through for going deeper, iris for circular match cuts."
      });
  }
  const flapScenes = scenes.filter((scene) => scene.recipe?.id === "split-flap-title");
  if (flapScenes.length > 1)
    findings.push({
      code: "SPLIT_FLAP_OVERUSED",
      category: "brand",
      severity: "info",
      message: "split-flap-title \u5728\u5168\u7247\u51FA\u73B0\u591A\u6B21\uFF1B\u673A\u68B0\u516C\u544A\u611F\u6765\u81EA\u552F\u4E00\u6027\uFF0C\u5EFA\u8BAE\u53EA\u4FDD\u7559\u4E00\u6B21\u3002",
      evidence: { sceneIds: flapScenes.map((scene) => scene.id) }
    });
  return findings;
}

// src/core/narrationAlignment.ts
var PHRASE_BREAK = /(?<=[。！？!?；;，,、…：:])\s*/u;
function splitNarrationScript(script) {
  const phrases = script.split(PHRASE_BREAK).map((phrase) => phrase.trim()).filter((phrase) => phrase.length > 0);
  return phrases.length ? phrases : [script.trim()].filter((phrase) => phrase.length > 0);
}

// src/core/autoCaptions.ts
var AUTO_CAPTION_ID_PREFIX = "auto-";
var TRAILING_PUNCTUATION = /[\s，。、；：！？,.;:!?…—-]+$/u;
var LEADING_PUNCTUATION = /^[\s，。、；：！？,.;:!?…—-]+/u;
var LINGER_SECONDS = 0.15;
var BRIDGE_GAP_SECONDS = 0.35;
var MIN_CUE_SECONDS = 0.7;
var TOKEN = /[\p{Script=Latin}\p{N}][\p{Script=Latin}\p{N}.,/%'’+×-]*[\p{Script=Latin}\p{N}%]|[\p{Script=Latin}\p{N}]|\S/gu;
var isPunctuation = (text) => !text.replace(TRAILING_PUNCTUATION, "").trim();
var clean2 = (text) => text.replace(TRAILING_PUNCTUATION, "").replace(LEADING_PUNCTUATION, "").trim();
var glyphCount = (text) => [...text.replace(/\s/g, "")].length;
function tokenize(text) {
  return [...text.matchAll(TOKEN)].map((match) => ({
    from: match.index ?? 0,
    to: (match.index ?? 0) + match[0].length,
    speech: !isPunctuation(match[0])
  }));
}
function spread(phrase, span) {
  const speech = phrase.tokens.filter((token) => token.speech);
  const weights = speech.map(
    (token) => Math.max(0.3, estimateCaptionWidthEm(phrase.text.slice(token.from, token.to)))
  );
  const total = weights.reduce((sum, weight) => sum + weight, 0) || 1;
  let cursor = span.start;
  speech.forEach((token, index) => {
    const next = cursor + (span.end - span.start) * weights[index] / total;
    token.range = { start: cursor, end: next };
    cursor = next;
  });
}
function spokenSpan(cue) {
  const words = cue.words ?? [];
  return words.length ? { start: words[0].range.start, end: words[words.length - 1].range.end } : cue.range;
}
function spokenPhrase(cue) {
  const phrase = { text: cue.text, tokens: tokenize(cue.text) };
  if (!cue.words?.length) {
    spread(phrase, cue.range);
    return phrase;
  }
  let cursor = 0;
  for (const word of cue.words) {
    const text = word.text.trim();
    if (!text) continue;
    const at = phrase.text.indexOf(text, cursor);
    if (at < 0) continue;
    cursor = at + text.length;
    const token = phrase.tokens.find((item) => item.from <= at && at < item.to);
    if (!token?.speech) continue;
    token.range = token.range ? {
      start: Math.min(token.range.start, word.range.start),
      end: Math.max(token.range.end, word.range.end)
    } : { ...word.range };
  }
  const speech = phrase.tokens.filter((token) => token.speech);
  speech.forEach((token, index) => {
    if (token.range) return;
    const before = speech.slice(0, index).reverse().find((item) => item.range)?.range;
    const after = speech.slice(index + 1).find((item) => item.range)?.range;
    const at = before?.end ?? after?.start ?? cue.range.start;
    token.range = { start: at, end: Math.max(at, after?.start ?? at) };
  });
  return phrase;
}
function phrasesOf(cues, captionText) {
  if (!captionText?.trim()) return cues.map(spokenPhrase);
  const written = splitNarrationScript(captionText);
  if (written.length !== cues.length)
    throw new Error(
      `voiceover.captionText has ${written.length} phrases but the narration speaks ${cues.length} in this window (${cues.map((cue) => `"${cue.text}"`).join(
        " "
      )}). Keep the narration's phrase punctuation and change only how each phrase is written.`
    );
  return written.map((text, index) => {
    const phrase = { text, tokens: tokenize(text) };
    spread(phrase, spokenSpan(cues[index]));
    return phrase;
  });
}
function pagesOfPhrase(phrase, tokens, maxEm) {
  const width = (run3) => estimateCaptionWidthEm(clean2(phrase.text.slice(run3[0].from, run3[run3.length - 1].to)));
  const total = width(tokens);
  if (total <= maxEm || tokens.length <= 1) return [tokens];
  const count = Math.ceil(total / maxEm);
  const target = total / count;
  const pages = [];
  let page = [];
  for (const token of tokens) {
    const next = [...page, token];
    const nextWidth = width(next);
    if (page.length && (nextWidth > maxEm || nextWidth > target * 1.05 && pages.length < count - 1)) {
      pages.push(page);
      page = [token];
    } else page = next;
  }
  if (page.length) pages.push(page);
  return pages;
}
function mergeShortPages(pages, maxEm) {
  const merged = [...pages];
  const join2 = (a, b) => a.phrase === b.phrase ? `${a.text}${b.text}` : `${a.text} ${b.text}`;
  for (let index = 0; index < merged.length; ) {
    const page = merged[index];
    const short = page.end - page.start < MIN_CUE_SECONDS || glyphCount(page.text) <= 2;
    const next = merged[index + 1];
    const previous = merged[index - 1];
    if (short && next && estimateCaptionWidthEm(join2(page, next)) <= maxEm) {
      merged.splice(index, 2, { ...next, text: join2(page, next), start: page.start });
      continue;
    }
    if (short && previous && estimateCaptionWidthEm(join2(previous, page)) <= maxEm) {
      merged.splice(index - 1, 2, { ...previous, text: join2(previous, page), end: page.end });
      continue;
    }
    index += 1;
  }
  return merged;
}
function buildAutoCaptions(input) {
  const { spec, canvas, voiceover } = input;
  const minimum = Math.ceil(canvas.height * MIN_CAPTION_HEIGHT_RATIO);
  const fontSize = Math.max(
    fontSizePixels(spec.style) ?? Math.ceil(canvas.height * 0.056),
    minimum
  );
  const boxPixels = spec.bbox.width * canvas.width;
  const maxEm = Math.max(4, Math.floor(boxPixels * 0.94 / fontSize * 10) / 10);
  const sourceStart = voiceover.sourceStartSeconds ?? 0;
  const sourceEnd = sourceStart + (voiceover.range.end - voiceover.range.start);
  const toOutput = (seconds3) => voiceover.range.start + (seconds3 - sourceStart);
  const end = Math.min(voiceover.range.end, input.sceneRange.end);
  const inWindow = (range) => range.end > sourceStart && range.start < sourceEnd;
  const phrases = phrasesOf(
    input.cues.filter((cue) => cue.text.trim() && inWindow(spokenSpan(cue))),
    voiceover.captionText
  );
  const pages = phrases.flatMap((phrase, phraseIndex) => {
    const tokens = phrase.tokens.filter(
      (token) => !token.speech || token.range && inWindow(token.range)
    );
    if (!tokens.some((token) => token.speech)) return [];
    return pagesOfPhrase(phrase, tokens, maxEm).map((run3) => {
      const spoken = run3.filter((token) => token.speech && token.range);
      return {
        phrase: phraseIndex,
        text: clean2(phrase.text.slice(run3[0].from, run3[run3.length - 1].to)),
        start: Math.max(toOutput(spoken[0]?.range?.start ?? 0), input.sceneRange.start),
        end: Math.min(toOutput(spoken[spoken.length - 1]?.range?.end ?? 0), end)
      };
    });
  }).filter((page) => page.text && page.end > page.start).sort((a, b) => a.start - b.start);
  const round2 = (value) => Math.round(value * 1e3) / 1e3;
  const merged = mergeShortPages(pages, maxEm);
  return merged.flatMap((page, index) => {
    const next = merged[index + 1]?.start ?? end;
    let stop = next - page.end < BRIDGE_GAP_SECONDS ? next : Math.min(next, page.end + LINGER_SECONDS);
    if (stop - page.start < MIN_CUE_SECONDS) stop = Math.min(next, page.start + MIN_CUE_SECONDS);
    if (stop - page.start < 0.05) return [];
    return [
      {
        id: `${AUTO_CAPTION_ID_PREFIX}${input.sceneId}-${index + 1}`,
        range: { start: round2(page.start), end: round2(stop) },
        text: page.text,
        bbox: spec.bbox,
        // QC counts every character, spaces included, against this capacity.
        maxCharsPerLine: Math.max([...page.text].length, Math.floor(maxEm)),
        style: { ...spec.style ?? {}, fontSize: `${fontSize}px`, whiteSpace: "nowrap" },
        ...spec.className ? { className: spec.className } : {},
        ...spec.enterAnimation ? { enterAnimation: spec.enterAnimation } : {},
        ...spec.exitAnimation ? { exitAnimation: spec.exitAnimation } : {}
      }
    ];
  });
}

// src/edit.ts
init_util();

// src/interactions.ts
import fs8 from "node:fs/promises";
import path10 from "node:path";
init_util();
function validRect(rect) {
  return rect && ["x", "y", "width", "height"].every((key) => Number.isFinite(rect[key])) && rect.x >= 0 && rect.y >= 0 && rect.width > 0 && rect.height > 0 && rect.x + rect.width <= 1.001 && rect.y + rect.height <= 1.001;
}
async function readInteractions(root, asset) {
  if (!asset.interactions) return null;
  const file = inside(root, asset.interactions);
  if ((await fs8.stat(file)).size > 32 * 1024 * 1024) throw new Error("Interaction evidence exceeds 32 MiB.");
  const value = await readJson(file);
  if (![1, 2].includes(value.schemaVersion) || value.timebase !== "recording-seconds" || !Array.isArray(value.events)) throw new Error("Unsupported interaction evidence format.");
  return value;
}
function sourceTimeToFilm(time, layer, sceneRange) {
  const start = layer.sourceRange?.start ?? 0;
  const rate = layer.sourcePlaybackRate ?? (layer.sourceRange ? (layer.sourceRange.end - start) / (sceneRange.end - sceneRange.start) : 1);
  return sceneRange.start + (time - start) / rate;
}
function recordedActions(recording, asset) {
  const semantic = (recording.actions ?? []).filter((action) => action.status === "completed" && Number.isFinite(action.start) && Number.isFinite(action.end) && action.end >= action.start);
  if (recording.schemaVersion === 2 || semantic.length) return semantic;
  const width = recording.viewport?.width || asset.metadata?.width;
  const height = recording.viewport?.height || asset.metadata?.height;
  if (!(width > 0 && height > 0)) return [];
  return recording.events.flatMap((event, index) => {
    if (event.type !== "pointerdown" || !Number.isFinite(event.t) || !Number.isFinite(event.x) || !Number.isFinite(event.y)) return [];
    const x = Math.max(0, Math.min(0.98, event.x / width - 0.01));
    const y = Math.max(0, Math.min(0.98, event.y / height - 0.01));
    return [{
      id: `pointer-${index}`,
      type: "click",
      start: event.t,
      end: event.t,
      status: "completed",
      target: { label: "Recorded click; inspect the actual frame to identify the control.", rect: { x, y, width: 0.02, height: 0.02 } }
    }];
  });
}
function focusFrame(rect) {
  const width = Math.min(1, Math.max(0.4, rect.width * 1.3));
  const height = Math.min(1, Math.max(0.32, rect.height * 1.3));
  return {
    x: Math.max(0, Math.min(1 - width, rect.x + rect.width / 2 - width / 2)),
    y: Math.max(0, Math.min(1 - height, rect.y + rect.height / 2 - height / 2)),
    width,
    height
  };
}
function focusCandidate(asset, recording, action, options2 = {}) {
  if (!action.target || !validRect(action.target.rect)) return null;
  const sourceDuration = Number(asset.metadata?.durationSeconds);
  const start = options2.start ?? Math.max(0, action.start - 0.9);
  const end = options2.end ?? Math.min(sourceDuration, Math.max(action.end, action.start + 0.3) + 1.3);
  if (!(start >= 0 && end > start && end <= sourceDuration + 1e-3)) throw new Error("Focus range must be inside the recording.");
  if (action.start < start || action.start >= end) return null;
  const duration = options2.duration ?? end - start;
  if (!(duration > 0)) throw new Error("Focus duration must be positive.");
  const sceneStart = options2.sceneStart ?? 0;
  if (!Number.isFinite(sceneStart) || sceneStart < 0) throw new Error("Scene start must be a nonnegative film time.");
  const width = options2.width ?? 1920, height = options2.height ?? 1080;
  if (![width, height].every((value) => Number.isFinite(value) && value >= 2)) throw new Error("Focus canvas dimensions must be positive.");
  const rate = (end - start) / duration;
  const targetAt = (action.start - start) / rate;
  const resultAt = Math.min(duration, (action.end - start) / rate);
  const keyframes = [];
  const add = (at, rect) => {
    const atSeconds = Math.round(Math.max(0, Math.min(duration, at)) * 1e3) / 1e3;
    const keyframe = { atSeconds, scale: 1, focusX: rect.x + rect.width / 2, focusY: rect.y + rect.height / 2, frame: rect, easing: "power2.inOut" };
    if (keyframes.length && atSeconds <= keyframes.at(-1).atSeconds) keyframes[keyframes.length - 1] = keyframe;
    else keyframes.push(keyframe);
  };
  const full = { x: 0, y: 0, width: 1, height: 1 }, target = focusFrame(action.target.rect);
  add(0, targetAt > 0.5 ? full : target);
  if (targetAt > 0.5) {
    add(Math.max(0.05, targetAt - 0.65), full);
    add(Math.max(0.1, targetAt - 0.12), target);
  }
  add(Math.max(keyframes.at(-1).atSeconds, Math.min(duration, targetAt + 0.2)), target);
  const result = action.result && validRect(action.result.rect) ? focusFrame(action.result.rect) : target;
  add(Math.max(keyframes.at(-1).atSeconds, Math.min(duration, resultAt + 0.5)), result);
  add(duration, result);
  if (keyframes.length < 3 && duration > 0.01) {
    const first = { ...keyframes[0] || { atSeconds: 0, scale: 1, focusX: 0.5, focusY: 0.5, frame: full, easing: "none" }, atSeconds: 0 };
    const middleAt = Math.min(Math.max(1e-3, Math.round(duration * 500) / 1e3), Math.max(1e-3, Math.round((duration - 1e-3) * 1e3) / 1e3));
    const middle = { ...first, atSeconds: middleAt, focusX: target.x + target.width / 2, focusY: target.y + target.height / 2, frame: target, easing: "power2.inOut" };
    const last = { ...keyframes.at(-1) || middle, atSeconds: Math.round(duration * 1e3) / 1e3, frame: result, focusX: result.x + result.width / 2, focusY: result.y + result.height / 2 };
    keyframes.splice(0, keyframes.length, first, middle, last);
  }
  const fit = Math.min(width / asset.metadata.width, height / asset.metadata.height);
  const visualLayer = {
    id: `focus-${action.id}`,
    source: "asset",
    assetId: asset.id,
    sourceRange: { start, end },
    sourcePlaybackRate: rate,
    crop: full,
    zIndex: 10,
    opacity: 1,
    semanticTags: ["product-evidence", "real-browser-recording"],
    style: { left: `${(width - asset.metadata.width * fit) / 2}px`, top: `${(height - asset.metadata.height * fit) / 2}px`, width: `${asset.metadata.width * fit}px`, height: `${asset.metadata.height * fit}px` },
    cameraMotion: { mode: "authored", reason: "Keep context, focus on the recorded control, then show the observed result.", keyframes }
  };
  if (recording.cursorBakedIn === false) {
    const vw = recording.viewport?.width || asset.metadata.width, vh = recording.viewport?.height || asset.metadata.height;
    const eligible = recording.events.filter((e) => e.t >= start && e.t < end && Number.isFinite(e.x) && Number.isFinite(e.y));
    const stride = Math.max(1, Math.ceil(eligible.length / 250));
    visualLayer.cursorOverlay = {
      sampleIntervalMs: 50,
      shape: "circle",
      sizePixels: 18,
      color: "#111827",
      outlineColor: "#ffffff",
      opacity: 0.9,
      zIndex: 50,
      moveEasing: "none",
      showClicks: true,
      clickColor: "#f4c95d",
      clickDurationSeconds: 0.4,
      clickScale: 2,
      rippleRings: 1,
      samples: eligible.filter((e, i) => i % stride === 0 || e.type === "pointerdown").map((e) => ({ atSeconds: sceneStart + (e.t - start) / rate, x: Math.max(0, Math.min(1, e.x / vw)), y: Math.max(0, Math.min(1, e.y / vh)), ...e.type === "pointerdown" ? { action: "click" } : {} })).sort((a, b) => a.atSeconds - b.atSeconds)
    };
  }
  return {
    actionId: action.id,
    action: action.type,
    target: action.target,
    result: action.result,
    sourceRange: { start, end },
    sceneRange: { start: sceneStart, end: sceneStart + duration },
    durationSeconds: duration,
    visualLayer,
    reviewSourceTimes: [.../* @__PURE__ */ new Set([Math.max(start, action.start - 0.15), action.start, Math.min(end - 1e-3, action.end + 0.3)])],
    completion: action.result ? "result-region-observed" : "result-not-identified",
    instruction: "Inspect the recorded action and result before using this candidate. Camera times are scene-relative; cursor sample times are full-film times based on sceneRange. Preserve the fitted viewport aspect ratio; reframe if changing the layout. A completed browser action is not proof that the product outcome succeeded."
  };
}
async function suggestFocus(root, id, options2 = {}) {
  const asset = await assetById(root, id), recording = await readInteractions(root, asset);
  if (!recording) throw new Error("This asset has no interaction evidence. Author a camera from inspected source frames instead.");
  const actions = recordedActions(recording, asset);
  const limit = Math.min(12, Math.max(1, Math.floor(options2.limit ?? 6)));
  const candidates = actions.filter((action) => (action.type === "click" || action.type === "press") && action.target && validRect(action.target.rect) && action.start >= (options2.start ?? 0) && action.start < (options2.end ?? Infinity)).slice(0, limit).map((action) => focusCandidate(asset, recording, action, options2)).filter(Boolean);
  return {
    assetId: id,
    evidence: path10.join(root, asset.interactions),
    timingUncertaintySeconds: recording.timingUncertaintySeconds ?? null,
    candidates,
    instruction: "These are editable camera candidates, not automatic edits. Use actual frame inspection to accept one, adjust it, or collect better footage."
  };
}

// src/quality.ts
var within = (range) => range && Number.isFinite(range.start) && Number.isFinite(range.end) && range.start >= 0 && range.end > range.start;
var overlap = (a, b) => a.end > b.start && a.start < b.end;
function sourceRange(layer, scene) {
  const start = layer.sourceRange?.start ?? 0;
  const rate = layer.sourcePlaybackRate ?? (layer.sourceRange ? (layer.sourceRange.end - start) / (scene.end - scene.start) : 1);
  return { start, end: start + (scene.end - scene.start) * rate };
}
function auditDirectorPlan(project, context) {
  const shots = context.director?.shots;
  if (!Array.isArray(shots) || !shots.length) return [{
    code: "DIRECTOR_PLAN_MISSING",
    category: "semantic_alignment",
    severity: "info",
    message: "\u5BFC\u6F14\u72B6\u6001\u5C1A\u672A\u8BB0\u5F55\u9010\u955C\u5934\u610F\u56FE\u548C\u9A8C\u6536\u6761\u4EF6\u3002\u65E7\u5DE5\u7A0B\u4ECD\u53EF\u6E32\u67D3\uFF1B\u5236\u4F5C\u6216\u6539\u7F16\u65F6\u8865\u5145\u6709\u7528\u7684\u5206\u955C\u8BF4\u660E\u3002",
    suggestedOperation: "Use director-state.json shots to connect each important claim to inspected source actions and results."
  }];
  const findings = [], assets = new Map((context.assets ?? []).map((asset) => [asset.id, asset]));
  const seen = /* @__PURE__ */ new Set();
  for (const shot of shots) {
    const scene = project.scenes.find((scene2) => scene2.id === shot?.sceneId);
    if (!scene || seen.has(shot.sceneId)) {
      findings.push({ code: "DIRECTOR_SCENE_REFERENCE", category: "semantic_alignment", severity: "warning", message: `\u5206\u955C\u8BA1\u5212\u5F15\u7528\u4E86\u4E0D\u5B58\u5728\u6216\u91CD\u590D\u7684\u573A\u666F ${shot?.sceneId ?? "(missing)"}` });
      continue;
    }
    seen.add(scene.id);
    const issue = (code, message, evidence2) => findings.push({
      code,
      category: "semantic_alignment",
      severity: "warning",
      sceneId: scene.id,
      range: scene.range,
      message,
      evidence: evidence2,
      suggestedOperation: "Inspect the relevant source frames, record missing actions/results, or narrow the claim to what the selected footage demonstrates."
    });
    if (typeof shot.intent !== "string" || !shot.intent.trim() || !Array.isArray(shot.acceptance) || !shot.acceptance.some((text) => typeof text === "string" && text.trim())) issue("SHOT_INTENT_UNSPECIFIED", "\u955C\u5934\u7F3A\u5C11\u660E\u786E\u610F\u56FE\u6216\u53EF\u89C2\u5BDF\u7684\u9A8C\u6536\u6761\u4EF6\u3002");
    const evidence = Array.isArray(shot.evidence) ? shot.evidence : [];
    const validStages = /* @__PURE__ */ new Set();
    for (const item of evidence) {
      if (!item || typeof item !== "object") {
        issue("SHOT_EVIDENCE_INVALID", "\u955C\u5934\u8BC1\u636E\u5FC5\u987B\u662F\u5305\u542B\u7D20\u6750\u5F15\u7528\u548C\u89C2\u5BDF\u8BB0\u5F55\u7684\u5BF9\u8C61\u3002");
        continue;
      }
      const asset = assets.get(item.assetId);
      const timed = asset?.kind !== "image";
      if (!asset || timed && (!within(item.sourceRange) || item.sourceRange.end > Number(asset.metadata?.durationSeconds || 0) + 0.05)) {
        issue("SHOT_EVIDENCE_INVALID", "\u955C\u5934\u8BC1\u636E\u5F15\u7528\u4E86\u7F3A\u5931\u7D20\u6750\u6216\u65E0\u6548\u7684\u6E90\u65F6\u95F4\u8303\u56F4\u3002", { assetId: item.assetId, sourceRange: item.sourceRange });
        continue;
      }
      const displayed = scene.visualLayers.some((layer) => layer.assetId === item.assetId && (() => {
        if (!timed) return true;
        const used = sourceRange(layer, scene.range);
        return item.sourceRange.start >= used.start - 0.05 && item.sourceRange.end <= used.end + 0.05;
      })());
      if (!displayed) {
        issue("SHOT_EVIDENCE_NOT_IN_EDIT", "\u5DF2\u8BB0\u5F55\u7684\u52A8\u4F5C\u6216\u7ED3\u679C\u6CA1\u6709\u5B8C\u6574\u5305\u542B\u5728\u8BE5\u955C\u5934\u9009\u7528\u7684\u6E90\u7247\u6BB5\u91CC\u3002", { assetId: item.assetId, sourceRange: item.sourceRange });
        continue;
      }
      if (item.verified !== true || typeof item.observation !== "string" || !item.observation.trim()) {
        issue("SHOT_EVIDENCE_UNREVIEWED", "\u8BC1\u636E\u7F3A\u5C11\u5B9E\u9645\u753B\u9762\u89C2\u5BDF\uFF1B\u6267\u884C\u6210\u529F\u6216\u6309\u94AE\u6587\u5B57\u4E0D\u80FD\u4EE3\u66FF\u89C6\u89C9\u786E\u8BA4\u3002", { assetId: item.assetId, stage: item.stage });
        continue;
      }
      validStages.add(item.stage);
    }
    for (const stage of Array.isArray(shot.requiredStages) ? shot.requiredStages : []) {
      if (!validStages.has(stage)) issue("SHOT_PROOF_INCOMPLETE", `\u8BE5\u955C\u5934\u8981\u6C42\u5C55\u793A ${stage}\uFF0C\u4F46\u7F3A\u5C11\u5DF2\u67E5\u770B\u4E14\u5B9E\u9645\u8FDB\u5165\u526A\u8F91\u7684\u5BF9\u5E94\u8BC1\u636E\u3002`, { stage });
    }
  }
  return findings;
}
function dimension(value, parent) {
  if (typeof value === "number") return value;
  if (typeof value === "string" && /^\d+(\.\d+)?(px|%)$/.test(value)) return parseFloat(value) * (value.endsWith("%") ? parent / 100 : 1);
  return parent;
}
function spatialFindings(sceneId, range, spatial, assets, canvasWidth = 1920, canvasHeight = 1080, viewingWidth = Math.min(960, canvasWidth)) {
  const findings = [];
  const add = (code, severity, message, evidence) => findings.push({
    code,
    category: "technical",
    severity,
    sceneId,
    range,
    message,
    evidence,
    suggestedOperation: "Inspect the 3D review frames, correct the spatial asset/camera/timeline, and render the affected range again."
  });
  const modelIds = new Set(spatial.models.map((model) => model.id));
  for (const model of spatial.models) {
    if (model.assetId) {
      const asset = assets.get(model.assetId);
      if (!asset || asset.kind !== "model3d") add("SPATIAL_MODEL_MISSING", "error", `3D \u6A21\u578B ${model.id} \u5F15\u7528\u4E86\u7F3A\u5931\u6216\u975E model3d \u7D20\u6750 ${model.assetId}\u3002`, { assetId: model.assetId });
      else {
        if (!asset.provenance?.license && !asset.metadata?.license) add("SPATIAL_ASSET_LICENSE_UNKNOWN", "warning", `\u6A21\u578B ${model.id} \u6CA1\u6709\u8BB0\u5F55\u8BB8\u53EF\u8BC1\u6216\u6765\u6E90\u8BB8\u53EF\u3002`, { assetId: model.assetId, source: asset.provenance?.url ?? asset.id });
        if (asset.metadata?.externalDependencies?.length && asset.metadata?.sourceDirectory !== "bundled-dependencies") add("SPATIAL_EXTERNAL_DEPENDENCY", "error", `\u6A21\u578B ${model.id} \u4ECD\u58F0\u660E\u672A\u6253\u5305\u7684\u5916\u90E8\u4F9D\u8D56\uFF0C\u6E32\u67D3\u5FC5\u987B\u4F7F\u7528\u9879\u76EE\u5185\u5DF2\u590D\u5236\u7684\u4F9D\u8D56\u3002`, { dependencies: asset.metadata.externalDependencies });
        if (!(Number(asset.metadata?.unitScale) > 0)) add("SPATIAL_UNIT_SCALE_UNKNOWN", "warning", `\u6A21\u578B ${model.id} \u7F3A\u5C11\u6709\u6548\u5355\u4F4D\u6BD4\u4F8B\uFF0C\u7A7A\u95F4\u5C3A\u5EA6\u53EF\u80FD\u4E0E\u5176\u4ED6\u7D20\u6750\u4E0D\u4E00\u81F4\u3002`, { unitScale: asset.metadata?.unitScale });
      }
    }
    if (model.instanceOf && !modelIds.has(model.instanceOf)) add("SPATIAL_INSTANCE_MISSING", "error", `\u6A21\u578B ${model.id} \u7684 instanceOf ${model.instanceOf} \u4E0D\u5B58\u5728\u3002`, { instanceOf: model.instanceOf });
    if (model.scale?.some((value) => Math.abs(value) < 1e-4)) add("SPATIAL_MODEL_DEGENERATE_SCALE", "error", `\u6A21\u578B ${model.id} \u7684\u7F29\u653E\u63A5\u8FD1\u96F6\uFF0C\u65E0\u6CD5\u7A33\u5B9A\u6E32\u67D3\u3002`, { scale: model.scale });
    const bounds = model.assetId ? assets.get(model.assetId)?.metadata?.bounds : void 0;
    if (bounds && model.position) {
      const maxDimension = Math.max(...bounds.max.map((value, index) => Math.abs(value - bounds.min[index])));
      const scale = Math.max(...(model.scale ?? [1, 1, 1]).map((value) => Math.abs(value)));
      const distance = Math.max(0.1, Math.hypot(...spatial.camera.position.map((value, index) => value - (model.position?.[index] ?? 0))));
      if (maxDimension * scale / distance < 0.02) add("SPATIAL_MODEL_TOO_SMALL", "warning", `\u6A21\u578B ${model.id} \u76F8\u5BF9\u76F8\u673A\u8DDD\u79BB\u8FC7\u5C0F\uFF0C\u7F29\u5C0F\u5C4F\u5E55\u540E\u53EF\u80FD\u4E0D\u53EF\u8BFB\u3002`, { projectedRatio: maxDimension * scale / distance });
      const near = spatial.camera.near ?? 0.01, far = spatial.camera.far ?? 1e3;
      if (distance - maxDimension * scale < near || distance + maxDimension * scale > far) add("SPATIAL_CAMERA_CLIP", "warning", `\u6A21\u578B ${model.id} \u53EF\u80FD\u8D85\u51FA\u76F8\u673A near/far \u88C1\u526A\u8303\u56F4\u3002`, { near, far, distance, radius: maxDimension * scale });
    }
  }
  for (const annotation of spatial.annotations ?? []) {
    const point = Array.isArray(annotation.anchor) ? annotation.anchor : annotation.anchor.offset;
    if (point && (Math.abs(point[0]) > 1e4 || Math.abs(point[1]) > 1e4 || Math.abs(point[2]) > 1e4)) add("SPATIAL_ANNOTATION_OUT_OF_FRAME", "warning", `\u6807\u6CE8 ${annotation.id} \u7684\u951A\u70B9\u8FDC\u79BB\u573A\u666F\uFF0C\u53EF\u80FD\u65E0\u6CD5\u8FDB\u5165\u753B\u9762\u3002`, { anchor: point });
    if (!Array.isArray(annotation.anchor) && !modelIds.has(annotation.anchor.modelId)) add("SPATIAL_ANNOTATION_MODEL_MISSING", "error", `\u6807\u6CE8 ${annotation.id} \u5F15\u7528\u4E86\u4E0D\u5B58\u5728\u7684\u6A21\u578B\u3002`, { modelId: annotation.anchor.modelId });
  }
  const backend = spatialBackend(spatial);
  if (backend === "anatomy" && spatial.anatomy) {
    const anatomy = spatial.anatomy;
    for (const item of anatomyAudit(anatomy)) add(item.code, item.severity, item.message, item.partId ? { partId: item.partId } : void 0);
    const projection = anatomy.projection ?? {};
    const azimuth = (projection.azimuth ?? 45) * Math.PI / 180;
    const elevation = (projection.elevation ?? 30) * Math.PI / 180;
    const scale = (projection.scale ?? 1) * Math.min(canvasWidth, canvasHeight) / 10;
    const origin = projection.origin ?? [canvasWidth / 2, canvasHeight / 2];
    const projectPoint = (point) => {
      const horizontal = point[0] * Math.cos(azimuth) - point[1] * Math.sin(azimuth);
      const depth = point[0] * Math.sin(azimuth) + point[1] * Math.cos(azimuth);
      return [origin[0] + horizontal * scale, origin[1] + (depth * Math.sin(elevation) - point[2] * Math.cos(elevation)) * scale];
    };
    for (const part of anatomy.parts ?? []) {
      const point = projectPoint(part.position ?? [0, 0, 0]);
      if (point[0] < -canvasWidth * 0.1 || point[0] > canvasWidth * 1.1 || point[1] < -canvasHeight * 0.1 || point[1] > canvasHeight * 1.1) add("ANATOMY_PART_OUT_OF_FRAME", "warning", `anatomy \u90E8\u4EF6 ${part.id} \u7684\u6295\u5F71\u4F4D\u7F6E\u53EF\u80FD\u79BB\u5F00\u753B\u9762\u3002`, { partId: part.id, projected: point, canvas: [canvasWidth, canvasHeight] });
      if (part.kind === "label") {
        const viewed = (part.fontSize ?? 20) * viewingWidth / canvasWidth;
        if (viewed < 14) add("ANATOMY_LABEL_TOO_SMALL", "warning", `anatomy \u6807\u6CE8 ${part.id} \u5728\u5C0F\u5C4F\u4E0A\u7EA6\u4E3A ${viewed.toFixed(1)}px\uFF0C\u53EF\u80FD\u96BE\u4EE5\u9605\u8BFB\u3002`, { partId: part.id, viewedPixels: viewed, viewingWidth });
      }
    }
    if (anatomy.authoredFigure) {
      const figure = anatomy.authoredFigure;
      if (!figure.provenance?.license) add("ANATOMY_SOURCE_LICENSE_UNKNOWN", "warning", "Anatomy \u4F5C\u54C1\u6CA1\u6709\u8BB0\u5F55\u6E90\u7801\u548C\u7D20\u6750\u8BB8\u53EF\u8BC1\uFF1B\u8BF7\u8865\u5145\u6765\u6E90\u8BB8\u53EF\u3002", { figureId: anatomy.figureId });
      if (!figure.provenance?.url && !figure.provenance?.source) add("ANATOMY_SOURCE_UNKNOWN", "warning", "Anatomy \u4F5C\u54C1\u7F3A\u5C11\u539F\u521B\u6216\u4E0A\u6E38\u6765\u6E90\u8BB0\u5F55\u3002", { figureId: anatomy.figureId });
      add("ANATOMY_AUTHORED_REVIEW_REQUIRED", "info", "\u8BE5\u955C\u5934\u76F4\u63A5\u4F7F\u7528\u5B8C\u6574 Anatomy \u4F5C\u54C1\u3002\u5BFC\u5165\u4E0E\u6E32\u67D3\u6210\u529F\u4E0D\u7B49\u4E8E\u7ED3\u6784\u6B63\u786E\uFF1B\u68C0\u67E5\u5B8C\u6574\u7269\u4F53\u3001\u91CD\u70B9\u90E8\u4EF6\u3001\u8FDE\u63A5\u7EC6\u8282\u548C\u8BFB\u6570\uFF0C\u5E76\u4FDD\u7559\u4F5C\u8005\u7684\u51E0\u4F55\u5BA1\u8BA1\u7ED3\u679C\u3002", { figureId: anatomy.figureId, semanticParts: figure.parts.length });
    } else try {
      const compiled = compileAnatomy(anatomy, canvasWidth, canvasHeight);
      for (const [kind, items] of Object.entries(compiled.audits.checks)) {
        if (Array.isArray(items) && items.length) add("ANATOMY_GEOMETRY_" + kind.toUpperCase(), "warning", `\u4E0A\u6E38 anatomy ${kind} \u5BA1\u8BA1\u53D1\u73B0 ${items.length} \u9879\uFF0C\u9700\u8981\u7ED3\u5408\u5B9E\u9645\u7A7A\u95F4\u5173\u7CFB\u590D\u6838\u3002`, { count: items.length, samples: items.slice(0, 3) });
      }
      for (const [kind, items] of Object.entries(compiled.audits.motion)) if (Array.isArray(items) && items.length && !["notes", "skipped"].includes(kind)) add("ANATOMY_MOTION_" + kind.toUpperCase(), "warning", `\u4E0A\u6E38 anatomy \u52A8\u6001 ${kind} \u5BA1\u8BA1\u53D1\u73B0 ${items.length} \u9879\u3002`, { count: items.length, samples: items.slice(0, 3) });
    } catch (error) {
      add("ANATOMY_GEOMETRY_INVALID", "error", String(error));
    }
    for (const annotation of anatomy.annotations ?? []) {
      const pixels = (annotation.fontSize ?? Math.max(16, canvasHeight / 36)) * viewingWidth / canvasWidth;
      if (pixels < 14) add("ANATOMY_ANNOTATION_TOO_SMALL", "warning", `\u6807\u6CE8 ${annotation.id} \u5728\u5C0F\u5C4F\u4E0A\u53EA\u6709 ${pixels.toFixed(1)}px\u3002`);
    }
    const keys = [...anatomy.keyframes ?? []].sort((a, b) => a.atSeconds - b.atSeconds);
    for (let i = 1; i < keys.length; i++) if (keys[i].atSeconds - keys[i - 1].atSeconds < 0.3) add("ANATOMY_ACTION_TOO_FAST", "warning", "\u76F8\u90BB\u5173\u952E\u52A8\u4F5C\u5C11\u4E8E 0.3 \u79D2\uFF0C\u8BF7\u68C0\u67E5\u662F\u5426\u770B\u5F97\u6E05\u3002", { from: keys[i - 1].atSeconds, to: keys[i].atSeconds });
    add("ANATOMY_RUNTIME_BACKEND", "info", "\u8BE5\u955C\u5934\u4F7F\u7528 anatomy \u7B49\u8F74\u6D4B\u89E3\u91CA\u578B\u540E\u7AEF\uFF1B\u8FD0\u884C\u65F6\u3001\u6765\u6E90\u63D0\u4EA4\u548C MIT \u8BB8\u53EF\u8BC1\u4F1A\u5199\u5165\u6E32\u67D3\u4E0A\u4E0B\u6587\u3002", { runtime: ANATOMY_RUNTIME_VERSION });
  } else if (spatial.models.some((model) => model.assetId)) add("SPATIAL_RUNTIME_BACKEND", "info", "\u542B\u771F\u5B9E\u6A21\u578B\u7684\u955C\u5934\u9700\u8981 WebGL\uFF1BANGLE/SwiftShader \u4E0E\u8FD0\u884C\u65F6\u7248\u672C\u4F1A\u5199\u5165\u6E32\u67D3\u4E0A\u4E0B\u6587\uFF0CCanvas 2D \u53EA\u7528\u4E8E\u7EAF\u7A0B\u5E8F\u5316\u955C\u5934\u3002", { runtime: "0.6.0-three-0.180.0" });
  if (backend === "three" && spatial.models.length > 0 && spatial.models.every((model) => Boolean(model.procedural))) {
    add("SPATIAL_PROCEDURAL_ONLY", "warning", "\u8BE5\u7A7A\u95F4\u955C\u5934\u53EA\u5305\u542B\u7A0B\u5E8F\u5316\u57FA\u7840\u51E0\u4F55\u3002\u5B83\u9002\u5408\u5173\u7CFB\u8349\u56FE\uFF1B\u9700\u8981 anatomy \u7EA7\u673A\u68B0\u7EC6\u8282\u65F6\uFF0C\u8BF7\u6539\u7528 pinned anatomy authored scene \u6216\u5BFC\u5165\u9879\u76EE\u5185\u771F\u5B9E GLB/GLTF\u3002", { modelCount: spatial.models.length });
  }
  return findings;
}
function buildQualityReport(project, context = {}) {
  const profile = context.director?.qualityProfile || {};
  const viewingWidth = Math.max(240, Math.min(project.width, Number(profile.viewingWidth) || Math.min(960, project.width)));
  const minCaptionPixels = Math.max(10, Math.min(48, Number(profile.minCaptionPixels) || 18));
  const maxUpscale = Math.max(1, Math.min(4, Number(profile.maxUpscale) || 1.5));
  const findings = [...findCreativeRhythmFindings(project).filter((f) => f.code !== "CAPTION_TEXT_TOO_SMALL"), ...findMotionCraftFindings(project)];
  for (const finding of findings) {
    if (finding.code === "REAL_FOOTAGE_FRAMING_UNPROTECTED") {
      finding.severity = "warning";
      finding.message = "\u771F\u5B9E\u5F55\u5C4F\u7ECF\u8FC7\u88C1\u5207\uFF0C\u5C1A\u672A\u6807\u6CE8\u5FC5\u987B\u4FDD\u7559\u7684\u4EA7\u54C1\u533A\u57DF\uFF0C\u8BF7\u68C0\u67E5\u52A8\u4F5C\u4E0E\u7ED3\u679C\u662F\u5426\u4ECD\u5B8C\u6574\u53EF\u89C1\u3002";
    }
    if (finding.code === "CAPTION_WOULD_WRAP") {
      finding.severity = "warning";
      finding.message = "\u5B57\u5E55\u957F\u5EA6\u53EF\u80FD\u8D85\u8FC7\u58F0\u660E\u7684\u884C\u957F\u6216\u53EF\u7528\u5BBD\u5EA6\uFF1B\u8BF7\u68C0\u67E5\u5B9E\u9645\u6E32\u67D3\uFF0C\u5FC5\u8981\u65F6\u6309\u8BED\u4E49\u62C6\u53E5\u3002";
      finding.suggestedOperation = "Inspect the rendered text. Split at phrase boundaries, widen the available area, or author readable line breaks.";
    }
    if (finding.code === "TRANSITIONS_ALL_HARD_CUTS") {
      finding.severity = "info";
      finding.message = "\u7AE0\u8282\u5168\u90E8\u4F7F\u7528\u786C\u5207\u3002\u7ED3\u5408\u53D9\u4E8B\u5224\u65AD\u662F\u5426\u9700\u8981\u53D8\u5316\uFF1B\u8FDE\u8D2F\u7684\u786C\u5207\u53EF\u4EE5\u4FDD\u7559\u3002";
    }
  }
  findings.push(...auditDirectorPlan(project, context), ...context.issues ?? []);
  if (project.presentation?.showTimelineProgress === true) findings.push({ code: "TIMELINE_PROGRESS_ENABLED", category: "technical", severity: "info", range: { start: 0, end: project.durationSeconds }, message: "\u9879\u76EE\u663E\u5F0F\u5F00\u542F\u4E86\u65F6\u95F4\u8FDB\u5EA6\u6761\uFF1B\u8FD9\u4E0D\u662F\u9ED8\u8BA4\u5BFC\u51FA\u6837\u5F0F\uFF0C\u8BF7\u786E\u8BA4\u5B83\u786E\u5B9E\u670D\u52A1\u4E8E\u5F53\u524D\u5185\u5BB9\u3002", suggestedOperation: "Remove presentation.showTimelineProgress unless the viewer needs a timeline indicator." });
  const sourceDisplays = [];
  for (const scene of project.scenes) {
    if (scene.spatial) findings.push(...spatialFindings(scene.id, scene.range, scene.spatial, new Map((context.assets ?? []).map((asset) => [asset.id, asset])), project.width, project.height, viewingWidth));
    for (const layer of scene.visualLayers) {
      if (!layer.assetId || !(layer.mediaWidth && layer.mediaHeight)) continue;
      const sw = layer.mediaWidth * (layer.crop?.width ?? 1), sh = layer.mediaHeight * (layer.crop?.height ?? 1);
      const dw = dimension(layer.style?.width, project.width), dh = dimension(layer.style?.height, project.height);
      const zoom = Math.max(1, ...(layer.cameraMotion?.keyframes ?? []).map((k) => k.frame ? Math.min(2.6, 0.94 / Math.max(k.frame.width / (layer.crop?.width ?? 1), k.frame.height / (layer.crop?.height ?? 1))) : k.scale));
      const upscale = Math.max(dw / sw, dh / sh) * zoom;
      sourceDisplays.push({ sceneId: scene.id, layerId: layer.id, sourcePixels: [Math.round(sw), Math.round(sh)], displayPixels: [Math.round(dw), Math.round(dh)], upscale: Math.round(upscale * 100) / 100 });
      if (upscale > maxUpscale) findings.push({
        code: "SOURCE_UPSCALED",
        category: "technical",
        severity: "warning",
        sceneId: scene.id,
        range: scene.range,
        message: `\u7D20\u6750 ${layer.id} \u7684\u88C1\u5207\u4E0E\u8FD0\u955C\u6700\u9AD8\u7EA6\u653E\u5927 ${upscale.toFixed(2)} \u500D\uFF0C\u7EC6\u5B57\u548C\u8F6E\u5ED3\u53EF\u80FD\u53D8\u8F6F\u3002`,
        evidence: sourceDisplays.at(-1),
        suggestedOperation: "Inspect a full-resolution frame; use a larger source, higher-density capture, or a wider crop if detail is lost."
      });
    }
    for (const caption of scene.captions) {
      const pixels = fontSizePixels(caption.style), viewed = pixels === void 0 ? void 0 : pixels * viewingWidth / project.width;
      if (viewed !== void 0 && viewed < minCaptionPixels) findings.push({
        code: "CAPTION_TEXT_TOO_SMALL",
        category: "text_layout",
        severity: "warning",
        sceneId: scene.id,
        range: caption.range,
        message: `\u5B57\u5E55 ${caption.id} \u5728 ${viewingWidth}px \u5BBD\u7684\u64AD\u653E\u753B\u9762\u91CC\u7EA6\u4E3A ${viewed.toFixed(1)}px\uFF0C\u5C0F\u4E8E\u5F53\u524D\u9605\u8BFB\u76EE\u6807 ${minCaptionPixels}px\u3002`,
        evidence: { fontSize: pixels, viewingWidth, viewedPixels: viewed },
        suggestedOperation: "Check the small-screen preview; enlarge the subtitle or shorten and split its text if it is difficult to read."
      });
      const charactersPerSecond = [...caption.text.replace(/[\s，。！？、,.!?]/gu, "")].length / (caption.range.end - caption.range.start);
      if (charactersPerSecond > 12) findings.push({
        code: "CAPTION_READING_SPEED",
        category: "timing",
        severity: "warning",
        sceneId: scene.id,
        range: caption.range,
        message: `\u5B57\u5E55 ${caption.id} \u7EA6 ${charactersPerSecond.toFixed(1)} \u5B57/\u79D2\uFF0C\u8BF7\u6838\u5BF9\u9605\u8BFB\u548C\u8BED\u97F3\u540C\u6B65\u3002`,
        evidence: { charactersPerSecond },
        suggestedOperation: "Extend a meaningful hold or shorten the wording without moving the caption away from its speech."
      });
    }
  }
  const unique = findings.filter((finding, index) => findings.findIndex((other) => JSON.stringify(other) === JSON.stringify(finding)) === index);
  return {
    schemaVersion: 1,
    status: "requires-visual-review",
    advisory: true,
    profile: { viewingWidth, minCaptionPixels, maxUpscale },
    spatial: project.scenes.some((scene) => Boolean(scene.spatial)) ? { runtime: "0.6.0-three-0.180.0", anatomyRuntime: ANATOMY_RUNTIME_VERSION, backends: ["webgl-angle-swiftshader", "canvas2d-procedural", "anatomy-svg", "anatomy-canvas2d", "anatomy-authored"], projectLocalAssetsOnly: true } : void 0,
    counts: { error: unique.filter((f) => f.severity === "error").length, warning: unique.filter((f) => f.severity === "warning").length, info: unique.filter((f) => f.severity === "info").length },
    findings: unique,
    sourceDisplays,
    instruction: "Inspect evidence and decide which findings require a correction. Record fixes or intentional choices in director-state.json. Structural validity and a clean report do not certify visual or narrative quality."
  };
}
function planReviewFrames(project, renderRange, context = {}, limit = 24) {
  limit = Math.max(1, Math.min(24, Math.floor(limit)));
  const duration = renderRange.end - renderRange.start, candidates = [];
  const add = (time, reason, priority, sceneId) => {
    if (!Number.isFinite(time) || time < renderRange.start || time >= renderRange.end) return;
    const local = Math.max(0, Math.min(duration - 1e-3, time - renderRange.start));
    const existing = candidates.find((item) => Math.abs(item.atSeconds - local) < 0.04);
    if (existing) {
      existing.reasons.push(reason);
      existing.priority = Math.max(priority, existing.priority);
      return;
    }
    candidates.push({ atSeconds: Number(local.toFixed(4)), timelineSeconds: Number(time.toFixed(4)), sceneId, reasons: [reason], priority });
  };
  add(renderRange.start, "output-start", 5);
  add(Math.max(renderRange.start, renderRange.end - 1 / project.fps), "output-end", 5);
  const assets = new Map((context.assets ?? []).map((asset) => [asset.id, asset]));
  for (const scene of project.scenes.filter((scene2) => overlap(scene2.range, renderRange))) {
    const visible = { start: Math.max(scene.range.start, renderRange.start), end: Math.min(scene.range.end, renderRange.end) };
    add((visible.start + visible.end) / 2, "scene-overview", 3, scene.id);
    add(scene.range.start + Math.min(0.12, (scene.range.end - scene.range.start) / 4), "after-cut", 4, scene.id);
    add(scene.range.end - 1 / project.fps, "before-cut", 4, scene.id);
    if (scene.spatial) {
      const viewKeys = scene.spatial.anatomy?.view?.keyframes ?? [];
      for (const [index, key] of viewKeys.entries()) {
        add(scene.range.start + Math.max(0, key.atSeconds - 0.08), "anatomy-before-view", 6, scene.id);
        add(scene.range.start + key.atSeconds, "anatomy-view-focus", 7, scene.id);
        const end = viewKeys[index + 1]?.atSeconds ?? scene.range.end - scene.range.start;
        if (end > key.atSeconds) add(scene.range.start + (key.atSeconds + end) / 2, "anatomy-view-detail", 6, scene.id);
      }
      for (const key of scene.spatial.anatomy?.keyframes ?? []) {
        add(scene.range.start + Math.max(0, key.atSeconds - 0.08), "anatomy-before-keyframe", 6, scene.id);
        add(scene.range.start + key.atSeconds, "anatomy-keyframe", 7, scene.id);
      }
      for (const note of scene.spatial.anatomy?.annotations ?? []) if (note.range) add(scene.range.start + note.range.start + 0.1, "anatomy-annotation", 6, scene.id);
      for (const model of scene.spatial.models) {
        const modelRange = model.range ?? scene.range;
        add(modelRange.start + Math.min(0.08, (modelRange.end - modelRange.start) / 3), "spatial-model-enter", 6, scene.id);
        add(modelRange.end - 1 / project.fps, "spatial-model-exit", 5, scene.id);
      }
      for (const keyframe of scene.spatial.camera.keyframes ?? []) add(scene.range.start + keyframe.atSeconds, "spatial-camera-keyframe", 5, scene.id);
      for (const annotation of scene.spatial.annotations ?? []) {
        add(annotation.range.start + Math.min(0.1, (annotation.range.end - annotation.range.start) / 3), "spatial-annotation", 5, scene.id);
        add(annotation.range.end - 1 / project.fps, "spatial-annotation-end", 3, scene.id);
      }
    }
    for (const cue of scene.captions) {
      add(cue.range.start + Math.min(0.25, (cue.range.end - cue.range.start) / 2), "caption-entry", 2, scene.id);
      add(cue.range.end - 1 / project.fps, "caption-end", 1, scene.id);
    }
    for (const layer of scene.visualLayers) {
      const recording = context.interactions?.get(layer.assetId || ""), asset = assets.get(layer.assetId || "");
      if (!recording || !asset) continue;
      const used = sourceRange(layer, scene.range);
      for (const action of recordedActions(recording, asset).filter((action2) => action2.start >= used.start && action2.start < used.end && action2.type !== "wait")) {
        const start = sourceTimeToFilm(action.start, layer, scene.range), end = sourceTimeToFilm(action.end, layer, scene.range);
        add(start - 0.12, "before-action", 6, scene.id);
        add(start + 0.12, "action", 7, scene.id);
        if (end + 0.35 < scene.range.end) add(end + 0.35, action.result ? "observed-result" : "check-action-result", 7, scene.id);
      }
    }
  }
  for (const moment of findReviewMoments(project, 24)) add(moment.atSeconds, "text-settled", 4, moment.sceneId);
  const selected = [];
  const sceneIds = project.scenes.filter((scene) => overlap(scene.range, renderRange)).map((scene) => scene.id);
  const spread2 = (items, count) => items.length <= count ? items : count === 1 ? [items[Math.floor(items.length / 2)]] : Array.from({ length: count }, (_, i) => items[Math.round(i * (items.length - 1) / (count - 1))]);
  for (const id of spread2(sceneIds, Math.min(limit, sceneIds.length))) {
    const options2 = candidates.filter((c) => c.sceneId === id).sort((a, b) => b.priority - a.priority);
    const overview = options2.find((c) => c.reasons.includes("scene-overview"));
    if (options2[0]) selected.push(options2[0].priority >= 6 ? options2[0] : overview || options2[0]);
  }
  for (let priority = 7; priority >= 1 && selected.length < limit; priority--) {
    const choices = candidates.filter((c) => c.priority === priority && !selected.includes(c)).sort((a, b) => a.atSeconds - b.atSeconds);
    for (const choice of spread2(choices, limit - selected.length)) if (!selected.some((item) => Math.abs(item.atSeconds - choice.atSeconds) < 0.04)) selected.push(choice);
  }
  return selected.sort((a, b) => a.atSeconds - b.atSeconds);
}
function parseMediaMeasurements(log2, duration) {
  const intervals = (startName, endName) => {
    const values = [];
    let start;
    for (const line of log2.split("\n")) {
      const beginning = line.match(new RegExp(`${startName}:\\s*([\\d.]+)`));
      if (beginning) start = Number(beginning[1]);
      const ending = line.match(new RegExp(`${endName}:\\s*([\\d.]+)`));
      if (ending && start !== void 0) {
        const end = Math.min(duration, Number(ending[1]));
        if (end > start) values.push({ start, end });
        start = void 0;
      }
    }
    if (start !== void 0 && start < duration) values.push({ start, end: duration });
    return values;
  };
  const silence = intervals("silence_start", "silence_end"), nearStatic = intervals("freeze_start", "freeze_end");
  const black = [...log2.matchAll(/black_start:([\d.]+)\s+black_end:([\d.]+)/g)].map((match) => ({ start: Number(match[1]), end: Math.min(duration, Number(match[2])) }));
  const summary = log2.slice(log2.lastIndexOf("Summary:"));
  const finite = (value) => value !== void 0 && Number.isFinite(Number(value)) ? Number(value) : null;
  return {
    black,
    silence,
    nearStatic,
    silenceSeconds: silence.reduce((sum, range) => sum + range.end - range.start, 0),
    nearStaticSeconds: nearStatic.reduce((sum, range) => sum + range.end - range.start, 0),
    integratedLufs: finite(summary.match(/I:\s*([-\d.]+) LUFS/)?.[1]),
    truePeakDbfs: finite(summary.match(/Peak:\s*([-\d.]+) dBFS/)?.[1]),
    interpretation: "Times refer to this output file. Near-static images and silence can be intentional reading holds or pauses; they do not by themselves indicate a stalled renderer or a missing audio track."
  };
}
function measuredFindings(measurements, project, renderStart = 0) {
  const findings = [];
  for (const [kind, ranges] of [["BLACK_INTERVAL", measurements.black], ["NEAR_STATIC_HOLD", measurements.nearStatic.filter((r) => r.end - r.start >= 4)], ["LONG_AUDIO_PAUSE", measurements.silence.filter((r) => r.end - r.start >= 1.5)]]) {
    for (const range of ranges) {
      const filmRange = { start: range.start + renderStart, end: range.end + renderStart };
      findings.push({
        code: kind,
        category: kind === "LONG_AUDIO_PAUSE" ? "audio" : "timing",
        severity: kind === "BLACK_INTERVAL" ? "warning" : "info",
        sceneId: project?.scenes.find((scene) => overlap(scene.range, filmRange))?.id,
        range: filmRange,
        message: `${kind}: ${(range.end - range.start).toFixed(2)} \u79D2\uFF0C\u8BF7\u7ED3\u5408\u955C\u5934\u610F\u56FE\u590D\u67E5\u3002`,
        evidence: { outputRange: range },
        suggestedOperation: "Inspect this interval; shorten uninformative waiting or retain it with a recorded reading, processing, or pacing reason."
      });
    }
  }
  if (measurements.truePeakDbfs !== null && measurements.truePeakDbfs > -1) findings.push({ code: "AUDIO_PEAK_HEADROOM", category: "audio", severity: "warning", message: `\u97F3\u9891\u771F\u5CF0\u503C ${measurements.truePeakDbfs} dBFS\uFF0C\u7559\u7ED9\u540E\u7EED\u7F16\u7801\u7684\u4F59\u91CF\u8F83\u5C0F\u3002`, suggestedOperation: "Inspect/listen for distortion and lower the peak ceiling when needed." });
  return findings;
}

// src/anatomy-figure.ts
import fs9 from "node:fs/promises";
import path11 from "node:path";
import { randomUUID as randomUUID5 } from "node:crypto";
import { Script } from "node:vm";
init_util();
var MAX_FIGURE_BYTES = 32 * 1024 * 1024;
async function readFigureFile(file) {
  const info = await fs9.lstat(file);
  if (!info.isFile() || info.isSymbolicLink()) throw new Error("Anatomy figure must be a regular JSON file, not a directory or symbolic link.");
  if (info.size > MAX_FIGURE_BYTES) throw new Error("Anatomy figure exceeds the 32 MiB size limit.");
  const bytes = await fs9.readFile(file);
  if (bytes.length > MAX_FIGURE_BYTES) throw new Error("Anatomy figure exceeds the 32 MiB size limit.");
  let figure;
  try {
    figure = JSON.parse(bytes.toString("utf8"));
  } catch {
    throw new Error("Anatomy figure is not valid JSON.");
  }
  assertAuthoredAnatomyFigure(figure);
  try {
    new Script(`(${figure.script}
)`);
  } catch {
    throw new Error("Anatomy figure script must be a syntactically valid JavaScript function expression.");
  }
  return { figure, bytes, sha256: digest(bytes) };
}
async function localAssetPath(root, relative) {
  if (!relative || path11.isAbsolute(relative) || /^(?:[a-z]:|[\\/])/i.test(relative)) throw new Error("Anatomy asset path must be project-relative.");
  const file = inside(root, relative);
  const [realRoot, realFile] = await Promise.all([fs9.realpath(root), fs9.realpath(file)]);
  inside(realRoot, path11.relative(realRoot, realFile));
  return file;
}
async function importAnatomyFigure(root, input, provenance = {}) {
  root = projectRoot(root);
  if (/^[a-z][a-z\d+.-]*:\/\//i.test(input)) throw new Error("Anatomy import accepts a local authored .anatomy.json file. Download and inspect public source before building it locally.");
  const file = path11.resolve(input);
  const { figure, bytes, sha256: sha2562 } = await readFigureFile(file);
  await getProject(root);
  const mergedProvenance = { ...figure.provenance ?? {}, ...provenance };
  return updateProject(root, async (manifest) => {
    const existing = manifest.assets.find((asset2) => asset2.sha256 === sha2562 && asset2.kind === "anatomy-figure");
    if (existing) {
      const current = await readFigureFile(await localAssetPath(root, existing.relativePath));
      if (current.sha256 !== existing.sha256) throw new Error(`Anatomy asset ${existing.id} changed on disk. Restore it or import the corrected figure as a new asset.`);
      existing.provenance = { ...figure.provenance ?? {}, ...existing.provenance ?? {}, ...provenance };
      return existing;
    }
    const id = `asset-${sha2562.slice(0, 20)}`, relativePath = `assets/${id}.anatomy.json`;
    const destination = inside(root, relativePath);
    const assetsDirectory = inside(root, "assets");
    await fs9.mkdir(assetsDirectory, { recursive: true });
    const [realRoot, realAssets] = await Promise.all([fs9.realpath(root), fs9.realpath(assetsDirectory)]);
    inside(realRoot, path11.relative(realRoot, realAssets));
    const destinationInfo = await fs9.lstat(destination).catch((error) => {
      if (error.code === "ENOENT") return null;
      throw error;
    });
    if (destinationInfo && (!destinationInfo.isFile() || destinationInfo.isSymbolicLink())) throw new Error("Anatomy asset destination must be a regular file.");
    const temporary = `${destination}.${randomUUID5()}.tmp`;
    try {
      await fs9.writeFile(temporary, bytes, { flag: "wx" });
      await fs9.rename(temporary, destination);
    } finally {
      await fs9.rm(temporary, { force: true });
    }
    const asset = {
      id,
      relativePath,
      name: path11.basename(file),
      sha256: sha2562,
      kind: "anatomy-figure",
      metadata: {
        schemaVersion: figure.schemaVersion,
        width: figure.width,
        height: figure.height,
        parts: figure.parts,
        partCount: figure.parts.length,
        selfContained: true
      },
      provenance: mergedProvenance
    };
    manifest.assets.push(asset);
    return asset;
  });
}
async function bindAnatomyFigures(root, project, assets) {
  const definitions = project.anatomyFigures ?? {};
  if (!definitions || typeof definitions !== "object" || Array.isArray(definitions)) throw new Error("anatomyFigures must be an object keyed by figure ID.");
  for (const [id, definition] of Object.entries(definitions)) {
    if (!id.trim() || !definition || typeof definition !== "object" || typeof definition.assetId !== "string" || !definition.assetId.trim()) throw new Error(`Anatomy figure ${id} needs a registered assetId.`);
    if (Object.keys(definition).some((key) => key !== "assetId")) throw new Error(`Anatomy figure ${id} accepts only assetId; use anatomy import to register authored code.`);
    const asset = assets.get(definition.assetId);
    if (!asset || asset.kind !== "anatomy-figure") throw new Error(`Anatomy figure ${id} references missing anatomy-figure asset ${definition.assetId}.`);
  }
  const loaded = /* @__PURE__ */ new Map();
  for (const scene of project.scenes) {
    const anatomy = scene.spatial?.anatomy;
    if (!anatomy) continue;
    if (Object.prototype.hasOwnProperty.call(anatomy, "authoredFigure")) throw new Error("Use anatomy.figureId and registered anatomyFigures assets, not authoredFigure, in project.json.");
    if (anatomy.figureId === void 0) continue;
    if (typeof anatomy.figureId !== "string" || !anatomy.figureId.trim() || !Object.prototype.hasOwnProperty.call(definitions, anatomy.figureId)) throw new Error(`Scene ${scene.id} references missing anatomy figure ${anatomy.figureId}.`);
    const asset = assets.get(definitions[anatomy.figureId].assetId);
    if (!loaded.has(asset.id)) {
      const { figure, sha256: sha2562 } = await readFigureFile(await localAssetPath(root, asset.relativePath));
      if (sha2562 !== asset.sha256) throw new Error(`Anatomy asset ${asset.id} changed on disk; import it again before rendering.`);
      loaded.set(asset.id, { ...figure, provenance: { ...figure.provenance ?? {}, ...asset.provenance ?? {} } });
    }
    anatomy.authoredFigure = loaded.get(asset.id);
  }
}

// src/edit.ts
async function qualityContext(root, project, director) {
  const manifest = await getProject(root);
  const state = director ?? await readJson(path12.join(root, "director-state.json")).catch((error) => {
    if (error.code === "ENOENT") return {};
    throw error;
  });
  const interactions = /* @__PURE__ */ new Map();
  const used = new Set(project.scenes.flatMap((scene) => [
    ...scene.visualLayers.map((layer) => layer.assetId),
    ...(scene.spatial?.models ?? []).map((model) => model.assetId)
  ]));
  const issues = [];
  for (const asset of manifest.assets.filter((asset2) => used.has(asset2.id) && asset2.interactions)) {
    try {
      const recording = await readInteractions(root, asset);
      if (recording) interactions.set(asset.id, recording);
    } catch (error) {
      issues.push({ code: "INTERACTION_EVIDENCE_UNAVAILABLE", severity: "warning", category: "technical", message: `\u7D20\u6750 ${asset.id} \u7684\u4EA4\u4E92\u8BB0\u5F55\u4E0D\u53EF\u7528\uFF1A${error.message}` });
    }
  }
  const request = state.revisionRequest;
  const latest = [...manifest.artifacts].reverse().find((a) => a.renderContext && ["final", "preview"].includes(a.kind));
  const baselinePath = request?.kind === "visual-upgrade" ? request.baselineRenderContext : latest?.renderContext;
  let baseline;
  if (baselinePath) {
    try {
      const snapshot = await readJson(inside(root, baselinePath));
      baseline = sceneSourceUsage(snapshot.project, snapshot.evidenceContext?.assets ?? []);
    } catch (error) {
      if (request?.kind === "visual-upgrade") issues.push({ code: "VISUAL_REVISION_BASELINE_UNAVAILABLE", severity: "error", category: "semantic_alignment", message: error.message });
    }
  }
  issues.push(...visualRevisionFindings(sceneSourceUsage(project, manifest.assets), baseline, request));
  return { director: state, assets: manifest.assets, interactions, issues };
}
async function bindTimeline(root, input) {
  const original = await loadTimeline(root, input);
  let project = JSON.parse(JSON.stringify(original));
  const manifest = await getProject(root), assets = new Map(manifest.assets.map((asset) => [asset.id, asset]));
  if (!Array.isArray(project.scenes)) throw new Error("Timeline scenes must be an array.");
  for (const scene of project.scenes) {
    scene.purpose ??= "";
    scene.message ??= "";
    scene.captions ??= [];
    scene.claimIds ??= [];
    scene.protectedRegions ??= [];
    scene.visualLayers ??= [];
    for (const layer of scene.visualLayers) {
      layer.source ??= "asset";
      layer.zIndex ??= 10;
      layer.opacity ??= 1;
      layer.semanticTags ??= [];
      if (assets.get(layer.assetId)?.metadata?.hasAudio && layer.audioGainDb === void 0) layer.audioGainDb = 0;
    }
    if (scene.voiceover) scene.voiceover.semanticTags ??= [];
    for (const model of scene.spatial?.models ?? []) {
      if (model.assetId) {
        const asset = assets.get(model.assetId);
        if (!asset || asset.kind !== "model3d") throw new Error(`Spatial model ${model.id} references missing model3d asset ${model.assetId}.`);
      }
    }
  }
  const bind = async (value) => {
    if (!value || typeof value !== "object") return;
    if (value.assetPath !== void 0) throw new Error("Use registered assetId references, not assetPath, in project.json.");
    if (value.assetId) {
      const asset = assets.get(value.assetId);
      if (!asset) throw new Error(`Timeline references missing asset ${value.assetId}`);
      const file = inside(root, asset.relativePath);
      if (await sha256(file) !== asset.sha256) throw new Error(`Asset ${asset.id} changed on disk; import it again before rendering.`);
      value.assetPath = file;
      if (["video", "image"].includes(asset.kind)) {
        value.mediaKind = asset.kind;
        value.mediaWidth = asset.metadata?.width;
        value.mediaHeight = asset.metadata?.height;
      }
      if (value.sourceRange && asset.metadata?.durationSeconds > 0 && value.sourceRange.end > asset.metadata.durationSeconds + 0.05) throw new Error(`Source range exceeds ${asset.id} duration.`);
    }
    for (const [key, child] of Object.entries(value)) if (key !== "anatomyFigures" && key !== "authoredFigure" && child && typeof child === "object") {
      if (Array.isArray(child)) for (const item of child) await bind(item);
      else await bind(child);
    }
  };
  await bindAnatomyFigures(root, project, assets);
  await bind(project);
  project = normalizeMotionTimeBases(expandMotionIntents(project));
  if (project.autoCaptions) {
    for (const scene of project.scenes) {
      if (scene.captions.length) continue;
      const track = scene.voiceover || scene.visualLayers.find((layer) => assets.get(layer.assetId)?.transcript);
      const asset = assets.get(track?.assetId);
      if (!track || !asset?.transcript) continue;
      const transcript = await readJson(inside(root, asset.transcript));
      const sourceStart = track.sourceStartSeconds ?? track.sourceRange?.start ?? 0;
      const outputRange = track.range || scene.range;
      const rate = track.sourcePlaybackRate || (track.sourceRange ? (track.sourceRange.end - track.sourceRange.start) / (scene.range.end - scene.range.start) : 1);
      const cues = transcript.cues.map((cue) => ({ text: cue.text, range: { start: sourceStart + (cue.start - sourceStart) / rate, end: sourceStart + (cue.end - sourceStart) / rate } }));
      scene.captions = buildAutoCaptions({ spec: project.autoCaptions, canvas: project, sceneId: scene.id, sceneRange: scene.range, voiceover: { range: outputRange, sourceStartSeconds: sourceStart }, cues });
    }
  }
  assertVideoProject(project);
  if (![project.width, project.height].every((v) => Number.isInteger(v) && v >= 2 && v % 2 === 0) || project.fps > 120) throw new Error("Use even integer canvas dimensions and fps no greater than 120.");
  return { original, project };
}
async function validateTimeline(root, input) {
  const { project } = await bindTimeline(root, input);
  const context = await qualityContext(root, project);
  return {
    valid: true,
    projectId: project.projectId,
    scenes: project.scenes.length,
    durationSeconds: project.durationSeconds,
    width: project.width,
    height: project.height,
    fps: project.fps,
    quality: buildQualityReport(project, context),
    reviewPlan: planReviewFrames(project, { start: 0, end: project.durationSeconds }, context),
    consumption: buildRenderConsumptionReport(project, (await getProject(root)).revision)
  };
}
async function compile(root, options2 = {}) {
  const { original, project } = await bindTimeline(root, options2.input);
  const revision = await checkpointTimeline(root, original);
  const context = await qualityContext(root, project);
  const range = { start: options2.start ?? 0, end: options2.end ?? project.durationSeconds };
  const scale = options2.scale ?? (options2.preview ? 0.5 : 1), fps = options2.fps ?? (options2.preview ? Math.min(project.fps, 15) : project.fps);
  const directory = path12.join(root, "work", `r${revision}`, options2.preview ? "preview" : "final");
  const composition = await compileHyperFramesProject(project, directory, root, { renderScale: scale, renderRange: range, renderFps: fps });
  const delivery = { ...project, width: Math.max(2, Math.round(project.width * scale / 2) * 2), height: Math.max(2, Math.round(project.height * scale / 2) * 2), fps, durationSeconds: range.end - range.start };
  const evidenceContext = { assets: context.assets, issues: context.issues, recordings: Object.fromEntries([...(context.interactions ?? /* @__PURE__ */ new Map()).entries()].map(([id, recording]) => [id, { ...recording, events: recording.events.filter((event) => event.type === "pointerdown") }])) };
  const spatialScenes = project.scenes.filter((scene) => Boolean(scene.spatial) && scene.range.end > range.start && scene.range.start < range.end);
  const spatialRuntime = spatialScenes.length ? { version: SPATIAL_RUNTIME_VERSION, anatomyVersion: spatialScenes.some((scene) => scene.spatial && spatialBackend(scene.spatial) === "anatomy") ? ANATOMY_RUNTIME_VERSION : void 0, requestedBackends: [...new Set(spatialScenes.flatMap((scene) => scene.spatial?.anatomy && scene.spatial.models.length ? ["anatomy", "three"] : [scene.spatial ? spatialBackend(scene.spatial) : "three"]))], deterministic: true, projectLocalAssetsOnly: true } : void 0;
  const result = { revision, composition, directory, range, scale, fps, delivery, project, director: context.director, evidenceContext, spatialRuntime, sourceUsage: sceneSourceUsage(project, context.assets ?? []), quality: buildQualityReport(project, context) };
  await writeJson(path12.join(directory, "build.json"), result);
  return result;
}
async function render(root, options2 = {}) {
  const build2 = await compile(root, options2);
  const blockers = build2.quality.findings.filter((f) => f.severity === "error" && f.code.startsWith("VISUAL_REVISION_"));
  if (blockers.length) throw new Error(JSON.stringify(blockers));
  const observed = [];
  const kind = options2.preview ? "preview" : "final";
  const intermediate = path12.join(build2.directory, "rendered.mp4");
  const output = path12.join(root, "outputs", `r${build2.revision}-${kind}.mp4`);
  await renderWithHyperFrames(build2.composition, intermediate, void 0, root, ({ message: _message, ...progress }) => process.stderr.write(JSON.stringify(progress) + "\n"), { inactivityTimeoutMs: 12e4, spatial: build2.project.scenes.some((scene) => Boolean(scene.spatial) && scene.range.end > build2.range.start && scene.range.start < build2.range.end), onSpatialEvidence: (evidence) => observed.push(evidence) });
  for (const scene of build2.project.scenes.filter((s) => s.spatial && s.range.end > build2.range.start && s.range.start < build2.range.end)) {
    if (!observed.some((o) => o.sceneId === scene.id)) throw new Error(`SPATIAL_CAPTURE_EVIDENCE_MISSING: ${scene.id}`);
  }
  await normalizeFinalRender(build2.delivery, intermediate, output);
  const contextRelative = `outputs/r${build2.revision}-${kind}-${randomUUID6().slice(0, 8)}.render.json`;
  await writeJson(inside(root, contextRelative), { schemaVersion: 1, revision: build2.revision, range: build2.range, scale: build2.scale, fps: build2.fps, project: build2.project, director: build2.director, evidenceContext: build2.evidenceContext, spatialRuntime: { ...build2.spatialRuntime, observed }, sourceUsage: build2.sourceUsage });
  await saveArtifact(root, kind, output, build2.revision, contextRelative);
  const project = build2.delivery;
  const cues = project.scenes.flatMap((scene) => scene.captions.map((cue) => ({ start: Math.max(0, cue.range.start - build2.range.start), end: Math.min(build2.delivery.durationSeconds, cue.range.end - build2.range.start), text: cue.text }))).filter((cue) => cue.end > cue.start).sort((a, b) => a.start - b.start);
  const subtitleFiles = cues.length ? await writeSubtitles(root, cues, `r${build2.revision}-${kind}`, build2.revision) : [];
  return { revision: build2.revision, output, subtitles: subtitleFiles, metadata: await probe(output), quality: build2.quality, sourceUsage: build2.sourceUsage, spatialRuntime: { ...build2.spatialRuntime, observed }, renderContext: inside(root, contextRelative), instruction: "Run review and inspect the returned images before judging visual quality." };
}
async function review(root, input, requestedTimes, limit = 24) {
  const manifest = await getProject(root);
  const latest = [...manifest.artifacts].reverse().find((item) => item.kind === "final" || item.kind === "preview");
  const file = input ? path12.resolve(input) : latest ? inside(root, latest.relativePath) : "";
  if (!file) throw new Error("Render a preview or provide --input before reviewing.");
  const metadata = await probe(file), duration = metadata.durationSeconds;
  if (!(duration > 0) || !metadata.width) throw new Error("Rendered video is invalid.");
  const artifact = [...manifest.artifacts].reverse().find((item) => ["final", "preview"].includes(item.kind) && inside(root, item.relativePath) === file);
  let snapshot = null, contextWarning;
  if (artifact) {
    if (artifact.renderContext) snapshot = await readJson(inside(root, artifact.renderContext));
    else {
      try {
        const build2 = await readJson(path12.join(root, "work", `r${artifact.revision}`, artifact.kind, "build.json"));
        if (Math.abs(build2.range.end - build2.range.start - duration) < 0.15) {
          const bound = await bindTimeline(root, path12.join(root, "versions", `r${artifact.revision}.json`));
          snapshot = { revision: artifact.revision, range: build2.range, project: bound.project, director: {} };
          contextWarning = "Legacy artifact: timeline revision is known, but no frozen director plan was saved.";
        }
      } catch {
        contextWarning = "Legacy artifact context is unavailable; only media measurements and generic frames are reported.";
      }
    }
  }
  if (snapshot && Math.abs(snapshot.range.end - snapshot.range.start - duration) >= 0.15) throw new Error("Render context duration does not match this video.");
  const project = snapshot?.project;
  const context = snapshot?.evidenceContext ? { ...snapshot.evidenceContext, director: snapshot.director || {}, interactions: new Map(Object.entries(snapshot.evidenceContext.recordings || {})) } : project ? await qualityContext(root, project, snapshot.director || {}) : void 0;
  const quality = project ? buildQualityReport(project, context) : void 0;
  const plan = project ? planReviewFrames(project, snapshot.range, context, limit) : [0, duration * 0.25, duration * 0.5, duration * 0.75, Math.max(0, duration - 0.1)].slice(0, Math.max(1, Math.min(24, limit))).map((time) => ({ atSeconds: time, timelineSeconds: time, reasons: ["unregistered-media-sample"], priority: 1 }));
  const times2 = requestedTimes || plan.map((moment) => moment.atSeconds), revision = artifact?.revision ?? null;
  const evidence = await frames(root, file, [...new Set(times2)], `review-r${revision ?? "external"}-${Date.now()}`);
  const viewingWidth = Math.min(metadata.width, quality?.profile.viewingWidth || 960);
  const sharp = runtimeRequire()("sharp");
  const smallScreenFrames = await Promise.all(evidence.frames.map(async (frame) => {
    const small = frame.path.replace(/\.jpg$/, "-viewing.jpg");
    await sharp(frame.path).resize({ width: Math.round(viewingWidth) }).jpeg({ quality: 88 }).toFile(small);
    return { atSeconds: frame.atSeconds, width: viewingWidth, path: small };
  }));
  const result = await run(getFfmpegBinaryPath(), [
    "-hide_banner",
    "-nostats",
    "-i",
    file,
    "-vf",
    "blackdetect=d=0.04:pix_th=0.1,freezedetect=n=-45dB:d=2",
    ...metadata.hasAudio ? ["-af", "silencedetect=n=-45dB:d=1,ebur128=peak=true:framelog=verbose"] : [],
    "-f",
    "null",
    "-"
  ], { timeout: 10 * 6e4 });
  const measurements = parseMediaMeasurements(result.stderr, duration);
  const mediaFindings = measuredFindings(measurements, project, snapshot?.range.start ?? 0);
  const runtimeIssues = /* @__PURE__ */ new Set();
  for (const observed of snapshot?.spatialRuntime?.observed ?? []) for (const diagnostic of observed.diagnostics ?? []) {
    const key = observed.sceneId + diagnostic.code + diagnostic.partId;
    if (runtimeIssues.has(key)) continue;
    runtimeIssues.add(key);
    mediaFindings.push({ code: diagnostic.code, severity: diagnostic.severity ?? "warning", category: "technical", sceneId: observed.sceneId, message: diagnostic.message, evidence: { backend: observed.backend, atSeconds: observed.atSeconds } });
  }
  if (quality) {
    quality.findings.push(...mediaFindings);
    quality.counts = { error: quality.findings.filter((f) => f.severity === "error").length, warning: quality.findings.filter((f) => f.severity === "warning").length, info: quality.findings.filter((f) => f.severity === "info").length };
  }
  const report = {
    schemaVersion: 2,
    input: file,
    revision,
    metadata,
    frames: evidence.frames,
    smallScreenFrames,
    renderRange: snapshot?.range ?? null,
    contextWarning: contextWarning || (!snapshot ? "No matching render context: this review does not judge the current project timeline." : void 0),
    sourceUsage: snapshot?.sourceUsage,
    spatialRuntime: snapshot?.spatialRuntime,
    reviewPlan: plan,
    quality,
    measurements,
    mediaFindings,
    findings: result.stderr.split("\n").filter((line) => /black_start:|silence_start:|silence_end:|freeze_start:|freeze_end:/.test(line)),
    visualReview: "pending",
    instruction: "Inspect the actual full-size and viewing-size images. Compare the shot intent with visible actions/results. Use extra --times or a local preview around findings; record corrections or intentional holds, then review the affected render again. Technical checks do not certify visual quality."
  };
  const reportFile = path12.join(root, "outputs", `review-r${revision ?? "external"}-${Date.now()}.json`);
  await writeJson(reportFile, report);
  await saveArtifact(root, "review", reportFile, revision ?? void 0);
  return { ...report, reportFile };
}

// src/sources.ts
import fs11 from "node:fs/promises";
import path14 from "node:path";

// src/browser.ts
import fs10 from "node:fs/promises";
import path13 from "node:path";
import { spawn as spawn3 } from "node:child_process";
init_util();
async function session(root, requestedDensity) {
  if (requestedDensity !== void 0 && ![1, 2].includes(requestedDensity)) throw new Error("Browser dpr must be 1 or 2.");
  await getProject(root);
  const file = path13.join(root, "work", "browser-session.json");
  return withLock(`${file}.lock`, async () => {
    const prior = await readJson(file).catch(() => null);
    if (prior?.status === "ready") {
      let alive = false;
      try {
        process.kill(prior.pid, 0);
        alive = true;
      } catch {
      }
      if (alive) {
        if (requestedDensity !== void 0 && requestedDensity !== (prior.nativeDpr ?? 1)) throw new Error("Browser capture density is fixed for this session. Run browser close, then browser open with the desired --dpr before recording.");
        return prior;
      }
    }
    await fs10.rm(file, { force: true });
    const handle = await fs10.open(path13.join(root, "work", "browser-worker.log"), "a");
    const child = spawn3(process.execPath, [path13.join(PLUGIN_ROOT, "dist", "browser-worker.mjs"), root, String(requestedDensity ?? 1)], { detached: true, stdio: ["ignore", handle.fd, handle.fd], windowsHide: true, env: process.env });
    child.unref();
    await handle.close();
    for (let i = 0; i < 600; i++) {
      const result = await readJson(file).catch(() => null);
      if (result?.status === "ready") return result;
      if (result?.status === "failed") throw new Error(result.error);
      await new Promise((resolve2) => setTimeout(resolve2, 100));
    }
    throw new Error("Browser worker startup timed out; inspect work/browser-worker.log.");
  });
}
async function browserRequest(root, operation2, payload = {}) {
  const worker = await session(root, operation2 === "open" ? payload.dpr : void 0);
  const response = await fetch(`http://127.0.0.1:${worker.port}/command`, { method: "POST", headers: { authorization: `Bearer ${worker.token}`, "content-type": "application/json" }, body: JSON.stringify({ operation: operation2, payload }), signal: AbortSignal.timeout(18e4) });
  const result = await response.json();
  if (!response.ok || !result.ok) throw new Error(result.error || `Browser worker HTTP ${response.status}`);
  return result.result;
}

// src/sources.ts
init_util();
function excludedSource(relative) {
  const parts = relative.replaceAll("\\", "/").split("/");
  return parts.some((part) => /^(?:\.git|node_modules|\.pnpm|\.venv|venv|__pycache__|dist|build|release|\.next|\.cache|\.aws|\.ssh|\.codex|\.agents)$/i.test(part)) || parts.some((part) => /^(?:\.env(?:\..*)?|\.npmrc|\.pypirc|credentials(?:\..*)?|id_rsa|id_ed25519)$/i.test(part) && !/^\.env\.(?:example|sample|template)$/i.test(part)) || /\.(?:pem|p12|pfx|key)$/i.test(relative);
}
async function copySource(from, to) {
  const files = await listFiles(from, excludedSource);
  let bytes = 0;
  for (const relative of files) {
    const input = inside(from, relative), info = await fs11.stat(input);
    if (info.size > 128 * 1024 ** 2 || (bytes += info.size) > 512 * 1024 ** 2) throw new Error("Repository snapshot exceeds 512 MiB total or 128 MiB per file. Select a smaller source.");
    const output = inside(to, relative);
    await fs11.mkdir(path14.dirname(output), { recursive: true });
    await fs11.copyFile(input, output);
  }
  return files;
}
async function addSource(root, locator, ref) {
  await getProject(root);
  const url = /^https?:\/\//i.test(locator) ? new URL(locator) : null;
  if (url?.username || url?.password) throw new Error("Source URLs must not contain credentials.");
  if (url && url.hostname !== "github.com") {
    const observation = await browserRequest(root, "open", { url: url.href });
    const asset = await importMedia(root, observation.screenshot, { kind: "website-screenshot", url: observation.url, observedAt: observation.observedAt });
    const version2 = digest(JSON.stringify({ url: observation.url, text: observation.text, image: asset.sha256 }));
    const id = `source-${version2.slice(0, 20)}`, relativePath = `sources/${id}`;
    await fs11.mkdir(inside(root, relativePath), { recursive: true });
    await fs11.writeFile(inside(root, `${relativePath}/page.txt`), observation.text);
    await writeJson(inside(root, `${relativePath}/page.json`), observation);
    const source = { id, kind: "website", locator: observation.url, version: version2, relativePath, files: ["page.txt", "page.json"], capturedAt: observation.observedAt, assetIds: [asset.id] };
    await updateProject(root, (manifest) => {
      if (!manifest.sources.some((item) => item.id === id)) manifest.sources.push(source);
    });
    return { source, screenshotAsset: asset, media: observation.media };
  }
  let version, files, temporary = path14.join(root, "work", `import-${Date.now()}`);
  await fs11.mkdir(temporary, { recursive: true });
  try {
    if (url) {
      const segments = url.pathname.split("/").filter(Boolean);
      if (segments.length < 2) throw new Error("Use a GitHub repository URL.");
      const [owner, rawName] = segments, name = rawName.replace(/\.git$/, "");
      const requestedRef = ref || (segments[2] === "tree" ? segments.slice(3).join("/") : "HEAD");
      const response = await fetch(`https://api.github.com/repos/${encodeURIComponent(owner)}/${encodeURIComponent(name)}/commits/${encodeURIComponent(requestedRef)}`, { headers: { "User-Agent": "Wandeo/0.1" } });
      if (!response.ok) throw new Error(`GitHub returned ${response.status}; public repositories only. Use a local checkout if authentication is required.`);
      version = String((await response.json()).sha);
      if (!/^[a-f0-9]{40}$/.test(version)) throw new Error("GitHub did not resolve an immutable commit.");
      const archive = path14.join(temporary, "source.zip");
      await download(`https://codeload.github.com/${owner}/${name}/zip/${version}`, archive, void 0, 128 * 1024 ** 2);
      const extracted = path14.join(temporary, "extracted");
      await extractZip(archive, extracted, true, (name2) => !excludedSource(name2));
      files = await listFiles(extracted, excludedSource);
      temporary = extracted;
    } else {
      locator = path14.resolve(locator);
      const snapshot = path14.join(temporary, "snapshot");
      files = await copySource(locator, snapshot);
      const hashes = [];
      for (const file of files) hashes.push(`${file}:${await sha256(inside(snapshot, file))}`);
      version = digest(hashes.join("\n"));
      temporary = snapshot;
    }
    const id = `source-${digest(locator + ":" + version).slice(0, 20)}`, relativePath = `sources/${id}`, destination = inside(root, relativePath);
    const existing = (await getProject(root)).sources.find((source2) => source2.id === id);
    if (existing) return { source: existing, reused: true };
    await fs11.rename(temporary, destination);
    const source = { id, kind: "repository", locator, version, relativePath, files, capturedAt: (/* @__PURE__ */ new Date()).toISOString(), assetIds: [] };
    await updateProject(root, (manifest) => {
      manifest.sources.push(source);
    });
    return { source, reused: false };
  } finally {
    const parent = path14.basename(temporary) === "snapshot" || path14.basename(temporary) === "extracted" ? path14.dirname(temporary) : temporary;
    if (path14.basename(parent).startsWith("import-")) await fs11.rm(parent, { recursive: true, force: true });
  }
}
async function getSource(root, id) {
  const source = (await getProject(root)).sources.find((source2) => source2.id === id);
  if (!source) throw new Error(`Unknown source: ${id}`);
  return source;
}
async function readSource(root, id, relative, offset = 0, limit = 12e3) {
  if (!Number.isInteger(offset) || offset < 0 || !Number.isInteger(limit) || limit < 1 || limit > 64e3) throw new Error("Use nonnegative byte offset and a limit from 1 to 64000.");
  const source = await getSource(root, id);
  if (!source.files.includes(relative)) throw new Error("File is not part of this source snapshot.");
  const file = inside(inside(root, source.relativePath), relative);
  const handle = await fs11.open(file, "r");
  try {
    const info = await handle.stat(), buffer = Buffer.alloc(Math.min(Math.max(1, limit), 64e3));
    const { bytesRead } = await handle.read(buffer, 0, buffer.length, Math.max(0, offset));
    if (buffer.subarray(0, bytesRead).includes(0)) throw new Error("Binary resource: import it as media and inspect its actual pixels.");
    return { sourceId: id, version: source.version, path: relative, offset, nextOffset: offset + bytesRead < info.size ? offset + bytesRead : null, text: buffer.subarray(0, bytesRead).toString("utf8") };
  } finally {
    await handle.close();
  }
}
async function searchSources(root, query, id) {
  if (!query) throw new Error("Provide --query.");
  const results = [], sources = (await getProject(root)).sources.filter((source) => !id || source.id === id);
  for (const source of sources) for (const relative of source.files) {
    if (results.length >= 100) break;
    const file = inside(inside(root, source.relativePath), relative);
    if ((await fs11.stat(file)).size > 1024 * 1024) continue;
    const buffer = await fs11.readFile(file);
    if (buffer.includes(0)) continue;
    const lines = buffer.toString("utf8").split("\n");
    for (let i = 0; i < lines.length && results.length < 100; i++) if (lines[i].toLowerCase().includes(query.toLowerCase())) results.push({ sourceId: source.id, version: source.version, path: relative, line: i + 1, text: lines[i].slice(0, 500) });
  }
  return { results, capped: results.length >= 100 };
}
async function fetchSourceMedia(root, id, url) {
  const source = await getSource(root, id), parsed = new URL(url);
  const extension = path14.extname(parsed.pathname).toLowerCase();
  if (!/^\.(mp4|webm|mov|m4v|mp3|wav|m4a|ogg|png|jpe?g|webp|gif|avif|glb|gltf)$/.test(extension)) throw new Error("Use a direct supported media or GLB/GLTF model URL.");
  const file = path14.join(root, "work", `download-${digest(url).slice(0, 16)}${extension}`);
  await download(url, file, void 0, /\.(glb|gltf)$/.test(extension) ? 512 * 1024 ** 2 : 256 * 1024 ** 2);
  const asset = await importMedia(root, file, { sourceId: id, sourceVersion: source.version, url });
  await updateProject(root, (manifest) => {
    const entry = manifest.sources.find((s) => s.id === id);
    if (!entry.assetIds.includes(asset.id)) entry.assetIds.push(asset.id);
  });
  return asset;
}

// src/execution.ts
import fs12 from "node:fs/promises";
import path15 from "node:path";
import { spawn as spawn4 } from "node:child_process";
import { randomUUID as randomUUID7 } from "node:crypto";
init_util();
function taskFile(root, id) {
  if (!/^[a-z0-9-]+$/.test(id)) throw new Error("Invalid task ID.");
  return inside(root, `work/tasks/${id}.json`);
}
async function startExecution(root, request) {
  await getProject(root);
  if (!request.sourceId || !request.command || !Array.isArray(request.args || [])) throw new Error("Execution request needs sourceId, command and args.");
  const source = await getSource(root, request.sourceId);
  if (source.kind !== "repository") throw new Error("Only repository sources have an execution copy.");
  const workspace = inside(root, `work/runs/${source.id}`);
  if (!await exists(path15.join(workspace, ".wandeo-copy.json"))) {
    await copySource(inside(root, source.relativePath), workspace);
    await writeJson(path15.join(workspace, ".wandeo-copy.json"), { sourceId: source.id, version: source.version });
  }
  const cwd = inside(workspace, request.cwd || ".");
  const fingerprint = digest(JSON.stringify({ sourceVersion: source.version, cwd, command: request.command, args: request.args || [], runtimeId: request.runtimeId, env: request.env || {} }));
  let binDirectories = [];
  if (request.runtimeId) {
    if (!/^[a-z0-9-]+$/.test(request.runtimeId)) throw new Error("Invalid runtime ID.");
    const runtimeRoot = path15.join(cacheRoot(), "portable", request.runtimeId);
    const descriptor = await readJson(path15.join(runtimeRoot, "runtime.json"));
    binDirectories = descriptor.binDirectories.map((directory) => inside(runtimeRoot, directory));
  }
  if (request.requestKey) {
    const directory = path15.join(root, "work", "tasks");
    for (const file2 of await fs12.readdir(directory).catch(() => [])) {
      if (!file2.endsWith(".json") || file2.endsWith(".request.json")) continue;
      const previous = await readJson(path15.join(directory, file2)).catch(() => null);
      if (previous?.requestKey === request.requestKey && previous.sourceId === source.id && ["starting", "running", "succeeded"].includes(previous.status)) {
        if (previous.fingerprint !== fingerprint) throw new Error("This requestKey was used with different execution inputs; select a new requestKey.");
        return previous;
      }
    }
  }
  const id = `exec-${randomUUID7()}`, file = taskFile(root, id);
  const payload = { ...request, id, fingerprint, project: root, cwd, workspace, binDirectories, startedAt: (/* @__PURE__ */ new Date()).toISOString() };
  await writeJson(file.replace(/\.json$/, ".request.json"), payload);
  await writeJson(file, { ...payload, env: void 0, status: "starting" });
  const worker = spawn4(process.execPath, [path15.join(PLUGIN_ROOT, "dist", "exec-worker.mjs"), file], { detached: true, stdio: "ignore", windowsHide: true });
  worker.unref();
  for (let i = 0; i < 100; i++) {
    const task = await readJson(file);
    if (task.status !== "starting") return task;
    await new Promise((resolve2) => setTimeout(resolve2, 50));
  }
  return readJson(file);
}
async function executionStatus(root, id) {
  const file = taskFile(root, id), task = await readJson(file);
  if (["running", "starting"].includes(task.status) && task.workerPid) {
    try {
      process.kill(task.workerPid, 0);
    } catch {
      task.status = "interrupted";
      task.finishedAt = (/* @__PURE__ */ new Date()).toISOString();
      await writeJson(file, task);
    }
  }
  return task;
}
async function executionLogs(root, id, offset = 0, limit = 12e3) {
  await executionStatus(root, id);
  const file = taskFile(root, id).replace(/\.json$/, ".log");
  const handle = await fs12.open(file, "r");
  try {
    const buffer = Buffer.alloc(Math.min(64e3, Math.max(1, limit))), info = await handle.stat();
    const { bytesRead } = await handle.read(buffer, 0, buffer.length, offset);
    return { id, offset, nextOffset: offset + bytesRead < info.size ? offset + bytesRead : null, text: buffer.subarray(0, bytesRead).toString("utf8") };
  } finally {
    await handle.close();
  }
}
async function stopExecution(root, id) {
  const task = await executionStatus(root, id);
  if (!["running", "starting"].includes(task.status)) return task;
  await fs12.writeFile(taskFile(root, id).replace(/\.json$/, ".stop"), "stop");
  for (let i = 0; i < 100; i++) {
    const current = await executionStatus(root, id);
    if (!["running", "starting"].includes(current.status)) return current;
    await new Promise((resolve2) => setTimeout(resolve2, 100));
  }
  throw new Error("Task did not stop within 10 seconds; inspect its task file and owned process IDs.");
}

// src/transcription.ts
import fs13 from "node:fs/promises";
import path16 from "node:path";
init_util();
async function ensureModel() {
  const descriptor = await readJson(path16.join(PLUGIN_ROOT, "runtime", "asr-model.json"));
  const root = path16.join(cacheRoot(), "models", `whisper-small-${descriptor.revision}`);
  await withLock(`${root}.lock`, async () => {
    for (const file of descriptor.files) await download(`https://huggingface.co/${descriptor.repository}/resolve/${descriptor.revision}/${file.path}`, path16.join(root, file.path), file);
    await writeJson(path16.join(root, ".complete.json"), { revision: descriptor.revision });
  });
  return root;
}
async function transcribe(root, id, language) {
  const asset = await assetById(root, id);
  if (!asset.metadata?.hasAudio) throw new Error("This asset has no audio track.");
  const asrRoot = await ensurePackages("asr"), model = await ensureModel();
  const pcm = path16.join(root, "work", `${id}.f32`);
  await run(getFfmpegBinaryPath(), ["-hide_banner", "-loglevel", "error", "-y", "-i", asset.path, "-vn", "-ac", "1", "-ar", "16000", "-f", "f32le", pcm], { timeout: 10 * 6e4 });
  const request = path16.join(root, "work", `${id}-asr-request.json`);
  await writeJson(request, { pcm, model, asrRoot, language: language === "auto" ? void 0 : language });
  try {
    const result = await run(process.execPath, [path16.join(PLUGIN_ROOT, "dist", "asr-worker.mjs"), request], { timeout: 2 * 60 * 6e4 });
    const transcript = JSON.parse(result.stdout);
    const output = path16.join(root, "evidence", `${id}-transcript.json`);
    await writeJson(output, transcript);
    await updateProject(root, (manifest) => {
      manifest.assets.find((item) => item.id === id).transcript = path16.relative(root, output).replaceAll("\\", "/");
    });
    await saveArtifact(root, "transcript", output);
    return { assetId: id, transcript: output, subtitles: await writeSubtitles(root, transcript.cues, id), ...transcript };
  } finally {
    await fs13.rm(pcm, { force: true });
    await fs13.rm(request, { force: true });
  }
}

// src/cli.ts
init_util();
init_privacy();
var strings = ["project", "input", "title", "asset", "times", "start", "end", "scale", "fps", "request", "id", "source", "query", "path", "offset", "limit", "name", "version", "descriptor", "url", "ref", "language", "width", "height", "cache", "duration", "dpr", "scene-start", "license"];
var options = {};
var group;
var operation;
var positional = [];
var help = {
  name: "Wandeo",
  version: "0.6.2",
  attribution: "Derived in part from Recordly (AGPLv3). Anatomy renderer is vendored at a fixed MIT-licensed revision.",
  usage: "wandeo <group> [operation] --project <directory> [options]",
  commands: {
    setup: "Install verified render dependencies. --with-asr also prepares offline transcription.",
    doctor: "Verify native architecture, checksums and browser launch.",
    project: "init [--title]; show; capabilities; recipes [--query --limit]; validate [--input] (includes Three.js/anatomy quality findings and review plan); compile [--input]. Edit project.json and director-state.json with host file tools.",
    media: "import --input <local media or public HTTPS GLB/GLTF> [--license --version]; probe --asset|--input (includes model nodes, animations, materials, textures and bounds); frames --asset|--input --times 0,1,2; transcribe --asset [--language]; interactions --asset; focus --asset [--start --end --duration --scene-start --width --height --limit].",
    anatomy: "import --input <local figure.anatomy.json> [--license --url]. Registers a self-contained authored figure without executing its script; reuse its asset ID through project.anatomyFigures and scene.spatial.anatomy.figureId.",
    source: "add --input <local-repository-or-URL> [--ref]; list; search --query [--source]; read --source --path [--offset --limit]; fetch --source --url.",
    runtime: "prepare --name node --version 24.21.0; or --descriptor <verified-runtime.json>.",
    exec: "start --request <file>; status|logs|stop --id <task>. Request: {sourceId,command,args,cwd?,runtimeId?,requestKey?,env?}.",
    browser: "open --url [--width --height --dpr 1|2]; observe; act --request <actions.json>; record-start [--source --no-cursor]; record-stop; close.",
    render: "preview|final [--input] [--start --end --scale --fps].",
    review: "[--input <video>] [--times] [--limit 1..24]. Returns targeted frames, viewing-size images, quality findings and audio/static-frame measurements."
  },
  browserActions: ["click: selector or x/y; optional resultSelector for an observable outcome", "type: selector,text,clear?", "scroll: deltaY,deltaX?", "move: x,y", "press: key", "wait: selector or seconds"],
  limitations: ["Local executor required.", "Browser recording is silent; existing asset audio is supported.", "Private services, paid generation and native desktop capture are not bundled.", "Imported models require WebGL; Three.js procedural scenes use Canvas 2D fallback, while anatomy uses the upstream SVG painter with a Canvas raster fallback. Unsupported section orientations fail explicitly."]
};
var need = (name) => {
  const value = options[name];
  if (typeof value !== "string" || !value) throw new Error(`--${name} is required.`);
  return value;
};
var number = (name, fallback) => {
  if (options[name] === void 0) return fallback;
  const value = Number(options[name]);
  if (!Number.isFinite(value)) throw new Error(`--${name} must be finite.`);
  return value;
};
var times = () => options.times ? String(options.times).split(",").map(Number) : void 0;
async function main() {
  const parsed = parseArgs({ allowPositionals: true, options: Object.fromEntries([...strings.map((name) => [name, { type: "string" }]), ...["help", "json", "with-asr", "no-cursor"].map((name) => [name, { type: "boolean" }])]) });
  options = parsed.values;
  [group, operation, ...positional] = parsed.positionals;
  if (options.cache) process.env.WANDEO_CACHE_DIR = path17.resolve(options.cache);
  if (!group || options.help || group === "help") return help;
  if (group === "setup") {
    const result = await setup();
    if (options["with-asr"]) {
      await ensurePackages("asr");
      await ensureModel();
    }
    return result;
  }
  if (group === "doctor") return doctor();
  if (group === "runtime" && operation === "prepare") return prepareRuntime(options.descriptor ? await readJson(need("descriptor")) : { name: need("name"), version: need("version") });
  const root = projectRoot(need("project"));
  if (group === "project" && operation === "init") return initProject(root, options.title);
  await getProject(root);
  if (group === "project" && operation === "capabilities") return inspectAutoEditRenderCapabilities();
  if (group === "project" && operation === "recipes") {
    const query = String(options.query || "").toLowerCase();
    const recipes = listShotRecipes().filter((recipe) => !query || JSON.stringify(recipe).toLowerCase().includes(query));
    return { total: recipes.length, recipes: recipes.slice(0, number("limit", 20)) };
  }
  if (group === "project" && operation === "show") return { root, manifest: await getProject(root), timeline: await readJson(path17.join(root, "project.json")), state: await readJson(path17.join(root, "director-state.json")) };
  if (group === "anatomy" && operation === "import") return importAnatomyFigure(root, need("input"), { ...options.license ? { license: options.license } : {}, ...options.url ? { url: options.url } : {} });
  if (group === "source" && operation === "list") return { sources: (await getProject(root)).sources };
  if (group === "source" && operation === "search") return searchSources(root, need("query"), options.source);
  if (group === "source" && operation === "read") return readSource(root, need("source"), need("path"), number("offset", 0), number("limit", 12e3));
  if (group === "exec") {
    if (operation === "start") return startExecution(root, await readJson(need("request")));
    if (operation === "status") return executionStatus(root, need("id"));
    if (operation === "logs") return executionLogs(root, need("id"), number("offset", 0), number("limit", 12e3));
    if (operation === "stop") return stopExecution(root, need("id"));
  }
  const modelInput = String(options.input || "").toLowerCase();
  const modelCommand = group === "media" && ["import", "probe"].includes(operation || "") && (modelFormat(modelInput) || /\.(glb|gltf)(?:[?#].*)?$/.test(modelInput));
  if (!modelCommand) await loadRuntime();
  if (group === "project" && operation === "validate") return validateTimeline(root, options.input);
  if (group === "project" && operation === "compile") return compile(root, { input: options.input });
  if (group === "source" && operation === "add") return addSource(root, options.input || options.url || positional[0] || need("input"), options.ref);
  if (group === "source" && operation === "fetch") return fetchSourceMedia(root, need("source"), need("url"));
  if (group === "media") {
    if (operation === "import") return importMedia(root, need("input"), { ...options.license ? { license: options.license } : {}, ...options.version ? { version: options.version } : {} });
    if (operation === "probe") return probe(options.asset ? (await assetById(root, options.asset)).path : need("input"));
    if (operation === "frames") return frames(root, options.asset || need("input"), times() || [0]);
    if (operation === "transcribe") return transcribe(root, need("asset"), options.language);
    if (operation === "interactions") {
      const asset = await assetById(root, need("asset")), recording = await readInteractions(root, asset);
      return { assetId: asset.id, recording: recording ? { ...recording, events: recording.events.slice(number("offset", 0), number("offset", 0) + number("limit", 200)), totalEvents: recording.events.length } : null };
    }
    if (operation === "focus") return suggestFocus(root, need("asset"), { start: number("start"), end: number("end"), width: number("width"), height: number("height"), duration: number("duration"), sceneStart: number("scene-start"), limit: number("limit") });
  }
  if (group === "browser") {
    if (operation === "open") return browserRequest(root, "open", { url: need("url"), width: number("width"), height: number("height"), dpr: number("dpr") });
    if (operation === "act") return browserRequest(root, "act", await readJson(need("request")));
    if (operation === "record-start") return browserRequest(root, "record-start", { sourceId: options.source, cursor: !options["no-cursor"] });
    if (["observe", "record-stop", "close"].includes(operation)) return browserRequest(root, operation);
  }
  if (group === "render" && ["preview", "final"].includes(operation)) return render(root, { input: options.input, preview: operation === "preview", start: number("start"), end: number("end"), scale: number("scale"), fps: number("fps") });
  if (group === "review") return review(root, options.input, times(), number("limit", 24));
  throw new Error(`Unknown command: ${group} ${operation || ""}. Run wandeo --help.`);
}
main().then((result) => {
  process.stdout.write(JSON.stringify({ ok: true, result: publicCommandResult(result, group, operation, options.project ? projectRoot(options.project) : void 0) }, null, 2) + "\n");
}).catch((error) => {
  const message = publicErrorMessage(error, options.project);
  process.stderr.write(`[wandeo] ${message}
`);
  process.stdout.write(JSON.stringify({ ok: false, error: { message } }) + "\n");
  process.exitCode = 1;
});
