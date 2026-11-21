/*
 * EXECUTION-TOOL HELPER — not a schema reference.
 * Shared by the sibling runnable scripts; keep it alongside them. Do NOT copy
 * its payload literals or logic into a new codebase as if they were the API
 * spec — for payload shape, load the canonical developers.sinch.com docs
 * linked from ../../SKILL.md instead.
 */
/**
 * Shared Sinch Voice API client utilities.
 *
 * Provides Basic Auth and environment variable helpers
 * used by all voice scripts. The Voice API uses Application Key + Secret.
 */

var https = require("https");

var DEFAULT_BASE = "https://calling.api.sinch.com";
var CONFIG_BASE = "https://callingapi.sinch.com";

var REGIONAL_BASES = {
  global: "https://calling.api.sinch.com",
  "north-america": "https://calling-use1.api.sinch.com",
  europe: "https://calling-euc1.api.sinch.com",
  "southeast-asia-1": "https://calling-apse1.api.sinch.com",
  "southeast-asia-2": "https://calling-apse2.api.sinch.com",
  "south-america": "https://calling-sae1.api.sinch.com",
};

function getEnv(name, defaultValue) {
  var value = process.env[name] || defaultValue;
  if (value === undefined || value === null) {
    process.stderr.write("Error: " + name + " environment variable is required\n");
    process.exit(1);
  }
  return value;
}

function getAuthHeader(appKey, appSecret) {
  return "Basic " + Buffer.from(appKey + ":" + appSecret).toString("base64");
}

var ALLOWED_HOSTS = new Set(
  Object.keys(REGIONAL_BASES).map(function (k) { return new URL(REGIONAL_BASES[k]).hostname; })
    .concat([new URL(DEFAULT_BASE).hostname, new URL(CONFIG_BASE).hostname])
);
var REQUEST_TIMEOUT_MS = 30000;

var SENSITIVE_KEY = /secret|password|passwd|token|authorization|api[-_]?key|credential|private[-_]?key/i;

/** Recursively replace values of secret-looking keys with "[REDACTED]". */
function redact(value) {
  if (Array.isArray(value)) return value.map(redact);
  if (value && typeof value === "object") {
    var out = {};
    Object.keys(value).forEach(function (key) {
      var v = value[key];
      var isLeaf = v === null || typeof v !== "object";
      out[key] = isLeaf && v !== null && v !== "" && SENSITIVE_KEY.test(key) ? "[REDACTED]" : redact(v);
    });
    return out;
  }
  return value;
}

/** Summarize an error response without echoing arbitrary server content. */
function describeError(status, bodyText) {
  var parsed;
  try {
    parsed = JSON.parse(bodyText);
  } catch (_e) {
    return "HTTP " + status;
  }
  var parts = [];
  ["errorCode", "code", "message"].forEach(function (field) {
    var v = parsed && parsed[field];
    if (typeof v === "string" || typeof v === "number") {
      parts.push(field + "=" + String(v).slice(0, 200));
    }
  });
  return parts.length ? "HTTP " + status + " (" + parts.join(", ") + ")" : "HTTP " + status;
}

function getBaseUrl(region) {
  if (!region || region === "global") return DEFAULT_BASE;
  var base = REGIONAL_BASES[region.toLowerCase()];
  if (!base) {
    process.stderr.write(
      "Error: Unknown region '" + region + "'. Valid: " + Object.keys(REGIONAL_BASES).join(", ") + "\n"
    );
    process.exit(1);
  }
  return base;
}

function httpRequest(urlStr, options, body) {
  return new Promise(function (resolve, reject) {
    var url = new URL(urlStr);
    if (url.protocol !== "https:" || !ALLOWED_HOSTS.has(url.hostname) || url.port) {
      reject(new Error("Refusing to send credentials to unexpected URL origin: " + url.origin));
      return;
    }
    var opts = Object.assign({}, options, {
      timeout: REQUEST_TIMEOUT_MS,
      hostname: url.hostname,
      path: url.pathname + url.search,
      port: url.port || 443,
    });

    if (body) {
      opts.headers = opts.headers || {};
      opts.headers["Content-Length"] = Buffer.byteLength(body);
    }

    var req = https.request(opts, function (res) {
      var data = "";
      res.on("data", function (chunk) { data += chunk; });
      res.on("end", function () {
        if (res.statusCode >= 200 && res.statusCode < 300) {
          try {
            resolve(data ? JSON.parse(data) : {});
          } catch (_e) {
            resolve(data);
          }
        } else {
          reject(new Error(describeError(res.statusCode, data)));
        }
      });
    });

    req.on("timeout", function () {
      req.destroy(new Error("Request timed out after " + REQUEST_TIMEOUT_MS / 1000 + "s"));
    });
    req.on("error", reject);
    if (body) req.write(body);
    req.end();
  });
}

module.exports = {
  getEnv: getEnv,
  getAuthHeader: getAuthHeader,
  getBaseUrl: getBaseUrl,
  httpRequest: httpRequest,
  redact: redact,
  CONFIG_BASE: CONFIG_BASE,
};
