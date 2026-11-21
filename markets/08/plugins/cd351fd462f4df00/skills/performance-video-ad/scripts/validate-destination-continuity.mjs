#!/usr/bin/env node
import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const nonEmpty = (value) => typeof value === "string" && value.trim().length > 0;

export function validateDestinationContinuity(contract, { now = new Date(), maxAgeDays = 30 } = {}) {
  assert.equal(contract.schemaVersion, 1, "unsupported schemaVersion");
  assert.equal(contract.destinationContractVersion, 1, "unsupported destinationContractVersion");
  assert.ok(nonEmpty(contract.jobId), "jobId missing");
  assert.ok(nonEmpty(contract.destinationId), "destinationId missing");
  const url = new URL(contract.url);
  assert.equal(url.protocol, "https:", "destination URL must use HTTPS");
  assert.ok(nonEmpty(contract.pageTitle) && contract.pageTitle !== "REPLACE_ME", "pageTitle must come from the reviewed destination");
  assert.ok(nonEmpty(contract.audience) && contract.audience !== "REPLACE_ME", "destination audience missing");
  assert.ok(nonEmpty(contract.entryPromise) && contract.entryPromise !== "REPLACE_ME", "destination entryPromise missing");

  const checkedAt = new Date(contract.checkedAt);
  assert.equal(Number.isNaN(checkedAt.getTime()), false, "checkedAt must be a valid timestamp");
  const ageDays = (now.getTime() - checkedAt.getTime()) / 86_400_000;
  assert.ok(ageDays >= -1, "checkedAt cannot be materially in the future");
  if (contract.status === "DESTINATION_REVIEWED") {
    assert.ok(ageDays <= maxAgeDays, `destination review is stale (${ageDays.toFixed(1)} days; max ${maxAgeDays})`);
  }

  const free = contract.freeConsult;
  assert.ok(free && Number.isFinite(free.durationMinutes) && free.durationMinutes > 0, "freeConsult.durationMinutes missing");
  assert.ok(nonEmpty(free.outcome) && free.outcome !== "REPLACE_ME", "free consult outcome missing");
  assert.ok(Array.isArray(free.ctaCopies) && free.ctaCopies.length > 0 && free.ctaCopies.every(nonEmpty), "destination CTA copy missing");
  assert.ok(nonEmpty(free.semanticAction), "free consult semantic action missing");

  const paid = contract.paidOffer;
  assert.ok(paid && nonEmpty(paid.name) && nonEmpty(paid.outcome), "paid offer name and outcome are required");
  assert.ok(Array.isArray(paid.included) && paid.included.length > 0, "paid offer included scope missing");
  assert.ok(Array.isArray(paid.excluded) && paid.excluded.length > 0, "paid offer excluded scope missing");
  assert.notEqual(free.outcome.trim(), paid.outcome.trim(), "free and paid outcomes must not collapse into the same promise");

  assert.ok(nonEmpty(contract.proofBoundary), "proofBoundary missing");
  assert.ok(Array.isArray(contract.trustSignals) && contract.trustSignals.length > 0, "trustSignals missing");
  assert.ok(contract.sourceEvidence?.type && contract.sourceEvidence?.ref, "sourceEvidence requires type and ref");

  const continuity = contract.adContinuity;
  assert.ok(continuity && nonEmpty(continuity.adCtaCopy), "ad CTA copy missing");
  assert.equal(continuity.adCtaSemanticAction, continuity.destinationCtaSemanticAction, "ad CTA and destination CTA must request the same action");
  assert.equal(continuity.adCtaSemanticAction, free.semanticAction, "ad CTA must lead to the destination's free-consult action");
  assert.equal(continuity.promiseRelation, "equal_or_narrower", "ad promise must be equal to or narrower than the destination promise");
  assert.ok(Array.isArray(continuity.adClaims) && continuity.adClaims.length > 0, "adClaims missing");
  assert.deepEqual(continuity.unsupportedClaims, [], "unsupported ad claims must be resolved before review");
  assert.equal(continuity.freePaidBoundaryPreserved, true, "ad must preserve the free-versus-paid offer boundary");

  return { destinationId: contract.destinationId, ageDays, ctaSemanticAction: free.semanticAction };
}

const isMain = process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url);
if (isMain) {
  const file = process.argv[2] ? path.resolve(process.argv[2]) : null;
  assert.ok(file, "Usage: node scripts/validate-destination-continuity.mjs <destination-contract.json>");
  const contract = JSON.parse(await readFile(file, "utf8"));
  const result = validateDestinationContinuity(contract);
  console.log(`Destination continuity: PASS (${result.destinationId} / ${result.ctaSemanticAction} / age=${result.ageDays.toFixed(1)}d)`);
}
