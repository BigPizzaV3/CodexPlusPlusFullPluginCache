---
name: site-status
description: Check whether one or more websites are up right now with a live request from the edge network: HTTP status, redirect chain, response time, TLS, page title, security-header grade, robots.txt and sitemap, plus a CSV download.
---

# Zovo Website Status Checker

Use `check_websites` when the user asks "is it down", "is this website down", "check if site is up", "website status", or wants an HTTP status or redirect chain for one or more addresses.

1. Collect every domain or http(s) address in the request and pass them together as `urls` (1 to 10). If the request already names the sites, call the tool right away; do not ask a question first.
2. A bare domain defaults to `https://`. A bare `host:port`, such as `example.com:80`, uses `http://`; give an explicit `https://` address to request HTTPS. IP literals, private/reserved addresses, local names and ports other than 80 and 443 are refused with a plain explanation.
3. After the tool returns, give the plain verdict for each site (up, down, blocked, page not found, redirects to ...), the final HTTP status and its meaning, the time, whether HTTPS was used, and the security grade. Mention any site that is down, blocked, or missing important headers.
4. A zovo.one domain or subdomain returns "Cannot check" because the checker runs inside the same network. Explain that the user must use another checker; count it as neither up nor down.
5. Share the CSV link when the user wants the full list of columns.

Use `check_security_headers` when the user asks specifically for a security-headers check of one site: it reports the six key headers present or missing with an A-F grade.

Do not use this skill for monitoring, uptime history, or checking private or internal addresses, and do not promise that a site will stay up.
