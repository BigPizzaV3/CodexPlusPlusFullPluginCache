import { readFile } from "node:fs/promises";
import { homedir } from "node:os";
import { join } from "node:path";

const path = join(homedir(), ".sigrank-mcp", "identity.json");

try {
  const identity = JSON.parse(await readFile(path, "utf8"));
  const codename = identity?.codename;
  const enrolled = typeof identity?.operator_id === "string" && identity.operator_id.length > 0;
  if (enrolled && typeof codename === "string" && /^[a-zA-Z0-9_-]{1,128}$/.test(codename)) {
    process.stdout.write(JSON.stringify({ status: "found", codename }) + "\n");
  } else {
    process.stdout.write('{"status":"no_identity"}\n');
  }
} catch {
  process.stdout.write('{"status":"no_identity"}\n');
}
