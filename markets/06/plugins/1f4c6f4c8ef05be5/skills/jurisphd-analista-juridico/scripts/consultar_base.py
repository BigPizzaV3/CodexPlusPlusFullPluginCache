#!/usr/bin/env python3
"""Consulta lexical somente leitura à base metodológica fornecida pelo autor."""
import argparse
import json
from pathlib import Path
import re
import sys
import unicodedata


def normalize(text):
    return ''.join(c for c in unicodedata.normalize('NFKD', text.casefold())
                   if not unicodedata.combining(c))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--query')
    group.add_argument('--id')
    parser.add_argument('--limit', type=int, default=5)
    args = parser.parse_args()
    if not 1 <= args.limit <= 20:
        parser.error('--limit deve estar entre 1 e 20')
    path = Path(__file__).resolve().parent.parent / 'references' / 'base_conhecimento_v6.2.1.jsonl'
    try:
        rows = [json.loads(line) for line in path.read_text(encoding='utf-8').splitlines() if line.strip()]
        if args.id is not None:
            results = [r for r in rows if r['id'] == args.id]
        else:
            terms = set(re.findall(r'\w+', normalize(args.query)))
            if not terms:
                parser.error('--query precisa conter letras ou números')
            ranked = []
            for row in rows:
                fields = ('categoria', 'subcategoria', 'tags', 'quando_usar', 'exemplo', 'contraexemplo', 'correcao_obrigatoria')
                words = set(re.findall(r'\w+', normalize(' '.join(str(row.get(k, '')) for k in fields))))
                score = len(terms & words)
                if score:
                    ranked.append((score, row['id'], row))
            results = [r for _, _, r in sorted(ranked, key=lambda x: (-x[0], x[1]))[:args.limit]]
        print(json.dumps({'status': 'found' if results else 'no_results',
                          'method': 'local_lexical', 'legal_authority': False,
                          'results': results}, ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError, KeyError) as exc:
        print(json.dumps({'status': 'error', 'message': str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
