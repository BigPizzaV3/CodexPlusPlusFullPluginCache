#!/usr/bin/env node
import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import path from "node:path";
import { fileURLToPath } from "node:url";
import {
  FAL_KEYCHAIN_SERVICE,
  resolveFalCredential,
  resolveKeychainAccount,
  validateFalCredentialCandidate,
} from "./fal-credential-resolver.mjs";

const args = process.argv.slice(2);
const scriptDir = path.dirname(fileURLToPath(import.meta.url));
if (args.includes("--help")) {
  console.log("Usage: node scripts/register-fal-keychain.mjs --clipboard");
  console.log("Stores the current clipboard value in macOS Keychain without writing it to files or logs.");
  process.exit(0);
}

assert.equal(process.platform, "darwin", "fal Keychain registration is supported only on macOS");
assert.ok(args.includes("--clipboard"), "Usage: node scripts/register-fal-keychain.mjs --clipboard");

const clipboard = spawnSync("/usr/bin/pbpaste", [], { encoding: "utf8", stdio: ["ignore", "pipe", "ignore"] });
assert.equal(clipboard.status, 0, "Could not read the macOS clipboard");
const checked = validateFalCredentialCandidate(clipboard.stdout);
assert.ok(checked.valid, `Clipboard does not contain a valid fal credential (${checked.reason})`);

const account = resolveKeychainAccount();
assert.ok(account, "Could not resolve the current macOS account");
const stored = spawnSync(
  "/usr/bin/expect",
  [
    path.join(scriptDir, "store-fal-keychain.exp"),
    FAL_KEYCHAIN_SERVICE,
    account,
    "MyMarketer fal API credential",
  ],
  {
    encoding: "utf8",
    stdio: ["ignore", "ignore", "ignore"],
  },
);
assert.equal(stored.status, 0, `Could not store the fal credential in macOS Keychain (status ${stored.status})`);

const verified = resolveFalCredential({ env: {}, account });
assert.ok(verified && verified.value === checked.value, "Keychain verification failed after registration");

spawnSync("/usr/bin/pbcopy", [], { input: "", encoding: "utf8", stdio: ["pipe", "ignore", "ignore"] });
console.log(`fal credential registered: ${FAL_KEYCHAIN_SERVICE}`);
console.log(`Account: ${account}`);
console.log("Verification: configured (secret value not displayed; clipboard cleared)");
