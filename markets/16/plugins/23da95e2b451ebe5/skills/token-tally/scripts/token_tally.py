#!/usr/bin/env python3
"""Token Tally: local, read-only account retrieval and deterministic card export."""
import argparse
import hashlib
import re
import datetime as dt
import json
import os
from pathlib import Path
import queue
import shutil
import subprocess
import sys
import tempfile
import threading
import time
from decimal import Decimal, ROUND_HALF_UP

SOURCE = 'codex-app-server/account/usage/read'
SUMMARY_KEYS = ('lifetimeTokens', 'peakDailyTokens', 'longestRunningTurnSec', 'currentStreakDays', 'longestStreakDays')

def counter(v):
    if v is not None and (type(v) is not int or v < 0):
        raise ValueError('Usage counters must be non-negative integers or null.')
    return v

def clean_result(result):
    summary = result.get('summary')
    if not isinstance(summary, dict):
        raise ValueError('Usage response has no summary object.')
    buckets = result.get('dailyUsageBuckets')
    if buckets is not None:
        if not isinstance(buckets, list):
            raise ValueError('Daily buckets must be an array or null.')
        clean = []
        for b in buckets:
            date = dt.date.fromisoformat(b['startDate']).isoformat()
            clean.append({'startDate':date, 'tokens':counter(b.get('tokens'))})
        buckets = clean
    return {'summary':{k:counter(summary.get(k)) for k in SUMMARY_KEYS}, 'dailyUsageBuckets':buckets}

def codex_path(explicit=None):
    if explicit:
        return str(Path(explicit).expanduser().resolve())
    executable = shutil.which('codex')
    if executable:
        return executable
    for app in ('ChatGPT','Codex'):
        p = Path('/Applications') / (app+'.app') / 'Contents/Resources/codex-cli/CodexCLI.app/Contents/MacOS/codex'
        if p.is_file():
            return str(p)
    raise RuntimeError('Codex CLI not found. Install/sign in to the official desktop app or CLI, or pass --codex.')

def fetch_usage(executable, timeout=30):
    # No shell, no credential-file reads, no generation, and no uploads.
    with tempfile.TemporaryFile() as errors:
        p = subprocess.Popen([executable,'app-server','--stdio'], stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE, stderr=errors, text=True, bufsize=1)
        q = queue.Queue()
        def reader():
            for line in p.stdout:
                q.put(line)
            q.put(None)
        thread = threading.Thread(target=reader, daemon=True)
        thread.start()
        def send(payload):
            p.stdin.write(json.dumps(payload)+'\n')
            p.stdin.flush()
        try:
            send({'id':1,'method':'initialize','params':{'clientInfo':{'name':'token_tally','title':'Token Tally','version':'0.4.6'},'capabilities':{'experimentalApi':True}}})
            deadline = time.monotonic()+timeout
            while True:
                remaining = deadline-time.monotonic()
                if remaining <= 0:
                    raise RuntimeError('Account usage request timed out. Check connectivity and official app sign-in.')
                try:
                    line = q.get(timeout=remaining)
                except queue.Empty:
                    raise RuntimeError('Account usage request timed out. Check connectivity and official app sign-in.')
                if line is None:
                    raise RuntimeError('App server stopped before returning usage. Check local state permissions and official app sign-in.')
                try:
                    response = json.loads(line)
                except json.JSONDecodeError:
                    continue
                request_id = response.get('id')
                if request_id not in (1,2):
                    continue
                if 'error' in response:
                    code = response['error'].get('code','unknown')
                    raise RuntimeError(f'App server rejected usage request (code {code}). Check sign-in, permissions, and app-server compatibility.')
                if request_id == 1:
                    send({'method':'initialized','params':{}})
                    send({'id':2,'method':'account/usage/read'})
                else:
                    result = clean_result(response['result'])
                    return {'schemaVersion':1,'source':SOURCE,'retrievedAt':dt.datetime.now(dt.timezone.utc).isoformat(),**result}
        finally:
            p.terminate()
            try:
                p.wait(timeout=3)
            except subprocess.TimeoutExpired:
                p.kill(); p.wait()
            for stream in (p.stdin,p.stdout):
                stream.close()

def compact(value, precision=2):
    if value is None:
        return '—'
    for divisor, suffix in [(10**15,'Q'),(10**12,'T'),(10**9,'B'),(10**6,'M'),(10**3,'K')]:
        if value >= divisor:
            amount = (Decimal(value)/Decimal(divisor)).quantize(Decimal(10)**-precision,rounding=ROUND_HALF_UP)
            if amount >= 1000 and divisor < 10**15:
                return compact(value, 0) if precision else f'{amount/1000:g}'+{10**3:'M',10**6:'B',10**9:'T',10**12:'Q'}[divisor]
            return format(amount,'f').rstrip('0').rstrip('.')+suffix if precision else format(amount,'f')+suffix
    return str(value)

def duration_label(seconds):
    if seconds is None:
        return '—'
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    if hours:
        return f'{hours}h {minutes:02d}m'
    if minutes:
        return f'{minutes}m {seconds:02d}s'
    return f'{seconds}s'

