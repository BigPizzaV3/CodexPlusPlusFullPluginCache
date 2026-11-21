#!/usr/bin/env python3
"""Encode a program JSON file as a portable signup/import link; stdlib only."""
import argparse
import base64
import json
from pathlib import Path
import zlib

parser = argparse.ArgumentParser()
parser.add_argument('program', type=Path)
args = parser.parse_args()
if args.program.stat().st_size > 300000:
    parser.error('Program is too large; split into smaller blocks.')
program = json.loads(args.program.read_text())
if not isinstance(program, dict) or program.get('v') != 1:
    parser.error('Expected a v1 program object.')
if set(program) != {'v', 'name', 'entries'}:
    parser.error('Only v, name and entries belong in a link. Never include personal account data.')
raw = json.dumps(program, ensure_ascii=False, separators=(',', ':')).encode()
if len(raw) > 300000:
    parser.error('Program is too large.')
token = base64.urlsafe_b64encode(zlib.compress(raw, 9)).decode().rstrip('=')
if len(token) > 24000:
    parser.error('Link is too long; split into smaller blocks.')
print('https://www.weightliftinganalytics.com/program-import#plan=' + token)
