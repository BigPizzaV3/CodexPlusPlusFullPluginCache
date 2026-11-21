#!/usr/bin/env node
/*
 * EXECUTION TOOL — not a schema reference.
 * Run this script as-is to PERFORM this task when you do not need to write
 * application code; side-effect rules still apply (billable/destructive calls
 * need explicit user approval). Do NOT copy its payload literals or logic into
 * a new codebase as if they were the API spec — for payload shape, load the
 * canonical developers.sinch.com docs linked from ../SKILL.md instead.
 *
 * Credentials are read only from environment variables so that secrets never
 * appear in process arguments, shell history, or tool transcripts.
 */

const fs = require('fs');

const BASE_URL = 'https://numbers.api.sinch.com/v1';
const ALLOWED_HOST = 'numbers.api.sinch.com';

const DEFAULTS = {
    pageSize: 100,
    maxPages: 50,
    maxResults: 5000,
    requestTimeoutMs: 15000,
    overallTimeoutMs: 120000,
};

const DIAGNOSTIC_FIELDS = ['code', 'status', 'message'];

function sanitizeError(status, body) {
    let parsed;
    try {
        parsed = JSON.parse(body);
    } catch {
        return `HTTP ${status}`;
    }
    const err = parsed && typeof parsed === 'object' && parsed.error && typeof parsed.error === 'object'
        ? parsed.error
        : parsed;
    const parts = [];
    for (const field of DIAGNOSTIC_FIELDS) {
        const value = err && err[field];
        if (typeof value === 'string' || typeof value === 'number') {
            parts.push(`${field}=${String(value).slice(0, 200)}`);
        }
    }
    return parts.length ? `HTTP ${status} (${parts.join(', ')})` : `HTTP ${status}`;
}

function buildUrl(projectId, { pageSize, regionCode, type, pageToken }) {
    const url = new URL(`${BASE_URL}/projects/${encodeURIComponent(projectId)}/activeNumbers`);
    url.searchParams.set('pageSize', String(pageSize));
    if (regionCode) url.searchParams.set('regionCode', regionCode);
    if (type) url.searchParams.set('type', type);
    if (pageToken) url.searchParams.set('pageToken', pageToken);
    if (url.protocol !== 'https:' || url.hostname !== ALLOWED_HOST) {
        throw new Error('Refusing to send credentials to an unexpected host');
    }
    return url;
}

/**
 * Fetch active numbers with bounded work. Returns { numbers, complete, reason }.
 * `complete` is false whenever retrieval stopped before the API reported the last page.
 */
async function getNumbers(projectId, keyId, keySecret, options = {}) {
    const opts = { ...DEFAULTS, ...options };
    const credentials = Buffer.from(`${keyId}:${keySecret}`).toString('base64');
    const deadline = Date.now() + opts.overallTimeoutMs;
    const seenTokens = new Set();
    const numbers = [];
    let pageToken = null;
    let pages = 0;

    while (true) {
        if (pages >= opts.maxPages) {
            return { numbers, complete: false, reason: `stopped after --max-pages ${opts.maxPages}` };
        }
        const remaining = deadline - Date.now();
        if (remaining <= 0) {
            return { numbers, complete: false, reason: 'overall timeout reached' };
        }

        const url = buildUrl(projectId, { ...opts, pageToken });
        const response = await fetch(url, {
            headers: { Authorization: `Basic ${credentials}` },
            redirect: 'error',
            signal: AbortSignal.timeout(Math.min(opts.requestTimeoutMs, remaining)),
        });

        if (!response.ok) {
            const body = await response.text().catch(() => '');
            throw new Error(sanitizeError(response.status, body));
        }

        const data = await response.json();
        pages++;

        const page = data && data.activeNumbers;
        if (page !== undefined && !Array.isArray(page)) {
            throw new Error('Unexpected response: activeNumbers is not an array');
        }
        const next = data && data.nextPageToken;
        if (next !== undefined && next !== null && typeof next !== 'string') {
            throw new Error('Unexpected response: nextPageToken is not a string');
        }

        for (const item of page || []) {
            if (numbers.length >= opts.maxResults) {
                return { numbers, complete: false, reason: `stopped at --max-results ${opts.maxResults}` };
            }
            numbers.push(item);
        }

        if (!next) {
            return { numbers, complete: true, reason: null };
        }
        if (seenTokens.has(next)) {
            return { numbers, complete: false, reason: 'API returned a repeated nextPageToken' };
        }
        seenTokens.add(next);
        pageToken = next;
    }
}

