#!/usr/bin/env python3
"""Read-only TfL requests. Python 3 and curl; optional TFL_APP_KEY."""
import argparse
import datetime as dt
import json
import os
import sys
import urllib.parse
import subprocess

BASE = 'https://api.tfl.gov.uk'

def request(path, params=None):
    params = dict(params or {})
    source = BASE + path + ('?' + urllib.parse.urlencode(params) if params else '')
    if os.environ.get('TFL_APP_KEY'):
        params['app_key'] = os.environ['TFL_APP_KEY']
    url = BASE + path + ('?' + urllib.parse.urlencode(params) if params else '')
    result = {'source': source, 'retrieved_at_utc': dt.datetime.now(dt.timezone.utc).isoformat()}
    try:
        # Send the URL through stdin so optional credentials are not in process arguments.
        config = 'url = "' + url.replace('\\', '\\\\').replace('"', '\\"') + '"\n'
        response = subprocess.run(
            ['curl', '--silent', '--show-error', '--max-time', '30',
             '--header', 'Accept: application/json', '--write-out', '\n%{http_code}',
             '--config', '-'], input=config, capture_output=True, text=True, timeout=35)
        if response.returncode:
            result['curl_exit_code'] = response.returncode
            result['error_kind'] = 'network' if response.returncode in (5, 6, 7, 28, 35, 60) else 'transport'
            result['error'] = 'Request did not reach a usable TfL response; live status is unknown.'
            result['next_step'] = ('If running in a network-restricted sandbox, retry this command once through the host network approval flow. '
                                   'Do not change sandbox settings or infer that an API key is required. If denied, stop and report the restriction.')
            return result
        body, status = response.stdout.rsplit('\n', 1)
        result['http_status'] = int(status)
        if int(status) in (200, 300):
            result['data'] = json.loads(body)
            if int(status) == 300:
                result['needs_disambiguation'] = True
        else:
            result['error_kind'] = {401: 'authentication', 403: 'access_denied', 429: 'rate_limit'}.get(int(status), 'http')
            result['error'] = 'TfL request failed; live status is unknown. Check service availability or API credentials.'
    except FileNotFoundError:
        result.update(error_kind='missing_dependency', error='curl is not installed or not on PATH; live status is unknown.')
    except subprocess.TimeoutExpired:
        result.update(error_kind='network', error='TfL request timed out; live status is unknown.')
    except ValueError:
        result.update(error_kind='invalid_response', error='TfL returned an invalid response; live status is unknown.')
    except (subprocess.SubprocessError, OSError):
        result.update(error_kind='execution', error='Unable to execute the HTTP client; live status is unknown.')
    return result

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    search = commands.add_parser('search')
    search.add_argument('query')
    journey = commands.add_parser('journey')
    journey.add_argument('origin')
    journey.add_argument('destination')
    journey.add_argument('--access', choices=['none', 'platform', 'vehicle'], default='none')
    journey.add_argument('--date', help='London local date YYYYMMDD')
    journey.add_argument('--time', help='London local time HHmm')
    journey.add_argument('--arrive-by', action='store_true')
    journey.add_argument('--bus-only', action='store_true')
    journey.add_argument('--max-walking-minutes', type=int)
    for command in ['arrivals', 'station', 'disruptions']:
        commands.add_parser(command).add_argument('stop_id')
    commands.add_parser('lifts')
    args = parser.parse_args()
    params = {}
    quote = lambda value: urllib.parse.quote(value, safe='')
    if args.command == 'search':
        path, params = '/StopPoint/Search', {'query': args.query, 'includeHubs': 'true'}
    elif args.command == 'journey':
        path = '/Journey/JourneyResults/' + quote(args.origin) + '/to/' + quote(args.destination)
        params = {'useRealTimeLiveArrivals': 'true', 'routeBetweenEntrances': 'true',
                  'timeIs': 'arriving' if args.arrive_by else 'departing'}
        if args.access != 'none':
            params['accessibilityPreference'] = {'platform': 'stepFreeToPlatform', 'vehicle': 'stepFreeToVehicle'}[args.access]
        for key in ['date', 'time']:
            if getattr(args, key):
                params[key] = getattr(args, key)
        if args.bus_only:
            params['mode'] = 'bus'
        if args.max_walking_minutes is not None:
            if args.max_walking_minutes < 0:
                parser.error('--max-walking-minutes must be nonnegative')
            params['maxWalkingMinutes'] = args.max_walking_minutes
    elif args.command == 'lifts':
        path = '/Disruptions/Lifts/v2'
    else:
        suffix = {'arrivals': '/Arrivals', 'station': '', 'disruptions': '/Disruption'}[args.command]
        path = '/StopPoint/' + quote(args.stop_id) + suffix
        if args.command == 'disruptions':
            params['getFamily'] = 'true'
    result = request(path, params)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if 'error' in result else 0

if __name__ == '__main__':
    sys.exit(main())
