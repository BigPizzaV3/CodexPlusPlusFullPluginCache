#!/usr/bin/env python3
"""Run BetterContext actions locally without registering an MCP server."""
import argparse
import json
from pathlib import Path
import sqlite3
import subprocess
import sys

sys.dont_write_bytecode = True
from memory_mcp import TOOLS, BY_NAME, invoke

def main():
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, 'reconfigure'):
            stream.reconfigure(encoding='utf-8')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', nargs='?', default='list', choices=['list', *BY_NAME])
    values = parser.add_mutually_exclusive_group()
    values.add_argument('--arguments-file', type=Path, help='UTF-8 JSON object containing action arguments.')
    values.add_argument('--arguments-json', help='A JSON object; prefer a file to avoid shell quoting problems.')
    args = parser.parse_args()
    if args.action == 'list':
        result = {'transport': 'local-command', 'actions': TOOLS}
    else:
        raw = args.arguments_file.read_text(encoding='utf-8-sig') if args.arguments_file else (args.arguments_json or '{}')
        result = invoke(args.action, json.loads(raw))
        if args.action == 'memory_health':
            result['transport'] = 'local-command'
    print(json.dumps(result, ensure_ascii=False, indent=2, default=str))

if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError, sqlite3.Error, subprocess.SubprocessError) as error:
        print(json.dumps({'error':str(error)}, ensure_ascii=False), file=sys.stderr)
        raise SystemExit(2)
