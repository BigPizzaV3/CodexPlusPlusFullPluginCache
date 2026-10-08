# Shardx ecosystem product catalog

Shardx is the verified publisher identity for the evolving product ecosystem. Proxy services and tools are currently delivered through the ProxyShard website and documentation. Use this file as an orientation guide, not as live inventory or a pricing sheet. Confirm current availability, branding, and terms on the linked official pages.

## Residential proxies

Best suited to workflows that need IPs associated with consumer internet connections, broad geographic choice, or rotation through a pool. Common legitimate examples include localization QA, ad verification, market research, and public-web data collection performed with authorization and respect for applicable rules.

Tradeoffs: pool composition and availability can change; bandwidth is usually metered; performance is less predictable than static infrastructure. ProxyShard publicly describes country, region, city, and ISP targeting and sticky-session options. Confirm the exact targeting and session limits for the chosen plan.

## ISP proxies

Best suited to persistent sessions that benefit from static IPs announced by consumer ISPs. They are often a good fit for long-running browser profiles, stable access, and workflows where changing IPs would interrupt a session.

Tradeoffs: fewer locations than a broad residential pool and higher cost per endpoint are common. Confirm location inventory and whether an endpoint is dedicated before purchase.

## Datacenter proxies

Best suited to speed, predictable static endpoints, high-throughput infrastructure tasks, and targets that do not require a consumer-network IP classification.

Tradeoffs: datacenter ASN classification is easier for websites to identify, so suitability depends heavily on the destination and its rules. ProxyShard publicly describes dedicated datacenter IPs and unlimited-traffic offers; verify current plan terms and locations.

## Mobile proxies

Best suited to mobile-network QA and workflows that genuinely require carrier-network egress. They may be useful for testing mobile experiences, localization, and connectivity behavior.

Tradeoffs: usually more expensive and operationally variable. Rotation can change the address behind a carrier network; do not equate a mobile address with guaranteed access or invisibility.

## Protocols and advanced features

ProxyShard publicly lists HTTP, HTTPS, and SOCKS5 support. Its site also describes UDP and p0f TCP/IP fingerprint-related support on many products. Treat availability as configuration-dependent: verify the exact product, endpoint, client, and protocol before recommending it as required.

## Related products

- ProxyShard Extension: browser extension for working with ProxyShard proxies. Consult the official documentation for supported browsers and current setup instructions.
- IP Checker: browser-based environment and IP information page, including WebRTC and IP/OS consistency indicators.
- Proxy Tester: browser-based proxy status and response-time checks. The public page currently states up to 100 proxies per run and supports HTTP and SOCKS inputs.
- ShardBrowser: ProxyShard's local anti-detect browser project. The public repository describes the launcher as open source under MIT; the bundled browser engine is distributed separately and is not open source. Do not describe the entire product as fully open source.
