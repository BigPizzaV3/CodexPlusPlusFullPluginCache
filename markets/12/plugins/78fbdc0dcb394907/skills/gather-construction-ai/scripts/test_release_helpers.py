#!/usr/bin/env python3
"""Synthetic regression cases for observed MCP shapes. No customer data."""
import json
import subprocess
from pathlib import Path
ROOT = Path(__file__).resolve().parent

def run(name, response, args=None):
    proc = subprocess.run(['python3', str(ROOT/'hooks'/name)], input=json.dumps({'tool_response':response,'tool_input':args or {}}), text=True, capture_output=True, check=True)
    return proc.stdout

def envelope(data):
    return {'content':[{'type':'text','text':json.dumps({'_meta':{},'data':data})}]}

full={'uuid':'synthetic-record','answers':{'notes':'Work complete','workers':[{'name':'Synthetic'}],'weather_conditions':'Dry','start_time':'2026-09-01T08:00:00Z','end_time':'2026-09-01T16:00:00Z'}}
assert run('record_check.py',envelope(full)) == ''
full['answers']['end_time']='2026-09-01T23:00:00Z'
assert 'over 14' in run('record_check.py',envelope(full))
assert 'access' in run('shift_records_scan.py',envelope({'data':[{'uuid':'synthetic','narrative':'access denied'}],'pagination':{}})).lower()
print('PASS: 3 synthetic regressions (nested answers and MCP envelope, recorded duration plausibility, summary envelope).')
