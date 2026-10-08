# -*- coding: utf-8 -*-
"""只为本机缓存账号可下载的插件包，不安装、不执行或公开上传。"""
from pathlib import Path
import collections
import concurrent.futures
import hashlib
import json
import os
import threading
import time
import urllib.error
import urllib.request
from urllib.parse import quote, urlparse

ROOT = Path(__file__).resolve().parents[1]
AUDIT = Path('/var/folders/0s/y8fsqjhd20d_twbcc2j7mj040000gn/T/codex-full-cloud-license-audit-s30t8w7j')
HOME = Path('/Users/mac/.codex')
MAX_BYTES = 128 * 1024**2
catalog = json.loads((AUDIT / 'catalog-snapshot.json').read_text())
items = catalog['plugins']
stop = threading.Event()
auth_failures = 0
lock = threading.Lock()

def headers():
    data = json.loads((HOME / 'auth.json').read_text())['tokens']
    return {'Authorization': 'Bearer '+data['access_token'], 'ChatGPT-Account-ID': data['account_id'], 'OAI-Product-Sku': 'codex', 'User-Agent': 'codex-cli/0.160.1', 'Accept': 'application/json'}

def archive_name(item):
    return hashlib.sha256(item['id'].encode()).hexdigest()+'.tar.gz'

for item in items:
    name = archive_name(item)
    destination = ROOT / 'archives' / name
    if destination.exists():
        continue
    for directory in ['archives', 'pending-archives']:
        source = AUDIT / directory / name
        if source.exists():
            os.link(source, destination)
            break

def download(item):
    global auth_failures
    name = archive_name(item)
    path = ROOT / 'archives' / name
    result = {'id': item['id'], 'directoryName': item['name'], 'directoryVersion': (item.get('release') or {}).get('version'), 'discoverability': item.get('discoverability')}
    if path.exists():
        return dict(result, state='cached', archiveFile=name, archiveBytes=path.stat().st_size, reused=True)
    if item.get('status') == 'DISABLED_BY_ADMIN' or item.get('installation_policy') == 'NOT_AVAILABLE':
        return dict(result, state='account_access_unavailable')
    if stop.is_set():
        return dict(result, state='authentication_unavailable')
    for attempt in range(2):
        stage = 'detail'
        try:
            request = urllib.request.Request('https://chatgpt.com/backend-api/ps/plugins/'+quote(item['id'],safe='')+'?includeDownloadUrls=true',headers=headers())
            with urllib.request.urlopen(request, timeout=25) as response:
                detail = json.load(response)
            with lock:
                auth_failures = 0
            url = (detail.get('release') or {}).get('bundle_download_url')
            if not url:
                return dict(result, state='no_downloadable_bundle')
            if urlparse(url).scheme != 'https':
                return dict(result, state='unsupported_download_scheme')
            stage = 'download'
            request = urllib.request.Request(url,headers={'User-Agent':'codex-cli/0.160.1'})
            with urllib.request.urlopen(request,timeout=35) as response:
                size = response.headers.get('Content-Length')
                if size and int(size)>MAX_BYTES:
                    return dict(result,state='archive_over_128MiB',archiveBytes=int(size))
                parts=[]
                size=0
                while True:
                    chunk=response.read(65536)
                    if not chunk:
                        break
                    size+=len(chunk)
                    if size>MAX_BYTES:
                        return dict(result,state='archive_over_128MiB',archiveBytes=size)
                    parts.append(chunk)
            data=b''.join(parts)
            if not data.startswith(b'\x1f\x8b'):
                return dict(result,state='unsupported_bundle_format')
            path.write_bytes(data)
            path.chmod(0o600)
            return dict(result,state='cached',archiveFile=name,archiveBytes=len(data),archiveSha256=hashlib.sha256(data).hexdigest(),reused=False)
        except urllib.error.HTTPError as error:
            if error.code==429:
                delay=int(error.headers.get('Retry-After','10'))
                if delay>60:
                    return dict(result,state='rate_limited',retryAfterSeconds=delay)
                time.sleep(max(2,delay))
                if attempt==0:
                    continue
            if stage=='detail' and error.code in [401,403]:
                with lock:
                    auth_failures+=1
                    if auth_failures>=3:
                        stop.set()
            if attempt==0 and error.code>=500:
                time.sleep(2)
                continue
            return dict(result,state='http_error',stage=stage,status=error.code)
        except Exception as error:
            if attempt==0:
                time.sleep(1)
                continue
            return dict(result,state='read_error',stage=stage,errorType=type(error).__name__)

log_path=ROOT/'download-results.jsonl'
previous=[json.loads(line) for line in log_path.read_text().splitlines()] if log_path.exists() else []
done={v['id'] for v in previous if v['state']=='cached'}
pending=[item for item in items if item['id'] not in done]
results={v['id']:v for v in previous}
started=last=time.monotonic()
print('FULL_LOCAL_DOWNLOAD_START',json.dumps({'directoryCount':len(items),'existingArchives':len(list((ROOT/'archives').glob('*.tar.gz'))),'workers':32,'publicUpload':False,'installerInvoked':False}),flush=True)
with log_path.open('a') as log,concurrent.futures.ThreadPoolExecutor(max_workers=32) as pool:
    futures=[pool.submit(download,item) for item in pending]
    for future in concurrent.futures.as_completed(futures):
        result=future.result();results[result['id']]=result;log.write(json.dumps(result,ensure_ascii=False)+'\n');log.flush()
        now=time.monotonic()
        if now-last>=20 or len(results)==len(items):
            summary={'directoryCount':len(items),'processed':len(results),'elapsedSeconds':round(now-started),'states':dict(collections.Counter(v['state'] for v in results.values())),'cachedBytes':sum(v.get('archiveBytes',0) for v in results.values() if v['state']=='cached'),'publicUpload':False,'installerInvoked':False}
            (ROOT/'download-summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2))
            print('FULL_LOCAL_DOWNLOAD_PROGRESS',json.dumps(summary,ensure_ascii=False),flush=True);last=now
(ROOT/'directory.json').write_text(json.dumps({'snapshotDate':'2026-10-08','entries':sorted(results.values(),key=lambda v:v['id'])},ensure_ascii=False,indent=2))
print('FULL_LOCAL_DOWNLOAD_COMPLETE',str(ROOT/'download-summary.json'),flush=True)