def base36(value):
    if type(value) is not int or value < 0:
        raise ValueError('Mark values must be non-negative integers.')
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    while value:
        value, digit = divmod(value, 36)
        result = digits[digit] + result
    return result or '0'

def record_mark(total, instant, source):
    if total is None:
        return ''
    kind = 'A' if source == SOURCE else 'S'
    payload = f'T1{kind}.{base36(total)}.{base36(int(instant.timestamp()))}'
    return payload + '.' + hashlib.sha256(payload.encode('ascii')).hexdigest()[:8].upper()

def decode_mark(mark, expected=None):
    mark = mark.strip().upper()
    if not re.fullmatch(r'T1[AS]\.[0-9A-Z]{1,32}\.[0-9A-Z]{1,13}\.[0-9A-F]{8}', mark):
        raise ValueError('Invalid Token Tally record mark format.')
    payload, checksum = mark.rsplit('.', 1)
    if hashlib.sha256(payload.encode('ascii')).hexdigest()[:8].upper() != checksum:
        raise ValueError('Record mark checksum mismatch; check transcription or editing.')
    version, tokens, timestamp = payload.split('.')
    count = int(tokens, 36)
    try:
        instant = dt.datetime.fromtimestamp(int(timestamp, 36), dt.timezone.utc)
    except (ValueError, OverflowError, OSError) as e:
        raise ValueError('Record mark timestamp is outside the supported range.') from e
    result = {'lifetimeTokens': count, 'displayTotal': compact(count),
              'collectedAt': instant.isoformat().replace('+00:00','Z'),
              'declaredSource': 'account-reported' if version == 'T1A' else 'supplied',
              'checksumValid': True, 'authenticated': False,
              'notice': 'Unsigned consistency record. Both the image and mark can be regenerated; this does not prove account usage.'}
    if expected is not None:
        result['matchesExactTotal'] = count == expected
    return result

def run(command):
    result = subprocess.run(command, capture_output=True, text=True, timeout=90)
    if result.returncode:
        raise RuntimeError(f'Renderer command failed: {result.stderr.strip()[:1200]}')
    return result.stdout

def resolve_fonts(regular=None, semibold=None, bold=None, font_set='auto'):
    explicit = (regular, semibold, bold)
    if any(explicit):
        if not all(explicit):
            raise ValueError('Supply all three font paths together.')
        paths = tuple(str(Path(f).expanduser().resolve()) for f in explicit)
    else:
        local = tuple(f'/Library/Fonts/SF-Pro-Display-{style}.otf' for style in ('Regular','Semibold','Bold'))
        folder = Path(__file__).resolve().parent.parent/'assets/fonts'
        paths = local if font_set == 'auto' and all(Path(f).is_file() for f in local) else tuple(str(folder/f'InterDisplay-{style}.otf') for style in ('Regular','SemiBold','Bold'))
    for path in paths:
        if not Path(path).is_file():
            raise RuntimeError(f'Required font missing: {path}. Reinstall the complete plugin package.')
    return paths

def resolve_renderer(explicit=None):
    candidates = [explicit] if explicit else [
        str(Path.home()/'Library/Application Support/TokenTally/Tesseract/bin/tsrct'),
        str(Path.home()/'Library/Application Support/Tesseract/bin/tsrct'),
        str(Path(os.environ.get('LOCALAPPDATA',str(Path.home())))/'Tesseract/bin/tsrct.cmd'),
        str(Path(os.environ.get('XDG_DATA_HOME',str(Path.home()/'.local/share')))/'Tesseract/bin/tsrct'),
        shutil.which('tsrct')]
    for candidate in candidates:
        if candidate and Path(candidate).is_file():
            try:
                if run([candidate,'--version']).startswith('tsrct 0.3.1 '):
                    return str(Path(candidate).resolve())
            except (OSError, RuntimeError, subprocess.TimeoutExpired):
                continue
    raise RuntimeError('Tesseract CLI 0.3.1 is missing or cannot run. Use the token-tally-setup skill or pass --tsrct with the pinned renderer path.')

