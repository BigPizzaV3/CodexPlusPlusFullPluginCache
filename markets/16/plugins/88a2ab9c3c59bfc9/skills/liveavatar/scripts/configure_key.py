#!/usr/bin/env python3
"""User-run local credential entry. No network calls or key output."""
import argparse
import getpass
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import warnings

TARGETS = {
    'web': ('apps/demo/.env.local', 'LIVEAVATAR_API_KEY', 'apps/demo/package.json'),
    'sales': ('.env.local', 'LIVEAVATAR_API_KEY', 'package.json'),
    'livekit': ('.env.local', 'LIVEAVATAR_API_KEY', 'pyproject.toml'),
    'gpt-live': ('.env', 'LIVEAVATAR_API_KEY', 'server/package.json'),
    'hyperframes': ('.env', 'LIVEAVATAR_API_KEY', 'backend/server.js'),
}

def target(project, sample):
    relative, variable, marker = TARGETS[sample]
    project = Path(project).resolve(strict=True)
    if not (project / marker).is_file():
        raise ValueError('This folder does not match the chosen sample.')
    path = project / relative
    if path.is_symlink() or not path.parent.resolve().is_relative_to(project):
        raise ValueError('Refusing an environment file outside the project or a symlink.')
    ignored = subprocess.run(['git', 'check-ignore', '--quiet', '--', str(path)], cwd=project,
                             stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if ignored.returncode != 0:
        raise ValueError('Add the environment file to .gitignore before entering a key.')
    tracked = subprocess.run(['git', 'ls-files', '--error-unmatch', '--', str(path)], cwd=project,
                             stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if tracked.returncode == 0:
        raise ValueError('The environment file is tracked. Remove it from version control first.')
    return path, variable

def has_value(text, variable):
    entries = re.findall(r'^\s*(?:export\s+)?' + re.escape(variable) + r'\s*=([^\n]*)', text, re.MULTILINE)
    return any(entry.strip() not in ('', '""', "''") and not entry.strip().startswith('#') for entry in entries)

def save_key(path, variable, value, replace=False):
    if not value or value != value.strip() or any(c.isspace() or ord(c) < 32 for c in value):
        raise ValueError('Enter a nonempty API key without whitespace.')
    if path.is_symlink():
        raise ValueError('Refusing a symlink environment file.')
    text = path.read_text() if path.exists() else ''
    pattern = re.compile(r'^\s*(?:export\s+)?' + re.escape(variable) + r'\s*=.*$', re.MULTILINE)
    existing = pattern.findall(text)
    if has_value(text, variable) and not replace:
        raise ValueError('A value already exists. Reuse it, or run with --replace to change it.')
    line = variable + '=' + json.dumps(value)
    if existing:
        # Remove duplicate definitions rather than leave an earlier value active.
        lines = text.splitlines(); emitted = False; output = []
        for old in lines:
            if pattern.fullmatch(old):
                if not emitted:
                    output.append(line); emitted = True
            else:
                output.append(old)
        updated = '\n'.join(output) + '\n'
    else:
        updated = text + ('\n' if text and not text.endswith('\n') else '') + line + '\n'
    fd, temporary = tempfile.mkstemp(prefix='.liveavatar-env-', dir=path.parent)
    try:
        os.chmod(temporary, 0o600)
        with os.fdopen(fd, 'w') as stream:
            stream.write(updated)
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--project-dir', required=True)
    parser.add_argument('--sample', choices=TARGETS, required=True)
    parser.add_argument('--replace', action='store_true')
    args = parser.parse_args()
    try:
        path, variable = target(args.project_dir, args.sample)
        existing = path.read_text() if path.exists() else ''
        if has_value(existing, variable) and not args.replace:
            print('An environment value already exists. Reuse it or run with --replace.')
            return 1
        if not sys.stdin.isatty():
            raise ValueError('Run this helper yourself in an interactive local terminal; do not send the key through chat or a tool.')
        print('Get your key at https://app.liveavatar.com/developers')
        with warnings.catch_warnings():
            warnings.simplefilter('error', getpass.GetPassWarning)
            value = getpass.getpass('LiveAvatar API key (input hidden): ')
        save_key(path, variable, value, args.replace)
        print('Key saved locally. No key was printed or sent over the network. API validity has not been checked.')
        return 0
    except (ValueError, OSError, EOFError, getpass.GetPassWarning):
        # Do not echo exception details that could contain environment content.
        print('Setup could not complete. Check the sample folder, ignored environment file and interactive terminal. No key will be echoed.', file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        print('\nCancelled.'); return 1

if __name__ == '__main__':
    raise SystemExit(main())
