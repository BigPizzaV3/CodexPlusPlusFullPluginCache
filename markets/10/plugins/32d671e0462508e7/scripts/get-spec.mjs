import { getSpecResponse } from '../src/spec.mjs';

try {
  const [section = 'overview', query = '', category] = process.argv.slice(2);
  console.log(JSON.stringify(getSpecResponse(section, query, category ? { category } : {}), null, 2));
} catch (error) { console.error(error.message); process.exitCode = 1; }
