# -*- coding: utf-8 -*-
"""在隔离 API Key 会话中只读取本地完整目录，不安装包。"""
from pathlib import Path
import json
import os
import queue
import re
import subprocess
import tempfile
import threading
import time

ROOT=Path(__file__).resolve().parents[1]
HOME=Path(tempfile.mkdtemp(prefix='codex-full-local-read-test-'))
settings=json.loads(Path('/Users/mac/.codex-session-delete/settings.json').read_text())
profile=next(v for v in settings['relayProfiles'] if v['id']==settings['activeRelayId'])
auth=json.loads(profile.get('authContents') or '{}');key=profile.get('apiKey') or auth.get('OPENAI_API_KEY')
if not key:
    match=re.search(r'experimental_bearer_token\s*=\s*("(?:[^"\\]|\\.)*")',profile.get('configContents',''));key=json.loads(match.group(1)) if match else None
if not key:raise RuntimeError('No relay key is available')
(HOME/'config.toml').write_text('cli_auth_credentials_store = "ephemeral"\n\n[features]\nremote_plugin = false\n')
env=os.environ.copy();env['CODEX_HOME']=str(HOME)
for name in ['OPENAI_API_KEY','CODEX_API_KEY','CODEX_ACCESS_TOKEN']:env.pop(name,None)
proc=subprocess.Popen(['/Applications/ChatGPT.app/Contents/Resources/codex-cli/bin/codex','app-server'],cwd=HOME,env=env,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.DEVNULL,text=True,bufsize=1)
messages=queue.Queue();sequence=0
def reader():
    for line in proc.stdout:
        try:messages.put(json.loads(line))
        except ValueError:pass
threading.Thread(target=reader,daemon=True).start()
def send(value):proc.stdin.write(json.dumps(value)+'\n');proc.stdin.flush()
def request(method,params):
    global sequence
    sequence+=1;current=sequence;send({'id':current,'method':method,'params':params});deadline=time.monotonic()+90
    while time.monotonic()<deadline:
        try:value=messages.get(timeout=max(.01,deadline-time.monotonic()))
        except queue.Empty:break
        if value.get('id')==current:return value
    return {'error':{'message':'timeout'}}
report={'authentication':'apiKey','installerInvoked':False,'browserAuthorizationInvoked':False,'registrations':[]}
try:
    request('initialize',{'clientInfo':{'name':'codex-full-local-read-test','version':'1.0.0'},'capabilities':{'experimentalApi':True}});send({'method':'initialized','params':{}})
    request('account/login/start',{'type':'apiKey','apiKey':key})
    summary=json.loads((ROOT/'summary.json').read_text())
    for market in summary['marketplaces']:
        response=request('marketplace/add',{'source':market['root']});report['registrations'].append({'name':market['name'],'success':'result' in response});print('REGISTER_READ_TEST',market['name'],'result' in response,flush=True)
    response=request('plugin/list',{'marketplaceKinds':['local']})
    markets=[v for v in response.get('result',{}).get('marketplaces',[]) if v['name'].startswith('codex-plus-full-local-')]
    report['marketplaceCounts']={v['name']:len(v['plugins']) for v in markets};report['totalAvailablePackages']=sum(report['marketplaceCounts'].values());report['loadErrors']=len(response.get('result',{}).get('marketplaceLoadErrors',[]));print('API_FULL_CATALOG',json.dumps(report,ensure_ascii=False),flush=True)
finally:
    proc.terminate()
    try:proc.wait(timeout=3)
    except subprocess.TimeoutExpired:proc.kill();proc.wait()
    (ROOT/'api-read-validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
if report.get('totalAvailablePackages')!=5491 or report.get('loadErrors') or not all(v['success'] for v in report['registrations']):raise SystemExit(1)
