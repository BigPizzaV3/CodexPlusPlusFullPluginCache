#!/usr/bin/env python3
"""Fetch individual sign metadata from the original, unauthenticated Zakros API."""
import argparse
import json
import re
import socket
from urllib import error, parse, request

ENDPOINT = 'https://zakros-api.vercel.app/api/glyphs'
NOT_FOUND = ('This glyph is not found in the attached Zakros Glyph API. This may mean it is '
             'unattested, malformed, or absent from the API dataset. Check SigLA/GORILA before drawing conclusions.')


class NoRedirect(request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def lookup(code, opener=None):
    code = re.sub(r'\s+', '', code).upper()
    if not re.fullmatch(r'[A-Z]{1,4}[0-9]{1,4}[A-Z]?', code):
        return {'status': 'INVALID_CODE', 'message': 'Supply one sign code such as AB60.'}
    url = ENDPOINT + '?' + parse.urlencode({'code': code})
    opener = opener or request.build_opener(NoRedirect())
    try:
        with opener.open(request.Request(url, headers={'Accept': 'application/json'}), timeout=20) as response:
            raw = response.read(1024 * 1024 + 1)
            if len(raw) > 1024 * 1024:
                raise ValueError('API response exceeds the 1 MiB limit')
            data = json.loads(raw)
        if not isinstance(data, dict):
            raise ValueError('API response is not an object')
        expected = {'glyph': str, 'phonetic': str, 'tablets': list, 'site': str, 'context': str, 'image_urls': list}
        for key, typ in expected.items():
            if not isinstance(data.get(key), typ):
                raise ValueError('API response has a missing or invalid ' + key)
        for key in ('tablets', 'image_urls'):
            if any(not isinstance(item, str) for item in data[key]):
                raise ValueError('API response has invalid list items in ' + key)
        return {'status': 'FOUND', 'endpoint': ENDPOINT, 'code': code, 'metadata': data,
                'missing_optional_fields': [k for k in ('source_version', 'confidence', 'notes') if k not in data],
                'limitation': 'API metadata only; not a translation, parser output or verified attestation. Check SigLA/GORILA.'}
    except error.HTTPError as exc:
        if exc.code == 404:
            return {'status': 'NOT_FOUND_IN_API', 'http_status': 404, 'code': code, 'message': NOT_FOUND}
        return {'status': 'LOOKUP_FAILED', 'http_status': exc.code, 'code': code, 'message': 'API HTTP error; no conclusion about attestation.'}
    except (error.URLError, socket.timeout, OSError, ValueError) as exc:
        return {'status': 'LOOKUP_FAILED', 'code': code, 'message': 'API lookup failed; no conclusion about attestation.', 'error_type': type(exc).__name__}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('code')
    result = lookup(parser.parse_args().code)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result['status'] in ('FOUND', 'NOT_FOUND_IN_API') else 1


if __name__ == '__main__':
    raise SystemExit(main())
