# Crawler access for AI bots

Technical preconditions so that GPTBot, ClaudeBot, and other AI crawlers can see
the content at all. This is the gate: if it fails, nothing downstream works.

## The core problem

AI crawlers such as GPTBot and ClaudeBot are technically simpler than Googlebot.
They usually read only the initial server HTML response and do not execute
JavaScript. Content rendered client-side does not exist for these bots.

## Requirements

1. **No client-side rendering for core content.** All relevant text, images, and
   links must be in the first server HTML response, via server-side rendering or
   static rendering. This is the single most critical factor.

2. **Explicit allowance in robots.txt.** Allow AI bots by name. The llms.txt
   convention is still experimental; robots.txt remains the binding control.

3. **Check firewall and CDN.** Server firewalls and CDN rules sometimes block AI
   crawler IPs by accident. Verify against the access logs regularly.

4. **Clean status codes.** Fix 4xx errors, prioritize 5xx errors because they can
   stop crawling of the whole domain. AI bots usually do not follow internal 301
   redirects, so every internal link must point straight at the final URL.

## Placement in the workflow

These are preconditions, not optimizations. If they are violated, neither
chunking nor citation-worthiness helps, because the content never reaches the
models. Verified sources for crawler behavior: OpenAI's crawler documentation at
platform.openai.com/docs/bots.
