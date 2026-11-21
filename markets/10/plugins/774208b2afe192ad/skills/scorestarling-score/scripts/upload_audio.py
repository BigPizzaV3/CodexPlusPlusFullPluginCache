"""Prepare one audio upload, POST raw bytes once, and inspect the original MCP job."""
import argparse
import asyncio
import json
import logging
import math
from pathlib import Path
import sys
import time
from urllib.parse import urlsplit

import httpx

# The server's limits (apps/server/upload_access.py): WAV, AIFF and FLAC, recognised by their first bytes,
# may be larger than other files.
MAX_BYTES = 50 * 1024 * 1024
MAX_LOSSLESS_BYTES = 120 * 1024 * 1024


def origin(url):
    value = urlsplit(url)
    if (not value.hostname or value.username or value.password or value.query or value.fragment
            or not (value.scheme == 'https' or
                    value.scheme == 'http' and value.hostname in ('127.0.0.1', 'localhost', '::1'))):
        raise ValueError('Use a credential-free HTTPS endpoint, or HTTP loopback for development')
    return value.scheme, value.hostname, value.port or (443 if value.scheme == 'https' else 80)


def lossless(head):
    return (head[:4] in (b'RIFF', b'RF64', b'BW64') and head[8:12] == b'WAVE'
            or head[:4] == b'FORM' and head[8:12] in (b'AIFF', b'AIFC') or head[:4] == b'fLaC')


def read_audio(path):
    path = Path(path)
    with path.open('rb') as source:
        audio = source.read(max(MAX_BYTES, MAX_LOSSLESS_BYTES) + 1)
    if not 0 < len(audio) <= (MAX_LOSSLESS_BYTES if lossless(audio[:12]) else MAX_BYTES):
        raise ValueError(f'Audio must be non-empty and no larger than {MAX_BYTES >> 20} MiB, or {MAX_LOSSLESS_BYTES >> 20} MiB '
                         'as WAV, AIFF or FLAC. Save it as FLAC or MP3 to make it smaller.')
    return audio


async def post_audio(ticket, audio, mcp_url, transport=None):
    job = ticket['job_id']
    print(f'Reserved job: {job}', file=sys.stderr, flush=True)
    if origin(ticket['upload_url']) != origin(mcp_url) or not urlsplit(ticket['upload_url']).path.startswith('/upload/'):
        raise ValueError(f'Unexpected upload origin/path for job {job}; inspect it before continuing')
    accepted = False
    # A separate client keeps the MCP bearer token off the capability POST; no redirects/retries.
    async with httpx.AsyncClient(timeout=30, follow_redirects=False, transport=transport) as upload:
        try:
            response = await upload.post(ticket['upload_url'], content=audio,
                                         headers={'Content-Type': 'application/octet-stream',
                                                  'Content-Length': str(len(audio))})
            accepted = response.status_code == 202
        except httpx.HTTPError:
            pass  # The server may have received it. Inspect this job, never POST again.
    return accepted


async def upload_audio(path, call_tool, mcp_url, *, bpm=None, provider='local',
                       mirelo_consent=False, timeout=600, poll_interval=2, transport=None):
    """Use a caller's already-authorized tool function; never obtain session credentials."""
    origin(mcp_url)
    if (provider not in ('local', 'piano', 'mirelo') or not math.isfinite(timeout)
            or not math.isfinite(poll_interval) or timeout <= 0 or poll_interval < 0):
        raise ValueError('Invalid provider or polling bounds')
    if provider == 'mirelo' and not mirelo_consent:
        raise ValueError('Mirelo requires explicit upload consent')
    audio = read_audio(path)
    ticket = await call_tool('prepare_audio_upload', {
        'filename': Path(path).name, 'size': len(audio), 'bpm': bpm,
        'provider': provider,
    })
    job = ticket['job_id']
    accepted = await post_audio(ticket, audio, mcp_url, transport)
    deadline = time.monotonic() + timeout
    while True:
        try:
            status = await asyncio.wait_for(call_tool('get_upload_status', {'job_id': job, 'wait_seconds': 20}),
                                            timeout=min(30, max(.001, deadline - time.monotonic())))
        except Exception:
            raise RuntimeError(f'Cannot confirm job {job}; inspect its status before retrying') from None
        state = status['status']
        if state == 'completed':
            return status  # Keep summary, tempo uncertainty and next_step for the caller's review.
        if state in ('failed', 'needs_review'):
            raise RuntimeError(f'Job {job} is {state}; inspect status and account usage before retrying')
        if state not in ('uploading', 'queued', 'running'):
            raise RuntimeError(f'Upload for job {job} is unconfirmed (HTTP 202: {accepted}); inspect it before retrying')
        if time.monotonic() >= deadline:
            raise TimeoutError(f'Job {job} still {state}; continue status checks, do not re-upload')
        await asyncio.sleep(min(poll_interval, max(0, deadline - time.monotonic())))


async def main(args, transport=None):
    # The connected host reserves/polls the job. This CLI receives only its one-use ticket.
    ticket = json.load(sys.stdin)
    audio = read_audio(args.audio)
    if type(ticket.get('size')) is not int or ticket['size'] != len(audio):
        raise ValueError('The local file must match the exact byte count used to prepare the ticket')
    accepted = await post_audio(ticket, audio, args.mcp_url, transport)
    print(json.dumps({'job_id': ticket['job_id'], 'upload_accepted': accepted}))
    return 0 if accepted else 2


if __name__ == '__main__':
    logging.getLogger('httpx').setLevel(logging.WARNING)
    logging.getLogger('httpcore').setLevel(logging.WARNING)
    parser = argparse.ArgumentParser(description='POST once using a prepare_audio_upload ticket JSON on stdin; poll through the connected host.')
    parser.add_argument('audio', type=Path)
    # Upload links live on the site, not the MCP host; --mcp-url is the earlier name of this option.
    parser.add_argument('--site', '--mcp-url', dest='mcp_url', default='https://scorestarling.com')
    try:
        code = asyncio.run(main(parser.parse_args()))
    except Exception:
        # SDK/network exceptions may embed credentials or capability URLs. Do not print them.
        raise SystemExit('Upload not confirmed. Inspect the original job in the connected host before retrying.') from None
    raise SystemExit(code)
