import {createHash} from "node:crypto";
import {readFile} from "node:fs/promises";

const CATALOG_ID_PATTERN = /^[A-Za-z0-9_-]{8,128}$/u;
const SHA256_PATTERN = /^[a-f0-9]{64}$/u;
const MAX_CATALOG_BYTES = 32 * 1024 * 1024;
const REQUIRED_FEATURE_DECISIONS = new Set([
  "GEOMARKETING_UI",
  "SC_SEGMENTATION",
  "SEGMENT_BY_EVENTS_PARAMETERS",
  "DATA_SOURCE_PG_USAGE",
  "TMP_SHOW_CUSTOMER_LIFECYCLE_IN_CONTACTS_ANALYTICS",
  "PRODUCT_EVENTS_VISIBILITY",
]);

export class SegmentCatalogError extends Error {
  constructor(code, message) {
    super(message);
    this.name = "SegmentCatalogError";
    this.code = code;
  }
}

function normalizedHttpUrl(value, name) {
  let parsed;
  try {
    parsed = new URL(value);
  } catch {
    throw new SegmentCatalogError("SEGMENT_CATALOG_CONFIGURATION", `${name} must be an absolute http(s) URL.`);
  }
  if (!new Set(["http:", "https:"]).has(parsed.protocol)) {
    throw new SegmentCatalogError("SEGMENT_CATALOG_CONFIGURATION", `${name} must be an absolute http(s) URL.`);
  }
  return parsed;
}

function normalizeReference(value) {
  const reference = value?.catalogRef ?? value;
  if (!reference || typeof reference !== "object" || Array.isArray(reference)) {
    throw new SegmentCatalogError(
      "SEGMENT_CATALOG_REFERENCE_INVALID",
      "Catalog JSON must contain the catalogRef returned by list_segment_definitions(for_sdk=true).",
    );
  }
  const catalogId = reference.catalogId;
  const checksum = typeof reference.sha256 === "string" ? reference.sha256.toLowerCase() : reference.sha256;
  const expiresAt = reference.expiresAt;
  const downloadUrl = reference.downloadUrl;
  if (typeof catalogId !== "string" || !CATALOG_ID_PATTERN.test(catalogId)) {
    throw new SegmentCatalogError("SEGMENT_CATALOG_REFERENCE_INVALID", "catalogRef.catalogId is invalid.");
  }
  if (typeof checksum !== "string" || !SHA256_PATTERN.test(checksum)) {
    throw new SegmentCatalogError("SEGMENT_CATALOG_REFERENCE_INVALID", "catalogRef.sha256 is invalid.");
  }
  if (typeof expiresAt !== "string" || !Number.isFinite(Date.parse(expiresAt))) {
    throw new SegmentCatalogError("SEGMENT_CATALOG_REFERENCE_INVALID", "catalogRef.expiresAt is invalid.");
  }
  if (typeof downloadUrl !== "string") {
    throw new SegmentCatalogError("SEGMENT_CATALOG_REFERENCE_INVALID", "catalogRef.downloadUrl is missing.");
  }
  normalizedHttpUrl(downloadUrl, "catalogRef.downloadUrl");
  if (
    reference.bytes !== undefined
    && (!Number.isSafeInteger(reference.bytes) || reference.bytes < 1 || reference.bytes > MAX_CATALOG_BYTES)
  ) {
    throw new SegmentCatalogError("SEGMENT_CATALOG_REFERENCE_INVALID", "catalogRef.bytes is invalid.");
  }
  return {...reference, catalogId, sha256: checksum, expiresAt, downloadUrl};
}

function digest(bytes) {
  return createHash("sha256").update(bytes).digest("hex");
}

