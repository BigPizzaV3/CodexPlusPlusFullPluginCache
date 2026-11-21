#!/usr/bin/env node
'use strict';

const fs = require('node:fs/promises');
const path = require('node:path');
const { randomUUID } = require('node:crypto');



const MAX_CHUNK = 50 * 1024 * 1024;

const mimes = {
    jpg: 'image/jpeg', jpeg: 'image/jpeg', png: 'image/png', webp: 'image/webp', gif: 'image/gif',
    svg: 'image/svg+xml', avif: 'image/avif', pdf: 'application/pdf', txt: 'text/plain', csv: 'text/csv',
    json: 'application/json', zip: 'application/zip', mp4: 'video/mp4', mov: 'video/quicktime',
    webm: 'video/webm', mp3: 'audio/mpeg', wav: 'audio/wav',
    doc: 'application/msword', docx: 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    xlsx: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    pptx: 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
};



const writeJson = async (filename, value, exclusive = false) => {
    const text = JSON.stringify(value, null, 2) + '\n';

    if (exclusive) {
        const handle = await fs.open(filename, 'wx', 0o600);

        try {
            await handle.writeFile(text);
            await handle.sync();
        } finally {
            await handle.close();
        }

        return;
    }

    const temporary = filename + '.' + randomUUID() + '.tmp';
    const handle = await fs.open(temporary, 'wx', 0o600);

    try {
        await handle.writeFile(text);
        await handle.sync();
    } finally {
        await handle.close();
    }

    await fs.rename(temporary, filename);
};

const inspect = async (source, recursive = false) => {
    const root = path.resolve(source);
    const stat = await fs.lstat(root);
    const files = [];
    const skipped = [];

    const visit = async (filename, relativePath) => {
        const info = await fs.lstat(filename);

        if (info.isSymbolicLink()) {
            skipped.push({ relativePath, reason: 'symbolic-link' });
            return;
        }

        if (info.isDirectory()) {
            if (filename !== root && !recursive) {
                skipped.push({ relativePath, reason: 'subfolder-not-requested' });
                return;
            }

            for (const entry of (await fs.readdir(filename)).sort()) {
                await visit(path.join(filename, entry), path.join(relativePath, entry));
            }

            return;
        }

        if (!info.isFile()) {
            skipped.push({ relativePath, reason: 'not-a-regular-file' });
            return;
        }

        // Existing PHP chunk assembly cannot process an empty chunk. Report it before any upload.
        if (info.size === 0) {
            skipped.push({ relativePath, reason: 'empty-file-not-supported-by-storage' });
            return;
        }

        files.push({
            path: filename,
            relativePath,
            name: path.basename(filename),
            size: info.size,
            mime: mimes[path.extname(filename).slice(1).toLowerCase()] || 'application/octet-stream',
            mtimeMs: info.mtimeMs,
        });
    };

    if (stat.isSymbolicLink()) throw new Error('Choose the actual source, not a symbolic link');
    await visit(root, stat.isDirectory() ? '' : path.basename(root));

    return { source: root, recursive, files, skipped, count: files.length, totalBytes: files.reduce((sum, file) => sum + file.size, 0) };
};

const checkedUrl = (value, allowLocal, origin) => {
    const url = new URL(value);
    const local = ['localhost', '127.0.0.1', '[::1]'].includes(url.hostname);

    if (url.username || url.password || url.hash || (url.protocol !== 'https:' && !(allowLocal && local && url.protocol === 'http:'))) {
        throw new Error('Expected a signed HTTPS URL (explicit --allow-local permits loopback HTTP)');
    }

    if (origin && url.origin !== origin) throw new Error('Next chunk URL changed origin');

    return url;
};

const jsonResponse = async response => {
    if (!response.ok) throw new Error('HTTP_' + response.status);

    const text = await response.text();
    if (text.length > 65536) throw new Error('Unexpectedly large upload response');
    const value = JSON.parse(text);
    if (value.error || value.result === false) throw new Error('Server rejected the upload operation');

    return value.data ?? value;
};

