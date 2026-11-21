export function options(argv, allowed) {
  const result = {};
  for (let i = 0; i < argv.length; i += 2) {
    const key = argv[i].replace(/^--/, '');
    if (!argv[i].startsWith('--') || !allowed.includes(key) || result[key] !== undefined || !argv[i + 1] || argv[i + 1].startsWith('--')) throw new Error(`Unknown, duplicate or incomplete option: ${argv[i]}`);
    result[key] = argv[i + 1];
  }
  return result;
}
export function required(args, key) {
  if (!args[key]) throw new Error(`Missing --${key}`);
  return args[key];
}
