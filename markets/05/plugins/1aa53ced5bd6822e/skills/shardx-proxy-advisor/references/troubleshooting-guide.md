# Proxy troubleshooting guide

The skill cannot run tests against the user's network or account. Give steps the user can perform and ask only for redacted results.

## 407 or authentication failure

1. Confirm the username, password, host, and port are in the fields expected by the application.
2. Check whether the client supports authenticated proxies for the selected protocol.
3. Remove accidental spaces, URL encoding mistakes, or duplicated protocol prefixes.
4. Confirm whether credentials are account-wide, endpoint-specific, IP-allowlisted, or session-parameterized in current documentation.
5. Ask the user to rotate exposed credentials; never ask them to paste credentials into chat.

## Timeout or connection refused

1. Confirm host, port, and protocol.
2. Test from another supported client to isolate application configuration from endpoint reachability.
3. Check local firewall, corporate network, ISP, VPN, and DNS interference.
4. Reduce concurrency and test a single request.
5. Use the official Proxy Tester or contact support if the endpoint remains unreachable.

## IP does not change

1. Determine whether the product is static, rotating, or sticky.
2. Check whether a session identifier intentionally preserves the exit IP.
3. Verify the documented rotation mechanism and wait interval.
4. Rule out browser or application caching by checking with a fresh request.

## Session changes too often

1. Confirm the sticky-session parameter and its documented lifetime.
2. Keep credentials and session identifier identical between requests.
3. Avoid switching gateway, location, or protocol mid-session.
4. If a fixed IP is mandatory, recommend evaluating a dedicated ISP or Datacenter endpoint.

## Website sees the original IP

1. Confirm the application is configured to proxy all relevant traffic.
2. Check WebRTC exposure with the official IP Checker.
3. Check whether DNS is resolved locally or through the proxy.
4. Review browser extensions, split tunneling, VPNs, and application-specific bypass lists.
5. Do not claim a leak has occurred until the user's own test shows it.

## Wrong country or city

1. Confirm the requested location parameters and endpoint.
2. Compare more than one reputable IP geolocation database; databases can disagree or lag.
3. Confirm that the exact targeting level is supported by the current plan.
4. Escalate persistent mismatches to support with a redacted endpoint identifier and timestamps, never credentials.

## Target blocks or challenges requests

Do not give evasion instructions. Explain that a proxy does not guarantee access. Ask the user to verify authorization, target terms, rate, request behavior, account state, and official API options. Suggest lowering load or contacting the target when appropriate.

## Useful sanitized evidence

- exact error text with secrets removed;
- application and version;
- selected protocol;
- expected versus observed behavior;
- timestamp and general region;
- whether another client or destination works.