const sendJson = async (url, token, body) => jsonResponse(await fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', 'X-File-Upload-Token': token },
    body: JSON.stringify(body),
    redirect: 'error',
    signal: AbortSignal.timeout(120000),
}));

const sendChunk = async (url, file, offset, length) => {
    const handle = await fs.open(file.path, 'r');
    const buffer = Buffer.alloc(length);

    try {
        const info = await handle.stat();
        if (info.size !== file.size || info.mtimeMs !== file.mtimeMs) throw new Error('Local file changed');
        let read = 0;

        while (read < length) {
            const result = await handle.read(buffer, read, length - read, offset + read);
            if (!result.bytesRead) throw new Error('Local file ended unexpectedly');
            read += result.bytesRead;
        }
    } finally {
        await handle.close();
    }

    const form = new FormData();
    form.set('upload_file', new Blob([buffer], { type: file.mime }), file.name);
    form.set('file_size', String(file.size));
    form.set('mime', file.mime);

    return jsonResponse(await fetch(url, {
        method: 'POST', body: form, redirect: 'error', signal: AbortSignal.timeout(1800000),
    }));
};

const bind = (files, sessions) => {
    if (!Array.isArray(files) || !Array.isArray(sessions) || !files.length || files.length !== sessions.length) {
        throw new Error('Provide equal ordered arrays of inspected files and upload sessions');
    }

    const ids = new Set();
    const entries = files.map((file, index) => {
        const session = sessions[index];

        if (ids.has(session.transferId) || file.size !== session.size || file.name !== session.name || file.mime !== session.mime
            || !Number.isFinite(file.mtimeMs) || !path.isAbsolute(file.path) || file.size < 1
            || !Number.isSafeInteger(session.chunkBytes) || session.chunkBytes < 1 || session.chunkBytes > MAX_CHUNK
            || !['AWAITING_UPLOAD', 'READY'].includes(session.status)) {
            throw new Error('File/session mismatch or existing upload in progress; preserve its original journal');
        }

        ids.add(session.transferId);

        return { file, session, offset: 0, nextUrl: session.uploadUrl, inFlight: false, receipt: null, result: session.file, status: session.status };
    });

    return { version: 1, entries };
};

