import test from "node:test";
import assert from "node:assert/strict";
import { mkdtempSync, mkdirSync, writeFileSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import { join, resolve } from "node:path";
import { spawnSync } from "node:child_process";

const script = resolve(import.meta.dirname, "../scripts/resolve-local-profile.mjs");

function run(identity) {
  const home = mkdtempSync(join(tmpdir(), "sigrank-profile-"));
  try {
    if (identity !== undefined) {
      mkdirSync(join(home, ".sigrank-mcp"));
      writeFileSync(join(home, ".sigrank-mcp", "identity.json"), JSON.stringify(identity));
    }
    const result = spawnSync(process.execPath, [script], { env: { ...process.env, HOME: home }, encoding: "utf8" });
    assert.equal(result.status, 0);
    return result.stdout.trim();
  } finally {
    rmSync(home, { recursive: true, force: true });
  }
}

test("only a bound public codename leaves the local identity file", () => {
  assert.equal(run({ codename: "public_operator", operator_id: "op-1", private_key_pkcs8_b64: "SECRET" }),
    '{"status":"found","codename":"public_operator"}');
  assert.equal(run({ codename: "public_operator", operator_id: null }), '{"status":"no_identity"}');
  assert.equal(run(undefined), '{"status":"no_identity"}');
});
