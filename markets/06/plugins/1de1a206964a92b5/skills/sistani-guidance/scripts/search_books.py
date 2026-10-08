#!/usr/bin/env python3
"""Read-only keyword lookup for the bundled source pages. No network or file writes."""
from __future__ import annotations
import argparse
from collections import Counter
import json
import math
from pathlib import Path
import re
import sys
import unicodedata
from typing import Any

SKILL_ROOT = Path(__file__).resolve().parents[1]
STOPWORDS = set('a an the and or of to in on at is are be for with from as by it this that what how can does do i my me according about'.split())
ALIASES = {
    'fasting': ['sawm', 'fast', 'ramadan', 'ramadhan'],
    'prayer': ['salat', 'salah', 'namaz'],
    'purity': ['taharah', 'tahara', 'tahir'],
    'wudu': ['wudhu', 'ablution'],
    'istihada': ['istihadha', 'istihadah', 'istihadhah'],
    'menstruation': ['haydh', 'hayd', 'period'],
    'pilgrimage': ['hajj'],
    'travelling': ['travel', 'traveler', 'traveller', 'journey'],
    'traveling': ['travel', 'traveler', 'traveller', 'journey'],
    'transactions': ['trade', 'economic', 'selling', 'buying'],
    'inheritance': ['inherit', 'heir', 'heirs'],
}

def normalize(text: str) -> str:
    text = unicodedata.normalize('NFKD', text).casefold()
    text = ''.join(c for c in text if not unicodedata.combining(c))
    text = ''.join(str(unicodedata.digit(c)) if c.isdigit() and unicodedata.category(c) == 'Nd' else c for c in text)
    return text

def terms(text: str) -> list[str]:
    return [w for w in re.findall(r'\w+', normalize(text), flags=re.UNICODE) if w not in STOPWORDS]

def checked_path(relative: str) -> Path:
    path = (SKILL_ROOT / relative).resolve()
    if SKILL_ROOT not in path.parents or path.suffix != '.md':
        raise ValueError('Invalid reference path in source registry.')
    if not path.is_file():
        raise FileNotFoundError(f'Bundled reference missing: {relative}')
    return path

def load() -> tuple[dict[str, Any], list[dict[str, Any]]]:
    registry_path = SKILL_ROOT / 'references' / 'source-registry.json'
    registry = json.loads(registry_path.read_text(encoding='utf-8'))
    pages = []
    pattern = re.compile(r'^## PDF PAGE (\d+)\n(.*?)(?=^## PDF PAGE |\Z)', re.M | re.S)
    for book in registry['books']:
        for block in book['blocks']:
            content = checked_path(block['path']).read_text(encoding='utf-8')
            for match in pattern.finditer(content):
                number = int(match.group(1))
                source = re.search(r'```text\n(.*?)\n```', match.group(2), re.S)
                if source is None:
                    raise ValueError(f'Missing source block: {book["id"]} page {number}')
                pages.append({'book_id': book['id'], 'book': book['title'], 'pdf_page': number,
                              'reference_path': block['path'], 'text': source.group(1),
                              'warnings': book.get('page_warnings', {}).get(str(number), []),
                              'page_image': book.get('visual_pages', {}).get(str(number))})
    return registry, pages

def read_pages(pages: list[dict[str, Any]], book: str, page: int, context: int) -> list[dict[str, Any]]:
    if not any(p['book_id'] == book and p['pdf_page'] == page for p in pages):
        raise ValueError(f'No page {page} in book {book}.')
    return [p for p in pages if p['book_id'] == book and page - context <= p['pdf_page'] <= page + context]

def search(pages: list[dict[str, Any]], query: str, limit: int, book: str | None) -> list[dict[str, Any]]:
    original_terms = terms(query)
    if not original_terms:
        raise ValueError('Use at least one meaningful search term.')
    weights = {term: 1.0 for term in original_terms}
    for term in original_terms:
        for alias in ALIASES.get(term, []):
            weights.setdefault(alias, 0.35)
    candidates = [p for p in pages if book is None or p['book_id'] == book]
    token_lists = [terms(p['text']) for p in candidates]
    counters = [Counter(tokens) for tokens in token_lists]
    n = len(candidates)
    avg_len = sum(map(len, token_lists)) / max(n, 1)
    frequencies = {term: sum(term in c for c in counters) for term in weights}
    results = []
    for page, tokens, counter in zip(candidates, token_lists, counters):
        score = 0.0
        for term, weight in weights.items():
            tf = counter.get(term, 0)
            if not tf:
                continue
            df = frequencies[term]
            idf = math.log(1 + (n - df + 0.5) / (df + 0.5))
            score += weight * idf * tf * 2.2 / (tf + 1.2 * (0.25 + 0.75 * len(tokens) / max(avg_len, 1)))
        if not score:
            continue
        lines = page['text'].splitlines()
        best_line = max(range(len(lines)), key=lambda i: len(set(terms(lines[i])) & set(weights)), default=0)
        snippet = '\n'.join(lines[max(0, best_line - 1): best_line + 5])
        result = {k: v for k, v in page.items() if k != 'text'}
        result.update({'score': round(score, 4), 'snippet': snippet,
                       'next_step': f'read {page["book_id"]} {page["pdf_page"]} --context 1'})
        results.append(result)
    return sorted(results, key=lambda r: (-r['score'], r['book_id'], r['pdf_page']))[:limit]

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    s = sub.add_parser('search', help='Keyword retrieval; read full pages before answering.')
    s.add_argument('query'); s.add_argument('--book', choices=['hajj', 'women', 'worship', 'jme', 'west'])
    s.add_argument('--limit', type=int, default=6)
    r = sub.add_parser('read', help='Read a full physical PDF page and its neighbors.')
    r.add_argument('book', choices=['hajj', 'women', 'worship', 'jme', 'west']); r.add_argument('page', type=int)
    r.add_argument('--context', type=int, choices=range(0, 4), default=1)
    n = sub.add_parser('rule', help='Find an exact Rule or Issue label, then return neighboring pages.')
    n.add_argument('book', choices=['hajj', 'worship']); n.add_argument('number', type=int)
    args = parser.parse_args()
    try:
        registry, pages = load()
        if args.command == 'search':
            if not 1 <= args.limit <= 20:
                raise ValueError('--limit must be between 1 and 20.')
            results = search(pages, args.query, args.limit, args.book)
        elif args.command == 'read':
            results = read_pages(pages, args.book, args.page, args.context)
        else:
            if args.number < 1:
                raise ValueError('The source number must be positive.')
            book = next(b for b in registry['books'] if b['id'] == args.book)
            label = book['source_number_label']
            pattern = re.compile(r'^[ \t]*' + label.casefold() + r'\s+' + str(args.number) + r'\s*:', re.M)
            hits = [p for p in pages if p['book_id'] == args.book and pattern.search(normalize(p['text']))]
            seen = set(); results = []
            for hit in hits:
                for p in read_pages(pages, args.book, hit['pdf_page'], 1):
                    key = (p['book_id'], p['pdf_page'])
                    if key not in seen:
                        results.append(p); seen.add(key)
        # Escaping non-ASCII preserves source characters without terminal encoding problems.
        print(json.dumps({'retrieval_type': 'local_keyword_and_page_lookup', 'results': results,
                          'notice': 'Read all continuations and applicable footnotes. Empty results do not prove corpus absence.'},
                         ensure_ascii=True, indent=2))
        return 0
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        print(json.dumps({'error': str(exc)}, ensure_ascii=True), file=sys.stderr)
        return 2

if __name__ == '__main__':
    raise SystemExit(main())
