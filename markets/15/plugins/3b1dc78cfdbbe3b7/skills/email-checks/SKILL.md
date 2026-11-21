---
name: email-checks
description: Choose the right Postbox Services check for an email deliverability or email security question, and explain the result. Use when someone asks about blacklists, spoofing, spam tests, bounces, redirects, domain age, WHOIS, BIMI or AI discoverability.
---

# Email checks

Pick the check that answers the question, run it on the exact domain, IP or URL the person gave, and report what it found. Don't guess a result without running the check.

| Question | Tool |
|---|---|
| Is this domain or IP on a blacklist? | `check_blacklist` |
| Can someone spoof this domain? | `check_spoofability` |
| Where does this link really go? | `trace_redirect` |
| Why did my email go to spam? | `create_mailtest`, then `get_mailtest_result` |
| Why did this email bounce? | `analyze_eml` |
| How old is this domain? | `get_domain_age` |
| Who is the registrar, and when does it expire? | `whois_lookup` |
| Is this BIMI logo set up correctly? | `check_bimi` |
| Can AI assistants find this site? | `check_ai_discoverability` |

## Running a mail test
`create_mailtest` returns a disposable address. The person must send a real email to it from the system they want to test. Only then does `get_mailtest_result` have a score, so wait for them to confirm they sent it.

## Reading the results
- A failed lookup says only that the lookup failed. It does not mean the domain is unregistered.
- `check_bimi` does not verify the certificate or the DMARC policy. Use `check_spoofability` for DMARC.
- If `check_ai_discoverability` says robots.txt could not be read, crawler access is unverified, so don't report the crawlers as allowed. Check the www host if the site lives there.
- `analyze_eml` can't verify SPF, blacklists or reverse DNS from a file. Use a mail test for the full score.