def export_card(snapshot, out, tsrct, regular, semibold, bold, font_set='auto'):
    data = clean_result(snapshot)
    timestamp = snapshot.get('retrievedAt')
    if not timestamp:
        raise ValueError('Snapshot requires retrievedAt so historical data is not dated as new.')
    instant = dt.datetime.fromisoformat(timestamp.replace('Z','+00:00'))
    if instant.tzinfo is None:
        raise ValueError('retrievedAt must include a timezone.')
    date = instant.astimezone(dt.timezone.utc)
    tsrct = resolve_renderer(tsrct)
    regular, semibold, bold = resolve_fonts(regular, semibold, bold, font_set)
    out.mkdir(parents=True,exist_ok=False)
    project = out/'Token-card.tsrct'
    png = out/'Token-card.png'
    run([tsrct,'project','create','--project',str(project)])
    icon = Path(__file__).resolve().parents[3]/'assets/token-tally-icon.png'
    run([tsrct,'project','import-asset','--project',str(project),'--file',str(icon),'--asset-id','token-tally-icon','--kind','image'])
    font_faces = {}
    for weight, f in zip(('Regular','Semibold','Bold'), (regular,semibold,bold)):
        imported = json.loads(run([tsrct,'project','import-font','--project',str(project),'--file',str(f)]))
        font_faces[weight] = (imported['fontFamily'], imported['fontStyle'])
    template = Path(__file__).resolve().parent.parent/'assets/card-template.json'
    document = json.loads(template.read_text())
    s = data['summary']; total=s['lifetimeTokens']; peak=s['peakDailyTokens']; streak=s['currentStreakDays']
    replacements = {'Hero total':compact(total),'Exact total':f'{total:,} to be exact.' if total is not None else 'Lifetime total unavailable',
                    'Peak value':compact(peak,1),
                    'Streak value':(f'{streak} '+('day' if streak==1 else 'days')) if streak is not None else '—',
                    'Longest value':duration_label(s['longestRunningTurnSec']),
                    'Record mark':record_mark(total, date, snapshot.get('source'))}
    for layer in document['composition']['layers']:
        name=layer['name']
        if 'sourceText' in layer:
            text_style = layer['sourceText']
            family, style = font_faces[text_style['fontStyle']]
            text_style['fontFamily'], text_style['fontStyle'] = family, style
        if name in replacements:
            layer['sourceText']['text']=replacements[name]
        if name=='Hero total':
            layer['sourceText']['fontSize']=min(300, 1500/max(len(replacements[name]),1))
        if name=='Streak value':
            layer['sourceText']['fontSize']=min(52,440/max(len(replacements[name]),1))
        if name=='Exact total' and total is not None and len(str(total))>16:
            layer['sourceText']['fontSize']=20
    layout = out/'card-layout.json'
    layout.write_text(json.dumps(document,indent=2)+'\n')
    run([tsrct,'project','commit','--project',str(project),'--file',str(layout)])
    run([tsrct,'preview','--project',str(project),'--time','1','--output',str(png)])
    return {'png':str(png),'editable':str(project),'width':1080,'height':1350}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    subs=parser.add_subparsers(dest='command',required=True)
    stats=subs.add_parser('stats'); stats.add_argument('--codex'); stats.add_argument('--output',type=Path,required=True)
    card=subs.add_parser('card'); card.add_argument('--snapshot',type=Path,required=True); card.add_argument('--output-dir',type=Path,required=True)
    stats.add_argument('--no-card', action='store_true', help='Explicitly retrieve statistics without exporting a card.')
    stats.add_argument('--card-dir', type=Path, help='New output directory; defaults to <snapshot-stem>-card beside the snapshot.')
    doctor=subs.add_parser('doctor', help='Check local dependencies without reading account data.')
    for command in (stats, card, doctor):
        command.add_argument('--tsrct')
        command.add_argument('--font-set', choices=('auto','bundled'), default='auto')
        command.add_argument('--font-regular')
        command.add_argument('--font-semibold')
        command.add_argument('--font-bold')
    decode=subs.add_parser('decode', help='Decode an unsigned card record mark.')
    decode.add_argument('mark')
    decode.add_argument('--tokens', type=int, help='Exact visible lifetime total to compare.')
    args=parser.parse_args()
    try:
        if args.command=='doctor':
            print(json.dumps({'codex':codex_path(), 'renderer':resolve_renderer(args.tsrct), 'fonts':resolve_fonts(args.font_regular,args.font_semibold,args.font_bold,args.font_set)}))
        elif args.command=='decode':
            print(json.dumps(decode_mark(args.mark, args.tokens)))
        elif args.command=='stats':
            result=fetch_usage(codex_path(args.codex))
            args.output.parent.mkdir(parents=True,exist_ok=True)
            with args.output.open('x') as f:
                json.dump(result,f,indent=2); f.write('\n')
            report={'snapshot':str(args.output.resolve()),'summary':result['summary'],'dailyRecordCount':len(result['dailyUsageBuckets']) if result['dailyUsageBuckets'] is not None else None}
            if not args.no_card:
                destination=(args.card_dir or args.output.with_name(args.output.stem+'-card')).resolve()
                try:
                    report.update(export_card(result,destination,args.tsrct,args.font_regular,args.font_semibold,args.font_bold,args.font_set))
                except (RuntimeError,ValueError,OSError,KeyError,subprocess.TimeoutExpired) as e:
                    print(json.dumps(report))
                    raise RuntimeError(f'Stats saved to {args.output.resolve()}, but automatic card export failed: {e}') from e
            print(json.dumps(report))
        else:
            print(json.dumps(export_card(json.loads(args.snapshot.read_text()),args.output_dir.resolve(),args.tsrct,args.font_regular,args.font_semibold,args.font_bold,args.font_set)))
    except (RuntimeError,ValueError,OSError,KeyError,subprocess.TimeoutExpired) as e:
        print(f'Token Tally: {e}',file=sys.stderr); return 1
    return 0

if __name__=='__main__':
    sys.exit(main())
