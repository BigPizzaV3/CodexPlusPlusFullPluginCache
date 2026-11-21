#!/usr/bin/env python3
"""Return dictionary candidates. Does not translate text, write files, or use a network."""
import argparse
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TERM_ROOT = ROOT/'resources/terminology'
MAX_TERMS = 20
MAX_TERM_CHARS = 160
MAX_CANDIDATES_PER_TERM = 5
MAX_RETURNED_RECORDS = 40

def normalize(value):
    value = unicodedata.normalize('NFKC', value)
    return re.sub(r'\s+', ' ', re.sub('[‐‑–—-]', ' ', value)).strip()

def protected_case(value, forms):
    return value.casefold() in {form.casefold() for form in forms}

def safe_file(relative):
    target = (TERM_ROOT/relative).resolve()
    if TERM_ROOT.resolve() not in target.parents:
        raise ValueError('Dictionary path must stay within the packaged terminology directory.')
    return target

def lookup(terms, direction, include_reference=False, limit=5):
    # These local bounds reduce accidental bulk output. They are not file access control.
    if direction not in ('en-ja', 'ja-en'):
        raise ValueError('Unsupported lookup direction.')
    if not isinstance(terms, (list, tuple)) or not 1 <= len(terms) <= MAX_TERMS:
        raise ValueError('Use between 1 and 20 actual terms from the requested text.')
    if type(limit) is not int or not 1 <= limit <= MAX_CANDIDATES_PER_TERM:
        raise ValueError('Candidate limit must be between 1 and 5.')
    for term in terms:
        if not isinstance(term, str) or not term.strip() or len(term) > MAX_TERM_CHARS or re.search(r'[\x00-\x1f\x7f]', term):
            raise ValueError('Each term must be a nonempty string of at most 160 characters without control characters.')
    index_name = 'en-index.json' if direction == 'en-ja' else 'ja-index.json'
    index = json.loads((TERM_ROOT/index_name).read_text(encoding='utf-8'))
    requested = []
    remaining = MAX_RETURNED_RECORDS
    for term in terms:
        normalized = normalize(term)
        matches = list(index['exact'].get(normalized, []))
        if direction == 'en-ja' and not protected_case(normalized, index.get('caseSensitiveForms', [])):
            matches.extend(index['casefold'].get(normalized.casefold(), []))
        seen = set()
        selected = []
        for item in matches:
            if item['tier'] == 'reference' and not include_reference:
                continue
            if item['id'] in seen:
                continue
            seen.add(item['id'])
            selected.append(item)
        selected.sort(key=lambda item: (item['tier'] != 'basic', item['id']))
        selected_limit = min(limit, remaining)
        chosen = selected[:selected_limit]
        remaining -= len(chosen)
        requested.append({'query':term, 'candidateCount':len(selected), 'matches':chosen,
                          'truncated':len(selected)>len(chosen)})
    needed = {}
    for item in requested:
        for match in item['matches']:
            needed.setdefault(match['path'], set()).add(match['line'])
    records = {}
    for relative, numbers in needed.items():
        with safe_file(relative).open(encoding='utf-8') as source:
            for number, line in enumerate(source, 1):
                if number in numbers:
                    record = json.loads(line)
                    records[record['id']] = record
    results = []
    for item in requested:
        candidates = []
        for match in item['matches']:
            record = records.get(match['id'])
            if record is None:
                raise ValueError('Index and dictionary record disagree: '+match['id'])
            candidates.append({'matchKind':match['matchKind'], 'record':record})
        results.append({key:value for key,value in item.items() if key != 'matches'} | {'candidates':candidates})
    return {
        'direction':direction, 'includeReference':include_reference,
        'selectionRequired':True, 'automaticReplacement':False,
        'limits':{'maxTerms':MAX_TERMS,'maxTermChars':MAX_TERM_CHARS,
                  'maxCandidatesPerTerm':MAX_CANDIDATES_PER_TERM,'maxReturnedRecords':MAX_RETURNED_RECORDS},
        'returnedRecordCount':MAX_RETURNED_RECORDS-remaining,
        'notice':'候補は確定訳ではありません。原文の意味・対象・定義・条件から選び、曖昧さを自動で解消しないでください。',
        'results':results,
    }

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--direction', required=True, choices=['en-ja', 'ja-en'])
    parser.add_argument('--terms', required=True, nargs='+')
    parser.add_argument('--include-reference', action='store_true')
    parser.add_argument('--limit', type=int, default=5)
    options = parser.parse_args()
    try:
        result = lookup(options.terms, options.direction, options.include_reference, options.limit)
    except ValueError as error:
        parser.error(str(error))
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
