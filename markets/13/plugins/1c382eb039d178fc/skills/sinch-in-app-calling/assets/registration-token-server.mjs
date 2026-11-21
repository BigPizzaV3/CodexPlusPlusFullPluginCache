// SERVER-SIDE ONLY. Never bundle this file into browser, Android, or iOS code:
// it needs the Sinch Application Secret, which must stay on your backend.
//
// Creates a Sinch In-App Calling user registration token (JWT) as described in
// https://developers.sinch.com/docs/in-app-calling/js/application-authentication
// Requires Node.js 18+. No third-party dependencies.

import { createHmac, randomUUID } from "node:crypto";

const DEFAULT_TTL_SECONDS = 600;
const MIN_TTL_SECONDS = 60;

function base64url(input) {
  return Buffer.from(input).toString("base64url");
}

// The kid date and the key-derivation date must be the current UTC date (YYYYMMDD).
export function utcDateStamp(date) {
  return date.toISOString().slice(0, 10).replaceAll("-", "");
}

export function deriveSigningKey(applicationSecret, date) {
  return createHmac("sha256", Buffer.from(applicationSecret, "base64"))
    .update(utcDateStamp(date), "utf8")
    .digest();
}

/**
 * @param {object} params
 * @param {string} params.applicationKey
 * @param {string} params.applicationSecret  Base64-encoded secret from the Sinch dashboard.
 * @param {string} params.userId             Identity your backend has already authenticated.
 * @param {number} [params.ttlSeconds=600]   JWT lifetime; Sinch requires at least 60 seconds.
 * @param {Date}   [params.now]              Override for tests.
 * @param {string} [params.nonce]            Override for tests.
 */
export function createRegistrationToken({
  applicationKey,
  applicationSecret,
  userId,
  ttlSeconds = DEFAULT_TTL_SECONDS,
  now = new Date(),
  nonce = randomUUID(),
}) {
  if (!applicationKey || !applicationSecret || !userId) {
    throw new Error("applicationKey, applicationSecret, and userId are required");
  }
  if (!Number.isInteger(ttlSeconds) || ttlSeconds < MIN_TTL_SECONDS) {
    throw new Error(`ttlSeconds must be an integer >= ${MIN_TTL_SECONDS}`);
  }

  const iat = Math.floor(now.getTime() / 1000);
  const header = { alg: "HS256", kid: `hkdfv1-${utcDateStamp(now)}` };
  const payload = {
    iss: `//rtc.sinch.com/applications/${applicationKey}`,
    sub: `//rtc.sinch.com/applications/${applicationKey}/users/${userId}`,
    iat,
    exp: iat + ttlSeconds,
    nonce,
  };

  const signingInput = `${base64url(JSON.stringify(header))}.${base64url(JSON.stringify(payload))}`;
  const signature = createHmac("sha256", deriveSigningKey(applicationSecret, now))
    .update(signingInput)
    .digest("base64url");
  return `${signingInput}.${signature}`;
}

/**
 * Example request handler for a token endpoint (framework-agnostic).
 *
 * `authenticate(req)` must verify the caller's own session (cookie, bearer token,
 * etc.) and return the Sinch user ID that session is allowed to register as, or
 * null. Never take the user ID from the request body or query string: a client
 * must not be able to obtain a token for someone else's identity.
 */
export async function handleTokenRequest(req, res, authenticate) {
  const userId = await authenticate(req);
  if (!userId) {
    res.writeHead(401, { "Content-Type": "application/json" });
    res.end(JSON.stringify({ error: "unauthenticated" }));
    return;
  }
  const token = createRegistrationToken({
    applicationKey: process.env.SINCH_APPLICATION_KEY,
    applicationSecret: process.env.SINCH_APPLICATION_SECRET,
    userId,
  });
  res.writeHead(200, { "Content-Type": "application/json", "Cache-Control": "no-store" });
  res.end(JSON.stringify({ token }));
}