const run = async (journalPath, options = {}) => {
    const { allowLocal = false, chunk = sendChunk, complete = sendJson, progress = () => {} } = options;
    const lockPath = journalPath + '.lock';
    const lock = await fs.open(lockPath, 'wx', 0o600).catch(() => { throw new Error('Uploader already running or interrupted: inspect the .lock before resuming'); });
    await lock.writeFile(String(process.pid));

    try {
        const job = JSON.parse(await fs.readFile(journalPath, 'utf8'));
        if (job.version !== 1 || !Array.isArray(job.entries)) throw new Error('Invalid upload journal');

        for (const entry of job.entries) {
            if (entry.status === 'READY') continue;
            const { file, session } = entry;

            try {
                const completionUrl = checkedUrl(session.completionUrl, allowLocal);
                if (entry.inFlight || entry.status === 'UNKNOWN') {
                    entry.status = 'UNKNOWN';
                    entry.error = 'Chunk outcome unknown; do not retry this file blindly';
                    await writeJson(journalPath, job);
                    await complete(completionUrl, session.completionToken, { action: 'uncertain' }).catch(() => {});
                    continue;
                }

                if (!entry.receipt) {
                    const info = await fs.lstat(file.path);
                    if (!info.isFile() || info.isSymbolicLink() || info.size !== file.size || info.mtimeMs !== file.mtimeMs) {
                        throw new Error('Local file changed since inspection');
                    }

                    if (Date.now() / 1000 >= session.uploadExpiresAt) throw new Error('Upload URL expired; do not renew an incomplete file blindly');
                    const origin = checkedUrl(session.uploadUrl, allowLocal).origin;
                    const started = await complete(completionUrl, session.completionToken, { action: 'started' });
                    if (started.status === 'READY') {
                        entry.status = 'READY';
                        entry.result = started.file;
                        await writeJson(journalPath, job);
                        continue;
                    }
                    if (started.status !== 'TRANSFERRING') throw new Error('Server session cannot be resumed');

                    while (entry.offset < file.size) {
                        const url = checkedUrl(entry.nextUrl, allowLocal, origin);
                        const length = Math.min(session.chunkBytes, file.size - entry.offset);
                        entry.inFlight = true;
                        entry.status = 'TRANSFERRING';
                        await writeJson(journalPath, job);
                        const result = await chunk(url, file, entry.offset, length);
                        const nextOffset = entry.offset + length;

                        if (nextOffset < file.size) {
                            checkedUrl(result.next_url, allowLocal, origin);
                            entry.nextUrl = result.next_url;
                        } else {
                            if (result.next_url || !result.path || !result.server) throw new Error('Final storage receipt missing');
                            entry.receipt = result;
                            entry.nextUrl = null;
                        }

                        entry.offset = nextOffset;
                        entry.inFlight = false;
                        await writeJson(journalPath, job);
                        progress({ name: file.name, uploaded: entry.offset, size: file.size });
                    }
                }

                const result = await complete(completionUrl, session.completionToken, { action: 'complete', result: entry.receipt });
                if (result.status !== 'READY' || !result.file?.fileUuid) throw new Error('File registration not confirmed');
                entry.result = result.file;
                entry.status = 'READY';
                entry.error = null;
            } catch (error) {
                entry.status = entry.inFlight ? 'UNKNOWN' : 'PAUSED';
                // Do not copy response bodies or signed addresses into human-readable output.
                entry.error = entry.inFlight ? 'Chunk outcome unknown; preserve this journal' : 'Upload paused; preserve this journal and check the session';
                if (entry.inFlight) await complete(checkedUrl(session.completionUrl, allowLocal), session.completionToken, { action: 'uncertain' }).catch(() => {});
            }

            await writeJson(journalPath, job);
        }

        return job.entries.map(entry => ({ name: entry.file.name, status: entry.status, file: entry.result, error: entry.error ?? null }));
    } finally {
        await lock.close();
        await fs.unlink(lockPath); // Only our local process lock. Never deletes files on the school storage.
    }
};

const main = async () => {
    const [command, first, second, third, ...rest] = process.argv.slice(2);
    const flags = process.argv.slice(2);

    if (command === 'inspect' && first && second) {
        const result = await inspect(first, flags.includes('--recursive'));
        await writeJson(second, result, true);
        process.stdout.write(JSON.stringify({ manifest: second, count: result.count, totalBytes: result.totalBytes, skipped: result.skipped }) + '\n');
    } else if (command === 'bind' && first && second && third && !rest.length) {
        const files = JSON.parse(await fs.readFile(first, 'utf8'));
        const sessions = JSON.parse(await fs.readFile(second, 'utf8'));
        await writeJson(third, bind(files.files ?? files, sessions.items ?? sessions), true);
        process.stdout.write('Upload journal created\n');
    } else if (command === 'run' && first) {
        const result = await run(first, { allowLocal: flags.includes('--allow-local'), progress: value => process.stdout.write(JSON.stringify(value) + '\n') });
        process.stdout.write(JSON.stringify(result, null, 2) + '\n');
        if (result.some(item => item.status !== 'READY')) process.exitCode = 1;
    } else {
        throw new Error('Usage: inspect SOURCE MANIFEST [--recursive] | bind FILES_JSON SESSIONS_JSON JOURNAL | run JOURNAL [--allow-local]');
    }
};



module.exports = { inspect, bind, run, checkedUrl, writeJson };

if (require.main === module) main().catch(error => {
    process.stderr.write(error.message + '\n');
    process.exitCode = 1;
});
