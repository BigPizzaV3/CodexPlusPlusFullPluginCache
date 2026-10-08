import assert from "node:assert/strict";
import { readdir, readFile } from "node:fs/promises";
import path from "node:path";
import test from "node:test";

const root = path.resolve("media2url-chatgpt-plugin");
const skillNames = [
  "publish-this",
  "update-live-version",
  "get-right-link",
  "developer-asset-pack",
  "temporary-secure-share",
  "link-doctor",
  "media-library-reuse",
  "batch-publish",
] as const;
const requiredSections = [
  "## Purpose",
  "## Trigger examples",
  "## Do not trigger",
  "## Allowed Media2URL App actions",
  "## Result interpretation",
  "## Missing authorization",
  "## Plan or quota restriction",
  "## Partial failure",
  "## Privacy and destructive actions",
  "## Natural-language examples",
];

test("plugin manifest declares Media2URL and all eight local skills", async () => {
  const manifest = JSON.parse(await readFile(path.join(root, ".codex-plugin/plugin.json"), "utf8"));
  assert.equal(manifest.name, "media2url-chatgpt-plugin");
  assert.equal(manifest.interface.displayName, "Media2URL");
  assert.match(manifest.description, /usable Media2URL links/i);
  assert.equal(manifest.interface.websiteURL, "https://media2url.com/");
  assert.equal(manifest.interface.privacyPolicyURL, "https://media2url.com/privacy");
  assert.equal(manifest.interface.termsOfServiceURL, "https://media2url.com/terms");
  assert.match(manifest.interface.longDescription, /90 uploads per month/i);
  assert.match(manifest.interface.longDescription, /connected Media2URL account/i);
  assert.doesNotMatch(manifest.interface.longDescription, /https?:\/\//i);
  assert.doesNotMatch(manifest.interface.longDescription, /\|/);
  assert.equal(manifest.skills, "./skills/");
});

test("submission listing exposes the real website, trust, and tool URLs", async () => {
  const listing = JSON.parse(await readFile(path.join(root, "submission/listing.json"), "utf8"));
  const expected = [
    "https://media2url.com/", "https://media2url.com/pricing", "https://media2url.com/privacy",
    "https://media2url.com/terms", "https://media2url.com/contact", "https://media2url.com/report-abuse",
    "https://media2url.com/security", "https://media2url.com/tools", "https://media2url.com/tools/link-doctor",
    "https://media2url.com/image-to-link", "https://media2url.com/video-to-link", "https://media2url.com/gif-to-link",
    "https://media2url.com/pdf-to-link", "https://media2url.com/audio-to-link", "https://media2url.com/file-to-link",
    "https://media2url.com/html-to-url", "https://media2url.com/features/media-library",
    "https://media2url.com/features/expiring-links", "https://media2url.com/features/private-links",
    "https://media2url.com/features/custom-domains", "https://media2url.com/features/media-processing",
    "https://media2url.com/features/pdf-workspace",
  ];
  const serialized = JSON.stringify(listing);
  for (const url of expected) assert.ok(serialized.includes(url), `missing ${url}`);
  for (const url of serialized.match(/https?:\/\/[^"\\]+/g) ?? []) assert.match(url, /^https:\/\/media2url\.com(?:\/|$)/);
});

test("every skill contains the complete safety and workflow contract", async () => {
  for (const name of skillNames) {
    const content = await readFile(path.join(root, "skills", name, "SKILL.md"), "utf8");
    for (const section of requiredSections) assert.ok(content.includes(section), `${name}: missing ${section}`);
    assert.match(content, /account connection|connected Media2URL App/i);
    assert.match(content, /must not|never/i);
  }
});

test("plugin package has no legacy manifest or unassigned App configuration", async () => {
  const entries = await readdir(root, { recursive: true });
  assert.equal(entries.some((entry) => entry === "ai-plugin.json"), false);
  assert.equal(entries.some((entry) => entry === ".app.json"), false);
  const allText = await Promise.all(entries.filter((entry) => entry.endsWith(".md") || entry.endsWith(".json")).map((entry) => readFile(path.join(root, entry), "utf8")));
  assert.equal(allText.some((text) => /app[_-]?id\s*[:=]\s*["'](?:TODO|TBD|CHANGE_ME|your-app-id)/i.test(text)), false);
});

test("README and listing visibly include the canonical trust links", async () => {
  const [readme, listing] = await Promise.all([
    readFile(path.join(root, "README.md"), "utf8"),
    readFile(path.join(root, "submission/listing.md"), "utf8"),
  ]);
  for (const url of ["https://media2url.com/", "https://media2url.com/privacy", "https://media2url.com/terms", "https://media2url.com/contact", "https://media2url.com/report-abuse"]) {
    assert.ok(readme.includes(url), `README missing ${url}`);
    assert.ok(listing.includes(url), `listing missing ${url}`);
  }
});

test("publishing skills preserve the key URL and content distinctions", async () => {
  const publish = await readFile(path.join(root, "skills/publish-this/SKILL.md"), "utf8");
  const update = await readFile(path.join(root, "skills/update-live-version/SKILL.md"), "utf8");
  const links = await readFile(path.join(root, "skills/get-right-link/SKILL.md"), "utf8");
  const pack = await readFile(path.join(root, "skills/developer-asset-pack/SKILL.md"), "utf8");
  assert.match(publish, /actual content|bytes/i);
  assert.match(publish, /HTML.*live|live.*HTML/i);
  assert.match(update, /preserv(e|ing).*URL|same.*URL/i);
  assert.match(update, /new.*asset|new.*URL/i);
  assert.match(links, /direct.*URL/i);
  assert.match(links, /share.*page/i);
  assert.match(pack, /deterministic|input order|ordering/i);
  assert.match(pack, /Markdown|HTML|CSS|JSON/i);
});

test("management skills enforce supported controls and safe partial results", async () => {
  const temporary = await readFile(path.join(root, "skills/temporary-secure-share/SKILL.md"), "utf8");
  const doctor = await readFile(path.join(root, "skills/link-doctor/SKILL.md"), "utf8");
  const library = await readFile(path.join(root, "skills/media-library-reuse/SKILL.md"), "utf8");
  const batch = await readFile(path.join(root, "skills/batch-publish/SKILL.md"), "utf8");
  assert.match(temporary, /actual.*expir|expiration/i);
  assert.match(temporary, /unsupported|available/i);
  assert.match(doctor, /redirect|content.?type|HTML/i);
  assert.match(doctor, /guess|safe/i);
  assert.match(library, /private|workspace/i);
  assert.match(library, /narrow|small|limit/i);
  assert.match(batch, /partial/i);
  assert.match(batch, /order|mapping|filename/i);
});

test("README and security docs explain app dependency and safety boundaries", async () => {
  const [readme, security, matrix] = await Promise.all([
    readFile(path.join(root, "README.md"), "utf8"),
    readFile(path.join(root, "SECURITY.md"), "utf8"),
    readFile(path.join(root, "submission/test-matrix.md"), "utf8"),
  ]);
  assert.match(readme, /\.app\.json/);
  assert.match(readme, /real Media2URL App ID/i);
  assert.match(readme, /ChatGPT|Codex/i);
  assert.match(security, /server.?side|App.*authorization|entitlement/i);
  assert.match(security, /OAuth token|presigned|storage key/i);
  assert.match(matrix, /generated HTML/i);
  assert.match(matrix, /partial failure/i);
  assert.match(matrix, /missing authentication|authorization/i);
  assert.match(matrix, /delete.*confirmation/i);
});

test("plugin materials make the account-only Free allowance explicit", async () => {
  const [manifestText, listingText, readme, security, matrix] = await Promise.all([
    readFile(path.join(root, ".codex-plugin/plugin.json"), "utf8"),
    readFile(path.join(root, "submission/listing.json"), "utf8"),
    readFile(path.join(root, "README.md"), "utf8"),
    readFile(path.join(root, "SECURITY.md"), "utf8"),
    readFile(path.join(root, "submission/test-matrix.md"), "utf8"),
  ]);

  assert.match(manifestText, /account.*required|sign in/i);
  assert.match(manifestText, /90 uploads per month|3 per day/i);
  assert.match(listingText, /account.*required|sign in/i);
  assert.match(listingText, /90 uploads per month|3 per day/i);
  assert.match(readme, /90 uploads per month/i);
  assert.match(readme, /3 per day/i);
  assert.match(security, /anonymous.*upload|account.*required/i);
  assert.match(matrix, /anonymous.*upload/i);
  assert.match(matrix, /90 uploads per month|3 per day/i);

  for (const name of skillNames) {
    const content = await readFile(path.join(root, "skills", name, "SKILL.md"), "utf8");
    assert.match(content, /free account|free tier/i, `${name}: missing Free-tier rule`);
    assert.match(content, /paid plan|premium/i, `${name}: missing paid-tier rule`);
  }
});