function validateUiContext(value) {
  if (!value || typeof value !== "object" || Array.isArray(value)) {
    throw new SegmentCatalogError(
      "SEGMENT_CATALOG_UI_CONTEXT_INVALID",
      "Segment definition catalog does not contain an authoritative uiContext object.",
    );
  }
  if (typeof value.timeZone !== "string" || value.timeZone.trim().length === 0) {
    throw new SegmentCatalogError("SEGMENT_CATALOG_UI_CONTEXT_INVALID", "uiContext.timeZone is missing.");
  }
  if (!new Set(["DYNAMIC", "PARAMETRIC"]).has(value.groupType)) {
    throw new SegmentCatalogError("SEGMENT_CATALOG_UI_CONTEXT_INVALID", "uiContext.groupType is invalid.");
  }
  if (!value.enabledFeatures || typeof value.enabledFeatures !== "object" || Array.isArray(value.enabledFeatures)) {
    throw new SegmentCatalogError("SEGMENT_CATALOG_UI_CONTEXT_INVALID", "uiContext.enabledFeatures is missing.");
  }
  for (const name of REQUIRED_FEATURE_DECISIONS) {
    if (typeof value.enabledFeatures[name] !== "boolean") {
      throw new SegmentCatalogError(
        "SEGMENT_CATALOG_UI_CONTEXT_INVALID",
        `uiContext.enabledFeatures.${name} is not a resolved boolean decision.`,
      );
    }
  }
  if (value.requireResolvedFeatures !== true) {
    throw new SegmentCatalogError(
      "SEGMENT_CATALOG_UI_CONTEXT_INVALID",
      "uiContext.requireResolvedFeatures must be true for trusted catalogs.",
    );
  }
  if (!Number.isSafeInteger(value.scEventDateValidPeriodDays) || value.scEventDateValidPeriodDays < 0) {
    throw new SegmentCatalogError(
      "SEGMENT_CATALOG_UI_CONTEXT_INVALID",
      "uiContext.scEventDateValidPeriodDays must be a non-negative integer.",
    );
  }
  if (
    value.mobilePushApplicationIds !== undefined
    && (!Array.isArray(value.mobilePushApplicationIds)
      || value.mobilePushApplicationIds.some((id) => typeof id !== "string" && typeof id !== "number"))
  ) {
    throw new SegmentCatalogError(
      "SEGMENT_CATALOG_UI_CONTEXT_INVALID",
      "uiContext.mobilePushApplicationIds must contain only string or number IDs.",
    );
  }
  return value;
}

function validatePayload(bytes, reference, now) {
  if (bytes.byteLength > MAX_CATALOG_BYTES) {
    throw new SegmentCatalogError("SEGMENT_CATALOG_TOO_LARGE", "Segment definition catalog exceeds 32 MiB.");
  }
  if (reference.bytes !== undefined && bytes.byteLength !== reference.bytes) {
    throw new SegmentCatalogError(
      "SEGMENT_CATALOG_SIZE_MISMATCH",
      "Downloaded segment definition catalog size does not match catalogRef.",
    );
  }
  if (digest(bytes) !== reference.sha256) {
    throw new SegmentCatalogError(
      "SEGMENT_CATALOG_CHECKSUM_MISMATCH",
      "Downloaded segment definition catalog checksum does not match catalogRef.",
    );
  }

  let payload;
  try {
    payload = JSON.parse(bytes.toString("utf8"));
  } catch {
    throw new SegmentCatalogError("SEGMENT_CATALOG_INVALID", "Segment definition catalog is not valid JSON.");
  }
  if (!payload || typeof payload !== "object" || Array.isArray(payload)) {
    throw new SegmentCatalogError("SEGMENT_CATALOG_INVALID", "Segment definition catalog must be an object.");
  }
  if (payload.catalogVersion !== 2 || payload.catalogId !== reference.catalogId) {
    throw new SegmentCatalogError(
      "SEGMENT_CATALOG_MISMATCH",
      "Segment definition catalog identity does not match catalogRef.",
    );
  }
  if (payload.expiresAt !== reference.expiresAt || Date.parse(payload.expiresAt) <= now.getTime()) {
    throw new SegmentCatalogError("SEGMENT_CATALOG_EXPIRED", "Segment definition catalog has expired.");
  }
  if (!Array.isArray(payload.definitions)) {
    throw new SegmentCatalogError(
      "SEGMENT_CATALOG_INVALID",
      "Segment definition catalog does not contain a definitions array.",
    );
  }
  validateUiContext(payload.uiContext);
  return payload;
}


export async function loadCatalog(referenceValue, catalogFile, now = new Date()) {
  const reference = normalizeReference(referenceValue);
  const bytes = await readFile(catalogFile);
  return validatePayload(bytes, reference, now);
}
