// Report-specific checks. The unchanged upstream checker has its MIT notice in licenses/.
// This checks text features, not truth, Korean semantics, or AI authorship.
const fs = require('node:fs');
const { validate } = require('./avoid-validate.js');

function bag(items) {
  const counts = new Map();
  for (const item of items) counts.set(item, (counts.get(item) || 0) + 1);
  return [...counts].sort(([a], [b]) => a.localeCompare(b));
}

function check(original, rewritten, protectedStrings = []) {
  if (!Array.isArray(protectedStrings) || protectedStrings.some(x => typeof x !== 'string' || !x)) {
    throw new Error('Protection file must contain an array of nonempty strings.');
  }
  const result = validate(original, rewritten, { skipResidual: true });
  const add = (code, message) => result.errors.push({ code, message });
  const urls = text => text.match(/https?:\/\/[^\s<>"'`\]\)]+/gu) || [];
  const figures = text => text.match(/[+−-]?(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?(?:%|‰)?/gu) || [];
  if (JSON.stringify(bag(urls(original))) !== JSON.stringify(bag(urls(rewritten)))) {
    add('exact-url-change', 'Detected URL strings or occurrence counts changed; no tracking-parameter normalization is allowed.');
  }
  if (JSON.stringify(bag(figures(original))) !== JSON.stringify(bag(figures(rewritten)))) {
    add('figure-change', 'Numeric text or occurrence counts changed. Check figures, signs, dates, and units manually.');
  }
  for (const value of protectedStrings) {
    if (!original.includes(value)) add('protection-not-in-original', `Protection string absent from original: ${value}`);
    if (!rewritten.includes(value)) add('protected-string-missing', `Protection string absent from rewrite: ${value}`);
  }
  result.ok = result.errors.length === 0;
  result.scope = 'Text preservation only. Manual comparison of meaning, units, conditions, uncertainty, causality, and scope is required.';
  return result;
}

module.exports = { check };
if (require.main === module) {
  try {
    const args = process.argv.slice(2);
    if (args.length < 2 || args.length > 3) throw new Error('Usage: node check-preservation.js before.md after.md [protected.json]');
    const result = check(fs.readFileSync(args[0], 'utf8'), fs.readFileSync(args[1], 'utf8'),
      args[2] ? JSON.parse(fs.readFileSync(args[2], 'utf8').replace(/^\uFEFF/, '')) : []);
    console.log(JSON.stringify(result, null, 2));
    process.exitCode = result.ok ? 0 : 1;
  } catch (error) {
    console.error(error.message);
    process.exitCode = 2;
  }
}