function parsePositiveInt(name, value) {
    const n = Number.parseInt(value, 10);
    if (!Number.isFinite(n) || n <= 0) {
        console.error(`Error: ${name} must be a positive integer`);
        process.exit(1);
    }
    return n;
}

function printHelp() {
    console.log(`
Usage: node get_numbers.cjs [options]

Options:
  --page-size <number>    Page size (default: ${DEFAULTS.pageSize})
  --max-pages <number>    Stop after this many pages (default: ${DEFAULTS.maxPages})
  --max-results <number>  Stop after this many numbers (default: ${DEFAULTS.maxResults})
  --timeout <seconds>     Overall time limit (default: ${DEFAULTS.overallTimeoutMs / 1000})
  --region <code>         Filter by region code (e.g. US, GB, SE)
  --type <type>           Filter by number type (MOBILE, LOCAL, TOLL_FREE)
  --output <file>         Write full records to a JSON file (created with mode 0600)
  --force                 Allow --output to overwrite an existing file
  --help, -h              Show this help message

Required environment variables:
  SINCH_PROJECT_ID        Sinch project ID
  SINCH_KEY_ID            Sinch API key ID
  SINCH_KEY_SECRET        Sinch API key secret

Credentials are accepted only from the environment. Load them from a secrets
manager or an untracked env file; do not type the secret on the command line.

Without --output, only a summary (phone number, type, region) is printed.

Examples:
  node get_numbers.cjs --region US --type LOCAL
  node get_numbers.cjs --output numbers.json
`);
}

function parseArgs(argv) {
    const options = {
        pageSize: DEFAULTS.pageSize,
        maxPages: DEFAULTS.maxPages,
        maxResults: DEFAULTS.maxResults,
        overallTimeoutMs: DEFAULTS.overallTimeoutMs,
        regionCode: null,
        type: null,
        output: null,
        force: false,
    };

    for (let i = 0; i < argv.length; i++) {
        switch (argv[i]) {
            case '--page-size':
                options.pageSize = parsePositiveInt('--page-size', argv[++i]);
                break;
            case '--max-pages':
                options.maxPages = parsePositiveInt('--max-pages', argv[++i]);
                break;
            case '--max-results':
                options.maxResults = parsePositiveInt('--max-results', argv[++i]);
                break;
            case '--timeout':
                options.overallTimeoutMs = parsePositiveInt('--timeout', argv[++i]) * 1000;
                break;
            case '--region':
                options.regionCode = argv[++i];
                break;
            case '--type':
                options.type = argv[++i];
                break;
            case '--output':
                options.output = argv[++i];
                break;
            case '--force':
                options.force = true;
                break;
            case '--help':
            case '-h':
                printHelp();
                process.exit(0);
                break;
            default:
                console.error(`Error: unknown option ${argv[i]} (use --help)`);
                process.exit(1);
        }
    }

    return options;
}

function writeOutput(file, numbers, force) {
    const flags = force ? 'w' : 'wx';
    try {
        fs.writeFileSync(file, JSON.stringify(numbers, null, 2), { mode: 0o600, flag: flags });
    } catch (error) {
        if (error.code === 'EEXIST') {
            throw new Error(`${file} already exists; pass --force to overwrite`);
        }
        throw error;
    }
    if (force) fs.chmodSync(file, 0o600);
}

async function main() {
    const options = parseArgs(process.argv.slice(2));
    const projectId = process.env.SINCH_PROJECT_ID;
    const keyId = process.env.SINCH_KEY_ID;
    const keySecret = process.env.SINCH_KEY_SECRET;

    if (!projectId || !keyId || !keySecret) {
        console.error('Error: set SINCH_PROJECT_ID, SINCH_KEY_ID, and SINCH_KEY_SECRET in the environment');
        process.exit(1);
    }

    const { numbers, complete, reason } = await getNumbers(projectId, keyId, keySecret, options);

    if (options.output) {
        writeOutput(options.output, numbers, options.force);
        console.log(`Saved ${numbers.length} numbers to ${options.output}`);
    } else {
        console.log(`Active numbers (${numbers.length}):`);
        for (const n of numbers) {
            console.log(`  ${n.phoneNumber}  ${n.type || ''}  ${n.regionCode || ''}`);
        }
    }

    if (!complete) {
        console.error(`WARNING: results are incomplete — ${reason}`);
        process.exit(2);
    }
}

if (require.main === module) {
    main().catch(error => {
        const message = error && error.name === 'TimeoutError' ? 'request timed out' : error.message;
        console.error(`Error: ${message}`);
        process.exit(1);
    });
}

module.exports = { getNumbers, sanitizeError };
